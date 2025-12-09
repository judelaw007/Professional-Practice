# Case Study 8: Staying Current

## Introduction

This case study concludes the ADIT Pillar Two Professional Practice Course by applying the monitoring and governance concepts from Part 8. You will analyse new regulatory guidance, update governance documentation, and prepare Board reporting—the ongoing professional skills essential for maintaining Pillar Two compliance.

**Context:** You are the Pillar Two compliance lead at Stratos Holdings plc. It is January 2026. The MNE Group has completed its first GloBE calculation cycle for FY 2025 (as covered in Case Study 7). The OECD has just released new Administrative Guidance that may affect Stratos's compliance position.

**Time estimate:** 90-120 minutes

---

## Background: Stratos's Current Position — January 2026

### FY 2025 Compliance Summary

Stratos has completed its first Pillar Two compliance cycle:

| Metric | FY 2025 Result |
|--------|----------------|
| Total Top-up Tax liability | €1,242,558 |
| IIR component (UK collected) | €807,518 |
| QDMTT component (Ireland) | €435,040 |
| Jurisdictions in scope | 7 |
| Safe Harbour jurisdictions | 5 of 7 |
| GIR filing deadline | 30 June 2027 (transitional) |

### Jurisdictional Status — FY 2025

| Jurisdiction | ETR | Status | Top-up Tax (€) | Notes |
|--------------|-----|--------|----------------|-------|
| UK | 25.00% | Above minimum | — | Compliant |
| Germany | 23.00% | Safe Harbour | — | Routine Profits test passed |
| Singapore | 9.81% | Below minimum | 529,408 | IIR applies; QDMTT from 2025 |
| Ireland | 11.80% | QDMTT | 435,040 | Qualified QDMTT collected |
| Luxembourg | 25.00% | De Minimis | — | Below €10M/€1M thresholds |
| USA | 15.49% | Safe Harbour | — | Simplified ETR test passed |
| Cayman | 1.00% | Below minimum | 278,110 | IIR applies; no QDMTT |

### Corporate Structure

```
Stratos Holdings plc (UK) — UPE / DFE
        │
        ├── 100% — SG Germany GmbH (Germany)
        │
        ├── 100% — SG Singapore Pte Ltd (Singapore)
        │
        ├── 100% — SG Ireland Ltd (Ireland)
        │
        ├── 100% — SG Luxembourg S.à r.l. (Luxembourg)
        │
        └── 100% — TechStart Inc. (Delaware, USA) [Acquired 1 July 2025]
                    │
                    ├── 100% — TechStart UK Ltd (UK)
                    │
                    ├── 100% — TechStart GmbH (Germany)
                    │
                    ├── 55% — TechStart JV Pte Ltd (Singapore) — JV
                    │
                    ├── 80% — TechStart IP LLC (Delaware) — Flow-through
                    │
                    └── 100% — TechStart Ventures Fund (Cayman)
```

### Key Stakeholders

| Role | Name | Responsibilities |
|------|------|------------------|
| Group CFO | Margaret Chen | Board reporting, financial statement impact, resource allocation |
| Group Tax Director | James Wilson | Technical compliance, risk mitigation, process efficiency |
| Head of Tax Technology | Priya Sharma | System updates, data quality, automation |
| UK Tax Manager | David Roberts | UK entity compliance, HMRC liaison |
| US Tax Manager | Sarah Mitchell | US entity compliance, IRS matters |
| External Auditor Partner | Michael Thompson (Ernst & Co.) | Audit trail, documentation, controls |

---

## Data Package: Administrative Guidance 6 (AG6)

The OECD/G20 Inclusive Framework on BEPS released Administrative Guidance on the GloBE Model Rules in December 2025. The following extracts are relevant to Stratos's compliance position.

### AG6 Extract 1: Partial-Year Acquisitions and QDMTT Safe Harbour

> **AG6 Paragraph 12.1 — Application of QDMTT Safe Harbour to Acquired Entities**
>
> Where a Constituent Entity joins an MNE Group partway through a Fiscal Year due to an acquisition, the QDMTT Safe Harbour may be applied on a proportionate basis for the partial period during which the entity was a member of the Group.
>
> **AG6 Paragraph 12.2 — Proportionate Period Calculation**
>
> The proportionate period shall be calculated as the number of days from the acquisition date to the Fiscal Year end, divided by 365 (or 366 for a leap year). This fraction applies to both the revenue and profit thresholds for De Minimis Test purposes.
>
> **AG6 Paragraph 12.3 — Data Requirements**
>
> For partial-year entities, the acquiring MNE Group shall use the acquired entity's financial data from the acquisition date. Where the acquired entity has a different fiscal year-end, adjustments shall be made to align reporting periods. The acquiring group is not required to include pre-acquisition data in its GloBE calculations but must document the cut-off date and any allocation methodology applied.
>
> **AG6 Paragraph 12.4 — Election to Apply Full-Year Treatment**
>
> An MNE Group may elect to apply full-year treatment to acquired entities where:
> (a) the acquisition occurs within the first quarter of the Fiscal Year; or
> (b) the acquired entity's ETR for the pre-acquisition period was at or above 15%.
>
> This election is binding for all acquired entities in the same transaction.

**Stratos-Specific Data for AG6 Extract 1:**

TechStart Inc. was acquired on **1 July 2025** (184 days remaining in calendar year).

| TechStart Entity | Full Year GloBE Income (€) | Partial Year (184/365) (€) | Full Year Covered Taxes (€) | Partial Year (€) |
|------------------|---------------------------|---------------------------|----------------------------|------------------|
| TechStart Inc. (USA) | 18,148,000 | 9,151,408 | 3,811,000 | 1,921,443 |
| TechStart UK Ltd | 6,050,000 | 3,050,356 | 1,512,400 | 762,414 |
| TechStart GmbH | 12,098,000 | 6,100,222 | 2,782,600 | 1,402,872 |
| TechStart Ventures Fund (Cayman) | 4,032,000 | 2,032,942 | 40,400 | 20,370 |
| TechStart IP LLC (80% share) | 6,452,800 | 3,253,311 | 0 | 0 |

TechStart pre-acquisition ETR (1 Jan – 30 June 2025): **21.0%** (USA consolidated)

---

### AG6 Extract 2: Marketable Transferable Tax Credits — Clarifications

> **AG6 Paragraph 15.1 — Scope of Marketable Transferable Tax Credit Definition**
>
> A tax credit qualifies as a Marketable Transferable Tax Credit (MTTC) under Article 10.1.1 if it meets both marketability and transferability requirements at the time of recognition. The credit need not have been actually transferred; the potential for transfer to an unrelated party at fair market value is sufficient.
>
> **AG6 Paragraph 15.2 — US Inflation Reduction Act Credits**
>
> Tax credits arising under Sections 45, 45Y, 48, and 48E of the US Internal Revenue Code (as amended by the Inflation Reduction Act of 2022) meet the definition of Marketable Transferable Tax Credits where the taxpayer has made a valid election under Section 6418 to transfer the credit.
>
> **AG6 Paragraph 15.3 — Treatment Where Election Not Made**
>
> Where a taxpayer holds a credit eligible for transfer under Section 6418 but has not made the transfer election by the GIR filing date, the credit shall be treated as follows:
> (a) If the transfer election deadline has passed without election: the credit is treated as a Non-Qualifying Refundable Tax Credit and added to GloBE Income per Article 3.2.4;
> (b) If the transfer election deadline has not yet passed: the taxpayer may apply MTTC treatment prospectively upon making the election, with a corresponding adjustment in the year of election.
>
> **AG6 Paragraph 15.4 — Quantification of MTTC**
>
> The MTTC is included in Covered Taxes at its face value (gross credit amount), not at any discounted transfer value. Any discount accepted on actual transfer is disregarded for GloBE purposes.

**Stratos-Specific Data for AG6 Extract 2:**

TechStart Inc. holds the following US tax credits:

| Credit Type | IRC Section | Amount (USD) | Amount (€) | Section 6418 Election Status |
|-------------|-------------|--------------|------------|------------------------------|
| Clean Energy Production Credit | Section 45 | $850,000 | €779,817 | Election made 15 Nov 2025 |
| Investment Tax Credit (Solar) | Section 48 | $320,000 | €293,578 | No election made |
| R&D Credit | Section 41 | $425,000 | €389,908 | Not transferable under 6418 |

Exchange rate: 1 USD = 0.9174 EUR

Current USA jurisdictional ETR calculation (FY 2025):
- Combined GloBE Income: €12,300,400
- Combined Covered Taxes: €1,905,500
- Current ETR: **15.49%**

The Section 48 credit ($320,000 / €293,578) was **not included** in the FY 2025 calculation as it was unclear whether MTTC treatment applied.

---

### AG6 Extract 3: Transitional Safe Harbour Extensions

> **AG6 Paragraph 18.1 — Extended Application Period**
>
> The Transitional CbCR Safe Harbour under Article 9.1 shall remain available for Fiscal Years beginning on or before 31 December 2028 (previously 31 December 2026). This extension applies to all three tests (De Minimis, Simplified ETR, and Routine Profits).
>
> **AG6 Paragraph 18.2 — Simplified ETR Threshold Adjustments**
>
> The Simplified ETR test thresholds are adjusted as follows:
>
> | Fiscal Year Beginning | Threshold Rate |
> |----------------------|----------------|
> | 2024 | 15% |
> | 2025 | 16% |
> | 2026 | 17% |
> | 2027 | 17% |
> | 2028 | 17% |
>
> **AG6 Paragraph 18.3 — Documentation Requirements**
>
> MNE Groups applying the Transitional Safe Harbour for extended years (2027-2028) must maintain documentation demonstrating:
> (a) Consistency of CbCR data preparation methodology across all application years;
> (b) Reconciliation between CbCR data and Qualified Financial Statements; and
> (c) No material restatements affecting prior-year safe harbour determinations.

**Stratos-Specific Data for AG6 Extract 3:**

Stratos's Safe Harbour status by jurisdiction:

| Jurisdiction | FY 2025 Status | Test Passed | CbCR ETR | Margin to 16% Threshold |
|--------------|----------------|-------------|----------|------------------------|
| Germany | Qualified | Routine Profits | 23.28% | +7.28pp |
| Luxembourg | Qualified | De Minimis | N/A | N/A |
| USA | Qualified | Simplified ETR | 21.11% | +5.11pp |
| UK | Above 15% | N/A | 24.58% | N/A |
| Ireland | QDMTT applies | N/A | 11.88% | N/A |
| Singapore | Below 15% | Failed all | 9.52% | -6.48pp |
| Cayman | Below 15% | Failed all | 1.00% | -15.00pp |

Projected FY 2026 CbCR ETRs (based on current forecasts):

| Jurisdiction | Projected CbCR ETR | 17% Threshold (FY 2026) | Status |
|--------------|-------------------|------------------------|--------|
| Germany | 22.5% | Pass | Safe Harbour likely |
| USA | 19.8% | Pass | Safe Harbour likely |
| Luxembourg | De Minimis | N/A | Safe Harbour likely |

---

### AG6 Extract 4: STTR Interaction with Domestic Law

> **AG6 Paragraph 22.1 — Domestic Implementation of STTR**
>
> Source jurisdictions implementing the STTR through domestic legislation (rather than treaty modification) shall ensure that:
> (a) The STTR applies only to Covered Income as defined in the STTR Model Provision;
> (b) The 9% nominal tax rate threshold is applied at the payee jurisdiction level; and
> (c) Credits are available for any underlying tax imposed by the residence jurisdiction on the same income.
>
> **AG6 Paragraph 22.2 — Interaction with Existing Treaties**
>
> Where an existing treaty contains a withholding tax rate below the STTR rate that would otherwise apply, the STTR takes precedence only if:
> (a) Both contracting states have signed the STTR MLI; or
> (b) The treaty has been bilaterally modified to incorporate STTR provisions.
>
> **AG6 Paragraph 22.3 — Timing of STTR Application**
>
> The STTR applies to payments made on or after the later of:
> (a) The date both jurisdictions have ratified the STTR MLI or bilateral modification; and
> (b) The first day of the calendar year following the deposit of ratification instruments.

**Stratos-Specific Data for AG6 Extract 4:**

Stratos has the following cross-border payments potentially subject to STTR:

| Payment Type | From Entity | To Entity | Annual Amount (€) | Current WHT Rate | Payee Jurisdiction Tax Rate |
|--------------|-------------|-----------|-------------------|------------------|---------------------------|
| Royalties | SG Ireland Ltd | SG Luxembourg S.à r.l. | 2,400,000 | 0% (EU directive) | 25% |
| Interest | SG Singapore Pte Ltd | Stratos Holdings plc (UK) | 1,800,000 | 0% (treaty) | 25% |
| Management fees | TechStart Inc. (USA) | SG Singapore Pte Ltd | 950,000 | 0% (no WHT on services) | 9.81% |
| Royalties | TechStart Inc. (USA) | TechStart IP LLC | 3,200,000 | 0% (domestic) | 0% (flow-through) |

STTR MLI status (as of January 2026):

| Jurisdiction | STTR MLI Signed | Ratified | Effective Date |
|--------------|-----------------|----------|----------------|
| UK | Yes | Yes | 1 January 2026 |
| Ireland | Yes | Pending | Expected 2027 |
| Singapore | Yes | Pending | Expected 2027 |
| Germany | Yes | Yes | 1 January 2026 |
| Luxembourg | Yes | Pending | Expected 2027 |
| USA | No | N/A | N/A |
| Cayman | No | N/A | N/A |

---

## Data Package: Existing Governance Documents

### Stratos Tax Risk Management Policy — Current Version (Excerpts)

**Document:** Tax Risk Management Policy
**Version:** 3.2
**Effective Date:** 1 March 2023
**Last Reviewed:** 15 December 2024
**Owner:** Group Tax Director
**Approved by:** Audit Committee

---

**Section 1: Purpose and Scope**

1.1 This Policy establishes the framework for managing tax risks across the Stratos Holdings plc group of companies.

1.2 This Policy applies to all entities within the consolidated group and covers all taxes including corporate income tax, VAT/GST, employment taxes, and customs duties.

1.3 This Policy does not currently address specific requirements arising from the OECD Pillar Two Global Anti-Base Erosion (GloBE) rules.

---

**Section 3: Governance Structure**

3.1 **Board Oversight**: The Audit Committee has oversight responsibility for tax risk management. The Committee receives an annual Tax Risk Report and is notified of any material tax disputes or assessments exceeding €500,000.

3.2 **Management Responsibility**: The Group Tax Director is responsible for day-to-day management of tax risk and reports to the Group CFO.

3.3 **Local Compliance**: Local finance directors are responsible for ensuring compliance with local tax filing and payment obligations in their respective jurisdictions.

---

**Section 5: Risk Appetite**

5.1 Stratos has a **low risk appetite** for tax compliance matters. The Group aims for full compliance with the letter and spirit of tax legislation in all jurisdictions.

5.2 Tax planning structures must have clear business substance and commercial rationale.

5.3 Aggressive tax positions that rely solely on technical interpretation without supporting business purpose are not permitted.

---

**Section 7: Monitoring and Reporting**

7.1 The Group Tax function monitors legislative developments and provides quarterly updates to the Group CFO.

7.2 Material tax risks (potential exposure exceeding €250,000) must be escalated to the Group Tax Director within 5 business days of identification.

7.3 The annual Tax Risk Report to the Audit Committee includes:
- Summary of compliance status across all jurisdictions
- Material tax disputes and provisions
- Legislative developments affecting the Group
- Tax governance effectiveness review

---

**Section 9: External Advisors**

9.1 External tax advisors are engaged for:
- Complex cross-border transactions
- Tax authority disputes exceeding €500,000
- Legislative interpretation where internal expertise is insufficient

9.2 The Group Tax Director maintains a panel of approved advisors for each major jurisdiction.

---

### Stratos RACI Matrix — Current Version (Tax Processes)

| Process | Group Tax | Local Finance | CFO | Audit Committee | External Advisor |
|---------|-----------|---------------|-----|-----------------|------------------|
| Annual tax provision | A | R | I | I | C |
| Tax return filing | A | R | I | I | C |
| Transfer pricing documentation | R | C | I | I | C |
| Tax audit response | R | C | I | I | R |
| Tax risk reporting | R | I | A | I | C |
| Legislative monitoring | R | I | I | I | C |

---

### Stratos Organisation Chart — Tax Function

```
Margaret Chen (Group CFO)
        │
        └── James Wilson (Group Tax Director)
                    │
                    ├── David Roberts (UK Tax Manager)
                    │       └── 2 Tax Analysts
                    │
                    ├── Sarah Mitchell (US Tax Manager) [Since TechStart acquisition]
                    │       └── 1 Tax Analyst
                    │
                    ├── Regional Tax Managers (Germany, Ireland, Singapore)
                    │       └── Report to Local Finance Directors with dotted line to Group Tax
                    │
                    └── Priya Sharma (Head of Tax Technology)
                            └── 2 System Analysts
```

**Current Pillar Two Responsibilities (Informal):**

| Activity | Current Owner | Notes |
|----------|---------------|-------|
| GloBE calculations | David Roberts + External advisor | Manual spreadsheet process |
| Data gathering | Local finance teams | Ad hoc requests |
| GIR preparation | David Roberts | First filing in progress |
| Regulatory monitoring | James Wilson | Personal RSS feeds |
| Safe Harbour assessment | External advisor | Outsourced for FY 2025 |
| QDMTT coordination | James Wilson + Ireland team | Direct liaison |

---

## Task 1: Administrative Guidance Impact Memo

### Scenario

James Wilson (Group Tax Director) has received notification of AG6 release. He has asked you to prepare a technical memo analysing the guidance and its impact on Stratos's compliance position.

### Your Task

Using the AG6 extracts provided, prepare a technical memo addressed to James Wilson analysing each relevant guidance item and recommending actions.

### Deliverable

Prepare a **Technical Memo** (2-3 pages) containing:

#### 1. Executive Summary (Half page)

Summarise:
- Number of AG6 items affecting Stratos
- Highest priority item requiring immediate action
- Overall timeline for implementing changes
- Estimated quantitative impact (if any)

#### 2. Detailed Analysis (1.5-2 pages)

For **each** of the four AG6 extracts, complete the following analysis:

**AG6 Extract 1 — Partial-Year Acquisitions:**

| Element | Your Analysis |
|---------|---------------|
| Relevant Article | [Cite GloBE Model Rules article] |
| Key Guidance Points | [List 2-3 key provisions from AG6 paragraphs 12.1-12.4] |
| Impact on Stratos | [Specific impact on TechStart acquisition treatment] |
| Affected Entities | [List specific entities] |
| Calculation Impact | [Quantify any change to FY 2025 numbers] |
| Election Available? | [Yes/No — if yes, recommendation] |
| Action Required | [Specific steps] |
| Priority | [High/Medium/Low with rationale] |
| Deadline | [Specific date] |

**AG6 Extract 2 — MTTC Clarifications:**

Complete same analysis table for US tax credit treatment.

**AG6 Extract 3 — Safe Harbour Extensions:**

Complete same analysis table for planning implications.

**AG6 Extract 4 — STTR Interaction:**

Complete same analysis table for cross-border payment exposure.

#### 3. Impact Summary

| AG6 Item | Affected Jurisdictions | FY 2025 Quantitative Impact (€) | FY 2026+ Impact | Priority |
|----------|----------------------|--------------------------------|-----------------|----------|
| Partial-year acquisitions | [List] | [Calculate] | [Describe] | [H/M/L] |
| MTTC clarifications | [List] | [Calculate] | [Describe] | [H/M/L] |
| Safe Harbour extensions | [List] | [Describe] | [Describe] | [H/M/L] |
| STTR interaction | [List] | [Calculate] | [Describe] | [H/M/L] |

#### 4. Recommended Actions

List specific actions in three timeframes:
- **Immediate** (within 30 days)
- **Short-term** (within 90 days)
- **Ongoing** (process changes)

For each action, specify the responsible person (use names from stakeholder list).

### Assessment Criteria

- [ ] All four AG6 extracts analysed
- [ ] Correct Article references cited
- [ ] Quantitative impacts calculated where data permits
- [ ] Specific action items with named owners
- [ ] Professional memo format

---

## Task 2: Tax Governance Policy Update

### Scenario

Following the first year of Pillar Two compliance, Margaret Chen (Group CFO) has requested an update to Stratos's Tax Risk Management Policy. The current policy (Version 3.2, excerpts provided above) does not address Pillar Two requirements.

### Your Task

Draft specific additions to the Tax Risk Management Policy and update the RACI matrix to incorporate Pillar Two processes.

### Deliverable

#### Section A: Policy Amendments (1-2 pages)

Draft the following **new sections** to be inserted into the existing policy:

**New Section 4: Pillar Two Compliance Governance**

Draft policy text (using "shall" for mandatory requirements) covering:

4.1 **Scope of Pillar Two Compliance**
- Definition of in-scope entities
- Reference to €750 million revenue threshold
- Annual confirmation process

4.2 **Compliance Ownership**
- Designation of Pillar Two Compliance Owner
- Reporting line (to whom?)
- Delegation authorities

4.3 **Calculation Methodology**
- Requirement for documented calculation methodology
- Approval process for methodology changes
- Version control requirements

4.4 **Data Governance**
- Data collection responsibilities
- Quality assurance requirements
- Retention period (minimum [specify] years)

4.5 **Materiality Thresholds**

Complete the following table with appropriate thresholds for Stratos:

| Matter | Threshold | Escalation To | Timeline |
|--------|-----------|---------------|----------|
| Calculation error affecting Top-up Tax | €[amount] | [Role] | [Days] |
| New jurisdiction coming into scope | Any | [Role] | [Days] |
| Change in Safe Harbour eligibility | Any | [Role] | [Days] |
| QDMTT qualification status change | Any | [Role] | [Days] |
| AG impact assessment (material) | €[amount] | [Role] | [Days] |

4.6 **Review Cycle**
- Frequency of policy review
- Trigger events requiring immediate review
- Approval requirements for updates

**New Section 4A: Three Lines of Defence — Pillar Two**

Map Pillar Two activities to the three lines model. For **each activity listed**, specify:
- Responsible role at Stratos (use actual names/titles from org chart)
- Key deliverables
- Escalation trigger

| Activity | Line | Responsible Role | Key Deliverable | Escalation Trigger |
|----------|------|------------------|-----------------|-------------------|
| Entity-level data collection | First | [Complete] | [Complete] | [Complete] |
| Jurisdictional GloBE calculation | First | [Complete] | [Complete] | [Complete] |
| GIR preparation and filing | First | [Complete] | [Complete] | [Complete] |
| Calculation methodology validation | Second | [Complete] | [Complete] | [Complete] |
| Safe Harbour assessment review | Second | [Complete] | [Complete] | [Complete] |
| Regulatory change monitoring | Second | [Complete] | [Complete] | [Complete] |
| Cross-jurisdictional consistency | Second | [Complete] | [Complete] | [Complete] |
| Annual process audit | Third | [Complete] | [Complete] | [Complete] |
| External audit liaison | Third | [Complete] | [Complete] | [Complete] |
| Board/Audit Committee reporting | Third | [Complete] | [Complete] | [Complete] |

**New Section 8A: Regulatory Change Management — Pillar Two**

Draft policy text covering:

8A.1 **Monitoring Responsibilities**
- Who monitors OECD releases?
- Frequency of monitoring
- Sources to be monitored

8A.2 **Impact Assessment Protocol**
- Timeline for initial assessment after AG release
- Documentation requirements
- Approval of assessment conclusions

8A.3 **Implementation Process**
- Steps from identification to implementation
- Testing requirements
- Sign-off process

#### Section B: Updated RACI Matrix (1 page)

Create an **updated RACI matrix** adding Pillar Two processes to the existing matrix. Include all existing processes **plus** the following new processes:

| Process | Group Tax | Local Finance | Tax Technology | External Advisor | CFO | Audit Committee |
|---------|-----------|---------------|----------------|------------------|-----|-----------------|
| *Existing processes from current matrix...* | | | | | | |
| GloBE data collection | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Jurisdictional ETR calculation | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Top-up Tax computation | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Safe Harbour assessment | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| QDMTT calculation & payment | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| GIR preparation | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| GIR filing | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| AG impact assessment | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Pillar Two Board reporting | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Pillar Two external audit support | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |

**RACI Definitions:**
- **R** = Responsible (does the work)
- **A** = Accountable (final decision authority — only one per row)
- **C** = Consulted (provides input before decision)
- **I** = Informed (notified after decision)

#### Section C: Stakeholder Communication Plan (Half page)

Draft a communication plan for rolling out the policy updates:

| Stakeholder | Communication Method | Key Messages | Owner | Timing |
|-------------|---------------------|--------------|-------|--------|
| Audit Committee | [Specify] | [2-3 key points] | [Name] | [Date/timing] |
| Local Finance Directors | [Specify] | [2-3 key points] | [Name] | [Date/timing] |
| Tax Technology team | [Specify] | [2-3 key points] | [Name] | [Date/timing] |
| External Auditors | [Specify] | [2-3 key points] | [Name] | [Date/timing] |
| Regional Tax Managers | [Specify] | [2-3 key points] | [Name] | [Date/timing] |

### Assessment Criteria

- [ ] Policy language uses appropriate mandatory terms ("shall")
- [ ] Materiality thresholds are reasonable for Stratos's scale
- [ ] Three Lines of Defence correctly mapped
- [ ] RACI has exactly one "A" per process
- [ ] Communication plan is actionable with specific owners

---

## Task 3: Audit Committee Board Paper

### Scenario

The Stratos Audit Committee meets quarterly. Margaret Chen has asked you to prepare the Pillar Two section of the Q1 2026 Board paper, covering FY 2025 compliance outcomes, AG6 implications, and recommended governance enhancements.

### Your Task

Prepare a Board-level executive summary suitable for non-tax specialist directors.

### Deliverable

#### Board Paper: Pillar Two Compliance Update — Q1 2026

**Format:** One-page executive summary + one-page data appendix (maximum 600 words for main text)

**Required Sections:**

**1. Compliance Status Summary**

Open with a clear status statement:
- FY 2025 compliance: [Confirmed/Pending/Issues]
- Total Pillar Two liability: €[amount]
- Filing status: [On track/At risk/Complete]

**2. FY 2025 Outcomes**

| Metric | Result |
|--------|--------|
| Total Top-up Tax | €[Use data from background] |
| — IIR (UK) | €[amount] |
| — QDMTT (Ireland) | €[amount] |
| Jurisdictions assessed | [number] |
| Safe Harbour applied | [number] jurisdictions |
| Next filing deadline | [date] |

**3. Significant Matters** (3-4 bullets)

Highlight for the Committee:
- TechStart acquisition integration (what was the compliance impact?)
- Elections exercised (any significant choices made?)
- Near-miss situations (any jurisdictions close to thresholds?)
- First-year challenges overcome

**4. Regulatory Update: AG6**

Summarise for non-specialists:
- When was AG6 released?
- How many items affect Stratos?
- What is the most significant impact?
- What action is management taking?

**5. Governance Enhancements**

Reference Task 2 deliverables:
- Policy updates proposed
- RACI clarifications
- Request for Committee endorsement

**6. Forward Look**

| Item | FY 2026 Outlook |
|------|-----------------|
| Expected liability trend | [Increase/Decrease/Stable] — [reason] |
| Safe Harbour availability | [Status for FY 2026] |
| Key jurisdictional changes | [Singapore QDMTT, etc.] |
| Resource requirements | [Any changes needed?] |

**7. Recommendations to the Committee**

List 2-3 specific recommendations requiring Committee action:
1. [First recommendation]
2. [Second recommendation]
3. [Third recommendation — if applicable]

#### Data Appendix

Attach a one-page supporting appendix with:

**Jurisdictional Detail — FY 2025**

| Jurisdiction | Entities | GloBE Income (€) | ETR | Status | Top-up Tax (€) |
|--------------|----------|------------------|-----|--------|----------------|
| UK | [number] | [amount] | [%] | [status] | [amount] |
| Germany | [number] | [amount] | [%] | [status] | [amount] |
| Singapore | [number] | [amount] | [%] | [status] | [amount] |
| Ireland | [number] | [amount] | [%] | [status] | [amount] |
| Luxembourg | [number] | [amount] | [%] | [status] | [amount] |
| USA | [number] | [amount] | [%] | [status] | [amount] |
| Cayman | [number] | [amount] | [%] | [status] | [amount] |
| **Total** | | | | | **€[total]** |

**Compliance Timeline**

| Milestone | Date | Status |
|-----------|------|--------|
| FY 2025 year-end | 31 December 2025 | Complete |
| GIR data finalisation | [Date] | [Status] |
| External advisor review | [Date] | [Status] |
| GIR filing (transitional deadline) | 30 June 2027 | Planned |

### Assessment Criteria

- [ ] Language appropriate for non-tax specialists
- [ ] Financial impact clearly quantified
- [ ] AG6 implications summarised accessibly
- [ ] Recommendations are specific and actionable
- [ ] Appendix provides supporting detail without overwhelming

---

## Model Answer Guidance

### Task 1: AG Impact Memo

**Key Calculations:**

*AG6 Extract 1 — Partial-Year Acquisitions:*
- TechStart acquisition date: 1 July 2025 = 184/365 = **50.4%** of year
- Stratos may elect full-year treatment because pre-acquisition ETR was 21% (above 15%)
- If partial-year treatment applies, TechStart entities contribute proportionately to jurisdictional totals
- Consider whether full-year vs. partial-year treatment is more advantageous

*AG6 Extract 2 — MTTC Clarifications:*
- Section 45 credit ($850,000 / €779,817): Election made — qualifies as MTTC, included in Covered Taxes at face value
- Section 48 credit ($320,000 / €293,578): No election — currently excluded
- Impact: If Section 48 credit is treated as MTTC (face value), USA Covered Taxes increase by €293,578
- Revised USA ETR: (€1,905,500 + €293,578) / €12,300,400 = **17.88%** (vs. current 15.49%)
- This improves USA's margin above 15% minimum

*AG6 Extract 3 — Safe Harbour Extensions:*
- Extension to 2028 provides planning certainty
- Germany, Luxembourg, and USA likely to continue qualifying through 2028
- FY 2026 threshold increases to 17% — all three still comfortably above
- Process impact: Must document CbCR consistency for extended years

*AG6 Extract 4 — STTR:*
- UK-Germany effective 1 January 2026 — but Stratos has no relevant payments between these jurisdictions
- Singapore payments to UK (€1,800,000 interest) — STTR not yet effective (Singapore pending ratification)
- TechStart IP LLC royalties (€3,200,000) — USA not signatory, no STTR applies
- **Current exposure: Nil**, but monitor for Singapore ratification

**Priority Assessment:**
- **High:** MTTC clarification (affects FY 2025 calculation, filing deadline approaching)
- **Medium:** Partial-year acquisition (confirm treatment before filing)
- **Low:** Safe Harbour extension (positive news, process update only)
- **Low:** STTR (no current exposure)

### Task 2: Governance Policy

**Materiality Threshold Guidance:**

| Matter | Suggested Threshold | Rationale |
|--------|-------------------|-----------|
| Calculation error | €50,000 | ~4% of total liability |
| New jurisdiction | Any | Compliance impact |
| Safe Harbour change | Any | Process change required |
| QDMTT status change | Any | Collection mechanism change |
| AG material impact | €100,000 | ~8% of total liability |

**RACI Solution:**

| Process | Group Tax | Local Finance | Tax Technology | External Advisor | CFO | Audit Committee |
|---------|-----------|---------------|----------------|------------------|-----|-----------------|
| GloBE data collection | A | R | C | — | I | — |
| Jurisdictional ETR calculation | A | R | R | C | I | — |
| Top-up Tax computation | A | C | R | C | I | — |
| Safe Harbour assessment | A | C | I | R | I | — |
| QDMTT calculation & payment | A | R | C | C | I | I |
| GIR preparation | A | C | R | C | I | — |
| GIR filing | A | — | R | C | I | I |
| AG impact assessment | R | I | C | C | A | I |
| Pillar Two Board reporting | R | — | — | C | A | I |
| Pillar Two external audit support | R | R | C | — | I | I |

### Task 3: Board Paper

**Key Points for Non-Specialists:**

- Lead with compliance status: "Stratos has successfully completed its first Pillar Two compliance cycle"
- Explain Top-up Tax simply: "Additional tax to bring low-taxed profits up to 15% minimum"
- Quantify clearly: Total liability of €1.2M represents X% of group tax charge
- AG6 summary: "New OECD guidance issued in December 2025 affects our calculations. Most significant item [X] will be addressed before filing"
- Recommendations should be specific: "Approve updated Tax Risk Management Policy" not "Consider governance improvements"

---

## Reflection Questions

After completing this case study, consider:

1. **Prioritisation:** How did you determine which AG6 items required immediate action versus monitoring?

2. **Quantification:** Where data was incomplete, how did you estimate impacts for the memo?

3. **Governance Design:** What factors influenced your materiality thresholds?

4. **Board Communication:** How did you balance technical accuracy with accessibility?

5. **Continuous Improvement:** What would you recommend Stratos implement to streamline AG monitoring for future releases?

---

## Course Conclusion

Congratulations on completing the ADIT Pillar Two Professional Practice Course.

### Skills Developed

| Part | Core Skills |
|------|-------------|
| **Part 1** | Scope determination, entity classification, exclusion application |
| **Part 2** | IIR/UTPR mechanics, allocation calculations, ordering rules |
| **Part 3** | GloBE Income adjustments, timing differences, PE allocations |
| **Part 4** | Covered Tax identification, DTA/DTL treatment, push-down mechanics |
| **Part 5** | ETR calculation, SBIE application, Top-up Tax computation |
| **Part 6** | Safe harbour assessment, QDMTT interaction, election strategies |
| **Part 7** | GIR preparation, filing requirements, compliance processes |
| **Part 8** | STTR awareness, regulatory monitoring, governance frameworks |

### The Stratos Journey

Throughout this course, you followed Stratos Holdings plc from initial scope assessment through first-year compliance and ongoing governance:

```
Part 1: Scope          Part 2: Charging       Part 3: Income
€1.2B revenue    →     IIR as primary    →    25 adjustments
In-scope confirmed     mechanism              €105.6M GloBE Income

Part 4: Taxes          Part 5: Calculation    Part 6: Elections
€21.0M covered    →    ETR range 1%-25%  →    5/7 Safe Harbour
DTA/DTL treated        SBIE applied           QDMTT coordination

Part 7: Filing         Part 8: Ongoing
€1,242,558 total  →    AG monitoring
GIR prepared           Governance framework
```

### Continuing Professional Development

Pillar Two compliance is not a one-time exercise:

1. **Monitor OECD releases** — New AG typically issued 2-3 times per year
2. **Track peer review outcomes** — QDMTT qualification affects safe harbour availability
3. **Follow jurisdictional changes** — National legislation continues to evolve
4. **Engage professional networks** — ADIT, CIOT, and other bodies provide practitioner updates
5. **Apply learning to practice** — Each compliance cycle builds institutional knowledge

---

**End of Course**

For questions or feedback on this course, contact the MojiTax team at admin@mojitax.com.
