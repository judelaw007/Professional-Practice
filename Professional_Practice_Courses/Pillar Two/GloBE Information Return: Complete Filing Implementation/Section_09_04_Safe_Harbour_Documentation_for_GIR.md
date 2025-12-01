# Section 9.4: Safe Harbour Documentation for GIR

## Learning Objectives

By the end of this section, you will be able to:

- Record safe harbour elections correctly in GIR Section 2
- Prepare comprehensive supporting documentation for safe harbour claims
- Build audit defence files that withstand tax authority scrutiny
- Implement quality control processes for safe harbour documentation
- Maintain records in accordance with statutory retention requirements

---

## 9.4.1 GIR Section 2: Safe Harbour Reporting

### Overview of Section 2

GIR Section 2 is specifically designed to capture **Jurisdictional Safe Harbours and Exclusions**. It contains nearly 40 data points covering:

- Safe harbour elections by jurisdiction
- Test results (De Minimis, Simplified ETR, Routine Profits)
- QDMTT Safe Harbour claims
- De Minimis Exclusion applications
- Supporting calculation summaries

### Section 2 Structure

```
GIR SECTION 2: JURISDICTIONAL SAFE HARBOURS AND EXCLUSIONS
==========================================================

Per Jurisdiction:
┌─────────────────────────────────────────────────────────────┐
│ 2.1 Jurisdiction Identification                             │
│     - Jurisdiction code                                     │
│     - Number of Constituent Entities                        │
│     - Reporting fiscal year                                 │
├─────────────────────────────────────────────────────────────┤
│ 2.2 Safe Harbour Elections                                  │
│     - Transitional CbCR Safe Harbour (Yes/No)               │
│     - Test applied (De Minimis/ETR/Routine Profits)         │
│     - QDMTT Safe Harbour (Yes/No)                           │
│     - Other exclusions                                      │
├─────────────────────────────────────────────────────────────┤
│ 2.3 Supporting Data (if Transitional CbCR)                  │
│     - CbCR Revenue                                          │
│     - CbCR Profit Before Tax                                │
│     - Simplified Covered Taxes (if ETR test)                │
│     - SBIE amount (if Routine Profits test)                 │
├─────────────────────────────────────────────────────────────┤
│ 2.4 Safe Harbour Outcome                                    │
│     - Test result (Pass/Fail)                               │
│     - Top-up Tax (deemed zero if pass)                      │
│     - Reason for non-application (if applicable)            │
└─────────────────────────────────────────────────────────────┘
```

### Completing Section 2 for Each Safe Harbour Type

#### Transitional CbCR Safe Harbour

| Field | Required Entry | Source |
|-------|----------------|--------|
| Safe Harbour Type | "Transitional CbCR" | Selection |
| Test Applied | De Minimis / Simplified ETR / Routine Profits | Selection |
| CbCR Revenue | €[amount] | CbCR Table 1 |
| CbCR Profit Before Tax | €[amount] | CbCR Table 1 |
| Simplified Covered Taxes | €[amount] | Tax workpaper |
| Simplified ETR | [percentage] | Calculation |
| SBIE Amount | €[amount] (if Routine Profits) | SBIE workpaper |
| Test Result | Pass / Fail | Automatic |
| Top-up Tax | €0 (if Pass) | System |

#### QDMTT Safe Harbour

| Field | Required Entry | Source |
|-------|----------------|--------|
| Safe Harbour Type | "QDMTT" | Selection |
| QDMTT Jurisdiction | [Country code] | Selection |
| QDMTT Status | Qualified / Transitional Qualified | OECD register |
| QDMTT Amount Paid | €[amount] | Local return |
| QDMTT Return Reference | [Reference number] | Local filing |
| Top-up Tax | €0 (deemed) | System |

#### De Minimis Exclusion

| Field | Required Entry | Source |
|-------|----------------|--------|
| Exclusion Type | "De Minimis" | Selection |
| GloBE Revenue | €[amount] | GloBE calculation |
| GloBE Income | €[amount] | GloBE calculation |
| Revenue < €10m? | Yes/No | Test |
| Income < €1m? | Yes/No | Test |
| Exclusion Applied | Yes/No | Outcome |

---

## 9.4.2 Documentation Framework

### The Documentation Hierarchy

Comprehensive safe harbour documentation operates at three levels:

```
DOCUMENTATION HIERARCHY
=======================

Level 1: GIR Filing
├── Section 2 completed with safe harbour elections
├── Supporting schedules attached (where required)
└── XML submission with all data points

Level 2: Working Papers
├── Calculation workpapers for each test
├── Data extraction from CbCR
├── Simplified Covered Taxes analysis
├── SBIE calculations (if applicable)
└── Reconciliations to source data

Level 3: Source Documentation
├── Country-by-Country Report (filed)
├── Consolidated Financial Statements (audited)
├── Local entity financial statements
├── Tax returns and assessments
└── QDMTT returns (where applicable)
```

### Core Documentation Requirements

**For Every Safe Harbour Claim:**

| Document | Purpose | Retention |
|----------|---------|-----------|
| GIR extract (Section 2) | Filed position | 10 years |
| Test calculation | How test was applied | 10 years |
| Data source evidence | Where numbers came from | 10 years |
| Qualification analysis | Why safe harbour applies | 10 years |
| Management sign-off | Governance approval | 10 years |

---

## 9.4.3 Transitional CbCR Safe Harbour Documentation

### CbCR Qualification Documentation

The CbCR used for safe harbour purposes must be a **Qualified CbCR**. Document:

**Qualification Checklist:**

```
CBCR QUALIFICATION DOCUMENTATION
================================

1. DATA SOURCE CONFIRMATION
   □ Consolidated financial statements used (top-down), OR
   □ Separate entity financial statements used (bottom-up)
   □ Same source used consistently for all entities in jurisdiction
   □ No mixing of top-down and bottom-up within jurisdiction

2. FINANCIAL STATEMENT STANDARD
   □ IFRS applied, OR
   □ US GAAP applied, OR
   □ Local GAAP (materially consistent with IFRS/US GAAP)
   □ Standard identified: _______________________________

3. AUDIT STATUS
   □ Consolidated FS audited by: _______________________
   □ Audit opinion: Unqualified / Qualified / Other
   □ Material misstatements affecting CbCR: None / Listed

4. CBCR FILING
   □ CbCR filed with: [Authority]
   □ Filing date: _______________
   □ Filing reference: _______________

5. CBCR PREPARER CONFIRMATION
   Prepared by: _______________
   Date: _______________
   Statement: "I confirm the CbCR meets qualification requirements
              for Transitional Safe Harbour purposes."
```

### Test-Specific Documentation

#### De Minimis Test Documentation

```
DE MINIMIS TEST DOCUMENTATION
=============================

Jurisdiction: _______________________
Fiscal Year: ________________________

SOURCE DATA (from Qualified CbCR):

Total Revenue:
  CbCR Table 1, Column [X]            €____________
  Reconciliation to FS:               □ Attached

Profit Before Tax:
  CbCR Table 1, Column [X]            €____________
  Reconciliation to FS:               □ Attached

TEST APPLICATION:

  Revenue < €10,000,000?
    €____________ < €10,000,000       □ YES  □ NO

  Profit Before Tax < €1,000,000?
    €____________ < €1,000,000        □ YES  □ NO

  BOTH conditions met?                □ YES  □ NO

RESULT: □ PASS - Safe Harbour applies
        □ FAIL - Proceed to other tests

Prepared by: _______________ Date: ____________
Reviewed by: _______________ Date: ____________
```

#### Simplified ETR Test Documentation

```
SIMPLIFIED ETR TEST DOCUMENTATION
=================================

Jurisdiction: _______________________
Fiscal Year: ________________________

PART A: PROFIT BEFORE TAX

CbCR Profit Before Tax              €______________

Source: CbCR Table 1, Column [X]
Reconciliation attached: □ Yes

PART B: SIMPLIFIED COVERED TAXES

Starting Point:
  Income Tax Expense - Current        €______________
  Income Tax Expense - Deferred       €______________
                                      ──────────────
  Total Tax Expense                   €______________

Less Adjustments:
  Non-Covered Taxes identified:
    - [Description]                  (€______________)
    - [Description]                  (€______________)

  Uncertain Tax Positions            (€______________)
                                      ──────────────
  Simplified Covered Taxes            €______________

PART C: SIMPLIFIED ETR CALCULATION

  Simplified Covered Taxes            €______________
  ÷ Profit Before Tax                 €______________
                                      ──────────────
  Simplified ETR                      ______________%

PART D: TRANSITION RATE COMPARISON

  Fiscal Year: ________
  Transition Rate: ________%

  Simplified ETR (____%) ≥ Transition Rate (____%)

  □ YES - PASS
  □ NO - FAIL

SUPPORTING SCHEDULES:
□ Tax expense reconciliation
□ Non-Covered Taxes analysis
□ UTP reserve breakdown

Prepared by: _______________ Date: ____________
Reviewed by: _______________ Date: ____________
```

#### Routine Profits Test Documentation

```
ROUTINE PROFITS TEST DOCUMENTATION
==================================

Jurisdiction: _______________________
Fiscal Year: ________________________

PART A: PROFIT BEFORE TAX

CbCR Profit Before Tax              €______________

PART B: SUBSTANCE-BASED INCOME EXCLUSION

Eligible Payroll Costs:
  Entity 1: _______________         €______________
  Entity 2: _______________         €______________
  Entity 3: _______________         €______________
                                    ──────────────
  Total Eligible Payroll            €______________

  × Payroll Carve-out Rate          × __________%
                                    ──────────────
  Payroll SBIE Component            €______________

Tangible Assets (Net Book Value):
  Entity 1: _______________         €______________
  Entity 2: _______________         €______________
  Entity 3: _______________         €______________
                                    ──────────────
  Total Tangible Assets             €______________

  × Asset Carve-out Rate            × __________%
                                    ──────────────
  Asset SBIE Component              €______________

Total SBIE:
  Payroll Component                 €______________
  Asset Component                   €______________
                                    ──────────────
  Total SBIE                        €______________

PART C: TEST APPLICATION

  Profit Before Tax                 €______________
  Total SBIE                        €______________

  PBT ≤ SBIE?                       □ YES  □ NO

RESULT: □ PASS - Safe Harbour applies
        □ FAIL - Full GloBE calculation required

SUPPORTING SCHEDULES:
□ Eligible payroll breakdown by entity
□ Tangible asset register by entity
□ Carve-out rate confirmation

Prepared by: _______________ Date: ____________
Reviewed by: _______________ Date: ____________
```

---

## 9.4.4 QDMTT Safe Harbour Documentation

### QDMTT Status Verification

```
QDMTT SAFE HARBOUR STATUS VERIFICATION
======================================

Jurisdiction: _______________________
Fiscal Year: ________________________

STEP 1: QDMTT LEGISLATION CHECK

□ QDMTT legislation enacted in jurisdiction
  Legislation reference: _______________________
  Effective date: _______________________

STEP 2: SAFE HARBOUR STATUS CHECK

□ Checked OECD central register of qualified legislation
  Date checked: _______________________
  Status recorded:
    □ Qualified
    □ Transitional Qualified
    □ Not Qualified
    □ Not Listed

  Evidence retained: □ Screenshot  □ Printout  □ Other

STEP 3: QDMTT COMPLIANCE CONFIRMATION

□ QDMTT return filed with local authority
  Filing date: _______________________
  Reference number: _______________________

□ QDMTT calculated in accordance with local law
  Calculation workpapers: □ Attached

□ QDMTT payment made
  Payment date: _______________________
  Payment amount: €_______________________
  Payment reference: _______________________

STEP 4: GIR REPORTING

□ QDMTT Safe Harbour elected in GIR Section 2
□ Top-up Tax reported as zero (deemed)
□ QDMTT amount cross-referenced

VERIFICATION SIGN-OFF

I verify that the QDMTT Safe Harbour conditions are met for
this jurisdiction and fiscal year.

Name: _______________________
Title: _______________________
Date: _______________________
```

### QDMTT Calculation Retention

Even though the QDMTT Safe Harbour deems Top-up Tax to be zero for GIR purposes, retain:

| Document | Purpose |
|----------|---------|
| Local QDMTT return | Evidence of compliance |
| QDMTT calculation workpapers | Support for amount paid |
| Payment confirmation | Proof of discharge |
| Local authority correspondence | Query responses |

---

## 9.4.5 Audit Defence Preparation

### Why Audit Defence Matters

Tax authorities are expected to scrutinise safe harbour claims given their potential to reduce or eliminate Top-up Tax. The burden of proof rests with the MNE group.

**Expected Audit Focus Areas:**

| Area | Authority Concern | Documentation Response |
|------|-------------------|----------------------|
| CbCR qualification | Was CbCR truly "qualified"? | Qualification checklist, auditor confirmation |
| Data accuracy | Are CbCR figures correct? | Reconciliation to audited FS |
| Consistent application | Same method used across entities? | Data source matrix |
| Test calculations | Were tests correctly applied? | Detailed workpapers with formulas |
| "Once out, always out" | Was safe harbour validly available? | Prior year tracking |

### Building the Audit Defence File

**Structure:**

```
SAFE HARBOUR AUDIT DEFENCE FILE
===============================

Tab 1: Summary and Index
├── Safe harbour summary by jurisdiction
├── Document index with references
└── Key contacts and responsibilities

Tab 2: GIR Filing Evidence
├── Filed GIR (XML and PDF)
├── Section 2 extract
├── Filing confirmation/receipt
└── Amendment history (if any)

Tab 3: CbCR Qualification
├── Qualification checklist (completed)
├── Data source confirmation
├── Auditor statement on materiality
└── Filed CbCR copy

Tab 4: Test Calculations (per jurisdiction)
├── De Minimis workpaper
├── Simplified ETR workpaper
├── Routine Profits workpaper (if used)
└── Reconciliations to source

Tab 5: QDMTT Documentation (if applicable)
├── Status verification
├── Local QDMTT return
├── Payment evidence
└── OECD register extract

Tab 6: Supporting Schedules
├── Simplified Covered Taxes breakdown
├── SBIE calculations by entity
├── Currency conversion documentation
└── Intercompany eliminations

Tab 7: Governance and Approvals
├── Management memo
├── Sign-off chain
├── Board/Committee papers
└── Advisor opinions (if obtained)

Tab 8: Prior Year Comparison
├── "Once out, always out" tracking
├── Year-on-year consistency analysis
└── Changes explained
```

### Reconciliation Requirements

**Key Reconciliations to Prepare:**

```
RECONCILIATION CHECKLIST
========================

1. CbCR to Financial Statements
   □ Revenue per CbCR → Revenue per FS
   □ PBT per CbCR → PBT per FS
   □ Differences explained and documented

2. Tax Expense to Simplified Covered Taxes
   □ Total tax expense per FS
   □ Less: Non-Covered Taxes (itemised)
   □ Less: UTP reserves (itemised)
   □ = Simplified Covered Taxes

3. Tangible Assets per Books to SBIE
   □ Fixed asset register totals
   □ GloBE adjustments (if any)
   □ = Eligible tangible assets for SBIE

4. Payroll per Books to SBIE
   □ Total payroll costs per GL
   □ Eligible vs ineligible breakdown
   □ = Eligible payroll for SBIE

5. GIR Section 2 to Workpapers
   □ Each Section 2 field traced to workpaper
   □ Formulas verified
   □ No unexplained differences
```

---

## 9.4.6 Quality Control Processes

### Pre-Filing Review Checklist

```
SAFE HARBOUR PRE-FILING REVIEW
==============================

COMPLETENESS CHECKS

□ All jurisdictions with CEs reviewed for safe harbour
□ Each jurisdiction has documented test application
□ "Once out, always out" status confirmed
□ All three tests considered (or documented why not)

ACCURACY CHECKS

□ CbCR data traced to filed CbCR
□ Calculations independently verified
□ Simplified ETR formula correct
□ SBIE rates correct for fiscal year
□ Currency conversions accurate

CONSISTENCY CHECKS

□ Same data source used throughout jurisdiction
□ Prior year approach followed (or change documented)
□ Group-wide methodology consistently applied
□ Intercompany items appropriately treated

DOCUMENTATION CHECKS

□ All workpapers complete and signed
□ Source documents retained
□ Reconciliations prepared
□ Audit trail clear

GOVERNANCE CHECKS

□ Preparer sign-off obtained
□ Reviewer sign-off obtained
□ Management approval documented
□ Filing authorisation confirmed

PRE-FILING CERTIFICATION

I certify that this safe harbour filing has been reviewed
and is ready for submission.

Reviewer: _______________________
Date: _______________________
```

### Post-Filing Procedures

After GIR submission:

1. **Confirm receipt** - Obtain filing confirmation from each authority
2. **Archive documentation** - File all workpapers securely
3. **Update tracking** - Record safe harbour status for "once out, always out" monitoring
4. **Lessons learned** - Document any issues for next year's process

---

## 9.4.7 Retention Requirements

### Statutory Retention Periods

| Jurisdiction | Minimum Retention | Recommended |
|--------------|-------------------|-------------|
| UK | 6 years from end of accounting period | 10 years |
| Germany | 10 years | 10 years |
| Netherlands | 7 years | 10 years |
| France | 6 years from filing | 10 years |
| Singapore | 5 years | 10 years |
| Australia | 5 years from lodgment | 10 years |
| OECD Best Practice | Not specified | 10 years |

### What to Retain

**Permanent Retention:**

- GIR filings (all years)
- Safe harbour election documentation
- "Once out, always out" tracking
- Major policy decisions

**10-Year Retention:**

- Working papers and calculations
- Source data extracts
- Reconciliations
- Correspondence with authorities
- Internal approvals

**7-Year Retention:**

- Routine correspondence
- Draft workpapers
- Superseded versions

### Secure Storage Requirements

```
DOCUMENT RETENTION FRAMEWORK
============================

Storage Requirements:

1. SECURITY
   □ Access restricted to authorised personnel
   □ Encryption for electronic files
   □ Backup and disaster recovery in place

2. ACCESSIBILITY
   □ Documents retrievable within reasonable time
   □ Index maintained and current
   □ Version control applied

3. INTEGRITY
   □ Documents protected from alteration
   □ Audit trail of any changes
   □ Original format preserved where possible

4. ORGANISATION
   □ Filed by fiscal year
   □ Sub-filed by jurisdiction
   □ Cross-referenced to GIR sections

Review Schedule:
□ Annual review of retention compliance
□ Destruction of documents past retention date
□ Documentation of destruction
```

---

## 9.4.8 Common Documentation Pitfalls

### Pitfall 1: Incomplete CbCR Qualification Evidence

**Issue:** Claiming safe harbour without documenting that CbCR is "qualified"

**Risk:** Entire safe harbour claim could be rejected

**Solution:** Complete CbCR qualification checklist before claiming safe harbour

### Pitfall 2: Missing Reconciliations

**Issue:** Safe harbour figures don't tie back to source documents

**Risk:** Authority challenges data integrity

**Solution:** Prepare reconciliations for every key figure

### Pitfall 3: Inadequate "Once Out, Always Out" Tracking

**Issue:** Claiming safe harbour for jurisdiction that previously failed

**Risk:** Invalid safe harbour claim; penalties

**Solution:** Maintain year-by-year tracking register for each jurisdiction

### Pitfall 4: Mixing Data Sources

**Issue:** Using top-down data for some entities, bottom-up for others in same jurisdiction

**Risk:** CbCR deemed non-qualified for that jurisdiction

**Solution:** Document data source approach and ensure consistency

### Pitfall 5: Outdated QDMTT Status

**Issue:** Relying on QDMTT safe harbour when status has changed

**Risk:** Invalid safe harbour claim

**Solution:** Verify QDMTT status close to filing date; document verification

---

## Deliverable: Safe Harbour Documentation Checklist

```
SAFE HARBOUR DOCUMENTATION CHECKLIST
====================================

Group: _______________________________________________
Fiscal Year: _________________________________________
Prepared by: __________________ Date: ________________

SECTION A: TRANSITIONAL CBCR SAFE HARBOUR

Per Jurisdiction Claiming Safe Harbour:

JURISDICTION: _______________________

1. CbCR QUALIFICATION
   □ Qualification checklist completed
   □ Data source documented (top-down/bottom-up)
   □ Financial statement standard confirmed
   □ Auditor confirmation obtained (if required)
   □ Filed CbCR copy retained

2. TEST DOCUMENTATION
   □ De Minimis Test
     □ Workpaper completed
     □ Revenue figure sourced and reconciled
     □ PBT figure sourced and reconciled
     □ Result documented

   □ Simplified ETR Test
     □ Workpaper completed
     □ PBT figure sourced
     □ Simplified Covered Taxes calculated
     □ Non-Covered Taxes identified and excluded
     □ UTP adjustments made
     □ ETR calculated and compared to transition rate
     □ Result documented

   □ Routine Profits Test (if used)
     □ Workpaper completed
     □ Eligible payroll by entity
     □ Tangible assets by entity
     □ SBIE calculation
     □ Comparison to PBT
     □ Result documented

3. GIR SECTION 2
   □ Safe harbour election marked
   □ Test applied identified
   □ Supporting figures entered
   □ Top-up Tax recorded as zero

4. AUDIT DEFENCE FILE
   □ Tab created for jurisdiction
   □ All workpapers filed
   □ Reconciliations attached
   □ Sign-offs obtained

[Repeat for each jurisdiction]

SECTION B: QDMTT SAFE HARBOUR

Per Jurisdiction Claiming QDMTT Safe Harbour:

JURISDICTION: _______________________

□ QDMTT legislation reference documented
□ OECD register status verified
□ Status verification evidence retained
□ Local QDMTT return filed
□ QDMTT calculation retained
□ Payment evidence obtained
□ GIR Section 2 completed
□ Audit defence file updated

[Repeat for each jurisdiction]

SECTION C: "ONCE OUT, ALWAYS OUT" TRACKING

| Jurisdiction | 2024 | 2025 | 2026 | Status |
|--------------|------|------|------|--------|
| ____________ | P/F  | P/F  | P/F  | ______ |
| ____________ | P/F  | P/F  | P/F  | ______ |
| ____________ | P/F  | P/F  | P/F  | ______ |
| ____________ | P/F  | P/F  | P/F  | ______ |

P = Pass (Safe Harbour applied)
F = Fail (Full calculation required)
N/A = Not applicable / Not in scope

□ Tracking register maintained
□ Prior year results verified before current year claim

SECTION D: QUALITY CONTROL

□ Pre-filing review completed
□ All sections of checklist addressed
□ Reviewer sign-off obtained
□ Management approval documented
□ Filing authorisation confirmed

SECTION E: POST-FILING

□ Filing confirmation received
□ Documents archived
□ Tracking register updated
□ Lessons learned documented

FINAL SIGN-OFF

Preparer: ______________________ Date: ____________
Reviewer: ______________________ Date: ____________
Approver: ______________________ Date: ____________
```

---

## Section Summary

Effective safe harbour documentation requires:

1. **Accurate GIR Section 2 reporting** with all required data points
2. **Comprehensive working papers** for each test applied
3. **CbCR qualification evidence** demonstrating "qualified" status
4. **QDMTT verification** for QDMTT Safe Harbour claims
5. **Audit defence files** structured for authority review
6. **Quality control processes** ensuring accuracy before filing
7. **Proper retention** of all documentation for 10 years

The burden of proof for safe harbour claims rests with the MNE group. Thorough documentation is essential for audit defence and ongoing compliance.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Section 2 Purpose** | Captures safe harbour elections and supporting data |
| **CbCR Qualification** | Must document that CbCR meets "qualified" standard |
| **Test Documentation** | Detailed workpaper for each test (De Minimis, ETR, Routine Profits) |
| **QDMTT Verification** | Check OECD register; retain status evidence |
| **Audit Defence** | Structured file with reconciliations and approvals |
| **"Once Out, Always Out"** | Track year-by-year status per jurisdiction |
| **Retention** | Minimum 10 years recommended |
| **Quality Control** | Pre-filing review checklist essential |

---

## Sources

Key references for this section include:

- [OECD GloBE Information Return Guidance](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-pillar-two_10977da1/91a49ec3-en.pdf)
- [KPMG - Pillar Two GloBE Information Return](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2023/tnf-pillar-2-gir-jul25-2023.pdf)
- [PwC - Pillar 2 Safe Harbours](https://www.pwc.co.uk/services/tax/insights/pillar-2-safe-harbours.html)
- [OECD Safe Harbours and Penalty Relief](https://www.oecd.org/tax/beps/safe-harbours-and-penalty-relief-global-anti-base-erosion-rules-pillar-two.pdf)

---

*Section 9.4 Complete. This concludes Section 9: Simplified Reporting and Safe Harbours. Proceed to Section 10: Real-World Scenarios and Worked Examples.*
