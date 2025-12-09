# Section 5.4.3: Top-Up Tax Computation

## Introduction

The Top-Up Tax computation is the culmination of the GloBE calculation process. This section brings together the ETR calculation, SBIE carve-outs, and QDMTT offsets to determine the final Top-up Tax liability for each jurisdiction where the MNE Group's effective taxation falls below the 15% minimum rate.

This section provides step-by-step guidance for computing Top-up Tax using the GIR Completion Calculator, including the complete formula, QDMTT offset mechanics, and Additional Top-up Tax adjustments.

**Learning Objectives:**
- Calculate the Top-up Tax Percentage for low-taxed jurisdictions
- Compute Excess Profit after SBIE deduction
- Apply QDMTT offset to reduce Top-up Tax
- Handle Additional Top-up Tax from prior period adjustments
- Document Top-up Tax computations for GIR Section 3

---

## 5.4.3.1 Top-Up Tax Computation Framework

### The Complete Formula

Under Article 5.2 of the GloBE Model Rules, the jurisdictional Top-up Tax is calculated as:

```
Jurisdictional Top-up Tax = (Top-up Tax % × Excess Profit) + Additional Top-up Tax − QDMTT

Where:
├── Top-up Tax % = 15% − Jurisdictional ETR (if ETR < 15%)
├── Excess Profit = Net GloBE Income − SBIE
├── Additional Top-up Tax = Prior period adjustments, recapture amounts
└── QDMTT = Qualified Domestic Minimum Top-up Tax paid
```

### Calculation Flow Diagram

```
Top-Up Tax Computation Flow:

┌─────────────────────────────┐
│ Step 1: Calculate ETR       │
│ ETR = Covered Taxes ÷ GloBE │
│ Income                      │
└──────────────┬──────────────┘
               │
               ▼
        ┌──────────────┐
        │ ETR < 15%?   │
        └──────┬───────┘
               │
        ┌──────┴──────┐
        │             │
        ▼ YES         ▼ NO
┌───────────────┐  ┌──────────────────┐
│ Step 2:       │  │ No Top-up Tax    │
│ Calculate     │  │ Required         │
│ Top-up %      │  │ (End)            │
└───────┬───────┘  └──────────────────┘
        │
        ▼
┌───────────────────────────────┐
│ Step 3: Calculate Excess      │
│ Profit                        │
│ = GloBE Income − SBIE         │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Step 4: Initial Top-up Tax    │
│ = Top-up % × Excess Profit    │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Step 5: Add Additional        │
│ Top-up Tax (if any)           │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Step 6: Deduct QDMTT          │
│ (if applicable)               │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Final Jurisdictional          │
│ Top-up Tax                    │
└───────────────────────────────┘
```

---

## 5.4.3.2 Top-Up Tax Percentage Calculation

### Article 5.2.1 Requirement

The Top-up Tax Percentage is the difference between the 15% minimum rate and the jurisdiction's ETR:

```
Top-up Tax Percentage = 15.00% − Jurisdictional ETR

Examples:
├── ETR = 10.00% → Top-up % = 15.00% − 10.00% = 5.00%
├── ETR = 12.50% → Top-up % = 15.00% − 12.50% = 2.50%
├── ETR = 14.99% → Top-up % = 15.00% − 14.99% = 0.01%
├── ETR = 15.00% → Top-up % = 0.00% (No Top-up Tax)
└── ETR = 20.00% → Top-up % = 0.00% (No Top-up Tax)
```

### Calculator Data Entry

**Tab:** `Section 3.3 - Top-Up Tax`

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| Jurisdiction | B5 | | IE |
| Jurisdictional ETR | C5 | From Section 3.1 | 12.48% |
| Minimum Rate | D5 | Fixed | 15.00% |
| **Top-up Tax Percentage** | E5 | =MAX(D5-C5,0) | **2.52%** |

**Validation Rules:**

```
Top-up Tax Percentage Validation:
├── Cannot be negative (floor at 0%)
├── Maximum theoretical: 15% (if ETR = 0%)
├── Must round to 4 decimal places (e.g., 2.5200%)
└── N/A if jurisdiction has GloBE Loss
```

---

## 5.4.3.3 Excess Profit Calculation

### Article 5.2.2 Requirement

Excess Profit represents the portion of GloBE Income that exceeds the substance-based return:

```
Excess Profit = Net GloBE Income − SBIE

Constraints:
├── Excess Profit cannot be negative
├── If SBIE > GloBE Income, Excess Profit = €0
└── Excess SBIE is lost (no carryforward)
```

### Calculator Data Entry

**Tab:** `Section 3.3 - Top-Up Tax`

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| Net GloBE Income | F5 | From Section 3.1 | €67,300,000 |
| Total SBIE | G5 | From Section 3.2 | €6,319,000 |
| **Excess Profit** | H5 | =MAX(F5-G5,0) | **€60,981,000** |

**Excess Profit Scenarios:**

| Scenario | GloBE Income | SBIE | Excess Profit |
|----------|-------------|------|---------------|
| Standard case | €100M | €20M | €80M |
| SBIE exceeds income | €15M | €25M | €0 (not negative) |
| No SBIE election | €100M | €0 | €100M |
| GloBE Loss | (€5M) | €20M | N/A (no calculation) |

---

## 5.4.3.4 Initial Top-Up Tax Calculation

### The Core Multiplication

```
Initial Top-up Tax = Top-up Tax Percentage × Excess Profit
```

### Calculator Data Entry

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| Top-up Tax Percentage | E5 | From above | 2.52% |
| Excess Profit | H5 | From above | €60,981,000 |
| **Initial Top-up Tax** | I5 | =E5×H5 | **€1,536,721** |

### Worked Examples

**Example 1: Ireland (Low ETR)**

| Component | Calculation | Result |
|-----------|-------------|--------|
| Net GloBE Income | | €67,300,000 |
| SBIE | | €6,319,000 |
| Excess Profit | €67,300,000 − €6,319,000 | €60,981,000 |
| ETR | | 12.48% |
| Top-up Tax % | 15.00% − 12.48% | 2.52% |
| Initial Top-up Tax | €60,981,000 × 2.52% | **€1,536,721** |

**Example 2: Luxembourg (Very Low ETR)**

| Component | Calculation | Result |
|-----------|-------------|--------|
| Net GloBE Income | | €8,500,000 |
| SBIE | | €766,000 |
| Excess Profit | €8,500,000 − €766,000 | €7,734,000 |
| ETR | | 10.59% |
| Top-up Tax % | 15.00% − 10.59% | 4.41% |
| Initial Top-up Tax | €7,734,000 × 4.41% | **€341,069** |

**Example 3: Switzerland (Near Threshold)**

| Component | Calculation | Result |
|-----------|-------------|--------|
| Net GloBE Income | | €18,900,000 |
| SBIE | | €2,689,000 |
| Excess Profit | €18,900,000 − €2,689,000 | €16,211,000 |
| ETR | | 13.23% |
| Top-up Tax % | 15.00% − 13.23% | 1.77% |
| Initial Top-up Tax | €16,211,000 × 1.77% | **€287,135** |

---

## 5.4.3.5 Additional Top-Up Tax

### Sources of Additional Top-Up Tax

Additional Top-up Tax arises from adjustments to prior period calculations:

```
Additional Top-up Tax Sources:
│
├── DTL Recapture (Article 4.4.4)
│   └── DTLs not reversed within 5 years trigger recapture
│
├── Prior Period Errors
│   └── Corrections to previously filed calculations
│
├── Allocation Adjustments
│   └── Changes in ownership or structure
│
└── Recomputation Triggers
    ├── Tax audit adjustments
    ├── Transfer pricing corrections
    └── Amended tax returns
```

### DTL Recapture Mechanics

When a DTL subject to recapture fails to reverse within 5 years:

```
DTL Recapture Calculation:
├── Year 1: DTL of €1,000,000 recorded at 25% = €250,000 Covered Tax benefit
├── Years 2-5: DTL partially reverses, €600,000 remains unreversed
├── Year 6: Recapture triggered
│   ├── Unreversed DTL: €600,000
│   ├── Recaptured tax benefit: €600,000 × 25% = €150,000
│   ├── Original Year 1 ETR: Recalculated without €150,000
│   ├── New Top-up Tax % for Year 1: Increases
│   └── Additional Top-up Tax in Year 6: €X
└── Report as Additional Top-up Tax in current year GIR
```

### Calculator Data Entry

| Field | Cell Reference | Format | Example |
|-------|---------------|--------|---------|
| DTL Recapture Amount | J5 | Currency | €150,000 |
| Prior Period Adjustment | K5 | Currency | €0 |
| Other Additional Top-up | L5 | Currency | €0 |
| **Total Additional Top-up Tax** | M5 | =SUM(J5:L5) | **€150,000** |

---

## 5.4.3.6 QDMTT Offset

### Understanding QDMTT

A Qualified Domestic Minimum Top-up Tax (QDMTT) is a domestic tax that:

```
QDMTT Requirements:
├── Imposed by the jurisdiction on its own low-taxed entities
├── Calculated using GloBE-consistent methodology
├── Applies before IIR or UTPR
└── Reduces Top-up Tax collected by other jurisdictions
```

### QDMTT Offset Mechanics

```
QDMTT Offset Application:
├── QDMTT paid reduces Jurisdictional Top-up Tax
├── If QDMTT ≥ Top-up Tax, no IIR/UTPR collection
├── If QDMTT < Top-up Tax, residual collected under IIR/UTPR
└── QDMTT has first priority in collection hierarchy
```

### Calculator Data Entry

| Field | Cell Reference | Format | Example |
|-------|---------------|--------|---------|
| QDMTT Jurisdiction | N5 | Y/N | Y |
| QDMTT Amount Paid | O5 | Currency | €1,200,000 |
| QDMTT Offset Applied | P5 | Currency | =MIN(O5,I5+M5) | €1,200,000 |

### Worked Example: Ireland with QDMTT

Ireland introduced a QDMTT effective January 1, 2024. For GlobalCo:

| Component | Calculation | Result |
|-----------|-------------|--------|
| Initial Top-up Tax | | €1,536,721 |
| Additional Top-up Tax | | €0 |
| **Pre-QDMTT Top-up Tax** | | **€1,536,721** |
| QDMTT Paid by Irish Entities | | €1,400,000 |
| QDMTT Offset | MIN(€1,400,000, €1,536,721) | (€1,400,000) |
| **Residual Top-up Tax (IIR/UTPR)** | | **€136,721** |

---

## 5.4.3.7 Final Top-Up Tax Calculation

### Complete Formula Application

```
Final Jurisdictional Top-up Tax:
= Initial Top-up Tax
+ Additional Top-up Tax
− QDMTT Offset

Subject to:
├── Cannot be negative (minimum €0)
├── Represents amount to be collected under IIR/UTPR
└── Must be allocated per Section 5.4.4 rules
```

### Calculator Summary

**Tab:** `Section 3.3 - Top-Up Tax Summary`

| Field | Cell Reference | Formula | IE Example |
|-------|---------------|---------|------------|
| Jurisdiction | B5 | | IE |
| Initial Top-up Tax | I5 | From calculation | €1,536,721 |
| Additional Top-up Tax | M5 | From calculation | €0 |
| QDMTT Offset | P5 | From calculation | (€1,400,000) |
| **Final Jurisdictional Top-up Tax** | Q5 | =MAX(I5+M5-P5,0) | **€136,721** |

### Multi-Jurisdiction Summary

**GlobalCo Holdings - FY 2024 Top-Up Tax Summary:**

| Jurisdiction | ETR | Top-up % | Excess Profit | Initial TUT | Additional | QDMTT | Final TUT |
|--------------|-----|----------|---------------|-------------|------------|-------|-----------|
| Ireland | 12.48% | 2.52% | €60.98M | €1,537K | €0 | (€1,400K) | **€137K** |
| Switzerland | 13.23% | 1.77% | €16.21M | €287K | €0 | (€287K) | **€0** |
| Luxembourg | 10.59% | 4.41% | €7.73M | €341K | €0 | €0 | **€341K** |
| **Total** | | | | **€2,165K** | **€0** | **(€1,687K)** | **€478K** |

---

## 5.4.3.8 GIR Section 3.3 Data Fields Reference

### Complete Field List for Top-Up Tax Computation

**Top-Up Tax Percentage Fields:**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.3.1.1 | Jurisdictional ETR | Percentage | Yes |
| 3.3.1.2 | Minimum Rate (15%) | Percentage | Fixed |
| 3.3.1.3 | Top-up Tax Percentage | Percentage | Calculated |

**Excess Profit Fields:**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.3.2.1 | Net GloBE Income | Currency | Yes |
| 3.3.2.2 | Total SBIE | Currency | Yes |
| 3.3.2.3 | Excess Profit | Currency | Calculated |

**Top-Up Tax Calculation Fields:**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.3.3.1 | Initial Top-up Tax | Currency | Calculated |
| 3.3.3.2 | DTL Recapture Adjustment | Currency | If applicable |
| 3.3.3.3 | Prior Period Adjustments | Currency | If applicable |
| 3.3.3.4 | Other Additional Top-up Tax | Currency | If applicable |
| 3.3.3.5 | Total Additional Top-up Tax | Currency | Calculated |

**QDMTT Offset Fields:**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.3.4.1 | QDMTT Jurisdiction Indicator | Y/N | Yes |
| 3.3.4.2 | QDMTT Amount Paid | Currency | If applicable |
| 3.3.4.3 | QDMTT Offset Applied | Currency | Calculated |

**Final Top-Up Tax Fields:**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.3.5.1 | Pre-Offset Top-up Tax | Currency | Calculated |
| 3.3.5.2 | Final Jurisdictional Top-up Tax | Currency | Calculated |
| 3.3.5.3 | Collection Mechanism | IIR/UTPR | Yes |

---

## 5.4.3.9 Validation and Reconciliation

### Top-Up Tax Validation Checks

**Calculator Built-in Validations:**

| Validation | Formula | Expected Result |
|------------|---------|-----------------|
| Top-up % ≤ 15% | =IF(E5>0.15,"ERROR","OK") | OK |
| Excess Profit ≥ 0 | =IF(H5<0,"ERROR","OK") | OK |
| QDMTT ≤ Pre-Offset TUT | =IF(P5>I5+M5,"WARNING","OK") | OK |
| Final TUT ≥ 0 | =IF(Q5<0,"ERROR","OK") | OK |
| ETR + Top-up % = 15% | =IF(C5+E5<>0.15,"CHECK","OK") | OK |

### Reconciliation to Pillar Two Tax Calculations

The GIR Top-up Tax should reconcile to the MNE's actual Pillar Two tax liability:

```
Reconciliation Framework:
├── GIR Section 3 Total Top-up Tax
├── = Pillar Two Tax Provision (Accounting)
├── + Timing Differences (Deferred vs Current)
├── + Currency Translation Adjustments
└── = Tax Return/Payment Amounts

Document any differences with explanations.
```

---

## 5.4.3.10 Complex Scenarios

### Scenario 1: SBIE Exceeds GloBE Income

**Facts:** Jurisdiction has significant substance but low profits.

| Component | Amount |
|-----------|--------|
| Net GloBE Income | €5,000,000 |
| Eligible Payroll | €15,000,000 |
| Payroll Carve-out (9.8%) | €1,470,000 |
| Eligible Tangible Assets | €80,000,000 |
| Asset Carve-out (7.8%) | €6,240,000 |
| Total SBIE | €7,710,000 |
| **Excess Profit** | **€0** |

**Result:** No Top-up Tax due. Excess SBIE (€2,710,000) is lost.

### Scenario 2: ETR Exactly at 15%

**Facts:** Jurisdiction's ETR rounds to exactly 15.00%.

| Component | Calculation | Result |
|-----------|-------------|--------|
| GloBE Income | | €50,000,000 |
| Covered Taxes | | €7,500,000 |
| ETR | €7,500,000 ÷ €50,000,000 | 15.0000% |
| Top-up Tax % | 15.00% − 15.00% | 0.00% |
| **Top-up Tax** | | **€0** |

**Result:** No Top-up Tax due. ETR meets minimum exactly.

### Scenario 3: Multiple QDMTT Sources

**Facts:** Jurisdiction has QDMTT paid by multiple entities.

| Entity | QDMTT Paid |
|--------|------------|
| CE 1 | €500,000 |
| CE 2 | €300,000 |
| CE 3 | €200,000 |
| **Total QDMTT** | **€1,000,000** |

| Component | Calculation | Result |
|-----------|-------------|--------|
| Initial Top-up Tax | | €1,200,000 |
| Total QDMTT Offset | | (€1,000,000) |
| **Residual Top-up Tax** | | **€200,000** |

### Scenario 4: Additional Top-up Tax from DTL Recapture

**Facts:** Year 6 triggers recapture from Year 1 DTL.

| Component | Amount |
|-----------|--------|
| Year 1 Original ETR | 14.50% |
| Year 1 Original Top-up % | 0.50% |
| Year 1 Excess Profit | €30,000,000 |
| Year 1 Original Top-up Tax | €150,000 |
| DTL Recapture (Year 6) | €200,000 tax benefit |
| Year 1 Revised ETR | 13.83% |
| Year 1 Revised Top-up % | 1.17% |
| Year 1 Revised Top-up Tax | €351,000 |
| **Additional Top-up Tax (Year 6)** | **€201,000** |

---

## 5.4.3.11 Common Errors

### Error 1: Negative Top-Up Tax Percentage

**Problem:** Calculating negative percentage when ETR > 15%.

**Solution:**
```
Correct Formula: =MAX(0.15 - ETR, 0)
├── ETR = 20% → MAX(0.15 - 0.20, 0) = MAX(-0.05, 0) = 0%
└── Never report negative Top-up Tax %
```

### Error 2: Negative Excess Profit

**Problem:** Not flooring Excess Profit at zero when SBIE > Income.

**Solution:**
```
Correct Formula: =MAX(GloBE_Income - SBIE, 0)
├── If SBIE exceeds Income, Excess Profit = €0
└── Document the excess SBIE amount (lost)
```

### Error 3: QDMTT Offset Exceeds Top-up Tax

**Problem:** Reporting negative Final Top-up Tax after QDMTT.

**Solution:**
```
Correct Formula: =MAX(Pre_Offset_TUT - QDMTT, 0)
├── QDMTT can only reduce Top-up Tax to €0
├── Excess QDMTT is not refunded or carried forward
└── Floor Final Top-up Tax at €0
```

### Error 4: Missing Additional Top-up Tax

**Problem:** Not including DTL recapture or prior period adjustments.

**Solution:**
```
Completeness Check:
☐ Review DTL recapture tracking (Year 6+)
☐ Check for amended tax returns in prior periods
☐ Review audit adjustments impacting prior GIR
☐ Include all sources of Additional Top-up Tax
```

### Error 5: Incorrect QDMTT Attribution

**Problem:** Misallocating QDMTT between jurisdictions.

**Solution:**
```
QDMTT Attribution Rules:
├── QDMTT offsets Top-up Tax in the SAME jurisdiction only
├── Irish QDMTT cannot offset Luxembourg Top-up Tax
├── Aggregate QDMTT from all entities in jurisdiction
└── Document entity-level QDMTT payments
```

---

## 5.4.3.12 Top-Up Tax Computation Checklist

Use this checklist to ensure complete and accurate Top-up Tax computation:

**ETR and Top-Up Percentage:**

| # | Check Item | Status |
|---|------------|--------|
| 1 | ETR calculated for all jurisdictions with GloBE Income | ☐ |
| 2 | ETR rounded to fourth decimal place | ☐ |
| 3 | Top-up Tax % calculated for ETR < 15% | ☐ |
| 4 | Top-up Tax % floored at 0% | ☐ |

**Excess Profit:**

| # | Check Item | Status |
|---|------------|--------|
| 5 | Net GloBE Income correctly aggregated | ☐ |
| 6 | SBIE correctly calculated and deducted | ☐ |
| 7 | Excess Profit floored at €0 | ☐ |
| 8 | Excess SBIE documented (if applicable) | ☐ |

**Initial Top-Up Tax:**

| # | Check Item | Status |
|---|------------|--------|
| 9 | Initial Top-up Tax = Top-up % × Excess Profit | ☐ |
| 10 | Calculation verified by independent review | ☐ |

**Additional Top-Up Tax:**

| # | Check Item | Status |
|---|------------|--------|
| 11 | DTL recapture tracking reviewed | ☐ |
| 12 | Year 6+ recapture calculated | ☐ |
| 13 | Prior period adjustments identified | ☐ |
| 14 | Additional Top-up Tax documented | ☐ |

**QDMTT Offset:**

| # | Check Item | Status |
|---|------------|--------|
| 15 | QDMTT jurisdictions identified | ☐ |
| 16 | QDMTT amounts per entity verified | ☐ |
| 17 | QDMTT aggregated by jurisdiction | ☐ |
| 18 | QDMTT offset limited to Top-up Tax | ☐ |

**Final Top-Up Tax:**

| # | Check Item | Status |
|---|------------|--------|
| 19 | Final Top-up Tax = Initial + Additional − QDMTT | ☐ |
| 20 | Final Top-up Tax floored at €0 | ☐ |
| 21 | Collection mechanism identified (IIR/UTPR) | ☐ |
| 22 | Reconciliation to tax provision completed | ☐ |
| 23 | Multi-jurisdiction total calculated | ☐ |
| 24 | Tax director sign-off obtained | ☐ |

---

## 5.4.3.13 Key Takeaways

### Strategic Considerations for Top-Up Tax

1. **QDMTT is the First Line of Defence**
   - QDMTT jurisdictions retain Top-up Tax domestically
   - Monitor QDMTT enactment in key jurisdictions
   - Coordinate QDMTT planning with IIR/UTPR exposure

2. **SBIE Reduces Excess Profit**
   - High-substance jurisdictions benefit most
   - Transitional rates (9.8%/7.8%) provide significant relief
   - Plan substance allocation to maximize SBIE

3. **DTL Recapture is a Multi-Year Issue**
   - Establish tracking from Year 1
   - Monitor DTLs subject to 5-year recapture
   - Consider elective exclusion for long-term DTLs

4. **Near-Threshold ETRs Require Sensitivity Analysis**
   - Small changes can flip Top-up Tax status
   - Model impact of key assumptions
   - Document margin of safety

5. **Documentation is Critical for Audit Defence**
   - Maintain complete calculation workpapers
   - Document judgment calls and elections
   - Prepare for multi-jurisdiction inquiries

---

## Practice This Skill: GIR Top-Up Tax Calculator

Now that you understand the complete Top-up Tax computation, you can practice using the **GIR Top-Up Tax Calculator (GIR-003)** on tools.mojitax.com.

| Tool | Tool ID | Purpose |
|------|---------|---------|
| GIR Top-Up Tax Calculator | GIR-003 | Calculate Top-up Tax by combining ETR and SBIE to determine final liability |

**Demo Tool vs Professional Tool**

This is a demo tool for learning purposes. In professional practice, you would use enterprise Pillar Two software that handles multi-entity allocation, QDMTT offsets, and IIR/UTPR coordination. The demo tool helps you understand the calculation mechanics.

**To Practice:**

1. Go to tools.mojitax.com and find **GIR Top-Up Tax Calculator**
2. Use the GlobalTech Ireland data from **Case Study 1**:
   - GloBE Income: €45,000,000
   - Adjusted Covered Taxes: €5,625,000
   - Total SBIE: €1,769,000
   - QDMTT Amount: €0 (Ireland has no QDMTT in 2024)
3. Enter the values and calculate
4. **Expected Results:**
   - ETR: 12.5000%
   - Top-up Tax %: 2.5000%
   - Excess Profit: €43,231,000
   - Top-up Tax: €1,080,775

If your results differ, review the calculation steps in this section.

---

## Section Summary

The Top-Up Tax computation determines the final liability for each low-taxed jurisdiction. Key requirements include:

- **Top-up Tax Percentage:** 15% minus ETR (minimum 0%)
- **Excess Profit:** GloBE Income minus SBIE (minimum €0)
- **Initial Top-up Tax:** Excess Profit × Top-up Tax %
- **Additional Top-up Tax:** DTL recapture and prior period adjustments
- **QDMTT Offset:** Reduces Top-up Tax collected under IIR/UTPR
- **Final Top-up Tax:** Subject to allocation per Section 5.4.4

The GIR Completion Calculator automates these calculations while maintaining validation checks and audit documentation.

---

## Navigation

**Previous:** [Section 5.4.2: Substance-Based Income Exclusion](Section_05_04_02_Substance_Based_Income_Exclusion.md)

You have completed the Top-Up Tax computation. Continue with the Top-Up Tax allocation in the subsequent subsection.

**Return to:** [Table of Contents](00_Table_of_Contents.md)
