# Playlist Research - Michael Buchanan's "Research" Playlist (2026-09-03 Run)

**Source playlist:** ["Research" by Michael Buchanan](https://youtube.com/playlist?list=PLamiZQJOzMbY) (`PLamiZQJOzMbY`)
**Special run:** playlist-targeted analysis. Playlist held 12 videos; 10 are new coverage. The other 2 (Superwall's $18M app teardown, Starter Story's $69k SaaS) were covered in the 2026-08-31 report and skipped. The `PLamiZQJOzMbYz0` link from the request returns YouTube error 400 (invalid playlist ID) - treated as a truncated paste of this same playlist.
**Coverage note (standing rule):** not every video is an automated-business pitch - some are general summary/analysis. Types are labeled per video: 6 business-model pitches, 3 general-analysis/education videos, and each gets the treatment it deserves.

## Videos Analyzed

| # | Title | Channel | Type | Views | Transcript |
|---|-------|---------|------|-------|------------|
| 1 | Watch Me Build an App With AI and Make a Sale in 85 Minutes | Chris Koerner / Koerner Office | Business demo | ~23k | Yes |
| 2 | If I Had 0 Subscribers, Here's How I'd Make $1M in 12 Months | Sunny Lenarduzzi | Business pitch | ~38k | Yes |
| 3 | Grok Bot Is Weirdly Revolutionary | Less Bitter | General analysis | ~73k | Yes |
| 4 | I Studied 1,000 Digital Product Businesses, Here's What Works in 2026 | Richard Yu | Business pitch | ~21k | Yes |
| 5 | I Found the Pattern Behind Every Viral Video | vidIQ | Education | ~48k | Yes |
| 6 | He Started YouTube After 40 - Now It's His Full-Time Career | Think Media Podcast | Case study | ~6.7k | Yes |
| 7 | Claude AI + Digital Products = $218,974 | The Ecom King | Business pitch | ~23k | Yes |
| 8 | Ask Claude These 3 Questions, It Will Change Your Bank Account | Dan Martell | Education | ~172k | Yes |
| 9 | Claude + Shopify = $12,000/Month | Jordan Welch | Business pitch | ~2k | Yes |
| 10 | The Faceless AI YouTube Niche Making People RICH | Wholesale Ted | Business pitch | ~44k | Yes |
| — | $18M/Year Apple Watch App | Superwall | Skipped - covered 08-31 | | |
| — | $69K/Month SaaS in 2 Months | Starter Story | Skipped - covered 08-31 | | |

---

## Video 1: Chris Koerner - "Watch Me Build an App With AI and Make a Sale in 85 Minutes"

**Story:** The most operationally detailed video in the playlist series: Koerner live-builds and launches **OnlyWaivers.com** - a liability-waiver SaaS for LDS church youth leaders (his own niche) - buying the domain ($12), prompting Claude (top model) to write the build prompt, building the app in ~20 minutes with Replit Agent 4, filming a 30-second iPhone selfie ad, and having the **official Facebook Ads MCP create and run the entire Meta campaign** concurrently. One real customer ($13/year, Idaho) lands within the session - no audience leverage.

**Mechanics:**
- Product: mobile-first tap-to-sign waivers; organizer dashboard with signed copies + IP/audit trail (Claude itself flagged that tap-signatures are worthless without audit trail and minor-compliant language)
- Pricing: $13/year or $17 lifetime, one plan; paywall only after the user has built their waiver (sunk-cost); "I'd rather get $17 than $0"
- Stack: Replit Agent 4 (built on Claude), Stripe (live-mode gotcha: must claim the connection on the live account, use `sk_live`), Resend for email, GA + Meta Pixel with server-side CAPI, autoscale deployment
- Ads via natural language: paused campaign created by the Facebook Ads MCP; $200/day CBO, traffic objective, men 25-60 US, Advantage+ OFF; **Meta banned religion targeting ~4 years ago → the niche is targeted via ad-copy vocabulary** ("ward, stake, trek, mutual") so outsiders self-select away. Live metrics: landing-page-view cost fell $1.49 → $0.65, CTR climbed 1% → 1.5%; a Utah-only geo fix (one prompt, no re-review) hit **7.3% CTR**
- AB testing: 5-6 ad variants with per-ad UTMs so Stripe reveals which ad converts
- Organic: Reddit story-first post (no link, product name in comments, link edited in at 93% upvote) → #8 post of the day on r/LatterDaySaints; Facebook groups: pain-point post + screenshot, solution in comments
- Costs: $12 domain; Replit + Claude ≈ **$200-250/month** ("PhD-level experts - coding, ads, copywriting - for $250/month"); ~$100 ad spend in session; ~6 hours total across sessions
- MCP fleet he runs daily: Beehiiv, Facebook Ads, Gmail, Google Calendar/Drive, GoHighLevel, Stripe, Typeform, Zapier + more. Side stat: a **$10,000 agency quote for newsletter automation replaced free** by the Beehiiv MCP + one prompt

**Quotes:** "Sell it before you have it." / "In any business, you want to remove friction to getting the money and add friction to losing the money." / "The first dollar for any business is the best dollar in the world."

**Automation angle:** The whole video is an automation showcase: prompt-chaining (Claude writes prompts for Claude-built tools), MCP orchestration replacing agency workflows, concurrent agent tasks, agents self-healing. Operator insight: **when an AI says it "can't," push back - it's usually credit-aversion, not incapability.**

**Red flags:** Net economics deeply negative and admitted: ~$100 + ~6 hours for one $13 customer; Claude's own math says $200/day needs ~15 sales/day to break even ("almost no chance") - the real bet is ward-level word-of-mouth virality, unproven. Title's "85 minutes" omits 3 prior hours. n=1 customer, no retention data. The $20/month framing understates ~$250/month real tooling.

---

## Video 2: Sunny Lenarduzzi - "If I Had 0 Subscribers, Here's How I'd Make $1M in 12 Months"

**Story:** The order-of-operations system: **build a high-ticket offer FIRST, get results, and only then publish YouTube** - an 8-video funnel-architected starter batch aimed at small-but-relevant search traffic, not reach. The "creator game" (views/AdSense at $2-3/1k) vs the "business owner game" (leads, dollar-per-view, relevance over reach).

**Mechanics:**
- Sequence: Offer → Ideal client → Messaging → Leads → Sales. "YouTube is step 4, not step 1."
- **POP (Profitable Offer Prototype):** bare-bones live version of the program - Google Docs, Zoom, a community; no tech build-out. Transformation statement = one sentence (who + zero state + hero state + outcome)
- **8-video Evergreen Revenue Machine:** 3 BOFU (pain/comparison - lowest views, highest conversion) + 2 MOFU (methodology/proof) + 2 TOFU (awareness) + 1 thought-leadership - "not experiments; deliberate architecture"
- Ideation buckets: client FAQs, "gateway" videos (outliers on similar channels - make your version), pain points (BOFU)
- Metrics in order: CTR (5-10% but from the *right* viewer - high CTR + low retention = wrong viewer), retention past 10%, **leads per video** (comment-trigger → auto-sent diagnostic link)
- Her receipts: one Sept 2024 video still converting ~2 years later - $469k direct sales, 5.2% CTR, 16,787 email opt-ins, 1,131 booked calls; client Jeff (marriage-saving niche): <$700 subs, $10k/month, $10M+ over 4 years, now $130-150k/mo all organic
- The math: $10k program × 100 clients = $1M; 8-9 clients/month at 30% close = ~28 calls/month
- Cadence: **one video per week is enough**

**Quotes:** "Views don't pay your bills, the right viewers do." / "A video can get 100,000 views and generate zero clients. A video can also get 800 views and generate $30,000."

**Automation angle:** Highly compatible with automated content ops: batch-produce funnel-mapped videos, auto-generate topics from FAQs + competitor outlier mining, keyword-trigger lead capture, dollar-per-view tracked per video programmatically.

**Red flags:** Funnel video for her own coaching; all case numbers self-reported; $1M math assumes a $10k offer at 30% close - plausible for warm experts, optimistic generally.

---

## Video 3: Less Bitter - "Grok Bot Is Weirdly Revolutionary" *(general analysis)*

**Story:** mo (mo.io / Ship Academy) stress-tests xAI's Grok Bot live by connecting real accounts (Plausible analytics, Gmail/Drive/Calendar, GitHub, Substack) and building an agent fleet: analytics alerts, NYT/Verge headline watchers, competitor-pricing espionage, uptime monitoring, paid-subscriber notifications, and a blog manager that edits markdown → commits → pushes → **deploys his static site from a chat command**. Walked in expecting annoyance; concluded "this is how AI is done from now on."

**Core findings:**
- Each request **spins up a computer** (VM with a browser); the agent navigates real websites instead of calling APIs - he prefers browser navigation as the more general, future-proof path. Sign-ins hand over control then resume
- **Routines:** any agent run saves as a recurring scheduled job (cron + browser + LLM)
- The fleet on camera: Analytics bot (alert at >10 realtime visitors - his site: 828 visitors/24h, +214%), Press bot (NYT lead-story changes), Chief of Staff aggregator, Drive screenshot archive every 5 min, Espionage bot (Linear/Slack/Notion pricing pages), Uptime/cert monitor, Substack paid-subscriber alerts, GitHub-connected blog publisher
- Verdict: "Not new technology, just combining them in cool ways" - but VM + browser + routines + plugins + per-assistant phone notifications crosses a usefulness threshold. Predicts Claude/OpenAI will copy it

**Quotes:** "It's actually revolutionary, but for very strange reasons." / "This is just going to be how AI is done from now on. It's just access to a computer."

**Applicability to automated content ops:** scheduled browser agents monitoring news/lab press pages can feed a content pipeline; screenshot archives build research history; a GitHub-connected markdown publisher is a direct fit for automated blog/newsletter publishing.

**Red flags:** Single-session demo - zero reliability/cost/rate-limit testing; euphoric tone with no stress test; shared agent file system with secrets only glances at security.

---

## Video 4: Richard Yu - "I Studied 1,000 Digital Product Businesses, Here's What Works in 2026"

**Story:** The 5-part Instagram machine distilled from his "1,000+ business" study: 7-15-second videos (algorithm ignores follower count) → comment-keyword auto-DM → $27 impulse product + $1,500-2,000 high-ticket offer closed via non-pushy "value calls" at 1-in-3 to 1-in-4.

**Mechanics:**
- Content: 7-15 sec Instagram clips, phone-only, one idea each; CTA videos only 2-3×/week - "an Instagram viewer can go from scroll to buying a $27 guide before the coffee finishes brewing"
- DM automation: ManyChat / GoHighLevel / "AllenAutoDM" - comment keyword triggers the free-guide DM, "build once, runs forever"; follow up with a real question
- Product pair: $27 low-ticket ("low enough that nobody hesitates, high enough that you're not giving your work away") + $2k core offer. **"You will not build a real income on $27 sales alone"** - $10k/month = 5 sales at $2k vs 370 at $27
- Authority: buyers purchase from someone **1-2 steps ahead, not 20** (relatability > credentials); 4 freebies rotated weekly - whichever blows up reveals demand; the 10-15-min value video (8-10 min pure teaching, then soft pitch) books the calls
- Diagnosis when stuck: traffic problem (more/sharper 7-sec videos) vs conversation problem (revive the DMs) - "the fix is completely different for each"

**Quotes:** "Nobody buys from the person who's 20 steps ahead of them... people buy from the person who's only one or two steps ahead." / "Either not enough people know you exist, or you're not talking to the ones who do."

**Automation angle:** Explicitly semi-automated: keyword-trigger DM funnels, unattended $27 checkout, evergreen value video. The 7-second no-edit format is mass-producible. The insisted-on human piece: live value calls for the $2k close.

**Red flags:** The "study" is a marketing frame; all numbers self-reported; the model quietly scales with your sales calendar, contradicting the passive vibe; "any niche" unqualified.

---

## Video 5: vidIQ - "I Found the Pattern Behind Every Viral Video" *(education)*

**Story:** A framework breakdown of "hundreds" of outlier videos (5×-100× channel average): what they share isn't equipment, volume, or frequency - it's how the first seconds interact with viewer psychology. Four rules, each with a named effect and a real channel example.

**The four rules:**
1. **Recognition beats novelty** (mere exposure effect): familiar formats (tier list, blind taste test, 30-day challenge) feel safe pre-click. The "outlier method": find a format already over-performing in *any* niche, pour your topic into that mold. Example: Family at Sea borrowed a ranking format → 175k views, ~10× average
2. **Open a loop the viewer must close** (Zeigarnik effect): never front-load the answer; raise the question in title + first sentence. Example: "Diary of a CEO is making you less successful" → 1M+ views, 8× average; 130 subs/day → 7,000 on release day
3. **Sell identity, not logistics:** "I left London for Bali alone 2 years ago. This is my life now." ~10× the same topic framed as living costs
4. **Answer "why trust you?" fast** (authority bias): a concrete number/credential in the first ~20 seconds ("I've shot over 300 weddings")

**Quote:** "Nobody subscribes to a topic. They subscribe to a version of themselves." / "You're not competing on the topic of the video. You're competing on how well you know the viewer who is browsing through this topic."

**Applicability to automated ops:** The outlier method is itself a data pipeline - programmatically detect over-performing formats and template your topic into the proven mold; open-loop titles, identity framing, and credential-first intros are all generatable patterns; vidIQ's outlier score is exactly the ranking signal an automated pipeline can select on.

**Red flags:** The video is a vidIQ ad for its outlier feature; examples cherry-picked, no base rates; psychology effects applied as just-so stories.

---

## Video 6: Think Media - "He Started YouTube After 40 - Now It's His Full-Time Career" *(case study)*

**Story:** Bloodline Adventures (Alberta hunting/fishing, two brothers) went ~1,000 → 100,000+ subs in ~2 years on viral Shorts (20-40M-view clips), then hit the classic wall: massive views, near-zero conversion, negative sub days. After a mastermind: reverse-engineer content for a defined viewer, diversify revenue, use proof-of-work to win affiliates. Bryce (ex-fire lieutenant/paramedic, 21 years) is now YouTube strategist for Wild TV.

**Key numbers and lessons:**
- Shorts→long-form conversion: **"next to zero, 0.0 maybe four"** (~0.04%); long-form CTR "if we could break 1%, good day"
- Root cause: 2 verticals/day vs ~1 long-form/week = "you're going to get a shorts channel" with an audience mismatch
- Fix: decide who each video is for **before** the trip; script what to shoot/say
- Repackaging: a 3,000-view coyote cut became 1.7M views re-cut; the spike came **75 days after publish**
- **Proof-of-work affiliate play:** rejected by Cabela's ("program full") → replied with an existing #1-ranking Cabela's review video → instantly accepted. "Prove you can do this work for them without asking for it first."
- Revenue: one viral short ≈ "a couple thousand dollars" AdSense; monetization went 1 stream → "six or seven"; now 60-70 sponsor offers/week, 90% declined

**Quote:** "We didn't make $1,000 [on what you taught us]. We made about six."

**Applicability to automated ops:** define the avatar before generating (targeting beats volume); monitor the back catalog for late-breaking outliers and re-cut rather than only producing new; deliberate shorts→long bridges (related-video links) instead of passive cross-posting.

**Red flags:** Think Media mastermind promo frames the whole story; all numbers self-reported; one channel's viral run as survivorship evidence.

---

## Video 7: The Ecom King - "Claude AI + Digital Products = $218,974"

**Story:** An AI-run digital-product pipeline: Claude + ChatGPT together ("I stopped trying to choose between them") with MCP connectors - **Everbe** (Etsy revenue scraping), **Winning Hunter** (ad intel), **Higgsfield/Sedance 2.5** (ad video) - to find validated demand, build a better product, and sell it on your own .store site with AI-made Facebook ads. Proof: a Stripe flash claiming $218k gross / $180k net at ~$241 AOV.

**Mechanics:**
- Research chain: Everbe MCP → top Etsy digital listings by monthly revenue + keywords (top find: a "custom spell ritual" listing doing $73k/month) → cross-validate in the Facebook Ad Library. "Any one tool can be fooled on its own, but it's very hard to fool all three" (Etsy data + live ads + reviews)
- Product criteria (verbatim rules): ad running 60+ days; Etsy listing $2,000+/month; price $20+; lots of reviews; boring evergreen problem (not a trend); buildable-better in one day
- Avatar research: hand findings to ChatGPT (high effort) → 5 avatars with pain points mined from 1-3-star reviews; pick a differentiated angle per avatar
- Build: Claude builds the product itself - demo: a debt-payoff spreadsheet (snowball/avalanche order, progression bar, "check the math" sheet) in ~20 minutes; **test everything AI builds**
- Ads: download competitors' best ads → Claude writes the script against the research doc → Sedance 2.5 renders the video. Ad copy: "You type your debts in once. It builds the payoff order... No app, no subscription. It's just an Excel file."
- Division of labor: "ChatGPT does the research. Claude writes and builds the actual product. A year ago, you'd have to pay different people to do four different jobs."

**Automation angle:** A near-fully AI-run product business with the human only validating/testing. Transferable patterns: cross-source validation before committing compute, negative-review mining for positioning, competitor ad-script cloning, agent handoffs via MD-file briefs.

**Red flags:** Stripe flash with no timeline, no ad-spend total, no refunds data; $218k vs $180k quietly glosses ~$38k fees; paid tools never costed; "skip all approvals" on an autonomous agent is bad safety advice; pensioner positioning example admitted "complete BS" by himself; $20-Etsy → $241-AOV arbitrage asserted, not demonstrated.

---

## Video 8: Dan Martell - "Ask Claude These 3 Questions, It Will Change Your Bank Account" *(education)*

**Story:** The three questions Martell asks AI before starting any business: what to sell (a painkiller, not a vitamin), what your unfair advantage is, and how to get a real payment to validate - "sell before you build." Framed by his own history (two failed companies, then Spheric sold in 4 years).

**The framework:**
- Taxonomy: vitamins get cut when budgets tighten; painkillers (make money, get leads, retain team) survive. People pay for only three things: **money, time, status**. "Million-dollar businesses aren't built on $10 problems."
- **Q1 - what to sell:** ask AI for 10 *observable, nuanced* pain points in your industry, "only getting worse," ranked by willingness to pay. Hack: a consulting firm's service menu proves demand
- **Q2 - your edge:** connect AI to your context (he's ingested meetings, transcripts, financials, 15 years of decisions); prompt: "Interview me about the last 10 years of my work. 10 questions one at a time, then tell me what my unique edge is." Then red-team: "Be brutally honest. Is that actually rare or am I overrating myself?" Tool named: **WhisperFlow** for voice-answering the interview. "Pain alone is a market, edge alone is a resume. Where they cross is the business."
- **Q3 - validate with money:** the "Wizard of Oz" test (at Flowtown: fake signup flow through card entry - 20% entered real payment details, then "servers over capacity"). Four validation prompts: cheapest test that gets **one real payment within 7 days**; one-page offer (promise, timeline, price, nothing else); the 10 people to contact + exact message + follow-up ("Not a call, not a demo, cash"); "why would some people say they want this and never pay?"
- Rules: first 10 outreach attempts **by hand** before automating; AI is a "world-class people pleaser" - always add "now push back on me"

**Quotes:** "Certainty brings currency. You sell before you build every single time." / "There's nothing more expensive than building something that nobody will pay for."

**Applicability to automated ops:** the question sequence is itself an AI pipeline (context ingestion → research → interview → red-team → offer generation); the people-pleaser caveat (every AI answer needs an adversarial pass) is directly applicable wherever unchecked LLM output compounds flattering errors.

**Red flags:** Funnel for his "AI company OS" via Instagram DM; the Wizard-of-Oz test collects real card details under false pretenses - ethically questionable; all numbers self-reported.

---

## Video 9: Jordan Welch - "Claude + Shopify = $12,000/Month"

**Story:** A three-step Claude-driven dropshipping demo: find a trending product (Trend Track ad-spy), validate with a Claude research verdict, clone a competitor's Shopify store (Clone Store) - both tools wired into the Claude desktop app as MCP connectors. Claimed: a new store to $424 day-one sales; titled $12,000/month.

**Mechanics:**
- Product criteria: already selling (never be first); not in Target/Walmart; **$25-30+ profit per order minimum**; wow factor. Case study: Alaskan volcanic clay mask stick, $2 COGS, sold as 2-pack ($35 profit) / 4-pack (~$40)
- Trend Track filter recipe: active ads + created last 30 days + "Shop Now" button + **10-50 live ads per brand** (under 10 = nothing happening; over 50 = big brand, too competitive); ~20 active ads for ~1 month = scaling signal
- Claude desktop (not browser): Co-work and Code modes; claims Co-work "memorizes everything in perpetuity" locally; custom connectors set to "always allow" (his habit; poor security hygiene)
- Validation prompt outputs a verdict document "in 10 minutes vs a week" of manual research; the doc is re-fed to Claude to write differentiated copy vs competitors
- Clone Store: paste competitor URL → product, images, copy into your Shopify in ~5 minutes; Blockify theme
- Funnel economics: the "free course + free AI store" is paid acquisition - **Shopify and Base44 pay him per signup**

**Automation angle:** The pitch IS the stack: MCP orchestration of ad-spy → research verdict → store clone → differentiated copy. Transferable: feed structured research output back into the LLM for positioning.

**Red flags:** $12k/month title vs $424 demonstrated day one with no ad-spend breakdown; every tool is an affiliate link; cloning competitor images/copy raises unaddressed IP issues; demo product never actually launched.

---

## Video 10: Wholesale Ted - "The Faceless AI YouTube Niche Making People RICH"

**Story:** AI music channels - long themed background-music videos from AI-generated songs + looped AI visuals - pitched as the best faceless AI niche for beginners: case channel started May 22, 27,000+ subs in 2 months, climbing to 90,000+ views/day, "well over $300/day" estimated. Then the full 4-step production pipeline.

**Mechanics:**
- **The monetization audit trick:** the Thanks/Join buttons are YPP-only features - a channel with them enabled is provably monetized. Use it to vet any niche (debunks "YouTube demonetizes AI videos")
- Niche research: VidIQ (free) → search music style → filter 20min+ / past month / by popularity → green score + verify small channels winning (130k views from a 4,000-sub channel; another from 2,700 subs). "Many people care more about the background of a music video than the music itself"
- Music: **Suno** - instrumental, 2 songs/prompt, 5 credits/song, extend function merges segments past 4 min; Pro plan = commercial rights, 500 songs/month; target 30min-2hr videos, 10-20 songs each
- Visuals: Nano Banana Pro static image, or the **frame-to-frame trick**: Kling 15s/16:9/720p loop with the SAME image as first and final frame → seamless loop; 2-4 mixed loops so the order is unpredictable
- Assembly: CapCut - the **crossfade trick** (overlap songs, drag the end handle into an arch both directions - no dead air), AI upscaler 720p→1080p, export
- Her own stack at the end: Claude Code + Nano Banana + Higgsfield automating print-on-demand product creation

**Automation angle:** An automated content factory blueprint: minutes of work → 30min-2hr watch-time assets monetized on passive ambient viewing; every step (music, loops, crossfades, upscale) is batchable today.

**Red flags:** $300+/day is an RPM extrapolation, not shown revenue; one 2-month channel as evidence; fast-scaling AI-music channels are exactly what YouTube's repetitious-content policy scrutinizes (unaddressed); all tool links are affiliates plus a self-sponsored ebook/course funnel; Suno Pro/Higgsfield costs never tallied against the claim.

---

# Cross-Playlist Synthesis

## The MCP watershed (the real story of this run)

Three unrelated videos converge on the same mechanism: **MCP connectors turning Claude from a chatbot into an operator with hands.** Koerner runs Facebook Ads/Beehiiv/Stripe/GHL MCPs (a $10k agency quote replaced free); The Ecom King chains Everbe → ChatGPT → Claude → Higgsfield for research-product-ads; Welch clones entire stores through Trend Track/Clone Store connectors; Less Bitter's Grok Bot demo shows xAI shipping the same pattern (agents with their own computers + browser + routines). When four operators in four different businesses independently converge on "connect the tools, let the agent drive," that's the 2026 stack consolidating.

## Patterns across this run

1. **Validation before compute** - Ecom King's three-source rule (Etsy + live ads + reviews), Welch's 10-50-live-ads filter, Koerner's "sell it before you have it," Martell's one-payment-in-7-days test, vidIQ's outlier scores. Every serious operator cross-checks demand before letting agents build.
2. **The human stays small but load-bearing** - Martell's manual-first-10, Yu's live value calls, Koerner's selfie ad and community credibility, Ted's niche curation. The pattern from every prior run holds: one human gate, deliberately placed.
3. **Funnel-mapped content beats content volume** - Lenarduzzi's 8-video BOFU/MOFU/TOFU architecture, vidIQ's format-over-topic, Think Media's avatar-first reverse-engineering, Ted's "background matters more than music." Reach is the vanity metric; relevance-per-view is the business metric.
4. **Ad platforms are the new agent surface** - Koerner's natural-language Meta campaigns (with copy-vocabulary targeting working around Meta's category bans) and Ecom King's AI-rendered ad videos: creative + media buying are collapsing into one prompted step.

## What we'd actually steal (analysis)

- **The Thanks/Join-button audit** (Ted) - a free, programmatic monetization check for any niche we evaluate
- **vidIQ outlier-method as code** - detect 5×+ formats across niches, template our topics into proven molds; combine with Think Media's 75-day-late-spike lesson (monitor the back catalog, not just new output)
- **Koerner's ad-copy-vocabulary targeting** - for any local/community product where protected-category targeting is banned
- **Martell's red-team prompt as a standing step** - "now push back on me" belongs in every automated pipeline before output ships
- **Lenarduzzi's dollar-per-view ledger** - the metric our own automated channels should optimize, not views

## Meta observations

Every video is still a funnel (masterclasses, $1 trials, per-signup sponsorships, affiliate stacks) - apply the Mom Test to the advisors. The most honest operators this run: Koerner (publishes the losing unit economics), Welch-rerun... is not present, but vidIQ and Martell at least teach transferable mechanics rather than pure income claims. The single least verifiable claim: Ecom King's Stripe flash. The single most replicable-by-us system: Ted's music-channel factory (every step automatable, economics view-dependent) - with YouTube's repetitious-content policy as the standing risk.

## Automation-potential ranking (business videos only, per standing rule)

| Model | Automatable today | Human bottleneck | Verdict |
|---|---|---|---|
| AI music channels (Ted) | Entire pipeline (Suno/Kling/CapCut batch) | Niche curation, policy risk | **High** - economics scale with views |
| Etsy digital products + own store (Ecom King) | Research→build→ads chain | Validation QC, testing | **High** - but claims unverified |
| Vibe-coded niche SaaS + MCP ads (Koerner) | Build, ads, AB tests, monitoring | Niche access/trust, unit economics | **Medium-high** - proven end-to-end, unproven profitable |
| 7-sec IG + DM funnel + $2k close (Yu) | Content, DMs, $27 checkout | Value calls | **Medium** - scales with calendar |
| High-ticket offer + 8-video funnel (Lenarduzzi) | Topic mining, lead capture, tracking | Offer delivery, calls | **Medium** - expert-dependent |
| Dropshipping store-in-a-day (Welch) | Research, verdict, store clone | Ad spend, IP risk | **Medium** - demo never launched |
