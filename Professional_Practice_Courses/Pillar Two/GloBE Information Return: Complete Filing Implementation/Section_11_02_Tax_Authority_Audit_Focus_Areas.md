# Section 11.2: Tax Authority Audit Focus Areas

## Learning Objectives

By the end of this section, you will be able to:
- Anticipate what tax authorities will scrutinise in GIR submissions
- Understand how cross-border data matching will identify inconsistencies
- Prepare reconciliations between GIR, CbCR, and financial statements
- Implement proactive audit defence strategies
- Use the Audit Readiness Checklist to ensure compliance

---

## Introduction

The GloBE Information Return (GIR) is designed to provide tax authorities with the information needed to:
1. **Perform risk assessments** - identifying MNEs requiring detailed examination
2. **Evaluate correctness** - verifying Top-up Tax calculations
3. **Cross-reference data** - matching GIR information against other filings

Tax authorities have established dedicated Pillar Two compliance teams (including HMRC's new Pillar 2 Compliance team) and will leverage the Multilateral Competent Authority Agreement (MCAA) for automatic exchange of GIR data. This section examines what authorities will check and how to prepare.

---

## Part 1: What Tax Authorities Will Check

### 1.1 Primary Verification Areas

Tax authorities will focus their initial review on areas with the highest risk of error or abuse:

**Tier 1: High-Priority Checks (Every GIR)**

| Area | Authority Interest | Risk Indicator |
|------|-------------------|----------------|
| Scope determination | Correct €750M threshold application | Groups near threshold |
| Entity completeness | All CEs identified and included | Mismatched entity counts vs. CbCR |
| ETR calculations | Mathematical accuracy | Low-ETR jurisdictions (<15%) |
| Top-up Tax allocation | Correct IIR/UTPR application | Allocation methodology |
| Safe harbour elections | Valid application of transitional rules | First-time claims |

**Tier 2: Targeted Checks (Risk-Based)**

| Area | Authority Interest | Trigger |
|------|-------------------|---------|
| Excluded entities | Proper Article 1.5 classification | High number of exclusions |
| Ownership percentages | Correct allocation calculations | Complex structures |
| GloBE adjustments | Appropriate application of Article 3.2 | Large adjustment amounts |
| Covered Taxes | Complete and accurate allocation | ETR close to 15% |
| SBIE calculations | Correct carve-out application | Significant SBIE claims |

**Tier 3: Deep-Dive Examination (Audit)**

| Area | Authority Interest | Trigger |
|------|-------------------|---------|
| Intercompany pricing | Arm's length principle alignment | Transfer pricing adjustments |
| Deferred tax positions | DTL recapture compliance | Large DTL balances |
| Election consistency | Five-year election adherence | Election changes |
| Historic positions | Prior year accuracy | Amended filings |

### 1.2 HMRC Compliance Approach (UK)

HMRC has established a specific compliance framework for Multinational Top-up Tax (MTT) and Domestic Top-up Tax (DTT):

**Registration Verification:**
- All groups meeting the €750M threshold must register
- Registration required even if no tax payable
- HMRC may verify UPE nomination during compliance checks

**Filing Compliance:**
- First return: 18 months after accounting period end
- Subsequent returns: 15 months after accounting period end
- GIR or Overseas Return Notification (ORN) required

**Compliance Check Timeline:**

| Phase | HMRC Action | MNE Requirement |
|-------|-------------|-----------------|
| Initial review | Automated validation checks | Respond to queries within 30 days |
| Information request | Formal information notice | Provide supporting documentation |
| Compliance check | Detailed examination | Attend meetings, provide full records |
| Assessment | Issue of assessment if liability found | Pay or appeal within time limits |

**Contact Points:**
- General queries: pillar2mailbox@hmrc.gov.uk
- Consultation feedback: pillar2.consultation@hmrc.gov.uk

### 1.3 Multi-Jurisdiction Authority Coordination

The MCAA enables coordinated compliance activity across jurisdictions:

**Information Exchange Framework:**

```
Filing Jurisdiction (DFE)
        │
        ▼
    Files GIR
        │
        ▼
Competent Authority
        │
        ├──► Exchange to all MCAA signatories
        │    (within 3 months, or 6 months first year)
        │
        ▼
Receiving Jurisdictions
        │
        ├──► Compare to local data
        ├──► Identify discrepancies
        └──► Initiate enquiries if needed
```

**MCAA Signatories (as at September 2025):**

| Jurisdiction | Signature Date |
|--------------|----------------|
| Austria | 6 August 2025 |
| Belgium | 6 August 2025 |
| Denmark | 6 August 2025 |
| France | 6 August 2025 |
| Germany | 30 September 2025 |
| Ireland | 6 August 2025 |
| Italy | 6 August 2025 |
| Japan | 6 August 2025 |
| Korea (Rep.) | 6 August 2025 |
| Liechtenstein | 30 September 2025 |
| Luxembourg | 6 August 2025 |
| Netherlands | 26 August 2025 |
| New Zealand | 6 August 2025 |
| Norway | 30 September 2025 |
| Portugal | 6 August 2025 |
| Slovak Republic | 6 August 2025 |
| Spain | 6 August 2025 |
| United Kingdom | 6 August 2025 |

**Exchange Timeline:**
- Standard: Within 3 months of filing date
- First year (FY2024 returns): Within 6 months (by 31 December 2026)

---

## Part 2: Data Consistency Verification

### 2.1 Internal Consistency Checks

Tax authorities will perform automated validation to ensure internal consistency within the GIR:

**Mathematical Verification:**

| Check | Formula | Error Flag |
|-------|---------|------------|
| ETR calculation | Adjusted Covered Taxes ÷ GloBE Income = ETR | Variance >0.01% |
| Top-up Tax percentage | 15% - ETR = Top-up Tax % | Negative result |
| Jurisdictional Top-up Tax | (Excess Profit × Top-up Tax %) = Top-up Tax | Calculation mismatch |
| SBIE | (Payroll × Rate) + (Assets × Rate) = SBIE | Component errors |
| Excess Profit | GloBE Income - SBIE = Excess Profit | Negative excess profit |
| Group total | Sum of jurisdictional Top-up Tax = Total | Summation error |

**Logical Consistency Checks:**

| Check | Expected Result | Error Flag |
|-------|-----------------|------------|
| Low-tax jurisdiction | ETR <15% → Top-up Tax >0 | No Top-up Tax reported |
| Safe harbour claim | Safe harbour → No Section 2 detail | Detailed data provided |
| QDMTT offset | QDMTT jurisdiction → Offset reported | No offset claimed |
| IIR priority | UPE jurisdiction → IIR collection | UTPR claimed instead |
| Entity ownership | Sum of ownership = 100% | Percentage anomaly |

### 2.2 Cross-GIR Verification

When multiple GIRs are filed for the same MNE Group (e.g., by different DFEs or local CEs), authorities will verify consistency:

**Multi-Filing Scenarios:**

| Scenario | Authority Check |
|----------|-----------------|
| DFE files centrally + local CE files | Same data reported |
| Multiple DFEs in different jurisdictions | No double-counting of Top-up Tax |
| Amended return filed | Changes properly reflected |
| Prior year carryforward | Consistent with previous GIR |

**Reconciliation Points:**

```
Central GIR (DFE)     Local Filing (CE)
       │                     │
       ▼                     ▼
   Section 2             Local Return
   IE Data               IE DTT Data
       │                     │
       └─────────┬───────────┘
                 │
                 ▼
         Must Match:
         • GloBE Income
         • Covered Taxes
         • Top-up Tax
         • QDMTT offset
```

### 2.3 Validation Rules (OECD)

The OECD is developing common validation rules for GIR data quality:

**Pre-Filing Validation:**
- XML schema compliance
- Required field completion
- Data type conformity
- Enumeration value validation

**Post-Filing Validation:**
- Cross-field consistency
- Historical consistency
- Cross-border matching
- CbCR alignment

---

## Part 3: Cross-Border Data Matching

### 3.1 GIR Exchange and Matching Process

Tax authorities receiving GIR data will match it against:
1. **Their own records** - local CE filings, tax returns
2. **Other GIRs** - from same MNE Group
3. **CbCR data** - Country-by-Country Reports
4. **Financial statement data** - published accounts

**Matching Matrix:**

| Data Point | GIR Source | Matching Source | Discrepancy Action |
|------------|------------|-----------------|-------------------|
| Revenue | Section 2 | CbCR Table 1 | Query to taxpayer |
| Profit before tax | Section 2 | CbCR Table 1 | Query to taxpayer |
| Tax paid | Section 2 | CbCR Table 1 | Query to taxpayer |
| Employee count | Section 2 (SBIE) | CbCR Table 1 | SBIE verification |
| Tangible assets | Section 2 (SBIE) | CbCR Table 1 | SBIE verification |
| Entity list | Section 1 | CbCR Table 2 | Entity completeness |

### 3.2 Bilateral Information Requests

Where MCAA exchange reveals discrepancies, authorities may initiate bilateral enquiries:

**Request Protocol:**

| Stage | Authority Action | Timeline |
|-------|------------------|----------|
| 1. Discrepancy identified | Document inconsistency | Immediate |
| 2. Initial review | Assess materiality | 30 days |
| 3. Bilateral contact | Request information from partner authority | 60 days |
| 4. Joint resolution | Coordinate approach | 90 days |
| 5. Taxpayer contact | Issue information request | As needed |

**Common Bilateral Issues:**

| Issue | Example | Resolution Approach |
|-------|---------|---------------------|
| Dual residence | CE reported in two jurisdictions | Tie-breaker rules |
| Ownership disputes | Different percentages reported | Documentary evidence |
| Tax allocation | Same taxes claimed twice | Covered tax attribution |
| QDMTT recognition | Offset claimed but QDMTT not qualified | Status verification |

### 3.3 Automatic Risk Scoring

Tax authorities are implementing automated risk scoring for GIR submissions:

**Risk Factors:**

| Factor | Weight | High-Risk Indicators |
|--------|--------|---------------------|
| ETR proximity | High | ETR between 14.5% and 15.5% |
| Safe harbour claim | Medium | Multiple jurisdictions claimed |
| Ownership complexity | Medium | >100 CEs or >5 ownership tiers |
| Prior amendments | Medium | Multiple amended returns |
| Industry sector | Low | Historically low-tax sectors |
| Geographic footprint | Low | Multiple low-tax jurisdictions |

**Risk Score Calculation:**

```
Risk Score = Σ (Factor Weight × Factor Presence)

Low Risk:     Score < 3
Medium Risk:  Score 3-6
High Risk:    Score > 6

Action:
Low    → Standard processing
Medium → Enhanced review
High   → Compliance check initiated
```

---

## Part 4: Reconciliation to CbCR and Financial Statements

### 4.1 GIR to CbCR Reconciliation

Although the GIR and CbCR serve different purposes, tax authorities will compare key data points:

**Key Differences:**

| Element | CbCR Treatment | GIR Treatment |
|---------|----------------|---------------|
| Revenue | Per local accounts | GloBE basis (after adjustments) |
| Profit | Profit before tax | GloBE Income (after Article 3.2) |
| Taxes | Tax paid AND accrued | Adjusted Covered Taxes |
| Entities | All CEs | CEs (excluding Excluded Entities) |

**Reconciliation Framework:**

| CbCR Data | Expected GIR Relationship | Variance Explanation |
|-----------|--------------------------|---------------------|
| Revenue | GloBE Revenue ≈ CbCR Revenue | Minor adjustments only |
| PBT | GloBE Income = PBT ± adjustments | Document each adjustment |
| Tax accrued | Covered Taxes ≈ Tax accrued | Deferred tax movements |
| Tax paid | May differ from Covered Taxes | Timing differences |
| Employees | SBIE headcount ≈ CbCR employees | Full-time equivalents |
| Assets | SBIE assets ≤ CbCR assets | Eligible tangible only |

**Reconciliation Template:**

| Jurisdiction | CbCR PBT | GIR GloBE Income | Variance | Explanation |
|--------------|----------|------------------|----------|-------------|
| Ireland | €28,400,000 | €42,600,000 | €14,200,000 | Royalty adjustment |
| Germany | €52,000,000 | €51,200,000 | (€800,000) | FX adjustment |
| Singapore | €18,500,000 | €18,500,000 | — | — |

### 4.2 GIR to Financial Statements Reconciliation

GloBE calculations start from Financial Accounting Net Income or Loss (FANIL), creating a direct link to audited financial statements:

**Starting Point Verification:**

```
Consolidated Financial Statements
              │
              ▼
    Group Profit Before Tax
              │
              ├── Less: Excluded Entities
              │
              ├── Less: Intercompany eliminations
              │
              ▼
    Statutory Entity FANIL (per jurisdiction)
              │
              ├── Add: Net tax expense
              │
              ├── Less: Excluded dividends
              │
              ├── Adjust: Per Article 3.2
              │
              ▼
        GloBE Income
```

**Financial Statement Linkage:**

| FS Line Item | GIR Connection | Verification |
|--------------|----------------|--------------|
| Revenue | GloBE Revenue | Trace to consolidation |
| Operating profit | Starting point for GloBE Income | Reconcile adjustments |
| Tax expense | Covered Taxes baseline | Add deferred movements |
| PPE | SBIE tangible assets | Verify eligible assets |
| Employee costs | SBIE payroll | Reconcile eligible costs |
| Provisions | Adjust for uncertainties | Track timing differences |

### 4.3 Transitional CbCR Safe Harbour Reconciliation

Special reconciliation requirements apply when using the Transitional CbCR Safe Harbour:

**Critical Requirement:**
All data used in Transitional CbCR Safe Harbour computations must come from the same Qualified Financial Statements. Making adjustments to data from Qualified Financial Statements disqualifies the jurisdiction from the Safe Harbour.

**Safe Harbour Data Integrity:**

| Element | Requirement | Verification |
|---------|-------------|--------------|
| Revenue | Per CbCR as filed | Match exactly |
| PBT | Per CbCR as filed | Match exactly |
| Tax accrued | Per CbCR as filed | Match exactly |
| Source documents | Same QFS for all | Document source |
| Adjustments | None permitted | Confirm no modifications |

**Reconciliation Documentation:**

```
For each Safe Harbour jurisdiction:

□ CbCR Table 1 extract attached
□ GIR Section 2 references CbCR data
□ No adjustments made to CbCR figures
□ QFS source identified and documented
□ Safe harbour test calculation attached
□ "Once out, always out" status confirmed
```

---

## Part 5: Authority Audit Procedures

### 5.1 Compliance Check Process

**UK HMRC Compliance Check Stages:**

| Stage | Description | Typical Duration |
|-------|-------------|------------------|
| **1. Notification** | HMRC opens compliance check in writing | — |
| **2. Information gathering** | Formal information notices issued | 1-3 months |
| **3. Review and analysis** | HMRC analyses documents and calculations | 2-6 months |
| **4. Meetings** | Discussion of positions and evidence | As needed |
| **5. Resolution** | Agreement reached or assessment issued | Variable |
| **6. Closure** | Closure notice issued | — |

**Time Limits:**

| Situation | Check Window | Reference |
|-----------|--------------|-----------|
| Standard return | 12 months from filing date | Schedule 14 |
| Amended return | 12 months from amendment date | Extended window |
| Careless error | 6 years | Discovery assessment |
| Deliberate error | 20 years | Discovery assessment |

### 5.2 Information Requests

Tax authorities will request supporting documentation:

**Common Document Requests:**

| Category | Documents | Retention Requirement |
|----------|-----------|----------------------|
| Entity structure | Ownership charts, share registers | 10 years |
| Financial data | FANIL calculations, adjustment workpapers | 10 years |
| Tax calculations | ETR workpapers, Covered Tax allocation | 10 years |
| Elections | Election forms, board resolutions | Life + 6 years |
| Safe harbour | CbCR reconciliation, test calculations | 10 years |
| Transfer pricing | Intercompany agreements, benchmarking | 10 years |

**Response Best Practices:**

1. **Respond within deadline** - extensions rarely granted
2. **Provide complete information** - partial responses invite follow-up
3. **Maintain privilege** - mark privileged documents clearly
4. **Document discussions** - keep meeting notes
5. **Coordinate globally** - ensure consistent positions

### 5.3 Multi-Authority Audits

Pillar Two creates new possibilities for coordinated multi-authority examinations:

**Joint Audit Scenarios:**

| Scenario | Authorities Involved | Coordination Mechanism |
|----------|---------------------|----------------------|
| IIR/UTPR allocation | UPE jurisdiction + UTPR jurisdiction | Bilateral exchange |
| QDMTT recognition | QDMTT jurisdiction + IIR jurisdiction | Qualification verification |
| Safe harbour validation | All jurisdictions claiming | MCAA data matching |
| Transfer pricing impact | Multiple affected jurisdictions | MAP or APA |

**Coordination Risks:**

- Inconsistent authority positions
- Double taxation without MAP relief
- Extended audit timelines
- Confidentiality across jurisdictions

---

## Part 6: Proactive Audit Defence Strategies

### 6.1 Documentation Strategy

Prepare audit defence documentation before filing:

**Pre-Filing Documentation Package:**

| Document | Purpose | Preparation Timing |
|----------|---------|-------------------|
| GIR methodology memo | Explain approach to key calculations | With GIR preparation |
| Judgment documentation | Support for estimates and elections | With GIR preparation |
| Reconciliation schedules | Link GIR to CbCR and FS | Before filing |
| Election register | Track all elections made | Ongoing |
| Process documentation | Evidence of controls | Annual update |

### 6.2 Position Papers

For significant positions, prepare technical support memoranda:

**Position Paper Structure:**

```
TECHNICAL POSITION MEMORANDUM

Issue: [Description of position taken]

Facts:
• Relevant factual background
• Amounts involved
• Entities affected

Analysis:
• Relevant GloBE Rules provisions
• Administrative Guidance references
• Supporting technical arguments
• Counter-arguments considered

Conclusion:
• Position taken
• Risk assessment (High/Medium/Low)
• Supporting documentation references

Prepared by: [Name]
Reviewed by: [Name]
Date: [Date]
```

### 6.3 Audit Trail Requirements

Maintain complete audit trails for all GIR data:

**Audit Trail Components:**

| Component | Requirement |
|-----------|-------------|
| Source data | Link to original systems |
| Calculations | Show all formulas and inputs |
| Adjustments | Document reason and authorisation |
| Reviews | Evidence of preparer/reviewer sign-off |
| Approvals | Management approval evidence |
| Filing evidence | Submission confirmation |

**System Requirements:**

```
GIR Data Flow with Audit Trail:

Source Systems          Calculation Engine         GIR Output
     │                        │                        │
     ▼                        ▼                        ▼
  ERP Data ──────────► Adjustment ──────────► GIR XML
     │               Workbooks         │          │
     │                   │             │          │
     ▼                   ▼             ▼          ▼
  Extract Log       Version Control  Reconciliation  Filing Log
     │                   │             │          │
     └───────────────────┴─────────────┴──────────┘
                         │
                         ▼
              AUDIT TRAIL ARCHIVE
              (10-year retention)
```

### 6.4 Authority Relationship Management

**Proactive Engagement:**

| Activity | Benefit | Timing |
|----------|---------|--------|
| Registration confirmation | Avoid late registration penalties | Within 6 months of first period |
| Voluntary disclosure | Penalty mitigation | Upon error discovery |
| Ruling requests | Certainty on positions | Before filing |
| Industry consultations | Early guidance | As available |

**HMRC Pillar 2 Engagement:**

- Registration: Gov.uk online portal
- Queries: pillar2mailbox@hmrc.gov.uk
- Consultation: pillar2.consultation@hmrc.gov.uk

---

## Practical Deliverable: Audit Readiness Checklist

### GIR Audit Readiness Checklist

**Section A: Entity and Scope**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| A.1 €750M threshold calculation documented | □ | ___ | ___ |
| A.2 All CEs identified and listed | □ | ___ | ___ |
| A.3 Excluded entities properly classified | □ | ___ | ___ |
| A.4 Ownership percentages verified | □ | ___ | ___ |
| A.5 CE list reconciled to consolidation | □ | ___ | ___ |
| A.6 CE list reconciled to CbCR Table 2 | □ | ___ | ___ |
| A.7 Changes from prior year documented | □ | ___ | ___ |

**Section B: GloBE Income Calculations**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| B.1 FANIL traced to audited financial statements | □ | ___ | ___ |
| B.2 All Article 3.2 adjustments documented | □ | ___ | ___ |
| B.3 Excluded dividends identified and supported | □ | ___ | ___ |
| B.4 Intercompany eliminations reconciled | □ | ___ | ___ |
| B.5 Policy elections documented and consistent | □ | ___ | ___ |
| B.6 GloBE Income reconciled to CbCR PBT | □ | ___ | ___ |
| B.7 Variances explained and documented | □ | ___ | ___ |

**Section C: Covered Taxes**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| C.1 Current taxes extracted from tax provision | □ | ___ | ___ |
| C.2 Deferred tax movements calculated | □ | ___ | ___ |
| C.3 WHT allocated to correct jurisdictions | □ | ___ | ___ |
| C.4 CFC taxes pushed down appropriately | □ | ___ | ___ |
| C.5 Uncertain tax positions adjusted | □ | ___ | ___ |
| C.6 Covered Taxes reconciled to CbCR tax | □ | ___ | ___ |
| C.7 DTL recapture rules applied | □ | ___ | ___ |

**Section D: ETR and Top-up Tax**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| D.1 ETR calculations mathematically verified | □ | ___ | ___ |
| D.2 SBIE calculations documented | □ | ___ | ___ |
| D.3 Transition rates correctly applied | □ | ___ | ___ |
| D.4 Excess Profit correctly calculated | □ | ___ | ___ |
| D.5 Top-up Tax % correctly calculated | □ | ___ | ___ |
| D.6 Top-up Tax allocation documented | □ | ___ | ___ |
| D.7 IIR/UTPR priority correctly applied | □ | ___ | ___ |

**Section E: Safe Harbours**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| E.1 CbCR data matches filed CbCR exactly | □ | ___ | ___ |
| E.2 No adjustments made to CbCR data | □ | ___ | ___ |
| E.3 QFS source documented | □ | ___ | ___ |
| E.4 Safe harbour test calculations verified | □ | ___ | ___ |
| E.5 Transition rate correct for fiscal year | □ | ___ | ___ |
| E.6 "Once out, always out" status confirmed | □ | ___ | ___ |
| E.7 QDMTT safe harbour qualification verified | □ | ___ | ___ |

**Section F: Documentation and Controls**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| F.1 Audit file structured and indexed | □ | ___ | ___ |
| F.2 All source documents retained | □ | ___ | ___ |
| F.3 Calculation workpapers complete | □ | ___ | ___ |
| F.4 Election evidence filed | □ | ___ | ___ |
| F.5 Sign-offs obtained (preparer/reviewer/approver) | □ | ___ | ___ |
| F.6 Position papers for significant judgments | □ | ___ | ___ |
| F.7 Process documentation current | □ | ___ | ___ |

**Section G: Filing and Coordination**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| G.1 XML validated against current schema | □ | ___ | ___ |
| G.2 Filing deadline verified | □ | ___ | ___ |
| G.3 DFE election in place | □ | ___ | ___ |
| G.4 Submission confirmation retained | □ | ___ | ___ |
| G.5 GIR reconciled to tax provision | □ | ___ | ___ |
| G.6 GIR reconciled to local returns | □ | ___ | ___ |
| G.7 GIR reconciled to CbCR | □ | ___ | ___ |

**Section H: Cross-Border Coordination**

| Item | Verified | Evidence Location | Reviewer |
|------|----------|-------------------|----------|
| H.1 MCAA exchange jurisdictions identified | □ | ___ | ___ |
| H.2 Consistent positions across jurisdictions | □ | ___ | ___ |
| H.3 QDMTT offset calculations coordinated | □ | ___ | ___ |
| H.4 Multi-jurisdiction queries anticipated | □ | ___ | ___ |
| H.5 Transfer pricing alignment verified | □ | ___ | ___ |

---

**Final Audit Readiness Sign-Off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tax Manager | ___ | ___ | ___ |
| Tax Director | ___ | ___ | ___ |
| CFO/Finance Director | ___ | ___ | ___ |

**Audit Readiness Score:**

| Section | Items Complete | Total Items | Score |
|---------|---------------|-------------|-------|
| A. Entity/Scope | ___ | 7 | ___% |
| B. GloBE Income | ___ | 7 | ___% |
| C. Covered Taxes | ___ | 7 | ___% |
| D. ETR/Top-up Tax | ___ | 7 | ___% |
| E. Safe Harbours | ___ | 7 | ___% |
| F. Documentation | ___ | 7 | ___% |
| G. Filing | ___ | 7 | ___% |
| H. Cross-Border | ___ | 5 | ___% |
| **Overall** | ___ | **54** | **___%** |

**Target: 100% completion before filing**

---

## Summary: Authority Focus Areas

| Focus Area | What They Check | Your Defence |
|------------|-----------------|--------------|
| **Scope** | €750M threshold, entity completeness | Documented threshold calculation, reconciled CE list |
| **ETR accuracy** | Mathematical correctness, adjustments | Verified calculations, adjustment workpapers |
| **Data consistency** | GIR vs. CbCR vs. FS alignment | Pre-prepared reconciliations |
| **Safe harbours** | Valid application, correct data | CbCR matching, test calculations |
| **Cross-border** | MCAA data matching | Consistent multi-jurisdiction positions |
| **Documentation** | Audit trail completeness | Structured audit file |

---

## Key Takeaways

1. **Tax authorities are prepared**: Dedicated Pillar Two teams (like HMRC's) are established and ready to verify GIR submissions

2. **Data matching is automated**: The MCAA enables automatic cross-border comparison of GIR data within 3-6 months of filing

3. **Reconciliation is critical**: Authorities will compare GIR data to CbCR and financial statements - proactive reconciliation is essential

4. **Documentation prevents penalties**: Under transitional penalty relief, "reasonable measures" including documentation provide protection

5. **Consistency across jurisdictions**: Multi-authority coordination means positions must be defensible globally

6. **Proactive preparation**: Audit defence documentation should be prepared before filing, not after queries arise

---

## Further Reading and Resources

- [HMRC: Register to report Pillar 2 Top-up Taxes](https://www.gov.uk/guidance/register-to-report-pillar-2-top-up-taxes)
- [HMRC: How to report Pillar 2 Top-up Taxes](https://www.gov.uk/guidance/how-to-report-pillar-2-top-up-taxes)
- [ICAEW: HMRC reminds groups of Pillar 2 requirements](https://www.icaew.com/insights/tax-news/2025/apr-2025/hmrc-reminds-groups-of-pillar-2-requirements)
- [IBFD: 14 Jurisdictions Sign GIR MCAA](https://www.ibfd.org/news/14-jurisdictions-sign-multilateral-competent-authority-agreement-exchange-globe-information)
- [PwC: Countries establish Pillar Two compliance procedures](https://www.pwc.com/us/en/services/tax/library/countries-begin-to-establish-pillar-two-compliance-procedures.html)
- [PwC: Pillar Two compliance challenges](https://www.pwc.com/us/en/services/tax/library/pillar-two-compliance-challenges.html)
- [CSC: GloBE Information Return - What MNEs Need to Know](https://blog.cscglobal.com/corptax-gir-reporting/)
- [oecdpillars.com: Pillar Two Administration](https://oecdpillars.com/pillar-tab/pillar-two-administration/)

---

*End of Section 11.2*
