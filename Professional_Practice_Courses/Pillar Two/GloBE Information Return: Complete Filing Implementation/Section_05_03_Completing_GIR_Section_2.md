# Section 5.3: Completing GIR Section 2: Safe Harbours and Exclusions

## Introduction

GIR Section 2 represents one of the most strategically significant portions of the GloBE Information Return. While containing approximately 40 data points compared to Section 3's 400+, the decisions recorded in Section 2 can eliminate extensive calculation requirements for qualifying jurisdictions—potentially saving hundreds of hours of compliance effort annually.

This section provides step-by-step guidance for completing Section 2 using the GIR Completion Calculator, covering safe harbour elections, exclusion documentation, and the critical decision trees that determine whether full GloBE calculations are required.

**Learning Objectives:**
- Master the data entry requirements for each safe harbour election
- Understand the "once out, always out" rule and its compliance implications
- Document exclusion elections with appropriate supporting rationale
- Navigate the interaction between Section 2 elections and Section 3 requirements

---

## 5.3.1 Safe Harbour Elections

### Overview of GIR Section 2 Architecture

Section 2 of the GIR captures safe harbour elections at the **jurisdiction level**, not the entity level. This fundamental design principle reflects the GloBE framework's jurisdiction-by-jurisdiction approach to determining Top-up Tax liability.

**Section 2 Structure:**

| Sub-Section | Description | Approximate Fields |
|-------------|-------------|-------------------|
| 2.1 | Transitional CbCR Safe Harbour Elections | 12-15 fields per jurisdiction |
| 2.2 | QDMTT Safe Harbour Elections | 8-10 fields per jurisdiction |
| 2.3 | Permanent Safe Harbour Elections | 6-8 fields per jurisdiction |
| 2.4 | Exclusion Summary | 4-6 fields per jurisdiction |

**Calculator Tab:** `Section 2 - Safe Harbours`

---

### 5.3.1.1 Transitional CbCR Safe Harbour

#### Understanding the Three Tests

The Transitional CbCR Safe Harbour allows MNE Groups to apply a simplified test using existing Country-by-Country Reporting data rather than performing full GloBE calculations. A jurisdiction qualifies if it meets **ANY ONE** of three tests:

**Test 1: De Minimis Test**
```
Qualifying Criteria:
├── Total Revenue < €10,000,000
│   └── AND
└── Profit (Loss) Before Income Tax < €1,000,000

Data Source: CbCR Table 1 - Revenues and Profit/Loss columns
```

**Test 2: Simplified ETR Test**
```
Qualifying Criteria:
├── Simplified ETR ≥ Transition Rate for Fiscal Year
│   ├── FY 2024: ≥ 15%
│   ├── FY 2025: ≥ 16%
│   └── FY 2026: ≥ 17%

Simplified ETR = Income Tax Accrued (Current Year) ÷ Profit Before Tax

Data Source: CbCR Table 1 - Income Tax Paid/Accrued columns
```

**Test 3: Routine Profits Test**
```
Qualifying Criteria:
├── Profit (Loss) Before Income Tax ≤ SBIE Amount
│   └── SBIE = Payroll Carve-out + Tangible Asset Carve-out
│       ├── Payroll: Eligible Payroll × SBIE Rate
│       └── Tangibles: Eligible Assets × SBIE Rate

SBIE Rates (Transitional):
├── FY 2024: Payroll 9.8%, Tangibles 7.8%
├── FY 2025: Payroll 9.6%, Tangibles 7.6%
├── FY 2026: Payroll 9.4%, Tangibles 7.4%
└── [Declining to 5.0%/5.0% by 2033+]
```

---

#### Calculator Data Entry: Transitional CbCR Safe Harbour

**Step 1: Navigate to Section 2 Tab**

Open the `Section 2 - Safe Harbours` tab in your GIR Completion Calculator. The transitional safe harbour fields appear in the upper section.

**Step 2: Enter Jurisdiction Identification**

| Field | Cell Reference | Format | Example |
|-------|---------------|--------|---------|
| Jurisdiction Code | B5 | ISO 3166-1 alpha-2 | DE |
| Jurisdiction Name | C5 | Text (auto-populated) | Germany |
| Fiscal Year | D5 | YYYY | 2024 |
| CbCR Data Available | E5 | Y/N dropdown | Y |

**Step 3: Enter CbCR Source Data**

For each jurisdiction where transitional safe harbour is being claimed, enter the CbCR Table 1 values:

| Field | Cell Reference | Format | Validation | Example |
|-------|---------------|--------|------------|---------|
| Total Revenue | F5 | Currency (€) | ≥ 0 | €45,000,000 |
| Profit (Loss) Before Tax | G5 | Currency (€) | Any value | €8,500,000 |
| Income Tax Accrued | H5 | Currency (€) | Any value | €2,125,000 |
| Eligible Payroll | I5 | Currency (€) | ≥ 0 | €12,000,000 |
| Eligible Tangible Assets | J5 | Currency (€) | ≥ 0 | €15,000,000 |

**Step 4: Test Results (Auto-Calculated)**

The calculator automatically determines which tests are satisfied:

| Field | Cell Reference | Formula | Result |
|-------|---------------|---------|--------|
| De Minimis Revenue Met | K5 | =IF(F5<10000000,"PASS","FAIL") | FAIL |
| De Minimis Profit Met | L5 | =IF(G5<1000000,"PASS","FAIL") | FAIL |
| **De Minimis Test Result** | M5 | =IF(AND(K5="PASS",L5="PASS"),"QUALIFIES","DOES NOT QUALIFY") | DOES NOT QUALIFY |
| Simplified ETR | N5 | =IF(G5>0,H5/G5,"N/A") | 25.00% |
| Transition Rate | O5 | =VLOOKUP(D5,Rates!A:B,2,FALSE) | 15% |
| **Simplified ETR Test Result** | P5 | =IF(N5>=O5,"QUALIFIES","DOES NOT QUALIFY") | QUALIFIES |
| SBIE Amount | Q5 | =(I5×PayrollRate)+(J5×TangibleRate) | €2,346,000 |
| **Routine Profits Test Result** | R5 | =IF(G5<=Q5,"QUALIFIES","DOES NOT QUALIFY") | DOES NOT QUALIFY |

**Step 5: Overall Safe Harbour Determination**

| Field | Cell Reference | Formula | Result |
|-------|---------------|---------|--------|
| **Transitional Safe Harbour Available** | S5 | =IF(OR(M5="QUALIFIES",P5="QUALIFIES",R5="QUALIFIES"),"YES","NO") | YES |
| Qualifying Test | T5 | =IF(M5="QUALIFIES","De Minimis",IF(P5="QUALIFIES","Simplified ETR",IF(R5="QUALIFIES","Routine Profits","None"))) | Simplified ETR |

---

#### Worked Example: GlobalCo Holdings - Germany

**Scenario:** GlobalCo Holdings plc has operations in Germany through three Constituent Entities. You need to determine transitional safe harbour eligibility for FY 2024.

**CbCR Data for Germany (Aggregated):**

| Data Element | Amount (€) |
|--------------|------------|
| Unrelated Party Revenue | €38,500,000 |
| Related Party Revenue | €6,500,000 |
| **Total Revenue** | **€45,000,000** |
| Profit Before Tax | €8,500,000 |
| Income Tax Accrued | €2,125,000 |
| Employee Costs | €12,000,000 |
| NBV Tangible Assets | €15,000,000 |
| Number of Employees | 85 |

**Calculator Entry:**

```
Section 2 - Safe Harbours Tab

Row 5: Germany
┌─────────────────────────────────────────────────────────────────────────┐
│ B5: DE                                                                  │
│ C5: Germany (auto)                                                      │
│ D5: 2024                                                                │
│ E5: Y                                                                   │
│ F5: €45,000,000                                                         │
│ G5: €8,500,000                                                          │
│ H5: €2,125,000                                                          │
│ I5: €12,000,000                                                         │
│ J5: €15,000,000                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Auto-Calculated Results:**

```
Test 1: De Minimis
├── Revenue Test: €45,000,000 ≥ €10,000,000 = FAIL
├── Profit Test: €8,500,000 ≥ €1,000,000 = FAIL
└── Overall: DOES NOT QUALIFY (both tests must pass)

Test 2: Simplified ETR
├── Simplified ETR: €2,125,000 ÷ €8,500,000 = 25.00%
├── Transition Rate (2024): 15.00%
├── Comparison: 25.00% ≥ 15.00%
└── Overall: QUALIFIES ✓

Test 3: Routine Profits
├── Payroll SBIE: €12,000,000 × 9.8% = €1,176,000
├── Tangible SBIE: €15,000,000 × 7.8% = €1,170,000
├── Total SBIE: €2,346,000
├── Comparison: €8,500,000 > €2,346,000
└── Overall: DOES NOT QUALIFY

FINAL DETERMINATION: TRANSITIONAL SAFE HARBOUR QUALIFIES
Qualifying Test: Simplified ETR
```

**Cell S5 Result:** `YES - Safe Harbour Available`
**Cell T5 Result:** `Simplified ETR`

---

#### The "Once Out, Always Out" Rule

**Critical Compliance Consideration:**

The transitional CbCR safe harbour includes a permanent exit provision. If a jurisdiction **fails to qualify** for the safe harbour in any fiscal year during the transition period, that jurisdiction is **permanently ineligible** for future transitional safe harbour elections.

**Calculator Implementation:**

| Field | Cell Reference | Formula | Purpose |
|-------|---------------|---------|---------|
| Prior Year Safe Harbour Status | U5 | Dropdown: QUALIFIED / DID NOT QUALIFY / FIRST YEAR | Historical tracking |
| Prior Year Exit Flag | V5 | =IF(U5="DID NOT QUALIFY","PERMANENTLY EXCLUDED","ELIGIBLE") | Exit rule enforcement |
| **Current Year Eligibility** | W5 | =IF(V5="PERMANENTLY EXCLUDED","INELIGIBLE",S5) | Final determination |

**Practical Application:**

```
Example: GlobalCo Germany - Multi-Year Analysis

Year 1 (FY 2024):
├── Simplified ETR: 25% ≥ 15%
├── Result: QUALIFIES
└── Status: Safe harbour elected

Year 2 (FY 2025):
├── Simplified ETR: 14% < 16% (new threshold)
├── De Minimis: FAILS
├── Routine Profits: FAILS
├── Result: DOES NOT QUALIFY
└── Status: EXIT TRIGGERED - Permanent exclusion

Year 3 (FY 2026):
├── Simplified ETR: 20% ≥ 17%
├── BUT: Prior exit flag = TRUE
├── Result: INELIGIBLE (permanent exclusion applies)
└── Status: Must perform full GloBE calculations
```

**Documentation Requirement:**

When a jurisdiction exits the transitional safe harbour, the calculator prompts for documentation:

| Field | Cell Reference | Input Required |
|-------|---------------|----------------|
| Exit Reason | X5 | Dropdown: ETR decline / Revenue increase / Profit increase / Other |
| Exit Notes | Y5 | Free text explanation |
| Full Calc Required From | Z5 | Auto-populated fiscal year |

---

#### Transitional Period Boundaries

**Availability Window:**

```
Transitional CbCR Safe Harbour Availability:
├── Start: Fiscal years beginning on or after 31 December 2023
├── End: Fiscal years beginning on or before 31 December 2026
│       (not including fiscal years ending after 30 June 2028)
└── Maximum Span: Approximately 3-4 fiscal years depending on year-end

Example Timeline (Calendar Year-End MNE):
├── FY 2024 (Jan-Dec 2024): Eligible
├── FY 2025 (Jan-Dec 2025): Eligible
├── FY 2026 (Jan-Dec 2026): Eligible
└── FY 2027 onwards: No longer available (permanent safe harbours only)
```

**Calculator Validation:**

The calculator automatically validates transitional period eligibility:

```
=IF(AND(FiscalYearStart>=DATE(2023,12,31),
        FiscalYearStart<=DATE(2026,12,31),
        FiscalYearEnd<=DATE(2028,6,30)),
   "WITHIN TRANSITION PERIOD",
   "OUTSIDE TRANSITION PERIOD")
```

---

### 5.3.1.2 QDMTT Safe Harbour

#### Understanding QDMTT Safe Harbour Requirements

The Qualified Domestic Minimum Top-up Tax (QDMTT) Safe Harbour allows MNE Groups to treat a jurisdiction's QDMTT liability as satisfying the GloBE Top-up Tax obligation, eliminating the need for cross-border IIR or UTPR calculations for that jurisdiction.

**Three Core Standards:**

| Standard | Requirement | Verification Approach |
|----------|-------------|----------------------|
| **Accounting Standard** | QDMTT uses GloBE-compliant financial accounting | Acceptable GAAP or adjustments to GloBE standard |
| **Consistency Standard** | QDMTT applies GloBE rules without material deviation | Permanent differences must be neutral or favourable |
| **Administration Standard** | QDMTT jurisdiction has adequate tax administration | Certified by filing jurisdiction |

---

#### Calculator Data Entry: QDMTT Safe Harbour

**Step 1: Navigate to QDMTT Section**

In the `Section 2 - Safe Harbours` tab, scroll to the QDMTT Safe Harbour section (typically rows 50+).

**Step 2: Enter Jurisdiction Information**

| Field | Cell Reference | Format | Example |
|-------|---------------|--------|---------|
| Jurisdiction Code | B50 | ISO 3166-1 alpha-2 | KR |
| Jurisdiction Name | C50 | Text (auto-populated) | South Korea |
| QDMTT Enacted | D50 | Y/N dropdown | Y |
| QDMTT Effective Date | E50 | Date | 01/01/2024 |

**Step 3: Standard Certifications**

| Field | Cell Reference | Input Type | Validation |
|-------|---------------|------------|------------|
| Accounting Standard Met | F50 | Dropdown: YES / NO / UNDER REVIEW | Required |
| Accounting Basis | G50 | Dropdown: Local GAAP / IFRS / Adjusted | If F50=YES |
| Consistency Standard Met | H50 | Dropdown: YES / NO / UNDER REVIEW | Required |
| Material Deviations Identified | I50 | Y/N | If H50=NO |
| Administration Standard Met | J50 | Dropdown: YES / NO / UNDER REVIEW | Required |

**Step 4: QDMTT Calculation Data**

| Field | Cell Reference | Format | Purpose |
|-------|---------------|--------|---------|
| QDMTT Liability Computed | K50 | Currency | Domestic top-up amount |
| QDMTT Payment Due Date | L50 | Date | Compliance tracking |
| QDMTT Filing Status | M50 | Dropdown | FILED / PENDING / NOT REQUIRED |

**Step 5: Safe Harbour Determination**

| Field | Cell Reference | Formula | Result |
|-------|---------------|---------|--------|
| **QDMTT Safe Harbour Available** | N50 | =IF(AND(F50="YES",H50="YES",J50="YES"),"YES","NO") | YES |
| Safe Harbour Election Made | O50 | Dropdown: YES / NO | Manual selection |

---

#### January 2025 Update: QDMTT Switch-Off Rule

The OECD's January 2025 guidance introduced the **QDMTT Switch-Off Rule**, which affects GIR Section 2 disclosure requirements.

**Switch-Off Rule Operation:**

When a QDMTT Safe Harbour is elected for a jurisdiction, the MNE Group is not required to:
- Complete full Section 3 GloBE calculations for that jurisdiction
- Report jurisdiction-specific ETR under GloBE rules
- Disclose Top-up Tax allocation details for that jurisdiction

**GIR Disclosure Impact:**

| With QDMTT Safe Harbour | Without QDMTT Safe Harbour |
|------------------------|---------------------------|
| Section 3 calculations: NOT REQUIRED | Section 3 calculations: REQUIRED |
| ETR disclosure: QDMTT basis only | ETR disclosure: Full GloBE basis |
| Top-up Tax: QDMTT amount only | Top-up Tax: Full IIR/UTPR allocation |

**Calculator Linkage:**

The calculator automatically adjusts Section 3 requirements based on Section 2 elections:

```
Section 3 Requirement Formula:
=IF(OR(TransitionalSHElected=TRUE, QDMTTSHElected=TRUE),
    "SECTION 3 NOT REQUIRED FOR THIS JURISDICTION",
    "FULL SECTION 3 COMPLETION REQUIRED")
```

---

#### QDMTT Safe Harbour Jurisdictions (As of January 2025)

The calculator includes a reference table of jurisdictions with enacted QDMTTs:

| Jurisdiction | QDMTT Effective | Accounting Standard | Notes |
|--------------|----------------|---------------------|-------|
| South Korea | 1 Jan 2024 | K-IFRS | First mover |
| United Kingdom | 1 Jan 2024 | UK GAAP / IFRS | Multinational Top-up Tax |
| Japan | 1 Apr 2024 | J-GAAP / IFRS | Fiscal year alignment |
| Canada | 1 Jan 2024 | ASPE / IFRS | Provincial coordination |
| Australia | 1 Jan 2024 | AASB / IFRS | Domestic minimum tax |
| European Union | 1 Jan 2024 | Local GAAP / IFRS | Member state implementation varies |
| Switzerland | 1 Jan 2024 | Swiss GAAP / IFRS | Cantonal coordination |
| Hong Kong | 1 Jan 2025 | HKFRS | Territorial system adaptation |
| Singapore | 1 Jan 2025 | SFRS / IFRS | Refundable tax credit interaction |

**Validation Rule:** The calculator cross-references jurisdiction codes against this table to validate QDMTT availability claims.

---

### 5.3.1.3 Permanent Safe Harbours

#### Overview

Permanent safe harbours, currently under OECD development, will provide ongoing simplified compliance options beyond the transitional period. While specific rules remain subject to finalisation, the GIR Section 2 architecture includes placeholder fields for:

**Anticipated Permanent Safe Harbour Categories:**

1. **Simplified Calculations Safe Harbour**
   - Streamlined ETR calculation methodology
   - Reduced data granularity requirements
   - Applicable to lower-risk jurisdictions

2. **QDMTT Permanent Safe Harbour**
   - Continuation of QDMTT safe harbour beyond transition
   - Enhanced accounting standard requirements
   - Ongoing monitoring and re-certification

3. **De Minimis Permanent Exclusion**
   - Ongoing exclusion for minimal operations
   - Potential higher thresholds than transitional version
   - Annual re-qualification required

**Calculator Placeholder Fields:**

| Field | Cell Reference | Current Status |
|-------|---------------|----------------|
| Permanent SH Category | B80 | AWAITING GUIDANCE |
| Permanent SH Effective Date | C80 | TBD |
| Qualification Criteria Met | D80 | N/A |

**Note:** These fields will be activated upon OECD finalisation of permanent safe harbour rules.

---

## 5.3.2 Exclusion Documentation

### Overview of GIR Section 2 Exclusions

Beyond safe harbour elections, GIR Section 2 captures jurisdictions that are **excluded** from GloBE calculations for reasons other than safe harbour qualification. Proper documentation of exclusions is critical for audit defence and demonstrates compliance rigour.

**Categories of Exclusions:**

| Exclusion Type | Basis | Section 3 Impact |
|----------------|-------|------------------|
| **No Constituent Entities** | No CEs present in jurisdiction | Not applicable |
| **Excluded Entities Only** | All entities qualify as Excluded Entities | Calculations not required |
| **Investment Entity Exclusion** | All entities are Investment Entities | Special rules apply |
| **Zero Liability** | Calculations performed, no Top-up Tax due | Section 3 required (zero result) |

---

### 5.3.2.1 Recording Excluded Jurisdictions

#### Calculator Data Entry: Exclusion Tab

**Tab:** `Section 2 - Exclusions`

**Step 1: Jurisdiction Identification**

| Field | Cell Reference | Format | Example |
|-------|---------------|--------|---------|
| Jurisdiction Code | B5 | ISO 3166-1 alpha-2 | BM |
| Jurisdiction Name | C5 | Text (auto-populated) | Bermuda |
| Exclusion Type | D5 | Dropdown (see below) | NO_CES |

**Exclusion Type Dropdown Options:**

```
Dropdown Values:
├── NO_CES - No Constituent Entities in jurisdiction
├── EXCLUDED_ONLY - Only Excluded Entities present
├── INVESTMENT_ENTITY - Investment Entity exclusion applies
├── TRANSITION_SH - Transitional Safe Harbour elected
├── QDMTT_SH - QDMTT Safe Harbour elected
├── PERM_SH - Permanent Safe Harbour elected
├── ZERO_LIABILITY - Calculations show zero Top-up Tax
└── OTHER - Other exclusion (requires explanation)
```

**Step 2: Exclusion Rationale**

For each excluded jurisdiction, the calculator requires supporting documentation:

| Field | Cell Reference | Input Type | Required When |
|-------|---------------|------------|---------------|
| Exclusion Rationale | E5 | Free text | All exclusions |
| Supporting Reference | F5 | Document reference | All exclusions |
| Entity Count in Jurisdiction | G5 | Number | NO_CES, EXCLUDED_ONLY |
| Excluded Entity Names | H5 | Text list | EXCLUDED_ONLY |
| Investment Entity Classification | I5 | Dropdown | INVESTMENT_ENTITY |

---

#### Worked Example: Exclusion Documentation

**Scenario:** GlobalCo Holdings plc has a dormant subsidiary in Bermuda that was acquired as part of a larger transaction. The entity holds no assets and generates no revenue.

**Calculator Entry:**

```
Section 2 - Exclusions Tab

Row 5: Bermuda
┌─────────────────────────────────────────────────────────────────────────┐
│ B5: BM                                                                  │
│ C5: Bermuda (auto)                                                      │
│ D5: EXCLUDED_ONLY                                                       │
│ E5: Single dormant entity acquired in 2019 transaction. Entity holds   │
│     no assets, generates no revenue, and has no employees. Qualifies   │
│     as Excluded Entity under Article 1.5.1 (Non-material entity).      │
│ F5: Acquisition Agreement dated 15/03/2019; Annual confirmation of     │
│     dormant status from local registered agent.                        │
│ G5: 1                                                                   │
│ H5: GlobalCo (Bermuda) Holdings Ltd                                    │
│ I5: N/A                                                                 │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 5.3.2.2 Excluded Entity Categories

The GloBE Model Rules define specific categories of entities that may be excluded from GloBE calculations. The calculator includes validation to ensure exclusion claims align with permitted categories.

**Excluded Entity Types:**

| Code | Entity Type | Model Rules Reference | Key Criteria |
|------|-------------|----------------------|--------------|
| GOV | Governmental Entity | Art. 1.5.1(a) | Owned by government, performs governmental functions |
| INTORG | International Organisation | Art. 1.5.1(b) | Recognised under international law |
| NPO | Non-Profit Organisation | Art. 1.5.1(c) | Operated exclusively for charitable purposes |
| PENSION | Pension Fund | Art. 1.5.1(d) | Regulated pension scheme |
| INVFUND | Investment Fund (UPE) | Art. 1.5.1(e) | UPE of MNE Group that is investment fund |
| REIT | Real Estate Investment Vehicle | Art. 1.5.1(f) | Qualifying REIT structure |
| HOLDING | 95% Holding Entity | Art. 1.5.2 | Meets 95% ownership test |
| DORMANT | Dormant/Non-Material Entity | Art. 1.5.1 | Below materiality thresholds |

**Calculator Validation:**

```
Excluded Entity Validation Formula:
=IF(AND(ExclusionType="EXCLUDED_ONLY",
        EntityCategory NOT IN ValidExcludedCategories),
   "WARNING: Entity category may not qualify for exclusion",
   "VALID")
```

---

### 5.3.2.3 Impact on Section 3 Requirements

The exclusions recorded in Section 2 directly affect Section 3 completion requirements. The calculator maintains linkage between sections to ensure consistency.

**Exclusion-to-Section 3 Mapping:**

| Section 2 Exclusion | Section 3 Requirement |
|--------------------|-----------------------|
| NO_CES | No Section 3 rows for jurisdiction |
| EXCLUDED_ONLY | No Section 3 rows (excluded entities not reported) |
| INVESTMENT_ENTITY | Limited Section 3 data (special calculation rules) |
| TRANSITION_SH | Section 3 not required (safe harbour switch-off) |
| QDMTT_SH | Section 3 not required (QDMTT switch-off rule) |
| ZERO_LIABILITY | Full Section 3 required (demonstrates zero result) |

**Automatic Section 3 Population:**

When exclusions are entered in Section 2, the calculator automatically:

1. **Suppresses** Section 3 input fields for excluded jurisdictions
2. **Displays** "EXCLUDED - See Section 2" notation
3. **Validates** that no conflicting data exists
4. **Calculates** total jurisdictions requiring full calculations

```
Section 3 Required Count Formula:
=COUNTIF(Section2Exclusions!D:D,"<>*") -
 COUNTIF(Section2Exclusions!D:D,"*SH") -
 COUNTIF(Section2Exclusions!D:D,"NO_CES") -
 COUNTIF(Section2Exclusions!D:D,"EXCLUDED_ONLY")
```

---

## 5.3.3 Section 2 Completion Workflow

### Step-by-Step Process

**Phase 1: Jurisdiction Inventory**

```
Step 1.1: List all jurisdictions with CEs
├── Import from Section 1 entity list
├── Aggregate to jurisdiction level
└── Validate against CbCR jurisdictions

Step 1.2: Initial categorisation
├── Jurisdictions with potential safe harbour
├── Jurisdictions with excluded entities only
├── Jurisdictions requiring full calculations
└── Review and confirm categorisation
```

**Phase 2: Transitional Safe Harbour Analysis**

```
Step 2.1: Gather CbCR data for each jurisdiction
├── Extract from filed CbCR Table 1
├── Verify data quality (Section 4 procedures)
└── Enter into calculator

Step 2.2: Review automated test results
├── Identify qualifying jurisdictions
├── Note "once out" implications
└── Document elections

Step 2.3: Handle near-threshold cases
├── Jurisdictions within 2% of ETR threshold
├── Jurisdictions within 10% of de minimis thresholds
├── Flag for detailed review
└── Consider full calculations as backup
```

**Phase 3: QDMTT Safe Harbour Analysis**

```
Step 3.1: Identify QDMTT jurisdictions
├── Cross-reference QDMTT enacted list
├── Verify effective dates
└── Confirm application to MNE Group

Step 3.2: Assess three standards
├── Accounting standard compliance
├── Consistency standard evaluation
├── Administration standard certification
└── Document standard-by-standard

Step 3.3: Record elections
├── Enter safe harbour elections
├── Link to QDMTT return filing
└── Note switch-off impact on Section 3
```

**Phase 4: Exclusion Documentation**

```
Step 4.1: Document each exclusion
├── Select exclusion type
├── Enter rationale narrative
├── Attach supporting references
└── Verify entity classifications

Step 4.2: Cross-validate with Section 1
├── Ensure excluded entities marked in Section 1
├── Verify consistency of classifications
└── Resolve any discrepancies

Step 4.3: Confirm Section 3 impact
├── Review suppressed jurisdictions
├── Validate calculation requirements
└── Update Section 3 scope
```

---

### Section 2 Completion Checklist

Use this checklist to ensure comprehensive Section 2 completion:

**Transitional CbCR Safe Harbour:**

| # | Check Item | Status |
|---|------------|--------|
| 1 | CbCR data entered for all candidate jurisdictions | ☐ |
| 2 | Three tests calculated for each jurisdiction | ☐ |
| 3 | Prior year safe harbour status verified (once out rule) | ☐ |
| 4 | Transition period eligibility confirmed | ☐ |
| 5 | Elections documented with test relied upon | ☐ |
| 6 | Near-threshold jurisdictions flagged | ☐ |
| 7 | Exit documentation completed where applicable | ☐ |

**QDMTT Safe Harbour:**

| # | Check Item | Status |
|---|------------|--------|
| 8 | QDMTT jurisdictions identified | ☐ |
| 9 | Accounting standard compliance confirmed | ☐ |
| 10 | Consistency standard evaluation completed | ☐ |
| 11 | Administration standard certification obtained | ☐ |
| 12 | QDMTT liability computed and entered | ☐ |
| 13 | Switch-off rule impact reflected in Section 3 | ☐ |

**Exclusions:**

| # | Check Item | Status |
|---|------------|--------|
| 14 | All exclusion types correctly categorised | ☐ |
| 15 | Rationale documented for each exclusion | ☐ |
| 16 | Supporting references attached | ☐ |
| 17 | Excluded entity classifications validated | ☐ |
| 18 | Section 1 cross-validation completed | ☐ |
| 19 | Section 3 impact correctly reflected | ☐ |

**Overall Section 2:**

| # | Check Item | Status |
|---|------------|--------|
| 20 | All jurisdictions accounted for | ☐ |
| 21 | No conflicting elections or exclusions | ☐ |
| 22 | Total Section 3 jurisdictions identified | ☐ |
| 23 | Section 2 summary statistics generated | ☐ |
| 24 | Sign-off obtained from tax director | ☐ |

---

## 5.3.4 Common Issues and Resolutions

### Issue 1: CbCR Data Inconsistencies

**Problem:** CbCR data used for transitional safe harbour tests doesn't match GloBE entity population.

**Symptoms:**
- Jurisdictions in GIR not present in CbCR
- Entity count mismatches
- Revenue/profit discrepancies

**Resolution:**

```
Resolution Approach:
├── Step 1: Reconcile entity populations
│   ├── Map GloBE CEs to CbCR entities
│   ├── Identify newly acquired entities (post-CbCR filing)
│   └── Document excluded entities in both reports
│
├── Step 2: Adjust for timing differences
│   ├── CbCR uses different fiscal year end
│   ├── Pro-rate where necessary
│   └── Document adjustment methodology
│
└── Step 3: Document in calculator
    ├── Enter adjusted figures
    ├── Note adjustment in comments field
    └── Attach reconciliation workpaper
```

**Calculator Field:** `CbCR Reconciliation Notes` (Cell AA5)

---

### Issue 2: "Once Out, Always Out" Identification

**Problem:** Uncertainty whether jurisdiction triggered permanent exit in prior year.

**Resolution:**

```
Verification Steps:
├── Step 1: Review prior year GIR filings
│   ├── Check Section 2 elections
│   ├── Identify safe harbour claims made
│   └── Note any failed qualifications
│
├── Step 2: Reconstruct historical tests
│   ├── Apply prior year thresholds (15% for 2024)
│   ├── Recalculate using CbCR data
│   └── Determine if any test was passed
│
└── Step 3: Document determination
    ├── If exit triggered: Mark jurisdiction as permanently excluded
    ├── If no exit: Confirm continued eligibility
    └── Maintain audit trail of analysis
```

**Best Practice:** Maintain a multi-year tracking schedule for all transitional safe harbour elections.

---

### Issue 3: QDMTT Standard Uncertainty

**Problem:** Unclear whether jurisdiction's QDMTT meets all three standards.

**Resolution:**

```
Assessment Approach:
├── Accounting Standard
│   ├── Review QDMTT legislation for accounting basis
│   ├── Compare to GloBE Article 3 requirements
│   ├── Identify any adjustments required
│   └── Consult Big 4 / local firm guidance
│
├── Consistency Standard
│   ├── Map QDMTT rules to GloBE Model Rules
│   ├── Identify deviations
│   ├── Assess if deviations increase or decrease tax
│   └── Neutral or taxpayer-favourable = acceptable
│
└── Administration Standard
    ├── Review OECD peer review materials
    ├── Check for administrative guidance issued
    └── Obtain local tax authority confirmation if needed
```

**Calculator Field:** `QDMTT Standard Assessment Notes` (Cell AB50)

---

### Issue 4: Exclusion Classification Disputes

**Problem:** Uncertainty about entity's excluded status.

**Resolution:**

```
Classification Verification:
├── Governmental Entity
│   ├── Verify government ownership documentation
│   ├── Confirm governmental function performed
│   └── Check no commercial activities
│
├── Non-Profit Organisation
│   ├── Verify charitable registration
│   ├── Confirm no profit distribution
│   └── Check activities are exclusively charitable
│
├── Pension Fund
│   ├── Verify regulatory registration
│   ├── Confirm pension fund purpose
│   └── Check beneficiary requirements met
│
└── General Approach
    ├── Apply GloBE Model Rules Article 1.5 definitions
    ├── Document entity characteristics
    ├── Obtain legal opinion if significant uncertainty
    └── Consider conservative approach (include if uncertain)
```

---

## 5.3.5 Section 2 Summary Dashboard

### Calculator Dashboard View

The `Section 2 - Summary` tab provides an overview of all safe harbour and exclusion elections:

**Safe Harbour Election Summary:**

| Metric | Value | Formula |
|--------|-------|---------|
| Total Jurisdictions with CEs | 12 | =COUNTA(Section1!JurisdictionList) |
| Transitional SH Elected | 4 | =COUNTIF(Section2!S:S,"YES") |
| QDMTT SH Elected | 2 | =COUNTIF(Section2!O:O,"YES") |
| Permanent SH Elected | 0 | =COUNTIF(Section2!D80:D99,"YES") |
| **Total Safe Harbour Jurisdictions** | **6** | =SUM(above) |

**Exclusion Summary:**

| Metric | Value | Formula |
|--------|-------|---------|
| No CEs Exclusions | 0 | =COUNTIF(Exclusions!D:D,"NO_CES") |
| Excluded Entities Only | 1 | =COUNTIF(Exclusions!D:D,"EXCLUDED_ONLY") |
| Investment Entity Exclusions | 0 | =COUNTIF(Exclusions!D:D,"INVESTMENT_ENTITY") |
| **Total Excluded Jurisdictions** | **1** | =SUM(above) |

**Section 3 Scope:**

| Metric | Value | Formula |
|--------|-------|---------|
| Total Jurisdictions | 12 | Base count |
| Less: Safe Harbour | (6) | Safe harbour elections |
| Less: Exclusions | (1) | Exclusion elections |
| **Jurisdictions Requiring Section 3** | **5** | Calculation required |

**Calculation Savings Estimate:**

| Metric | Value | Notes |
|--------|-------|-------|
| Jurisdictions Simplified | 7 | Safe harbours + exclusions |
| Estimated Hours Saved | 70 | @ 10 hours per jurisdiction |
| Estimated Cost Saved | £28,000 | @ £400/hour blended rate |

---

## 5.3.6 Key Takeaways

### Strategic Considerations

1. **Safe Harbour Elections Are Valuable**
   - Each successful safe harbour election eliminates 50+ data points from Section 3
   - Prioritise transitional CbCR analysis for all jurisdictions with existing CbCR data
   - Track near-threshold jurisdictions for proactive management

2. **The "Once Out" Rule Requires Multi-Year Planning**
   - Maintain rolling three-year projections for all safe harbour jurisdictions
   - Model impact of business changes on test results
   - Consider voluntary full calculations in borderline years to preserve optionality

3. **QDMTT Safe Harbour Will Become Increasingly Important**
   - Monitor QDMTT enactment in key jurisdictions
   - Engage with local advisors on three-standards compliance
   - Plan for switch-off rule benefits

4. **Documentation Is Defence**
   - Detailed rationale protects against examination challenges
   - Maintain supporting evidence for all elections and exclusions
   - Review annually for continuing validity

### Section 2 Quick Reference

```
Section 2 Decision Tree:

For each jurisdiction with Constituent Entities:
│
├─► Does transitional CbCR safe harbour apply?
│   ├── YES → Document election, skip Section 3
│   └── NO → Continue
│
├─► Does QDMTT safe harbour apply?
│   ├── YES → Document election, skip Section 3
│   └── NO → Continue
│
├─► Are all entities excluded entities?
│   ├── YES → Document exclusion, skip Section 3
│   └── NO → Continue
│
└─► Full GloBE calculations required → Complete Section 3
```

---

## Section Summary

Section 2 of the GIR captures critical elections that can significantly reduce GloBE compliance burden. Key completion requirements include:

- **Transitional CbCR Safe Harbour:** Three tests (De Minimis, Simplified ETR, Routine Profits) with escalating thresholds and permanent exit consequences
- **QDMTT Safe Harbour:** Three standards (Accounting, Consistency, Administration) with switch-off rule benefits
- **Exclusion Documentation:** Proper categorisation and rationale for all excluded jurisdictions
- **Section 3 Integration:** Elections directly reduce Section 3 scope

The GIR Completion Calculator automates test calculations, validates elections, and maintains linkage between sections to ensure consistent and defensible GIR completion.

---

## Navigation

**Previous:** [Section 5.2: Completing GIR Section 1: MNE Group Information](Section_05_02_Completing_GIR_Section_1.md)

**Next:** [Section 5.4: Completing GIR Section 3: GloBE Computations](Section_05_04_Completing_GIR_Section_3.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
