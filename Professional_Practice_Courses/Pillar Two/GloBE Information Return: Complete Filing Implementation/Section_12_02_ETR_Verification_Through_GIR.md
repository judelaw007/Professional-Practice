# Section 12.2: ETR Verification Through GIR

## Learning Objectives

By the end of this section, you will be able to:
- Use GIR data to verify jurisdictional ETR calculations
- Identify common discrepancies between calculated and reported ETRs
- Apply systematic resolution procedures for ETR variances
- Implement ETR verification controls as part of the GIR preparation process
- Document ETR verification for audit defence purposes

---

## Introduction

The Effective Tax Rate (ETR) is the cornerstone of Pillar Two compliance. The GloBE ETR determines whether a jurisdiction triggers Top-up Tax liability:

**Fundamental Rule:**
> If Jurisdictional ETR < 15% Minimum Rate → Top-up Tax applies

The GIR provides a structured framework for reporting ETR calculations, but the complexity of the underlying rules creates significant risk of calculation errors. This section establishes a systematic approach to ETR verification using GIR data.

---

## Part 1: Understanding the GloBE ETR Calculation

### 1.1 ETR Formula

**Basic ETR Calculation (Article 5.1):**

```
                    Adjusted Covered Taxes (Jurisdiction)
Jurisdictional ETR = ────────────────────────────────────────
                    Net GloBE Income (Jurisdiction)
```

**Expression:** Percentage rounded to the fourth decimal place (e.g., 14.2567%)

### 1.2 ETR Components

**Numerator: Adjusted Covered Taxes**

| Component | Description | Article Reference |
|-----------|-------------|-------------------|
| Current tax expense | Tax expense per financial accounts | Art. 4.1 |
| + Deferred tax adjustment | Net movement in deferred taxes | Art. 4.4 |
| - Excluded taxes | Taxes on excluded income | Art. 4.1.3 |
| ± UTP adjustments | Uncertain tax position timing | Art. 4.6 |
| - Recaptured DTLs | 5-year rule recapture | Art. 4.4.4 |
| = **Adjusted Covered Taxes** | | |

**Denominator: Net GloBE Income**

| Component | Description | Article Reference |
|-----------|-------------|-------------------|
| FANIL | Financial Accounting Net Income/Loss | Art. 3.1 |
| + Tax expense add-back | Net tax expense reversed | Art. 3.2.1(a) |
| - Excluded dividends | Qualifying dividend exclusion | Art. 3.2.1(b) |
| - Excluded equity gains | Qualifying equity exclusion | Art. 3.2.1(c) |
| ± Other adjustments | Per Article 3.2 | Art. 3.2 |
| = **GloBE Income** | Per Constituent Entity | |
| Σ GloBE Income - Σ GloBE Loss | Jurisdictional aggregation | Art. 5.1.2 |
| = **Net GloBE Income** | Jurisdictional total | |

### 1.3 Critical ETR Thresholds

| ETR Result | Consequence | Action Required |
|------------|-------------|-----------------|
| ETR ≥ 15.0000% | No Top-up Tax | Report in GIR Section 2 |
| ETR < 15.0000% | Top-up Tax triggered | Calculate Top-up Tax |
| ETR = Negative | Special rules apply | Excess Negative Tax Expense |
| Net GloBE Loss | No ETR calculation needed | ETR = N/A |

### 1.4 Transition Rate for Safe Harbour

For Transitional CbCR Safe Harbour purposes, the Simplified ETR test uses different thresholds:

| Fiscal Year Beginning | Transition Rate |
|-----------------------|-----------------|
| 2023-2024 | 15% |
| 2025 | 16% |
| 2026 | 17% |

---

## Part 2: Using GIR Data to Verify ETR Calculations

### 2.1 GIR Section 2 ETR Data Points

The GIR captures the following ETR-related data for each jurisdiction:

| GIR Field | Description | Verification Use |
|-----------|-------------|------------------|
| GloBE Revenue | Total revenue | Reasonableness check |
| GloBE Income/(Loss) | Net jurisdictional income | ETR denominator |
| Covered Taxes | Current taxes included | ETR numerator component |
| Adjusted Covered Taxes | After all adjustments | ETR numerator |
| ETR | Calculated rate | Primary verification point |
| SBIE | Substance carve-out | Excess Profit check |
| Top-up Tax % | 15% - ETR | Consequential check |
| Jurisdictional Top-up Tax | Top-up Tax % × Excess Profit | Final calculation |

### 2.2 ETR Verification Framework

**Three-Level Verification:**

```
Level 1: Mathematical Verification
─────────────────────────────────
□ ETR = Adjusted Covered Taxes ÷ GloBE Income
□ Calculation matches to 4 decimal places
□ Rounding correctly applied

Level 2: Component Verification
─────────────────────────────────
□ Adjusted Covered Taxes reconciles to workpapers
□ GloBE Income reconciles to workpapers
□ All adjustments correctly applied

Level 3: Consequential Verification
─────────────────────────────────
□ Top-up Tax % = 15% - ETR (if ETR < 15%)
□ Excess Profit = GloBE Income - SBIE
□ Top-up Tax = Top-up Tax % × Excess Profit
```

### 2.3 ETR Verification Workpaper

**Jurisdictional ETR Verification Template:**

| Jurisdiction: | [Name] | Code: | [XX] |
|---------------|--------|-------|------|

**A. Denominator Verification (GloBE Income)**

| Ref | Element | Per Workpapers | Per GIR | Variance | Status |
|-----|---------|----------------|---------|----------|--------|
| A.1 | Entity 1 GloBE Income | ___ | ___ | ___ | □ |
| A.2 | Entity 2 GloBE Income | ___ | ___ | ___ | □ |
| A.3 | Entity 3 GloBE Income | ___ | ___ | ___ | □ |
| A.4 | **Total GloBE Income** | ___ | ___ | ___ | □ |
| A.5 | Less: GloBE Losses | ___ | ___ | ___ | □ |
| A.6 | **Net GloBE Income** | ___ | ___ | ___ | □ |

**B. Numerator Verification (Adjusted Covered Taxes)**

| Ref | Element | Per Workpapers | Per GIR | Variance | Status |
|-----|---------|----------------|---------|----------|--------|
| B.1 | Current tax expense | ___ | ___ | ___ | □ |
| B.2 | Deferred tax adjustment | ___ | ___ | ___ | □ |
| B.3 | Less: Excluded taxes | ___ | ___ | ___ | □ |
| B.4 | UTP adjustments | ___ | ___ | ___ | □ |
| B.5 | DTL recapture | ___ | ___ | ___ | □ |
| B.6 | **Adjusted Covered Taxes** | ___ | ___ | ___ | □ |

**C. ETR Calculation Verification**

| Ref | Element | Per Workpapers | Per GIR | Variance | Status |
|-----|---------|----------------|---------|----------|--------|
| C.1 | ETR (B.6 ÷ A.6) | ___% | ___% | ___% | □ |
| C.2 | Top-up Tax % (15% - C.1) | ___% | ___% | ___% | □ |
| C.3 | SBIE Amount | ___ | ___ | ___ | □ |
| C.4 | Excess Profit (A.6 - C.3) | ___ | ___ | ___ | □ |
| C.5 | Jurisdictional Top-up Tax | ___ | ___ | ___ | □ |

**D. Sign-Off**

| Verification | Completed | Initials | Date |
|--------------|-----------|----------|------|
| Mathematical accuracy | □ | ___ | ___ |
| Component reconciliation | □ | ___ | ___ |
| Consequential checks | □ | ___ | ___ |
| Variances documented | □ | ___ | ___ |

---

## Part 3: Identifying Discrepancies

### 3.1 Common ETR Discrepancy Categories

**Category 1: Mathematical Errors**

| Error Type | Description | Detection Method |
|------------|-------------|------------------|
| Division error | Wrong formula applied | Recalculate manually |
| Rounding error | Incorrect decimal places | Check rounding methodology |
| Sign error | Positive/negative confusion | Trace to source |
| Aggregation error | Sum incorrect | Re-sum components |

**Category 2: GloBE Income Errors**

| Error Type | Description | Impact on ETR |
|------------|-------------|---------------|
| FANIL extraction error | Wrong starting point | Denominator error |
| Missing adjustment | Article 3.2 item omitted | Denominator over/understated |
| Excluded income included | Dividends/equity not excluded | Denominator overstated → ETR understated |
| Intercompany not eliminated | Double-counting | Denominator overstated |
| Entity omission | CE income missing | Denominator understated → ETR overstated |

**Category 3: Covered Taxes Errors**

| Error Type | Description | Impact on ETR |
|------------|-------------|---------------|
| Current tax extraction | Wrong tax figure used | Numerator error |
| Deferred tax methodology | Incorrect DTL/DTA treatment | Numerator error |
| DTL recapture missed | 5-year rule not applied | Numerator overstated → ETR overstated |
| WHT allocation | Wrong jurisdiction | Numerator misallocated |
| UTP timing | Wrong period recognised | Numerator timing error |
| QRTC treatment | Credit in wrong location | Numerator vs. denominator |

**Category 4: Structural Errors**

| Error Type | Description | Impact on ETR |
|------------|-------------|---------------|
| Wrong jurisdiction | CE allocated incorrectly | Both numerator and denominator |
| Ownership error | Allocation percentage wrong | Proportional impact |
| Excluded entity error | CE wrongly included/excluded | Complete miscalculation |
| Fiscal year mismatch | Different periods used | Comparability failure |

### 3.2 ETR Variance Analysis Matrix

**Variance Impact Assessment:**

| Variance Type | ETR Impact | Top-up Tax Impact | Risk Level |
|---------------|------------|-------------------|------------|
| Numerator ↑ | ETR ↑ | Top-up Tax ↓ | Low (conservative) |
| Numerator ↓ | ETR ↓ | Top-up Tax ↑ | High (underpayment) |
| Denominator ↑ | ETR ↓ | Top-up Tax ↑ | High (underpayment) |
| Denominator ↓ | ETR ↑ | Top-up Tax ↓ | Low (conservative) |

**Critical Variance Scenarios:**

| Scenario | Calculated ETR | Actual ETR | Consequence |
|----------|----------------|------------|-------------|
| False positive | 14.8% | 15.2% | Unnecessary Top-up Tax |
| False negative | 15.2% | 14.8% | Missed Top-up Tax liability |
| Near threshold | 14.9% - 15.1% | Unknown | Requires precision verification |

### 3.3 Tax Incentive and Credit Errors

**Qualified Refundable Tax Credit (QRTC) Treatment:**

| Treatment | Correct Position | Common Error |
|-----------|------------------|--------------|
| QRTC | Add to GloBE Income (denominator) | Reduce Covered Taxes (numerator) |
| Non-QRTC | Reduce Covered Taxes (numerator) | Add to GloBE Income |
| Timing | When credit granted | When cash received |

**Impact Analysis:**

```
Correct QRTC Treatment:
GloBE Income = 100 + 10 (QRTC) = 110
Covered Taxes = 20
ETR = 20/110 = 18.18%

Incorrect QRTC Treatment (as tax reduction):
GloBE Income = 100
Covered Taxes = 20 - 10 = 10
ETR = 10/100 = 10.00%

Difference: 8.18% ETR reduction (significant Top-up Tax impact)
```

### 3.4 Deferred Tax Adjustment Errors

**5-Year DTL Recapture Rule:**

| Year | DTL Created | DTL Reversed | Recapture Required |
|------|-------------|--------------|-------------------|
| Year 1 | €1,000,000 | — | — |
| Year 2 | — | — | — |
| Year 3 | — | — | — |
| Year 4 | — | — | — |
| Year 5 | — | — | — |
| Year 6 | — | €0 | Yes - €1,000,000 |

**Recapture Impact:**
- Original Year 1 ETR must be recalculated
- Covered Taxes reduced by recaptured DTL
- May trigger retrospective Top-up Tax liability

---

## Part 4: Resolution Procedures

### 4.1 Discrepancy Resolution Workflow

```
Step 1: Identify Discrepancy
            │
            ▼
Step 2: Quantify Impact
            │
            ├── <1% variance → Document only
            │
            ├── 1-5% variance → Investigate
            │
            └── >5% variance → Escalate
            │
            ▼
Step 3: Root Cause Analysis
            │
            ├── Data error → Correct source
            │
            ├── Methodology error → Revise approach
            │
            └── System error → Fix and reprocess
            │
            ▼
Step 4: Correction
            │
            ├── Pre-filing → Correct GIR
            │
            └── Post-filing → File amendment
            │
            ▼
Step 5: Prevention
            │
            └── Update controls
```

### 4.2 Resolution Documentation

**Discrepancy Resolution Form:**

| Field | Entry |
|-------|-------|
| Jurisdiction | ___ |
| Discrepancy ID | ___ |
| Date Identified | ___ |
| Identified By | ___ |

**Discrepancy Details:**

| Element | Original | Corrected | Variance |
|---------|----------|-----------|----------|
| GloBE Income | ___ | ___ | ___ |
| Covered Taxes | ___ | ___ | ___ |
| ETR | ___% | ___% | ___% |
| Top-up Tax | ___ | ___ | ___ |

**Root Cause Analysis:**

| Question | Response |
|----------|----------|
| What was the error? | ___ |
| Where did it originate? | ___ |
| Why did it occur? | ___ |
| When was it introduced? | ___ |
| Who is responsible for correction? | ___ |

**Resolution:**

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| ___ | ___ | ___ | □ |
| ___ | ___ | ___ | □ |

**Prevention:**

| Control Enhancement | Implementation Date |
|--------------------|---------------------|
| ___ | ___ |

**Sign-Off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Preparer | ___ | ___ | ___ |
| Reviewer | ___ | ___ | ___ |
| Approver | ___ | ___ | ___ |

### 4.3 Specific Resolution Procedures

**GloBE Income Corrections:**

| Error Type | Resolution Steps |
|------------|------------------|
| FANIL error | 1. Obtain correct FANIL from finance<br>2. Re-apply all adjustments<br>3. Recalculate jurisdictional total |
| Missing adjustment | 1. Identify omitted adjustment<br>2. Calculate correct amount<br>3. Add to GloBE Income calculation |
| Excluded income error | 1. Review dividend/equity exclusion criteria<br>2. Apply correct exclusion<br>3. Document basis |

**Covered Taxes Corrections:**

| Error Type | Resolution Steps |
|------------|------------------|
| Current tax error | 1. Reconcile to tax provision<br>2. Trace to local tax return<br>3. Correct extraction |
| Deferred tax error | 1. Recalculate DTL/DTA movement<br>2. Apply 15% cap where required<br>3. Check recapture rules |
| Allocation error | 1. Review allocation methodology<br>2. Apply correct push-down<br>3. Document basis |

### 4.4 Near-Threshold Jurisdictions

**Special Procedures for ETR 14.5% - 15.5%:**

| Procedure | Purpose |
|-----------|---------|
| Enhanced precision | Calculate to 6+ decimal places |
| Independent recalculation | Second person verification |
| Source document review | Verify all inputs to original source |
| Sensitivity analysis | Test impact of key assumptions |
| Position paper | Document judgment calls |

**Sensitivity Analysis Template:**

| Variable | Base Case | Sensitivity +5% | Sensitivity -5% |
|----------|-----------|-----------------|-----------------|
| GloBE Income | ___ | ___ | ___ |
| Covered Taxes | ___ | ___ | ___ |
| ETR | ___% | ___% | ___% |
| Top-up Tax Impact | ___ | ___ | ___ |

---

## Part 5: ETR Verification Controls

### 5.1 Control Framework

**Preventive Controls:**

| Control | Objective | Frequency |
|---------|-----------|-----------|
| Standardised templates | Consistent calculation methodology | Per filing |
| Data validation rules | Catch input errors | Automated |
| Four-eyes review | Independent verification | Per jurisdiction |
| Training | Competent preparers | Annual |

**Detective Controls:**

| Control | Objective | Frequency |
|---------|-----------|-----------|
| Analytical review | Identify anomalies | Per jurisdiction |
| Year-on-year comparison | Detect unusual changes | Per filing |
| Cross-jurisdictional comparison | Identify outliers | Per filing |
| Reconciliation | Verify to source | Per filing |

### 5.2 ETR Analytical Review

**Reasonableness Checks:**

| Check | Expected Range | Investigation Trigger |
|-------|----------------|----------------------|
| ETR vs. statutory rate | Within 5% of statutory | Variance >5% |
| ETR vs. prior year | Within 2% of prior year | Variance >2% |
| ETR vs. group average | Within 10% of average | Variance >10% |
| GloBE Income vs. CbCR PBT | Within 10% | Variance >10% |
| Covered Taxes vs. CbCR tax | Within 10% | Variance >10% |

**Year-on-Year Analysis:**

| Jurisdiction | FY2024 ETR | FY2025 ETR | Change | Explanation Required |
|--------------|------------|------------|--------|---------------------|
| ___ | ___% | ___% | ___% | □ Yes / □ No |
| ___ | ___% | ___% | ___% | □ Yes / □ No |

### 5.3 ETR Verification Checklist

**Pre-Filing ETR Verification Checklist:**

| Section | Check | Verified | Reviewer |
|---------|-------|----------|----------|
| **A. Data Integrity** ||||
| A.1 | GloBE Income extracted from approved source | □ | ___ |
| A.2 | Covered Taxes extracted from approved source | □ | ___ |
| A.3 | All CEs included in jurisdictional totals | □ | ___ |
| A.4 | Currency conversion rates verified | □ | ___ |
| **B. Calculation Accuracy** ||||
| B.1 | ETR formula correctly applied | □ | ___ |
| B.2 | Rounding to 4 decimal places | □ | ___ |
| B.3 | Net GloBE Loss jurisdictions = N/A | □ | ___ |
| B.4 | Top-up Tax % = 15% - ETR (where ETR < 15%) | □ | ___ |
| **C. Adjustment Completeness** ||||
| C.1 | All Article 3.2 adjustments applied | □ | ___ |
| C.2 | Deferred tax adjustments complete | □ | ___ |
| C.3 | DTL recapture rules applied | □ | ___ |
| C.4 | QRTC correctly treated | □ | ___ |
| **D. Reconciliation** ||||
| D.1 | ETR reconciled to tax provision | □ | ___ |
| D.2 | Variances documented | □ | ___ |
| D.3 | Near-threshold jurisdictions reviewed | □ | ___ |
| **E. Sign-Off** ||||
| E.1 | Preparer sign-off obtained | □ | ___ |
| E.2 | Reviewer sign-off obtained | □ | ___ |
| E.3 | Approver sign-off obtained | □ | ___ |

---

## Part 6: Special Considerations

### 6.1 Stock-Based Compensation

**Election Impact on ETR:**

| Treatment | GloBE Income | Covered Taxes | ETR Impact |
|-----------|--------------|---------------|------------|
| Book expense (default) | Reduced by expense | Tax benefit included | Standard |
| Election: Use tax deduction | Different reduction | Different benefit | Variable |

**Verification Point:**
Confirm election consistency across all CEs and fiscal years.

### 6.2 Loss Jurisdictions

**Treatment:**

| Scenario | ETR Calculation | GIR Treatment |
|----------|-----------------|---------------|
| Net GloBE Loss | Not calculated | Report loss amount |
| GloBE Loss with Covered Taxes | Negative ETR possible | Special handling |
| Loss carryforward | Affects future ETR | Track for NMCE |

### 6.3 QDMTT Interaction

**ETR After QDMTT:**

| Step | Calculation |
|------|-------------|
| 1. Calculate initial ETR | Covered Taxes ÷ GloBE Income |
| 2. Determine QDMTT | If ETR < 15%, QDMTT applies |
| 3. QDMTT becomes Covered Tax | Included in next calculation |
| 4. Recalculate if needed | May iterate for final ETR |

---

## Key Takeaways

1. **ETR is the trigger**: The 15% threshold determines Top-up Tax liability - accuracy is critical

2. **Four decimal places**: ETR must be calculated and reported to 0.0001% precision

3. **Systematic verification**: Use three-level verification (mathematical, component, consequential)

4. **Near-threshold scrutiny**: Jurisdictions with ETR 14.5%-15.5% require enhanced procedures

5. **QRTC treatment matters**: Incorrect treatment of tax credits significantly impacts ETR

6. **DTL recapture**: The 5-year rule can retrospectively change prior year ETRs

7. **Document everything**: All variances, resolutions, and judgment calls must be documented

8. **Preventive controls**: Standardised templates and training prevent errors before they occur

---

## Further Reading and Resources

- [oecdpillars.com: ETR Calculation and Top-up Tax](https://oecdpillars.com/pillar-tab/etr-calculation-and-top-up-tax-2/)
- [OECD: GloBE Rules Fact Sheets](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/pillar-two-globe-rules-fact-sheets.pdf)
- [EY: Why 15% ETR May Not Avoid Global Minimum Tax](https://www.ey.com/en_us/insights/tax/why-a-15-percent-financial-statement-tax-rate-may-not-avoid-global-minimum-tax)
- [oecdpillars.com: Qualified Refundable Tax Credits](https://oecdpillars.com/pillar-tab/qualified-refundable-tax-credits/)
- [Deloitte: Pillar Two FAQ](https://dart.deloitte.com/USDART/home/publications/deloitte/financial-reporting-alerts/2024/faq-pillar-two-international-tax-oecd)
- [KPMG: Pillar Two and Tax Incentives](https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/02/pillar-two-and-tax-incentives-jan-2025.pdf)

---

*End of Section 12.2*
