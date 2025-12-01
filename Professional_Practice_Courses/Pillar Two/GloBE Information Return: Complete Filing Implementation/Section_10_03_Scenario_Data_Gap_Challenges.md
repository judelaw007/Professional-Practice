# Section 10.3: Scenario 3 - Data Gap Challenges

## Learning Objectives

By the end of this section, you will be able to:

- Identify common data gaps in GloBE compliance
- Apply systematic gap identification processes
- Implement estimation techniques with appropriate documentation
- Exercise professional judgment in data-constrained situations
- Develop risk mitigation strategies for incomplete data
- Build audit-defensible documentation for estimated figures

---

## Scenario Overview

### The Facts

**Nexus Technologies Group Ltd** is a UK-headquartered technology conglomerate that recently completed a significant acquisition and faces multiple data challenges in preparing its first GIR.

**Group Profile:**

| Attribute | Detail |
|-----------|--------|
| **Ultimate Parent Entity** | Nexus Technologies Group Ltd (UK) |
| **Fiscal Year End** | 31 December 2024 |
| **Consolidated Revenue** | €1.8 billion |
| **Total Constituent Entities** | 95 |
| **Recent Acquisition** | DataFlow Solutions Inc. (USA) - acquired 1 July 2024 |
| **Legacy ERP Issues** | 3 entities with outdated systems |
| **Incomplete Records** | Historical acquisition from 2019 |

### Data Challenge Summary

```
NEXUS TECHNOLOGIES - DATA CHALLENGE MATRIX
==========================================

Challenge 1: Mid-Year Acquisition
─────────────────────────────────
  Entity: DataFlow Solutions Inc. (USA)
  Acquired: 1 July 2024
  Issue: Only 6 months of data under Nexus ownership
  Sub-entities: 8 (including 3 subsidiaries)

Challenge 2: Legacy ERP Systems
───────────────────────────────
  Entities: 3 (Germany, Poland, Brazil)
  Issue: Cannot extract SBIE data (payroll/assets)
  System: SAP R/3 (legacy, unsupported)

Challenge 3: Historical Acquisition
───────────────────────────────────
  Entity: Nexus India Pvt Ltd
  Original acquisition: 2019 (pre-transition rules)
  Issue: No records of original carrying values
  Impact: Deferred tax calculations uncertain

Challenge 4: Incomplete Tax Records
───────────────────────────────────
  Entity: Nexus Singapore Pte Ltd
  Issue: UTP reserve breakdown unavailable
  Impact: Simplified Covered Taxes uncertain
```

---

## Part 1: Gap Identification Process

### 1.1 Systematic Data Gap Analysis

The first step in addressing data challenges is systematic identification:

```
DATA GAP IDENTIFICATION FRAMEWORK
=================================

STEP 1: Map Required Data Points
        └── ~150 data points per entity
        └── Categorise by GIR section
        └── Identify source systems

STEP 2: Assess Data Availability
        └── Available and validated
        └── Available but needs processing
        └── Partially available
        └── Not available

STEP 3: Classify Gap Severity
        └── Critical (blocks filing)
        └── Material (affects calculations)
        └── Minor (disclosure only)

STEP 4: Identify Root Cause
        └── System limitation
        └── Process gap
        └── Historical data loss
        └── Timing mismatch
        └── Definitional uncertainty

STEP 5: Develop Resolution Strategy
        └── Extract from alternative source
        └── Estimate with methodology
        └── Apply safe harbour
        └── Request extension
```

### 1.2 Data Gap Assessment Template

```
DATA GAP ASSESSMENT WORKSHEET
=============================

Entity: _________________________________
Jurisdiction: ___________________________
Assessment Date: ________________________

DATA CATEGORY: GloBE INCOME INPUTS
──────────────────────────────────
| Data Point                | Available? | Source      | Gap Severity |
|---------------------------|------------|-------------|--------------|
| Net accounting income     | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Excluded dividends        | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Excluded equity gains     | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Stock-based compensation  | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Policy disallowed exp.    | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Asymmetric FX gains       | □ Y □ N □ P| ___________| □ C □ M □ m  |

DATA CATEGORY: COVERED TAXES INPUTS
───────────────────────────────────
| Data Point                | Available? | Source      | Gap Severity |
|---------------------------|------------|-------------|--------------|
| Current tax expense       | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Deferred tax expense      | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Non-Covered Taxes detail  | □ Y □ N □ P| ___________| □ C □ M □ m  |
| UTP reserve breakdown     | □ Y □ N □ P| ___________| □ C □ M □ m  |

DATA CATEGORY: SBIE INPUTS
──────────────────────────
| Data Point                | Available? | Source      | Gap Severity |
|---------------------------|------------|-------------|--------------|
| Eligible payroll costs    | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Tangible assets (NBV)     | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Asset location detail     | □ Y □ N □ P| ___________| □ C □ M □ m  |
| Payroll by jurisdiction   | □ Y □ N □ P| ___________| □ C □ M □ m  |

Key: Y = Yes, N = No, P = Partial
     C = Critical, M = Material, m = Minor

Gaps Identified: _______
Resolution Strategy Required: _______

Prepared by: _________________ Date: ____________
```

---

## Part 2: Challenge 1 - Mid-Year Acquisition

### 2.1 The DataFlow Acquisition

**Facts:**
- DataFlow Solutions Inc. (USA) acquired 1 July 2024
- 8 entities in the DataFlow group
- Only 6 months of data under Nexus ownership
- Pre-acquisition period under different accounting policies

### 2.2 GloBE Treatment of Mid-Year Acquisitions

Under the GloBE Rules, entities become Constituent Entities from the date of acquisition:

```
MID-YEAR ACQUISITION TIMELINE
=============================

1 Jan 2024          1 Jul 2024              31 Dec 2024
    │                   │                        │
    │   Pre-acquisition │    Post-acquisition    │
    │   (Not CE)        │    (CE)                │
    ▼                   ▼                        ▼
┌───────────────────┬───────────────────────────────┐
│ DataFlow as       │ DataFlow as Nexus CE          │
│ independent       │ 6 months included in GIR      │
│ (excluded)        │                               │
└───────────────────┴───────────────────────────────┘

GIR includes: 1 July 2024 - 31 December 2024 only
```

### 2.3 Data Collection Approach

**Option A: Annualise 6-Month Data**
- Take 6-month figures and multiply by 2
- Simple but may distort seasonal businesses
- Not recommended for GloBE purposes

**Option B: Actual Period Data (Recommended)**
- Use actual 6-month data
- Apply GloBE adjustments to actual period
- Pro-rate SBIE (if applicable)

**Recommended Approach:**

```
DATAFLOW ACQUISITION - DATA APPROACH
====================================

GloBE Income Calculation:
  Use actual financial data for 1 Jul - 31 Dec 2024
  Apply all GloBE adjustments to actual period
  No annualisation required

Covered Taxes:
  Use actual tax expense for 6-month period
  Include only taxes accrued post-acquisition
  Deferred tax: opening balance at acquisition date

SBIE Calculation:
  Payroll: Actual costs incurred 1 Jul - 31 Dec
  Assets: Average of acquisition date and year-end NBV
  Rates: Full year rates (not pro-rated)

Example:
  Acquisition date assets:     $15,000,000
  Year-end assets:             $16,000,000
  Average for SBIE:            $15,500,000
  Asset carve-out (7.8%):      $1,209,000

  6-month payroll:             $8,500,000
  Payroll carve-out (9.8%):    $833,000

  Total SBIE:                  $2,042,000
```

### 2.4 Documentation for Mid-Year Acquisition

```
MID-YEAR ACQUISITION DOCUMENTATION
==================================

Entity: DataFlow Solutions Inc. (USA)
Acquisition Date: 1 July 2024
Inclusion Period: 1 July 2024 - 31 December 2024

1. ACQUISITION AGREEMENT EXTRACT
   □ Purchase agreement dated: _______________
   □ Completion date confirmed: 1 July 2024
   □ Entities acquired: 8

2. OPENING BALANCE SHEET (at acquisition)
   □ Fair value balance sheet: □ Attached
   □ Carrying values for GloBE: □ Reconciled
   □ Tangible assets at 1 July: $15,000,000

3. FINANCIAL DATA (6-month period)
   □ Management accounts 1 Jul - 31 Dec: □ Attached
   □ GloBE adjustments identified: □ Documented
   □ Tax provision for period: □ Attached

4. SBIE DATA
   □ Payroll costs (6 months): $8,500,000
   □ Asset register at year-end: □ Attached
   □ Average calculation: □ Documented

5. CONSOLIDATION ENTRIES
   □ Elimination of intercompany: □ Completed
   □ Alignment of accounting policies: □ Confirmed
   □ FX translation: □ Documented

Prepared by: _________________ Date: ____________
Reviewed by: _________________ Date: ____________
```

---

## Part 3: Challenge 2 - Legacy ERP Systems

### 3.1 The Legacy System Problem

**Affected Entities:**
- Nexus Germany GmbH
- Nexus Poland Sp.z.o.o
- Nexus Brazil Ltda

**System:** SAP R/3 (end-of-life, no longer supported)

**Data Gaps:**
- Cannot extract payroll by employee category
- Asset register lacks jurisdictional allocation detail
- No automated reconciliation capability

### 3.2 Gap Analysis for SBIE Data

```
SBIE DATA GAP ANALYSIS - LEGACY ERP ENTITIES
============================================

ENTITY: Nexus Germany GmbH
─────────────────────────

Eligible Payroll:
  Required: Breakdown of eligible vs ineligible costs
  Available: Total payroll cost only (€12,500,000)
  Gap: Cannot distinguish employee types

  Resolution Options:
  a) Manual analysis of payroll records
  b) Sampling and extrapolation
  c) Use total payroll (conservative - may overstate SBIE)

Tangible Assets:
  Required: NBV of eligible tangible assets by location
  Available: Total fixed assets (€8,200,000)
  Gap: Includes intangibles; no location breakdown

  Resolution Options:
  a) Manual review of asset register
  b) Apply ratio from prior year analysis
  c) Use management estimate with documentation

RECOMMENDED APPROACH:
  Payroll: Use total payroll (€12,500,000) as conservative estimate
           Document that all payroll assumed eligible
           SBIE impact: Overstates exclusion (favourable)

  Assets: Engage local team to manually classify assets
          If not possible, apply 85% eligible ratio
          Based on: Industry benchmarks and prior analysis
```

### 3.3 Estimation Methodology

When data cannot be extracted, apply structured estimation:

```
ESTIMATION METHODOLOGY FRAMEWORK
================================

STEP 1: Identify Best Available Data
        └── What data CAN be extracted?
        └── What proxy data exists?
        └── Historical data available?

STEP 2: Select Estimation Method
        ┌──────────────────────────────────────┐
        │ Method         │ When to Use         │
        ├──────────────────────────────────────┤
        │ Extrapolation  │ Partial data exists │
        │ Ratio/Benchmark│ Comparable data     │
        │ Sampling       │ Large population    │
        │ Management     │ No other source     │
        │   Estimate     │                     │
        └──────────────────────────────────────┘

STEP 3: Apply Conservatism
        └── For income: Lower estimate preferred
        └── For taxes: Higher estimate preferred
        └── For SBIE: Context-dependent

STEP 4: Quantify Uncertainty Range
        └── Best estimate
        └── Low estimate
        └── High estimate

STEP 5: Document Thoroughly
        └── Method selected
        └── Data sources used
        └── Assumptions made
        └── Sensitivity analysis
```

### 3.4 Legacy System Workaround Documentation

```
ESTIMATION DOCUMENTATION - LEGACY ERP
=====================================

Entity: Nexus Germany GmbH
Data Point: Eligible Payroll Costs
Fiscal Year: 2024

1. DATA GAP DESCRIPTION
   The legacy SAP R/3 system cannot distinguish between
   employee categories for GloBE eligible payroll purposes.
   Only aggregate payroll is available.

2. ESTIMATION METHOD SELECTED
   □ Extrapolation
   ☑ Benchmark/Ratio
   □ Sampling
   □ Management Estimate

3. METHOD APPLICATION

   Available Data:
   - Total payroll per GL: €12,500,000
   - Industry benchmark for eligible %: 92-98%
   - Prior year detailed analysis (FY2023): 95% eligible

   Estimate Calculation:
   - Applied ratio: 95% (based on FY2023 analysis)
   - Eligible payroll estimate: €12,500,000 × 95% = €11,875,000

   Sensitivity:
   - Low (92%): €11,500,000
   - Best (95%): €11,875,000
   - High (98%): €12,250,000

4. CONSERVATISM ASSESSMENT
   Using 95% is mid-range; reduces SBIE slightly from
   using 100%. Conservative for Top-up Tax purposes.

5. SUPPORTING EVIDENCE
   □ FY2023 detailed payroll analysis: Attached
   □ Industry benchmark source: [Industry association data]
   □ GL payroll extract: Attached

6. SIGN-OFF
   Prepared by: _________________ Date: ____________
   Reviewed by: _________________ Date: ____________

   Statement: "This estimate represents management's best
   estimate based on available information and appropriate
   methodology."
```

---

## Part 4: Challenge 3 - Historical Acquisition Records

### 4.1 The Nexus India Problem

**Facts:**
- Nexus India Pvt Ltd acquired in 2019
- Pre-dates GloBE transition rules (30 November 2021)
- No records of original carrying values at acquisition
- Fair value adjustments were made at acquisition
- Current book values include unidentifiable step-up

### 4.2 GloBE Transition Rules Context

The OECD Administrative Guidance provides:

> "In cases where an acquisition occurred prior to 1 December 2021 and no sufficient records are available to determine the Financial Accounting Net Income or Loss with reasonable accuracy based on the unadjusted carrying values of the acquired assets and liabilities, the Constituent Entity may use the carrying value reflected in its separate accounts."

### 4.3 Resolution Approach

```
HISTORICAL ACQUISITION - RESOLUTION
===================================

Entity: Nexus India Pvt Ltd
Acquisition Date: March 2019
Issue: No records of pre-acquisition carrying values

ANALYSIS:

Option 1: Reconstruct Historical Values
  - Review 2019 due diligence files
  - Examine pre-acquisition target accounts
  - Calculate implied step-up

  Outcome: Files located but incomplete
           Reconstruction NOT feasible

Option 2: Use Current Carrying Values (Permitted)
  - Per AG guidance for pre-Dec 2021 acquisitions
  - Use values in separate entity accounts
  - Accept that step-up is embedded

  Outcome: Pragmatic approach
           SELECTED

IMPACT ASSESSMENT:

GloBE Income:
  - Depreciation/amortisation includes step-up
  - May be higher than "true" GloBE basis
  - Potential understatement of GloBE Income

Covered Taxes:
  - Deferred tax reflects book basis
  - May include DTA from step-up reversal
  - Potential complexity in tax calculations

Net Effect:
  - Minor; step-up largely amortised since 2019
  - Remaining unamortised: ~€2.5 million
  - Annual P&L impact: ~€500,000 depreciation
```

### 4.4 Documentation for Historical Gap

```
HISTORICAL ACQUISITION DOCUMENTATION
====================================

Entity: Nexus India Pvt Ltd
Acquisition Date: 15 March 2019
Documentation Date: [Current date]

1. SEARCH FOR RECORDS

   Sources Reviewed:
   □ 2019 acquisition files - Reviewed, incomplete
   □ Pre-acquisition target FS - Not available
   □ Due diligence reports - Partial only
   □ Purchase price allocation - Available (high level)

   Conclusion: Insufficient records to reconstruct
               original carrying values

2. RELIANCE ON ADMINISTRATIVE GUIDANCE

   Reference: OECD AG December 2023, Para [X]

   Applicable Provision:
   "Where no sufficient records are available...
   the Constituent Entity may use the carrying value
   reflected in its separate accounts."

3. CARRYING VALUES USED

   Per Local Accounts (31 Dec 2024):
   - Property, Plant & Equipment: €15,200,000
   - Intangible Assets: €8,500,000
   - Deferred Tax Assets: €1,200,000
   - Deferred Tax Liabilities: €2,100,000

4. RESIDUAL STEP-UP ESTIMATE

   Based on available PPA summary:
   - Original step-up (2019): ~€10,000,000
   - Estimated amortisation (5 years): ~€7,500,000
   - Residual step-up: ~€2,500,000
   - Annual P&L impact: ~€500,000

5. IMPACT QUANTIFICATION

   GloBE Income (overstatement risk):
   - Depreciation includes step-up
   - Estimated impact: €500,000 higher depreciation
   - GloBE Income potentially understated by €500,000

   Materiality Assessment:
   - India GloBE Income (pre-adjustment): €12,000,000
   - Step-up impact: €500,000 (4.2%)
   - Conclusion: Not material to group

6. SIGN-OFF

   Prepared by: _________________ Date: ____________
   Technical Reviewer: __________ Date: ____________

   Statement: "We have applied the Administrative Guidance
   provisions for historical acquisitions with incomplete
   records. The impact is not material to the group's
   GloBE calculations."
```

---

## Part 5: Challenge 4 - Incomplete Tax Records

### 5.1 The Singapore UTP Issue

**Facts:**
- Nexus Singapore Pte Ltd has €800,000 UTP reserve
- Breakdown between covered and non-covered positions unavailable
- Tax team turnover; historical documentation incomplete

### 5.2 Impact on Simplified Covered Taxes

For Transitional CbCR Safe Harbour, UTP adjustments are required:

```
SIMPLIFIED COVERED TAXES - UTP ISSUE
====================================

Standard Calculation:
  Total Tax Expense           €2,500,000
  Less: Non-Covered Taxes       (€50,000)
  Less: UTP Reserve            (€???  )  ← Unknown breakdown
  = Simplified Covered Taxes    €???

The Problem:
  - €800,000 total UTP reserve
  - Mix of income tax and other positions
  - Cannot identify GloBE-relevant portion
```

### 5.3 Resolution Approaches

```
UTP BREAKDOWN RESOLUTION OPTIONS
================================

OPTION A: Detailed Analysis
──────────────────────────
  - Review each UTP position
  - Classify as Covered Tax or not
  - Time: 2-3 weeks
  - Accuracy: High

  Feasibility: Limited (no documentation)

OPTION B: Conservative Full Exclusion
─────────────────────────────────────
  - Exclude entire €800,000
  - Simplified Covered Taxes reduced
  - Lower Simplified ETR
  - May cause safe harbour failure

  Risk: Could trigger full GloBE calculation

OPTION C: Proportionate Allocation
──────────────────────────────────
  - Allocate based on tax expense composition
  - Corporate tax: 90% of total expense
  - Apply 90% to UTP: €720,000 covered
  - Exclude €80,000 (non-covered)

  Risk: Requires judgement; document basis

OPTION D: Reasoned Estimate
───────────────────────────
  - Review available UTP summary
  - Identify clearly non-covered items
  - Remainder assumed covered

  Basis: Most UTP in Singapore relates to
         corporate income tax positions

SELECTED: Option D - Reasoned Estimate
```

### 5.4 UTP Estimation Documentation

```
UTP ESTIMATION DOCUMENTATION
============================

Entity: Nexus Singapore Pte Ltd
Fiscal Year: 2024
UTP Reserve Balance: €800,000

1. AVAILABLE INFORMATION

   UTP Schedule Summary (high-level):
   - Transfer pricing positions: €450,000
   - R&D credit claims: €200,000
   - Other timing positions: €150,000

   Detailed position papers: Not available

2. ANALYSIS

   Transfer Pricing (€450,000):
   - Relates to income allocation
   - Affects taxable income
   - Classification: COVERED TAX

   R&D Credits (€200,000):
   - Singapore income tax credits
   - Reduces tax payable
   - Classification: COVERED TAX

   Other Timing (€150,000):
   - Assumed to be income tax timing
   - No indication of non-covered taxes
   - Classification: COVERED TAX (assumed)

3. CONCLUSION

   Total UTP: €800,000
   Covered Tax UTP: €800,000 (100%)
   Non-Covered Tax UTP: €0

   Simplified Covered Taxes Adjustment: (€800,000)

4. SENSITIVITY

   If 20% non-covered:
   - Covered adjustment: (€640,000)
   - Impact on Simplified ETR: +0.8%

   ETR still above 15% threshold: YES

5. PROFESSIONAL JUDGEMENT STATEMENT

   "Based on the available UTP summary and the nature
   of Singapore's tax system, we have concluded that
   all UTP positions relate to Covered Taxes. This
   represents our best estimate given data limitations."

Prepared by: _________________ Date: ____________
Tax Director: ________________ Date: ____________
```

---

## Part 6: Risk Mitigation Strategies

### 6.1 Documentation-Based Risk Mitigation

```
RISK MITIGATION FRAMEWORK
=========================

FOR EACH DATA GAP:

1. Document the Gap
   └── What data is missing
   └── Why it is unavailable
   └── Impact on calculations

2. Document the Method
   └── Estimation approach selected
   └── Alternative methods considered
   └── Rationale for selection

3. Document the Calculation
   └── Step-by-step workings
   └── Data sources used
   └── Assumptions applied

4. Document the Sensitivity
   └── Range of possible outcomes
   └── Impact on ETR/Top-up Tax
   └── Materiality assessment

5. Obtain Sign-off
   └── Preparer certification
   └── Technical review
   └── Management approval

6. Retain Supporting Evidence
   └── Source documents
   └── Correspondence
   └── Working papers
   └── 10-year retention
```

### 6.2 Hierarchy of Data Sources

When gaps exist, use this hierarchy:

| Priority | Source | Reliability |
|----------|--------|-------------|
| 1 | Audited financial statements | Highest |
| 2 | Statutory accounts (filed) | High |
| 3 | Management accounts (reviewed) | Medium-High |
| 4 | System extracts (reconciled) | Medium |
| 5 | Manual analysis (documented) | Medium |
| 6 | Estimates (supported) | Lower |
| 7 | Management assertion | Lowest |

### 6.3 Disclosure Considerations

When estimates are material, consider:

```
GIR DISCLOSURE CONSIDERATIONS
=============================

Mandatory Disclosures:
□ All required data points populated
□ Basis of preparation (if non-standard)
□ Accounting policies applied

Voluntary Disclosures (Best Practice):
□ Significant estimates noted
□ Methodology briefly described
□ Range of uncertainty indicated

Internal Documentation:
□ Full methodology papers retained
□ Available for authority review
□ Supports filed position
```

---

## Part 7: Consolidated Resolution Summary

### 7.1 Nexus Technologies - Complete Picture

```
NEXUS TECHNOLOGIES - DATA GAP RESOLUTION SUMMARY
=================================================

CHALLENGE 1: DataFlow Mid-Year Acquisition
──────────────────────────────────────────
Resolution: Use actual 6-month data
SBIE: Average of acquisition and year-end values
Documentation: Acquisition file with period data
Status: RESOLVED ✓

CHALLENGE 2: Legacy ERP (Germany, Poland, Brazil)
─────────────────────────────────────────────────
Resolution: Estimation based on benchmarks
Payroll: 95% eligible ratio applied
Assets: Manual classification + 85% eligible ratio
Documentation: Estimation methodology papers
Status: RESOLVED ✓

CHALLENGE 3: Historical Acquisition (India)
───────────────────────────────────────────
Resolution: Use current carrying values per AG
Basis: Pre-Dec 2021 acquisition rule
Impact: Residual step-up €2.5m (immaterial)
Documentation: AG reliance memo
Status: RESOLVED ✓

CHALLENGE 4: Singapore UTP
──────────────────────────
Resolution: Reasoned estimate - 100% covered
Basis: Nature of positions; Singapore tax system
Sensitivity: Robust (ETR above threshold)
Documentation: UTP analysis memo
Status: RESOLVED ✓
```

### 7.2 GIR Impact Summary

```
GIR IMPACT OF DATA GAPS
=======================

Jurisdictions Affected:

USA (DataFlow):
  GloBE Income: Based on 6-month actual data
  Safe Harbour: Simplified ETR test passed
  Uncertainty: Low

Germany:
  SBIE: €11,875,000 payroll (95% estimate)
  SBIE: €6,970,000 assets (85% estimate)
  Safe Harbour: Simplified ETR test passed
  Uncertainty: Low-Medium

India:
  GloBE Income: May be understated by ~€500,000
  Impact on ETR: Minimal (<0.5% effect)
  Safe Harbour: N/A (full calculation)
  Uncertainty: Low (immaterial)

Singapore:
  Simplified Covered Taxes: Full UTP excluded
  Simplified ETR: 19.2% (above 15% threshold)
  Safe Harbour: Passed
  Uncertainty: Low

Overall GIR Reliability:
□ High confidence in material jurisdictions
□ Estimates immaterial to group position
□ Documentation supports filed position
```

---

## Deliverable: Data Gap Resolution Workbook

### Template: Comprehensive Gap Resolution

```
DATA GAP RESOLUTION WORKBOOK
============================

Group: _________________________________
Fiscal Year: ___________________________
Prepared by: ____________ Date: ________

PART A: GAP INVENTORY

| # | Entity          | Data Point      | Gap Type    | Severity | Status    |
|---|-----------------|-----------------|-------------|----------|-----------|
| 1 | ______________ | ______________ | ___________| □ C □ M  | □ R □ P   |
| 2 | ______________ | ______________ | ___________| □ C □ M  | □ R □ P   |
| 3 | ______________ | ______________ | ___________| □ C □ M  | □ R □ P   |
| 4 | ______________ | ______________ | ___________| □ C □ M  | □ R □ P   |
| 5 | ______________ | ______________ | ___________| □ C □ M  | □ R □ P   |

Gap Type: ACQ = Acquisition, LEG = Legacy System, HIS = Historical,
          INC = Incomplete Records, OTH = Other

Severity: C = Critical, M = Material
Status: R = Resolved, P = Pending

PART B: RESOLUTION SUMMARY (per gap)

Gap #: ___
Entity: _________________________________
Data Point: _____________________________

Resolution Method:
□ Data extraction (alternative source)
□ Estimation (benchmark/ratio)
□ Estimation (sampling)
□ Estimation (management)
□ Administrative Guidance reliance
□ Other: _________________

Method Description:
_____________________________________________________
_____________________________________________________

Data/Assumptions Used:
_____________________________________________________
_____________________________________________________

Calculation:
_____________________________________________________

Result: _______________________

Sensitivity Analysis:
  Low estimate: _______________
  Best estimate: ______________
  High estimate: ______________

Impact on ETR: _______________

Materiality Assessment:
□ Material to jurisdiction
□ Material to group
□ Not material

Documentation Attached:
□ Methodology memo
□ Calculation workpaper
□ Supporting evidence
□ Sign-off obtained

PART C: OVERALL ASSESSMENT

Total Gaps Identified: ___________
Gaps Resolved: ___________
Gaps Pending: ___________

Aggregate Uncertainty:
□ Low - High confidence in GIR figures
□ Medium - Some estimates, adequately supported
□ High - Significant estimates, monitor closely

Overall Risk Assessment:
□ Low - Defensible position with documentation
□ Medium - Some risk; additional support may help
□ High - Consider alternative approaches

PART D: SIGN-OFF

I confirm that all data gaps have been identified,
appropriate resolution methods applied, and
documentation retained.

Preparer: _____________________ Date: ____________
Reviewer: _____________________ Date: ____________
Approver: _____________________ Date: ____________
```

---

## Section Summary

Data gap challenges are common in first-year GloBE compliance:

1. **Mid-Year Acquisitions** - Use actual period data; pro-rate SBIE inputs
2. **Legacy Systems** - Apply estimation with benchmark ratios
3. **Historical Acquisitions** - Rely on AG provisions for pre-transition deals
4. **Incomplete Records** - Use reasoned estimates with documentation
5. **Documentation is Key** - Thorough records support defensible positions

The goal is not perfect data, but a **well-documented, reasonable approach** that can withstand scrutiny.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Gap Identification** | Systematic process across ~150 data points per entity |
| **Mid-Year Acquisitions** | Include from acquisition date; use actual period data |
| **Legacy Systems** | Estimate using benchmarks with documented methodology |
| **Pre-2021 Acquisitions** | AG permits use of current carrying values |
| **UTP Breakdown** | Reasoned allocation based on available information |
| **Documentation** | Essential for audit defence; retain 10 years |
| **Conservatism** | Apply where direction of error is clear |
| **Materiality** | Assess impact on ETR and group position |

---

## Sources

Key references for this section include:

- [EY - How to Alleviate BEPS 2.0 Pillar Two Data Challenges](https://www.ey.com/en_gl/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges)
- [Wolters Kluwer - Understanding Pillar Two Data Requirements](https://www.wolterskluwer.com/en/expert-insights/understanding-beps-pillar-two-data)
- [KPMG - Pillar Two: Data Gaps, Technology Needs, and Modeling](https://kpmg.com/us/en/articles/2023/pillar-two-data-and-technology.html)
- [PwC - Pillar Two Data and Compliance Challenges](https://www.pwc.com/us/en/services/tax/library/pillar-two-compliance-challenges.html)
- [OECD Administrative Guidance - December 2023](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/12/globe-model-rules-pillar-two.pdf)

---

*Section 10.3 Complete. Proceed to Section 10.4: Scenario 4 - Multi-QDMTT Jurisdictions.*
