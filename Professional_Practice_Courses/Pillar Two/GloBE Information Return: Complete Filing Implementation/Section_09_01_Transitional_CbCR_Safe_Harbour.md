# Section 9.1: Transitional CbCR Safe Harbour

## Learning Objectives

By the end of this section, you will be able to:

- Determine eligibility for the Transitional CbCR Safe Harbour
- Apply the three qualifying tests: De Minimis, Simplified ETR, and Routine Profits
- Calculate Simplified Covered Taxes for the Simplified ETR test
- Understand the "once out, always out" rule and its implications
- Prepare CbCR Safe Harbour Election documentation for the GIR
- Identify limitations and restrictions on safe harbour use

---

## 9.1.1 Introduction to the Transitional CbCR Safe Harbour

### Purpose and Policy Rationale

The OECD Inclusive Framework introduced the Transitional CbCR Safe Harbour to ease the compliance burden faced by MNE groups during the initial implementation years of the GloBE Rules. Full GloBE calculations require significant systems changes, data collection infrastructure, and expertise that many groups may not have in place for early filing periods.

**Key Benefits:**

| Benefit | Description |
|---------|-------------|
| **Compliance simplification** | Avoid detailed GloBE calculations where low top-up tax risk |
| **Cost reduction** | Leverage existing CbCR data and processes |
| **Resource allocation** | Focus detailed work on high-risk jurisdictions |
| **Transition period** | Time to build full GloBE compliance capability |

### How the Safe Harbour Works

The Transitional CbCR Safe Harbour operates by deeming the Top-up Tax for a jurisdiction to be **zero** where one of three simplified tests demonstrates low risk of actual top-up tax liability.

```
TRANSITIONAL CBCR SAFE HARBOUR MECHANISM
========================================

For each Tested Jurisdiction:

┌─────────────────────────────────────────────┐
│         Apply One of Three Tests            │
│                                             │
│  ┌─────────┐  ┌───────────┐  ┌───────────┐  │
│  │De Minimis│  │Simplified │  │ Routine   │  │
│  │  Test   │  │ ETR Test  │  │Profits Test│  │
│  └────┬────┘  └─────┬─────┘  └─────┬─────┘  │
│       │             │              │        │
│       └──────────┬──┴──────────────┘        │
│                  │                          │
│                  ▼                          │
│         Pass ANY ONE test?                  │
│              │                              │
│     ┌────────┴────────┐                     │
│     │                 │                     │
│    YES               NO                     │
│     │                 │                     │
│     ▼                 ▼                     │
│ Top-up Tax = 0    Full GloBE                │
│ (Safe Harbour)    Calculation               │
│                   Required                  │
└─────────────────────────────────────────────┘
```

### Applicability Period

The Transitional CbCR Safe Harbour applies to fiscal years:

- **Beginning on or before:** 31 December 2026
- **Ending no later than:** 30 June 2028

**Practical Application:**

| Fiscal Year End | Safe Harbour Available |
|-----------------|------------------------|
| 31 December 2024 | Yes (FY beginning 1 Jan 2024) |
| 31 December 2025 | Yes (FY beginning 1 Jan 2025) |
| 31 December 2026 | Yes (FY beginning 1 Jan 2026) |
| 31 December 2027 | No (FY begins after 31 Dec 2026) |

For most calendar year-end MNE groups, this provides **three fiscal years** of potential safe harbour relief (2024, 2025, 2026).

---

## 9.1.2 Eligibility Criteria

### Qualifying CbCR Requirement

The safe harbour relies on Country-by-Country Report (CbCR) data. To qualify, the CbCR must be a **Qualified CbCR**, meaning:

1. **Data Source:** Drawn from either:
   - Consolidated financial statements, OR
   - Individual entity accounts prepared using an acceptable financial standard

2. **Acceptable Financial Standards:**
   - IFRS
   - US GAAP
   - Local GAAP that produces materially similar results
   - Authorised financial accounting standard under GloBE Rules

3. **Consistency:** The same data source must be used consistently for all entities within a jurisdiction

**Important:** A CbCR may be "qualified" for some jurisdictions but not others within the same group.

**Example:**

```
Qualification Status by Jurisdiction
====================================

Jurisdiction A: Qualified Financial Statements used ──► QUALIFIES
Jurisdiction B: Management accounts used ──────────────► DOES NOT QUALIFY
Jurisdiction C: Qualified Financial Statements used ──► QUALIFIES
```

### Tested Jurisdiction Concept

A "Tested Jurisdiction" is any jurisdiction where the MNE group has Constituent Entities. Each Tested Jurisdiction is assessed independently against the three safe harbour tests.

**Key Principle:** You may apply the safe harbour selectively—qualifying for some jurisdictions while performing full GloBE calculations for others.

---

## 9.1.3 The Three Qualifying Tests

### Test 1: De Minimis Test

The De Minimis Test provides safe harbour treatment for jurisdictions with minimal activity.

**Criteria:**

| Metric | Threshold |
|--------|-----------|
| Total Revenue | Less than €10 million |
| Profit (Loss) Before Income Tax | Less than €1 million |

**Both conditions must be met.**

**Data Source:** CbCR figures for the jurisdiction

**Calculation Example:**

```
DE MINIMIS TEST - JURISDICTION A
================================

CbCR Data:
- Total Revenue: €8.5 million
- Profit Before Tax: €0.7 million

Test Application:
- Revenue < €10 million? YES (€8.5m < €10m)
- PBT < €1 million? YES (€0.7m < €1m)

Result: PASS - Safe Harbour applies
Top-up Tax deemed to be: €0
```

**Comparison to GloBE De Minimis Exclusion:**

| Feature | CbCR Safe Harbour De Minimis | GloBE Article 5.5 De Minimis |
|---------|------------------------------|------------------------------|
| Data Source | CbCR | GloBE calculations |
| Revenue Test | <€10 million | <€10 million |
| Profit Test | <€1 million PBT | <€1 million GloBE Income |
| Time Period | Current year only | Current year only |
| Multi-year averaging | Not available | Available |

---

### Test 2: Simplified ETR Test

The Simplified ETR Test compares a jurisdiction's effective tax rate (calculated using simplified methods) against a transition rate.

**Formula:**

```
                     Simplified Covered Taxes
Simplified ETR  =  ─────────────────────────────
                   Profit (Loss) Before Income Tax
```

**Transition Rates:**

| Fiscal Year Beginning | Transition Rate |
|----------------------|-----------------|
| 2023 | 15% |
| 2024 | 15% |
| 2025 | 16% |
| 2026 | 17% |

**Pass Condition:** Simplified ETR ≥ Transition Rate

#### Calculating Simplified Covered Taxes

Simplified Covered Taxes start with income tax expense from qualified financial statements, with specific adjustments:

```
SIMPLIFIED COVERED TAXES CALCULATION
====================================

Starting Point:
  Income Tax Expense (Current Year)         XXX
  + Deferred Tax Expense                    XXX
  ─────────────────────────────────────────────
  Total Income Tax Expense                  XXX

Adjustments:
  - Taxes that are NOT Covered Taxes       (XXX)
  - Uncertain Tax Positions (UTP reserves) (XXX)
  ─────────────────────────────────────────────
  = Simplified Covered Taxes                XXX
```

**Non-Covered Taxes to Exclude:**

| Tax Type | Treatment |
|----------|-----------|
| Taxes on distributions | Exclude |
| Taxes imposed on the payer (withholding) | Generally exclude |
| Non-income based taxes | Exclude |
| QDMTT | Exclude |
| IIR/UTPR Top-up Tax | Exclude |

**Calculation Example:**

```
SIMPLIFIED ETR TEST - JURISDICTION B (FY2024)
=============================================

Step 1: Gather Data from Qualified Financial Statements

  Current Tax Expense                    €3,200,000
  Deferred Tax Expense                     €800,000
  ────────────────────────────────────────────────
  Total Tax Expense per Accounts         €4,000,000

Step 2: Adjustments

  Less: Withholding taxes on dividends    (€150,000)
  Less: Uncertain tax position reserve    (€350,000)
  ────────────────────────────────────────────────
  Simplified Covered Taxes               €3,500,000

Step 3: CbCR Profit Before Tax

  Profit Before Tax (from CbCR)         €22,000,000

Step 4: Calculate Simplified ETR

  Simplified ETR = €3,500,000 / €22,000,000 = 15.91%

Step 5: Compare to Transition Rate

  Transition Rate (FY2024): 15%
  Simplified ETR (15.91%) ≥ 15%? YES

Result: PASS - Safe Harbour applies
Top-up Tax deemed to be: €0
```

#### Loss-Making Jurisdictions

Where a jurisdiction has a loss before income tax:

- **Loss with positive taxes:** Calculate ETR as normal (will produce high/negative ETR)
- **Loss with negative taxes (credits):** Generally qualifies under De Minimis or Routine Profits instead
- **Zero denominator situations:** Use Routine Profits Test

---

### Test 3: Routine Profits Test

The Routine Profits Test provides safe harbour treatment where the jurisdiction's profits do not exceed the Substance-Based Income Exclusion (SBIE) amount.

**Concept:** If all profits are attributable to substantive activities (payroll and tangible assets), there is deemed to be no excess profit subject to top-up tax.

**Pass Condition:** Profit Before Tax ≤ SBIE Amount

#### SBIE Calculation

The SBIE uses transitional percentages that decline over time:

**Transitional SBIE Rates:**

| Fiscal Year | Payroll Carve-out | Tangible Assets Carve-out |
|-------------|-------------------|---------------------------|
| 2024 | 9.8% | 7.8% |
| 2025 | 9.6% | 7.6% |
| 2026 | 9.4% | 7.4% |
| 2027 | 9.2% | 7.2% |
| 2028 | 9.0% | 7.0% |
| ... | ... | ... |
| 2033+ | 5.0% | 5.0% |

**SBIE Formula:**

```
SBIE = (Eligible Payroll × Payroll %) + (Eligible Tangible Assets × Asset %)
```

**Eligible Payroll Includes:**
- Wages, salaries, bonuses
- Employer social security contributions
- Pension contributions
- Share-based compensation (subject to elections)
- Other employee benefits

**Eligible Tangible Assets Include:**
- Property, plant, and equipment (net book value)
- Natural resources
- Right-of-use assets under leases
- Licences/concessions from government for tangible asset use

**Calculation Example:**

```
ROUTINE PROFITS TEST - JURISDICTION C (FY2024)
==============================================

Step 1: Calculate SBIE

  Eligible Payroll Costs               €5,000,000
  Payroll Carve-out (9.8%)             ×    9.8%
  ─────────────────────────────────────────────
  Payroll Component                      €490,000

  Tangible Assets (NBV)               €12,000,000
  Asset Carve-out (7.8%)               ×    7.8%
  ─────────────────────────────────────────────
  Asset Component                        €936,000

  Total SBIE                           €1,426,000

Step 2: Compare to Profit Before Tax

  CbCR Profit Before Tax               €1,200,000
  SBIE Amount                          €1,426,000

  PBT (€1.2m) ≤ SBIE (€1.426m)? YES

Result: PASS - Safe Harbour applies
Top-up Tax deemed to be: €0
```

**Important Note:** Unlike the other two tests, the Routine Profits Test requires **full SBIE calculations** under the GloBE Rules, not simplified CbCR data. This makes it more complex but useful for high-substance, lower-profit jurisdictions.

---

## 9.1.4 The "Once Out, Always Out" Rule

### Rule Application

A critical feature of the Transitional CbCR Safe Harbour is the **"once out, always out"** rule:

> If a jurisdiction fails to meet any of the three safe harbour tests in a fiscal year (or the MNE chooses not to apply the safe harbour), that jurisdiction **cannot benefit from the Transitional CbCR Safe Harbour in any subsequent fiscal year**.

**Practical Implications:**

```
"ONCE OUT, ALWAYS OUT" EXAMPLE
==============================

Jurisdiction D:

FY2024: Applies Safe Harbour, Passes Simplified ETR Test ──► OK
FY2025: Applies Safe Harbour, Fails All Three Tests ──────► FAILS
FY2026: Cannot use Transitional Safe Harbour ─────────────► BLOCKED
        (Must perform full GloBE calculations)

Jurisdiction E:

FY2024: Chooses NOT to apply Safe Harbour ────────────────► WAIVED
FY2025: Cannot use Transitional Safe Harbour ─────────────► BLOCKED
FY2026: Cannot use Transitional Safe Harbour ─────────────► BLOCKED
```

### Strategic Considerations

Given the "once out, always out" rule, MNE groups should:

1. **Assess carefully before first filing:** Model all three tests for each jurisdiction before deciding to apply

2. **Consider voluntary exclusion:** For borderline jurisdictions, it may be better to perform full calculations from the start rather than risk failing mid-period

3. **Monitor year-on-year:** Jurisdictions passing in Year 1 may fail in Year 2 due to:
   - Increased profitability
   - Reduced substance
   - Tax rate changes
   - One-off items

4. **Document decisions:** Record the rationale for applying or not applying the safe harbour for each jurisdiction

### Transition Rate Increases

The increasing transition rates create additional risk:

| Fiscal Year | Transition Rate | Risk Profile |
|-------------|-----------------|--------------|
| 2024 | 15% | Lower risk of failure |
| 2025 | 16% | Moderate risk |
| 2026 | 17% | Higher risk for borderline jurisdictions |

**Example Impact:**

```
Jurisdiction with Simplified ETR of 15.5%:

FY2024: 15.5% ≥ 15% ──► PASS
FY2025: 15.5% ≥ 16% ──► FAIL
FY2026: Blocked by "once out, always out" rule
```

---

## 9.1.5 Using CbCR Data for GIR

### Data Mapping: CbCR to GIR

When the Transitional CbCR Safe Harbour applies, GIR reporting is simplified:

| GIR Element | Full Calculation Required | Safe Harbour Approach |
|-------------|---------------------------|----------------------|
| Section 1: Group Info | Yes | Yes (unchanged) |
| Section 2: Jurisdiction Data | Full GloBE calculations | Simplified—CbCR-based |
| Section 3: Entity Data | Detailed per-entity | Reduced requirements |
| Top-up Tax | Calculate per rules | Deemed zero |

### GIR Section 2 Reporting Under Safe Harbour

For jurisdictions qualifying for safe harbour, the GIR Section 2 requires:

```
GIR SECTION 2 - SAFE HARBOUR JURISDICTION
=========================================

Required Fields:
☑ Jurisdiction identifier
☑ Safe harbour election indicator
☑ Test applied (De Minimis / Simplified ETR / Routine Profits)
☑ CbCR revenue (for De Minimis)
☑ CbCR profit/loss before tax
☑ Simplified Covered Taxes (for Simplified ETR)
☑ SBIE amount (for Routine Profits)
☑ Top-up Tax: €0

NOT Required (when safe harbour applies):
☐ Detailed GloBE Income calculations
☐ Full Covered Taxes calculations
☐ Detailed ETR computation
☐ Allocation of Top-up Tax to entities
```

### CbCR Data Quality Considerations

Using CbCR data for safe harbour purposes requires attention to data quality:

| Consideration | Recommendation |
|---------------|----------------|
| **Consistency** | Use same data source (consolidated or separate) for all entities in jurisdiction |
| **Currency** | Ensure consistent EUR conversion methodology |
| **Timing** | CbCR and GIR should cover same fiscal period |
| **Reconciliation** | Document any differences between CbCR and GloBE data |

---

## 9.1.6 Limitations and Restrictions

### Situations Where Safe Harbour Cannot Apply

The Transitional CbCR Safe Harbour is **not available** in certain circumstances:

1. **Non-Qualifying CbCR:**
   - CbCR populated using management accounts (not qualified financial statements)
   - Inconsistent data sources within a jurisdiction

2. **Permanent Establishments:**
   - PE data in CbCR may not align with GloBE treatment
   - Additional analysis required for PE jurisdictions

3. **Hybrid Entity Situations:**
   - Reverse hybrid entities
   - Stateless entities
   - Complex flow-through structures

4. **Minority-Owned Constituent Entities:**
   - Where CbCR consolidation differs from GloBE ownership rules

5. **Investment Entities:**
   - Excluded entities under GloBE
   - Require separate analysis

### Limitations on Relief

Even where the safe harbour applies, certain obligations remain:

| Obligation | Still Required? |
|------------|-----------------|
| GIR filing | Yes |
| Safe harbour election in GIR | Yes |
| Documentation retention | Yes |
| Local Top-up Tax returns | Yes (where applicable) |
| QDMTT returns | Yes (separate from safe harbour) |

### Coordination with QDMTT Safe Harbour

The Transitional CbCR Safe Harbour is separate from the QDMTT Safe Harbour:

- **Transitional CbCR Safe Harbour:** Applies to IIR and UTPR calculations
- **QDMTT Safe Harbour:** Applies to recognition of QDMTT paid in a jurisdiction

A jurisdiction may qualify for both, one, or neither safe harbour.

---

## 9.1.7 Practical Application Workflow

### Step-by-Step Safe Harbour Assessment

```
SAFE HARBOUR ASSESSMENT WORKFLOW
================================

STEP 1: Identify All Tested Jurisdictions
         └── List all jurisdictions with Constituent Entities

STEP 2: Verify CbCR Qualification
         └── Confirm Qualified Financial Statements used
         └── Check consistency within each jurisdiction

STEP 3: Apply De Minimis Test
         └── Revenue < €10m AND PBT < €1m?
         └── If YES → Safe Harbour applies → Move to next jurisdiction
         └── If NO → Continue to Step 4

STEP 4: Apply Simplified ETR Test
         └── Calculate Simplified Covered Taxes
         └── Calculate Simplified ETR
         └── Compare to Transition Rate
         └── If PASS → Safe Harbour applies → Move to next jurisdiction
         └── If FAIL → Continue to Step 5

STEP 5: Apply Routine Profits Test
         └── Calculate SBIE (full calculation required)
         └── Compare PBT to SBIE
         └── If PBT ≤ SBIE → Safe Harbour applies
         └── If PBT > SBIE → Full GloBE calculation required

STEP 6: Document Results
         └── Record test applied and results
         └── Prepare safe harbour election for GIR
         └── Retain supporting documentation
```

### Documentation Requirements

For each jurisdiction where safe harbour is claimed:

**Required Documentation:**

| Document | Purpose |
|----------|---------|
| CbCR extract | Source data evidence |
| Financial statements | Qualified FS confirmation |
| Tax expense reconciliation | Simplified Covered Taxes |
| SBIE calculation (if applicable) | Routine Profits Test |
| Test calculation workpaper | Audit trail |
| Management approval | Governance |

---

## 9.1.8 Case Studies

### Case Study 1: Multi-Test Assessment

**Scenario:** UK MNE group with operations in Ireland, Netherlands, and Singapore. Assess safe harbour eligibility for FY2024.

**Ireland Data:**
- Revenue: €8 million
- PBT: €0.8 million

**Analysis:**
```
De Minimis Test:
- Revenue €8m < €10m ✓
- PBT €0.8m < €1m ✓
Result: PASS - Apply safe harbour
```

**Netherlands Data:**
- Revenue: €45 million
- PBT: €5 million
- Simplified Covered Taxes: €850,000

**Analysis:**
```
De Minimis Test:
- Revenue €45m < €10m ✗
- FAIL De Minimis

Simplified ETR Test:
- Simplified ETR = €850,000 / €5,000,000 = 17%
- Transition Rate (2024): 15%
- 17% ≥ 15% ✓
Result: PASS - Apply safe harbour
```

**Singapore Data:**
- Revenue: €30 million
- PBT: €4 million
- Simplified Covered Taxes: €500,000
- Eligible Payroll: €8 million
- Tangible Assets: €25 million

**Analysis:**
```
De Minimis Test: FAIL (Revenue > €10m)

Simplified ETR Test:
- Simplified ETR = €500,000 / €4,000,000 = 12.5%
- 12.5% < 15%
- FAIL Simplified ETR

Routine Profits Test:
- SBIE = (€8m × 9.8%) + (€25m × 7.8%)
- SBIE = €784,000 + €1,950,000 = €2,734,000
- PBT €4m > SBIE €2.734m
- FAIL Routine Profits

Result: Full GloBE calculation required for Singapore
```

### Case Study 2: "Once Out, Always Out" Planning

**Scenario:** German subsidiary has Simplified ETR of 15.3% in FY2024. Should the group apply the safe harbour?

**Analysis:**

| Year | Transition Rate | Projected ETR | Outcome |
|------|-----------------|---------------|---------|
| 2024 | 15% | 15.3% | Pass |
| 2025 | 16% | 15.3% | **Fail** |
| 2026 | 17% | - | Blocked |

**Recommendation:** Consider performing full GloBE calculations from FY2024 rather than risking safe harbour failure in FY2025 and being locked out for FY2026.

**Alternative:** If ETR improvement is expected (e.g., new investment, law change), may be worth applying safe harbour in FY2024, but document the risk assessment.

---

## Deliverable: CbCR Safe Harbour Election Form

### Template: Safe Harbour Assessment and Election

```
TRANSITIONAL CBCR SAFE HARBOUR
ASSESSMENT AND ELECTION FORM
==============================

PART A: GROUP INFORMATION

MNE Group Name: _____________________________________
UPE Name: ___________________________________________
Fiscal Year End: ____________________________________
Prepared by: __________________ Date: _______________
Reviewed by: __________________ Date: _______________

PART B: TESTED JURISDICTIONS

List all jurisdictions with Constituent Entities:

| # | Jurisdiction | # of CEs | CbCR Qualified? | Safe Harbour Claimed? |
|---|--------------|----------|-----------------|----------------------|
| 1 | ____________ | ________ | Yes / No        | Yes / No             |
| 2 | ____________ | ________ | Yes / No        | Yes / No             |
| 3 | ____________ | ________ | Yes / No        | Yes / No             |
| 4 | ____________ | ________ | Yes / No        | Yes / No             |
| 5 | ____________ | ________ | Yes / No        | Yes / No             |
[Continue as needed]

PART C: SAFE HARBOUR TEST RESULTS

For each jurisdiction claiming safe harbour:

JURISDICTION: _______________________

Test 1: De Minimis
□ Applied  □ Not Applied

Revenue (CbCR):                    €____________
PBT (CbCR):                        €____________
Revenue < €10m?                    □ Yes  □ No
PBT < €1m?                         □ Yes  □ No
De Minimis Test Result:            □ PASS  □ FAIL

Test 2: Simplified ETR
□ Applied  □ Not Applied

PBT (CbCR):                        €____________
Simplified Covered Taxes:          €____________
Simplified ETR:                    ____________%
Transition Rate (FY____):          ____________%
ETR ≥ Transition Rate?             □ Yes  □ No
Simplified ETR Test Result:        □ PASS  □ FAIL

Test 3: Routine Profits
□ Applied  □ Not Applied

PBT (CbCR):                        €____________
Eligible Payroll:                  €____________
Payroll Carve-out (%):             ____________%
Payroll SBIE:                      €____________
Tangible Assets (NBV):             €____________
Asset Carve-out (%):               ____________%
Asset SBIE:                        €____________
Total SBIE:                        €____________
PBT ≤ SBIE?                        □ Yes  □ No
Routine Profits Test Result:       □ PASS  □ FAIL

OVERALL RESULT FOR JURISDICTION:
□ Safe Harbour Applies (at least one test passed)
□ Safe Harbour Does Not Apply (all tests failed)

[Repeat Part C for each jurisdiction]

PART D: SUMMARY

| Jurisdiction | Test Applied | Result | Top-up Tax |
|--------------|--------------|--------|------------|
| ____________ | ____________ | PASS   | €0         |
| ____________ | ____________ | PASS   | €0         |
| ____________ | N/A          | FAIL   | Calculate  |
[Continue as needed]

PART E: ELECTION DECLARATION

The MNE Group hereby elects to apply the Transitional CbCR Safe Harbour
for the jurisdictions marked "PASS" above for the fiscal year ending
________________.

We confirm that:
□ The CbCR used is a Qualified CbCR for the relevant jurisdictions
□ The data sources are consistent with GloBE requirements
□ The calculations have been performed in accordance with OECD guidance
□ Supporting documentation is retained for audit purposes

Authorised Signatory: _______________________________
Name: _____________________________________________
Title: _____________________________________________
Date: ______________________________________________

PART F: ATTACHMENTS

□ CbCR extract for relevant jurisdictions
□ Simplified Covered Taxes calculation workpapers
□ SBIE calculations (where Routine Profits Test applied)
□ Financial statement extracts (tax expense)
□ Currency conversion documentation
```

---

## Section Summary

The Transitional CbCR Safe Harbour provides valuable compliance relief during the initial years of GloBE implementation by:

1. **Reducing calculation burden** through use of existing CbCR data
2. **Providing three alternative tests** to demonstrate low top-up tax risk
3. **Simplifying GIR reporting** for qualifying jurisdictions
4. **Allowing jurisdiction-by-jurisdiction application**

However, the **"once out, always out"** rule requires careful planning, as failure in any year permanently excludes that jurisdiction from future safe harbour treatment.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Applicability Period** | FY beginning on or before 31 Dec 2026 |
| **Three Tests** | De Minimis, Simplified ETR, Routine Profits |
| **De Minimis Thresholds** | Revenue <€10m AND PBT <€1m |
| **Transition Rates** | 15% (2024), 16% (2025), 17% (2026) |
| **SBIE Rates (2024)** | 9.8% payroll, 7.8% tangible assets |
| **Once Out, Always Out** | Failure in one year blocks all future years |
| **Qualified CbCR** | Must use qualified financial statements |
| **GIR Impact** | Simplified Section 2 reporting; Top-up Tax = €0 |

---

## Sources

Key references for this section include:

- [OECD Safe Harbours and Penalty Relief Guidance](https://www.oecd.org/tax/beps/safe-harbours-and-penalty-relief-global-anti-base-erosion-rules-pillar-two.pdf)
- [Transitional CbCR Safe Harbour - OECD Pillars](https://oecdpillars.com/pillar-tab/transitional-cbcr-safe-harbour/)
- [PwC - Pillar 2 Safe Harbours](https://www.pwc.co.uk/services/tax/insights/pillar-2-safe-harbours.html)
- [EY - Pillar Two Country-by-Country Safe Harbors](https://www.ey.com/en_be/insights/tax/pillar-two-what-is-the-importance-of-the-country-by-country-safe-harbors)

---

*Section 9.1 Complete. Proceed to Section 9.2: QDMTT Safe Harbour Impact on GIR.*
