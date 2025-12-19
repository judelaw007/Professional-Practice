# Chapter 7.2: GIR Data Requirements

## Learning Objective

After completing this chapter, you will be able to identify the key data elements required in each GIR section, understand the volume and complexity of data points for ETR and Top-Up Tax computations, navigate the XML schema structure, and prepare data collection processes to meet GIR requirements.

## Introduction

The GloBE Information Return demands an unprecedented volume and granularity of tax data from multinational groups. While the Top-Up Tax calculations themselves are conceptually complex, many groups discover that the practical challenge of populating the GIR exceeds the intellectual challenge of understanding the rules. A group with operations in seven jurisdictions and twelve entities faces roughly 1,500 individual data points—each requiring sourcing, validation, and reconciliation across multiple systems that were never designed with Pillar Two in mind.

This data challenge reflects a fundamental design tension within Pillar Two. The framework aims to measure something that accounting systems do not naturally track: the relationship between financial accounting profit and taxes actually paid, adjusted for timing differences, across every jurisdiction where a group operates. Consolidated financial statements aggregate; Pillar Two disaggregates. Local tax returns focus on taxable income; Pillar Two starts from accounting profit. Deferred tax follows local GAAP; Pillar Two imposes specific recast requirements. Every data point in the GIR represents a translation between systems with different purposes and conventions.

Understanding the GIR data structure is therefore essential preparation for Pillar Two compliance. Groups that map their data sources early, identify gaps and inconsistencies, and build collection processes into existing year-end procedures will manage the compliance burden far more effectively than those that attempt to compile GIR data on an ad hoc basis each year.

## 1. GIR Structure Overview

The GIR is organised into distinct sections, each requiring specific data elements:

```
┌─────────────────────────────────────────────────────────────────────┐
│ GIR STRUCTURE                                                       │
│                                                                     │
│ ┌─────────────────────────────────────────────────────────────────┐│
│ │ 1. FILING INFO                                                  ││
│ │    Filing CE identification, MNE Group, Fiscal Year             ││
│ └─────────────────────────────────────────────────────────────────┘│
│                              │                                      │
│ ┌─────────────────────────────────────────────────────────────────┐│
│ │ 2. GENERAL SECTION (Corporate Structure)                        ││
│ │    Ownership chain, CE list, Entity classifications             ││
│ └─────────────────────────────────────────────────────────────────┘│
│                              │                                      │
│ ┌─────────────────────────────────────────────────────────────────┐│
│ │ 3. SUMMARY                                                      ││
│ │    High-level jurisdictional summary                            ││
│ └─────────────────────────────────────────────────────────────────┘│
│                              │                                      │
│ ┌─────────────────────────────────────────────────────────────────┐│
│ │ 4. JURISDICTION SECTION (For each jurisdiction)                 ││
│ │    ├── Safe Harbours and Exclusions                            ││
│ │    ├── ETR Computation (~50 data points)                       ││
│ │    ├── Top-Up Tax Computation (~40 data points)                ││
│ │    └── Deferred Tax & Elections (~90 data points)              ││
│ └─────────────────────────────────────────────────────────────────┘│
│                              │                                      │
│ ┌─────────────────────────────────────────────────────────────────┐│
│ │ 5. UTPR ATTRIBUTION                                             ││
│ │    Top-Up Tax allocation among UTPR jurisdictions               ││
│ └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Section 1: Filing Info

### 2.1 Purpose

Identifies the entity filing the GIR, the MNE Group, and the reporting period.

### 2.2 Key Data Elements

| Data Element | Description | Format |
|--------------|-------------|--------|
| **Filing CE Name** | Legal name of entity filing the GIR | Text |
| **Filing CE Jurisdiction** | 2-character ISO country code | ISO 3166-1 Alpha-2 |
| **Filing CE Tax ID** | Local tax identification number | Text |
| **MNE Group Name** | Name commonly used in Consolidated Financial Statements | Text |
| **UPE Name** | Legal name of Ultimate Parent Entity | Text |
| **UPE Jurisdiction** | Country where UPE is located | ISO 3166-1 Alpha-2 |
| **Fiscal Year Start** | First day of reporting period | Date (YYYY-MM-DD) |
| **Fiscal Year End** | Last day of reporting period | Date (YYYY-MM-DD) |
| **Reporting Currency** | Currency used throughout GIR | ISO 4217 (e.g., EUR, USD) |

### 2.3 Exchange Jurisdictions

The Filing CE must identify jurisdictions where filing obligations are intended to be met through QCAA exchange:

```
EXCHANGE JURISDICTION DECLARATION

Filing CE: Stratos Holdings plc (UK)

Jurisdictions covered by QCAA exchange:
□ Germany
□ Ireland
□ Luxembourg
□ Singapore
□ USA

Jurisdictions requiring local filing:
□ Cayman Islands (no QCAA)
```

## Section 2: General Section (Corporate Structure)

### 2.1 Purpose

Provides the complete ownership structure of the MNE Group, including all Constituent Entities and their classifications.

### 2.2 Key Data Elements

| Data Element | Description |
|--------------|-------------|
| **CE List** | All Constituent Entities with identification details |
| **Entity Name** | Legal name of each CE |
| **Entity Jurisdiction** | 2-character country code |
| **Entity Tax ID** | Local tax identification number(s) |
| **Ownership Percentage** | Direct and indirect ownership by UPE |
| **Entity Classification** | UPE, IPE, POPE, MOCE, JV, Excluded Entity, etc. |
| **Main Parent** | Direct parent entity for each CE |
| **Consolidation Method** | Full, proportional, equity method |

### 3.3 Entity Classifications

| Code | Classification | Description |
|------|----------------|-------------|
| UPE | Ultimate Parent Entity | Top of ownership chain |
| IPE | Intermediate Parent Entity | Parent with IIR obligation |
| POPE | Partially-Owned Parent Entity | <80% owned by UPE |
| MOCE | Minority-Owned Constituent Entity | ≤30% owned, consolidated |
| JV | Joint Venture | ≥50% equity-accounted |
| IE | Investment Entity | Article 7.4 entity |
| PE | Permanent Establishment | Branch operations |
| EE | Excluded Entity | Article 1.5 exclusions |

The entity classification scheme within the GIR serves multiple purposes beyond mere identification. Each classification triggers different computational rules—POPEs require separate Top-Up Tax calculations, MOCEs face the 30% ownership threshold test, JVs are treated as separate MNE Groups for ETR purposes. Getting classifications wrong cascades through subsequent calculations. The challenge for many groups is that these classifications do not correspond to categories used in consolidated financial statements or legal entity management systems. A subsidiary may be "wholly-owned" for legal purposes but a MOCE for GloBE purposes if only 28% of its results flow through consolidation. Groups must therefore build specific classification logic into their Pillar Two data processes rather than relying on existing categorisations.

### Stratos Example: Corporate Structure Data

| Entity | Jurisdiction | Tax ID | Ownership | Classification |
|--------|--------------|--------|-----------|----------------|
| Stratos Holdings plc | GB | GB123456789 | 100% | UPE |
| SG Germany GmbH | DE | DE987654321 | 100% | CE |
| SG Singapore Pte Ltd | SG | SG12345678X | 100% | CE |
| SG Ireland Ltd | IE | IE1234567T | 100% | CE |
| Atlas Ireland Ltd | IE | IE7654321T | 28% | MOCE |
| TechStart Inc. | US | US-12-3456789 | 100% | CE |
| TechStart JV Pte Ltd | SG | SG87654321X | 55% | JV |

## 4. Section 3: Summary

### 2.1 Purpose

Provides a high-level overview of GloBE outcomes by jurisdiction before detailed calculations.

### 2.2 Key Data Elements

| Data Element | Description |
|--------------|-------------|
| **Jurisdiction** | 2-character country code |
| **Number of CEs** | Count of Constituent Entities in jurisdiction |
| **Safe Harbour Applied** | Yes/No and type (CbCR, QDMTT, etc.) |
| **De Minimis Applied** | Yes/No |
| **ETR** | Jurisdictional Effective Tax Rate |
| **Top-Up Tax** | Total jurisdictional Top-Up Tax |
| **QDMTT** | QDMTT amount (if applicable) |
| **IIR Liability** | IIR amount allocated |
| **UTPR Liability** | UTPR amount allocated |

### Summary Table Format

| Jurisdiction | CEs | Safe Harbour | De Minimis | ETR | Top-Up Tax (€) | QDMTT (€) | IIR (€) |
|--------------|-----|--------------|------------|-----|----------------|-----------|---------|
| GB | 2 | No | No | 25.00% | 0 | 0 | 0 |
| DE | 2 | No | No | 23.00% | 0 | 0 | 0 |
| US | 2 | No | No | 15.49% | 0 | 0 | 0 |
| SG | 1 | No | No | 9.81% | 197,498 | 0 | 197,498 |
| IE | 2 | No | No | 11.80% | 426,394 | 426,394 | 0 |
| LU | 1 | No | **Yes** | N/A | 0 | 0 | 0 |
| KY | 1 | No | No | 1.00% | 280,480 | 0 | 280,480 |

## 5. Section 4: Jurisdiction Section

### 5.1 Overview

The most detailed section of the GIR, containing all computational data for each jurisdiction. This section has **approximately 180+ data points** per jurisdiction.

### 4.1 Safe Harbours and Exclusions

| Data Element | Description |
|--------------|-------------|
| **Transitional CbCR Safe Harbour** | Claimed? Test met? |
| **QDMTT Safe Harbour** | Claimed? |
| **De Minimis Exclusion** | 3-year revenue average, income average |
| **Routine Profits Test** | If applicable |
| **ETR Test** | If applicable |

### 4.2 ETR Computation (~50 Data Points)

#### GloBE Income Data

| Data Element | Article Reference |
|--------------|-------------------|
| Financial Accounting Net Income/Loss | Art. 3.1.2 |
| Net taxes expense | Art. 3.2.1(a) |
| Excluded dividends | Art. 3.2.1(b) |
| Excluded equity gains/losses | Art. 3.2.1(c) |
| Asymmetric foreign currency gains/losses | Art. 3.2.1(e) |
| Policy disallowed expenses | Art. 3.2.1(f) |
| Prior period errors | Art. 3.2.1(g) |
| Accrued pension expense | Art. 3.2.1(h) |
| Stock-based compensation (election) | Art. 3.2.2 |
| International shipping income exclusion | Art. 3.3 |
| Arm's length adjustments | Art. 3.2.3 |
| **Total GloBE Income** | Art. 3.1.1 |

#### Covered Taxes Data

| Data Element | Article Reference |
|--------------|-------------------|
| Current tax expense | Art. 4.1.2(a) |
| Deferred tax expense | Art. 4.1.2(a) |
| Taxes on excluded income | Art. 4.1.3(a) |
| Uncertain tax positions | Art. 4.1.3(b) |
| Non-creditable foreign taxes | Art. 4.1.3(c) |
| Qualified refundable tax credits | Art. 4.1.3(d) |
| Disqualified refundable credits | Art. 4.1.3(e) |
| **Adjusted Covered Taxes** | Art. 4.1.1 |

#### ETR Calculation

| Data Element | Formula |
|--------------|---------|
| **Jurisdictional Net GloBE Income** | Sum of all CEs |
| **Adjusted Covered Taxes** | Sum of all CEs |
| **Effective Tax Rate** | ACT ÷ Net GloBE Income |

### 4.3 Top-Up Tax Computation (~40 Data Points)

#### SBIE Calculation

| Data Element | Description |
|--------------|-------------|
| Eligible employees | Count per jurisdiction |
| Eligible payroll costs | Total qualifying payroll |
| Payroll carve-out rate | Transition rate (9.8% for 2025) |
| **Payroll carve-out amount** | Payroll × Rate |
| Tangible assets carrying value | NBV of qualifying assets |
| Asset carve-out rate | Transition rate (7.8% for 2025) |
| **Asset carve-out amount** | Assets × Rate |
| **Total SBIE** | Payroll + Asset carve-outs |

#### Top-Up Tax Calculation

| Data Element | Formula |
|--------------|---------|
| Net GloBE Income | From ETR section |
| Less: SBIE | From SBIE calculation |
| **Excess Profit** | GloBE Income − SBIE |
| Minimum Rate | 15% |
| Jurisdictional ETR | From ETR calculation |
| **Top-Up Tax Percentage** | 15% − ETR |
| **Jurisdictional Top-Up Tax** | Excess Profit × Top-Up Tax % |

#### Additional Top-Up Tax Items

| Data Element | Article Reference |
|--------------|-------------------|
| QDMTT payable | Art. 10.1 |
| IIR Top-Up Tax | Art. 2.1 |
| UTPR Top-Up Tax | Art. 2.4 |
| Recapture amounts | Art. 4.4 |
| Additional current Top-Up Tax | Various |

### 4.4 Deferred Tax Adjustments (~50 Data Points)

| Data Element | Description |
|--------------|-------------|
| Opening deferred tax liability | By category |
| Movements in DTL | Current year changes |
| DTL recapture amounts | 5-year rule |
| Deferred tax assets | GloBE Loss Election |
| DTL categories | Accelerated depreciation, provisions, etc. |

### 4.5 Elections (~40 Data Points)

| Election | Article | Data Required |
|----------|---------|---------------|
| Stock-based compensation | Art. 3.2.2 | Amount adjusted |
| GloBE Loss Election | Art. 4.5 | DTA amount |
| SBIE allocation | Art. 5.3.5 | Allocation method |
| De Minimis | Art. 5.5 | 3-year averages |
| Investment Entity elections | Art. 7.5/7.6 | Entity list, method |
| Aggregate DTL recapture | Art. 4.4.4 | DTL details |

## 6. Section 5: UTPR Attribution

### 2.1 Purpose

Details the allocation of UTPR Top-Up Tax among jurisdictions where CEs are located.

### Data Elements

| Data Element | Description |
|--------------|-------------|
| **Low-taxed jurisdiction** | Source of Top-Up Tax |
| **UTPR jurisdictions** | Jurisdictions collecting UTPR |
| **UTPR percentage** | Based on employees and assets |
| **UTPR amount** | Allocated Top-Up Tax per jurisdiction |

### UTPR Allocation Formula

```
UTPR Percentage = (Employees in Jurisdiction + Tangible Assets in Jurisdiction)
                  ────────────────────────────────────────────────────────────────
                  (Total Employees + Total Tangible Assets in UTPR Jurisdictions)

UTPR Amount = Total UTPR Top-Up Tax × UTPR Percentage
```

## Data Volume Summary

The GIR requires substantial data collection:

| Section | Approximate Data Points |
|---------|------------------------|
| Filing Info | 15 |
| General Section (Corporate Structure) | 10 per entity |
| Summary | 10 per jurisdiction |
| Jurisdiction Section | 180+ per jurisdiction |
| UTPR Attribution | 5 per allocation |

**For a group like Stratos with 7 jurisdictions and 12 entities:**

```
Filing Info:                    15 data points
Corporate Structure:            120 data points (12 entities × 10)
Summary:                        70 data points (7 jurisdictions × 10)
Jurisdiction Sections:          1,260 data points (7 × 180)
UTPR Attribution:               10 data points (estimated)
                                ─────────────────────────────
TOTAL:                          ~1,475 data points
```

The sheer volume of data points explains why Pillar Two compliance cannot be treated as a year-end exercise. Even a moderately complex group must source, validate, and reconcile hundreds of data points from disparate systems—consolidated accounts, local statutory accounts, tax provisions, HR databases, fixed asset registers. Each data point represents a potential reconciliation issue. The 180+ data points per jurisdiction for the detailed Jurisdiction Section are particularly demanding, as they require not just extraction but adjustment to GloBE requirements that may differ from local accounting or tax treatment. Groups that have invested in tax data management systems for transfer pricing or CbCR purposes have significant advantages, but even these systems rarely contain all required Pillar Two data elements without modification.

## 7. XML Schema Structure

The GIR is filed using a standardised XML format:

### Schema Components

```xml
<GIR>
  <MessageHeader>
    <SendingEntityIN>...</SendingEntityIN>
    <ReceivingCountry>...</ReceivingCountry>
    <MessageType>GIR</MessageType>
    <ReportingPeriod>...</ReportingPeriod>
  </MessageHeader>

  <FilingInfo>
    <FilingCE>...</FilingCE>
    <MNEGroup>...</MNEGroup>
    <FiscalYear>...</FiscalYear>
  </FilingInfo>

  <GeneralSection>
    <CorporateStructure>
      <ConstituentEntity>...</ConstituentEntity>
      <!-- Repeated for each CE -->
    </CorporateStructure>
  </GeneralSection>

  <Summary>
    <JurisdictionSummary>...</JurisdictionSummary>
    <!-- Repeated for each jurisdiction -->
  </Summary>

  <JurisdictionSection>
    <SafeHarbours>...</SafeHarbours>
    <ETRComputation>...</ETRComputation>
    <TopUpTaxComputation>...</TopUpTaxComputation>
    <!-- Repeated for each jurisdiction -->
  </JurisdictionSection>

  <UTPRAttribution>
    <Allocation>...</Allocation>
  </UTPRAttribution>
</GIR>
```

### Validation Requirements

The XML must pass schema validation:
- Required elements present
- Data types correct (dates, numbers, codes)
- Cross-references valid (entity IDs match)
- Calculations consistent (ETR = ACT ÷ Income)

## Data Collection Process

### Recommended Workflow

```
DATA COLLECTION WORKFLOW

Phase 1: STRUCTURAL DATA (Month 1-3 post year-end)
├── Confirm CE list and ownership
├── Verify entity classifications
├── Document JVs, MOCEs, Investment Entities
└── Map data sources per entity

Phase 2: FINANCIAL DATA (Month 3-6 post year-end)
├── Extract financial accounting data
├── Gather local tax return data
├── Collect deferred tax schedules
└── Obtain payroll and asset registers

Phase 3: ADJUSTMENTS (Month 6-9 post year-end)
├── Calculate GloBE Income adjustments
├── Compute Covered Tax adjustments
├── Apply elections
└── Verify arm's length pricing

Phase 4: COMPUTATIONS (Month 9-12 post year-end)
├── Calculate ETR per jurisdiction
├── Compute SBIE
├── Determine Top-Up Tax
└── Allocate IIR/UTPR

Phase 5: REVIEW & FILING (Month 12-15 post year-end)
├── Internal review and sign-off
├── XML generation and validation
├── Submit GIR
└── File notifications
```

### Data Source Mapping

| Data Element | Primary Source | Secondary Source |
|--------------|----------------|------------------|
| Financial Accounting Net Income | Consolidated accounts | Local statutory accounts |
| Current tax expense | Tax provisions | Tax returns |
| Deferred tax | Tax provisions | DTA/DTL schedules |
| Payroll | HR systems | Payroll providers |
| Tangible assets | Fixed asset register | Accounts |
| Ownership | Legal records | Group structure database |

## January 2025 Simplifications

The January 2025 Administrative Guidance provides simplifications where:

### Single Jurisdiction Taxing Rights

If only **one jurisdiction** has taxing rights (e.g., only IIR applies):
- GIR can be completed based on domestic rules rather than pure GloBE Rules
- Reduces need to maintain parallel calculations

### QDMTT Safe Harbour

If **QDMTT Safe Harbour** applies:
- Simplified reporting for that jurisdiction
- Less granular data required
- Focus on domestic QDMTT computation

### Purpose of Simplifications

```
SIMPLIFICATION RATIONALE

Without simplification:
→ Complete GIR per GloBE Rules
→ Complete local return per domestic rules
→ Reconcile differences
→ Double compliance burden

With simplification:
→ Single source of data
→ Domestic rules accepted in GIR
→ Reduced reconciliation
→ Lower compliance cost
```

The January 2025 simplifications represent pragmatic recognition that theoretical purity must sometimes yield to practical administrability. When only one jurisdiction has taxing rights, requiring groups to maintain both pure GloBE calculations and domestic QDMTT calculations—then reconcile the two—produces compliance costs without corresponding enforcement benefit. The simplifications allow groups to leverage domestic calculations directly, reducing the parallel processing burden. However, groups should not assume simplifications apply universally; the conditions must be carefully verified, and changes in group structure or jurisdictional implementation status can affect eligibility from year to year.

## 8. Common Data Quality Issues

### Issue 1: Entity Identification Mismatches

**Problem:** Tax IDs don't match across systems.

**Solution:** Establish single source of truth for entity identification. Reconcile tax IDs across all jurisdictions before filing.

### Issue 2: Ownership Percentage Inconsistencies

**Problem:** Different ownership figures in legal records vs. accounts.

**Solution:** Use ownership per Consolidated Financial Statements. Document basis for any differences.

### Issue 3: Currency Translation Errors

**Problem:** Inconsistent exchange rates across data points.

**Solution:** Use consistent rates (typically average for P&L, closing for balance sheet). Document rate source.

### Issue 4: Missing Substance Data

**Problem:** Payroll and asset data not available by jurisdiction.

**Solution:** Work with local teams early to establish data collection processes. Build into year-end close procedures.

### Issue 5: Deferred Tax Reconciliation

**Problem:** Local deferred tax doesn't match GloBE requirements.

**Solution:** Maintain separate GloBE DTL tracking. Reconcile to local accounts with documented adjustments.

## 9. Stratos Data Collection Example

### Data Sources for Stratos Group

| Entity | Financial Data | Tax Data | Substance Data |
|--------|----------------|----------|----------------|
| Stratos Holdings plc | SAP | UK tax return | UK HR/Assets |
| SG Germany GmbH | SAP | German tax return | German HR/Assets |
| SG Singapore Pte | Local ERP | Singapore tax return | Singapore HR/Assets |
| SG Ireland Ltd | SAP | Irish tax return | Irish HR/Assets |
| TechStart Inc. | Oracle | US tax return | US HR/Assets |
| TechStart JV Pte | JV accounts | JV tax returns | JV data request |

### Key Data Collection Challenges

| Challenge | Mitigation |
|-----------|------------|
| TechStart post-acquisition | Partial year data extraction |
| JV data access | Data sharing agreement with JV partner |
| Atlas Ireland MOCE | Separate data collection from main Irish entity |
| Multiple ERP systems | Data mapping and consolidation |

## 10. GIR Data Checklist

```
GIR DATA REQUIREMENTS CHECKLIST
MNE Group: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: FILING INFO DATA
═══════════════════════════════════════════════════════════════════════

□ Filing CE name and jurisdiction                           COMPLETE / PENDING
□ Filing CE tax identification number(s)                    COMPLETE / PENDING
□ MNE Group name (per CFS)                                  COMPLETE / PENDING
□ UPE identification details                                COMPLETE / PENDING
□ Fiscal year dates                                         COMPLETE / PENDING
□ Reporting currency                                        COMPLETE / PENDING
□ QCAA exchange jurisdiction list                           COMPLETE / PENDING

═══════════════════════════════════════════════════════════════════════
SECTION B: CORPORATE STRUCTURE DATA
═══════════════════════════════════════════════════════════════════════

□ Complete CE list with jurisdictions                       COMPLETE / PENDING
□ Tax identification numbers for all CEs                    COMPLETE / PENDING
□ Ownership percentages (direct and indirect)               COMPLETE / PENDING
□ Entity classifications (UPE, MOCE, JV, etc.)             COMPLETE / PENDING
□ Excluded Entity identification                            COMPLETE / PENDING
□ JV Group structures                                       COMPLETE / PENDING

═══════════════════════════════════════════════════════════════════════
SECTION C: FINANCIAL DATA (Per Jurisdiction)
═══════════════════════════════════════════════════════════════════════

Jurisdiction: _________________________

□ Financial Accounting Net Income                           COMPLETE / PENDING
□ GloBE adjustments (dividends, gains, etc.)               COMPLETE / PENDING
□ Current tax expense                                       COMPLETE / PENDING
□ Deferred tax movements                                    COMPLETE / PENDING
□ DTL schedule by category                                  COMPLETE / PENDING

(Repeat for each jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION D: SUBSTANCE DATA (Per Jurisdiction)
═══════════════════════════════════════════════════════════════════════

Jurisdiction: _________________________

□ Employee count                                            COMPLETE / PENDING
□ Eligible payroll costs                                    COMPLETE / PENDING
□ Tangible asset carrying values                            COMPLETE / PENDING
□ Asset location verification                               COMPLETE / PENDING

(Repeat for each jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION E: ELECTIONS AND SAFE HARBOURS
═══════════════════════════════════════════════════════════════════════

□ Elections made (list):
   □ _________________________
   □ _________________________
   □ _________________________

□ Safe harbours claimed:
   □ Transitional CbCR Safe Harbour (jurisdictions): _________________________
   □ QDMTT Safe Harbour (jurisdictions): _________________________
   □ De Minimis (jurisdictions): _________________________

═══════════════════════════════════════════════════════════════════════
SECTION F: DATA QUALITY REVIEW
═══════════════════════════════════════════════════════════════════════

□ Entity IDs reconciled across all sources?                 YES / NO
□ Ownership percentages verified?                           YES / NO
□ Currency translation rates documented?                    YES / NO
□ ETR calculations cross-checked?                           YES / NO
□ SBIE data verified with source systems?                   YES / NO
□ XML schema validation passed?                             YES / NO
```

## Concluding Discussion

The GIR data requirements reveal why Pillar Two implementation is fundamentally a data management challenge as much as a tax technical one. Groups with robust tax data infrastructure—centralised entity management, consistent tax provision processes, integrated HR and asset systems—will navigate these requirements far more efficiently than those relying on fragmented spreadsheets and annual data requests.

For practitioners advising on Pillar Two readiness, the data mapping exercise should precede detailed calculation work. Understanding where each required data point will come from, what adjustments it requires, and who owns it organisationally establishes the foundation for sustainable compliance. The five-phase workflow presented in this chapter—Structural Data, Financial Data, Adjustments, Computations, Review & Filing—provides a framework, but each group must adapt it to their specific systems and organisational structure.

The common data quality issues highlighted are not theoretical concerns but reflect actual challenges encountered by early adopters. Entity identification mismatches between legal, tax, and accounting systems; ownership figures that differ across consolidation and legal records; currency translation inconsistencies—these mundane issues consume disproportionate compliance effort unless addressed systematically. Groups that invest in data quality before their first GIR filing will benefit for years; those that defer this work will repeat the same reconciliation exercises annually.

