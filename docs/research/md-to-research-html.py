#!/usr/bin/env python
"""Convert research markdown to styled HTML matching the site template.

v2 (2026-09-12): heading anchor ids ({#custom-id} override or auto-slug),
in-heading link anchors, [text](url) markdown links, bare-URL autolinking,
and per-family document titles (Playlist vs Daily research).
"""
import sys
import os
import re
from html import escape


def make_anchor_id(text, used):
    base = re.sub(r'[^\w\s-]', '', text.lower())
    base = re.sub(r'[\s]+', '-', base.strip())
    base = re.sub(r'-{2,}', '-', base).strip('-') or 'section'
    id_ = base
    n = 2
    while id_ in used:
        id_ = f"{base}-{n}"
        n += 1
    used.add(id_)
    return id_


def inline_format(text):
    """Convert inline markdown formatting to HTML."""
    # Markdown links [text](url-or-anchor)
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)',
                  r'<a href="\2">\1</a>', text)
    # Bare URLs (not already inside an attribute/tag)
    text = re.sub(r'(?<!["\'=>])(https?://[^\s<>)\]"`]+)',
                  r'<a href="\1">\1</a>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italics *(...)* or *(...)*
    text = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{escape(m.group(1))}</code>', text)
    return text


def md_to_html(md_path, output_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract date from any H1
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', content)
    date_str = date_match.group(1) if date_match else "Unknown"

    base = os.path.basename(md_path)
    is_playlist = base.startswith('playlist')
    if is_playlist:
        doc_title = f"Playlist Research — {date_str}"
    else:
        doc_title = f"Daily YouTube Strategy Research — {date_str}"

    used_ids = set()
    lines = content.split('\n')

    # Standalone docs (playbooks/kits: not daily-research_*, not playlist-research_*)
    # keep their own H1 title — the synthesized "Daily YouTube Strategy Research"
    # heading only fits the daily reports. Daily/playlist behavior unchanged.
    if not is_playlist and not base.startswith('daily-research_'):
        m_h1 = re.search(r'^#\s+(.+?)\s*$', content, re.MULTILINE)
        if m_h1:
            doc_title = m_h1.group(1).strip()

    # TOC pre-pass (daily reports): "Jump to a section" nav under the H1.
    # Mirrors the main pass anchor algorithm so links land on the same ids.
    toc_entries = []
    if not is_playlist:
        used_pre = set()
        for raw in lines:
            hm = re.match(r'^(#{2,4}) (.*)$', raw.strip())
            if not hm:
                continue
            text = hm.group(2).strip()
            cm = re.match(r'^(.*?)\s*\{#([\w-]+)\}\s*$', text)
            if cm:
                text, anchor = cm.group(1), cm.group(2)
                used_pre.add(anchor)
            else:
                anchor = make_anchor_id(text, used_pre)
            if re.match(r'^Videos Analyzed', text):
                anchor = 'videos'
                used_pre.add(anchor)
            label = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
            toc_entries.append((len(hm.group(1)), label, anchor))
    toc_html = ''
    if toc_entries:
        toc_html = ('<nav class="toc"><div class="toc-title">Jump to a section:</div><ul>'
                    + ''.join(f'<li class="toc-h{lvl}"><a href="#{anc}">{escape(label)}</a></li>'
                              for lvl, label, anc in toc_entries)
                    + '</ul></nav>')
    toc_placed = [False]
    html_lines = []
    in_table = False
    in_list = False

    def close_table():
        # Close an open table; the daily-report TOC is injected directly
        # after the FIRST table (Videos Analyzed) closes, per Mike's layout:
        # H1 -> subtitle -> table -> Jump-to TOC -> sections.
        nonlocal in_table
        html_lines.append('</tbody></table>')
        in_table = False
        if toc_html and not toc_placed[0]:
            html_lines.append(toc_html)
            toc_placed[0] = True

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip the H1 title (we add it in the template)
        if line.startswith('# '):
            i += 1
            continue

        # Convert headers (with anchor ids)
        hm = re.match(r'^(#{2,4}) (.*)$', line)
        if hm:
            level = len(hm.group(1))
            text = hm.group(2).strip()
            cm = re.match(r'^(.*?)\s*\{#([\w-]+)\}\s*$', text)
            if cm:
                text, anchor = cm.group(1), cm.group(2)
                used_ids.add(anchor)
            else:
                anchor = make_anchor_id(text, used_ids)
            # Stable id for the table-of-contents heading
            if re.match(r'^Videos Analyzed', text):
                anchor = 'videos'
                used_ids.add(anchor)
            # Heading affordances: daily reports get "↑ Index" on per-video
            # headings (their own TOC row if tagged, else the table) plus
            # "↑ top" on every h2/h3 (returns to the H1 + Jump-to TOC).
            # Playlists keep only the row back-link — build-research-nav
            # injects its own prev/next nav on playlist pages.
            to_top = ''
            toc_back = ''
            vm = re.match(r'^Video (\d+):', text)
            if not vm and not is_playlist and re.match(r'^\d+[.)]\s', text):
                # Dailies: numbered headings are videos, back-link to the
                # table. Standalone docs (no Videos Analyzed section):
                # back-link to #top — '#videos' would be a dead anchor.
                if 'videos' in used_ids:
                    toc_back = ('<a class="toc-back" href="#videos" '
                                'aria-label="Back to video index">&uarr; Index</a>')
                else:
                    toc_back = ('<a class="toc-back" href="#top" '
                                'aria-label="Back to index">&uarr; Index</a>')
            if vm:
                rid = f'row-video-{vm.group(1)}'
                target = rid if rid in used_ids else 'videos'
                toc_back = (f'<a class="toc-back" href="#{target}" '
                            f'aria-label="Back to video index">&uarr; Index</a>')
            if not is_playlist:
                to_top = '<span class="toTop"><a href="#top">&#8593; top</a></span>'
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                close_table()
            html_lines.append(
                f'<h{level} id="{anchor}">{inline_format(text)}'
                f'<a class="anchor" href="#{anchor}" aria-label="Link to this section">#</a>'
                f'{toc_back}'
                f'{to_top}'
                f'</h{level}>')
        elif line.startswith('---'):
            if in_table:
                close_table()
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<hr>')
        elif line.startswith('|') and '|' in line[1:]:
            # Table handling
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if all(re.match(r'^[-:]+$', c) for c in cells):
                i += 1
                continue  # skip separator row
            if not in_table:
                # Check if next line is separator
                if i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1]):
                    html_lines.append('<table class="data-table"><thead><tr>')
                    html_lines.append(''.join(f'<th>{escape(c)}</th>' for c in cells))
                    html_lines.append('</tr></thead><tbody>')
                    in_table = True
                    i += 2
                    continue
            if in_table:
                # Tag TOC rows with a row anchor so per-video back-links can
                # return positioned on that story's link
                row_open = '<tr>'
                rm = re.search(r'\]\(#(video-\d+)\)', line)
                if rm:
                    rid = f'row-{rm.group(1)}'
                    if rid not in used_ids:
                        used_ids.add(rid)
                        row_open = f'<tr id="{rid}">'
                html_lines.append(row_open)
                for c in cells:
                    html_lines.append(f'<td>{inline_format(c)}</td>')
                html_lines.append('</tr>')
        elif re.match(r'^[-*] ', line):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{inline_format(line[2:])}</li>')
        elif line.strip() == '':
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                close_table()
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                close_table()
            html_lines.append(f'<p>{inline_format(line)}</p>')

        i += 1

    if in_list:
        html_lines.append('</ul>')
    if in_table:
        close_table()
    # Fallback: no table in the doc -> TOC goes at the end of the header area
    if toc_html and not toc_placed[0]:
        html_lines.append(toc_html)

    body_content = '\n'.join(html_lines)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(doc_title)}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #2d1b69 100%);
            min-height: 100vh;
            padding: 40px 20px;
            color: #e0e0e0;
            line-height: 1.7;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        h1 {{
            font-size: 2em;
            margin-bottom: 8px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        h2 {{
            font-size: 1.4em;
            margin-top: 40px;
            margin-bottom: 16px;
            color: #a78bfa;
            border-bottom: 1px solid rgba(167,139,250,0.2);
            padding-bottom: 8px;
        }}
        h3 {{
            font-size: 1.15em;
            margin-top: 28px;
            margin-bottom: 12px;
            color: #c4b5fd;
        }}
        h2, h3 {{ position: relative; }}
        h2 .anchor, h3 .anchor {{
            opacity: 0;
            margin-left: 8px;
            font-size: 0.7em;
            text-decoration: none;
            -webkit-text-fill-color: #667eea;
        }}
        h2:hover .anchor, h3:hover .anchor {{ opacity: 0.75; }}
        h2 .anchor:hover, h3 .anchor:hover {{ opacity: 1; text-decoration: underline; }}
        h2 .toc-back, h3 .toc-back {{
            float: right;
            font-size: 0.62em;
            font-weight: 400;
            opacity: 0.55;
            text-decoration: none;
            -webkit-text-fill-color: #667eea;
            margin-left: 10px;
            white-space: nowrap;
        }}
        h2 .toc-back:hover, h3 .toc-back:hover {{ opacity: 1; text-decoration: underline; }}
        .toc {{
            background: rgba(102,126,234,0.08);
            border: 1px solid rgba(102,126,234,0.25);
            border-radius: 10px;
            padding: 16px 20px;
            margin: 20px 0 8px;
        }}
        .toc-title {{
            color: #a78bfa;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        .toc ul {{ list-style: none; margin: 0; padding: 0; }}
        .toc li {{ margin: 4px 0; }}
        .toc-h2 {{ font-weight: 600; }}
        .toc-h3 {{ padding-left: 18px; font-size: 0.95em; }}
        .toTop {{
            float: right;
            font-size: 0.62em;
            font-weight: 400;
        }}
        .toTop a {{ color: #888; -webkit-text-fill-color: #888; }}
        p {{ margin-bottom: 14px; color: #ccc; }}
        strong {{ color: #fff; }}
        a {{ color: #667eea; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        code {{
            background: rgba(255,255,255,0.1);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.9em;
            color: #a78bfa;
        }}
        hr {{
            border: none;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin: 40px 0;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0 24px;
            font-size: 0.95em;
        }}
        .data-table th {{
            background: rgba(102,126,234,0.2);
            color: #a78bfa;
            padding: 12px 16px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid rgba(102,126,234,0.3);
        }}
        .data-table td {{
            padding: 10px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            color: #ccc;
        }}
        .data-table tr:hover td {{
            background: rgba(255,255,255,0.03);
        }}
        .data-table tr:target td {{
            background: rgba(102,126,234,0.18);
        }}
        .verdict-good {{ color: #4ade80; }}
        .verdict-warn {{ color: #fbbf24; }}
        .medal {{ font-size: 1.2em; }}
        ul {{ margin: 8px 0 16px 24px; }}
        li {{ margin-bottom: 6px; color: #ccc; }}
        .back-link {{
            display: inline-block;
            margin-bottom: 30px;
            color: #667eea;
            text-decoration: none;
            font-size: 0.9em;
        }}
        .back-link:hover {{ text-decoration: underline; }}
        .footer {{
            text-align: center;
            color: #555;
            margin-top: 50px;
            font-size: 0.85em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a class="back-link" href="../index.html">&larr; All Reports</a>
        <h1 id="top">{escape(doc_title)}</h1>

{body_content}

        <p class="footer">Generated by OpenClaw · {date_str}</p>
    </div>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML written to {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: md-to-research-html.py <input.md> <output.html>")
        sys.exit(1)
    md_to_html(sys.argv[1], sys.argv[2])
