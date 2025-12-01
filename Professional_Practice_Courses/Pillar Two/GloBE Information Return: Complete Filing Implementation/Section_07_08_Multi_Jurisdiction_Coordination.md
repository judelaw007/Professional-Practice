# Section 7.8: Multi-Jurisdiction Coordination

## Learning Objectives

By the end of this section, you will be able to:
- Develop a coordinated multi-jurisdiction Pillar Two filing strategy
- Identify the primary filing jurisdiction and notification requirements
- Leverage the GIR MCAA for efficient compliance
- Manage timeline dependencies across jurisdictions
- Ensure data consistency across all filings
- Apply the Multi-Jurisdiction Filing Coordination Framework

## Introduction

MNE Groups with constituent entities in multiple jurisdictions face the challenge of coordinating Pillar Two filings across different tax authorities, each with their own portals, deadlines, and requirements. Effective coordination is essential to:

- Avoid duplicate filings and unnecessary compliance burden
- Ensure data consistency across all jurisdictions
- Meet all deadlines without last-minute pressure
- Leverage the GIR MCAA automatic exchange mechanism
- Minimise penalty exposure across the group

This section provides a practical framework for managing multi-jurisdiction Pillar Two compliance.

---

## 7.8.1 The GIR MCAA Framework

### Understanding Central Filing and Exchange

The OECD developed the GIR Multilateral Competent Authority Agreement (MCAA) to enable:

```
GIR MCAA Framework:
│
├── CENTRAL FILING
│   ├── GIR filed once in one jurisdiction
│   ├── Typically the UPE jurisdiction
│   ├── Eliminates duplicate full filings
│   └── Reduces compliance burden significantly
│
├── AUTOMATIC EXCHANGE
│   ├── Filing jurisdiction shares GIR with other jurisdictions
│   ├── Via secure government-to-government exchange
│   ├── Receiving jurisdictions get relevant data
│   └── No action required from taxpayer for exchange
│
├── NOTIFICATION REQUIREMENT
│   ├── Local entities notify their tax authority
│   ├── Confirm where GIR was filed
│   ├── Provide filing entity identification
│   └── Much simpler than full GIR filing
│
└── BENEFITS
    ├── Single source of truth for GIR data
    ├── Reduced compliance costs
    ├── Consistent information across authorities
    └── Streamlined global compliance
```

### GIR MCAA Signatories

As of 2025, numerous jurisdictions have signed the GIR MCAA. Key signatories include:

| Region | Jurisdictions |
|--------|---------------|
| Europe | UK, Germany, Netherlands, France, Ireland, Luxembourg, Austria, Switzerland, Spain, Italy |
| Asia-Pacific | Singapore, Australia, Japan, South Korea |
| Americas | Canada |
| Other | Many additional OECD/IF members |

**Important:** Always verify current signatory status at the OECD website, as new jurisdictions continue to join.

---

## 7.8.2 Determining the Primary Filing Jurisdiction

### Decision Framework

```
Primary Filing Jurisdiction Determination:
│
├── STEP 1: Identify UPE Location
│   ├── Where is the Ultimate Parent Entity tax resident?
│   ├── Has that jurisdiction implemented Pillar Two?
│   └── If YES → likely primary filing jurisdiction
│
├── STEP 2: Check GIR MCAA Participation
│   ├── Is the UPE jurisdiction a GIR MCAA signatory?
│   ├── Does it have exchange agreements with other jurisdictions?
│   └── If YES → central filing will work
│
├── STEP 3: Consider Designated Filing Entity (DFE)
│   ├── Has the group designated an alternative filing entity?
│   ├── Is the DFE in a jurisdiction with GIR MCAA?
│   └── DFE location may become primary filing jurisdiction
│
├── STEP 4: Evaluate Practical Considerations
│   ├── Portal accessibility and language
│   ├── Group expertise in jurisdiction
│   ├── Adviser support availability
│   └── Historical compliance relationships
│
└── STEP 5: Document Decision
    ├── Record rationale for primary jurisdiction choice
    ├── Communicate to all affected entities
    └── Update as circumstances change
```

### Common Scenarios

| Scenario | Primary Filing Jurisdiction | Other Jurisdictions |
|----------|----------------------------|---------------------|
| UK-parented group | UK | Notifications only |
| US-parented group (US not implementing) | Designated jurisdiction | Notifications where possible |
| German-parented group | Germany | Notifications only |
| Multi-tier structure | Usually top-tier Pillar Two jurisdiction | Depends on structure |

---

## 7.8.3 Mapping Filing Obligations

### Jurisdiction-by-Jurisdiction Analysis

For each jurisdiction where the group has constituent entities, determine:

```
Filing Obligation Mapping:
│
├── FOR EACH JURISDICTION
│   │
│   ├── QUESTION 1: Has Pillar Two been implemented?
│   │   ├── YES → Continue analysis
│   │   └── NO → No Pillar Two obligations (monitor for changes)
│   │
│   ├── QUESTION 2: Is this the primary filing jurisdiction?
│   │   ├── YES → Full GIR filing required
│   │   └── NO → Proceed to Question 3
│   │
│   ├── QUESTION 3: Will the primary jurisdiction exchange GIR?
│   │   ├── YES → Notification only required
│   │   └── NO → May need full GIR filing
│   │
│   ├── QUESTION 4: Are domestic returns required?
│   │   ├── IIR Return? (parent entities)
│   │   ├── QDMTT/DMT Return? (local entities)
│   │   ├── UTPR Return? (if applicable)
│   │   └── Document all domestic obligations
│   │
│   └── QUESTION 5: Is registration required?
│       ├── When is registration deadline?
│       ├── What information is needed?
│       └── Who is responsible for registering?
│
└── OUTPUT: Complete obligation map by jurisdiction
```

### Filing Obligation Matrix Template

```
FILING OBLIGATION MATRIX

Group: _________________________ Fiscal Year: _____________

┌─────────────┬────────┬────────┬──────────┬────────┬────────┬──────────┐
│ Jurisdiction│ GIR    │ Notify │ IIR      │ QDMTT  │ UTPR   │ Register │
│             │ Filing │ Only   │ Return   │ Return │ Return │ Required │
├─────────────┼────────┼────────┼──────────┼────────┼────────┼──────────┤
│ [Primary]   │ ☑      │ N/A    │ [Y/N]    │ [Y/N]  │ [Y/N]  │ [Y/N]    │
│ [Juris 2]   │ ☐      │ ☑      │ [Y/N]    │ [Y/N]  │ [Y/N]  │ [Y/N]    │
│ [Juris 3]   │ ☐      │ ☑      │ [Y/N]    │ [Y/N]  │ [Y/N]  │ [Y/N]    │
│ [Juris 4]   │ ☐      │ ☑      │ [Y/N]    │ [Y/N]  │ [Y/N]  │ [Y/N]    │
│ ...         │        │        │          │        │        │          │
└─────────────┴────────┴────────┴──────────┴────────┴────────┴──────────┘

Notes:
- GIR Filing: Full GIR submitted in this jurisdiction
- Notify Only: Notification that GIR filed elsewhere
- Domestic Returns: Jurisdiction-specific tax returns
- Register: Pre-filing registration required
```

---

## 7.8.4 Timeline Coordination

### Master Deadline Calendar

```
Creating a Master Deadline Calendar:
│
├── STEP 1: List All Jurisdictions
│   └── Include every jurisdiction with Pillar Two presence
│
├── STEP 2: Identify All Deadlines
│   ├── Registration deadlines
│   ├── GIR/Notification deadlines
│   ├── Domestic return deadlines
│   ├── Payment deadlines
│   └── Any unique jurisdiction-specific deadlines
│
├── STEP 3: Order by Date
│   ├── Earliest deadline drives the timeline
│   ├── Allow buffer before each deadline
│   └── Account for review and approval cycles
│
├── STEP 4: Add Dependencies
│   ├── GIR must be filed before notifications
│   ├── Some returns depend on GIR data
│   └── Payments may depend on return filing
│
└── STEP 5: Build in Contingency
    ├── Allow for validation errors
    ├── Plan for system issues
    └── Include re-submission time if needed
```

### Sample Timeline (Calendar Year-End Group, FY 2024)

```
MASTER FILING TIMELINE - FY 2024 (31 DECEMBER YEAR-END)

2025
────────────────────────────────────────────────────────────────────────
│ Feb 28 │ Germany Group Head Notification deadline
│        │
│ Sep 30 │ Singapore registration deadline (for FY 2025)
│        │
│ Oct 20 │ Canada PT Account registration available
│        │
│ Dec 31 │ Ireland registration deadline
│        │
2026
────────────────────────────────────────────────────────────────────────
│ Mar    │ Internal: GIR data compilation complete
│        │
│ Apr    │ Internal: GIR XML validation complete
│        │
│ May 1  │ TARGET: File GIR in primary jurisdiction
│        │ (allows 2-month buffer before June 30)
│        │
│ May 15 │ TARGET: Submit notifications to secondary jurisdictions
│        │
│ Jun 1  │ TARGET: File domestic returns (IIR, QDMTT, UTPR)
│        │
│ Jun 30 │ DEADLINE: GIR and most domestic returns
│        │ (UK, Germany, France, Canada, Australia, Ireland, etc.)
│        │
│ Jul 25 │ Spain: Complementary Tax Return deadline
│        │
│ Jul 31 │ Singapore: MTT payment deadline (for FY 2025)
│        │
│ Aug 31 │ Netherlands: Top-up Tax Return deadline
│        │
────────────────────────────────────────────────────────────────────────
```

### Critical Path Management

```
Critical Path for Multi-Jurisdiction Filing:
│
├── PHASE 1: DATA COLLECTION (Months 1-12 of FY)
│   ├── Establish data collection processes
│   ├── Gather financial data from all CEs
│   ├── Compile covered taxes information
│   └── Deadline: 3 months after FY end
│
├── PHASE 2: GIR PREPARATION (Months 1-6 after FY)
│   ├── Calculate ETR by jurisdiction
│   ├── Determine top-up tax
│   ├── Prepare GIR data per OECD specification
│   ├── Generate and validate XML
│   └── Deadline: 4 months before filing deadline
│
├── PHASE 3: INTERNAL REVIEW (6-8 weeks before deadline)
│   ├── Technical review of calculations
│   ├── Legal/compliance review
│   ├── Management sign-off
│   └── Final XML validation
│
├── PHASE 4: PRIMARY FILING (4-8 weeks before deadline)
│   ├── Submit GIR in primary jurisdiction
│   ├── Receive confirmation
│   ├── Record filing details
│   └── Prepare notification data
│
├── PHASE 5: SECONDARY FILINGS (2-4 weeks before deadline)
│   ├── Submit notifications to other jurisdictions
│   ├── File domestic returns (IIR, QDMTT, UTPR)
│   ├── Arrange payments
│   └── Collect all confirmations
│
└── PHASE 6: CLOSE-OUT (By deadline)
    ├── Verify all filings complete
    ├── Confirm all payments made
    ├── Archive documentation
    └── Update filing register
```

---

## 7.8.5 Data Consistency Management

### The Single Source of Truth Principle

```
Data Consistency Framework:
│
├── SINGLE SOURCE OF TRUTH
│   ├── One master GIR dataset
│   ├── All filings derive from same source
│   ├── Centralised data management
│   └── Version control on all changes
│
├── CONSISTENCY CHECKPOINTS
│   ├── GIR figures = Domestic return figures
│   ├── Entity names/IDs consistent across filings
│   ├── Covered taxes reconcile to local returns
│   └── Top-up tax allocations balance
│
├── COMMON CONSISTENCY ISSUES
│   ├── Entity naming variations
│   ├── Currency conversion differences
│   ├── Timing differences in data updates
│   ├── Manual entry errors
│   └── Version control failures
│
└── PREVENTION STRATEGIES
    ├── Centralised data repository
    ├── Automated data extraction
    ├── Reconciliation procedures
    └── Change control processes
```

### Reconciliation Procedures

```
Multi-Jurisdiction Reconciliation:
│
├── STEP 1: GIR to Domestic Return Reconciliation
│   ├── Compare GIR jurisdictional data to local returns
│   ├── Verify top-up tax amounts match
│   ├── Check entity coverage is consistent
│   └── Document any differences with explanations
│
├── STEP 2: Cross-Border Consistency Check
│   ├── Intercompany transactions balance
│   ├── Ownership percentages consistent
│   ├── Covered taxes properly allocated
│   └── No double-counting of entities
│
├── STEP 3: Prior Period Comparison
│   ├── Compare to previous year GIR
│   ├── Identify and explain significant changes
│   ├── Verify brought-forward amounts
│   └── Check election consistency
│
└── STEP 4: Sign-Off
    ├── Document reconciliation completed
    ├── Explain any residual differences
    └── Obtain preparer and reviewer sign-off
```

---

## 7.8.6 Communication and Governance

### Stakeholder Management

```
Multi-Jurisdiction Communication Framework:
│
├── INTERNAL STAKEHOLDERS
│   │
│   ├── Group Tax Function (Central)
│   │   ├── Overall coordination responsibility
│   │   ├── GIR preparation and filing
│   │   ├── Policy and methodology decisions
│   │   └── Reporting to leadership
│   │
│   ├── Local Finance/Tax Teams
│   │   ├── Local data provision
│   │   ├── Domestic return preparation
│   │   ├── Local registration and filing
│   │   └── Payment processing
│   │
│   ├── CFO/Tax Director
│   │   ├── Strategic oversight
│   │   ├── Sign-off on major positions
│   │   └── Risk management
│   │
│   └── Audit Committee/Board
│       ├── Periodic updates on compliance status
│       └── Material issue escalation
│
├── EXTERNAL STAKEHOLDERS
│   │
│   ├── External Tax Advisers
│   │   ├── Technical support by jurisdiction
│   │   ├── Filing support where needed
│   │   └── Position papers and advice
│   │
│   ├── External Auditors
│   │   ├── Tax provision review
│   │   ├── Disclosure review
│   │   └── Process understanding
│   │
│   └── Tax Authorities
│       ├── Formal filings only
│       ├── Query responses
│       └── Voluntary disclosures if needed
│
└── COMMUNICATION CALENDAR
    ├── Monthly: Status update to Group Tax
    ├── Quarterly: Update to CFO/Tax Director
    ├── Pre-filing: Sign-off from leadership
    └── Post-filing: Confirmation to stakeholders
```

### RACI Matrix

```
MULTI-JURISDICTION PILLAR TWO RACI MATRIX

Task                          │ Group │ Local │ CFO  │ External │
                              │ Tax   │ Tax   │      │ Adviser  │
──────────────────────────────┼───────┼───────┼──────┼──────────┤
GIR data specification        │   A   │   C   │  I   │    C     │
Local data collection         │   C   │   R   │  I   │    -     │
GIR preparation               │   R   │   C   │  I   │    C     │
GIR validation                │   R   │   C   │  I   │    C     │
Primary jurisdiction filing   │   R   │   I   │  A   │    C     │
Secondary notifications       │   C   │   R   │  I   │    C     │
Domestic returns              │   C   │   R   │  I   │    C     │
Payment processing            │   I   │   R   │  A   │    -     │
Documentation/archiving       │   R   │   R   │  I   │    -     │

Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed
```

---

## 7.8.7 Risk Management

### Multi-Jurisdiction Risk Register

```
PILLAR TWO MULTI-JURISDICTION RISK REGISTER

┌────┬─────────────────────────┬────────┬────────┬─────────────────────────┐
│ #  │ Risk                    │ Impact │ Likely │ Mitigation              │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 1  │ Missed deadline in one  │ High   │ Medium │ Master calendar with    │
│    │ jurisdiction            │        │        │ early warning alerts    │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 2  │ Data inconsistency      │ High   │ Medium │ Single source of truth  │
│    │ across filings          │        │        │ and reconciliation      │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 3  │ Portal access issues    │ Medium │ Medium │ Early registration and  │
│    │                         │        │        │ access testing          │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 4  │ XML validation failure  │ Medium │ High   │ Three-tier validation   │
│    │ at submission           │        │        │ before filing           │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 5  │ Regulatory change       │ Medium │ Medium │ Monitor OECD and local  │
│    │ during filing period    │        │        │ guidance updates        │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 6  │ Key person dependency   │ High   │ Medium │ Cross-training and      │
│    │                         │        │        │ documentation           │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 7  │ Adviser capacity        │ Medium │ Medium │ Early engagement and    │
│    │ constraints             │        │        │ scope agreement         │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 8  │ Currency/FX issues in   │ Low    │ Medium │ Consistent FX policy    │
│    │ calculations            │        │        │ and documentation       │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 9  │ Intercompany data gaps  │ Medium │ High   │ Early data requests     │
│    │                         │        │        │ and follow-up           │
├────┼─────────────────────────┼────────┼────────┼─────────────────────────┤
│ 10 │ Penalty exposure from   │ High   │ Low    │ File primary first,     │
│    │ non-exchange            │        │        │ verify exchange status  │
└────┴─────────────────────────┴────────┴────────┴─────────────────────────┘
```

### Contingency Planning

```
Contingency Procedures:
│
├── SCENARIO 1: Primary Filing Delayed
│   ├── Impact: Secondary notifications cannot reference filing
│   ├── Action: File notifications with expected filing details
│   ├── Follow-up: Amend notifications once primary filed
│   └── Communication: Alert local teams immediately
│
├── SCENARIO 2: Portal Outage at Deadline
│   ├── Impact: Cannot submit by deadline
│   ├── Action: Document attempts, screenshot errors
│   ├── Follow-up: File immediately when available
│   └── Communication: Contact tax authority, prepare penalty defence
│
├── SCENARIO 3: Validation Error Discovered Post-Filing
│   ├── Impact: Incorrect data submitted
│   ├── Action: Prepare amended filing
│   ├── Follow-up: Submit correction per amendment procedures
│   └── Communication: Notify all jurisdictions affected
│
└── SCENARIO 4: Exchange Not Occurring
    ├── Impact: Secondary jurisdiction not receiving GIR
    ├── Action: May need to file full GIR in that jurisdiction
    ├── Follow-up: Monitor exchange confirmation
    └── Communication: Engage with both tax authorities
```

---

## 7.8.8 Deliverable: Multi-Jurisdiction Filing Coordination Framework

```
MULTI-JURISDICTION FILING COORDINATION FRAMEWORK

Group Name: ________________________________
Fiscal Year: ____ / ____ / ____  to  ____ / ____ / ____
Primary Filing Jurisdiction: _________________
Number of Jurisdictions: _______

═══════════════════════════════════════════════════════════════════════════════

PART 1: JURISDICTION INVENTORY
─────────────────────────────────────────────────────────────────────────────

List all jurisdictions with Pillar Two presence:

1. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
2. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
3. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
4. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
5. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
6. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
7. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2
8. _________________________ ☐ Primary Filing ☐ Notification ☐ No P2

═══════════════════════════════════════════════════════════════════════════════

PART 2: DEADLINE MATRIX
─────────────────────────────────────────────────────────────────────────────

┌─────────────────┬──────────────┬──────────────┬──────────────┬─────────────┐
│ Jurisdiction    │ Registration │ GIR/Notify   │ Domestic     │ Payment     │
│                 │ Deadline     │ Deadline     │ Return       │ Deadline    │
├─────────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
│                 │              │              │              │             │
├─────────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
│                 │              │              │              │             │
├─────────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
│                 │              │              │              │             │
├─────────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
│                 │              │              │              │             │
├─────────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
│                 │              │              │              │             │
└─────────────────┴──────────────┴──────────────┴──────────────┴─────────────┘

EARLIEST CRITICAL DEADLINE: _________________

═══════════════════════════════════════════════════════════════════════════════

PART 3: RESPONSIBILITY ASSIGNMENT
─────────────────────────────────────────────────────────────────────────────

┌─────────────────┬─────────────────────┬─────────────────────┬─────────────┐
│ Jurisdiction    │ Responsible Person  │ Backup Contact      │ Adviser     │
├─────────────────┼─────────────────────┼─────────────────────┼─────────────┤
│                 │                     │                     │             │
├─────────────────┼─────────────────────┼─────────────────────┼─────────────┤
│                 │                     │                     │             │
├─────────────────┼─────────────────────┼─────────────────────┼─────────────┤
│                 │                     │                     │             │
├─────────────────┼─────────────────────┼─────────────────────┼─────────────┤
│                 │                     │                     │             │
└─────────────────┴─────────────────────┴─────────────────────┴─────────────┘

═══════════════════════════════════════════════════════════════════════════════

PART 4: FILING SEQUENCE CHECKLIST
─────────────────────────────────────────────────────────────────────────────

PHASE 1: PRE-FILING
☐ All registrations completed
☐ Portal access tested for all jurisdictions
☐ GIR data compilation complete
☐ XML generated and validated
☐ Internal review and sign-off obtained
☐ Adviser review completed (if applicable)

PHASE 2: PRIMARY FILING
☐ GIR submitted in primary jurisdiction: _________________
☐ Filing date: ____ / ____ / ____
☐ Reference number: _________________
☐ Confirmation archived
☐ Notification data prepared for secondary jurisdictions

PHASE 3: SECONDARY NOTIFICATIONS
☐ Jurisdiction: _____________ Filed: ____ / ____ / ____ Ref: __________
☐ Jurisdiction: _____________ Filed: ____ / ____ / ____ Ref: __________
☐ Jurisdiction: _____________ Filed: ____ / ____ / ____ Ref: __________
☐ Jurisdiction: _____________ Filed: ____ / ____ / ____ Ref: __________
☐ Jurisdiction: _____________ Filed: ____ / ____ / ____ Ref: __________

PHASE 4: DOMESTIC RETURNS
☐ Jurisdiction: _____________ Return: _______ Filed: ____ / ____ / ____
☐ Jurisdiction: _____________ Return: _______ Filed: ____ / ____ / ____
☐ Jurisdiction: _____________ Return: _______ Filed: ____ / ____ / ____
☐ Jurisdiction: _____________ Return: _______ Filed: ____ / ____ / ____
☐ Jurisdiction: _____________ Return: _______ Filed: ____ / ____ / ____

PHASE 5: PAYMENTS
☐ Jurisdiction: _____________ Amount: _______ Paid: ____ / ____ / ____
☐ Jurisdiction: _____________ Amount: _______ Paid: ____ / ____ / ____
☐ Jurisdiction: _____________ Amount: _______ Paid: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

PART 5: DATA CONSISTENCY VERIFICATION
─────────────────────────────────────────────────────────────────────────────

☐ GIR total top-up tax reconciles to sum of domestic returns
☐ Entity coverage consistent across all filings
☐ Covered taxes reconcile to local tax filings
☐ Ownership percentages consistent
☐ No data conflicts identified

Reconciliation performed by: _____________ Date: ____ / ____ / ____
Reconciliation reviewed by: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

PART 6: SIGN-OFF AND CERTIFICATION
─────────────────────────────────────────────────────────────────────────────

I confirm that all Pillar Two filing obligations across all jurisdictions
for the above fiscal year have been properly coordinated and completed.

All Filings Complete: ☐ Yes ☐ No (explain below)

Prepared By: _________________________________ Date: ____ / ____ / ____
             (Group Tax Manager)

Reviewed By: _________________________________ Date: ____ / ____ / ____
             (Head of Tax)

Approved By: _________________________________ Date: ____ / ____ / ____
             (CFO / Tax Director)

═══════════════════════════════════════════════════════════════════════════════

NOTES AND EXCEPTIONS
─────────────────────────────────────────────────────────────────────────────

[Document any issues, exceptions, pending items, or matters for follow-up]

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________

═══════════════════════════════════════════════════════════════════════════════
```

---

## Summary

Effective multi-jurisdiction Pillar Two coordination requires:

1. **Strategic Planning:** Identify the primary filing jurisdiction early
2. **GIR MCAA Leverage:** Use central filing and automatic exchange
3. **Timeline Management:** Build a master calendar driven by earliest deadline
4. **Data Consistency:** Maintain single source of truth for all filings
5. **Clear Governance:** Define responsibilities with RACI matrix
6. **Risk Management:** Identify and mitigate key risks
7. **Documentation:** Maintain comprehensive filing records

The Multi-Jurisdiction Filing Coordination Framework provides a practical tool for managing compliance across multiple tax authorities.

---

## Section Review Questions

1. What is the primary benefit of the GIR MCAA for MNE groups?

2. What is typically the primary filing jurisdiction for a Pillar Two GIR?

3. Why is "single source of truth" important for multi-jurisdiction filings?

4. What should drive the timeline for multi-jurisdiction filing coordination?

5. What is the recommended buffer between target filing date and actual deadline?

**Answers:** 1) Enables central filing and automatic exchange, reducing duplicate filings; 2) Usually the UPE jurisdiction (if implementing Pillar Two); 3) Ensures data consistency across all filings and prevents reconciliation issues; 4) The earliest deadline across all jurisdictions; 5) 4-8 weeks for primary filing, 2-4 weeks for secondary filings.

---

*Section 7.8 Complete. This concludes Part 2, Section 7: Jurisdiction-Specific Filing Procedures. Proceed to Section 8 for Post-Filing Procedures and Ongoing Compliance.*
