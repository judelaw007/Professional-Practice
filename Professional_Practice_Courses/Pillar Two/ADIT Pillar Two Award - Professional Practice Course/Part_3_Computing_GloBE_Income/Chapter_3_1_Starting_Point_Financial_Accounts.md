# Chapter 3.1: Starting Point—Financial Accounts

## Learning Objective

After completing this chapter, you will be able to identify the correct financial accounts to use as the starting point for GloBE Income calculations and navigate the hierarchy of accounting standard options.

## Introduction

The GloBE Rules' decision to anchor calculations in financial accounting rather than tax accounting represents one of the framework's most significant design choices. This approach reflects a pragmatic recognition: financial accounts are prepared consistently across jurisdictions using comparable standards, audited for reliability, and already available—whereas tax computations vary dramatically by country, use different bases, and would require harmonisation efforts beyond the scope of Pillar Two. By starting with Financial Accounting Net Income, the GloBE framework leverages decades of accounting standard convergence while making targeted adjustments for items where book treatment diverges from tax policy objectives.

## 1. The Starting Point: Financial Accounting Net Income or Loss

GloBE Income or Loss begins with **Financial Accounting Net Income or Loss** *(Article 3.1.1)*. This is the "below the line" net income or loss of the Constituent Entity—the figure after tax expense in the financial accounts.

**Critical distinction:** GloBE calculations use entity-level accounts, NOT the consolidated group accounts.

| Common Misconception | Correct Approach |
|---------------------|------------------|
| Use consolidated P&L for GloBE Income | Use each CE's individual P&L before consolidation eliminations |
| Group adjustments don't matter | Each CE's accounts must be evaluated separately |
| Errors that net to zero at group level are fine | Entity-level errors affect that jurisdiction's ETR |

The use of entity-level rather than consolidated accounts may seem counterintuitive—after all, the revenue threshold test and other scoping rules focus on consolidated figures. But this entity-level approach is essential to the GloBE framework's goal of measuring effective taxation jurisdiction by jurisdiction. Consolidated accounts eliminate intercompany transactions and present the group as if it were a single entity; such elimination would obscure the profit actually earned in each jurisdiction. By using pre-elimination figures, Pillar Two ensures that arm's-length intercompany transactions—properly priced and taxed locally—are captured in each jurisdiction's GloBE Income.

## 2. Article 3.1 Hierarchy

The GloBE Rules establish a hierarchy for determining which financial accounts to use:

```
┌─────────────────────────────────────────────────────────────────┐
│           Article 3.1 - Financial Accounts Hierarchy            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. PRIMARY RULE (Article 3.1.2)                               │
│     Use accounts prepared under UPE's accounting standard       │
│     BEFORE consolidation eliminations                           │
│                           │                                     │
│                           ▼                                     │
│  2. ALTERNATIVE (Article 3.1.3)                                │
│     If not "reasonably practicable" to use UPE standard:       │
│     → Use Acceptable Financial Accounting Standard, OR          │
│     → Use Authorised Financial Accounting Standard              │
│     Subject to conditions                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

This hierarchy reflects a tension in the GloBE framework's design: the desire for consistency (using one standard across all entities) versus pragmatism (not forcing costly conversions for every subsidiary). The primary rule—using the UPE's accounting standard throughout—ensures that profit recognition, expense timing, and valuation methods are comparable across the group, making jurisdictional ETRs genuinely comparable. But the alternative rule recognises that full accounting standard conversion is expensive and time-consuming; for newly acquired entities or those in jurisdictions with different statutory requirements, forcing immediate conversion would impose costs disproportionate to the benefit.

## 3. Step 1: Identify the UPE's Accounting Standard

### 3.1 Process

1. Obtain the UPE's consolidated financial statements
2. Identify the accounting framework used (typically stated in Note 1 or accounting policies section)
3. This becomes the "default" standard for all CE calculations

### 3.2 Common UPE Accounting Standards

| Standard | Typical Users |
|----------|--------------|
| IFRS | EU-listed companies, UK companies, Australian companies, many Asian groups |
| US GAAP | US-listed companies, US-headquartered MNEs |
| Japanese GAAP | Japanese groups not using IFRS |
| Swiss GAAP FER | Swiss companies (explicitly an Acceptable Standard) |

### 3.3 Stratos Example

Stratos Group plc prepares consolidated financial statements under **IFRS** (as required for UK-listed companies). Therefore, IFRS is the primary accounting standard for all Stratos CE GloBE calculations.

## 4. Step 2: Determine Each CE's Financial Accounts

### 4.1 The Primary Rule (Article 3.1.2)

For each Constituent Entity, use the **net income or loss determined in preparing the Consolidated Financial Statements** of the UPE, **before any consolidation adjustments eliminating intra-group transactions**.

**What this means in practice:**

| Item | Treatment |
|------|-----------|
| Intra-group sales | **Include** in CE's GloBE Income (not eliminated) |
| Intra-group dividends | **Include** initially (eliminated via Article 3.2 adjustments) |
| Intra-group interest | **Include** in CE's GloBE Income (not eliminated) |
| Management charges | **Include** in CE's GloBE Income |
| Purchase Price Allocation (PPA) adjustments | Generally **include** as reflected in consolidation |

### 4.2 Worked Example: Intra-Group Sale

**Scenario:** SG Germany GmbH sells software licences to SG France SAS for €5 million. In Stratos's consolidated accounts, this revenue is eliminated.

| Approach | GloBE Treatment |
|----------|-----------------|
| **Wrong:** Use consolidated accounts | Sale eliminated; German GloBE Income understated |
| **Correct:** Use pre-elimination accounts | €5M included in German GloBE Income; €5M cost in French GloBE Income |

**Result:** Each entity's GloBE Income reflects the arm's-length intra-group transaction.

The preservation of intra-group transactions in GloBE Income has profound implications for transfer pricing. If intercompany prices are set artificially—too high or too low—the resulting profit allocation will flow directly into jurisdictional ETRs. An inflated charge from a low-tax entity to a high-tax entity shifts profit to the low-tax jurisdiction; that shifted profit becomes GloBE Income in the recipient jurisdiction and may trigger Top-Up Tax. This creates a natural alignment between Pillar Two and transfer pricing compliance: groups with arm's-length pricing will see their GloBE Income appropriately distributed, while those with aggressive positions face potential Top-Up Tax on inappropriately shifted profits.

## 5. Step 3: Apply the Alternative Standard Exception (If Needed)

### 5.1 When Does Article 3.1.3 Apply?

The alternative standard exception applies when it is **"not reasonably practicable"** to determine a CE's Financial Accounting Net Income using the UPE's standard.

**Common situations:**

| Situation | Example |
|-----------|---------|
| Recently acquired entity | TechStart Ltd still maintains accounts under local Irish GAAP pending integration |
| Local statutory requirement | Japanese subsidiary required to file accounts under Japanese GAAP |
| System limitations | Legacy accounting system cannot produce IFRS-compliant reports |
| Materiality | Small entity where conversion cost exceeds benefit |

### 5.2 Conditions for Using Alternative Standard

If invoking Article 3.1.3, **three conditions must be met**:

| Condition | Requirement |
|-----------|-------------|
| 1. Maintained accounts | CE's financial accounts are **maintained** based on that alternative standard |
| 2. Reliable information | The information in those accounts is **reliable** |
| 3. Conform permanent differences | Permanent differences **exceeding €1 million** are adjusted to conform to UPE's standard |

### 5.3 The €1 Million Threshold

**Key rule:** If using an alternative accounting standard, any permanent difference exceeding €1 million must be adjusted to align with the UPE's accounting standard.

**What is a permanent difference?**
A permanent difference arises when the alternative standard treats an item differently from the UPE's standard in a way that will **never reverse**. This differs from a timing difference, which reverses over time.

| Type | Example | Treatment |
|------|---------|-----------|
| **Permanent difference >€1M** | Different revenue recognition principle resulting in €2M variance | **Must adjust** to UPE standard |
| **Permanent difference ≤€1M** | Minor difference in expense classification | **No adjustment** required |
| **Timing difference** | Different depreciation rates (IFRS vs local GAAP) | **No adjustment** required (reverses over asset life) |

### 5.4 Worked Example: Alternative Standard Application

**Scenario:** Stratos acquires TechStart Ltd (Ireland) on 1 July 2025. TechStart maintains accounts under Irish GAAP, which differs from IFRS.

**Step 1: Assess practicability**
- TechStart's systems are not yet integrated with Stratos's IFRS reporting
- Conversion to IFRS would require significant manual adjustment
- Conclusion: Not reasonably practicable to use IFRS for FY 2025

**Step 2: Verify conditions**

| Condition | Assessment |
|-----------|------------|
| Maintained accounts | Yes—TechStart prepares Irish GAAP accounts for statutory filing |
| Reliable information | Yes—accounts are audited |
| Permanent differences >€1M | One identified (see below) |

**Step 3: Identify and adjust permanent differences**

| Item | Irish GAAP | IFRS | Difference | Adjustment? |
|------|------------|------|------------|-------------|
| R&D costs | Capitalised and amortised | Expensed as incurred | €1.8M permanent | **Yes—adjust** |
| Lease accounting | Operating lease | IFRS 16 right-of-use | Timing difference | No |
| Revenue recognition | Similar to IFRS 15 | IFRS 15 | €0.3M | No (below €1M) |

**Result:** TechStart's Irish GAAP accounts are used, with a €1.8M adjustment for R&D treatment.

## 6. Acceptable vs Authorised Financial Accounting Standards

The GloBE Rules distinguish between two categories of alternative standards:

### 6.1 Acceptable Financial Accounting Standard *(Article 10.1)*

These are **specifically recognised** standards that can be used without additional adjustment for competitive distortions:

| Standard | Status |
|----------|--------|
| IFRS (as issued by IASB) | Acceptable |
| US GAAP | Acceptable |
| Swiss GAAP FER | Acceptable (explicitly listed) |
| Australian AASB standards | Acceptable (IFRS-based) |
| UK-adopted IFRS | Acceptable |

### 6.2 Authorised Financial Accounting Standard *(Article 10.1)*

These are **generally accepted accounting principles** in a jurisdiction that are authorised by an accounting standard setter or government. They are acceptable BUT may require adjustment for **Material Competitive Distortions**.

| Standard | Status | Notes |
|----------|--------|-------|
| Japanese GAAP | Authorised | Check for material distortions |
| Chinese Accounting Standards | Authorised | Check for material distortions |
| Indian GAAP (Ind AS) | Authorised | Largely IFRS-converged |
| Swiss Code of Obligations | Authorised | May have distortions vs IFRS |
| Irish GAAP (FRS 102) | Authorised | Largely UK GAAP aligned |

### 6.3 Material Competitive Distortion Test

When using an Authorised (but not Acceptable) standard, check whether application creates a **Material Competitive Distortion**:

**Definition:** A variation exceeding **€75 million** in a fiscal year between the authorised standard treatment and what IFRS would produce.

| Test | Threshold | Consequence |
|------|-----------|-------------|
| Material Competitive Distortion | >€75M aggregate variance | **Must adjust** to eliminate distortion |
| No Material Competitive Distortion | ≤€75M aggregate variance | No adjustment required |

**Note:** The €75M threshold applies at the MNE Group level, not per entity.

The distinction between "Acceptable" and "Authorised" standards reflects the reality of global accounting convergence—or its absence. IFRS and US GAAP have been refined through decades of standard-setter dialogue to produce comparable economic representations. Other national standards, while perfectly legitimate for their intended purposes, may produce materially different income figures due to different principles for revenue recognition, asset valuation, or expense timing. The €75 million threshold for Material Competitive Distortion is set high enough to avoid burdening groups with immaterial differences, but low enough to catch cases where an authorised standard could meaningfully distort GloBE calculations.

## 7. Decision Tree: Which Financial Accounts to Use

```
START: Identify CE's GloBE Income starting point
                    │
                    ▼
    ┌───────────────────────────────────────┐
    │ Can CE's accounts be determined using │
    │ UPE's accounting standard?            │
    └───────────────────────────────────────┘
                    │
         ┌─────────┴─────────┐
         │                   │
        YES                  NO
         │                   │
         ▼                   ▼
    ┌─────────┐    ┌────────────────────────┐
    │ Use UPE │    │ Is it "reasonably      │
    │ standard│    │ practicable" to        │
    │         │    │ convert to UPE std?    │
    └─────────┘    └────────────────────────┘
                             │
                  ┌──────────┴──────────┐
                  │                     │
                 YES                    NO
                  │                     │
                  ▼                     ▼
             ┌─────────┐    ┌──────────────────────┐
             │ Convert │    │ Apply Article 3.1.3  │
             │ to UPE  │    │ Alternative Standard │
             │ standard│    │ Exception            │
             └─────────┘    └──────────────────────┘
                                       │
                                       ▼
                           ┌──────────────────────┐
                           │ Three conditions:    │
                           │ 1. Maintained accts  │
                           │ 2. Reliable info     │
                           │ 3. Adjust >€1M perm  │
                           │    differences       │
                           └──────────────────────┘
                                       │
                                       ▼
                           ┌──────────────────────┐
                           │ Is standard          │
                           │ "Acceptable" or      │
                           │ "Authorised"?        │
                           └──────────────────────┘
                                       │
                            ┌──────────┴──────────┐
                            │                     │
                       ACCEPTABLE            AUTHORISED
                            │                     │
                            ▼                     ▼
                       ┌─────────┐    ┌──────────────────┐
                       │ No MCD  │    │ Check for        │
                       │ check   │    │ Material         │
                       │ needed  │    │ Competitive      │
                       └─────────┘    │ Distortion       │
                                      │ (>€75M)          │
                                      └──────────────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │                     │
                                  ≤€75M                 >€75M
                                    │                     │
                                    ▼                     ▼
                               ┌─────────┐    ┌──────────────────┐
                               │ Use as  │    │ Adjust to        │
                               │ is      │    │ eliminate MCD    │
                               └─────────┘    └──────────────────┘
```

## 8. Consolidation Adjustments: What Stays, What Goes

### 8.1 Adjustments Made During Consolidation

When preparing consolidated accounts, the parent makes various adjustments. For GloBE purposes, you need to understand which adjustments apply:

| Consolidation Adjustment | GloBE Treatment | Reason |
|-------------------------|-----------------|--------|
| Eliminate intra-group sales | **Do NOT eliminate** | GloBE uses pre-elimination accounts |
| Eliminate intra-group dividends | **Do NOT eliminate** (adjust later per Art. 3.2.1) | Handled separately |
| Eliminate intra-group profits in inventory | **Do NOT eliminate** | Entity-level profit is recognised |
| Goodwill amortisation/impairment | **Include** | Part of entity's P&L |
| Purchase Price Allocation (PPA) | **Include** | Reflected in acquiree's accounts |
| Currency translation adjustments | **Include** (if in P&L) | Part of financial accounting income |
| Minority interest share | **Do NOT deduct** | Handled in Top-Up Tax allocation |

### 8.2 Worked Example: Pre-Elimination vs Post-Elimination

**Stratos Group Consolidation — German Subsidiary**

| Item | SG Germany Individual Accounts | Consolidated Accounts | GloBE Starting Point |
|------|-------------------------------|----------------------|---------------------|
| External revenue | €35,000,000 | €35,000,000 | **€35,000,000** |
| Intra-group revenue (to France) | €5,000,000 | Eliminated | **€5,000,000** |
| **Total revenue** | **€40,000,000** | **€35,000,000** | **€40,000,000** |
| External costs | (€22,000,000) | (€22,000,000) | **(€22,000,000)** |
| Intra-group costs (from UK) | (€3,000,000) | Eliminated | **(€3,000,000)** |
| Other expenses | (€8,000,000) | (€8,000,000) | **(€8,000,000)** |
| Tax expense | (€2,100,000) | (€2,100,000) | **(€2,100,000)** |
| **Net Income** | **€4,900,000** | **€2,900,000** | **€4,900,000** |

**Key insight:** The German entity's GloBE starting point is **€4,900,000** (individual accounts), not €2,900,000 (consolidated contribution).

## 9. Minority Interest Treatment

A common question: How do minority interests affect the GloBE Income starting point?

**Answer:** There is **no reduction** in Financial Accounting Net Income or Loss for minority interests at the starting point stage. Minority interests are addressed later, during Top-Up Tax allocation *(see Chapter 2.4)*.

### 9.1 Worked Example: Minority Interest

**Scenario:** SG Ireland Ltd has 60% Stratos ownership and 40% external investor ownership. Net income is €5,200,000.

| Approach | Value |
|----------|-------|
| GloBE Income starting point | **€5,200,000** (full amount) |
| Minority share of income | Not deducted |
| Adjustment in allocation | 40% attributed to external investor at Top-Up Tax stage |

## 10. Materiality in GloBE Calculations

### 10.1 Inherited Materiality Threshold

The GloBE Rules do not specify a separate materiality threshold for calculating GloBE Income. Instead, **the same materiality threshold used for consolidated financial statements applies**.

**Practical implication:** If an item was immaterial for consolidated accounts purposes, it remains immaterial for GloBE purposes.

### 10.2 When Materiality Matters

| Situation | Consideration |
|-----------|---------------|
| Small adjustments | If below materiality, no need to calculate precisely |
| Alternative standard differences | €1M threshold for permanent differences is separate from general materiality |
| Entity-level errors | May be immaterial at group level but material at entity/jurisdiction level |

**Warning:** An error that nets to zero at group level can still affect GloBE calculations if it misstates income between jurisdictions.

## 11. Stratos Practical Application

### 11.1 Stratos Group Accounting Framework Summary

| Entity | Jurisdiction | Statutory Accounts | GloBE Accounts | Notes |
|--------|--------------|-------------------|----------------|-------|
| Stratos Group plc | UK | IFRS | IFRS | UPE |
| SG Holdings Ltd | UK | UK GAAP (FRS 101) | IFRS | Converted for consolidation |
| SG Germany GmbH | Germany | German HGB | IFRS | Converted for consolidation |
| SG France SAS | France | French GAAP | IFRS | Converted for consolidation |
| SG Netherlands BV | Netherlands | Dutch GAAP | IFRS | Converted for consolidation |
| SG Ireland Ltd | Ireland | Irish GAAP (FRS 102) | IFRS | Converted for consolidation |
| SG Singapore Pte Ltd | Singapore | SFRS | IFRS | SFRS is IFRS-identical |
| TechStart Ltd | Ireland | Irish GAAP | Irish GAAP* | *Art. 3.1.3 exception applied |

### 11.2 TechStart Exception Documentation

For TechStart Ltd, Stratos must document why the Article 3.1.3 exception applies:

**Documentation Checklist:**

| Item | Evidence |
|------|----------|
| Not reasonably practicable | Integration timeline extends beyond FY 2025; manual conversion would require €150K consultancy cost |
| Maintained accounts | Audited Irish GAAP accounts filed with CRO |
| Reliable information | Unqualified audit opinion |
| Permanent differences >€1M | R&D capitalisation: €1.8M adjusted to IFRS treatment |

## 12. Common Pitfalls

### 12.1 Pitfall 1: Using Consolidated P&L Directly

**Wrong:** Taking the consolidated P&L and allocating to jurisdictions based on revenue splits.

**Correct:** Using each CE's individual financial accounts before consolidation eliminations.

### 12.2 Pitfall 2: Eliminating Intra-Group Transactions

**Wrong:** Removing intra-group sales when calculating GloBE Income because "they're eliminated at group level."

**Correct:** Including all intra-group transactions at arm's-length values in each CE's GloBE Income.

### 12.3 Pitfall 3: Deducting Minority Interest

**Wrong:** Reducing a CE's GloBE Income by the minority share (e.g., 40% for external investor).

**Correct:** Using full GloBE Income; minority adjustment occurs during Top-Up Tax allocation.

### 12.4 Pitfall 4: Ignoring Alternative Standard Conditions

**Wrong:** Using local GAAP accounts "because that's what we have" without checking the three conditions.

**Correct:** Verifying maintained accounts, reliability, and adjusting permanent differences >€1M.

### 12.5 Pitfall 5: Missing Material Competitive Distortions

**Wrong:** Using an Authorised standard without checking for the €75M distortion threshold.

**Correct:** Comparing key principles to IFRS and quantifying any aggregate variance.

Establishing the correct financial account starting point may seem like a preliminary administrative step, but it fundamentally shapes all subsequent GloBE calculations. An error at this stage—using the wrong accounts, applying incorrect eliminations, or failing to adjust permanent differences—propagates through the entire ETR computation. For groups with complex structures, the interplay between consolidation reporting, statutory accounts, and GloBE requirements demands careful coordination between group accounting, local finance teams, and tax departments. Investing time to establish clear processes and documentation at this foundational stage pays dividends in accuracy and audit-readiness throughout the GloBE compliance cycle.

