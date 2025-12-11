# Chapter 7.1: GloBE Information Return Overview

## Learning Objective

After completing this chapter, you will be able to identify who must file a GloBE Information Return, determine filing deadlines and notification requirements, understand the central filing mechanism and Designated Filing Entity role, and navigate the key sections of the GIR structure.

---

## Key References

**OECD GloBE Model Rules:**
- Article 8.1.1 — Filing obligation for Constituent Entities
- Article 8.1.2 — Central filing exemption
- Article 8.1.3 — Notification requirements
- Article 8.1.4 — Information to be included in GIR
- Article 8.1.5 — Timing of filing
- Article 8.1.6 — Currency requirements

**Administrative Guidance:**
- July 2023: GloBE Information Return structure
- December 2023: Filing deadline clarifications (first GIR due 30 June 2026)
- January 2025: Updated GIR XML Schema and MCAA

**OECD Publications:**
- GloBE Information Return (July 2023, updated January 2025)
- GIR Multilateral Competent Authority Agreement (MCAA)

---

## What Is the GloBE Information Return?

The **GloBE Information Return (GIR)** is a standardised return that provides tax administrations with the information needed to evaluate an MNE Group's Pillar Two calculations.

```
┌─────────────────────────────────────────────────────────────────────┐
│ GIR PURPOSE                                                         │
│                                                                     │
│ The GIR enables tax authorities to:                                 │
│                                                                     │
│ → Verify ETR calculations by jurisdiction                          │
│ → Confirm Top-Up Tax amounts                                        │
│ → Understand group structure and ownership                         │
│ → Assess QDMTT, IIR, and UTPR liabilities                          │
│ → Exchange information with other jurisdictions                    │
│                                                                     │
│ KEY PRINCIPLE:                                                      │
│ One standardised return → Multiple tax authorities                 │
│ Filed once centrally → Exchanged automatically                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Who Must File? *(Article 8.1.1)*

### Default Rule: Every Constituent Entity

Under Article 8.1.1, **each Constituent Entity** located in an implementing jurisdiction must file a GIR with its local tax administration.

```
DEFAULT FILING OBLIGATION

MNE Group
├── UPE (UK) ────────────────► Files GIR with HMRC
├── SubCo A (Germany) ───────► Files GIR with BZSt
├── SubCo B (France) ────────► Files GIR with DGFiP
├── SubCo C (Ireland) ───────► Files GIR with Revenue
└── SubCo D (Singapore) ─────► Files GIR with IRAS

Result: 5 separate GIR filings
```

### Central Filing Exception *(Article 8.1.2)*

The local filing obligation **does not apply** if:

1. The **UPE** or a **Designated Filing Entity (DFE)** files the GIR centrally, AND
2. A **Qualifying Competent Authority Agreement (QCAA)** is in place to exchange GIR information with the Constituent Entity's jurisdiction

```
CENTRAL FILING MECHANISM

MNE Group
├── UPE (UK) ──────► Files GIR centrally with HMRC
│                          │
│                    QCAA Exchange
│                          │
│                    ┌─────▼─────┐
│                    │  Germany  │
│                    │  France   │
│                    │  Ireland  │
│                    │ Singapore │
│                    └───────────┘
│
├── SubCo A (Germany) ───► No local filing (QCAA in place)
├── SubCo B (France) ────► No local filing (QCAA in place)
├── SubCo C (Ireland) ───► No local filing (QCAA in place)
└── SubCo D (Singapore) ─► No local filing (QCAA in place)

Result: 1 central GIR filing, exchanged automatically
```

**Key benefit:** Central filing dramatically reduces compliance burden — one filing instead of potentially dozens.

---

## Designated Filing Entity (DFE)

### What Is a DFE?

A **Designated Filing Entity** is a Constituent Entity appointed by the MNE Group to file the GIR on behalf of all Group members.

### Who Can Be the DFE?

| Eligible Entity | Requirements |
|-----------------|--------------|
| **UPE** | Default filer if located in implementing jurisdiction |
| **Any Constituent Entity** | If UPE is not in implementing jurisdiction, any CE can be designated |
| **Surrogate Parent Entity** | If appointed under local rules |

### DFE Appointment Process

```
DFE APPOINTMENT WORKFLOW

Step 1: Identify potential DFE
        → Usually UPE or major intermediate holding company
        → Must be in jurisdiction with QCAA coverage

Step 2: Notify local tax authorities
        → Each CE notifies its tax authority of DFE appointment
        → Notification deadline: typically 3 months before GIR due date

Step 3: DFE files GIR centrally
        → Single filing with DFE's tax authority
        → Tax authority exchanges via QCAA

Step 4: Exchange occurs automatically
        → Other jurisdictions receive relevant sections
        → No action required from other CEs
```

---

## Notification Requirements *(Article 8.1.3)*

### When Is Notification Required?

Each Constituent Entity must **notify** its local tax authority:

| Notification Type | Content | Deadline |
|-------------------|---------|----------|
| **DFE Notification** | Identity of the entity filing the GIR | Typically **3 months** before GIR due date |
| **QCAA Reliance** | Confirmation that QCAA exchange will occur | Same as above |
| **Local Filing** | If filing locally (no QCAA), confirm local filing | Per local rules |

### What Happens Without Notification?

```
FAILURE TO NOTIFY

If CE does not notify local tax authority:
→ Local filing obligation remains
→ CE must file full GIR locally
→ Potential duplicate filings
→ Penalties may apply for late/non-filing
```

### Country-Specific Notification Deadlines

| Jurisdiction | Notification Deadline |
|--------------|----------------------|
| Ireland | 3 months before GIR due date |
| Spain | 3 months before GIR due date |
| South Africa | 6 months before first submission deadline |
| UK | Per HMRC guidance (typically 3 months) |

---

## Filing Deadlines *(Article 8.1.5)*

### Standard Deadline: 15 Months

The GIR must be filed within **15 months** after the end of the Fiscal Year.

### First Year Extension: 18 Months

For the **first Fiscal Year** that Pillar Two applies, the deadline is extended to **18 months**.

```
FILING DEADLINE EXAMPLES

Fiscal Year End: 31 December 2024 (first year)
Standard deadline: 31 March 2026 (15 months)
First-year extension: 30 June 2026 (18 months)
→ Actual deadline: 30 June 2026

Fiscal Year End: 31 December 2025 (second year)
Standard deadline: 31 March 2027 (15 months)
→ Actual deadline: 31 March 2027
```

### First GIR Filing: 30 June 2026

Per December 2023 Administrative Guidance, the **earliest due date** for GIR filing is **30 June 2026**.

| Fiscal Year End | First Year? | Deadline |
|-----------------|-------------|----------|
| 31 Dec 2024 | Yes | **30 June 2026** |
| 31 March 2025 | Yes | 30 September 2026 |
| 30 June 2025 | Yes | 31 December 2026 |
| 31 Dec 2025 | No | 31 March 2027 |

---

## GIR Structure Overview

The GIR is organised into distinct sections, with different sections shared with different tax authorities:

### Section Overview

| Section | Content | Shared With |
|---------|---------|-------------|
| **General Information** | Group identification, fiscal year, UPE details | All implementing jurisdictions |
| **Corporate Structure** | Ownership chain, CE list, jurisdictions | All implementing jurisdictions |
| **ETR Computation** | Jurisdictional ETR calculations, GloBE Income, Covered Taxes | Jurisdictions with taxing rights |
| **Top-Up Tax** | QDMTT, IIR, UTPR amounts by jurisdiction | Jurisdictions with taxing rights |
| **Elections** | GloBE elections made (SBIE, De Minimis, etc.) | Relevant jurisdictions |
| **Safe Harbours** | Transitional safe harbour claims | Relevant jurisdictions |

### Information Flow

```
GIR INFORMATION EXCHANGE

                    ┌─────────────────────────┐
                    │  COMPLETE GIR           │
                    │  (All sections)         │
                    │                         │
                    │  Received by:           │
                    │  → UPE jurisdiction     │
                    └───────────┬─────────────┘
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
┌───────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ ETR + Top-Up Tax  │ │ ETR + Top-Up Tax│ │ General +       │
│ Sections          │ │ Sections        │ │ Structure only  │
│                   │ │                 │ │                 │
│ Received by:      │ │ Received by:    │ │ Received by:    │
│ → Taxing rights   │ │ → Taxing rights │ │ → All other     │
│   jurisdictions   │ │   jurisdictions │ │   implementing  │
│   (IIR/UTPR/QDMTT)│ │   (IIR/UTPR/    │ │   jurisdictions │
└───────────────────┘ │    QDMTT)       │ └─────────────────┘
                      └─────────────────┘
```

---

## Key GIR Data Elements

### General Information Section

| Data Element | Description |
|--------------|-------------|
| MNE Group name | Legal name of the Group |
| UPE identification | Name, jurisdiction, tax ID |
| Fiscal year | Start and end dates |
| Reporting currency | Currency used in GIR |
| DFE identification | If different from UPE |

### Corporate Structure Section

| Data Element | Description |
|--------------|-------------|
| Constituent Entity list | All CEs with jurisdiction and tax ID |
| Ownership percentages | Direct and indirect ownership |
| Entity classification | UPE, IPE, POPE, MOCE, JV, etc. |
| Excluded Entities | Identified with exclusion basis |

### ETR Computation Section

| Data Element | Description |
|--------------|-------------|
| GloBE Income by jurisdiction | Aggregated jurisdictional income |
| Adjusted Covered Taxes | By jurisdiction |
| ETR calculation | Income ÷ Taxes |
| SBIE computation | Payroll and asset carve-outs |
| Excess Profit | GloBE Income less SBIE |
| Top-Up Tax Percentage | 15% minus ETR |

### Top-Up Tax Section

| Data Element | Description |
|--------------|-------------|
| Jurisdictional Top-Up Tax | Per low-taxed jurisdiction |
| QDMTT amounts | By jurisdiction |
| IIR allocation | To UPE/IPE |
| UTPR allocation | By jurisdiction |
| Total Top-Up Tax | Group-wide summary |

---

## Stratos Worked Example: GIR Filing Strategy

### Background

Stratos Holdings plc (UK) must determine its GIR filing strategy for FY 2025 (year ending 31 December 2025).

### Group Structure (Post-TechStart Acquisition)

```
Stratos Holdings plc (UK) — UPE
├── SG Germany GmbH (Germany)
├── SG Singapore Pte Ltd (Singapore)
├── SG Ireland Ltd (Ireland)
├── SG Luxembourg S.à r.l. (Luxembourg)
├── Atlas Ireland Ltd (Ireland) — 28% MOCE
└── TechStart Inc. (USA)
    ├── TechStart UK Ltd (UK)
    ├── TechStart GmbH (Germany)
    ├── TechStart JV Pte Ltd (Singapore) — 55% JV
    ├── TechStart IP LLC (USA)
    └── TechStart Ventures Fund (Cayman)
```

### Step 1: Identify Filing Options

| Option | Description | Filings Required |
|--------|-------------|------------------|
| **A: Local Filing** | Each CE files locally | 11+ separate filings |
| **B: Central Filing (UPE)** | Stratos plc files for all | 1 filing (if QCAA covers all) |
| **C: Central Filing (DFE)** | Designate another CE | 1 filing (if QCAA covers all) |

### Step 2: Assess QCAA Coverage

| Jurisdiction | QCAA with UK? | Central Filing Available? |
|--------------|---------------|---------------------------|
| Germany | Yes (EU MCAA) | ✓ |
| Singapore | Expected | ✓ |
| Ireland | Yes (EU MCAA) | ✓ |
| Luxembourg | Yes (EU MCAA) | ✓ |
| USA | Expected | ✓ |
| Cayman | TBD | Potentially local filing |

**Issue:** Cayman may not have QCAA with UK. If not, TechStart Ventures Fund may require local filing (if Cayman implements Pillar Two).

### Step 3: Determine Filing Strategy

**Recommended Approach:** Central filing via Stratos Holdings plc (UPE)

| Element | Decision |
|---------|----------|
| **DFE** | Stratos Holdings plc (UK) |
| **Filing jurisdiction** | UK (HMRC) |
| **Notification required** | All CEs notify local authorities of UK central filing |
| **Local filings** | Cayman only (if no QCAA) |

### Step 4: Timeline for FY 2025

| Date | Action |
|------|--------|
| 31 Dec 2025 | Fiscal year end |
| 31 Dec 2026 | Notification deadline (3 months before GIR due) |
| 31 Mar 2027 | GIR filing deadline (15 months) |

### Step 5: GIR Content Summary

**Jurisdictions to Report:**

| Jurisdiction | GloBE Income (€) | ETR | Top-Up Tax (€) | Mechanism |
|--------------|------------------|-----|----------------|-----------|
| UK | 11,525,000 | 25.00% | 0 | — |
| Germany | 59,929,000 | 23.00% | 0 | — |
| USA | 12,300,400 | 15.49% | 0 | — |
| Singapore | 4,000,000 | 9.81% | 197,498 | IIR |
| Ireland | 15,000,000 | 11.80% | 426,394 | QDMTT |
| Luxembourg | — | — | 0 | De Minimis |
| Cayman | 2,016,000 | 1.00% | 280,480 | IIR |

**JV Reporting (Separate Section):**

| JV Jurisdiction | GloBE Income (€) | Top-Up Tax (€) | Stratos Share |
|-----------------|------------------|----------------|---------------|
| Singapore | 10,000,000 | 485,750 | 55% |
| Malaysia | 5,000,000 | 140,520 | 55% |

---

## Common Pitfalls

### Pitfall 1: Missing Notification Deadline

**Error:** Failing to notify local tax authorities of central filing arrangement.

**Consequence:** Local filing obligation remains; potential penalties.

**Correct approach:** Calendar notification deadlines (typically 3 months before GIR due) and file notifications proactively.

### Pitfall 2: Assuming QCAA Coverage

**Error:** Assuming all jurisdictions have QCAA with central filing jurisdiction.

**Consequence:** Local filing required but not prepared.

**Correct approach:** Verify QCAA status for each jurisdiction where CEs are located. Prepare local filings where QCAA not confirmed.

### Pitfall 3: Incomplete JV Reporting

**Error:** Omitting JV data from GIR because JV is "separate."

**Correct approach:** JVs require separate reporting within the GIR. Include JV Group calculations and allocation to parent entities.

### Pitfall 4: Currency Inconsistency

**Error:** Reporting different sections in different currencies.

**Correct approach:** GIR must be in a single **presentation currency** (typically Group reporting currency). Apply consistent exchange rates.

### Pitfall 5: First-Year Deadline Confusion

**Error:** Using 15-month deadline for first Pillar Two year.

**Correct approach:** First year has **18-month** deadline. For FY 2024 (Dec year-end), deadline is 30 June 2026, not 31 March 2026.

---

## GIR Filing Checklist

```
GIR FILING CHECKLIST
MNE Group: _________________________
Fiscal Year: _________________________
UPE Jurisdiction: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: FILING STRATEGY
═══════════════════════════════════════════════════════════════════════

□ Filing approach selected:
   □ Central filing (UPE files)
   □ Central filing (DFE files)
   □ Local filing (each CE files separately)

□ Designated Filing Entity (if applicable):
   Name: _________________________
   Jurisdiction: _________________________

□ QCAA coverage verified for all CE jurisdictions?        YES / NO

   Jurisdictions WITHOUT QCAA coverage:
   1. _________________________
   2. _________________________

   → Local filings required for above jurisdictions

═══════════════════════════════════════════════════════════════════════
SECTION B: NOTIFICATION
═══════════════════════════════════════════════════════════════════════

□ Notification deadline calculated:                  ___________________

□ Notifications filed with local authorities:

   | Jurisdiction | CE Name | Notification Filed? | Date |
   |--------------|---------|---------------------|------|
   | | | YES / NO | |
   | | | YES / NO | |
   | | | YES / NO | |

═══════════════════════════════════════════════════════════════════════
SECTION C: FILING DEADLINE
═══════════════════════════════════════════════════════════════════════

□ Fiscal year end date:                              ___________________

□ Is this the first Pillar Two year?                      YES / NO

□ Filing deadline:
   Standard (15 months):                             ___________________
   First-year extension (18 months):                 ___________________
   **Actual deadline:**                              ___________________

═══════════════════════════════════════════════════════════════════════
SECTION D: GIR CONTENT PREPARATION
═══════════════════════════════════════════════════════════════════════

□ General Information section complete?                   YES / NO
□ Corporate Structure section complete?                   YES / NO
□ ETR Computation by jurisdiction complete?               YES / NO
□ Top-Up Tax calculations complete?                       YES / NO
□ Elections documented?                                   YES / NO
□ Safe Harbour claims documented?                         YES / NO
□ JV reporting (if applicable) complete?                  YES / NO
□ MOCE reporting (if applicable) complete?                YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION E: QUALITY REVIEW
═══════════════════════════════════════════════════════════════════════

□ Currency consistency verified?                          YES / NO
□ Ownership percentages reconciled?                       YES / NO
□ ETR calculations cross-checked?                         YES / NO
□ Top-Up Tax totals reconciled?                           YES / NO
□ XML schema validation passed?                           YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION F: FILING CONFIRMATION
═══════════════════════════════════════════════════════════════════════

□ GIR filed with:                                    ___________________
□ Filing date:                                       ___________________
□ Filing confirmation/reference:                     ___________________

□ Local filings (if required):

   | Jurisdiction | Filed? | Date | Reference |
   |--------------|--------|------|-----------|
   | | YES / NO | | |
   | | YES / NO | | |
```

---

## Summary

The GloBE Information Return is the central compliance document for Pillar Two:

| Aspect | Key Rule |
|--------|----------|
| **Who files** | Each CE locally, OR UPE/DFE centrally (if QCAA in place) |
| **Deadline** | 15 months (18 months for first year) |
| **First GIR** | Due 30 June 2026 for Dec 2024 year-ends |
| **Notification** | Required ~3 months before filing (varies by jurisdiction) |
| **Content** | General info, structure, ETR, Top-Up Tax, elections, safe harbours |
| **Exchange** | Via QCAA — UPE jurisdiction gets full GIR; others get relevant sections |

**Key planning point:** Central filing via UPE or DFE significantly reduces compliance burden. Verify QCAA coverage early and file notifications on time.

---

## Integration with GIR Tools

The GIR structure aligns with GIR-001 GloBE Calculator outputs:

| GIR Section | GIR-001 Output |
|-------------|----------------|
| ETR Computation | Step 1: ETR by jurisdiction |
| SBIE | Step 2: Payroll and asset carve-outs |
| Top-Up Tax | Step 3: Jurisdictional Top-Up Tax |
| QDMTT/IIR | Step 3: Collection mechanism |

**Workflow:**
```
Step 1: Complete GIR-001 calculations for all jurisdictions
Step 2: Export data to GIR template
Step 3: Add corporate structure and general information
Step 4: Apply elections and safe harbour claims
Step 5: Validate against XML schema
Step 6: File centrally or locally as determined
```

---

## Next Step

You have learned the fundamentals of GloBE Information Return filing. Proceed to **Chapter 7.2: GIR Data Requirements** for detailed guidance on the specific data elements required for each section of the GloBE Information Return.
