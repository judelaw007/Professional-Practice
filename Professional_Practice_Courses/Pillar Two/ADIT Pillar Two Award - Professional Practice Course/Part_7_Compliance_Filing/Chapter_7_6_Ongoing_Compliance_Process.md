# Chapter 7.6: Ongoing Compliance Process

## Learning Objective

After completing this chapter, you will be able to establish a sustainable annual Pillar Two compliance cycle, design data gathering processes that integrate with existing financial systems, identify system and technology requirements for GloBE calculations, and implement governance frameworks with appropriate controls for audit-ready compliance.

---

## Key References

**OECD Guidance:**
- GloBE Information Return Template and Instructions (2024)
- Administrative Guidance (January 2025) — Filing requirements
- MCAA Framework for GIR Exchange

**Filing Deadlines:**
- Standard: 15 months after fiscal year-end
- Transitional: 18 months for first fiscal year
- First GIR due: 30 June 2026 (for FY ending 31 December 2024)

---

## Overview: Compliance as an Ongoing Process

Pillar Two compliance is not a one-time project—it is an **enduring requirement** that must be embedded into annual business cycles.

```
┌─────────────────────────────────────────────────────────────────────┐
│ PILLAR TWO COMPLIANCE: ONE-TIME vs ONGOING                          │
│                                                                     │
│ ONE-TIME ACTIVITIES (Year 1):                                       │
│ ├── Scope determination and entity classification                  │
│ ├── System and process implementation                               │
│ ├── Initial data mapping and gap analysis                          │
│ ├── Governance framework design                                     │
│ └── Transition year adjustments (Article 9.1, 9.2)                  │
│                                                                     │
│ ONGOING ANNUAL ACTIVITIES:                                          │
│ ├── Data gathering and validation                                   │
│ ├── ETR calculations by jurisdiction                                │
│ ├── Safe Harbour assessments                                        │
│ ├── Top-up Tax computations                                         │
│ ├── GIR preparation and filing                                      │
│ ├── Local QDMTT filings                                             │
│ ├── Election management                                             │
│ └── Documentation and audit file maintenance                        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Annual Compliance Calendar

### Standard Timeline (15-Month Cycle)

For an MNE with a **31 December fiscal year-end**:

| Month | Activity | Milestone |
|-------|----------|-----------|
| **January** | Fiscal year closes | Year-end close begins |
| **February-March** | Financial statement preparation | Audit process |
| **April** | Statutory accounts finalised | Data available |
| **May-June** | GloBE data extraction | Entity-level data compiled |
| **July-August** | ETR calculations | Jurisdictional analysis |
| **September** | Safe Harbour assessment | Compliance strategy confirmed |
| **October** | Top-up Tax calculations | Liability quantified |
| **November-December** | GIR preparation | Draft GIR reviewed |
| **January (Y+2)** | GIR finalisation | Internal sign-off |
| **February-March (Y+2)** | GIR filing | Filed within 15 months |
| **March (Y+2)** | **Filing deadline** | 31 March (for 31 Dec YE) |

### Transitional Timeline (18-Month Cycle)

For the **first fiscal year** (FY 2024), the extended deadline applies:

| Fiscal Year End | Standard Deadline | Transitional Deadline |
|-----------------|-------------------|----------------------|
| 31 December 2024 | 31 March 2026 | **30 June 2026** |
| 31 March 2025 | 30 June 2026 | **30 September 2026** |
| 30 June 2025 | 30 September 2026 | **31 December 2026** |

### Critical Path Milestones

```
COMPLIANCE TIMELINE: FY ENDING 31 DECEMBER 2024

Year 1 (2024)                    Year 2 (2025)                    Year 3 (2026)
│                                │                                │
│ ●─────────────────────────────●────────────────────────────────●
│ │                              │                                │
│ FY 2024                        │                                │
│ in progress                    │                                │
│                                ▼                                │
│                           31 Dec 2024                           │
│                           Year-end                              │
│                                │                                │
│                                ├──► Feb-Apr: Financial close    │
│                                ├──► May-Aug: GloBE calculations │
│                                ├──► Sep-Dec: GIR preparation    │
│                                │                                │
│                                │                                ▼
│                                │                           30 Jun 2026
│                                │                           FIRST GIR DUE
│                                │                           (18-month
│                                │                            transitional)
```

---

## Data Gathering Process

### Data Sources

Pillar Two calculations require data from **multiple systems**:

| Data Category | Source Systems | Key Data Points |
|---------------|----------------|-----------------|
| **Financial** | ERP, Consolidation system | Net income, revenue, assets |
| **Tax** | Tax provision software | Current tax, deferred tax, CFC |
| **Payroll** | HR/Payroll systems | Employee costs, headcount |
| **Fixed Assets** | Asset register | Tangible asset NBV by location |
| **Entity Master** | Corporate secretarial | Ownership %, entity classification |
| **CbCR** | CbCR filing system | Revenue, PBT, tax paid by jurisdiction |

### The 122 Data Point Framework

The GIR requires approximately **122 key data points** per entity/jurisdiction:

```
DATA POINT CATEGORIES

1. Entity Information (~15 data points)
   ├── Entity name, identification
   ├── Jurisdiction
   ├── Ownership percentage
   └── Entity classification (CE, POPE, JV, etc.)

2. GloBE Income Calculation (~25 data points)
   ├── Financial accounting net income
   ├── Intra-group dividends
   ├── Equity gains/losses
   ├── Asymmetric FX adjustments
   └── Policy disallowed expenses

3. Covered Taxes (~20 data points)
   ├── Current tax expense
   ├── Deferred tax expense
   ├── CFC tax allocations
   ├── Uncertain tax positions
   └── DTA/DTL movements

4. SBIE Components (~15 data points)
   ├── Eligible payroll costs
   ├── Eligible employee count
   ├── Tangible asset NBV
   └── Transition rate applied

5. Top-up Tax Calculation (~20 data points)
   ├── Jurisdictional ETR
   ├── Excess Profit
   ├── Top-up Tax percentage
   └── Allocation factors

6. Elections and Safe Harbours (~15 data points)
   ├── Elections made
   ├── Safe Harbour test results
   └── Prior year data for comparisons

7. Reconciliation Items (~12 data points)
   ├── Prior year adjustments
   ├── DTL recapture
   └── GloBE loss carryforwards
```

### Data Flow Architecture

```
DATA FLOW: FROM SOURCE TO GIR

┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│    ERP      │   │   Tax       │   │   HR/       │
│   System    │   │  Provision  │   │  Payroll    │
└──────┬──────┘   └──────┬──────┘   └──────┬──────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────────────────────────────────────────┐
│           DATA WAREHOUSE / REPOSITORY           │
│                                                 │
│  □ Standardised data definitions                │
│  □ Entity master alignment                      │
│  □ Validation rules applied                     │
│  □ Reconciliation to source systems             │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│              GloBE CALCULATION ENGINE           │
│                                                 │
│  □ ETR calculations                             │
│  □ SBIE computations                            │
│  □ Safe Harbour tests                           │
│  □ Top-up Tax allocation                        │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│              GIR PREPARATION MODULE             │
│                                                 │
│  □ XML schema population                        │
│  □ Validation checks                            │
│  □ GIR filing generation                        │
└─────────────────────────────────────────────────┘
```

### Data Gathering Checklist

```
DATA GATHERING PROCESS CHECKLIST

MNE Group: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
PRE-CLOSE ACTIVITIES (Before Year-End)
═══════════════════════════════════════════════════════════════════════

□ Confirm entity list for GloBE purposes
□ Update ownership percentages for acquisitions/disposals
□ Identify Safe Harbour candidates (prioritise data gathering)
□ Confirm accounting standard used by each entity
□ Validate chart of accounts mapping to GloBE categories

═══════════════════════════════════════════════════════════════════════
POST-CLOSE DATA EXTRACTION (Months 1-4)
═══════════════════════════════════════════════════════════════════════

□ Extract financial data from consolidation system
□ Obtain statutory accounts for material entities
□ Extract tax provision data (current and deferred)
□ Compile payroll costs and headcount by entity
□ Obtain tangible asset NBV by location
□ Verify CbCR data alignment with GloBE entities

═══════════════════════════════════════════════════════════════════════
DATA VALIDATION (Months 4-6)
═══════════════════════════════════════════════════════════════════════

□ Reconcile entity-level to consolidated totals
□ Validate intercompany eliminations
□ Cross-check tax data to filed returns
□ Verify payroll to HR systems
□ Confirm asset locations to fixed asset register
□ Document data sources and adjustments

═══════════════════════════════════════════════════════════════════════
CALCULATION INPUTS (Months 6-10)
═══════════════════════════════════════════════════════════════════════

□ Apply GloBE Income adjustments
□ Apply Covered Tax adjustments
□ Calculate SBIE by jurisdiction
□ Test Safe Harbour eligibility
□ Compute ETR by jurisdiction
□ Calculate Top-up Tax where applicable
```

---

## System Requirements

### Technology Landscape

MNEs typically require **three tiers** of technology support:

| Tier | Purpose | Examples |
|------|---------|----------|
| **Source Systems** | Transaction processing | ERP (SAP, Oracle), Consolidation (Hyperion, OneStream) |
| **Tax Technology** | Provision and compliance | ONESOURCE, Vertex, Longview |
| **GloBE-Specific** | Pillar Two calculations | EY GloBE Engine, PwC Pillar Two solution, Deloitte solution |

### Build vs Buy Decision

```
BUILD vs BUY: TECHNOLOGY OPTIONS

OPTION 1: SPREADSHEET-BASED (Small MNEs)
├── Pros: Low cost, familiar tools
├── Cons: Manual, error-prone, limited audit trail
└── Suitable for: 5-20 entities, simple structures

OPTION 2: ENHANCED TAX PROVISION (Medium MNEs)
├── Pros: Integrated with existing tools
├── Cons: May require significant customisation
└── Suitable for: 20-100 entities, moderate complexity

OPTION 3: DEDICATED GloBE SOLUTION (Large MNEs)
├── Pros: Purpose-built, scalable, audit-ready
├── Cons: Implementation cost, integration effort
└── Suitable for: 100+ entities, complex structures, high volume
```

### Minimum System Capabilities

Any GloBE compliance system should support:

| Capability | Requirement |
|------------|-------------|
| **Data Import** | Multiple formats (Excel, CSV, XML, API) |
| **Entity Management** | Ownership structures, classifications, changes |
| **Calculation Engine** | ETR, SBIE, Top-up Tax with adjustment tracking |
| **Safe Harbour Testing** | Automated De Minimis, ETR, Routine Profits tests |
| **Election Tracking** | Annual elections, irrevocability flags |
| **GIR Generation** | XML schema output, validation against OECD schema |
| **Audit Trail** | Full change log, version control, sign-off workflow |
| **Reporting** | Jurisdictional summaries, variance analysis |

### Integration Requirements

```
SYSTEM INTEGRATION MAP

                           ┌──────────────────────┐
                           │   CONSOLIDATION      │
                           │   SYSTEM             │
                           │   (OneStream, HFM)   │
                           └──────────┬───────────┘
                                      │
                                      │ Financial data
                                      │ Ownership %
                                      ▼
┌──────────────────┐          ┌───────────────────┐          ┌──────────────────┐
│   TAX PROVISION  │          │                   │          │   HR/PAYROLL     │
│   (ONESOURCE,    │ ◄───────►│  GloBE ENGINE     │◄────────►│   (Workday,      │
│    Vertex)       │          │                   │          │    ADP)          │
└──────────────────┘          └─────────┬─────────┘          └──────────────────┘
        │                               │                            │
        │ Tax data                      │ GIR output                 │ Payroll
        │ CFC allocations               │                            │ Headcount
        │                               ▼                            │
        │                     ┌───────────────────┐                  │
        │                     │   GIR FILING      │                  │
        │                     │   PORTAL          │                  │
        │                     │   (Local or DFE)  │                  │
        │                     └───────────────────┘                  │
        │                                                            │
        └────────────────────────────────────────────────────────────┘
                    Common data standards & API connections
```

---

## Governance and Controls

### Operating Model

Establish clear **roles and responsibilities** across functions:

| Role | Function | Responsibilities |
|------|----------|------------------|
| **Pillar Two Lead** | Tax | Overall accountability, filing sign-off |
| **Technical Owner** | Tax | GloBE calculations, elections, technical queries |
| **Data Owner** | Finance | Data extraction, validation, reconciliation |
| **System Owner** | IT/Tax Technology | System maintenance, integrations, access control |
| **Local Tax Manager** | Local Tax | Entity-level data, local QDMTT filings |
| **External Advisor** | External | Technical advice, review, quality assurance |

### Three Lines of Defence

Apply a **three lines of defence** governance model:

```
THREE LINES OF DEFENCE: PILLAR TWO

FIRST LINE: OPERATIONAL CONTROLS
├── Data extraction procedures
├── Calculation review and sign-off
├── Reconciliation processes
├── Documentation standards
└── Owner: Tax/Finance teams

SECOND LINE: OVERSIGHT FUNCTIONS
├── Independent calculation review
├── Exception reporting
├── Policy compliance monitoring
├── Training and awareness
└── Owner: Tax Director / Internal Compliance

THIRD LINE: INDEPENDENT ASSURANCE
├── Internal audit review
├── External advisor review (periodic)
├── Process effectiveness assessment
└── Owner: Internal Audit / External Auditor
```

### Control Framework

| Control Area | Control Description | Frequency |
|--------------|---------------------|-----------|
| **Completeness** | All CEs included in GloBE scope | Annual |
| **Accuracy** | Calculation review and recalculation | Each filing |
| **Timeliness** | Filing deadline monitoring | Quarterly |
| **Authorisation** | GIR sign-off by authorised officer | Each filing |
| **Data Integrity** | Reconciliation to source systems | Monthly |
| **Change Control** | System changes documented and tested | As needed |
| **Segregation** | Preparer vs reviewer separation | Each filing |

### Documentation Requirements

Maintain an **audit-ready file** for each fiscal year:

```
PILLAR TWO AUDIT FILE STRUCTURE

📁 FY 2024 Pillar Two Compliance File
│
├── 📁 1. Scope and Entity Classification
│   ├── Entity list with ownership %
│   ├── Scope determination memo
│   └── Excluded entity analysis
│
├── 📁 2. GloBE Income Calculations
│   ├── Adjustment schedules by entity
│   ├── Source document references
│   └── Review sign-off
│
├── 📁 3. Covered Taxes
│   ├── Tax expense analysis by entity
│   ├── Deferred tax workings
│   └── CFC/hybrid allocations
│
├── 📁 4. ETR and Top-up Tax
│   ├── Jurisdictional ETR calculations
│   ├── SBIE workings
│   └── Top-up Tax allocation
│
├── 📁 5. Safe Harbours
│   ├── Safe Harbour qualification analysis
│   ├── CbCR data reconciliation
│   └── Test results by jurisdiction
│
├── 📁 6. Elections
│   ├── Election register
│   ├── Analysis supporting elections
│   └── Board/committee approval
│
├── 📁 7. GIR Filing
│   ├── Filed GIR (XML and PDF)
│   ├── Filing confirmation receipt
│   └── Prior year comparison
│
└── 📁 8. Governance
    ├── Sign-off matrix
    ├── Review comments and resolutions
    └── Issue log and remediation
```

---

## Process Map: Annual Pillar Two Compliance Cycle

### The Twelve-Step Cycle

```
ANNUAL PILLAR TWO COMPLIANCE CYCLE

                          ┌───────────────────┐
                          │    1. PLANNING    │
                          │    (Month -1)     │
                          │                   │
                          │ □ Update entity   │
                          │   list            │
                          │ □ Confirm         │
                          │   timelines       │
                          │ □ Assign          │
                          │   responsibilities│
                          └─────────┬─────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            ▼                       ▼                       ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│   2. DATA         │   │   3. DATA         │   │   4. DATA         │
│   EXTRACTION      │   │   VALIDATION      │   │   ENRICHMENT      │
│   (Months 1-3)    │   │   (Months 3-4)    │   │   (Months 4-5)    │
│                   │   │                   │   │                   │
│ □ Financial data  │   │ □ Reconcile to    │   │ □ Apply GloBE     │
│ □ Tax data        │   │   source          │   │   adjustments     │
│ □ Payroll data    │   │ □ Identify gaps   │   │ □ Allocate CFC    │
│ □ Asset data      │   │ □ Resolve issues  │   │   taxes           │
└─────────┬─────────┘   └─────────┬─────────┘   └─────────┬─────────┘
          │                       │                       │
          └───────────────────────┴───────────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │      5. SAFE HARBOUR          │
                    │      ASSESSMENT               │
                    │      (Months 5-6)             │
                    │                               │
                    │ □ Test De Minimis             │
                    │ □ Test Simplified ETR         │
                    │ □ Test Routine Profits        │
                    │ □ Identify QDMTT jurisdictions│
                    └───────────────┬───────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            │                                               │
            ▼                                               ▼
┌───────────────────────┐                   ┌───────────────────────┐
│   6. ETR CALCULATION  │                   │   7. TOP-UP TAX       │
│   (Months 6-8)        │                   │   CALCULATION         │
│                       │                   │   (Months 8-9)        │
│ □ Calculate GloBE     │                   │                       │
│   Income by CE        │                   │ □ Apply SBIE          │
│ □ Calculate Covered   │                   │ □ Calculate Excess    │
│   Taxes by CE         │                   │   Profit              │
│ □ Aggregate by        │                   │ □ Determine Top-up    │
│   jurisdiction        │                   │   Tax                 │
│ □ Compute ETR         │                   │ □ Allocate via        │
│                       │                   │   IIR/UTPR            │
└───────────────────────┘                   └───────────────┬───────┘
                                                            │
                                    ┌───────────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │      8. ELECTION REVIEW       │
                    │      (Months 9-10)            │
                    │                               │
                    │ □ Review annual elections     │
                    │ □ Assess new elections        │
                    │ □ Document irrevocable        │
                    │   elections                   │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│   9. GIR          │   │   10. INTERNAL    │   │   11. FILING      │
│   PREPARATION     │   │   REVIEW          │   │                   │
│   (Months 10-12)  │   │   (Months 12-13)  │   │   (Months 13-15)  │
│                   │   │                   │   │                   │
│ □ Populate GIR    │   │ □ Technical       │   │ □ Submit GIR      │
│   template        │   │   review          │   │ □ Local QDMTT     │
│ □ Run validation  │   │ □ Data validation │   │   filings         │
│ □ Generate XML    │   │ □ Management      │   │ □ Confirm receipt │
│                   │   │   sign-off        │   │                   │
└─────────┬─────────┘   └─────────┬─────────┘   └─────────┬─────────┘
          │                       │                       │
          └───────────────────────┴───────────────────────┘
                                    │
                                    ▼
                          ┌───────────────────┐
                          │   12. POST-FILING │
                          │   ACTIVITIES      │
                          │   (Month 15+)     │
                          │                   │
                          │ □ Archive         │
                          │   documentation   │
                          │ □ Lessons learned │
                          │ □ System updates  │
                          │ □ Plan next cycle │
                          └───────────────────┘
```

---

## Stratos Worked Example: Compliance Process Design

### Background

Stratos Holdings plc is establishing its ongoing Pillar Two compliance process for FY 2025 onwards.

### Stratos Compliance Calendar (FY 2025)

| Phase | Period | Stratos Activity |
|-------|--------|------------------|
| **Year-end** | Dec 2025 | FY 2025 closes |
| **Financial close** | Jan-Mar 2026 | Consolidation, statutory audits |
| **Data extraction** | Apr-May 2026 | GloBE data from OneStream |
| **Safe Harbour** | Jun 2026 | Test 7 jurisdictions |
| **ETR calculations** | Jul-Aug 2026 | Calculate for SG, Cayman (non-SH) |
| **Top-up Tax** | Sep 2026 | €477,978 total liability |
| **GIR preparation** | Oct-Dec 2026 | UK DFE filing preparation |
| **Review** | Jan 2027 | Tax Director sign-off |
| **Filing** | Feb 2027 | GIR filed via UK HMRC |
| **Deadline** | 31 Mar 2027 | 15-month deadline |

### Stratos Data Gathering Matrix

| Data Category | Source | Owner | Extraction Date |
|---------------|--------|-------|-----------------|
| Financial statements | OneStream | Group Finance | April 2026 |
| Tax provision | ONESOURCE | Tax Provision Team | April 2026 |
| Payroll costs | Workday | HR Finance | May 2026 |
| Tangible assets | SAP | Fixed Assets Team | May 2026 |
| Ownership structure | Diligent | Company Secretary | January 2026 |
| CbCR data | CbCR Tool | Tax Compliance | April 2026 |

### Stratos Governance Structure

```
STRATOS PILLAR TWO GOVERNANCE

                        ┌─────────────────────────┐
                        │      AUDIT COMMITTEE    │
                        │                         │
                        │ Annual compliance       │
                        │ oversight               │
                        └────────────┬────────────┘
                                     │
                        ┌────────────┴────────────┐
                        │      CFO                │
                        │                         │
                        │ GIR filing authorisation│
                        │ (Designated signatory)  │
                        └────────────┬────────────┘
                                     │
                        ┌────────────┴────────────┐
                        │   TAX DIRECTOR          │
                        │   (Pillar Two Lead)     │
                        │                         │
                        │ Overall accountability  │
                        │ Technical decisions     │
                        │ Election approvals      │
                        └────────────┬────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
        ▼                            ▼                            ▼
┌───────────────────┐    ┌───────────────────┐    ┌───────────────────┐
│   HEAD OF TAX     │    │   FINANCE         │    │   TAX TECHNOLOGY  │
│   COMPLIANCE      │    │   CONTROLLER      │    │   MANAGER         │
│                   │    │                   │    │                   │
│ GIR preparation   │    │ Data extraction   │    │ System maintenance│
│ Local filings     │    │ Reconciliation    │    │ Integration       │
│ Safe Harbour tests│    │ Validation        │    │ Reporting         │
└───────────────────┘    └───────────────────┘    └───────────────────┘
        │                            │                            │
        └────────────────────────────┼────────────────────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
                    ▼                                 ▼
            ┌───────────────────┐          ┌───────────────────┐
            │   LOCAL TAX       │          │   EXTERNAL        │
            │   MANAGERS        │          │   ADVISOR         │
            │   (7 jurisdictions)│          │   (Annual review) │
            └───────────────────┘          └───────────────────┘
```

### Stratos Control Matrix

| Control | Description | Owner | Frequency |
|---------|-------------|-------|-----------|
| Entity completeness | Verify all CEs included | Company Secretary | Quarterly |
| Data reconciliation | Match to statutory accounts | Finance Controller | Each extraction |
| Calculation review | Independent recalculation | External Advisor | Annually |
| ETR reasonableness | Compare to prior year | Tax Director | Each calculation |
| Election tracking | Maintain election register | Head of Tax Compliance | Ongoing |
| GIR validation | Schema validation pre-filing | Tax Technology | Each filing |
| Sign-off | CFO authorisation | CFO | Each filing |

### Stratos Resource Requirements

| Role | FTE Equivalent | Cost Estimate (Annual) |
|------|----------------|----------------------|
| Pillar Two Lead (Tax Director) | 0.2 FTE | Absorbed |
| Technical compliance | 1.0 FTE | €85,000 |
| Data gathering | 0.5 FTE | €35,000 |
| External advisory | — | €100,000 |
| Technology (GloBE solution) | — | €50,000 |
| **Total incremental cost** | | **€270,000** |

---

## Common Pitfalls

### Pitfall 1: Treating Pillar Two as a One-Time Project

**Error:** Completing the first GIR filing and disbanding the project team.

**Correct approach:** Establish Pillar Two as an ongoing compliance process with permanent resources, documented procedures, and annual cycle planning.

### Pitfall 2: Siloed Data Gathering

**Error:** Tax function attempting to gather all data independently without Finance and IT involvement.

**Correct approach:** Establish cross-functional data ownership with clear extraction schedules, validation procedures, and escalation paths for data quality issues.

### Pitfall 3: Inadequate Documentation

**Error:** Relying on spreadsheet calculations without supporting documentation.

**Correct approach:** Maintain an audit-ready file with source references, calculation workings, review evidence, and sign-off trails for each jurisdiction.

### Pitfall 4: Missing Local Filing Requirements

**Error:** Focusing only on the central GIR and overlooking local QDMTT or notification requirements.

**Correct approach:** Map all local filing obligations, which may have different deadlines (some jurisdictions require Q3 filings). Monitor jurisdiction-specific guidance.

### Pitfall 5: No Contingency Planning

**Error:** Assuming data will be available on schedule without backup plans.

**Correct approach:** Build buffer time into the compliance calendar. Identify critical path dependencies and alternative data sources if primary sources are delayed.

### Pitfall 6: Underestimating System Requirements

**Error:** Attempting Pillar Two calculations in Excel for a 50+ entity group.

**Correct approach:** Assess technology needs based on group complexity. Invest in appropriate tools that provide audit trail, version control, and scalability.

---

## Ongoing Compliance Process Checklist

```
ONGOING COMPLIANCE PROCESS CHECKLIST
MNE Group: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: ANNUAL PLANNING
═══════════════════════════════════════════════════════════════════════

□ Compliance calendar confirmed for fiscal year           Due: ________
□ Roles and responsibilities assigned                     Due: ________
□ Data extraction schedule agreed with Finance            Due: ________
□ Safe Harbour pre-assessment completed                   Due: ________
□ Resource requirements confirmed                         Due: ________

═══════════════════════════════════════════════════════════════════════
SECTION B: DATA GATHERING
═══════════════════════════════════════════════════════════════════════

□ Entity list updated (acquisitions, disposals)           Due: ________
□ Financial data extracted                                Due: ________
□ Tax provision data extracted                            Due: ________
□ Payroll data extracted                                  Due: ________
□ Tangible asset data extracted                           Due: ________
□ Data reconciled to source systems                       Due: ________
□ Data gaps identified and resolved                       Due: ________

═══════════════════════════════════════════════════════════════════════
SECTION C: CALCULATIONS
═══════════════════════════════════════════════════════════════════════

□ Safe Harbour tests completed                            Due: ________
   - Jurisdictions qualifying: ____________________________
   - Jurisdictions requiring full calculation: ____________
□ GloBE Income calculated by jurisdiction                 Due: ________
□ Covered Taxes calculated by jurisdiction                Due: ________
□ ETR calculated by jurisdiction                          Due: ________
□ SBIE calculated by jurisdiction                         Due: ________
□ Top-up Tax calculated                                   Due: ________
□ Allocation (IIR/UTPR) determined                        Due: ________

═══════════════════════════════════════════════════════════════════════
SECTION D: ELECTIONS
═══════════════════════════════════════════════════════════════════════

□ Election register reviewed                              Due: ________
□ New elections evaluated                                 Due: ________
□ Irrevocable elections confirmed still appropriate       Due: ________
□ Elections documented and approved                       Due: ________

═══════════════════════════════════════════════════════════════════════
SECTION E: GIR PREPARATION
═══════════════════════════════════════════════════════════════════════

□ GIR template populated                                  Due: ________
□ XML validation completed (no errors)                    Due: ________
□ Internal review completed                               Due: ________
□ Management sign-off obtained                            Due: ________

═══════════════════════════════════════════════════════════════════════
SECTION F: FILING
═══════════════════════════════════════════════════════════════════════

□ GIR filed with DFE jurisdiction                         Due: ________
   - Filing confirmation received: YES / NO
□ Local QDMTT filings completed                           Due: ________
   - Jurisdictions filed: _________________________________
□ Local notification requirements met                     Due: ________

═══════════════════════════════════════════════════════════════════════
SECTION G: POST-FILING
═══════════════════════════════════════════════════════════════════════

□ Audit file archived                                     Due: ________
□ Lessons learned documented                              Due: ________
□ System/process improvements identified                  Due: ________
□ Next year planning initiated                            Due: ________
```

---

## Summary

Establishing an effective ongoing Pillar Two compliance process requires:

| Component | Key Actions |
|-----------|-------------|
| **Compliance Calendar** | 15-month cycle (18-month transitional); milestone-driven |
| **Data Gathering** | Cross-functional ownership; 122+ data points; standardised extraction |
| **Systems** | Source integration; GloBE calculation engine; GIR generation capability |
| **Governance** | Three lines of defence; clear roles; sign-off authority |
| **Controls** | Completeness, accuracy, timeliness; reconciliation; documentation |
| **Documentation** | Audit-ready file; calculation workings; election register |

**Key points:**
- Pillar Two is an **ongoing annual process**, not a one-time project
- **Cross-functional collaboration** (Tax, Finance, IT, HR) is essential
- **Technology investment** scales with group complexity
- **Governance and controls** must be proportionate and embedded
- **Documentation** is critical for audit defence

---

## Integration with GIR Tools

The ongoing compliance process integrates with the GIR tool suite:

```
COMPLIANCE PROCESS TOOL INTEGRATION

Phase 1: Planning
└── GIR-005 DFE Assessment Tool → Confirm filing entity

Phase 2: Safe Harbour Assessment
└── GIR-002 Safe Harbour Qualifier → Test all jurisdictions

Phase 3: Calculations
└── GIR-001 GloBE Calculator → ETR, SBIE, Top-up Tax

Phase 4: Filing Preparation
├── GIR-003 Filing Deadline Calculator → Confirm deadlines
├── GIR-004 GIR Practice Form → Complete GIR
└── GIR-006 Audit File Checklist → Documentation

Phase 5: Ongoing Monitoring
└── Bookmark OECD Central Record → Monitor guidance updates
```

---

## Next Step

You have learned how to establish and manage an ongoing Pillar Two compliance process. Proceed to **Case Study 7: Stratos's First GIR Filing** to apply all Part 7 concepts in a comprehensive end-to-end exercise covering GIR preparation, Safe Harbour testing, and filing procedures.
