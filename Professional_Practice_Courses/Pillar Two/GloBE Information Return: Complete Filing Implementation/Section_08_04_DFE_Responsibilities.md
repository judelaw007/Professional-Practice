# Section 8.4: DFE Responsibilities

## Learning Objectives

By the end of this section, you will be able to:

- Establish data collection processes from all Constituent Entities
- Coordinate effectively with local tax authorities across jurisdictions
- Implement compliant record-keeping systems for DFE operations
- Understand and manage liability considerations for DFE appointments
- Design governance frameworks for ongoing DFE compliance

---

## 8.4.1 Data Collection from Constituent Entities

### The Data Collection Challenge

The DFE must collect comprehensive data from every Constituent Entity to complete the GIR. This represents one of the most operationally demanding aspects of DFE responsibility.

**Data Volume Perspective:**

| Group Size | Typical CE Count | Data Points per CE | Total Data Points |
|------------|------------------|--------------------|--------------------|
| Mid-size MNE | 20-50 | ~150 | 3,000-7,500 |
| Large MNE | 50-150 | ~150 | 7,500-22,500 |
| Very Large MNE | 150-500+ | ~150 | 22,500-75,000+ |

### Core Data Requirements

The DFE must collect data to populate all three GIR sections:

**Section 1: Group Information**
- UPE identification and details
- Consolidated financial statement basis
- Accounting standards applied
- Elections and safe harbour claims

**Section 2: Jurisdictional Information (per jurisdiction)**
- Aggregate GloBE Income/Loss
- Covered Taxes
- Substance-Based Income Exclusion components
- Top-up Tax calculations
- Safe harbour elections

**Section 3: Entity Information (per CE)**
- Legal name and identifiers
- Ownership structure
- Entity classification
- Financial data per GloBE rules

### Data Collection Framework

**Phase 1: Pre-Collection Setup**

```
DATA COLLECTION INFRASTRUCTURE
==============================

1. Centralised Data Platform
   - Secure portal or shared environment
   - Standardised templates
   - Version control
   - Audit trail capability

2. Entity Contact Network
   - Primary contact per CE/jurisdiction
   - Backup contacts
   - Escalation paths
   - Time zone considerations

3. Data Dictionary
   - Field definitions
   - Required vs. optional fields
   - Acceptable formats
   - Validation rules
```

**Phase 2: Data Request Distribution**

| Week | Activity |
|------|----------|
| T-16 | Distribute data request templates to all CEs |
| T-14 | Confirm receipt; address queries |
| T-12 | First submission deadline (draft data) |
| T-10 | DFE review; issue clarification requests |
| T-8 | Final data submission deadline |
| T-6 | Data validation and reconciliation |
| T-4 | Final review and sign-off |
| T-0 | GIR filing deadline |

**Phase 3: Data Validation**

The DFE must validate data before filing:

| Validation Type | Description | Action on Failure |
|-----------------|-------------|-------------------|
| **Completeness** | All required fields populated | Return to CE |
| **Format** | Data in correct format | Correct or return |
| **Consistency** | Cross-checks between fields | Investigate |
| **Reasonableness** | Values within expected ranges | Query CE |
| **Reconciliation** | Ties to financial statements | Document differences |

### Standardised Data Request Template

```
GIR DATA REQUEST - CONSTITUENT ENTITY
=====================================

Entity: _________________________________
Jurisdiction: ___________________________
Fiscal Year: ____________________________
Due Date: _______________________________

SECTION A: ENTITY IDENTIFICATION

A1. Legal name (as registered): _______________________
A2. Tax ID / Registration number: ____________________
A3. Date of incorporation: ___________________________
A4. Entity type (company/partnership/trust/other): ___
A5. Principal business activity: _____________________

SECTION B: OWNERSHIP AND STRUCTURE

B1. Immediate parent entity: _________________________
B2. Ownership percentage: ____________________________
B3. UPE ownership percentage (direct + indirect): ____
B4. Any minority interests? (Y/N): ___________________
B5. Part of tax-consolidated group? (Y/N): ___________

SECTION C: FINANCIAL DATA (Local Currency: _______)

C1. Revenue (per local accounts): ____________________
C2. GloBE Income / (Loss): ___________________________
C3. Covered Taxes - Current: _________________________
C4. Covered Taxes - Deferred: ________________________
C5. Payroll costs (for SBIE): ________________________
C6. Tangible asset NBV (for SBIE): ___________________

SECTION D: ADJUSTMENTS

D1. Stock-based compensation adjustment: _____________
D2. Asymmetric foreign currency adjustment: __________
D3. Policy disallowed expenses: ______________________
D4. Other GloBE adjustments (list): __________________

SECTION E: ELECTIONS (if applicable)

E1. SBIE election made? (Y/N): _______________________
E2. Stock comp. election? (Y/N): _____________________
E3. Realisation basis election? (Y/N): _______________
E4. Other elections: _________________________________

SECTION F: CERTIFICATION

I certify that the information provided is accurate and
complete to the best of my knowledge.

Name: _____________________ Title: ___________________
Signature: _________________ Date: ___________________
```

---

## 8.4.2 Coordination with Local Tax Authorities

### Multi-Authority Relationship Management

The DFE interacts with tax authorities in multiple jurisdictions:

```
DFE AUTHORITY RELATIONSHIPS
===========================

                    ┌─────────────────┐
                    │   DFE Entity    │
                    │  (e.g., UK Co)  │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
   ┌───────────┐      ┌───────────┐      ┌───────────┐
   │   HMRC    │      │   BZSt    │      │   IRAS    │
   │    (UK)   │      │ (Germany) │      │(Singapore)│
   └───────────┘      └───────────┘      └───────────┘
         │                   │                   │
    Files GIR           Files GIR           Files GIR
    for UK CEs         for DE CEs          for SG CEs
```

### Authority Coordination Responsibilities

| Responsibility | Description | Frequency |
|----------------|-------------|-----------|
| **Registration** | Maintain DFE registration with each authority | Annual/ongoing |
| **Filing** | Submit GIR by deadline | Annual |
| **Queries** | Respond to authority questions | As needed |
| **Amendments** | Submit corrections if errors discovered | As needed |
| **Audits** | Support authority examinations | As needed |

### Communication Protocols

**Inbound Communications (Authority → DFE):**

1. **Acknowledgments** - Confirm receipt of filings
2. **Information requests** - Queries about filed data
3. **Audit notifications** - Formal examination notices
4. **Penalty notices** - Late filing or error penalties

**Outbound Communications (DFE → Authority):**

1. **Filings** - GIR submissions
2. **Amendments** - Corrections to filed returns
3. **Voluntary disclosures** - Proactive error correction
4. **Correspondence** - Responses to queries

### Managing Authority Queries

**Query Response Framework:**

```
AUTHORITY QUERY RESPONSE PROCESS
================================

Step 1: Receipt and Logging
- Log query in central register
- Assign reference number
- Note response deadline

Step 2: Triage
- Identify subject matter
- Determine responsible team/person
- Assess complexity and risk

Step 3: Information Gathering
- Collect relevant documentation
- Consult with affected CEs
- Engage advisors if needed

Step 4: Response Preparation
- Draft response
- Internal review
- Sign-off from appropriate level

Step 5: Submission
- Submit within deadline
- Retain copy with proof of submission
- Update query register

Step 6: Follow-up
- Monitor for further queries
- Close matter when resolved
- Document lessons learned
```

---

## 8.4.3 Record-Keeping Requirements

### Statutory Retention Obligations

The DFE must maintain records to support filed GIRs:

| Record Type | Minimum Retention | Best Practice |
|-------------|-------------------|---------------|
| Filed GIRs (copies) | 6-10 years | 10 years |
| Supporting calculations | 6-10 years | 10 years |
| CE data submissions | 6-10 years | 10 years |
| Authority correspondence | 6-10 years | 10 years |
| Election documentation | Life of election + 6 years | Permanent |
| Working papers | 6-10 years | 10 years |

### Record Categories

**Category 1: Filing Records**
- Submitted GIR (XML and PDF)
- Filing confirmations/receipts
- Reference numbers
- Submission timestamps

**Category 2: Source Data**
- CE data request responses
- Financial statements used
- Exchange rates applied
- Supporting schedules

**Category 3: Calculation Workpapers**
- GloBE Income computations
- Covered Tax calculations
- SBIE calculations
- Top-up Tax computations
- ETR calculations by jurisdiction

**Category 4: Elections and Claims**
- Election forms
- Safe harbour claims
- Supporting analysis
- Board approvals

**Category 5: Correspondence**
- Authority communications
- Internal approvals
- Advisor opinions
- Query responses

### Record Management System

**Essential Features:**

| Feature | Purpose |
|---------|---------|
| **Secure storage** | Protect confidential data |
| **Access controls** | Limit to authorised personnel |
| **Version control** | Track changes over time |
| **Search capability** | Locate records efficiently |
| **Backup/recovery** | Protect against data loss |
| **Audit trail** | Track who accessed what, when |

**Folder Structure Example:**

```
GloBE_Records/
├── FY2024/
│   ├── 01_Planning/
│   │   ├── Timeline
│   │   └── Responsibility_matrix
│   ├── 02_Data_Collection/
│   │   ├── Templates_issued/
│   │   ├── CE_responses/
│   │   └── Validation_logs/
│   ├── 03_Calculations/
│   │   ├── Section_1_Group/
│   │   ├── Section_2_Jurisdiction/
│   │   └── Section_3_Entity/
│   ├── 04_Filed_Returns/
│   │   ├── UK_GIR/
│   │   ├── DE_GIR/
│   │   └── [Other jurisdictions]/
│   ├── 05_Correspondence/
│   │   └── [By authority]/
│   └── 06_Sign_offs/
│       └── Approvals_and_certifications
├── FY2025/
└── Elections/
    └── [Ongoing elections]
```

---

## 8.4.4 Liability Considerations

### DFE Liability Framework

The DFE assumes significant responsibility when accepting the role:

**Direct Liabilities:**

| Liability Type | Exposure | Mitigation |
|----------------|----------|------------|
| **Filing penalties** | Late/non-filing penalties | Robust process controls |
| **Accuracy penalties** | Incorrect information penalties | Validation procedures |
| **Interest charges** | On late Top-up Tax | Timely filing |
| **Professional liability** | If DFE is advisor firm | Engagement terms |

**Indirect Liabilities:**

| Liability Type | Exposure | Mitigation |
|----------------|----------|------------|
| **Reputational** | Group reputation with authorities | Quality controls |
| **Operational** | CE reliance on DFE performance | Clear responsibilities |
| **Commercial** | Intercompany disputes | Written agreements |

### Penalty Exposure by Jurisdiction

| Jurisdiction | Maximum Filing Penalty | Accuracy Penalty |
|--------------|------------------------|------------------|
| **UK** | £10,000+ per failure | Tax-geared penalties |
| **Germany** | €30,000 | Additional penalties possible |
| **Netherlands** | €900,000 (serious cases) | Tax-geared penalties |
| **France** | €100,000+ | Tax-geared penalties |
| **Singapore** | S$10,000+ | Additional penalties |
| **Australia** | A$825,000 | Shortfall penalties |

### Risk Allocation Mechanisms

**Intercompany Agreement Provisions:**

The DFE should have written agreements with the UPE and/or CEs covering:

```
KEY AGREEMENT PROVISIONS
========================

1. SCOPE OF SERVICES
   - Specific filing obligations covered
   - Jurisdictions included
   - Data to be provided by CEs

2. DATA RESPONSIBILITIES
   - CE obligation to provide accurate data
   - DFE reliance on CE-provided information
   - Consequences of data errors

3. COST ALLOCATION
   - DFE costs (systems, personnel, advisors)
   - Filing fees
   - Recharge mechanism

4. INDEMNIFICATION
   - CE indemnifies DFE for CE data errors
   - UPE indemnifies for group-level decisions
   - Carve-outs for DFE negligence

5. LIABILITY CAPS
   - Maximum DFE liability
   - Exclusion of consequential damages
   - Insurance requirements

6. TERMINATION
   - Notice period
   - Transition assistance
   - Survival provisions
```

### Insurance Considerations

**Professional Indemnity Insurance:**

If the DFE function is performed by an advisory firm, PI insurance should cover:
- GIR filing services
- Pillar Two advisory services
- Multi-jurisdictional scope

**Directors & Officers Insurance:**

For in-house DFE arrangements, D&O policies should be reviewed to confirm coverage for:
- Tax filing responsibilities
- Regulatory penalties (where insurable)
- Defence costs

---

## 8.4.5 Governance Framework

### DFE Governance Structure

Effective DFE operation requires clear governance:

```
DFE GOVERNANCE MODEL
====================

┌─────────────────────────────────────────┐
│         Group Tax Committee             │
│   (Strategic oversight, major decisions)│
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│         DFE Steering Group              │
│  (Operational oversight, issue resolution)│
│  Members: Group Tax, Finance, Legal     │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│         DFE Operations Team             │
│    (Day-to-day execution, filing)       │
│  Members: Tax managers, analysts        │
└────────────────────┬────────────────────┘
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
┌─────────────────┐    ┌─────────────────┐
│  CE Data        │    │  External       │
│  Contributors   │    │  Advisors       │
└─────────────────┘    └─────────────────┘
```

### Roles and Responsibilities Matrix

| Role | Responsibilities |
|------|------------------|
| **Group Tax Director** | Strategic oversight; authority sign-off; escalation point |
| **DFE Manager** | Operational management; timeline management; quality control |
| **DFE Analysts** | Data collection; validation; calculation preparation |
| **CE Tax Contacts** | Local data provision; query resolution; local compliance |
| **IT Support** | System maintenance; data security; portal access |
| **External Advisors** | Technical advice; filing support; audit defence |

### Quality Control Procedures

**Three Lines of Defence Model:**

| Line | Function | Activities |
|------|----------|------------|
| **First** | DFE Operations | Data validation; calculation checks; filing preparation |
| **Second** | DFE Management | Review and approval; process monitoring; exception handling |
| **Third** | Internal Audit | Periodic review; control testing; compliance verification |

**Sign-off Requirements:**

| Document/Filing | Preparer | Reviewer | Approver |
|-----------------|----------|----------|----------|
| CE data compilation | Analyst | Manager | - |
| Jurisdictional calculations | Analyst | Manager | Director |
| GIR filing (each jurisdiction) | Manager | Director | Group Tax Head |
| Elections/safe harbours | Manager | Director | Group Tax Head |

---

## 8.4.6 Ongoing Compliance Calendar

### Annual DFE Compliance Cycle

```
DFE ANNUAL COMPLIANCE CALENDAR
==============================

Month 1-3 (Post Year-End)
├── Finalise prior year financial statements
├── Commence data collection from CEs
└── Review elections and safe harbour positions

Month 4-6
├── Complete data validation
├── Prepare jurisdictional calculations
└── Draft GIR content

Month 7-9
├── Internal review and sign-off
├── Resolve open queries
└── Prepare filing packages

Month 10-12
├── Submit GIR filings
├── Obtain filing confirmations
└── Archive records

Month 13-15 (Standard deadline)
├── Final filings completed
├── Post-filing review
└── Process improvement for next cycle

Month 16-18 (Transitional first year only)
├── Extended deadline filings
└── Transition to standard cycle
```

### Key Milestone Checklist

```
DFE ANNUAL MILESTONE CHECKLIST
==============================

Client/Group: _______________________________
Fiscal Year: ________________________________

PRE-FILING PHASE                              Date Due    Done
================                              ========    ====
□ Data request templates updated              _______     [  ]
□ CE contact list confirmed                   _______     [  ]
□ Data requests distributed                   _______     [  ]
□ Training/briefing for CEs completed         _______     [  ]

DATA COLLECTION PHASE
=====================
□ All CE responses received                   _______     [  ]
□ Data validation completed                   _______     [  ]
□ Queries resolved                            _______     [  ]
□ Data sign-off obtained from CEs             _______     [  ]

CALCULATION PHASE
=================
□ Section 2 calculations completed            _______     [  ]
□ Section 3 entity data compiled              _______     [  ]
□ Top-up Tax calculations verified            _______     [  ]
□ Safe harbour analysis completed             _______     [  ]

REVIEW PHASE
============
□ Internal review completed                   _______     [  ]
□ Manager sign-off obtained                   _______     [  ]
□ Director approval obtained                  _______     [  ]
□ External advisor review (if applicable)     _______     [  ]

FILING PHASE
============
□ UK GIR filed                                _______     [  ]
□ Germany GIR filed                           _______     [  ]
□ Netherlands GIR filed                       _______     [  ]
□ [Other jurisdictions]                       _______     [  ]
□ All filing confirmations received           _______     [  ]

POST-FILING PHASE
=================
□ Records archived                            _______     [  ]
□ Lessons learned documented                  _______     [  ]
□ Process improvements identified             _______     [  ]
```

---

## Section Summary

DFE responsibilities encompass four critical areas:

1. **Data Collection** - Systematic gathering and validation of CE data
2. **Authority Coordination** - Managing relationships with multiple tax authorities
3. **Record-Keeping** - Maintaining comprehensive documentation for compliance and audit
4. **Liability Management** - Understanding and mitigating exposure through agreements and controls

Effective discharge of these responsibilities requires robust governance, clear processes, and adequate resourcing.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Data Volume** | Large MNEs may have 20,000+ data points to collect |
| **Timeline** | Start data collection 16+ weeks before filing deadline |
| **Validation** | Multi-layer validation essential before filing |
| **Retention** | Minimum 6-10 years; best practice 10 years |
| **Liability** | Written agreements essential for risk allocation |
| **Governance** | Three lines of defence model recommended |
| **Sign-off** | Formal approval chain for all filings |

---

*Section 8.4 Complete. Proceed to Section 8.5: Local Filing Obligations Post-DFE for understanding what local entities must still file after DFE appointment.*
