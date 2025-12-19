# Chapter 5.5: De Minimis Exclusion

## Learning Objective

After completing this chapter, you will be able to apply the De Minimis Exclusion to eliminate Top-Up Tax liability for jurisdictions with minimal operations, calculate the three-year average thresholds, and determine which jurisdictions qualify for exclusion.

## Introduction

The global minimum tax framework was designed to address profit shifting by large multinational enterprises, yet its jurisdictional scope means that even modest operations can fall within the calculation requirements. Without appropriate relief, MNE Groups would face disproportionate compliance burdens for jurisdictions where their presence is minimal—perhaps a single representative office, a dormant entity retained for historical reasons, or a small service company supporting regional operations. The De Minimis Exclusion addresses this by creating objective thresholds below which jurisdictions are simply excluded from the ETR and Top-Up Tax calculation entirely.

This chapter examines the De Minimis Exclusion as a compliance simplification mechanism. The exclusion reflects a proportionality principle: the administrative cost of performing full GloBE calculations for a jurisdiction with €8 million in revenue and €500,000 in profit would likely exceed any Top-Up Tax that might result. By deeming such jurisdictions to have zero GloBE Income and zero Top-Up Tax, the framework focuses compliance resources where they matter most—on jurisdictions with material operations that could genuinely generate significant undertaxed income.

## 1. The De Minimis Exclusion Purpose

The De Minimis Exclusion provides **compliance relief** for jurisdictions with minimal operations. If a jurisdiction meets both thresholds, the MNE Group:

- Does **not** need to calculate Adjusted Covered Taxes for that jurisdiction
- Does **not** need to calculate ETR for that jurisdiction
- Does **not** have any Top-Up Tax liability for that jurisdiction

**Result:** GloBE Income and Top-Up Tax for the jurisdiction are **deemed to be zero**.

## 2. Qualification Criteria (Article 5.5.1)

A jurisdiction qualifies for the De Minimis Exclusion if **both** thresholds are met:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DE MINIMIS QUALIFICATION                         │
│                                                                     │
│  TEST 1: Average GloBE Revenue < €10 million                       │
│                        AND                                          │
│  TEST 2: Average GloBE Income < €1 million (or is a loss)          │
│                                                                     │
│  Both tests must pass for exclusion to apply                        │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.1 The Two Thresholds

| Test | Threshold | What It Measures |
|------|-----------|------------------|
| **Revenue Test** | Average GloBE Revenue < €10 million | Size of operations |
| **Profit Test** | Average GloBE Income < €1 million | Profitability of operations |

### 2.2 Critical Points

1. **Both tests must be met** — Passing only one test does not qualify
2. **Loss qualifies for Test 2** — If Average GloBE Income is a loss, Test 2 is passed
3. **GloBE amounts used** — Not local GAAP or CbCR figures (except under Safe Harbour)
4. **Annual election** — Must be elected each year; not automatic

The dual-threshold requirement serves an important purpose: it prevents gaming through either of the two measures alone. A jurisdiction might have low revenue but high profit margins (suggesting valuable intellectual property or similar income), or high revenue with minimal profits (suggesting transfer pricing arrangements that compress local margins). By requiring both tests to pass, the exclusion targets genuinely small operations rather than artificially structured arrangements. The loss-qualification for Test 2 recognises that loss-making operations, by definition, cannot generate undertaxed profits—there is no excess profit to subject to the 15% floor.

## 3. Three-Year Averaging (Article 5.5.1 and 5.5.2)

The De Minimis thresholds use a **three-year average** of the current fiscal year and the two preceding fiscal years:

```
                        FY-2 + FY-1 + FY (Current)
Average GloBE Revenue = ──────────────────────────────
                                    3

                       FY-2 + FY-1 + FY (Current)
Average GloBE Income = ──────────────────────────────
                                   3
```

### 3.1 Example: Three-Year Calculation

**Jurisdiction:** Luxembourg (small service entity)

| Fiscal Year | GloBE Revenue | GloBE Income |
|-------------|---------------|--------------|
| FY 2023 | €7,800,000 | €450,000 |
| FY 2024 | €8,200,000 | €680,000 |
| FY 2025 (Current) | €9,100,000 | €820,000 |
| **Total** | **€25,100,000** | **€1,950,000** |

**Average Calculation:**

| Test | Calculation | Result | Threshold | Pass? |
|------|-------------|--------|-----------|-------|
| Revenue | €25,100,000 ÷ 3 | €8,366,667 | < €10 million | ✓ Yes |
| Income | €1,950,000 ÷ 3 | €650,000 | < €1 million | ✓ Yes |

**Result:** Luxembourg qualifies for De Minimis Exclusion in FY 2025.

The three-year averaging mechanism serves to smooth fluctuations in revenue and income that might otherwise cause jurisdictions to oscillate between qualifying and not qualifying. Many small operations experience year-to-year variability due to contract timing, one-off transactions, or cyclical factors unrelated to their underlying substance. Without averaging, a jurisdiction might qualify in year one, fail in year two due to a single large contract, and qualify again in year three—creating unpredictable compliance burdens. The three-year window provides stability while still allowing the thresholds to adapt over time as operations grow or shrink.

## 4. Excluded Years (Article 5.5.2)

Certain years are **excluded** from the averaging calculation:

| Excluded Year Scenario | Treatment |
|------------------------|-----------|
| No Constituent Entities in jurisdiction | Year excluded from average |
| Only **dormant** Constituent Entities | Year excluded from average |
| No Constituent Entity with GloBE Income or Loss | Year excluded from average |
| Pre-GloBE implementation year | Year excluded from average |

### 4.1 Effect of Excluded Years

If a year is excluded, the average is calculated over fewer years:

**Scenario:** Entity established in FY 2024 (no operations in FY 2022 or FY 2023)

| Fiscal Year | Included? | GloBE Revenue | GloBE Income |
|-------------|-----------|---------------|--------------|
| FY 2023 | No (no CE) | — | — |
| FY 2024 | Yes | €4,500,000 | €320,000 |
| FY 2025 (Current) | Yes | €6,200,000 | €580,000 |
| **Total** | | **€10,700,000** | **€900,000** |

**Average (2 years):**

| Test | Calculation | Result | Threshold | Pass? |
|------|-------------|--------|-----------|-------|
| Revenue | €10,700,000 ÷ 2 | €5,350,000 | < €10 million | ✓ Yes |
| Income | €900,000 ÷ 2 | €450,000 | < €1 million | ✓ Yes |

**Result:** De Minimis applies with two-year average.

### 4.2 First Year of Operations

If the current fiscal year is the **first year** with Constituent Entities:
- Only the current year's figures are used
- No averaging required

The excluded years provisions prevent artificial distortion of the averaging calculation. Without these rules, a newly established entity might benefit from including "phantom" zero-revenue years that would artificially depress the three-year average and allow qualification even when current-year operations exceed the thresholds. Conversely, a jurisdiction where operations have wound down to dormancy should not be penalised by historical years of larger activity. The exclusion rules ensure that the averaging calculation reflects the genuine operational footprint during periods when the MNE Group actually had functioning Constituent Entities in the jurisdiction.

## 5. Currency Conversion (Article 5.5.3)

The €10 million and €1 million thresholds are in **euros**. If the MNE Group's Consolidated Financial Statements use a different presentation currency:

```
Convert thresholds using:
- Average exchange rate for December of the calendar year
- Immediately preceding the start of the MNE Group's Fiscal Year
```

### 5.1 Example: USD-Reporting Group

**MNE Group FY:** January 1, 2025 – December 31, 2025
**Presentation currency:** USD
**December 2024 average EUR/USD rate:** 1.08

| Threshold (EUR) | Converted (USD) |
|-----------------|-----------------|
| €10 million | €10M × 1.08 = **$10.8 million** |
| €1 million | €1M × 1.08 = **$1.08 million** |

The currency conversion mechanism ensures that the De Minimis thresholds function equivalently regardless of an MNE Group's reporting currency. Using the December average rate from the year before the fiscal year begins provides certainty—the converted thresholds can be determined in advance, rather than waiting for year-end exchange rates. This forward-looking approach allows MNE Groups to anticipate whether jurisdictions are likely to qualify for De Minimis and plan their compliance efforts accordingly. Exchange rate fluctuations can cause marginal jurisdictions to move in or out of qualification, making regular monitoring important for groups with operations near the thresholds.

## 6. Entities Excluded from De Minimis (Article 5.5.1)

The De Minimis Exclusion does **not** apply to:

| Entity Type | Treatment |
|-------------|-----------|
| **Stateless Constituent Entities** | Never qualify for De Minimis; excluded from threshold calculations |
| **Investment Constituent Entities** | Never qualify for De Minimis; excluded from threshold calculations |

### 6.1 Treatment of Excluded Entities

When calculating whether a jurisdiction qualifies:
- **Remove** revenue and income of Stateless Entities
- **Remove** revenue and income of Investment Entities
- Calculate thresholds using **remaining** Constituent Entities only

**Example:** Jurisdiction with mixed entities

| Entity | Type | GloBE Revenue | GloBE Income |
|--------|------|---------------|--------------|
| OpCo A | Operating | €6,500,000 | €480,000 |
| InvestCo | Investment | €3,200,000 | €2,100,000 |
| **For De Minimis Test** | | **€6,500,000** | **€480,000** |

**Result:** InvestCo excluded from calculation; jurisdiction may still qualify on OpCo A's figures.

The exclusion of Stateless and Investment Entities from the De Minimis calculation reflects their special treatment elsewhere in the GloBE Rules. Stateless Entities—those without a tax residence—present unique concerns because they have no jurisdiction that can impose the minimum tax, making them subject to specific anti-avoidance provisions. Investment Entities are governed by separate rules in Articles 7.4 and 7.5 that address their particular characteristics. Including either category in the De Minimis calculation would distort the measurement of ordinary operating activity in a jurisdiction and could create opportunities for structuring around the thresholds by adding or removing such entities.

## 7. Annual Election Requirement

The De Minimis Exclusion is an **annual election** *(Article 5.5.1)*:

- Must be **actively elected** each fiscal year
- Jurisdiction may qualify in one year but not the next
- Election is made jurisdiction-by-jurisdiction
- No binding effect on future years

### 7.1 Year-by-Year Assessment

| Fiscal Year | Avg Revenue | Avg Income | Qualifies? | Election Made? |
|-------------|-------------|------------|------------|----------------|
| FY 2024 | €7.2M | €0.6M | Yes | Yes |
| FY 2025 | €9.8M | €1.3M | No (income) | N/A |
| FY 2026 | €11.5M | €0.8M | No (revenue) | N/A |
| FY 2027 | €8.9M | €0.7M | Yes | Yes |

**Practical implication:** Monitor thresholds annually; eligibility can change.

The elective nature of the De Minimis Exclusion reflects a recognition that circumstances vary across MNE Groups. In most cases, electing the exclusion for qualifying jurisdictions reduces compliance burden without adverse consequences. However, there may be situations where an MNE Group prefers to perform the full calculation—perhaps to generate documentation supporting a low-risk tax position, or where the jurisdiction's ETR is comfortably above 15% and the group wants to demonstrate this affirmatively. The annual election mechanism ensures flexibility while requiring conscious decision-making for each fiscal year and each qualifying jurisdiction.

## 8. Transitional CbCR Safe Harbour De Minimis Test

A **simplified version** of the De Minimis test is available under the Transitional CbCR Safe Harbour:

### 8.1 Simplified Test (Transition Period Only)

| Feature | Standard De Minimis | Transitional Safe Harbour |
|---------|---------------------|---------------------------|
| **Data source** | GloBE amounts | CbCR data |
| **Averaging period** | 3-year average | Current year only |
| **Revenue threshold** | €10 million | €10 million |
| **Income threshold** | €1 million | €1 million |
| **Available until** | Permanent | FY starting on or before 31 Dec 2026 |

### 8.2 When to Use Transitional Test

The Transitional CbCR Safe Harbour De Minimis Test is advantageous when:
- CbCR data is readily available
- GloBE Income calculations are burdensome for small jurisdictions
- The jurisdiction would clearly pass the CbCR-based thresholds

**Example:** Use CbCR Revenue (€6.5M) and CbCR Profit Before Tax (€0.4M) instead of calculating GloBE amounts.

The Transitional CbCR Safe Harbour De Minimis Test provides meaningful simplification during the initial implementation years. Many MNE Groups already prepare Country-by-Country Reports as part of their BEPS compliance obligations, making CbCR data readily available without additional calculation. While CbCR revenue and profit figures differ from GloBE Revenue and GloBE Income (due to the various GloBE adjustments), they provide a reasonable proxy for identifying small jurisdictions. The single-year measurement eliminates the averaging calculation entirely. For jurisdictions clearly below both thresholds based on CbCR data, this offers substantial compliance savings during the transition period while the full GloBE calculation infrastructure is being developed.

## 9. Decision Flowchart: De Minimis Qualification

```
START: Jurisdiction assessment for De Minimis
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Does jurisdiction have only Stateless or          │
│ Investment Entities?                              │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────┐
  YES       NO
   │         │
   ▼         ▼
┌────────┐   │
│ De     │   │
│ Minimis│   │
│ NOT    │   │
│ available│ │
└────────┘   │
             ▼
┌───────────────────────────────────────────────────┐
│ Gather 3-year GloBE Revenue and Income            │
│ (current year + 2 preceding years)                │
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Exclude any years with:                           │
│ - No Constituent Entities                         │
│ - Only dormant entities                           │
│ - No GloBE Income or Loss                         │
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Calculate Average GloBE Revenue                   │
│ = Sum of Revenue ÷ Number of included years       │
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Is Average GloBE Revenue < €10 million?           │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────┐
   NO       YES
   │         │
   ▼         ▼
┌────────┐  ┌───────────────────────────────────────┐
│ De     │  │ Calculate Average GloBE Income        │
│ Minimis│  │ = Sum of Income ÷ Number of included  │
│ does   │  │   years                               │
│ NOT    │  └───────────────────────────────────────┘
│ apply  │          │
└────────┘          ▼
           ┌───────────────────────────────────────┐
           │ Is Average GloBE Income < €1 million  │
           │ OR a loss?                             │
           └───────────────────────────────────────┘
                    │
               ┌────┴────┐
               NO       YES
               │         │
               ▼         ▼
        ┌────────┐  ┌────────────────────────────┐
        │ De     │  │ DE MINIMIS EXCLUSION       │
        │ Minimis│  │ AVAILABLE                   │
        │ does   │  │                             │
        │ NOT    │  │ → Elect exclusion           │
        │ apply  │  │ → No ETR calculation needed │
        └────────┘  │ → Top-Up Tax = €0           │
                    └────────────────────────────┘
```

## 10. Stratos Worked Example: De Minimis Assessment

Stratos Group has operations in multiple jurisdictions. Let's assess each for De Minimis eligibility.

### 10.1 Jurisdiction Assessment Table

| Jurisdiction | 3-Year Avg Revenue | 3-Year Avg Income | Revenue < €10M? | Income < €1M? | Qualifies? |
|--------------|-------------------|-------------------|-----------------|---------------|------------|
| Germany | €85,000,000 | €9,200,000 | No | No | **No** |
| Singapore | €18,500,000 | €3,800,000 | No | No | **No** |
| Ireland | €52,000,000 | €14,200,000 | No | No | **No** |
| **Luxembourg** | **€8,500,000** | **€620,000** | **Yes** | **Yes** | **Yes** |

### 10.2 Luxembourg Detailed Analysis

Stratos Luxembourg S.à r.l. provides intra-group treasury services.

**Three-Year Data:**

| Fiscal Year | GloBE Revenue | GloBE Income |
|-------------|---------------|--------------|
| FY 2023 | €7,900,000 | €580,000 |
| FY 2024 | €8,400,000 | €650,000 |
| FY 2025 (Current) | €9,200,000 | €630,000 |
| **Total** | **€25,500,000** | **€1,860,000** |

**Average Calculation:**

| Test | Calculation | Result | Threshold | Pass? |
|------|-------------|--------|-----------|-------|
| Revenue | €25,500,000 ÷ 3 | €8,500,000 | < €10 million | ✓ Yes |
| Income | €1,860,000 ÷ 3 | €620,000 | < €1 million | ✓ Yes |

**Result:** Luxembourg qualifies for De Minimis Exclusion.

### 10.3 Luxembourg Preliminary ETR (Before De Minimis)

If De Minimis were **not** elected:

| Item | Amount |
|------|--------|
| GloBE Income (FY 2025) | €630,000 |
| Adjusted Covered Taxes | €55,000 |
| ETR | 8.73% |
| Top-Up Tax % | 6.27% |
| Top-Up Tax | ~€39,500 |

**With De Minimis Election:**
- No ETR calculation required
- No Top-Up Tax liability
- Administrative burden eliminated

### 10.4 Updated Stratos Top-Up Tax Summary

| Jurisdiction | ETR | Top-Up Tax % | Top-Up Tax | De Minimis? | Final Liability |
|--------------|-----|--------------|------------|-------------|-----------------|
| Germany | 23.00% | — | €0 | No | €0 |
| Singapore | 9.81% | 5.19% | €197,498 | No | €197,498 (IIR) |
| Ireland | 11.80% | 3.20% | €426,394 | No | €0 (QDMTT offset) |
| **Luxembourg** | N/A | N/A | N/A | **Yes** | **€0** |
| **Total** | | | | | **€197,498** |

The Stratos example demonstrates the practical value of the De Minimis Exclusion in action. Luxembourg's small treasury operation, while generating positive income at a low effective rate (8.73%), would produce only approximately €39,500 in Top-Up Tax if fully calculated. The administrative effort required to compute GloBE Income, Adjusted Covered Taxes, SBIE, and allocate any resulting Top-Up Tax far exceeds the economic significance of this amount. By electing the De Minimis Exclusion, Stratos eliminates this compliance burden entirely while focusing its GloBE resources on jurisdictions with material exposure—Singapore's €197,498 IIR liability and Ireland's QDMTT calculation.

## 11. Common Pitfalls

### 11.1 Pitfall 1: Using CbCR Data Without Safe Harbour Election

**Error:** Using CbCR revenue and profit figures for De Minimis without formally electing the Transitional Safe Harbour.

**Correct approach:** Use GloBE Revenue and GloBE Income for standard De Minimis test. Only use CbCR data if electing the Transitional Safe Harbour De Minimis Test.

### 11.2 Pitfall 2: Forgetting Three-Year Averaging

**Error:** Using current year figures only for the standard De Minimis test.

**Correct approach:** Calculate three-year averages (unless years are excluded per Article 5.5.2).

### 11.3 Pitfall 3: Including Investment Entities

**Error:** Including Investment Entity revenue and income when calculating jurisdiction totals.

**Correct approach:** Exclude Stateless and Investment Entities from De Minimis threshold calculations.

### 11.4 Pitfall 4: Assuming De Minimis is Automatic

**Error:** Assuming the exclusion applies automatically if thresholds are met.

**Correct approach:** The De Minimis Exclusion must be **actively elected** each year.

### 11.5 Pitfall 5: Failing to Monitor Year-on-Year

**Error:** Assuming qualification in one year guarantees qualification in future years.

**Correct approach:** Reassess annually; growing operations may exceed thresholds.

## 12. De Minimis Assessment Checklist

Use this checklist to assess each jurisdiction:

```
DE MINIMIS QUALIFICATION CHECKLIST
Jurisdiction: _________________________
Fiscal Year: _________________________

□ Step 1: Exclude Ineligible Entities
   □ Identify any Stateless Constituent Entities → Exclude
   □ Identify any Investment Entities → Exclude
   □ Remaining entities: ____________________

□ Step 2: Determine Averaging Period
   □ Current fiscal year: FY ______
   □ Two preceding years: FY ______ and FY ______
   □ Exclude years with no CEs or only dormant CEs
   □ Years included in average: ______ years

□ Step 3: Calculate Average GloBE Revenue
   □ FY-2 Revenue:     €__________________
   □ FY-1 Revenue:     €__________________
   □ FY Revenue:       €__________________
   □ Total Revenue:    €__________________
   □ Average Revenue:  €__________________ (Total ÷ years)
   □ Is Average < €10 million? YES / NO

   If NO → De Minimis does NOT apply. STOP.

□ Step 4: Calculate Average GloBE Income
   □ FY-2 Income:      €__________________
   □ FY-1 Income:      €__________________
   □ FY Income:        €__________________
   □ Total Income:     €__________________
   □ Average Income:   €__________________ (Total ÷ years)
   □ Is Average < €1 million OR a loss? YES / NO

   If NO → De Minimis does NOT apply. STOP.

□ Step 5: Election
   □ Both thresholds met? YES / NO
   □ Election made for this fiscal year? YES / NO
   □ Document election in GIR filing

RESULT:
□ De Minimis Exclusion APPLIES — No ETR or Top-Up Tax calculation required
□ De Minimis Exclusion does NOT apply — Proceed with full GloBE calculations
```

## Concluding Discussion

The De Minimis Exclusion exemplifies the pragmatic approach that permeates the GloBE framework. While the global minimum tax represents an ambitious attempt to establish a floor on corporate taxation worldwide, the Inclusive Framework recognised that mechanically applying this floor to every jurisdiction—regardless of the operational footprint—would create disproportionate compliance burdens without commensurate policy benefits. Small jurisdictions with minimal GloBE Income generate minimal Top-Up Tax liability; the De Minimis Exclusion simply acknowledges this reality and provides appropriate relief.

For MNE Groups with extensive geographic footprints, the De Minimis Exclusion can significantly reduce compliance complexity. A group operating in forty jurisdictions might find that ten to fifteen qualify for De Minimis treatment, eliminating the need for full GloBE calculations in those locations. This allows tax departments to concentrate resources on jurisdictions that present genuine exposure—those with material operations and ETRs below the 15% threshold. The annual election requirement ensures that this assessment happens regularly, catching jurisdictions as they grow beyond the thresholds or shrink back below them.

Practitioners should maintain systematic processes for De Minimis monitoring. As the three-year averaging window rolls forward, jurisdictions near the thresholds may move in or out of qualification. Currency movements can shift the converted thresholds for non-euro reporters. The Transitional CbCR Safe Harbour offers additional simplification during the implementation period but will eventually expire, requiring groups to build full GloBE calculation capabilities even for small jurisdictions if they want to demonstrate qualification. Effective De Minimis management thus becomes an ongoing compliance discipline rather than a one-time assessment.

