# Chapter 5.5: De Minimis Exclusion

## Learning Objective

After completing this chapter, you will be able to apply the De Minimis Exclusion to eliminate Top-up Tax liability for jurisdictions with minimal operations, calculate the three-year average thresholds, and determine which jurisdictions qualify for exclusion.

---

## Key References

**OECD GloBE Model Rules:**
- Article 5.5.1 — De Minimis Exclusion criteria (revenue and income thresholds)
- Article 5.5.2 — Excluded years from averaging calculation
- Article 5.5.3 — Currency conversion for thresholds

**OECD Commentary:**
- Chapter 5, paragraphs 146-162 — De Minimis Exclusion methodology

**Administrative Guidance:**
- December 2023: Transitional CbCR Safe Harbour De Minimis Test (simplified single-year test)

---

## The De Minimis Exclusion Purpose

The De Minimis Exclusion provides **compliance relief** for jurisdictions with minimal operations. If a jurisdiction meets both thresholds, the MNE Group:

- Does **not** need to calculate Adjusted Covered Taxes for that jurisdiction
- Does **not** need to calculate ETR for that jurisdiction
- Does **not** have any Top-up Tax liability for that jurisdiction

**Result:** GloBE Income and Top-up Tax for the jurisdiction are **deemed to be zero**.

---

## Qualification Criteria *(Article 5.5.1)*

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

### The Two Thresholds

| Test | Threshold | What It Measures |
|------|-----------|------------------|
| **Revenue Test** | Average GloBE Revenue < €10 million | Size of operations |
| **Profit Test** | Average GloBE Income < €1 million | Profitability of operations |

### Critical Points

1. **Both tests must be met** — Passing only one test does not qualify
2. **Loss qualifies for Test 2** — If Average GloBE Income is a loss, Test 2 is passed
3. **GloBE amounts used** — Not local GAAP or CbCR figures (except under Safe Harbour)
4. **Annual election** — Must be elected each year; not automatic

---

## Three-Year Averaging *(Article 5.5.1 and 5.5.2)*

The De Minimis thresholds use a **three-year average** of the current fiscal year and the two preceding fiscal years:

```
                        FY-2 + FY-1 + FY (Current)
Average GloBE Revenue = ──────────────────────────────
                                    3

                       FY-2 + FY-1 + FY (Current)
Average GloBE Income = ──────────────────────────────
                                   3
```

### Example: Three-Year Calculation

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

---

## Excluded Years *(Article 5.5.2)*

Certain years are **excluded** from the averaging calculation:

| Excluded Year Scenario | Treatment |
|------------------------|-----------|
| No Constituent Entities in jurisdiction | Year excluded from average |
| Only **dormant** Constituent Entities | Year excluded from average |
| No Constituent Entity with GloBE Income or Loss | Year excluded from average |
| Pre-GloBE implementation year | Year excluded from average |

### Effect of Excluded Years

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

### First Year of Operations

If the current fiscal year is the **first year** with Constituent Entities:
- Only the current year's figures are used
- No averaging required

---

## Currency Conversion *(Article 5.5.3)*

The €10 million and €1 million thresholds are in **euros**. If the MNE Group's Consolidated Financial Statements use a different presentation currency:

```
Convert thresholds using:
- Average exchange rate for December of the calendar year
- Immediately preceding the start of the MNE Group's Fiscal Year
```

### Example: USD-Reporting Group

**MNE Group FY:** January 1, 2025 – December 31, 2025
**Presentation currency:** USD
**December 2024 average EUR/USD rate:** 1.08

| Threshold (EUR) | Converted (USD) |
|-----------------|-----------------|
| €10 million | €10M × 1.08 = **$10.8 million** |
| €1 million | €1M × 1.08 = **$1.08 million** |

---

## Entities Excluded from De Minimis *(Article 5.5.1)*

The De Minimis Exclusion does **not** apply to:

| Entity Type | Treatment |
|-------------|-----------|
| **Stateless Constituent Entities** | Never qualify for De Minimis; excluded from threshold calculations |
| **Investment Constituent Entities** | Never qualify for De Minimis; excluded from threshold calculations |

### Treatment of Excluded Entities

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

---

## Annual Election Requirement

The De Minimis Exclusion is an **annual election** *(Article 5.5.1)*:

- Must be **actively elected** each fiscal year
- Jurisdiction may qualify in one year but not the next
- Election is made jurisdiction-by-jurisdiction
- No binding effect on future years

### Year-by-Year Assessment

| Fiscal Year | Avg Revenue | Avg Income | Qualifies? | Election Made? |
|-------------|-------------|------------|------------|----------------|
| FY 2024 | €7.2M | €0.6M | Yes | Yes |
| FY 2025 | €9.8M | €1.3M | No (income) | N/A |
| FY 2026 | €11.5M | €0.8M | No (revenue) | N/A |
| FY 2027 | €8.9M | €0.7M | Yes | Yes |

**Practical implication:** Monitor thresholds annually; eligibility can change.

---

## Transitional CbCR Safe Harbour De Minimis Test

A **simplified version** of the De Minimis test is available under the Transitional CbCR Safe Harbour:

### Simplified Test (Transition Period Only)

| Feature | Standard De Minimis | Transitional Safe Harbour |
|---------|---------------------|---------------------------|
| **Data source** | GloBE amounts | CbCR data |
| **Averaging period** | 3-year average | Current year only |
| **Revenue threshold** | €10 million | €10 million |
| **Income threshold** | €1 million | €1 million |
| **Available until** | Permanent | FY starting on or before 31 Dec 2026 |

### When to Use Transitional Test

The Transitional CbCR Safe Harbour De Minimis Test is advantageous when:
- CbCR data is readily available
- GloBE Income calculations are burdensome for small jurisdictions
- The jurisdiction would clearly pass the CbCR-based thresholds

**Example:** Use CbCR Revenue (€6.5M) and CbCR Profit Before Tax (€0.4M) instead of calculating GloBE amounts.

---

## Decision Flowchart: De Minimis Qualification

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
        └────────┘  │ → Top-up Tax = €0           │
                    └────────────────────────────┘
```

---

## Stratos Worked Example: De Minimis Assessment

Stratos Group has operations in multiple jurisdictions. Let's assess each for De Minimis eligibility.

### Jurisdiction Assessment Table

| Jurisdiction | 3-Year Avg Revenue | 3-Year Avg Income | Revenue < €10M? | Income < €1M? | Qualifies? |
|--------------|-------------------|-------------------|-----------------|---------------|------------|
| Germany | €85,000,000 | €9,200,000 | No | No | **No** |
| Singapore | €18,500,000 | €3,800,000 | No | No | **No** |
| Ireland | €52,000,000 | €14,200,000 | No | No | **No** |
| **Luxembourg** | **€8,500,000** | **€620,000** | **Yes** | **Yes** | **Yes** |

### Luxembourg Detailed Analysis

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

### Luxembourg Preliminary ETR (Before De Minimis)

If De Minimis were **not** elected:

| Item | Amount |
|------|--------|
| GloBE Income (FY 2025) | €630,000 |
| Adjusted Covered Taxes | €55,000 |
| ETR | 8.73% |
| Top-up Tax % | 6.27% |
| Top-up Tax | ~€39,500 |

**With De Minimis Election:**
- No ETR calculation required
- No Top-up Tax liability
- Administrative burden eliminated

### Updated Stratos Top-Up Tax Summary

| Jurisdiction | ETR | Top-up Tax % | Top-up Tax | De Minimis? | Final Liability |
|--------------|-----|--------------|------------|-------------|-----------------|
| Germany | 23.00% | — | €0 | No | €0 |
| Singapore | 9.81% | 5.19% | €197,734 | No | €197,734 (IIR) |
| Ireland | 11.80% | 3.20% | €427,699 | No | €0 (QDMTT offset) |
| **Luxembourg** | N/A | N/A | N/A | **Yes** | **€0** |
| **Total** | | | | | **€197,734** |

---

## Common Pitfalls

### Pitfall 1: Using CbCR Data Without Safe Harbour Election

**Error:** Using CbCR revenue and profit figures for De Minimis without formally electing the Transitional Safe Harbour.

**Correct approach:** Use GloBE Revenue and GloBE Income for standard De Minimis test. Only use CbCR data if electing the Transitional Safe Harbour De Minimis Test.

### Pitfall 2: Forgetting Three-Year Averaging

**Error:** Using current year figures only for the standard De Minimis test.

**Correct approach:** Calculate three-year averages (unless years are excluded per Article 5.5.2).

### Pitfall 3: Including Investment Entities

**Error:** Including Investment Entity revenue and income when calculating jurisdiction totals.

**Correct approach:** Exclude Stateless and Investment Entities from De Minimis threshold calculations.

### Pitfall 4: Assuming De Minimis is Automatic

**Error:** Assuming the exclusion applies automatically if thresholds are met.

**Correct approach:** The De Minimis Exclusion must be **actively elected** each year.

### Pitfall 5: Failing to Monitor Year-on-Year

**Error:** Assuming qualification in one year guarantees qualification in future years.

**Correct approach:** Reassess annually; growing operations may exceed thresholds.

---

## De Minimis Assessment Checklist

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
□ De Minimis Exclusion APPLIES — No ETR or Top-up Tax calculation required
□ De Minimis Exclusion does NOT apply — Proceed with full GloBE calculations
```

---

## Summary

The De Minimis Exclusion provides meaningful compliance relief for jurisdictions with minimal operations:

| Aspect | Key Point |
|--------|-----------|
| **Revenue threshold** | Average GloBE Revenue < €10 million |
| **Income threshold** | Average GloBE Income < €1 million (or loss) |
| **Averaging period** | Current year + 2 preceding years |
| **Excluded entities** | Stateless and Investment Entities |
| **Effect** | No ETR calculation; Top-up Tax deemed zero |
| **Election** | Must be elected annually |
| **Transitional option** | CbCR-based single-year test available until FY 2026 |

For Stratos, Luxembourg qualifies for De Minimis, eliminating the need to calculate ETR and potential Top-up Tax (~€39,500 saved).

---

## Integration with GIR Tools

The De Minimis assessment is a **pre-screening step** before using GIR-001 GloBE Calculator:

| Step | Tool | Action |
|------|------|--------|
| **Pre-screening** | Manual assessment | Apply De Minimis checklist to each jurisdiction |
| **If qualifies** | N/A | No GIR-001 calculation needed; document election |
| **If does not qualify** | GIR-001 GloBE Calculator | Proceed with full ETR → SBIE → Top-up Tax workflow |

**GIR-002 Safe Harbour Qualifier** can assess the **Transitional CbCR Safe Harbour De Minimis Test**:
- Input CbCR revenue and profit data
- Tool applies single-year thresholds
- Returns qualification status

**Workflow for Multiple Jurisdictions:**

```
For each jurisdiction:
├── Apply De Minimis checklist
│   ├── If qualifies → Document election; skip GIR-001
│   └── If does not qualify → Continue
├── Check Transitional Safe Harbour (GIR-002)
│   ├── If qualifies → Apply Safe Harbour; skip full calculation
│   └── If does not qualify → Continue
└── Perform full GloBE calculation (GIR-001)
```

---

## Next Step

You have learned how to apply the De Minimis Exclusion to eliminate compliance burden for small jurisdictions. Proceed to **Chapter 5.6: Minority-Owned Constituent Entities** for guidance on the separate ETR calculation and Top-up Tax treatment for entities with 30% or less ownership.
