# Playlist Research - Michael Buchanan's "Research" Playlist (2026-09-09 Run)

> **Run note:** 17 videos in the playlist — biggest batch yet. 16 new (Shane Hummus "night jobs" already covered 09-05, skipped). Full transcripts 16/16. Morning daily cron (`c57014f1`) died silently with no 09-09 daily report — playlist published first, daily recovery next.

**Videos found:** 17 · **Analyzed:** 16 · **Skipped:** 1 (already covered)

## Videos Analyzed

| # | Title | Channel | Views | Length |
|---|-------|---------|-------|--------|
| 1 | 5 GitHub Repos: Kill AI Slop, Go Viral, Make Money | Greg Isenberg | ~191K | 25 min |
| 2 | Why AI Agents Could Finally Reinvent the Credit Card | a16z | ~35K | 59 min |
| 3 | Hormozi's New YouTube Strategy Is Genius (but Dangerous) | Wes McDowell | ~8.7K | 18 min |
| 4 | I Built An Entire AI Filmmaking Team With Claude | Mira AI | ~20K | 10 min |
| 5 | Why Doesn't Everyone Play Bubble Craps Like This? | Casino Steve | ~7K | 12 min |
| 6 | If I Had to Get My Brand Cited by AI, I'd Build This Grok Bot | Jake Bauman | ~2.2K | 21 min |
| 7 | ChatGPT Images 2.5 Is Here (And It's A LOT Of Fun) | Paul J Lipsky | ~193K | 9 min |
| 8 | Forget Amazon! Shopify Just Became The Better Bet For Sellers | MyWifeQuitHerJob | ~18K | 13 min |
| 9 | TikTok Is Quietly Creating Six-Figure Publishers | Jonathan Nilsen | ~35K | 16 min |
| 10 | The NEW Way to make $ with chatgpt in 2026 | Nick Ponte | ~11K | 41 min |
| 11 | New: Your agent handles finances now | The Next New Thing | ~13K | 13 min |
| 12 | If We Had to Make $1M Fast, We'd Start These Businesses | Koerner Office | ~188K | 61 min |
| 13 | If I Had 0 Subscribers, Here's How I'd Make $1M in 12 Months | Sunny Lenarduzzi | ~89K | 28 min |
| 14 | The Simple One-Man Side Hustle That Runs Itself | Koerner Office | ~72K | 43 min |
| 15 | 8 Ways I Get Paid on YouTube (Without Millions of Views) | Glo Atanmo | ~5.8K | 48 min |
| 16 | Inside OpenClaw 2.0: Multiplayer, Dashboards, and Worker Nodes | OpenClaw | ~8.8K | 51 min |

## Run Theme

**Agent-legibility is the 2026 acquisition channel.** Across GEO/AEO bots, Shopify FAQ schema, TikTok-manufactured KDP demand, and Hormozi's "watch me work" videos, the winners aren't ranking in search — they're making themselves machine-citable and buyer-specific. Parallel thread: agent-native infrastructure (Slowbooks, OpenClaw 2.0, Higgsfield crews, agentic payments) replacing click-tools with named agents that have jobs, audit trails, and persistent rules. Best receipts of the batch are analog: Nathan's contactless trailer rentals (~$4K/mo net on 2–4 hrs/week). Worst: vendor/guru funnels with dollar figures and no dashboards.

## Video 1: Greg Isenberg — "5 GitHub Repos" *(tooling roundup)*

- **Business model:** Mine GitHub trending, install repos as agent skills, productize one working workflow (video-editing-as-a-service, mobile QA).
- **Revenue model:** none given — "$100–$500/mo QA" is hypothetical.
- **Replication steps:** (1) trending repos last 30 days; (2) `npx skills add`; (3) scan with Nvidia Skill Specter before install; (4) one small workflow per repo; (5) productize only after it works.
- **Automation:** 8/10 · **Quality:** 5/10 · **Verdict: Mixed**
- **Keep:** Skill Specter as install hygiene. Named: No-AI-Slop, trycompai CRM, browser-use Video Use, Skill Specter, Phone Harness.
- **Red flags:** intro says six repos, delivers five; zero results; heavy deps.

## Video 2: a16z — "AI Agents Could Finally Reinvent the Credit Card" *(VC thesis)*

- **Thesis:** Agentic *payments* (execute a known SKU at best terms) ≠ agentic *shopping* (robots picking your outfits). Visa/MC 2.5-second window froze card innovation; agents timeshift underwriting/fraud like Apple Pay did. Instacart already trained substitution tolerance.
- **Revenue model:** none (VC). Affirm receipts: 30–35% conversion lifts when financing is upfunnel; negative-CAC via merchant-funded MDR.
- **Small-operator plays:** CamelCamelCamel-style price-track-and-execute in underserved SKUs; substitution-tolerant repeat buys (office/MRO); make a retailer *agent-legible* (structured data, reviews, fulfillment).
- **Automation:** 9/10 · **Quality:** 9/10 · **Verdict: Mixed** (Skip as playbook, Worth Trying as rails map)
- **Red flags:** a16z investment narrative; no small-operator economics.

## Video 3: Wes McDowell — "Hormozi's New YouTube Strategy" *(content strategy)*

- **The internet's read is wrong.** Second channel is an overflow pipe for already-filmed workshop footage (~4,000 clips/year), not the funnel. Money is in **narrow "watch me work" videos** (quoted buyer questions). Student David Jackson: 5 clients in 4 months; 35-view dentist-SEO videos converting because every viewer is the buyer.
- **Revenue model:** "small channel out-earns 4M-sub main" asserted, not evidenced. Kansas case is checkable.
- **Replication:** run wide + narrow on ONE channel until you have Hormozi-level volume; one Zoom/livestream → 4–8 clips; cap 1–2 uploads/week.
- **Automation:** 6/10 · **Quality:** 7/10 · **Verdict: Worth Trying**
- **Red flags:** ends in McDowell's own masterclass funnel.

## Video 4: Mira AI — "AI Filmmaking Team With Claude" *(sponsored tutorial)*

- **Architecture worth stealing:** screenwriter + image + video + director in shared context; director writes QC fixes as **persistent rules**; every video prompt specifies the shot's END state for continuity.
- **Revenue model:** none. Higgsfield affiliate.
- **Automation:** 8/10 · **Quality:** 5/10 · **Verdict: Mixed** — steal the pattern, not the platform.

## Video 5: Casino Steve — Bubble Craps *(standing rule)*

- Session: $500 → $542. Don't Come ~1.36% house edge — still negative EV. Only replicable business is the session-video format + craps-channel shoutout economy.
- **Verdict: Mixed** as content niche, **Skip** as money strategy.

## Video 6: Jake Bauman — "Grok Bot to Get My Brand Cited by AI" *(GEO/AEO)*

- **Strongest new playbook of the batch.** 7-bot Grok team ($20/mo) doing AI-visibility ops vs $2K–$50K/mo agencies. Diagnostic: 20–50 prompts across branded / unbranded / comparison, re-run every 2 weeks. Gate: ~4.0+ stars or AI won't recommend you at all. llms.txt is theater (97% get zero requests).
- **Revenue model:** none for himself. Cited: Ahrefs 75K brands, mention correlation 0.664 vs backlinks 0.218; ChatGPT recommends 1.2% of locations vs Google 35.9%.
- **Measured proof of HIS system: none.** Third-party correlational only. Unusually honest about that.
- **Automation:** 9/10 · **Quality:** 7/10 · **Verdict: Worth Trying** (as diagnostic + ops checklist)
- **Do this week:** 10-minute brand diagnostic on ChatGPT + Perplexity + Google AI; check GPTBot/ClaudeBot/PerplexityBot/Google-Extended on robots + WAF.

## Video 7: Paul J Lipsky — ChatGPT Images 2.5 *(tool review)*

- New: character/face consistency across iterative comment-edits. Productizable: thumbnails, photo restoration, pet portraits, interior mockups.
- **Automation:** 5/10 · **Quality:** 7/10 · **Verdict: Worth Trying** as format + as a signal the tool is good enough to productize.

## Video 8: MyWifeQuitHerJob — "Forget Amazon, Shopify" *(ecommerce)*

- Amazon blocked AI crawlers; Shopify stores are citable. FAQ-schema audit: 26 pages → 85% improved ranking; bridal handkerchiefs 7→4 with 5× traffic. Honest miss: napkins 30→12, zero clicks. Shop Campaigns = pay per verified new customer; 48% of Shop-app orders are first-time.
- **Automation:** 8/10 · **Quality:** 7/10 · **Verdict: Worth Trying**
- **Red flags:** he doesn't even use Shopify (built his own); course/conference funnel.

## Video 9: Jonathan Nilsen — TikTok Six-Figure Publishers *(KDP)*

- Demand engine: TikTok/IG attention → TikTok Shop → Amazon spillover rank. Lark and Road $2.25M TikTok Shop Jan–Jul; reusable 11-sec format. Claremont: 4 months / 200+ videos before it clicked. Amar: one IG reel, $3.5K/mo → $1–1.5K/day.
- **Automation:** 7/10 · **Quality:** 6/10 · **Verdict: Worth Trying** (price in the quiet window)
- KDP $ are BookBeam estimates; coaching funnel; survivorship.

## Video 10: Nick Ponte — "NEW Way to make $ with chatgpt" *(local AI services)*

- Dead Facebook profiles (500–1K followers, 6+ months silent) → 2 weeks free AI posts → $500–$3K/mo social-posting retainers. Claims $123K/mo QuickBooks (established agency, not the $150/mo newbie testimonial).
- **Automation:** 8/10 · **Quality:** 5/10 · **Verdict: Mixed** — tactic is testable; video is a HighLevel affiliate funnel.

## Video 11: The Next New Thing — Slowbooks *(open-source agent accounting)*

- Free anti-QuickBooks: CLI agent IS the books. Receipt OCR → file → audit-logged reversible AI changes. 344 GitHub stars. Live demo with an OCR stumble.
- **Automation:** 9/10 · **Quality:** 6/10 · **Verdict: Worth Trying** as a pilot, not production books yet.

## Video 12: Koerner — "If We Had to Make $1M Fast" *(idea roundup)*

Density of real playbooks: RV rentals ($5K/mo net/unit at 50% occ), vibe-coding agency (Billy Howell ~$60K/mo, secondhand), overseas staffing, corporate AI-audit (Ben: charity-backed guarantee, 6 figures/customer), **dormant newsletter roll-up (~10¢/sub)**, hero-workflow AI agency (live 57-min garage-door close on camera), liquidation, buy-a-business + AI, equity-for-services, glamping lease-option.
- **Quality:** 7.5/10 · **Verdict: Worth Trying** — treat $1M/6mo as clickbait, steal individual playbooks.
- **New mechanics:** newsletter roll-up; equity-for-services ("Bro Mozi").

## Video 13: Sunny Lenarduzzi — "$1M in 12 Months from 0 subs" *(YouTube lead-gen)*

- Offer FIRST ($10K POP, live Zoom), then 8-video evergreen machine (3 BOFU / 2 MOFU / 2 TOFU / 1 depth). Math: 8–9 clients/mo at 30% close. Self-reported $469K from one video. Course-funnel test: framework is fully given, but every proof lives in the guru economy.
- **Automation:** 3/10 · **Quality:** 4/10 · **Verdict: Mixed**

## Video 14: Koerner — Contactless Trailer Rentals *(operator interview)*

- **Best receipts of the night.** Nathan, Lancaster PA: 10 used trailers $35K, $5.5–7.5K/mo gross, ~$4K/mo net, 2–4 hrs/week, ~$200–250/hr. Prior owner did $28K/yr on the same fleet. Lockbox + CRM + GPS + photo check-in. Price ~1.5% of purchase/day. Dump trailers rent most.
- **Automation:** 9/10 · **Quality:** 9/10 · **Verdict: Worth Trying**
- **This weekend test:** list a trailer (or stock image) on FB Marketplace + Neighbors; scrape residents-per-trailer across sister cities.

## Video 15: Glo Atanmo — "8 Ways I Get Paid on YouTube" *(creator monetization)*

- Memberships 3-tier ($4.99 / $49 / $499) claimed six figures/year; $45 CPM; 45-day monetization posting daily 25-min videos. New-to-archive: Player for Education licensing; YouTube nudging memberships (~30% cut); affiliate + brand-deal double-dip.
- **Automation:** 3/10 · **Quality:** 8/10 · **Verdict: Worth Trying**
- Six-figure membership claim unverified in transcript.

## Video 16: OpenClaw — ClawCast Ep 9 *(platform podcast)*

- 2.0: multiplayer gateway (n people, one agent, Tailscale/Cloudflare), agent-generated dashboards as deliverables, worker nodes (still rough), default "dreaming" memory, skills workshop that self-prunes.
- Money is around the platform: agencies, dashboards-as-a-service, VPS. Foundation can't be bought — that's the enterprise pitch.
- **Automation:** 9/10 · **Quality:** 7/10 · **Verdict: Worth Trying** for anyone selling agent-run ops.
- Nodes not SLA-ready; shared-gateway trust boundary is real.

## Final Ranking (by automation potential)

1. GEO/AEO Grok crew (Bauman) — 9/10 · Worth Trying
2. Slowbooks agent accounting — 9/10 · Worth Trying (pilot)
3. Contactless trailer rentals — 9/10 · Worth Trying · **best receipts**
4. OpenClaw 2.0 ops layer — 9/10 · Worth Trying
5. Agentic payment rails (a16z) — 9/10 · Mixed (thesis)
6. Dead-profile social retainers (Ponte) — 8/10 · Mixed
7. Shopify AI-citability (MWQHJ) — 8/10 · Worth Trying
8. GitHub skill roundup (Isenberg) — 8/10 · Mixed
9. Higgsfield film crew — 8/10 · Mixed
10. TikTok→KDP publishers — 7/10 · Worth Trying
11. Koerner $1M roundup — 7/10 · Worth Trying
12. Hormozi narrow videos — 6/10 · Worth Trying
13. Images 2.5 productize — 5/10 · Worth Trying
14. Lenarduzzi $10K offer-first — 3/10 · Mixed
15. Glo 8 YouTube streams — 3/10 · Worth Trying
16. Bubble craps — Skip as strategy

## Cross-Video Synthesis

**Three threads.** (1) **Be citable.** Bauman's GEO diagnostic, MWQHJ's FAQ schema (85% hit rate), Nilsen's manufactured TikTok demand, Hormozi's exact-question titles — same inversion: stop bidding on rank, become the answer machines and buyers already want. (2) **Named agents with jobs beat click-tools.** Slowbooks, OpenClaw dashboards, Mira's persistent-rules director, Bauman's 7-bot crew. (3) **The analog businesses still have the cleanest P&Ls.** Nathan's trailers beat every AI tutorial on receipts. Koerner's roundup is the idea menu; Nathan is the worked example.

**New vs known themes:** GEO/AEO as a $20/mo vs $50K/mo wedge; agent-native vertical software (bookkeeping); agentic-payment vs agentic-shopping split; dormant-newsletter roll-up at ~10¢/sub; equity-for-services; Player-for-Education licensing; OpenClaw multiplayer + dashboards-as-a-service. Re-skins: local AI retainers, KDP, YouTube funnels, GitHub roundups.

**Numbers-to-credibility still inverted:** Shortfundly-style dollar catalogs vs Nathan naming insurance line items. Use Ted's YPP-check + Casey's live-dashboard standard on every future batch.

**Do this week:** brand/category AI-citation diagnostic; robots/WAF bot crawl check; trailer (or stock-image) demand test if you want the analog play.
