# Section 12.1: GIR and Tax Calculation Alignment

## Learning Objectives

By the end of this section, you will be able to:
- Map data dependencies between GIR reporting and Pillar Two tax calculations
- Coordinate timing between GIR preparation and tax provision processes
- Reconcile GIR data to tax calculations and financial statement disclosures
- Use the GIR-to-Tax Calculation Reconciliation Tool effectively
- Implement integrated workflows to ensure consistency across all outputs

---

## Introduction

The GloBE Information Return (GIR) and Pillar Two tax calculations are intrinsically linked but serve different purposes:

| Output | Purpose | Audience | Timing |
|--------|---------|----------|--------|
| **GIR** | Compliance reporting | Tax authorities | 15/18 months post-FY |
| **Tax Provision** | Financial reporting | Auditors, investors | Year-end close |
| **Tax Return** | Tax liability settlement | Tax authorities | Local deadlines |
| **Cash Tax Payment** | Settlement of liability | Tax authorities | Payment deadlines |

Misalignment between these outputs creates:
- Authority scrutiny and potential penalties
- Audit adjustments and restatements
- Cash flow planning failures
- Governance and control deficiencies

This section establishes the framework for ensuring alignment across all Pillar Two compliance outputs.

---

## Part 1: Data Dependencies Between GIR and Tax Calculations

### 1.1 Shared Data Architecture

The GIR and Pillar Two tax calculations share common data inputs:

**Single Source of Truth Model:**

```
                     MASTER GloBE CALCULATION
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
    GIR Section 2       Tax Provision        Local Tax
   (Jurisdictional)    (IAS 12/ASC 740)       Returns
         │                    │                    │
         ▼                    ▼                    ▼
    GIR Section 3      Financial Statement   QDMTT/IIR/UTPR
   (Top-up Tax)         Disclosures            Payments
```

### 1.2 Core Data Elements

**Entity and Scope Data:**

| Data Element | GIR Use | Tax Provision Use | Tax Return Use |
|--------------|---------|-------------------|----------------|
| CE list | Section 1 entity identification | Scope determination | Filing entities |
| Ownership percentages | Allocation calculations | Consolidation | Attribution |
| Excluded entities | Scope exclusion | Scope exclusion | N/A |
| €750M threshold | Scope test | Scope test | N/A |

**Financial Data:**

| Data Element | GIR Use | Tax Provision Use | Tax Return Use |
|--------------|---------|-------------------|----------------|
| FANIL | GloBE Income starting point | Tax expense calculation | N/A |
| GloBE Income | ETR denominator | ETR denominator | Taxable base |
| Revenue | Section 2 reporting | Disclosure | Local reporting |

**Tax Data:**

| Data Element | GIR Use | Tax Provision Use | Tax Return Use |
|--------------|---------|-------------------|----------------|
| Current tax expense | Covered Taxes input | Current tax provision | Tax payable |
| Deferred tax movement | Covered Taxes adjustment | Deferred tax provision | N/A |
| Covered Taxes | ETR numerator | ETR numerator | N/A |
| Top-up Tax | Section 3 allocation | Additional tax expense | Tax liability |

**Carve-Out Data:**

| Data Element | GIR Use | Tax Provision Use | Tax Return Use |
|--------------|---------|-------------------|----------------|
| Eligible payroll | SBIE calculation | SBIE calculation | Local deduction |
| Tangible assets | SBIE calculation | SBIE calculation | N/A |
| Transition rates | Rate application | Rate application | N/A |

### 1.3 Data Flow Architecture

**Recommended Process Flow:**

```
Phase 1: Data Collection (Months 1-3 post-FY)
─────────────────────────────────────────────
• Extract FANIL from financial close
• Gather tax provision workpapers
• Collect payroll and asset data for SBIE
• Confirm entity list and ownership

Phase 2: GloBE Calculation (Months 3-6 post-FY)
─────────────────────────────────────────────
• Compute GloBE Income per jurisdiction
• Calculate Adjusted Covered Taxes
• Determine jurisdictional ETRs
• Calculate Top-up Tax

Phase 3: Reconciliation (Months 6-9 post-FY)
─────────────────────────────────────────────
• Reconcile to tax provision
• Reconcile to CbCR
• Reconcile to financial statements
• Resolve variances

Phase 4: GIR Preparation (Months 9-15 post-FY)
─────────────────────────────────────────────
• Prepare GIR sections
• Validate XML
• Obtain approvals
• File GIR
```

### 1.4 Critical Data Dependencies

**Circular Dependencies:**

| Calculation | Depends On | Creates Circularity |
|-------------|------------|---------------------|
| GloBE Income | Tax expense add-back | Tax expense depends on Top-up Tax |
| Covered Taxes | Deferred tax | Deferred tax affected by Top-up Tax |
| Top-up Tax | ETR | ETR depends on Covered Taxes |
| QDMTT | Top-up Tax calculation | QDMTT is Covered Tax |

**Breaking Circularity:**

The OECD rules address circularity through:
1. **Initial calculation without Top-up Tax**: Calculate provisional GloBE Income and ETR
2. **Top-up Tax determination**: Calculate Top-up Tax based on provisional figures
3. **Iteration if needed**: QDMTT becomes Covered Tax in subsequent calculation
4. **Final determination**: Settle on final figures

---

## Part 2: Timing Considerations

### 2.1 Comparative Timeline

**Key Milestones for December Year-End MNE:**

| Milestone | Typical Timing | Pillar Two Relevance |
|-----------|----------------|---------------------|
| Year-end | 31 December | FY close |
| Preliminary close | January | Initial data available |
| Audit fieldwork | February-March | Tax provision finalised |
| Annual report filing | March-April | FS disclosures required |
| **Tax provision lock** | March | Pillar Two expense determined |
| CbCR preparation | April-June | Safe harbour data source |
| CbCR filing deadline | December | 12 months post-FY |
| **First GIR filing** | 30 June Year+2 | 18 months (first year) |
| **Subsequent GIR filing** | 31 March Year+2 | 15 months (ongoing) |

### 2.2 Tax Provision vs. GIR Timing Mismatch

**Challenge:**
The tax provision is finalised 3-4 months after year-end, but the GIR is filed 15-18 months after year-end.

**Potential Issues:**

| Timing Gap Issue | Consequence | Mitigation |
|------------------|-------------|------------|
| Data changes post-provision | GIR differs from provision | Document variances |
| True-ups identified | Provision adjustment needed | Prior period adjustment |
| Election decisions | Different elections in GIR | Align elections early |
| Amended returns | GIR inconsistent with local | Coordinate amendments |

### 2.3 Integrated Timeline Model

**Recommended Approach:**

| Activity | Q1 (Year+1) | Q2 (Year+1) | Q3 (Year+1) | Q4 (Year+1) | Q1-Q2 (Year+2) |
|----------|-------------|-------------|-------------|-------------|----------------|
| Data collection | ████████ | | | | |
| GloBE calculation | ████ | ████████ | | | |
| Tax provision | ████████ | ████ | | | |
| Provision lock | █ | | | | |
| GIR preparation | | | ████████ | ████████ | ████ |
| Reconciliation | | ████ | ████ | ████ | |
| GIR filing | | | | | ████ |

### 2.4 IAS 12 Amendments and Timing

**Temporary Exception:**
The May 2023 IAS 12 amendments provide temporary relief from recognising deferred taxes arising from Pillar Two legislation.

**Timing Implications:**

| Period | Treatment | Disclosure Required |
|--------|-----------|---------------------|
| Pre-enactment | No Pillar Two deferred tax | Qualitative exposure |
| Post-enactment | Current Top-up Tax only | Quantitative disclosure |
| Ongoing | Exception continues | Annual reassessment |

**Disclosure Requirements:**
- Qualitative and quantitative information about exposure to Pillar Two taxes
- Known or reasonably estimable information about exposure
- Separate disclosure of Top-up Tax expense

---

## Part 3: Reconciliation Requirements

### 3.1 GIR-to-Tax Provision Reconciliation

**Why Reconciliation is Critical:**
Tax authorities will compare GIR data to published financial statements. Unexplained variances trigger scrutiny.

**Required Reconciliation Points:**

| GIR Element | Tax Provision Element | Expected Relationship |
|-------------|----------------------|----------------------|
| GloBE Income (total) | Group PBT ± adjustments | Traceable difference |
| Covered Taxes (total) | Tax expense ± adjustments | Traceable difference |
| ETR by jurisdiction | Jurisdictional ETR | Should match |
| Top-up Tax (total) | Additional tax expense | Exact match |
| QDMTT offset | Tax credit/offset | Exact match |

### 3.2 Reconciliation Framework

**Level 1: Group-Level Reconciliation**

```
Tax Provision (per Financial Statements)
                            │
                            ▼
           ┌────────────────────────────────┐
           │   RECONCILING ITEMS            │
           │                                │
           │ + Non-GloBE jurisdictions      │
           │ - Excluded entities            │
           │ ± Timing differences           │
           │ ± Election differences         │
           │ ± Adjustment basis differences │
           │                                │
           └────────────────────────────────┘
                            │
                            ▼
               GIR Total (Section 3)
```

**Level 2: Jurisdiction-Level Reconciliation**

| Line | Description | Amount (€) |
|------|-------------|------------|
| 1 | Tax provision - jurisdictional current tax | ___ |
| 2 | Add: Deferred tax movement (per provision) | ___ |
| 3 | Tax provision total | ___ |
| 4 | Adjust: Timing differences | ___ |
| 5 | Adjust: Basis differences | ___ |
| 6 | Adjust: Covered Tax exclusions | ___ |
| 7 | **GIR Covered Taxes** | ___ |
| 8 | GIR GloBE Income | ___ |
| 9 | **GIR ETR** (Line 7 ÷ Line 8) | ___% |
| 10 | Tax provision ETR | ___% |
| 11 | **ETR Variance** | ___% |
| 12 | Variance explanation | [Document] |

### 3.3 Common Reconciling Items

**GloBE Income Differences:**

| Reconciling Item | Direction | Explanation |
|------------------|-----------|-------------|
| Policy disallowed expenses | GloBE > FS | Fines, penalties added back |
| Excluded dividends | GloBE < FS | Intercompany dividends removed |
| Stock compensation | Variable | Election-dependent |
| Asset gains/losses | Variable | Election-dependent |
| Prior period errors | Variable | Timing allocation differs |

**Covered Taxes Differences:**

| Reconciling Item | Direction | Explanation |
|------------------|-----------|-------------|
| DTL recapture | Covered < Provision | 5-year rule adjustment |
| UTP adjustments | Variable | Different treatment timing |
| Allocation basis | Variable | Push-down methodology |
| WHT timing | Variable | Accrual vs. payment |

### 3.4 Variance Tolerance and Documentation

**Tolerance Framework:**

| Variance Level | Action Required |
|----------------|-----------------|
| <1% | Document, no action |
| 1-5% | Investigate, document explanation |
| 5-10% | Senior review, formal memo |
| >10% | Escalate, potential restatement |

**Documentation Standard:**
Every variance must have:
1. Quantification (amount and percentage)
2. Root cause explanation
3. Supporting calculation
4. Sign-off by reviewer

---

## Part 4: GIR-to-Tax Calculation Reconciliation Tool

### 4.1 Tool Structure

The GIR-to-Tax Calculation Reconciliation Tool provides a standardised framework for documenting alignment between GIR and tax calculations.

**Workbook Tabs:**

| Tab | Purpose |
|-----|---------|
| 1. Instructions | How to use the tool |
| 2. Group Summary | High-level reconciliation |
| 3. Jurisdiction Detail | Per-jurisdiction reconciliation |
| 4. GloBE Income Recon | Income reconciliation |
| 5. Covered Taxes Recon | Tax reconciliation |
| 6. ETR Comparison | ETR alignment verification |
| 7. Top-up Tax Recon | Allocation reconciliation |
| 8. Variance Analysis | Exception reporting |
| 9. Sign-off | Approval documentation |

### 4.2 Group Summary Tab

**GIR-to-Tax Provision Reconciliation Summary**

| Reference | Description | GIR (€) | Tax Provision (€) | Variance (€) | Variance % |
|-----------|-------------|---------|-------------------|--------------|------------|
| **A. GloBE Income** |||||
| A.1 | Total GloBE Income | ___ | ___ | ___ | ___% |
| A.2 | Total GloBE Loss | ___ | ___ | ___ | ___% |
| A.3 | Net GloBE Income | ___ | ___ | ___ | ___% |
| **B. Covered Taxes** |||||
| B.1 | Current tax component | ___ | ___ | ___ | ___% |
| B.2 | Deferred tax component | ___ | ___ | ___ | ___% |
| B.3 | Total Adjusted Covered Taxes | ___ | ___ | ___ | ___% |
| **C. Aggregate ETR** |||||
| C.1 | Weighted average ETR | ___% | ___% | ___% | — |
| **D. Top-up Tax** |||||
| D.1 | Gross Top-up Tax | ___ | ___ | ___ | ___% |
| D.2 | Less: QDMTT offset | ___ | ___ | ___ | ___% |
| D.3 | Net Top-up Tax | ___ | ___ | ___ | ___% |
| **E. Reconciliation Status** |||||
| E.1 | Variances within tolerance? | □ Yes / □ No |||
| E.2 | All variances documented? | □ Yes / □ No |||
| E.3 | Sign-off obtained? | □ Yes / □ No |||

### 4.3 Jurisdiction Detail Tab

**Per-Jurisdiction Reconciliation**

For each jurisdiction with GloBE presence:

| Jurisdiction: | [Name] | Code: | [XX] |
|---------------|--------|-------|------|

| Line | Element | GIR | Tax Calc | Variance | Explanation |
|------|---------|-----|----------|----------|-------------|
| **GloBE Income** ||||||
| 1 | Revenue | ___ | ___ | ___ | ___ |
| 2 | GloBE Income/(Loss) | ___ | ___ | ___ | ___ |
| **Covered Taxes** ||||||
| 3 | Current tax | ___ | ___ | ___ | ___ |
| 4 | Deferred tax | ___ | ___ | ___ | ___ |
| 5 | Adjusted Covered Taxes | ___ | ___ | ___ | ___ |
| **ETR** ||||||
| 6 | ETR (Line 5 ÷ Line 2) | ___% | ___% | ___% | ___ |
| **SBIE** ||||||
| 7 | Payroll carve-out | ___ | ___ | ___ | ___ |
| 8 | Asset carve-out | ___ | ___ | ___ | ___ |
| 9 | Total SBIE | ___ | ___ | ___ | ___ |
| **Top-up Tax** ||||||
| 10 | Excess Profit | ___ | ___ | ___ | ___ |
| 11 | Top-up Tax % | ___% | ___% | ___% | ___ |
| 12 | Jurisdictional Top-up Tax | ___ | ___ | ___ | ___ |
| 13 | QDMTT offset | ___ | ___ | ___ | ___ |
| 14 | **Net Top-up Tax** | ___ | ___ | ___ | ___ |

### 4.4 Variance Analysis Tab

**Exception Report**

| Jurisdiction | Element | GIR | Tax Calc | Variance | % | Root Cause | Action |
|--------------|---------|-----|----------|----------|---|------------|--------|
| ___ | ___ | ___ | ___ | ___ | ___% | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___% | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___% | ___ | ___ |

**Variance Categories:**

| Code | Category | Description |
|------|----------|-------------|
| T | Timing | Different recognition period |
| B | Basis | Different calculation methodology |
| E | Election | Different election applied |
| R | Rounding | Immaterial rounding difference |
| S | Source | Different data source used |
| X | Error | Requires correction |

### 4.5 Sign-Off Tab

**Reconciliation Approval**

| MNE Group: | ___ |
|------------|-----|
| Fiscal Year: | ___ |
| Prepared by: | ___ |
| Date: | ___ |

**Certification:**

| Certification Statement | Confirmed |
|------------------------|-----------|
| All jurisdictions have been reconciled | □ |
| All variances are documented and explained | □ |
| Variances within tolerance (or escalated) | □ |
| GIR data matches master GloBE calculation | □ |
| Tax provision aligned with GIR | □ |

**Approvals:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Preparer | ___ | ___ | ___ |
| Tax Manager | ___ | ___ | ___ |
| Tax Director | ___ | ___ | ___ |
| Finance Director | ___ | ___ | ___ |

---

## Part 5: Implementation Best Practices

### 5.1 Single Source of Truth Governance

**Data Ownership Model:**

| Data Category | Owner | Custodian | Consumers |
|---------------|-------|-----------|-----------|
| Entity structure | Legal | Tax | All |
| Financial data | Finance | Accounting | Tax, GIR |
| Tax provision | Tax | Tax Technology | GIR, Finance |
| GloBE calculation | Tax | Tax Technology | GIR, Provision |
| GIR | Tax | Tax Technology | Authorities |

**Change Control:**
Once the master GloBE calculation is locked:
1. Any change requires formal request
2. Impact analysis on all dependent outputs
3. Approval from Tax Director
4. Documented amendment trail

### 5.2 Process Integration

**Integrated Calendar:**

| Month | Finance | Tax Provision | GIR |
|-------|---------|---------------|-----|
| Jan | Close | Data gathering | — |
| Feb | Audit | Calculations | — |
| Mar | Filing | Lock | — |
| Apr | — | True-up monitoring | Data validation |
| May | — | — | Draft preparation |
| Jun | Q2 close | Q2 update | — |
| Jul-Sep | — | — | GIR finalisation |
| Oct-Dec | Year-end prep | Estimate | GIR review |
| Jan-Mar | Close | Lock | Filing |

### 5.3 Technology Enablement

**System Requirements:**

| Capability | Purpose | Solution Options |
|------------|---------|------------------|
| Centralised data | Single source | ERP, data warehouse |
| Calculation engine | GloBE computation | Specialist software, Excel |
| Workflow management | Process control | GRC tool, workflow software |
| Document management | Audit trail | DMS, SharePoint |
| Reporting | Reconciliation | BI tool, Excel |

### 5.4 Control Framework

**Key Controls:**

| Control | Objective | Frequency | Owner |
|---------|-----------|-----------|-------|
| Data extraction validation | Complete/accurate data | Per extraction | Tax Technology |
| Calculation review | Mathematical accuracy | Per calculation | Tax Manager |
| Reconciliation review | GIR-provision alignment | Pre-filing | Tax Director |
| Sign-off verification | Governance compliance | Pre-filing | CFO/Tax Director |
| Amendment tracking | Change documentation | As needed | Tax Manager |

---

## Key Takeaways

1. **Single source of truth**: All Pillar Two outputs (GIR, provision, returns) must derive from one master calculation

2. **Timing coordination**: 12-15 month gap between provision lock and GIR filing requires careful change management

3. **Mandatory reconciliation**: GIR-to-provision reconciliation is essential for audit defence and authority credibility

4. **Variance documentation**: Every difference must be quantified, explained, and signed off

5. **IAS 12 alignment**: Temporary deferred tax exception simplifies provision but requires disclosure

6. **Integrated process**: Calendar-driven coordination between finance, tax, and GIR teams prevents misalignment

7. **Governance framework**: Clear ownership, change control, and sign-off protocols are non-negotiable

---

## Further Reading and Resources

- [PwC: Global Implementation of Pillar Two - Deferred Taxes and Disclosures](https://viewpoint.pwc.com/dt/gx/en/pwc/in_depths/in_depths_INT/in_depths_INT/global-implementation-of-pillar-two-impact-on-deferred-taxes-and-financial-statement-disclosures.html)
- [Deloitte: Pillar Two FAQ](https://dart.deloitte.com/USDART/home/publications/deloitte/financial-reporting-alerts/2024/faq-pillar-two-international-tax-oecd)
- [BDO: What Pillar Two Means for Income Tax Accounting](https://www.bdo.com/insights/tax/what-pillar-two-means-for-income-tax-accounting)
- [oecdpillars.com: ETR Calculation and Top-up Tax](https://oecdpillars.com/pillar-tab/etr-calculation-and-top-up-tax-2/)
- [oecdpillars.com: Deferred Tax](https://oecdpillars.com/pillar-tab/deferred-tax/)
- [OECD: GloBE Rules Fact Sheets](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/pillar-two-globe-rules-fact-sheets.pdf)

---

*End of Section 12.1*
