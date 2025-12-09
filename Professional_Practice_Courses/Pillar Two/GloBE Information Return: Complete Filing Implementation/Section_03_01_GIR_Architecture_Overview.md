# Section 3: Understanding the GIR Structure

## 3.1 GIR Architecture Overview

**Estimated Reading Time:** 20 minutes
**Pages:** 8-10

---

## Learning Objectives for This Section

By the end of this section, you will be able to:

- Explain the three-section architecture of the GIR and how sections relate to each other
- Identify data dependencies between GIR sections
- Determine whether to file a single centralized GIR or multiple local GIRs
- Describe the five core elements of the OECD XML schema
- Map GIR sections to their corresponding XML schema elements

---

## The Three-Section Architecture

The GloBE Information Return (GIR) is organized into **three main sections**, each serving a distinct purpose in the overall filing. Understanding how these sections work together is essential before you begin data collection and completion.

**Structural Note:** The current three-section structure was established in the OECD's January 2025 GIR Template and XML Schema. Earlier consultation documents used a different four-section structure—ensure you reference the January 2025 version for accurate section numbering.

---

### High-Level Section Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       GloBE INFORMATION RETURN STRUCTURE                     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  SECTION 1: MNE GROUP INFORMATION                                           │
│  ─────────────────────────────────                                          │
│  • Filed ONCE per GIR                                                       │
│  • ~50+ data points (base)                                                  │
│  • Identifies WHO you are and HOW you're structured                         │
│                                                                              │
│  Contains:                                                                   │
│  ├── Filing Constituent Entity identification                               │
│  ├── Ultimate Parent Entity information                                     │
│  ├── Corporate structure (all constituent entities)                         │
│  └── Summary information (ETR ranges by jurisdiction)                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Provides foundation for
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  SECTION 2: JURISDICTIONAL SAFE HARBOURS AND EXCLUSIONS                     │
│  ──────────────────────────────────────────────────────                     │
│  • Filed ONCE per jurisdiction where safe harbour applies                   │
│  • Variable data points (depends on elections)                              │
│  • Documents WHERE simplified reporting applies                             │
│                                                                              │
│  Contains:                                                                   │
│  ├── Transitional CbCR Safe Harbour elections                               │
│  ├── QDMTT Safe Harbour elections                                           │
│  ├── Transitional UTPR Safe Harbour elections                               │
│  └── Jurisdictional exclusions documentation                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Determines which jurisdictions require
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  SECTION 3: GloBE COMPUTATIONS                                              │
│  ─────────────────────────────                                              │
│  • Filed for EACH jurisdiction (where safe harbour does NOT apply)          │
│  • ~400 data points (scales with jurisdictions and entities)                │
│  • Calculates WHAT you owe and WHERE                                        │
│                                                                              │
│  Contains:                                                                   │
│  ├── ETR computation (GloBE Income/Loss, Covered Taxes)                     │
│  ├── Substance-Based Income Exclusion (SBIE) calculation                    │
│  ├── Top-up Tax computation                                                 │
│  └── Top-up Tax allocation (IIR, UTPR, QDMTT)                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Section Relationship Summary

| Section | Scope | Repetition | Data Points | Key Question |
|---------|-------|------------|-------------|--------------|
| **Section 1** | MNE Group | Once per GIR | ~50+ base | Who are we and how are we structured? |
| **Section 2** | Per jurisdiction | Once per safe harbour election | Variable | Where can we use simplified reporting? |
| **Section 3** | Per jurisdiction | Once per non-excluded jurisdiction | ~400+ (scales) | What is our ETR and top-up tax? |

---

## Data Dependencies Between Sections

Understanding data dependencies is critical for planning your GIR completion workflow. Sections do not stand alone—data flows between them and must be consistent.

### Section Dependency Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATA DEPENDENCY FLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

        ┌──────────────────────────────────────────────────────────┐
        │                     SECTION 1                             │
        │              MNE Group Information                        │
        │                                                           │
        │  Outputs:                                                 │
        │  • Constituent Entity list (all entities)                 │
        │  • Jurisdiction list (all operating jurisdictions)        │
        │  • QIIR/UTPR applicability indicators                     │
        │  • Filing CE and UPE identification                       │
        └──────────────────────────┬───────────────────────────────┘
                                   │
                                   │ Feeds entity and
                                   │ jurisdiction data to
                                   ▼
        ┌──────────────────────────────────────────────────────────┐
        │                     SECTION 2                             │
        │       Jurisdictional Safe Harbours and Exclusions        │
        │                                                           │
        │  Receives:                                                │
        │  • Jurisdiction list from Section 1                       │
        │                                                           │
        │  Determines:                                              │
        │  • Which jurisdictions are excluded from Section 3        │
        │  • Which safe harbours apply per jurisdiction             │
        │                                                           │
        │  Outputs:                                                 │
        │  • List of excluded jurisdictions                         │
        │  • List of jurisdictions requiring full computation       │
        └──────────────────────────┬───────────────────────────────┘
                                   │
                                   │ Determines scope of
                                   │ Section 3 reporting
                                   ▼
        ┌──────────────────────────────────────────────────────────┐
        │                     SECTION 3                             │
        │                 GloBE Computations                        │
        │                                                           │
        │  Receives:                                                │
        │  • Constituent entities per jurisdiction (from Section 1) │
        │  • Safe harbour status per jurisdiction (from Section 2)  │
        │                                                           │
        │  Computes (for non-excluded jurisdictions):               │
        │  • GloBE Income/Loss                                      │
        │  • Adjusted Covered Taxes                                 │
        │  • ETR by jurisdiction                                    │
        │  • SBIE amounts                                           │
        │  • Top-up Tax amounts                                     │
        │  • Top-up Tax allocation                                  │
        │                                                           │
        │  Feeds back to Section 1:                                 │
        │  • ETR range summary by jurisdiction                      │
        └──────────────────────────────────────────────────────────┘
```

---

### Critical Data Consistency Points

Data must be consistent across sections. The following table identifies key fields that must reconcile:

| Section 1 Field | Must Match | Related Field |
|-----------------|------------|---------------|
| **Jurisdiction list** (Section 1.3) | → | Section 2 and 3 jurisdictions |
| **Constituent Entity count** (Section 1.3) | → | Entities reported in Section 3 |
| **ETR range summary** (Section 1.4) | ← | Computed ETR from Section 3 |
| **QIIR indicators** (Section 1.3) | → | IIR allocation in Section 3.4 |
| **UTPR indicators** (Section 1.3) | → | UTPR allocation in Section 3.4 |

**Warning:** The OECD XML schema and tax authority validation systems will check for consistency across sections. Mismatches will generate validation errors.

---

### Data Computation Sequence

Because of these dependencies, complete the GIR sections in this order:

```
RECOMMENDED COMPLETION SEQUENCE
───────────────────────────────

Step 1: SECTION 1.1-1.3 (Core Group Information)
        ├── Filing CE identification
        ├── UPE identification
        └── Complete constituent entity database
              │
              ▼
Step 2: SECTION 2 (Safe Harbour Determination)
        ├── Evaluate each jurisdiction for safe harbour eligibility
        ├── Document elections
        └── Identify excluded vs. full-computation jurisdictions
              │
              ▼
Step 3: SECTION 3 (GloBE Computations)
        ├── Complete Section 3 for each non-excluded jurisdiction
        ├── Calculate ETR, SBIE, Top-up Tax
        └── Determine allocation (IIR, UTPR, QDMTT)
              │
              ▼
Step 4: SECTION 1.4 (Summary - Complete Last)
        ├── Populate ETR range by jurisdiction (from Section 3)
        └── Complete high-level summary fields
```

**Key Insight:** Section 1.4 (Summary) should be completed **last** because it requires ETR data from Section 3 calculations.

---

## Filing Structure: Single vs. Multiple GIRs

One of the most important architectural decisions is whether to file a **single centralized GIR** or **multiple local GIRs**.

### Single Centralized GIR (Recommended)

The OECD designed the GIR system to enable **central filing**, reducing compliance burden for MNE groups.

**How It Works:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SINGLE GIR FILING (Centralized)                          │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────────────────┐
                    │   DESIGNATED FILING ENTITY       │
                    │   (or UPE)                       │
                    │                                  │
                    │   Files single, comprehensive    │
                    │   GIR covering all jurisdictions │
                    └──────────────────┬───────────────┘
                                       │
                                       │ Files GIR
                                       ▼
                    ┌──────────────────────────────────┐
                    │   TAX AUTHORITY                  │
                    │   (DFE/UPE jurisdiction)         │
                    │                                  │
                    │   Receives complete GIR          │
                    └──────────────────┬───────────────┘
                                       │
                                       │ Exchanges relevant sections via
                                       │ Qualifying Competent Authority Agreement (QCAA)
                                       ▼
        ┌──────────────┬──────────────┬──────────────┬──────────────┐
        │              │              │              │              │
        ▼              ▼              ▼              ▼              ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │Country A│   │Country B│   │Country C│   │Country D│   │Country E│
   │   Tax   │   │   Tax   │   │   Tax   │   │   Tax   │   │   Tax   │
   │Authority│   │Authority│   │Authority│   │Authority│   │Authority│
   └─────────┘   └─────────┘   └─────────┘   └─────────┘   └─────────┘

   Each receives: General information + sections relevant to their taxing rights
```

**Requirements for Single GIR Filing:**

| Requirement | Description |
|-------------|-------------|
| **Designated Filing Entity (DFE)** | One entity designated to file on behalf of the group |
| **QCAA in Place** | Qualifying Competent Authority Agreement between jurisdictions |
| **DFE Jurisdiction** | DFE must be in a jurisdiction with implemented exchange framework |
| **Notification to Local Authorities** | Local constituent entities must notify their tax authority of DFE election |

**Benefits of Single GIR:**

- One filing instead of multiple
- Consistent data across all jurisdictions
- Centralized control and review
- Reduced coordination complexity
- Single point of amendment if errors found

---

### Multiple Local GIRs

Without centralized filing mechanisms, each constituent entity would need to file locally.

**When Multiple GIRs May Be Required:**

| Scenario | Consequence |
|----------|-------------|
| No DFE election | Each CE files in its jurisdiction |
| No QCAA between jurisdictions | Affected jurisdictions require local filing |
| DFE files late | Local filing obligations triggered |
| Jurisdiction does not accept exchange | Local filing required |

**Multiple GIR Structure:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MULTIPLE GIR FILING (Decentralized)                      │
└─────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
   │     CE A    │   │     CE B    │   │     CE C    │   │     CE D    │
   │  (Country A)│   │  (Country B)│   │  (Country C)│   │  (Country D)│
   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
          │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼
   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
   │   GIR for   │   │   GIR for   │   │   GIR for   │   │   GIR for   │
   │  Country A  │   │  Country B  │   │  Country C  │   │  Country D  │
   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
          │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼
   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
   │ Country A   │   │ Country B   │   │ Country C   │   │ Country D   │
   │    Tax      │   │    Tax      │   │    Tax      │   │    Tax      │
   │  Authority  │   │  Authority  │   │  Authority  │   │  Authority  │
   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

**Implications of Multiple GIR Filing:**

- Increased compliance burden (multiple filings)
- Risk of data inconsistencies between filings
- Multiple deadlines to track
- Multiple portals and procedures to manage
- Higher potential for errors

---

### Filing Structure Decision Matrix

| Factor | Single GIR | Multiple GIRs |
|--------|------------|---------------|
| **QCAA Status** | QCAA in place | No QCAA or gaps |
| **Complexity** | Lower | Higher |
| **Cost** | Lower | Higher |
| **Consistency Risk** | Lower | Higher |
| **DFE Requirement** | Yes | No |
| **Local Notification** | Yes | Not applicable |

**Recommendation:** File a single centralized GIR through a Designated Filing Entity wherever possible. This is the OECD's intended design and reduces compliance burden significantly.

---

## XML Schema Structure

The OECD XML Schema (January 2025) provides the technical framework for GIR data submission. Understanding this structure helps you map your GIR data correctly.

### Five Core XML Elements

The GloBE Body element comprises **five main elements**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OECD XML SCHEMA STRUCTURE (January 2025)                 │
└─────────────────────────────────────────────────────────────────────────────┘

GlobeBody
    │
    ├── 1. FilingInfo (Required)
    │       ├── Filing Constituent Entity identification
    │       ├── MNE Group identification
    │       ├── Accounting information
    │       └── Reporting Fiscal Year
    │
    ├── 2. GeneralSection (Optional - Mandatory)
    │       ├── Corporate structure information
    │       ├── All constituent entities
    │       └── Ownership chains
    │
    ├── 3. Summary (Optional, Repeatable)
    │       ├── Corresponds to GIR Section 1.4
    │       ├── High-level ETR ranges
    │       └── Summary by jurisdiction
    │
    ├── 4. JurisdictionSection (Optional, Repeatable)
    │       ├── Corresponds to GIR Sections 2 and 3
    │       ├── Safe harbour elections
    │       └── GloBE computations by jurisdiction
    │
    └── 5. Subgroup (Repeatable)
            └── Used when GloBE calculations apply to subgroups
```

---

### XML Element to GIR Section Mapping

| XML Element | GIR Section(s) | Purpose |
|-------------|----------------|---------|
| **FilingInfo** | Header information | Identifies who is filing, for which group, which fiscal year |
| **GeneralSection** | Section 1.1, 1.2, 1.3 | Filing CE, UPE, and corporate structure |
| **Summary** | Section 1.4 | High-level summary information by jurisdiction |
| **JurisdictionSection** | Section 2 + Section 3 | Safe harbours, exclusions, and GloBE computations |
| **Subgroup** | (Special cases) | Calculations at subgroup level |

---

### XML Element Details

#### 1. FilingInfo Element (Required)

**Purpose:** Identifies the filing entity, MNE group, and reporting period.

| Field | Description | Format |
|-------|-------------|--------|
| **FilingCE** | Filing Constituent Entity | TIN, Name, Jurisdiction |
| **MNEGroup** | MNE Group identification | UPE name, TIN, Jurisdiction |
| **AccountingInfo** | Accounting standard, currency | GAAP type, ISO currency code |
| **ReportingFY** | Fiscal year start and end | YYYY-MM-DD format |

---

#### 2. GeneralSection Element (Optional but Mandatory for Complete Filing)

**Purpose:** Contains the corporate structure of the MNE group.

| Component | Description | Notes |
|-----------|-------------|-------|
| **ConstituentEntityList** | All entities in the group | Entity name, TIN, jurisdiction, GloBE status |
| **OwnershipInfo** | Ownership percentages | Direct and indirect ownership |
| **QIIRIndicators** | Which entities apply QIIR | By entity |
| **UTPRIndicators** | Which entities apply UTPR | By entity |

**Recipient Jurisdictions:** The GeneralSection indicates which jurisdictions should receive this data via exchange.

---

#### 3. Summary Element (Optional, Repeatable)

**Purpose:** Provides high-level summary by jurisdiction.

| Component | Description | Source |
|-----------|-------------|--------|
| **JurisdictionName** | ISO 2-character country code | ISO 3166-1 Alpha-2 |
| **ETRRange** | ETR banding (2.5% increments) | Computed from Section 3 |
| **SafeHarbourIndicator** | Whether safe harbour applies | From Section 2 |
| **TopUpTaxSummary** | Summary top-up tax | Computed from Section 3 |

**Note:** The Summary element corresponds to GIR Section 1.4 and is populated **after** Section 3 calculations are complete.

---

#### 4. JurisdictionSection Element (Optional, Repeatable)

**Purpose:** Contains safe harbour elections and full GloBE computations for each jurisdiction.

| Component | Corresponds To | Content |
|-----------|----------------|---------|
| **SafeHarbours** | GIR Section 2 | Transitional CbCR, QDMTT, UTPR safe harbour elections |
| **GlobeComputation** | GIR Section 3 | ETR computation, SBIE, Top-up Tax, allocation |

This element is repeated for each jurisdiction where the MNE group has operations.

**Conditional Reporting:** Sections 3.1.5 to 3.1.10 do not need to be reported if:
- Only a single jurisdiction is reported as having taxing rights in Section 3.1.4, OR
- The QDMTT Safe Harbour applies with respect to the jurisdiction or subgroup

---

#### 5. Subgroup Element (Repeatable)

**Purpose:** Used when the GloBE calculation perimeter is a subgroup rather than the full MNE group.

| Use Case | Application |
|----------|-------------|
| Joint Ventures | Separate GloBE calculations for JV groups |
| Minority-Owned Parent Entities | MOPE subgroup calculations |
| Multi-Parented MNE Groups | Separate calculations per subgroup |

---

### Key XML Technical Requirements

| Requirement | Specification | Example |
|-------------|---------------|---------|
| **Character Encoding** | UTF-8 | Standard for all files |
| **Country Codes** | ISO 3166-1 Alpha-2 | "GB" for United Kingdom |
| **Currency Codes** | ISO 4217 | "EUR", "USD", "GBP" |
| **TIN Format** | Jurisdiction-specific | Use "NOTIN" if no TIN issued |
| **Date Format** | YYYY-MM-DD | 2024-12-31 |
| **Percentage Format** | Decimal (0 to 1) | 0.15 = 15% |
| **Decimal Precision** | Per field specification | Max 4 decimal places for percentages |

---

## GIR Section Relationship Flowchart

The following comprehensive flowchart shows how all components work together:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE GIR ARCHITECTURE FLOWCHART                      │
└─────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────────────┐
                         │      MNE GROUP          │
                         │  (€750M+ consolidated   │
                         │       revenue)          │
                         └───────────┬─────────────┘
                                     │
                         ┌───────────▼─────────────┐
                         │   DESIGNATED FILING     │
                         │        ENTITY           │
                         │   (or UPE if no DFE)    │
                         └───────────┬─────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
         ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
         │ SECTION 1    │  │ SECTION 2    │  │ SECTION 3    │
         │ MNE GROUP    │  │ SAFE         │  │ GloBE        │
         │ INFORMATION  │  │ HARBOURS     │  │ COMPUTATIONS │
         └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
                │                 │                 │
    ┌───────────┴───────────┐     │     ┌───────────┴───────────┐
    │                       │     │     │                       │
    ▼                       ▼     ▼     ▼                       ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│ 1.1   │ │ 1.2   │ │ 1.3   │ │ 2.1   │ │ 3.1   │ │ 3.2   │ │ 3.3   │
│Filing │ │  UPE  │ │Corp.  │ │Safe   │ │  ETR  │ │ SBIE  │ │Top-up │
│  CE   │ │ Info  │ │Struct │ │Harb.  │ │Comp.  │ │       │ │ Tax   │
└───────┘ └───────┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
                        │         │         │         │         │
                        │         │         └─────────┴─────────┘
                        │         │                   │
                        │         │         ┌─────────┴─────────┐
                        │         │         ▼                   ▼
                        │         │    ┌─────────┐        ┌─────────┐
                        │         │    │  3.4    │        │  1.4    │
                        │         │    │ Alloc.  │        │ Summary │
                        │         │    │(IIR/    │        │  (ETR   │
                        │         │    │ UTPR)   │        │ Ranges) │
                        │         │    └────┬────┘        └────┬────┘
                        │         │         │                  │
                        └─────────┴─────────┴──────────────────┘
                                            │
                                            ▼
                              ┌─────────────────────────┐
                              │     XML GENERATION      │
                              │  (January 2025 Schema)  │
                              └───────────┬─────────────┘
                                          │
                              ┌───────────▼─────────────┐
                              │     XML VALIDATION      │
                              │  • Schema validation    │
                              │  • Business rules       │
                              │  • Consistency checks   │
                              └───────────┬─────────────┘
                                          │
                              ┌───────────▼─────────────┐
                              │        FILING           │
                              │  • Tax authority portal │
                              │  • Confirmation receipt │
                              │  • Exchange to other    │
                              │    jurisdictions        │
                              └─────────────────────────┘
```

---

## Information Exchange Architecture

When a centralized GIR is filed, different sections are exchanged to different recipients:

### What Each Jurisdiction Receives

| Recipient Type | Sections Received | Purpose |
|----------------|-------------------|---------|
| **All Implementing Jurisdictions** (where CEs located) | General Section + Corporate Structure | Verify entity presence and taxing rights |
| **Jurisdictions with Taxing Rights** | Section 3 (ETR, Top-up Tax, Allocation) | Verify top-up tax calculations |
| **UPE Jurisdiction** (if different from DFE) | Full GIR | Complete oversight |
| **UTPR Jurisdictions** | Section 3.4 (UTPR Allocation) | Verify UTPR amounts |

---

### Exchange Mechanism

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INFORMATION EXCHANGE ARCHITECTURE                        │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────────────────┐
                    │         FILED GIR                 │
                    │   (with DFE jurisdiction)         │
                    └──────────────────┬───────────────┘
                                       │
                        ┌──────────────┴──────────────┐
                        │     EXCHANGE SYSTEM          │
                        │  (Qualifying Competent       │
                        │   Authority Agreement)       │
                        └──────────────┬──────────────┘
                                       │
            ┌──────────────────────────┼──────────────────────────┐
            │                          │                          │
            ▼                          ▼                          ▼
   ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
   │  Implementing   │      │  Taxing Rights  │      │  UPE            │
   │  Jurisdictions  │      │  Jurisdictions  │      │  Jurisdiction   │
   │                 │      │                 │      │                 │
   │  Receives:      │      │  Receives:      │      │  Receives:      │
   │  • GeneralSect. │      │  • GeneralSect. │      │  • Full GIR     │
   │  • Corp. Struct.│      │  • Corp. Struct.│      │                 │
   │                 │      │  • Section 3    │      │                 │
   └─────────────────┘      └─────────────────┘      └─────────────────┘
```

---

## Section 3.1 Summary: Architecture Checklist

Before proceeding to the detailed section-by-section guidance, confirm you understand:

| Concept | Checkpoint |
|---------|------------|
| **Three-section structure** | Can identify purpose of Sections 1, 2, and 3 |
| **Data dependencies** | Understand that Section 1.4 depends on Section 3 calculations |
| **Filing structure** | Know whether single GIR (via DFE) or multiple local GIRs apply |
| **XML schema elements** | Can map GIR sections to FilingInfo, GeneralSection, Summary, JurisdictionSection |
| **Completion sequence** | Know to complete Section 1.4 last (after Section 3) |
| **Exchange mechanism** | Understand what sections go to which jurisdictions |

---

## Next Steps

You now understand the overall GIR architecture and how the three sections relate to each other. The following subsections will provide detailed guidance on completing each GIR section with specific data requirements, examples, and templates.

---

## Sources and References

This section incorporates information from:

- [OECD GloBE Information Return (Pillar Two) XML Schema (January 2025)](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html)
- [OECD GIR XML Schema PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/01/globe-information-return-pillar-two-xml-schema_3980638f/c594935a-en.pdf)
- [OECD Tax Challenges Arising from the Digitalisation of the Economy – GloBE Information Return (January 2025)](https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html)
- [OECD Draft User Guide for the GloBE Information Return XML Schema](https://www.oecd.org/en/events/public-consultations/2024/07/draft-user-guide-for-the-globe-information-return-xml-schema.html)
- [KPMG - Pillar Two: GloBE Information Return](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/07/pillar-two-globe-information-return.pdf)
- [EY - OECD releases new documents on GloBE Information Return](https://globaltaxnews.ey.com/news/2025-0289-oecd-releases-new-documents-on-globe-information-return)
- [Loyens & Loeff - GloBE Information Return](https://www.loyensloeff.com/insights/news--events/news/globe-information-return/)
- [Wolters Kluwer - Overcoming challenges in preparing GloBE Information Return](https://www.wolterskluwer.com/en-au/expert-insights/overcoming-challenges-in-preparing-for-beps-pillar-two)
- [oecdpillars.com - A Review of Changes in the OECD's Updated January 2025 GloBE Information Return](https://oecdpillars.com/a-review-of-changes-in-the-oecds-updated-january-2025-globe-information-return/)
- [Citco - Pillar 2 update: getting to grips with the GloBE Information Return](https://www.citco.com/insights/pillar-2-update-getting-to-grips-with-the-globe-information-return)

---

*End of Section 3.1*
