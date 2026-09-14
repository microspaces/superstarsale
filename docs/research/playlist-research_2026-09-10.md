# Playlist Research - Michael Buchanan's "Research" Playlist (2026-09-10 Run)

> **Run note:** Playlist swapped — 7 videos, 6 new (Nick Ponte's ChatGPT video repeats from 09-09, skipped). Full transcripts 6/6. The 9 AM daily cron claimed success but never published (second consecutive silent publish failure) — daily reports for 09-09 and 09-10 recovered separately from surviving JSON.

**Videos found:** 7 · **Analyzed:** 6 · **Skipped:** 1 (repeat)

## Videos Analyzed

| # | Title | Views | Length |
|---|-------|-------|--------|
| 1 | [WebMCP: Let AI Agents pay you money](#video-1) || — | — |
| 2 | [I Turned Claude Code into an AI Hedge Fund](#video-2) || — | — |
| 3 | [$390K/Month With Claude AI Dropshipping](#video-3) || — | — |
| 4 | [How To Pick a YouTube Niche That Can Make You Rich (With Claude AI)](#video-4) || — | — |
| 5 | [How 12,000 Subscribers Landed a Five-Figure Brand Deal](#video-5) || — | — |
| 6 | [How a Faceless Channel Made $39K With Claude + ChatGPT](#video-6) || — | — |

## Run Theme

**Selling the shovel, part 2.** Five of six videos monetize attention around an AI workflow rather than showing verified P&L — the one receipt that matters is infrastructure, not income. WebMCP is the standout: a live, cloneable Google/Microsoft browser protocol that lets sites expose agent-callable tools. It advances the tracked agent-infrastructure thread one layer earlier in the funnel: before agents can pay (a16z, 09-09) they must be able to *complete the journey*.

### Video 1: WebMCP — Let AI Agents Pay You Money *(agent infrastructure)* {#video-1}

> ▶ Watch: https://youtu.be/EoNH3Tn8wYE


- **Business model:** Education + two proposed plays built on WebMCP, a new Google/Microsoft browser standard that lets websites expose clean, agent-callable tools (search/book/buy/coupon) instead of forcing agents to scrape the DOM. (1) "WebMCP conversion agency" — retrofit boring-business sites (law firms, HVAC, med spas, dentists) to be agent-ready; (2) "Agent mystery shopper" — automated eval service testing whether agents can complete a site's key user journeys (buy hoodie, book consult, file claim) and selling the reports.
- **Revenue model:** None given — proposed pricing only: agency at $200–$10,000 setup + ~$500–$700/mo retainer for monitoring/evals; mystery-shopper reports at ~$100 to a few hundred/mo, with "turn repeated fixes into software" as the upsell path. All figures are host speculation ("I bet," "could cash flow"), zero customer receipts.
- **Replication steps:**
  1. Enable WebMCP in Chrome flags + allow remote debugging via chrome://inspect (experimental feature; launched February as a joint Google/Microsoft effort, proposed ~2 years ago).
  2. Study the live demo store (espresso-gear shop, 16 exposed tools; repo is free to clone) to see conditional tools, login-state gating, cart/coupon actions, and spec-matching in action.
  3. Pick a niche of "boring businesses" (law, home services, med spas) and build V1 WebMCP tool manifests: request-a-quote, book-a-consult, buy flows.
  4. Pitch AI visitors as a new traffic class that books jobs; package MCP server + WebMCP + internal-tool variants as the retainer offer.
  5. Layer the mystery-shopper audit: agent runs the site's critical journeys monthly, reports stuck points/bad descriptions/missing tools/conversion risk.
  6. Alternatively, add WebMCP tools to your own store/SaaS (compatibility-driven commerce, admin panels, read-only tools for regulated industries like insurance/banking self-service).
- **Automation potential:** 9/10 — the entire deliverable (tool manifests, agent-run journey tests, eval reports, monitoring) is agent-executable; humans only do the sales call.
- **Quality:** 7/10 — real, verifiable tech: named standard with a shipped Chrome flag, live working demo with 16 tools, public GitHub repo, credible spectrum framing (headless API → MCP server → computer use → browser MCP → WebMCP → in-app agent). But the two business ideas are unproven thought experiments with invented price points and no customer evidence.
- **Verdict:** Worth Trying
- **Key actions:**
  - Clone the demo repo and ship one WebMCP-enabled tool on our own property this week to learn the protocol hands-on.
  - Track where WebMCP sits vs. the agentic-payments thread: this is the "can the agent finish the job" layer (post-SEO/AEO); payments rails are adjacent but not covered in this video.
  - Pilot the agent mystery-shopper concept as an internal eval harness first (tests our own funnels' agent-completability), then decide if it's a sellable product.
  - Watch Chrome-flag adoption as the timing signal; "experimental" is also the reason the arbitrage window exists.
- **Red flags:** Requires enabling experimental browser flags — spec and APIs may churn; adoption by mainstream sites unproven; all revenue numbers are fabricated-for-the-podcast; "first mover advantage" is the standard guru hook; 24-36-month consumer-agent adoption timeline is asserted, not sourced.

### Video 2: Claude Code AI Hedge Fund *(agent orchestration / finance)* {#video-2}

> ▶ Watch: https://youtu.be/OCj1ewRHag0


- **Business model:** YouTube content engine (prior similar video did ~2.4M views) feeding a paid Skool community — 1-on-1 calls, templates, and access to the project itself. The video IS the top of the funnel.
- **Revenue model:** none given (no Skool price, no revenue figures; only indirect evidence: 2.4M-view prior video, community upsell at the end).
- **Replication steps:**
  1. Have Claude Code architect a 5-agent pipeline with **information asymmetry** — each agent gets a different data feed (economic news, market depth, social sentiment, etc.) so disagreement is real, not five flavors of the same answer.
  2. Build data ingestion: prices every 5 min, fundamentals daily, SEC insider trades daily, news every 15 min (~420 bars, 687 insider trades, 200 articles in his day-2 run — all automated).
  3. Assign investor personas with restricted views: Buffett = fundamentals only; Munger = fundamentals + news; Ackman = fundamentals + insider trades; Cohen = price action only; Dalio = price action + news. Agents cannot see each other's data.
  4. Add a quality gate (composite score ≥ 0.35) so boring blue-chip picks never reach the agents.
  5. Wire a visual dashboard (Next.js/React + Python/FastAPI + Timescale + Celery, Dockerized): pipeline nodes, per-agent verdicts, confidence, reasoning, committee consensus.
  6. Validate with a **blind backtest**: load data only up to a cutoff date, run the full pipeline as if it were that day, record picks BEFORE looking at outcomes, then compare vs S&P 500 and hedge fund index.
- **Automation potential:** 9/10 — the entire loop (ingest → scan → multi-agent analyze → rank → dashboard) runs unattended; the only manual steps were bug-fixing and the experiment framing.
- **Quality:** 5/10 — the methodology is unusually honest for this genre (blind cutoff, pre-recorded picks, published allocations, admits losing to the hedge fund index by 2.46 pts). But it's a **simulated backtest, not paper trading and not real money** — a single 3-month window (n=1), "beat the S&P by 1.01%" is statistical noise, hedge-fund comparison is fuzzy by his own admission, and the results dashboard is self-reported with no independently checkable artifact in the transcript.
- **Verdict:** Mixed
- **Key actions:**
  - Steal the core orchestration pattern: give agents **different data views** instead of the same context — directly applicable to any multi-agent research/analysis task.
  - Steal the blind-backtest protocol for evaluating any predictive agent system (cutoff data, record-before-look).
  - SEC EDGAR insider-trade feed = free, underused signal source for finance agents.
  - Do NOT extrapolate one quarter's backtest to "AI beats Wall Street" — his own numbers show it lost to the HF index.
- **Red flags:** Simulated P&L presented as proof ("results are real" = a backtest); single-window sample; monetization is a Skool community funnel behind unverifiable claims; "school community" endgame revealed only at the end; hedge-fund benchmark unfalsifiable (funds don't disclose returns).

### Video 3: $390K/Month Claude Dropshipping *(ecommerce)* {#video-3}

> ▶ Watch: https://youtu.be/ZU7EhrOCmmM


- **Business model:** Creator tutorial monetized via affiliate links (Winning Hunter spy tool, USA Drop supplier), a clearly sponsored Photoroom segment, and like-gated "step-by-step guides, skills, and prompts" (engagement farming; likely community/course funnel behind the description link). The $390K/mo in the title is a Winning Hunter *estimate of a stranger's store*, not the creator's revenue.
- **Revenue model:** none given for the creator or his clone store; the headline $390K/mo is a third-party spy-tool estimate of a competitor store launched in February — unverifiable and not his money.
- **Replication steps:**
  1. Find proven designs on Winning Hunter (paid) filtered by niche + estimated revenue; pull top-spend image ads from the competitor's ad library as creative references.
  2. Deconstruct into 3 components sourced from *different* stores: best homepage, best product/landing page, best hero section (check mobile view via inspect element).
  3. Use a ChatGPT prompt template (his Google-doc cheat sheet) to turn reference URLs into build prompts.
  4. Build each page as an HTML concept in Claude Design — homepage and product page in *separate* tabs (combining corrupts the file); export standalone HTML.
  5. Add the product to Shopify FIRST via a supplier app (USA Drop) so Claude's page build can find it.
  6. In Claude Co-work, connect the Shopify connector (set permissions to always-allow), upload both HTML files with a merge prompt instructing it to use the connector; wait ~25–35 min while it converts HTML into a native, fully editable Shopify Liquid theme.
  7. In parallel, build brand assets in Photoroom (sponsored): AI logo, product-staging images recreated from the competitor's top-spend ads (ChatGPT writes image prompts matched to the HTML placeholders), AI video animations for the hero.
  8. Upload images/logo into the Shopify product and theme sections; set title/variants/description; store is done.
- **Automation potential:** 7/10 — the 25–35 min HTML→Liquid build is genuinely unattended, but the workflow is hand-orchestrated across 5 tools with copy-paste prompt relays, and the hard parts of dropshipping (product selection, ad testing, traffic, margins) stay fully manual.
- **Quality:** 3/10 — the *tutorial* looks real (specific UI steps that match actual tool behavior: connector app install, file-corruption quirk, export-to-chat-section, build times). The *money claim* fails the receipts test: no dashboard screenshot, no store name (his clone is a throwaway "914RR" store), headline number is a spy-tool estimate of someone else's store, plus like-gated deliverables and a ~2-minute sponsored read framed as tutorial content.
- **Verdict:** Mixed
- **Key actions:**
  - The one genuinely new mechanic: Claude Co-work + Shopify connector converting cloned HTML concepts into **native editable Shopify Liquid** — closer to what a $1–3K Shopify design agency ships than typical AI template generators. Real capability, but a wrapper workflow (manual ChatGPT↔Claude relay), zero moat.
  - More valuable as a **productized service** ("AI-built branded storefront" for ecommerce/local clients) than as dropshipping yourself.
  - Reuse the 3-part design deconstruction (best homepage + best PDP + best hero from different stores) for any landing-page work.
  - Photoroom product staging + AI video is a cheap way to make generic supplier products look branded.
- **Red flags:** Headline revenue is unverifiable third-party data presented as proof; like-gated "free" prompts; affiliate links for every recommended tool; sponsored segment (Photoroom, with self-reported stats like "63% of shoppers") embedded in the tutorial; "FREE" in title is misleading (Winning Hunter is a paid spy tool; Claude Pro + Photoroom premium aren't free); no evidence the creator runs a profitable store; never addresses ad costs, margins, or fulfillment economics.

### Video 4: Pick a YouTube Niche With Claude AI *(course funnel)* {#video-4}

> ▶ Watch: https://youtu.be/d2_E2JsrOVM


- **Business model:** High-ticket coaching funnel disguised as an AI tutorial. Free framework video → free "light version" Claude "niche validator" skill in the description → free live training (waitlist capture) → expensive 1-on-1 mentorship/cohort ("very expensive to buy," 5 seats, ~18% application acceptance). The Claude skill is the lead magnet; niche-picking education is the product.
- **Revenue model:** Presenter claims: ~$33K/mo AdSense on main channel; ~$37K/mo on a 10K-views/mo second channel (~$3,700 per 1,000 views — vs "~$5/1K" for entertainment channels). Testimonials (all unverifiable): French-dads fitness "8 figures/yr"; Ivy-admissions student $80K/mo; options-trading creator $700K/mo; Thomas Frank Notion templates $100K/mo; accountant→controller coach $70K/mo; CAD-software course $12K in months; tinnitus/hearing-aid reviews $1,500/mo under 500 subs; solar installer $500K/yr in contracts; brother $214 in one day 29 days in; $106K contract from a 1,500-sub channel. No receipts shown for any.
- **Replication steps:**
  1. Apply three filters to your own history — problems you've overcome, content you binge-consume, what people ask your help with — writing 5+ items each (goal: 3-5 niche ideas).
  2. Dig with two frameworks: the "time machine" (what would you tell your younger self?) and Naval's "feels like play to you, looks like work to others."
  3. Run the free Claude "niche validator" skill — an interview-style prompt that keeps asking until specifics (e.g., "foreign exchange student who got into an elite US university") surface; feed it messy, detailed answers.
  4. Gut-check the shortlist: does it touch wealth, health, or relationships? Avoid gaming/entertainment/vlogs/under-18 audiences unless selling cheap mass-market goods.
  5. Confirm money potential: audience with disposable income + a monetization ladder beyond AdSense (digital products $50, courses $200-2K, coaching $500-5K, memberships $20-200/mo).
  6. Ship content on 3-5 ideas and let the market pick; treat "you are the niche" as permission to pivot later.
- **Automation potential:** 4/10 — the "Claude AI" is a structured interview prompt, not analysis; niche selection is inherently personal. Downstream content production is automatable, but that isn't what's taught; the funnel itself (waitlists, booking calls) is partially automated.
- **Quality:** 3/10 — underlying advice is coherent and standard (specific beats broad, money audience beats big audience, monetize beyond ads) and the method itself is given away free. But every income figure is an unverified testimonial, the $3,700/1K-views RPM conflates product revenue with view counts, the Claude angle is prompt theater (an LLM interviewing you ≈ a good worksheet), and the video's true job is funneling to high-ticket coaching.
- **Verdict:** Mixed
- **Key actions:**
  - Skip the funnel; keep the framework — "specific expensive problem + audience with money + monetization beyond ads" is a decent positioning test for any content/lead-gen play we run.
  - Note the tactic, not the course: a free Claude skill as a lead magnet is a cheap, replicable list-builder worth borrowing for our own funnels.
  - Don't bank the testimonial numbers; if any cite matters later (e.g., Thomas Frank Notion templates), verify independently.
- **Red flags:** Course-funnel architecture end to end (scarcity "5 seats," "18% acceptance," "expensive" 1-on-1); zero receipts for income claims; implausible AdSense RPM presented as normal; AI framed as magic when it's an interview prompt; "hundreds of comments love it" social-proof assertions.

### Video 5: 12,000 Subscribers → Five-Figure Brand Deal *(creator monetization)* {#video-5}

> ▶ Watch: https://youtu.be/CzUadSAaNB8


- **Business model:** Personal-brand creator in the video-editing education niche. Guest Daniel Batal (~580K subs, 83M+ views) built authority via tool-tutorial series ("Filmora tutorials", then "DaVinci Resolve for Noobs" shorts series) and monetizes audience *connection* through direct-negotiated annual brand ambassadorships (Filmora → DaVinci Resolve), plus AdSense, coaching/consulting, and event speaking. Core pitch: sponsors buy connection, not reach — so even ~12K subs can command five figures.
- **Revenue model:** DaVinci Resolve deal: "very strong six-figure year" sponsorship (current flagship). First Filmora deal: five figures/year, signed at ~12K subs after a 3–4 page proposal. AdSense: best year ~$25K pre-tax; hundreds of shorts with tens of millions of views earned only ~$5–6K total — deliberately de-emphasized. Framework: 10 revenue streams × $10K = $100K/yr. Coaching-client proof: BBQ channel with ~2,000 subs signed 7 ambassador deals totaling ~$30K/yr after his outreach playbook.
- **Replication steps:**
  1. Pick one tool/skill you're actively learning and build a branded, repeatable series around it (e.g., "<Tool> for Noobs" shorts) so you become the discoverable authority for that tool.
  2. Post consistently across all four YouTube formats (long-form, shorts, live, community) — 2–3×/week — optimizing for connection and returning viewers, not raw CTR.
  3. Collect channel evidence: 90-day growth trajectory, views/comments/shares trends, retention, and a 12-month projection.
  4. Write a 3–4 page sponsorship proposal: your data + exactly what you'll deliver (integrations, livestreams, series) + annual term with a lock-in-now discount argument; make "yes" effortless.
  5. Create competitive tension (a second interested brand) and pitch the brand's marketing contact directly — negotiate an annual ambassadorship, refuse affiliate-link-only offers.
  6. Stack ~10 independent five-figure revenue streams (sponsorships, AdSense, coaching, speaking) toward $100K/yr instead of relying on AdSense.
  7. Use AI/vidIQ to draft the analytics-based proposal, then humanize it before sending.
- **Automation potential:** 3/10 — AI can draft the proposal, but the entire moat is months/years of on-camera content and genuine audience connection; nothing here is faceless or hands-off.
- **Quality:** 6/10 — named verifiable brands (Filmora, Movavi, DaVinci Resolve) and a real, long-track-record creator lend credibility, and details are internally consistent; but all figures are self-reported on a coaching-selling podcast with no dashboards/screenshots, and the $30K client story is secondhand.
- **Verdict:** Worth Trying (for anyone already creating content; it's a slow grind — 8 years, full-time leap in year 2 — not a fast-money play)
- **Key actions:**
  - Launch a single-tool tutorial series with a sticky name; treat it as the brand asset sponsors will buy into.
  - Build the data-backed 3–4 page proposal template (trajectory + projections + deliverables + annual-pricing lock) — reusable for any niche.
  - Pitch annual ambassadorships directly to brand marketing teams; leverage competing offers; walk away from product-for-video/affiliate-only deals.
  - Diversify beyond AdSense (which caps low for short-form-heavy channels) into sponsorships + services/coaching.
- **Red flags:**
  - No dashboards or screenshots; "six-figure year" is unverifiable podcast talk from a host who sells coaching mid-episode.
  - Survivorship bias: the playbook took 8 years and a construction-business exit; most channels quit long before sponsorship leverage materializes.
  - Niche dependence: video-editing software has unusually rich brand budgets; a reaction/vlog channel can't replicate this CPM pool.
  - Demonetization risk acknowledged for repetitive/short-form-heavy channels (his own shorts series earned ~$5–6K despite tens of millions of views).

### Video 6: Faceless Channel $39K With Claude + ChatGPT *(faceless AI content)* {#video-6}

> ▶ Watch: https://youtu.be/8Rf0xna31xg


- **Business model:** Faceless YouTube Shorts channel in the "interesting facts" micro-documentary niche (30-second AI-narrated explainers: history, science, mystery). Full AI production pipeline: ChatGPT for channel branding, Claude + free vidIQ connector for competitor analysis/topic research/scripting/scene planning, and "Rank Reel" for AI voiceover, stock/AI-generated clips, captions, and rendering. Revenue = pure Shorts ad RPM at massive view scale; the video itself monetizes via tutorial audience (likely affiliate links "linked below").
- **Revenue model:** No receipts — all figures are VidIQ *estimates* of third-party channels: ~$40K/90 days from 250M views ("almost $40,000"), ~$25K and ~$33K for two other tracked channels; one at 2B views/365 days ≈ $170K estimated. Air Media Tech benchmark: Shorts RPM 7–20¢/1K views, ~33¢/1K US-heavy (so 100M views ≈ $33K). Own earnings: none given.
- **Replication steps:**
  1. Pick an "interesting facts" niche (history/space/mystery/tech); watch the niche's Shorts feed to surface 3–5 top competitor channels.
  2. In Claude, connect the free vidIQ Chrome extension/connector, paste each competitor's channel ID, and run "competitor breakdown" — extract the 5 best-performing video topics with links.
  3. Prompt Claude to turn a proven topic into an original ~30-second script, then a second prompt to break it into scene-by-scene visuals with timestamps.
  4. In Rank Reel: paste script → pick an AI voice → generate voiceover; fill each scene with matching stock footage or AI-generate clips (9:16); trim to Claude's timestamps; auto-generate and style captions; render/export.
  5. Set up the channel: prefer repurposing an aged account, or warm up a new one (30 min/day of normal Shorts browsing, likes, comments, subs for ~2 days), verify phone, enable standard/intermediate features.
  6. Use ChatGPT for branding: one-word name, simple readable logo, matching banner, channel description — 4 quick prompts.
  7. Post, then repeat the loop on topics that get views: "find what's working, make your own version, post, repeat more of what works."
- **Automation potential:** 9/10 — research, scripting, scene planning, voiceover, visuals, and captions are all AI-generated; only clip selection, trimming, and posting are manual. This is a genuine near-end-to-end content pipeline.
- **Quality:** 3/10 — zero receipts: every dollar figure is a VidIQ estimate of anonymous third-party channels, no dashboards, no named owners, no own-earnings proof; classic numbers-to-credibility inversion. The workflow demo itself is real and concrete, which keeps it from scoring 1–2.
- **Verdict:** Mixed — the AI production pipeline is genuinely replicable and highly automatable, but the revenue story is estimate-only, success requires ~100M+ views per quarter (extreme outlier), and the format sits squarely in YouTube's "farmed content" demonetization pattern.
- **Key actions:**
  - Steal the Claude + vidIQ competitor-analysis workflow for any content research task (works beyond facts-shorts: it surfaces proven topics with real view data in minutes).
  - If attempting the model, budget for RPM reality: at 33¢/1K, $10K/month needs ~30M views/month — plan volume and niche (US-heavy audiences) accordingly.
  - Reuse an aged channel or run the 2-day account warm-up before posting to reduce new-account friction.
  - Never rely on Shorts ad revenue alone — pair the pipeline with sponsorships/products (per Video 1's model) since ~$5–6K per 100M shorts views is the realistic AdSense ceiling.
- **Red flags:**
  - All revenue = third-party VidIQ estimates, explicitly worded "estimated revenue" — no verified income anywhere in the video.
  - Survivorship outliers presented as opportunity: 250M views/90 days is top-0.01% performance, framed as "one of the biggest opportunities on the internet."
  - Direct demonetization exposure: AI voice + similar-format high-volume shorts is precisely the farmed-content pattern Video 1 says YouTube's AI bots are demonetizing en masse ("sometimes unfairly" for legitimate creators — this model isn't that).
  - Undisclosed affiliate incentive: "everything I showed you is linked below" — the tutorial likely earns from Rank Reel referrals regardless of viewer outcomes.
  - Google Trends "search interest at 5-year low" is spun as proof the niche is open, when it equally signals fading hype (and tutorial demand).

## Final Ranking (by automation potential)

1. WebMCP agent-readiness — 9/10 · Worth Trying · **best buildable artifact**
2. AI Hedge Fund orchestration — 9/10 · Mixed (pattern, not P&L)
3. Faceless AI Shorts pipeline — 9/10 · Mixed (demonetization-exposed)
4. Claude→Shopify Liquid — 7/10 · Mixed (service play, not dropshipping)
5. Shane Hummus niche funnel — 4/10 · Mixed
6. Brand-deal proposals (Batal) — 3/10 · Worth Trying

## Cross-Video Synthesis

**The agent-readiness ladder now has four rungs in the archive:** GEO/AEO citations (09-09: Bauman) → journey completion (today: WebMCP) → payment rails (a16z agentic payments) → agent-native vertical software (Slowbooks). WebMCP is the first *live, cloneable protocol* in that stack — the arbitrage window is "experimental flag" status, same shape as early SEO.

**Cross-video contradiction of the day:** Batal says YouTube is demonetizing high-volume AI-shorts accounts; the faceless-shorts video teaches exactly that model as "one of the biggest opportunities on the internet." Both can't be right; the archive's demonetization-risk flag goes to the shorts model.

**Receipts ledger stays inverted:** zero verified P&L in six videos. The most credible number is Batal's ~$5–6K AdSense per 100M shorts views — used to *demosuade* AdSense dependence. Steal patterns (info-asymmetric agents, blind backtests, WebMCP manifests, annual brand proposals), ignore the dollar claims.

**Do this week:** clone WebMCP demo repo + expose one tool on our own site; run the internal agent mystery-shopper eval; steal the Claude+vidIQ research loop for playlist pipeline research.
