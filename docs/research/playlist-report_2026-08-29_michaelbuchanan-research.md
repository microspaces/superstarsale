# Playlist Research — Michael Buchanan's "Research" Playlist (2026-08-29)

**Source playlist:** ["Research" by Michael Buchanan](https://youtube.com/playlist?list=PLamiZQJOzMbY) (`PLamiZQJOzMbY`)
**Special run:** playlist-targeted analysis (not the search-based daily job).
**Coverage:** 4 videos in playlist. 4 full English transcripts fetched. 0 blocked.

## Videos Analyzed

| # | Title | Channel | Views | Length | Transcript |
|---|-------|---------|-------|--------|------------|
| 1 | I Did Something Insane. Here Are the Businesses I Found in It (Chris Koerner) | The Koerner Office Podcast | ~22k | 28:06 | Yes |
| 2 | His project went viral this week | The Next New Thing | ~10k | 17:32 | Yes |
| 3 | She Made $7M in 2 Days from Instagram… Here's How (Jessi Jean Interview) | ManyChat | ~52k | 60:32 | Yes |
| 4 | I Cloned Podium's Business Model — Here's the Blueprint | John Whitford | ~3.1k | 14:41 | Yes |

---

## Video 1: The Koerner Office — "I Did Something Insane. Here Are the Businesses I Found in It"

**Story:** Chris Koerner bought a 231-acre cattle ranch ~45 minutes from his DFW home for ~$10,300–$10,500/acre (~$2.4M), negotiated "almost $400 grand off" list on a non-distressed property. The video is a teardown of every business idea he found during six months of diligence.

**Deal mechanics (the real playbook):**
- Used Claude ($20/mo) to pick apart the seller's appraisal — it flagged comps based on 60-acre parcels vs. his 231 acres ("the bigger the parcel, the cheaper per acre"). His words: Claude alone "saved me hundreds of thousands of dollars."
- Local farm-credit bank financed 85% at ~6.7%, 20-year amortization, 5-year ARM. Closing ~2 months. Own appraisal came in above purchase price.
- Texas ag exemption = property taxes ~97% lower ($1,500/yr vs $45–50K/yr on a $2M ranch). Lapse the exemption and the county claws back back taxes — a real compliance trap.
- Wife got her real estate license (~$1K, tens of hours) → 3% commission kickback; they gave back 2% ($50K) at closing as negotiating leverage.
- Floodplain land valued ~$5K/acre vs $15–16K non-floodplain — price it as a blend; cows graze both.
- Seller picked him because he isn't a developer — identity/relationships as a discount mechanism. Kept the existing tenant on the 2,400 sq ft shop at below-market rent: "You don't want to make enemies right when you buy."
- Thesis: DFW adds 150–200K people/year; ranch is 57 miles from downtown, in the path of growth, near a rail-trail becoming a state park (rail-trail adjacency historically outperforms).

**Business ideas surfaced:**
1. **Grass-fed beef shares without owning land** — buy/earmark calves from a rancher, book the slaughterhouse months out, sell quarters: ~$12/lb × 125 lbs ≈ $1,500/quarter, $6K/whole cow, ~40% net margin. "ButcherBox and Snake River don't own cows."
2. **Grazing lease** — seller keeps ~85–100 cows and pays a nominal monthly fee; calves (~$1,400 each at 500–600 lbs at auction) stay his. Pure passive land income.
3. **Own the heavy equipment** — dozers $10–30K, dump trucks $5–15K at auction; hired operators $20–50/hr vs $200–500/hr for a company. Buddy paid $125K to dredge a pond — could have bought the equipment, done the work, and sold it.
4. **Heavy equipment flipping** — a guy he knows buys at auction and resells "without ever taking delivery."
5. **Pond database** — ~800,000 farm ponds in Texas, no public database. GIS + satellite imagery + AI agents could build it; monetize via fishing-access marketplace and leads for pond management/dredging companies. "It's data. You can do whatever you want with data."
6. **Farm stays / tiny homes** — neighboring 20-acre parcel runs 14 tiny homes at $1,450/mo, fully occupied ≈ $17–18K/mo. Plus Hipcamp, RV sites, a glass-floor "bridge Airbnb" over the river.
7. **Rent-to-own land + portable storage** — his Canadian friend leases highway-front raw land cheap, drops portable storage units, proves the model, then exercises the option to buy. "It's always worked out."
8. **YouTube channel (Triple 8 Ranch)** — leverages learnings (hooks, thumbnails, retention) rather than his existing audience; goal: cover the ranch payment within a year.
9. Shop rent, depreciation/tax benefits, hunting leases (explicitly not bullish — liability).

**Automation Potential: 5/10** — Land itself is passive-appreciating; the operating businesses (beef, equipment, stays) are semi-passive once systematized but need labor or operators.

**Quality Score: 8/10** — Real numbers everywhere (price/acre, tax deltas, per-cow economics, hourly rates), honest about risk ("either I bought the dip or I bought at a bad time — I won't know for years"). Two ad reads (Bizee, channel membership) but the core content is ungatekept.

**Verdict: Strong** — Not a copyable recipe for most (capital-intensive), but the single best source in the playlist for asset-light spinoffs: beef shares, equipment flipping, land-lease storage, and the pond database each stand alone.

---

## Video 2: The Next New Thing — "His project went viral this week"

**Story:** Interview with Jonathan (maker of Superstarter, a SaaS boilerplate selling at $349) about outbid.lol — a pay-to-rank leaderboard built with Cursor in ~3 hours that has done $212K.

**The mechanic:** Outbid anyone by $1+ to take their rank. #1 rank cost $17,005 (paid by seed.io) at interview time. Site did 3.3M visitors in 5 days; launch tweet hit 4.4M impressions; $21K revenue in the first 24 hours. Buyers get attention: Crowd Reply claims ~50 demo calls from a top-10 link.

**The flywheel:** Every new leaderboard entrant got reposted on X with their link → more traffic → higher rank value → higher bids → more posts. Payment isn't bolted on; payment IS the product.

**Notable quotes/numbers:**
- "99% luck with just 1% execution."
- He stayed up to 2:30 AM shipping it; expected top rank "at a few hundred bucks."
- Didn't know the Million Dollar Homepage existed — "if I had known, I probably wouldn't have launched this."
- Superstarter pricing journey: launched at $20–49, now $349, "and I still think that is too low."
- 85+ clones appeared — he says clones increased the hype.

**Operational lessons (the underrated part):**
- Payment platform risk: Polar (merchant-of-record, handles international sales tax) doesn't allow this business type in its policies — he's evaluating Stripe. MoR convenience vs. ToS/platform risk is a real tradeoff.
- A botnet DDoS hammered the site overnight; Vercel spend limits auto-paused it; Vercel reacted, refunded, CEO stepped in. Spend limits saved him from a catastrophic bill.
- Analytics (The Metrics) crashed at 400K visitors/hour from Hacker News; switched to DataFast, whose live API now powers the on-site visitor counters.
- Workflow: Cursor plan mode + Matt Pocock's "grill me" skill to interrogate the spec before building; voice-prompted the original spec (Next.js + shadcn/ui + Polar).

**Automation Potential: 9/10** — The entire business is software; one person, no inventory, no support staff mentioned.

**Quality Score: 8/10** — Public revenue stats on the site itself, specific failure modes (DDoS, payments, analytics), honest luck attribution. Sponsor reads (Zapier, Cursor) but they're woven into the actual workflow shown.

**Verdict: Strong as a pattern, weak as a plan** — You can't copy the luck, but the pattern is replicable: tiny payment-native mechanic + public leaderboard + build-in-public distribution loop + spend limits. Expect most attempts to earn ~$0; the tail pays for all of them.

---

## Video 3: ManyChat — "She Made $7M in 2 Days from Instagram… Here's How"

**Story:** Jessi Jean interview. Started a fresh Instagram account Nov 2025 documenting being "career confused" (after a 7-year binge-eating-recovery business that did "a few million"). Furniture flipping + oversharing finances → pivoted into teaching what was resonating: talking direct to camera ("yapping"). Launched the YAP Challenge in May.

**Numbers:**
- Launch 1: $1.2–1.3M, 4,500 students (she'd projected $100–200K).
- Launch 2, three weeks later: $5.5M+ — driven by 4,500 satisfied students posting organically ("marketing you can't pay for").
- Total: $7.4M in 10 weeks, ~25,000 students, $0 in ads, all organic.
- Costs: a 1099 assistant + $2K/mo business coach. "Very, very lean."
- Sales page converted >15% vs a 4–6% industry standard.
- Reps: ~170 posts in 8 months, 5–10 takes per post ≈ 800+ videos recorded.

**Playbook details:**
- **Validate before building:** waitlist sold first, course built LIVE during the 11-day open cart. "A lot of creators get it backwards — they spend all this time building and then go look for people to buy it." She didn't sleep for ~8 weeks, but says the live build made the product better.
- **DM-native capture (ManyChat):** comment "yap" → auto-DM → capture email inside the DM → checkout link in-thread. No link-in-bio hop. "Attention does not equal currency… you have to know how to capture it." Large share of sales happened in DMs.
- **Double down on resonance:** when communication posts popped, she ran the topic dry instead of moving on. "The things that are too obvious to you are valuable to people who don't know them yet."
- **Radical directness:** "My intention with posting is to make money… I'm here to make money for my son." In "the age of distrust," declaring intent + disclosing bots/paid posts built trust rather than eroding it.
- **Courses vs AI:** "Information is abundant, but people still buy into communities" and trust humans more than AI output.

**Automation Potential: 7/10** — Funnel, DM capture, and email are automated; the moat is 800+ reps of an unautomatable skill (on-camera presence) plus community energy during launch windows.

**Quality Score: 7/10** — Verified-feeling numbers, full-funnel transparency (she shares a launch debrief with expenses inside the challenge). Caveat: it's on ManyChat's channel — effectively a long-form case study for their product; and the outcome is a massive outlier from a creator with 10+ years of prior audience/business skill.

**Verdict: Strong** — The most complete launch anatomy in the playlist: audience signals → waitlist → live-built challenge → DM-native checkout → testimonial flywheel → immediate relaunch. The skill (talking to camera) is free to start practicing today.

---

## Video 4: John Whitford — "I Cloned Podium's Business Model — Here's the Blueprint"

**Story:** Clone Podium (local home-services software: unified inbox, review requests, AI phone answering, web chat, SMS) — a $3B-valuation (Nov 2021) company with an estimated ~$400M 2023 revenue charging $399/mo (core) and $599/mo (pro, per location).

**The blueprint:**
1. White-label an existing SaaS platform (he shows a "SaaS configurator" inside his own tool, FreedomKit — he claims 2,500+ sub-accounts and a 2024 "diamond level" award for 1,000+ paying clients; the platform is HighLevel-style reselling).
2. Rebrand a pre-built website template (he gives one away).
3. Configure plans: $399/mo core (CRM, unified inbox, SMS), $599 pro tier with AI features, 7–14 day trials, annual discount.
4. Sell to local service businesses; setup takes "less than 30 minutes per client."

**The math to $500/day:** 5 clients/week at $399/mo with 20% weekly churn → ~12 clients by end of month 1 ($4,788 MRR ≈ $159/day) → cross $500/day (~$16K MRR) before week 10 → at 100 clients, $1,330/day / $40K/mo. Real expenses: platform fee + maybe 1–2 assistants (or AI support).

**Automation Potential: 7/10** — Software is already built; recurring revenue; the human work is sales and onboarding, which he says is a few hours/day at the target pace.

**Quality Score: 5/10** — He's a real operator with verifiable award tiers, and the model is proven (Podium, plus the white-label vendor's public awards pages). But: this is an affiliate funnel — every resource gates behind subscribe/like/comment, and the income math assumes a beginner consistently signing 5 clients/week, which is the actual hard part, glossed in "day-by-day training." 20% weekly churn in the model is framed as conservative but would be catastrophic in reality if adds ever slowed.

**Verdict: Viable with heavy caveats** — The mechanics are real and the recurring-revenue chassis is sound (it matched the #1 strategy in the 2026-08-28 playlist report: white-label vertical SaaS). Success depends entirely on distribution to local businesses, which the video doesn't teach.

---

## Cross-Playlist Ranked Strategies

### 1. Pay-to-rank attention marketplace (outbid.lol pattern)

**Why ranked #1:** Best effort-to-upside ratio in the playlist — 3 hours of vibe-coding → $212K. Payment is native to the mechanic (no monetization step), the leaderboard creates self-reinforcing distribution (every buyer promotes you), and build cost is near zero with AI coding tools.
**Reasoning:** The pattern generalizes beyond leaderboards: any "public status + pay to enter/jump" surface (directories, walls, maps, countdowns) inherits the flywheel. The video also delivers the risk syllabus: payment-provider ToS (Polar kicked him off), DDoS/hosting bills (spend limits saved him), analytics collapse at scale, and 85+ clones.
**Actionable takeaways:**
- Build payment-native micro-mechanics, not free tools with ads bolted on later.
- Make every customer's purchase publicly visible — that's your distribution.
- Set infra spend limits on day one; expect and survive the botnet.
- Pick a payment provider whose ToS actually allows your mechanic, or go Stripe and own the tax complexity.

### 2. Viral challenge launch with DM-native capture (Jessi Jean pattern)

**Why ranked #2:** Highest documented revenue in the playlist ($7.4M/10 weeks, $0 ads) and the most replicable *system* even if the outcome isn't replicable: listen for resonance → waitlist → sell before building → build live → capture emails inside DMs → let satisfied students market launch 2.
**Reasoning:** Two structural insights beat the income claim: (1) "attention does not equal currency" — capture friction (link-in-bio hops) is where conversions die, and >15% sales-page conversion came from DM-native flow; (2) in an AI-saturated feed, declared intent and disclosed automation outperform performed authenticity.
**Actionable takeaways:**
- Start the reps now: daily direct-to-camera posts; voice is a trainable habit, not a gift (news anchors rehearse; teleprompters are fine).
- When a post topic pops, double down until it's dry — that's your product market.
- Sell the waitlist before building the course.
- Put email capture inside the DM thread, not behind a bio link.

### 3. White-label vertical SaaS — "clone Podium" (Whitford pattern)

**Why ranked #3:** Proven, beginner-accessible recurring revenue with the software already built; Podium's $399/mo pricing proves willingness-to-pay in local services. Ranked below the top two because the hard part (local-business distribution) is unaddressed, and the promoted math (5 clients/week) hides the grind.
**Reasoning:** Same chassis as the 2026-08-28 report's #1 (HighLevel white-label to one vertical). The edge isn't features — it's picking one niche (roofers, med spas, HVAC) and selling the outcome (missed-call text-back, reviews), not "AI."
**Actionable takeaways:**
- Price at $197–$497/mo, never at cost-leader $97.
- Clone from public award winner lists instead of inventing a niche.
- One killer workflow demo > full feature matrix.
- Assume churn; the business only works if sales never stop.

### 4. Asset-light land/ranch arbitrage (Koerner spinoffs)

**Why ranked #4:** The land deal itself needs capital, but four spinoffs don't: (a) beef shares with ~40% margins and zero land ownership — buy from ranchers, book slaughter slots early, sell quarters at ~$12/lb; (b) heavy-equipment flipping at auction, never taking delivery; (c) rent-to-own highway land + portable storage — prove the business before exercising the option; (d) grazing/shop leases as passive land income.
**Reasoning:** Each is a real business with real unit economics stated on-screen. The umbrella lesson: negotiation (Claude-vs-appliance-sized parcel comps), tax structure (ag exemption = 97% off property tax), and relationship capital (seller discount for non-developers) are where land money is actually made.
**Actionable takeaways:**
- Run any appraisal through an LLM with the comps attached — parcel-size mismatch is a systemic appraisal flaw.
- Get the real estate license before buying; the 3% kickback funded 2% of his negotiation.
- Talk to a farm-credit lender, not a residential bank, for raw land.
- Test land-based business models on leased land (farmers lease 20 acres for low hundreds/month) before buying.

### 5. Niche data monopoly — the pond database (speculative)

**Why ranked #5:** ~800K Texas farm ponds, no public database, and GIS/imagery/AI agents make compilation feasible for the first time. Monetization is multi-door (fishing-access marketplace, leads for dredging/management companies, insurance/real estate data). Ranked last because it's an unexecuted idea — zero revenue proof in the video.
**Actionable takeaways:**
- Data no one has compiled + obvious buyers of leads = classic unboring boring business.
- Satellites + AI agents have collapsed the cost of building niche geodatabases; the moat is distribution to the buyers, not the data itself.

---

## Recommendations for SuperStar Sale

1. **Prototype a payment-native micro-mechanic** (Strategy 1). The outbid pattern is a weekend build with AI tools; the downside is a few hours, the tail is six figures. Document the build publicly — the documentation IS the distribution.
2. **Adopt DM-native email capture everywhere** (Strategy 2). Whatever SuperStar Sale sells, moving capture into the DM thread is the single highest-leverage funnel change demonstrated in this playlist (>15% vs 4–6% conversion).
3. **Keep white-label SaaS on the roadmap as the recurring-revenue chassis** (Strategy 3), but budget for distribution (niche selection + outreach) as the primary cost, not setup.
4. **Logistics edge case worth tracking:** beef shares and pond-lead marketplaces are both lead-gen businesses in unglamorous niches — the "boring is a moat" thesis from the 2026-08-05 report appears again here from the opposite direction.

---

*Research generated from 4 YouTube videos with full transcript analysis*
*Playlist: "Research" by Michael Buchanan (PLamiZQJOzMbY) — special run, not the daily search job*
*Data collected: 2026-08-29 (PDT)*
*Report generated: 2026-08-29*
