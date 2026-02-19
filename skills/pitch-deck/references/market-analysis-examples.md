# Game Market Analysis Reference

How to research, construct, and present credible market analysis for game
pitches. This guide covers TAM/SAM/SOM methodology, data sources, revenue
estimation, comparable title analysis, and trend identification.

---

## 1. TAM / SAM / SOM for Games

### Definitions

| Term | Meaning | Question It Answers |
|---|---|---|
| **TAM** (Total Addressable Market) | The total global revenue for your broad game category | "How big is the entire pie?" |
| **SAM** (Serviceable Available Market) | The segment you can realistically reach (your platforms, regions, sub-genre) | "How big is the slice you could theoretically serve?" |
| **SOM** (Serviceable Obtainable Market) | The revenue you can realistically capture in year one | "How big is the bite you can actually take?" |

### How to Calculate Each

#### TAM

Start with the broadest relevant category. For Infinite Voyage:

```
Global RPG market (PC + console + mobile): ~$18B annually
Source: Newzoo Global Games Market Report, 2024
```

TAM is impressive but meaningless on its own. It establishes that the
category is large enough to support your game.

#### SAM

Narrow by platform, sub-genre, and region:

```
Narrative/story-driven RPGs on PC and console (global): ~$2.5B annually

Breakdown:
- PC (Steam + Epic + GOG): ~$1.4B
- Console (PlayStation + Xbox + Switch): ~$1.1B

Sources:
- VG Insights (Steam revenue estimates)
- NPD/Circana (console sales data)
- SteamDB genre tag revenue aggregation
```

#### SOM

Estimate your realistic first-year revenue using comparable titles:

```
Conservative estimate: $3M (based on lower-performing comparable titles)
Mid estimate: $8M (based on median comparable performance)
Optimistic estimate: $18M (based on breakout comparable titles)

Method: Median first-year revenue of 5 comparable titles (see Section 5)
adjusted for team size, marketing budget, and platform mix.
```

### Presenting the Funnel

Always present TAM > SAM > SOM as a visual funnel or nested circles.
This shows intellectual honesty. Showing only TAM is a red flag that signals
you have not done the work.

```
TAM: $18B (Global RPG Market)
  SAM: $2.5B (Narrative RPGs, PC + Console)
    SOM: $3M-$18M (First-year target)
```

---

## 2. Data Sources

### Steam / PC

| Source | What It Provides | Cost |
|---|---|---|
| **SteamDB** | Player counts, review counts, price history | Free |
| **VG Insights** | Revenue estimates, genre breakdowns, tag analysis | Free tier + paid |
| **Steam Spy** | Ownership estimates, playtime, concurrent players | Free (limited) |
| **Gamalytic** | Revenue estimates, audience demographics | Paid |
| **SteamCharts** | Historical concurrent player data | Free |
| **Steam Store Tags** | Genre popularity by player-applied tags | Free (manual) |

### Console

| Source | What It Provides | Cost |
|---|---|---|
| **NPD / Circana** | US physical + digital sales data | Paid (expensive) |
| **GfK / ISFE** | European market data | Paid |
| **Famitsu** | Japanese market data | Free (limited) |
| **PlayStation Store / Xbox Store** | Bestseller rankings | Free (qualitative) |

### Mobile

| Source | What It Provides | Cost |
|---|---|---|
| **Sensor Tower** | Revenue estimates, download counts | Paid |
| **Data.ai (App Annie)** | Market intelligence, top charts | Paid |
| **Google Play / App Store** | Top charts, ratings | Free (qualitative) |

### Industry Reports

| Source | What It Provides | Cost |
|---|---|---|
| **Newzoo** | Global market sizing, forecasts, segments | Paid (summary free) |
| **SuperData (Nielsen)** | Digital revenue tracking | Paid |
| **GDC State of the Industry** | Developer surveys, trends | Free |
| **IGDA Developer Satisfaction Survey** | Team size, budget trends | Free |

---

## 3. Steam Market Data Patterns

Steam is the largest PC storefront and offers the richest public data.
Understanding its patterns helps you set realistic expectations.

### Revenue Estimation from Reviews

The widely-used Boxleiter method (refined by VG Insights):

```
Estimated gross revenue = review_count * average_price * multiplier

Multiplier ranges (varies by genre and price):
- High-engagement genres (RPGs, strategy): 30-50x
- Average genres: 20-40x
- Low-engagement genres (casual, puzzle): 50-80x

Example (Disco Elysium):
- ~55,000 Steam reviews (all time)
- $39.99 average price
- Multiplier: ~35x (narrative RPG)
- Estimated Steam gross: 55,000 * $39.99 * 35 = ~$77M lifetime Steam revenue
```

This is a rough estimate. Use VG Insights or Gamalytic for more refined data.

### Typical Revenue Curves

| Period | % of Lifetime Revenue | Notes |
|---|---|---|
| Launch week | 20-30% | Wishlists convert, initial press coverage |
| Month 1 | 35-50% | Word of mouth, streamer coverage |
| Months 2-6 | 15-25% | Steady decline, sale spikes |
| Months 7-12 | 5-15% | Major sales (Summer, Winter) |
| Year 2+ | 5-15% | Long tail, deep discounts, DLC halo |

### Wishlist Conversion

```
Typical Steam wishlist-to-purchase conversion: 10-20% at launch
Median: ~15%

If you have 100,000 wishlists at launch:
  Expected launch sales: 10,000-20,000 copies
  At $29.99: $300K-$600K launch revenue (gross, before Steam cut)
```

---

## 4. Console and Mobile Market Patterns

### Console

- Console games typically earn 40-60% of lifetime revenue in the first month.
- Physical retail adds 10-30% on top of digital, declining year over year.
- PlayStation typically accounts for 50-60% of third-party multi-platform
  console sales, Xbox 25-35%, Switch varies by genre.
- Console ports of PC indie games typically earn 0.5-1.5x the PC revenue.

### Mobile

- Mobile is F2P-dominated. Premium mobile games are a niche market.
- Premium mobile RPGs typically earn $1M-$10M lifetime (successful ones).
- F2P RPGs in the top 100 earn $10M-$500M+ annually.
- For a premium game like Infinite Voyage, mobile is a secondary market.
  Estimate mobile revenue at 10-20% of PC revenue if porting.

---

## 5. Comparable Titles Analysis

### How to Select Comparables

Choose 5-8 titles that share at least 3 of these attributes with your game:

1. Same primary genre (RPG)
2. Similar sub-genre (narrative-driven, exploration-focused)
3. Similar scope (indie/AA, not AAA)
4. Similar platform mix (PC + console)
5. Similar price point ($20-$40)
6. Released within the last 5 years
7. Similar team size and budget

### Comparable Analysis Template

For each comparable title, document:

```
Title: [Game Name]
Developer: [Studio]
Publisher: [Publisher or self-published]
Release Date: [Date]
Platforms: [PC, PS5, Xbox, Switch]
Price: [$X.XX at launch]
Genre Tags: [narrative RPG, exploration, sci-fi]
Metacritic: [Score]
Steam Reviews: [Count, % positive]
Estimated Revenue: [$XM lifetime, $YM first year]
Team Size: [X people]
Development Time: [X years]
Marketing Budget: [Estimate if known]

Key Strengths:
- [What this game does well]

Key Weaknesses:
- [Where it fell short]

Relevance to Our Game:
- [Why this is a valid comparable]

Lessons:
- [What we learn from this title's performance]
```

### Revenue Estimation for Comparables

Use multiple methods and triangulate:

1. **Review-based estimate** (Steam): reviews * price * multiplier
2. **VG Insights / Gamalytic** direct estimate
3. **Sensor Tower / Data.ai** for mobile
4. **Developer GDC talks** (some studios share revenue publicly)
5. **SteamDB owner estimates** (less reliable post-2018)

Always present a range, not a single number:

```
Outer Wilds estimated lifetime revenue:
  Low estimate: $25M (conservative multiplier)
  Mid estimate: $40M (median multiplier + console)
  High estimate: $55M (generous multiplier + all platforms + DLC)
```

---

## 6. Revenue Estimation Methods

### Bottom-Up Method

```
Revenue = units_sold * average_selling_price * (1 - platform_cut)

units_sold = wishlists_at_launch * conversion_rate
           + organic_sales_month_1
           + sale_event_units * num_sale_events
           + long_tail_monthly * remaining_months

Platform cuts:
  Steam: 30% (20% after $10M, 25% after $50M)
  Epic: 12%
  Console: 30%
  GOG: 30%
```

### Top-Down Method

```
Revenue = SAM * market_share_capture

For an indie narrative RPG:
  SAM: $2.5B
  Realistic capture: 0.1% - 0.5%
  Revenue range: $2.5M - $12.5M
```

### Comparable-Based Method

```
Revenue = median_comparable_revenue * adjustment_factors

Adjustment factors:
  Team experience: 0.8x (first game) to 1.2x (proven team)
  Marketing budget: 0.7x (minimal) to 1.3x (well-funded)
  Market timing: 0.8x (crowded release window) to 1.2x (clear window)
  Platform breadth: 0.8x (PC only) to 1.3x (PC + all consoles day one)
```

### Presenting Revenue Projections

Always show three scenarios:

| Scenario | Year 1 | Year 2 | Lifetime |
|---|---|---|---|
| Conservative | $3M | $1.5M | $6M |
| Base Case | $8M | $4M | $15M |
| Optimistic | $18M | $8M | $32M |

Explain assumptions for each scenario. Investors respect honesty about
uncertainty more than false precision.

---

## 7. Trend Identification

### Where to Spot Trends

1. **Steam tag growth:** Track which tags are growing in number of games
   and revenue (SteamDB, VG Insights).
2. **GDC talks:** Developers share what is working and what is not.
3. **Streamer/content creator attention:** What are they playing?
4. **Wishlist surges:** Which unreleased games are gaining wishlists fastest?
5. **Game jam themes:** What are creators experimenting with?
6. **Award nominees:** What is being recognized by critics?

### Current Trends Relevant to Infinite Voyage

| Trend | Evidence | Relevance |
|---|---|---|
| Narrative RPG growth | Baldur's Gate 3 ($650M+), Disco Elysium ($85M+) | Validates demand for story-rich RPGs |
| Solo/small-team exploration games | Outer Wilds, Tunic, Cocoon | Exploration as a core verb is commercially viable |
| Player agency demand | Success of branching narrative games | Players want choices that matter |
| Cozy sci-fi emergence | Citizen Sleeper, In Other Waters | Not all sci-fi needs to be action-focused |
| Long-tail discoverability | Games earning 50%+ revenue after year 1 | Quality games sustain revenue through word of mouth |

### How to Present Trends

Show 3-4 trends with data points. For each:

1. **Name the trend** in a clear headline.
2. **Provide evidence** (sales data, growth metrics, specific examples).
3. **Connect to your game** ("Infinite Voyage rides this trend because...").
4. **Show growth trajectory** (year-over-year data if available).

---

## 8. Presenting Market Data Credibly

### Do

- Source every number (even "estimates" need a methodology)
- Show the funnel (TAM > SAM > SOM)
- Use conservative estimates as your baseline
- Acknowledge uncertainty ("estimated range of $X-$Y")
- Update data regularly (stale data undermines credibility)
- Show comparable titles with actual performance data

### Do Not

- Cite only TAM ("The gaming market is $180B")
- Use projections from 3+ years ago
- Cherry-pick only the most successful comparables
- Claim you will capture unrealistic market share
- Present a single revenue number without a range
- Ignore failed titles in your genre (survivorship bias)

### The Credibility Test

Before presenting market data, ask: "If I were the investor hearing this
for the first time, would I believe it or would I think this team is
delusional?" If the latter, revise your assumptions downward.

---

## 9. One-Page Market Summary Template

For the pitch deck, distill all market analysis into one slide:

```
MARKET OPPORTUNITY

TAM: $18B (Global RPG Market)
SAM: $2.5B (Narrative RPGs, PC + Console)
SOM: $8M (Year 1 Base Case)

Growth: Narrative RPGs growing 12% YoY
Trend: Post-BG3 audience seeking next deep RPG experience

Top Comparables:
  Outer Wilds — $40M+ lifetime
  Disco Elysium — $85M+ lifetime
  Citizen Sleeper — $5M+ lifetime

Our Positioning: Intersection of exploration + narrative + player agency
where no competitor currently dominates.
```
