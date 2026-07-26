#!/usr/bin/env python
"""Convert daily research markdown to styled HTML matching the site template."""
import sys
import re
from html import escape

def md_to_html(md_path, output_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract date from title
    date_match = re.search(r'# Daily YouTube Strategy Research — (\d{4}-\d{2}-\d{2})', content)
    date_str = date_match.group(1) if date_match else "Unknown"

    lines = content.split('\n')
    html_lines = []
    in_table = False
    in_list = False
    table_headers = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip the H1 title (we add it in the template)
        if line.startswith('# Daily YouTube Strategy Research'):
            i += 1
            continue

        # Convert headers
        if line.startswith('### '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                html_lines.append('</tbody></table>')
                in_table = False
            html_lines.append(f'<h3>{inline_format(line[4:])}</h3>')
        elif line.startswith('## '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                html_lines.append('</tbody></table>')
                in_table = False
            html_lines.append(f'<h2>{inline_format(line[3:])}</h2>')
        elif line.startswith('---'):
            if in_table:
                html_lines.append('</tbody></table>')
                in_table = False
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
                if i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i+1]):
                    html_lines.append('<table class="data-table"><thead><tr>')
                    html_lines.append(''.join(f'<th>{escape(c)}</th>' for c in cells))
                    html_lines.append('</tr></thead><tbody>')
                    in_table = True
                    table_headers = cells
                    i += 2
                    continue
            if in_table:
                html_lines.append('<tr>')
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
                html_lines.append('</tbody></table>')
                in_table = False
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                html_lines.append('</tbody></table>')
                in_table = False
            html_lines.append(f'<p>{inline_format(line)}</p>')

        i += 1

    if in_list:
        html_lines.append('</ul>')
    if in_table:
        html_lines.append('</tbody></table>')

    body_content = '\n'.join(html_lines)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Research — {date_str}</title>
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
        <h1>Daily YouTube Strategy Research — {date_str}</h1>

{body_content}

        <p class="footer">Generated by OpenClaw · {date_str}</p>
    </div>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML written to {output_path}")


def inline_format(text):
    """Convert inline markdown formatting to HTML."""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{escape(m.group(1))}</code>', text)
    # Escape HTML entities in remaining text (but not our tags)
    # Be careful not to double-escape
    return text


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: md-to-research-html.py <input.md> <output.html>")
        sys.exit(1)
    md_to_html(sys.argv[1], sys.argv[2])
