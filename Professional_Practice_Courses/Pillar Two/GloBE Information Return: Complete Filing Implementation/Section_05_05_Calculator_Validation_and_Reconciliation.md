# Section 5.5: Calculator Validation and Reconciliation

## Introduction

Before generating the XML file for submission, rigorous validation and reconciliation procedures are essential to ensure GIR accuracy and avoid rejection by tax authorities. The OECD has established comprehensive validation rules, and tax authorities are increasingly identifying common filing errors that can result in penalties and resubmission requirements.

This section provides step-by-step guidance for validating GIR data using the Calculator's built-in checks, reconciling to underlying financial and tax records, and preparing for tax authority review.

**Learning Objectives:**
- Execute comprehensive validation checks across all GIR sections
- Interpret and resolve validation error messages
- Reconcile GIR data to financial statements, tax provisions, and CbCR
- Prepare documentation for audit defence
- Complete final review procedures before XML generation

---

## 5.5.1 Validation Framework Overview

### OECD Validation Architecture

The OECD has established a structured validation framework for GIR data quality:

```
GIR Validation Levels:
│
├── Level 1: File-Level Validation
│   ├── XML schema compliance
│   ├── File structure and formatting
│   ├── Mandatory element presence
│   └── Character encoding (UTF-8)
│
├── Level 2: Record-Level Validation
│   ├── Field format and data type
│   ├── Value range compliance
│   ├── Conditional field logic
│   └── Cross-reference integrity
│
├── Level 3: Business Logic Validation
│   ├── Mathematical accuracy
│   ├── Cross-section consistency
│   ├── Jurisdictional reasonableness
│   └── Year-over-year comparison
│
└── Level 4: Reconciliation Validation
    ├── Financial statement tie-out
    ├── Tax provision alignment
    ├── CbCR consistency
    └── Prior year continuity
```

### GIR Status Message Schema

The OECD has developed a standardized error reporting mechanism:

```
GIR Status Message Framework:
├── File-Level Errors: Entire file rejected
├── Record-Level Errors: Specific records flagged
├── Warning Messages: Data accepted but flagged for review
└── Correction Instructions: Guidance for resubmission
```

---

### Calculator Validation Dashboard

**Tab:** `Validation Dashboard`

The GIR Completion Calculator includes a comprehensive validation dashboard:

| Section | Total Checks | Pass | Fail | Warning |
|---------|-------------|------|------|---------|
| Section 1: MNE Group Information | 35 | 33 | 1 | 1 |
| Section 2: Safe Harbours | 24 | 24 | 0 | 0 |
| Section 3: GloBE Computations | 85 | 82 | 2 | 1 |
| Cross-Section Checks | 20 | 18 | 1 | 1 |
| **Total** | **164** | **157** | **4** | **3** |

**Status Indicators:**

| Status | Colour | Meaning |
|--------|--------|---------|
| PASS | Green | Validation passed |
| FAIL | Red | Critical error - must resolve before filing |
| WARNING | Amber | Review recommended - may proceed with justification |
| N/A | Grey | Not applicable based on elections/exclusions |

---

## 5.5.2 Section 1 Validation Checks

### Filing Constituent Entity Validation

**Checks for FCE Information:**

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S1-001 | FCE TIN format valid | Matches jurisdiction TIN pattern | Verify TIN with local records |
| S1-002 | FCE jurisdiction code valid | ISO 3166-1 alpha-2 | Use standard country codes |
| S1-003 | FCE name not blank | LEN(FCE_Name) > 0 | Enter legal entity name |
| S1-004 | Fiscal year end format | Valid date (DD/MM/YYYY) | Use correct date format |
| S1-005 | Accounting standard specified | Dropdown selection made | Select IFRS/US GAAP/Other |

### UPE Information Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S1-010 | UPE identified | UPE_Name not blank | Enter UPE legal name |
| S1-011 | UPE TIN or NOTIN | TIN entered OR "NOTIN" flag | Use NOTIN if no TIN issued |
| S1-012 | UPE jurisdiction valid | ISO 3166-1 alpha-2 | Verify UPE residence |
| S1-013 | UPE type specified | UPE/POPE/IPE selected | Confirm parent entity type |

### Corporate Structure Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S1-020 | All CEs have unique IDs | No duplicate CE identifiers | Assign unique identifiers |
| S1-021 | CE jurisdiction valid | All use ISO codes | Standardize jurisdiction codes |
| S1-022 | Ownership % ≤ 100% | Sum of ownership ≤ 100% per CE | Review ownership structure |
| S1-023 | Entity type specified | GloBE status code entered | Select from valid codes |
| S1-024 | Excluded entities flagged | Exclusion reason documented | Document exclusion basis |
| S1-025 | Flow-through entities identified | FTE indicator set | Review entity classifications |

### Summary Information Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S1-030 | ETR range populated | For all Section 3 jurisdictions | Complete ETR for each |
| S1-031 | ETR range valid | 0% to 30%+ bands used | Use standard bands |
| S1-032 | Top-up Tax range populated | For low-taxed jurisdictions | Complete Top-up ranges |
| S1-033 | Reason if no ETR | GloBE Loss documented | Explain N/A ETR |

---

## 5.5.3 Section 2 Validation Checks

### Safe Harbour Election Validation

**Transitional CbCR Safe Harbour:**

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S2-001 | Transition period valid | FY begins ≤ 31 Dec 2026 | Verify fiscal year eligibility |
| S2-002 | CbCR data source documented | Data reference provided | Link to filed CbCR |
| S2-003 | Three tests calculated | All three test results shown | Complete all test calculations |
| S2-004 | Qualifying test identified | At least one test passes | Document qualifying test |
| S2-005 | Prior year exit check | "Once out" rule verified | Check historical elections |
| S2-006 | Transition rate correct | 15%/16%/17% by year | Apply correct year's rate |

**QDMTT Safe Harbour:**

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S2-010 | QDMTT jurisdiction valid | On enacted QDMTT list | Verify QDMTT status |
| S2-011 | Three standards confirmed | Accounting, Consistency, Admin | Document standard compliance |
| S2-012 | QDMTT amount entered | Currency value provided | Enter QDMTT liability |
| S2-013 | Switch-off rule applied | Section 3 reduced appropriately | Verify Section 3 scope |

### Exclusion Documentation Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S2-020 | Exclusion type valid | From approved list | Use standard exclusion codes |
| S2-021 | Rationale documented | Free text explanation provided | Enter detailed rationale |
| S2-022 | Supporting reference | Document reference included | Attach supporting evidence |
| S2-023 | Section 1 consistency | Excluded in both sections | Cross-check Section 1 |

---

## 5.5.4 Section 3 Validation Checks

### ETR Computation Validation

**GloBE Income Checks:**

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S3-001 | FANIL entered | Starting point not blank | Enter financial accounts data |
| S3-002 | Adjustments documented | Non-zero adjustments explained | Document all adjustments |
| S3-003 | Entity totals = Jurisdiction | Sum of CE = Jurisdiction total | Verify aggregation |
| S3-004 | GloBE Income sign logical | Loss where expected | Review negative income |
| S3-005 | Currency consistent | All EUR or group currency | Convert to standard currency |

**Covered Taxes Checks:**

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S3-010 | Current tax reasonable | Within expected range | Compare to statutory rate |
| S3-011 | Deferred tax cap applied | DTA ≤ 15% rate equivalent | Apply minimum rate cap |
| S3-012 | DTL recapture tracked | 5-year tracking active | Verify recapture schedule |
| S3-013 | Tax credits classified | Qualified vs non-qualified | Review credit treatment |
| S3-014 | Total = Current + Deferred | Mathematical accuracy | Verify calculation |

**ETR Calculation Checks:**

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S3-020 | ETR formula correct | Covered Taxes ÷ GloBE Income | Verify formula |
| S3-021 | ETR rounded correctly | Four decimal places | Apply standard rounding |
| S3-022 | ETR vs statutory reasonable | Within expected deviation | Document variance |
| S3-023 | GloBE Loss = No ETR | ETR blank if loss | Confirm N/A treatment |
| S3-024 | ETR range matches | Summary = Detail ETR | Cross-check Section 1 |

### SBIE Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S3-030 | Payroll data complete | All CEs with payroll entered | Complete payroll data |
| S3-031 | Payroll rate correct | 9.8%/9.6%/9.4% by year | Apply transitional rate |
| S3-032 | Asset data complete | Opening and closing values | Enter both values |
| S3-033 | Asset rate correct | 7.8%/7.6%/7.4% by year | Apply transitional rate |
| S3-034 | Average calculated | (Opening + Closing) ÷ 2 | Verify average formula |
| S3-035 | Location adjustments | Pro-rata if < 50% time | Apply location rules |
| S3-036 | SBIE total = Components | Payroll + Assets carve-out | Verify summation |

### Top-Up Tax Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S3-040 | Top-up % = 15% - ETR | Mathematical accuracy | Verify percentage |
| S3-041 | Top-up % ≥ 0 | Floor at zero | Apply minimum |
| S3-042 | Excess Profit = Income - SBIE | Mathematical accuracy | Verify calculation |
| S3-043 | Excess Profit ≥ 0 | Floor at zero | Apply minimum |
| S3-044 | Initial TUT correct | Top-up % × Excess Profit | Verify multiplication |
| S3-045 | QDMTT offset ≤ TUT | Cannot exceed Top-up Tax | Apply offset limit |
| S3-046 | Final TUT ≥ 0 | Floor at zero | Apply minimum |

### Allocation Validation

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| S3-050 | Collection mechanism specified | IIR/UTPR/QDMTT identified | Select mechanism |
| S3-051 | IIR ownership traced | Chain to UPE documented | Map ownership |
| S3-052 | UTPR formula correct | 50% employees + 50% assets | Verify formula |
| S3-053 | UTPR % sums to 100% | All UTPR jurisdictions | Check total allocation |
| S3-054 | Total allocation = TUT | Sum of allocations = Total | Reconcile amounts |

---

## 5.5.5 Cross-Section Validation

### Section 1 to Section 3 Consistency

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| X-001 | All Section 1 CEs in Section 3 | Unless excluded | Verify completeness |
| X-002 | Jurisdiction count matches | Section 1 = Section 3 | Reconcile jurisdictions |
| X-003 | ETR Summary matches Section 3 | S1 ETR range = S3 ETR | Cross-verify ETR |
| X-004 | Excluded entities not in S3 | Exclusions honored | Verify exclusions |

### Section 2 to Section 3 Consistency

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| X-010 | Safe harbour = No Section 3 | If elected, S3 not required | Verify switch-off |
| X-011 | QDMTT offset matches | S2 QDMTT = S3 offset | Reconcile amounts |
| X-012 | Exclusions reduce S3 scope | Exclusions reflected | Verify S3 reduction |

### Mathematical Consistency

| Check ID | Description | Formula/Logic | Resolution |
|----------|-------------|---------------|------------|
| X-020 | GloBE Income aggregation | Sum of CEs = Jurisdiction | Verify totals |
| X-021 | Covered Taxes aggregation | Sum of CEs = Jurisdiction | Verify totals |
| X-022 | Top-up Tax aggregation | Sum = Total liability | Verify group total |
| X-023 | Allocation reconciles | QDMTT + IIR + UTPR = Total | Full reconciliation |

---

## 5.5.6 Running Validation Checks

### Calculator Validation Procedure

**Step 1: Navigate to Validation Dashboard**

Open the `Validation Dashboard` tab in your GIR Completion Calculator.

**Step 2: Run All Checks**

Click the **[Run All Validations]** button to execute all validation checks.

**Step 3: Review Results Summary**

| Category | Count | Action Required |
|----------|-------|-----------------|
| Critical Errors (FAIL) | X | Must resolve before filing |
| Warnings (WARNING) | X | Review and document |
| Passed (PASS) | X | No action required |

**Step 4: Address Critical Errors**

For each FAIL status:

```
Error Resolution Process:
├── Step 1: Click error code to navigate to source cell
├── Step 2: Review error message and guidance
├── Step 3: Correct the underlying data
├── Step 4: Re-run validation for that check
└── Step 5: Document correction in audit trail
```

**Step 5: Review Warnings**

For each WARNING status:

```
Warning Review Process:
├── Step 1: Understand the warning nature
├── Step 2: Determine if data is correct
├── Step 3: If correct, document justification
├── Step 4: If incorrect, make correction
└── Step 5: Retain warning documentation
```

---

### Common Error Codes and Resolutions

**Section 1 Errors:**

| Error Code | Message | Common Cause | Resolution |
|------------|---------|--------------|------------|
| ERR-S1-001 | Invalid TIN format | TIN doesn't match country pattern | Verify TIN with local records |
| ERR-S1-020 | Duplicate CE identifier | Same ID used twice | Assign unique IDs |
| ERR-S1-022 | Ownership exceeds 100% | Sum of ownership > 100% | Review ownership chain |
| ERR-S1-024 | Exclusion reason missing | Excluded entity without rationale | Document exclusion basis |

**Section 2 Errors:**

| Error Code | Message | Common Cause | Resolution |
|------------|---------|--------------|------------|
| ERR-S2-001 | Transition period invalid | FY outside safe harbour window | Check fiscal year dates |
| ERR-S2-005 | Prior exit not addressed | "Once out" rule triggered | Document exit status |
| ERR-S2-010 | QDMTT jurisdiction invalid | Country not on QDMTT list | Verify QDMTT enactment |

**Section 3 Errors:**

| Error Code | Message | Common Cause | Resolution |
|------------|---------|--------------|------------|
| ERR-S3-001 | FANIL missing | No starting income entered | Enter financial data |
| ERR-S3-011 | DTA cap not applied | DTA recorded > 15% rate | Recalculate DTA |
| ERR-S3-021 | ETR rounding error | More than 4 decimal places | Apply standard rounding |
| ERR-S3-041 | Negative Top-up % | ETR > 15% but Top-up calculated | Floor at zero |
| ERR-S3-054 | Allocation mismatch | Sum ≠ Total Top-up Tax | Reconcile allocation |

**Cross-Section Errors:**

| Error Code | Message | Common Cause | Resolution |
|------------|---------|--------------|------------|
| ERR-X-001 | CE missing from Section 3 | Entity in S1 not in S3 | Add to S3 or exclude |
| ERR-X-003 | ETR range mismatch | S1 summary ≠ S3 detail | Synchronize sections |
| ERR-X-011 | QDMTT offset inconsistent | S2 ≠ S3 amounts | Reconcile QDMTT |

---

## 5.5.7 Reconciliation Procedures

### Financial Statement Reconciliation

**Purpose:** Ensure GIR data ties back to audited financial statements.

**Tab:** `Reconciliation - FS`

**Reconciliation Points:**

| GIR Data Point | Financial Statement Source | Expected Relationship |
|----------------|---------------------------|----------------------|
| Financial Accounting Net Income | Consolidated P&L (Entity level) | Should match (after adjustments) |
| Current Tax Expense | Income Tax Note | Direct match |
| Deferred Tax Expense | Income Tax Note | Direct match |
| Tangible Assets | Balance Sheet / Fixed Asset Note | Carrying value match |
| Payroll Costs | Staff Costs Note | Should reconcile |

**Reconciliation Template:**

| Item | GIR Amount | FS Amount | Difference | Explanation |
|------|-----------|-----------|------------|-------------|
| GloBE Income (Pre-Adj) | €XX,XXX | €XX,XXX | €X,XXX | [Document] |
| Current Tax Expense | €XX,XXX | €XX,XXX | €0 | Matched |
| Deferred Tax Expense | €XX,XXX | €XX,XXX | €X,XXX | [Document] |
| Tangible Assets (Avg) | €XX,XXX | €XX,XXX | €0 | Matched |
| Payroll Costs | €XX,XXX | €XX,XXX | €X,XXX | [Document] |

**Common Reconciling Items:**

```
Financial Statement to GIR Reconciliation:
│
├── FS Income → FANIL
│   ├── Eliminate: Consolidation adjustments
│   ├── Adjust: Inter-company eliminations
│   └── Convert: Currency translation
│
├── FS Tax Expense → Covered Taxes
│   ├── Exclude: Deferred tax on items not in GloBE Income
│   ├── Add: Withholding taxes borne
│   └── Adjust: DTA minimum rate cap
│
└── FS Assets → SBIE Assets
    ├── Include: ROU assets under IFRS 16
    ├── Exclude: Investment property (unless operational)
    └── Average: (Opening + Closing) ÷ 2
```

---

### Tax Provision Reconciliation

**Purpose:** Ensure GIR tax data aligns with tax provision workpapers.

**Tab:** `Reconciliation - Tax Provision`

| GIR Data Point | Tax Provision Source | Reconciliation Notes |
|----------------|---------------------|---------------------|
| Current Tax by Entity | Current provision schedules | Direct match expected |
| Deferred Tax by Entity | Deferred tax movement | After GloBE adjustments |
| ETR by Jurisdiction | Effective rate analysis | May differ (GloBE vs GAAP) |
| Top-up Tax Provision | Pillar Two provision | Should align |

**ETR Reconciliation:**

```
GAAP ETR vs GloBE ETR Reconciliation:

GAAP Effective Tax Rate: 22.5%
├── Permanent differences: (2.0%)
├── Foreign rate differential: (3.5%)
├── Tax credits: (1.5%)
└── GAAP ETR: 22.5%

GloBE Adjustments:
├── Excluded dividends: +1.0%
├── Excluded equity gains: +0.5%
├── DTA cap adjustment: +0.3%
├── Policy disallowed add-back: (0.2%)
└── GloBE ETR: 24.1%

Difference: 1.6% (documented and explained)
```

---

### CbCR Reconciliation

**Purpose:** Ensure consistency between GIR and Country-by-Country Report for safe harbour purposes.

**Tab:** `Reconciliation - CbCR`

| GIR Field | CbCR Field | Reconciliation |
|-----------|------------|----------------|
| Revenue by Jurisdiction | Table 1: Revenues | Should reconcile |
| Profit Before Tax | Table 1: Profit (Loss) | Should match for SH test |
| Income Tax Accrued | Table 1: Income Tax | Used for Simplified ETR |
| Employees | Table 1: Number of Employees | UTPR allocation |
| Tangible Assets | Table 1: Tangible Assets | UTPR allocation |

**CbCR Safe Harbour Reconciliation:**

| Jurisdiction | CbCR Revenue | CbCR PBT | CbCR Tax | Simplified ETR | Test Met |
|--------------|-------------|----------|----------|----------------|----------|
| Germany | €45.0M | €8.5M | €2.1M | 24.7% | ✓ ETR |
| France | €32.5M | €4.2M | €0.9M | 21.4% | ✓ ETR |
| Ireland | €67.3M | €12.5M | €1.2M | 9.6% | ✗ None |

---

### Prior Year Reconciliation

**Purpose:** Ensure year-over-year consistency and explain significant changes.

**Tab:** `Reconciliation - Prior Year`

| Data Point | FY 2024 | FY 2023 | Change | Explanation Required |
|------------|---------|---------|--------|---------------------|
| Total GloBE Income | €XXX | €XXX | XX% | If > 10% change |
| Total Covered Taxes | €XXX | €XXX | XX% | If > 10% change |
| Group ETR | XX.X% | XX.X% | X.X% | If > 2% change |
| Total Top-up Tax | €XXX | €XXX | XX% | All changes |
| CE Count | XX | XX | X | If changed |
| Jurisdiction Count | XX | XX | X | If changed |

**Significant Change Documentation:**

```
Prior Year Variance Analysis:

Change: GloBE Income increased by 25% in Germany
├── Driver: Acquisition of TechCo GmbH in July 2024
├── Impact: Added €15M GloBE Income
├── Supporting Documentation: Acquisition completion memo
└── Section 1 Update: 3 new CEs added

Change: Ireland ETR decreased by 3%
├── Driver: Increased R&D credits claimed
├── Impact: ETR fell from 14.5% to 11.5%
├── GloBE Treatment: Credits are qualified refundable
└── Top-up Tax Impact: Increased by €XXX
```

---

## 5.5.8 Final Review Procedures

### Pre-XML Generation Checklist

Complete this checklist before generating the XML file:

**Data Completeness:**

| # | Check Item | Status |
|---|------------|--------|
| 1 | All mandatory fields populated | ☐ |
| 2 | All CEs entered in Section 1 | ☐ |
| 3 | All jurisdictions addressed in Section 2 or 3 | ☐ |
| 4 | All calculations completed | ☐ |
| 5 | No placeholder or dummy values remaining | ☐ |

**Validation Status:**

| # | Check Item | Status |
|---|------------|--------|
| 6 | All Level 1 validations passed | ☐ |
| 7 | All Level 2 validations passed | ☐ |
| 8 | All Level 3 validations passed | ☐ |
| 9 | All cross-section validations passed | ☐ |
| 10 | All warnings reviewed and documented | ☐ |

**Reconciliation Completeness:**

| # | Check Item | Status |
|---|------------|--------|
| 11 | Financial statement reconciliation completed | ☐ |
| 12 | Tax provision reconciliation completed | ☐ |
| 13 | CbCR reconciliation completed (if safe harbour) | ☐ |
| 14 | Prior year reconciliation completed | ☐ |
| 15 | All variances explained and documented | ☐ |

**Review and Approval:**

| # | Check Item | Status |
|---|------------|--------|
| 16 | Preparer self-review completed | ☐ |
| 17 | Independent reviewer sign-off | ☐ |
| 18 | Tax director approval obtained | ☐ |
| 19 | Supporting documentation filed | ☐ |
| 20 | Audit trail maintained | ☐ |

---

### Sign-Off Documentation

**Tab:** `Sign-Off Record`

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Prepared By | [Name] | [Date] | [Signature] |
| Reviewed By | [Name] | [Date] | [Signature] |
| Approved By (Tax Director) | [Name] | [Date] | [Signature] |

**Certification Statement:**

> I confirm that the GIR data has been:
> - Prepared in accordance with the GloBE Model Rules and applicable guidance
> - Validated using the Calculator's built-in checks with all errors resolved
> - Reconciled to financial statements, tax provisions, and CbCR data
> - Reviewed by an independent party
> - Approved for XML generation and submission

---

## 5.5.9 Error Correction and Amendment

### Identifying Errors Post-Filing

If errors are discovered after GIR submission:

```
Post-Filing Error Response:
│
├── Assess Materiality
│   ├── > €1M or > 5% of Top-up Tax: Material
│   ├── Impact on collection mechanism: Material
│   └── < €1M and < 5%: Consider threshold
│
├── Document Discovery
│   ├── Date error discovered
│   ├── Nature of error
│   ├── Root cause analysis
│   └── Impact assessment
│
├── Correction Process
│   ├── Recalculate affected sections
│   ├── Run full validation
│   ├── Prepare amended XML
│   └── Submit per jurisdiction rules
│
└── Prevention Measures
    ├── Update procedures
    ├── Enhance controls
    └── Train team members
```

### Amendment Tracking

| Error ID | Discovery Date | Description | Impact | Amendment Filed | Status |
|----------|---------------|-------------|--------|-----------------|--------|
| [Unique ID] | [Date] | [Brief description] | [€ impact] | [Date/Pending] | [Open/Closed] |

---

## 5.5.10 Audit Trail and Documentation

### Required Documentation

Maintain comprehensive audit trail for examination defence:

**Calculation Workpapers:**

```
Workpaper Index:
├── WP-100: Entity Population and Ownership
├── WP-200: Safe Harbour Analysis by Jurisdiction
├── WP-300: GloBE Income Calculation
│   ├── WP-310: FANIL by Entity
│   ├── WP-320: GloBE Adjustments
│   └── WP-330: Jurisdictional Aggregation
├── WP-400: Covered Taxes Calculation
│   ├── WP-410: Current Tax by Entity
│   ├── WP-420: Deferred Tax Adjustments
│   └── WP-430: DTL Recapture Tracking
├── WP-500: SBIE Calculation
│   ├── WP-510: Eligible Payroll
│   └── WP-520: Eligible Tangible Assets
├── WP-600: Top-up Tax Computation
├── WP-700: Top-up Tax Allocation
└── WP-800: Reconciliations
    ├── WP-810: FS Reconciliation
    ├── WP-820: Tax Provision Reconciliation
    ├── WP-830: CbCR Reconciliation
    └── WP-840: Prior Year Reconciliation
```

**Supporting Documents:**

| Document Type | Retention Period | Location |
|---------------|-----------------|----------|
| Completed GIR Calculator | 7 years | [Specify location] |
| XML file submitted | 7 years | [Specify location] |
| Validation reports | 7 years | [Specify location] |
| Reconciliation workpapers | 7 years | [Specify location] |
| Sign-off documentation | 7 years | [Specify location] |
| Source data extracts | 7 years | [Specify location] |
| Tax authority correspondence | 10 years | [Specify location] |

---

## 5.5.11 Key Takeaways

### Validation Best Practices

1. **Run Validations Early and Often**
   - Don't wait until completion to validate
   - Address errors as sections are completed
   - Prevents cascading errors across sections

2. **Document All Warnings**
   - Warnings may be acceptable but need justification
   - Tax authorities may query warning items
   - Maintain contemporaneous documentation

3. **Reconciliation is Defence**
   - Reconciled data withstands examination
   - Unexplained variances create audit risk
   - Build reconciliation into standard process

4. **Prior Year Comparison is Critical**
   - Significant changes attract scrutiny
   - Explain all material variances
   - Ensure consistency or justify changes

5. **Maintain Complete Audit Trail**
   - Who, what, when for all decisions
   - Calculations fully documented
   - Evidence retained for 7+ years

---

## Section Summary

Validation and reconciliation are critical final steps before GIR submission. Key requirements include:

- **Validation Framework:** File-level, record-level, business logic, and reconciliation checks
- **Error Resolution:** All FAIL items must be resolved; warnings documented
- **Reconciliation:** Financial statements, tax provision, CbCR, and prior year
- **Final Review:** Preparer, reviewer, and tax director sign-off
- **Audit Trail:** Complete documentation retained for examination defence

The GIR Completion Calculator automates validation checks while maintaining comprehensive audit trail and reconciliation documentation.

---

## Navigation

**Previous:** [Section 5.4.4: Top-Up Tax Allocation](Section_05_04_04_Top_Up_Tax_Allocation.md)

**Next:** [Section 6: XML Generation and Validation](Section_06_XML_Generation_and_Validation.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
