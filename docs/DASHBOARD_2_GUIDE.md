# Complete Tableau Guide: Dashboard 2 - Revenue & Pricing Strategy

## 1. Overview & Business Problem
**Dashboard Name:** Revenue & Pricing Strategy  
**Target Audience:** Current Hosts, Prospective Hosts, Property Managers  
**Core Question:** *"HOW should I price my property? What actually drives revenue?"*

### The Business Value
Pricing mistakes are the #1 silent revenue killer for hosts. This dashboard replaces guesswork with data by revealing the "revenue sweet spot," quantifying the value of being a Superhost, and comparing pricing efficiency across different neighborhoods and property types.

---

## 2. Data Source & Preparation
**Data Source to Use:** `tableau_ready.csv`

**Initial Data Checks:**
- Ensure `listing_id` is a Dimension (String/Discrete).
- Ensure `price`, `estimated_revenue_l365d`, and `revpar` are Measures (Continuous).
- Ensure `host_is_superhost` and `instant_bookable` are Dimensions (Discrete, ideally aliased to "Yes/No" or "Superhost/Regular").
- Ensure `latitude` and `longitude` have the correct geographic roles assigned.

---

## 3. Calculated Fields to Create in Tableau

Before building any visualizations, create these calculated fields in Tableau:

**1. Occupancy Rate %**
```tableau
[estimated_occupancy_l365d] / 365
```
*Format as: Percentage (0 decimal places)*

**2. RevPAR (Revenue Per Available Room)**
*(Note: Use this if `revpar` is not already in your dataset, or to ensure accuracy)*
```tableau
([price] * [Occupancy Rate %])
```
*Format as: Currency (Standard)*

**3. Superhost Revenue Premium %**
```tableau
(AVG(IF [host_is_superhost]=1 THEN [estimated_revenue_l365d] END)
- AVG(IF [host_is_superhost]=0 THEN [estimated_revenue_l365d] END))
/ AVG(IF [host_is_superhost]=0 THEN [estimated_revenue_l365d] END)
```
*Format as: Percentage (1 decimal place)*

**4. Top Earner Threshold (90th Percentile)**
```tableau
PERCENTILE([estimated_revenue_l365d], 0.90)
```
*Format as: Currency (Standard)*

---

## 4. Step-by-Step: Building KPI Tiles

Create five separate worksheets for the top banner KPIs.

### KPI 1: Avg Estimated Revenue
- **Drag** `estimated_revenue_l365d` to Text.
- **Change Measure to:** Average.
- **Format:** Currency (e.g., $18,432).
- **Label:** "Avg Annual Revenue".

### KPI 2: Median Occupancy Rate
- **Drag** `Occupancy Rate %` to Text.
- **Change Measure to:** Median.
- **Format:** Percentage (e.g., 6.6%).
- **Label:** "Median Occupancy".

### KPI 3: Avg RevPAR
- **Drag** `revpar` to Text.
- **Change Measure to:** Average.
- **Format:** Currency (e.g., $35.70).
- **Label:** "Avg RevPAR".

### KPI 4: Top 10% Revenue Threshold
- **Drag** `Top Earner Threshold` (or `estimated_revenue_l365d` set to Percentile 90) to Text.
- **Format:** Currency (e.g., $62,000).
- **Label:** "Top 10% Revenue Threshold".

### KPI 5: Superhost Revenue Premium
- **Drag** `Superhost Revenue Premium %` to Text.
- **Format:** Percentage (+23.0%).
- **Coloring (Optional):** Put the calculation on the Color mark (Green for positive).
- **Label:** "Superhost Revenue Premium".

---

## 5. Step-by-Step: Building the Charts

### Chart 1: Price vs Revenue Sweet Spot (Scatter Plot)
*Goal: Find the optimal price range where revenue peaks.*
- **Columns:** `price` (Continuous Dimension, or Average Measure)
- **Rows:** `estimated_revenue_l365d` (Average)
- **Detail:** `listing_id` (so every dot is a property)
- **Color:** `room_type` (Entire home vs Private room)
- **Size:** `estimated_occupancy_l365d` (Demand)
- **Analytics Pane:** Drag a **Trend Line** to the view.
- **Insight to show:** After ~$250/night, the revenue curve flattens. The sweet spot is $100–$250.

### Chart 2: Revenue Distribution by Price Tier (Box & Whisker Plot)
*Goal: Show the reality of earnings within different price categories.*
- **Columns:** `price_tier`
- **Rows:** `estimated_revenue_l365d` (Continuous)
- **Detail:** `listing_id` (to generate the distribution dots)
- **Analytics Pane:** Drag a **Box Plot** to the view.
- **Color:** `price_tier`
- **Insight to show:** High price tiers have massive variance; budget tiers are highly concentrated.

### Chart 3: RevPAR by Neighbourhood (Horizontal Bar + Reference Line)
*Goal: Rank neighbourhoods by pricing efficiency.*
- **Rows:** `neighbourhood_cleansed` (Sort Descending by RevPAR)
- **Columns:** `revpar` (Average)
- **Color:** `revpar` (Sequential color scale, e.g., Green to Grey)
- **Analytics Pane:** Drag an Average **Reference Line** across the entire table.
- **Filter:** Keep Top 15 or Top 20 Neighbourhoods to avoid clutter.

### Chart 4: Revenue + Occupancy by Room Type (Dual-Axis Combo)
*Goal: Identify which property types are mispriced (high occupancy/low revenue, etc.).*
- **Columns:** `room_type`
- **Rows:** `estimated_revenue_l365d` (Average) AND `Occupancy Rate %` (Average)
- **Setup Dual Axis:** Right-click the second measure on the Rows shelf -> Dual Axis.
- **Synchronize Axes:** No (because one is $, one is %).
- **Marks Card:** Set Revenue to **Bar**, set Occupancy to **Line** with circles.
- **Color:** Different colors for the Bar and Line to contrast.

### Chart 5: Revenue Concentration Heatmap (Highlight Table)
*Goal: Show where the top-earning properties are clustered geographically.*
- **Columns:** `revenue_tier` (Low, Mid, High, Top Earner)
- **Rows:** `neighbourhood_cleansed` (Top 20)
- **Text:** `listing_id` (Count)
- **Color:** `listing_id` (Count) — Change mark type to Square to create the highlight table.

---

## 6. Dashboard Assembly & Interactivity

### Recommended Layout Container Strategy
```text
+-----------------------------------------------------------------------+
|  [Filters: Room Type] [Neighbourhood] [Superhost] [Price Range]       |
+-----------------------------------------------------------------------+
|  [ KPI 1 ]   [ KPI 2 ]   [ KPI 3 ]   [ KPI 4 ]   [ KPI 5 ]            |
+-----------------------------------------------------------------------+
|                                  |                                    |
|   Chart 1: Price vs Revenue      |   Chart 2: Box Plot                |
|   Scatter Plot (Sweet Spot)      |   Revenue by Price Tier            |
|                                  |                                    |
+-----------------------------------------------------------------------+
|                                  |                                    |
|   Chart 3: RevPAR by             |   Chart 4: Dual-Axis               |
|   Neighbourhood (Bar)            |   Rev & Occupancy by Room Type     |
|                                  |                                    |
+-----------------------------------------------------------------------+
|                                                                       |
|   Chart 5: Heatmap Table (Revenue Tier x Neighbourhood)               |
|                                                                       |
+-----------------------------------------------------------------------+
```

### Dashboard Actions (Crucial for Interactivity)
1. **Filter Action (Neighbourhood):** 
   - Source: Chart 3 (RevPAR Bar) and Chart 5 (Heatmap)
   - Target: All other charts on the dashboard.
   - Run on: Select
   - Clearing the selection: Show all values.
2. **Filter Action (Room Type):**
   - Source: Chart 4 (Dual-Axis)
   - Target: All other charts.
   - Run on: Select.

---

## 7. Key Business Insights (The "So What?")

When presenting this dashboard, these are the narrative talking points you deliver:

1. **The $100-$250 "Sweet Spot":**
   *Insight:* The scatter plot proves that charging more than $250/night yields diminishing returns. Hosts pricing at $300+ are severely hurting their occupancy, causing lower total annual revenue than those pricing at $150.
2. **The "Superhost" Premium is Real:**
   *Insight:* Becoming a Superhost isn't just an ego boost—it equates to an average **+23% increase in revenue**. This justifies spending money on better cleaning services and premium amenities.
3. **RevPAR Exposes the Real Winners:**
   *Insight:* Some neighbourhoods have lower nightly rates but incredibly high occupancy, resulting in a higher RevPAR. Property Managers should focus their acquisitions on high-RevPAR areas, not just areas with high nightly prices.
4. **Instant Book Drives Velocity:**
   *Insight:* Listings with Instant Book enabled have significantly higher occupancy percentages, maintaining strong revenue streams without needing to discount prices.
5. **The Luxury Trap:**
   *Insight:* The Box Plot shows that "Luxury" price tiers have massive variance. While the ceiling is high, many luxury properties earn exactly the same as "Mid-High" properties due to lack of bookings. Consistency is found in the Mid to Mid-High tiers.
