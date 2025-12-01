# Section 10.4: Scenario 4 - Multi-QDMTT Jurisdictions

## Learning Objectives

By the end of this section, you will be able to:

- Understand the GloBE rule ordering with multiple QDMTTs
- Calculate QDMTT offsets against IIR charges
- Coordinate Top-up Tax filings across QDMTT jurisdictions
- Handle variations in QDMTT regimes between countries
- Report multi-QDMTT scenarios correctly in the GIR
- Manage filing sequences and payment timing

---

## Scenario Overview

### The Facts

**Atlantic Manufacturing Group plc** is a UK-headquartered industrial conglomerate with significant operations in five jurisdictions that have all enacted QDMTTs.

**Group Profile:**

| Attribute | Detail |
|-----------|--------|
| **Ultimate Parent Entity** | Atlantic Manufacturing Group plc (UK) |
| **Headquarters** | Birmingham, United Kingdom |
| **Fiscal Year End** | 31 December 2024 |
| **Consolidated Revenue** | €3.2 billion |
| **Total Constituent Entities** | 85 |
| **QDMTT Jurisdictions** | 5 (UK, Germany, Netherlands, Switzerland, Ireland) |

### QDMTT Jurisdiction Profile

```
ATLANTIC MANUFACTURING - QDMTT JURISDICTIONS
============================================

Jurisdiction 1: United Kingdom (UPE Location)
├── QDMTT: UK Domestic Top-up Tax (DTT)
├── IIR: UK Multinational Top-up Tax (MTT)
├── Entities: 12
├── Combined statutory rate: 25%
└── ETR Status: Above 15% (no domestic Top-up Tax)

Jurisdiction 2: Germany
├── QDMTT: Nationale Ergänzungssteuer
├── Entities: 15
├── Statutory rate: ~30%
└── ETR Status: Above 15% (no Top-up Tax)

Jurisdiction 3: Netherlands
├── QDMTT: Wet minimumbelasting
├── Entities: 8 (including HoldCo/Treasury)
├── Statutory rate: 25.8%
└── ETR Status: MIXED (IP regime entities below 15%)

Jurisdiction 4: Switzerland
├── QDMTT: Mindeststeuer (Canton level)
├── Entities: 3 (Trading hub)
├── Effective rate: 12-14%
└── ETR Status: Below 15% (QDMTT applies)

Jurisdiction 5: Ireland
├── QDMTT: Qualified Domestic Minimum Top-up Tax
├── Entities: 6 (IP holding, services)
├── Statutory rate: 15% (new minimum)
└── ETR Status: MIXED (legacy IP below 15%)
```

---

## Part 1: GloBE Rule Ordering

### 1.1 The Ordering Principle

The GloBE Rules apply in a specific sequence designed to prevent double taxation:

```
GLOBE RULE ORDER
================

STEP 1: QDMTT (Domestic Collection - Priority)
         │
         ├── Each jurisdiction with QDMTT calculates own Top-up Tax
         ├── QDMTT collected by local jurisdiction
         └── Applies before IIR or UTPR

         │
         ▼

STEP 2: IIR (Income Inclusion Rule)
         │
         ├── Parent jurisdiction charges Top-up Tax
         ├── QDMTT already paid is CREDITED
         └── Only residual Top-up Tax charged (if any)

         │
         ▼

STEP 3: UTPR (Undertaxed Profits Rule - Backstop)
         │
         ├── Applies if no IIR in parent jurisdiction
         ├── QDMTT and IIR amounts credited
         └── Allocated to UTPR jurisdictions
```

### 1.2 QDMTT Offset Mechanism

The QDMTT operates as a "pound-for-pound" offset against IIR liability:

```
IIR CALCULATION WITH QDMTT OFFSET
=================================

Formula:
IIR Charge = Top-up Tax - QDMTT Paid

Where:
  Top-up Tax = max(0, 15% - ETR) × (GloBE Income - SBIE)

Example:
  Jurisdiction ETR: 11%
  GloBE Income: €20,000,000
  SBIE: €3,000,000
  Excess Profit: €17,000,000
  Top-up Tax %: 4% (15% - 11%)
  Total Top-up Tax: €680,000

  QDMTT Paid in Jurisdiction: €680,000

  IIR Charge (UK): €680,000 - €680,000 = €0
```

---

## Part 2: Jurisdiction-by-Jurisdiction Analysis

### 2.1 Netherlands - IP Regime Entities

**Structure:**
- Atlantic Netherlands BV (HoldCo)
- Atlantic IP Netherlands BV (IP holding - innovation box)
- Atlantic Treasury BV (group treasury)
- 5 other entities (normal trading)

**IP Entity Analysis:**

```
NETHERLANDS IP ENTITY - QDMTT CALCULATION
=========================================

Entity: Atlantic IP Netherlands BV
IP Regime: Innovation Box (9% effective rate on qualifying income)

Pre-QDMTT Position:
  Total Income:                    €25,000,000
  Innovation Box Income:           €20,000,000
  Regular Income:                   €5,000,000

  Tax on Innovation Box (9%):       €1,800,000
  Tax on Regular Income (25.8%):    €1,290,000
  Total Covered Taxes:              €3,090,000

  Blended ETR: €3,090,000 / €25,000,000 = 12.36%

GLOBE CALCULATION:
  GloBE Income:                    €25,000,000
  Adjusted Covered Taxes:           €3,090,000
  ETR:                                  12.36%
  Top-up Tax %:                          2.64%

  SBIE:
    Eligible Payroll (€4,000,000 × 9.8%):   €392,000
    Tangible Assets (€2,500,000 × 7.8%):    €195,000
    Total SBIE:                             €587,000

  Excess Profit: €25,000,000 - €587,000 = €24,413,000
  Top-up Tax: €24,413,000 × 2.64% = €644,503

QDMTT COLLECTION:
  Dutch QDMTT Payable:              €644,503
  Collected by: Belastingdienst
  Filing: Aangifte minimumbelasting

IIR IMPACT (UK):
  Top-up Tax for NL IP entity:      €644,503
  Less: QDMTT offset:              (€644,503)
  IIR Charge (UK):                        €0
```

### 2.2 Switzerland - Trading Hub

**Structure:**
- Atlantic Trading AG (principal trading)
- Atlantic Finance AG (treasury)
- Atlantic Holding AG (holding)

**Swiss QDMTT Analysis:**

```
SWITZERLAND - QDMTT CALCULATION
===============================

Aggregate Swiss Entities:
  GloBE Income:                    €35,000,000
  Adjusted Covered Taxes:           €4,550,000
  Jurisdictional ETR:                   13.0%
  Top-up Tax %:                          2.0%

  SBIE:
    Eligible Payroll (€12,000,000 × 9.8%):  €1,176,000
    Tangible Assets (€5,000,000 × 7.8%):      €390,000
    Total SBIE:                             €1,566,000

  Excess Profit: €35,000,000 - €1,566,000 = €33,434,000
  Top-up Tax: €33,434,000 × 2.0% = €668,680

SWISS QDMTT COLLECTION:
  Swiss QDMTT Payable:              €668,680
  Collected by: Cantonal tax authority
  Note: Switzerland has canton-level QDMTT

ALLOCATION TO ENTITIES:
  Atlantic Trading AG:              €450,000 (67%)
  Atlantic Finance AG:              €180,000 (27%)
  Atlantic Holding AG:               €38,680 (6%)

IIR IMPACT (UK):
  Top-up Tax for Swiss entities:    €668,680
  Less: QDMTT offset:              (€668,680)
  IIR Charge (UK):                        €0
```

### 2.3 Ireland - Legacy IP Below 15%

**Structure:**
- Atlantic Ireland Ltd (IP holding - 12.5% historic rate)
- Atlantic Services Ireland Ltd (shared services)
- Atlantic R&D Ireland Ltd (R&D operations)
- 3 other entities (normal operations at 15%+)

**Irish QDMTT Analysis:**

```
IRELAND - QDMTT CALCULATION (FY2024)
====================================

Note: Ireland introduced 15% minimum rate for large groups
      Legacy arrangements may still result in ETR <15%

Legacy IP Entity: Atlantic Ireland Ltd
  Income from pre-2024 IP:          €18,000,000
  Covered Taxes (12.5%):             €2,250,000
  ETR:                                   12.5%

Modern Entities (at 15%+):
  Combined Income:                  €12,000,000
  Covered Taxes:                     €1,920,000
  ETR:                                   16.0%

JURISDICTIONAL BLENDING:
  Total GloBE Income:               €30,000,000
  Total Covered Taxes:               €4,170,000
  Blended ETR:                          13.9%

  Top-up Tax %: 15% - 13.9% = 1.1%

  SBIE:
    Eligible Payroll (€22,000,000 × 9.8%):  €2,156,000
    Tangible Assets (€8,000,000 × 7.8%):      €624,000
    Total SBIE:                             €2,780,000

  Excess Profit: €30,000,000 - €2,780,000 = €27,220,000
  Top-up Tax: €27,220,000 × 1.1% = €299,420

IRISH QDMTT COLLECTION:
  Irish QDMTT Payable:              €299,420
  Collected by: Revenue Commissioners
  Filing: QDMTT return

IIR IMPACT (UK):
  Top-up Tax for Irish entities:    €299,420
  Less: QDMTT offset:              (€299,420)
  IIR Charge (UK):                        €0
```

### 2.4 UK and Germany - No Top-up Tax

Both jurisdictions have ETR above 15%, so no QDMTT or Top-up Tax arises:

```
UK AND GERMANY - NO TOP-UP TAX
==============================

UNITED KINGDOM:
  GloBE Income:                   €120,000,000
  Covered Taxes:                   €30,000,000
  ETR:                                  25.0%
  Top-up Tax:                            NIL

GERMANY:
  GloBE Income:                    €85,000,000
  Covered Taxes:                   €25,500,000
  ETR:                                  30.0%
  Top-up Tax:                            NIL
```

---

## Part 3: Consolidated Top-up Tax Summary

### 3.1 Group-Wide Position

```
ATLANTIC MANUFACTURING - TOP-UP TAX SUMMARY FY2024
==================================================

QDMTT BY JURISDICTION:
──────────────────────
Jurisdiction      GloBE Income    ETR      QDMTT Payable
─────────────────────────────────────────────────────────
Netherlands       €25,000,000    12.36%   €644,503
Switzerland       €35,000,000    13.00%   €668,680
Ireland           €30,000,000    13.90%   €299,420
─────────────────────────────────────────────────────────
TOTAL QDMTT                              €1,612,603

UK (no QDMTT):    €120,000,000   25.00%   NIL
Germany (no QDMTT): €85,000,000  30.00%   NIL


IIR POSITION (UK):
──────────────────
Gross Top-up Tax (all jurisdictions):    €1,612,603
Less: QDMTT offsets:                    (€1,612,603)
                                        ─────────────
NET UK IIR CHARGE:                              €0
                                        =============


SUMMARY:
────────
Total Top-up Tax Collected:              €1,612,603
  - By Netherlands:                        €644,503
  - By Switzerland:                        €668,680
  - By Ireland:                            €299,420
  - By UK (IIR):                                €0
```

### 3.2 Impact Assessment

```
QDMTT IMPACT ANALYSIS
=====================

Without QDMTT (hypothetical):
  All Top-up Tax would be collected by UK under IIR
  UK MTT liability: €1,612,603

With QDMTT (actual):
  Top-up Tax collected locally in each jurisdiction
  UK MTT liability: €0

GROUP PERSPECTIVE:
  Total tax: Same (€1,612,603)
  Difference: WHERE tax is paid, not HOW MUCH

JURISDICTIONAL PERSPECTIVE:
  Netherlands retains: €644,503
  Switzerland retains: €668,680
  Ireland retains: €299,420
  UK foregoes: €1,612,603

Note: This is the intended policy outcome of QDMTT -
      preserving source country taxing rights.
```

---

## Part 4: QDMTT Regime Variations

### 4.1 Key Differences Between Jurisdictions

| Feature | UK (DTT) | Germany | Netherlands | Switzerland | Ireland |
|---------|----------|---------|-------------|-------------|---------|
| **Accounting Standard** | IFRS or UK GAAP | IFRS or German GAAP | IFRS or Dutch GAAP | IFRS or Swiss GAAP | IFRS or Irish GAAP |
| **Filing Entity** | Responsible Member | Group entity | Each CE | Cantonal | Each CE |
| **Return Deadline** | Aligned with MTT | 12 months | 17/20 months | Cantonal varies | 9 months |
| **Payment Deadline** | With return | With return | With return | Cantonal varies | With return |
| **Safe Harbour** | QDMTT SH available | QDMTT SH available | QDMTT SH available | QDMTT SH available | QDMTT SH available |

### 4.2 Handling Accounting Standard Differences

QDMTT jurisdictions may use local GAAP, creating potential mismatches:

```
ACCOUNTING STANDARD MISMATCH
============================

Scenario:
  UPE (UK) uses IFRS
  Swiss subsidiary uses Swiss GAAP for local accounts
  Swiss QDMTT calculated on Swiss GAAP basis
  GIR calculated on IFRS basis

Potential Issues:
  - Timing differences (revenue recognition)
  - Lease accounting (IFRS 16 vs local)
  - Fair value measurements

Resolution:
  - QDMTT Safe Harbour accommodates this
  - Use local GAAP for QDMTT return
  - Use IFRS for GIR Section 2
  - Document reconciliation if material

QDMTT Paid:                    CHF 750,000 (Swiss GAAP)
Converted to EUR:              €680,000
GIR Top-up Tax (IFRS):         €668,680
Difference:                    €11,320 (1.7%)

Treatment:
  - QDMTT paid exceeds IFRS calculation
  - No residual IIR charge
  - Difference documented
```

### 4.3 Entity-Level vs Group-Level QDMTT

Some jurisdictions require entity-level QDMTT returns:

```
ENTITY-LEVEL QDMTT (Netherlands)
================================

Each Dutch CE files separately:

Atlantic Netherlands BV (HoldCo):
  GloBE Income: €5,000,000
  ETR: 25.8%
  QDMTT: NIL (above 15%)

Atlantic IP Netherlands BV:
  GloBE Income: €20,000,000
  ETR: 9% (innovation box)
  QDMTT: €644,503

Note: Jurisdictional blending happens for IIR purposes,
but local QDMTT is per-entity in Netherlands.

Correction: Netherlands uses jurisdictional aggregation
for QDMTT. The example above simplified for illustration.
```

---

## Part 5: Filing Sequence and Coordination

### 5.1 Filing Timeline

```
MULTI-QDMTT FILING TIMELINE (FY2024)
====================================

31 Dec 2024    Fiscal Year End
     │
     │    ┌─────────────────────────────────────────────┐
     │    │ Phase 1: Data Collection (Jan-Jun 2025)     │
     │    │ - Gather GloBE data from all jurisdictions  │
     │    │ - Calculate jurisdictional ETR              │
     │    │ - Identify QDMTT exposures                  │
     │    └─────────────────────────────────────────────┘
     │
Sep 2025  Ireland QDMTT Return (9-month deadline)
     │
     │    ┌─────────────────────────────────────────────┐
     │    │ Phase 2: QDMTT Returns (Sep 2025 - Jun 2026)│
     │    │ - File Ireland QDMTT (Sep 2025)             │
     │    │ - File Germany QDMTT (Dec 2025)             │
     │    │ - File Switzerland QDMTT (varies)           │
     │    │ - File Netherlands QDMTT (Jun 2026)         │
     │    └─────────────────────────────────────────────┘
     │
Dec 2025  Germany QDMTT Return (12-month deadline)
     │
     │    Swiss QDMTT varies by canton
     │
Jun 2026  Netherlands QDMTT Return (17-month transitional)
     │
Jun 2026  UK GIR Filing Deadline (18-month transitional)
     │    └── Reports all jurisdictions
     │    └── Shows QDMTT offsets
     │
Jun 2026  UK MTT Self-Assessment
     │    └── Reports IIR charge (after QDMTT offset)
     │    └── Payment due
     │
     ▼
COMPLETE
```

### 5.2 Data Flow Between Returns

```
DATA FLOW - MULTI-QDMTT COORDINATION
====================================

             ┌────────────────────┐
             │   Central GloBE    │
             │   Calculation      │
             │   (Group Tax)      │
             └─────────┬──────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │   NL     │  │   CH     │  │   IE     │
   │ QDMTT    │  │ QDMTT    │  │ QDMTT    │
   │ Return   │  │ Return   │  │ Return   │
   └────┬─────┘  └────┬─────┘  └────┬─────┘
        │             │             │
        │    QDMTT amounts paid     │
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
              ┌───────────────┐
              │   UK GIR      │
              │ + MTT Return  │
              │               │
              │ - Reports all │
              │   Top-up Tax  │
              │ - Shows QDMTT │
              │   offsets     │
              │ - Net IIR = 0 │
              └───────────────┘
```

### 5.3 Coordination Checklist

```
MULTI-QDMTT COORDINATION CHECKLIST
==================================

PRE-FILING:
□ All jurisdictional ETR calculations complete
□ QDMTT exposures identified
□ Local filing deadlines mapped
□ Responsible persons assigned per jurisdiction
□ Data sharing protocol established

QDMTT FILING:
□ Ireland QDMTT return prepared
□ Ireland QDMTT filed by deadline
□ Ireland QDMTT payment made

□ Germany QDMTT return prepared
□ Germany QDMTT filed by deadline
□ Germany QDMTT payment made

□ Switzerland QDMTT return prepared
□ Switzerland QDMTT filed by cantonal deadline
□ Switzerland QDMTT payment made

□ Netherlands QDMTT return prepared
□ Netherlands QDMTT filed by deadline
□ Netherlands QDMTT payment made

GIR FILING:
□ All QDMTT amounts confirmed
□ QDMTT offsets calculated
□ GIR Section 2 completed for all jurisdictions
□ Net IIR charge determined
□ UK GIR filed
□ UK MTT Self-Assessment filed
□ UK MTT payment made (if any)

POST-FILING:
□ All filing confirmations retained
□ QDMTT payment receipts retained
□ Reconciliation completed
□ Documentation archived
```

---

## Part 6: GIR Reporting for Multi-QDMTT

### 6.1 Section 2 - Jurisdictional Data

```xml
<!-- GIR SECTION 2 - MULTI-QDMTT REPORTING -->

<JurisdictionInfo>
  <!-- Netherlands - QDMTT Jurisdiction -->
  <Jurisdiction>
    <JurisdictionCode>NL</JurisdictionCode>
    <NumberOfCEs>8</NumberOfCEs>
    <GloBECalculation>
      <GloBEIncome currCode="EUR">25000000</GloBEIncome>
      <AdjustedCoveredTaxes currCode="EUR">3090000</AdjustedCoveredTaxes>
      <ETR>12.36</ETR>
      <TopUpTaxPercentage>2.64</TopUpTaxPercentage>
      <EligiblePayroll currCode="EUR">4000000</EligiblePayroll>
      <TangibleAssets currCode="EUR">2500000</TangibleAssets>
      <SBIE currCode="EUR">587000</SBIE>
      <ExcessProfit currCode="EUR">24413000</ExcessProfit>
      <GrossTopUpTax currCode="EUR">644503</GrossTopUpTax>
    </GloBECalculation>
    <QDMTT>
      <QDMTTApplied>true</QDMTTApplied>
      <QDMTTAmount currCode="EUR">644503</QDMTTAmount>
      <QDMTTStatus>TransitionalQualified</QDMTTStatus>
    </QDMTT>
    <TopUpTaxAfterQDMTT currCode="EUR">0</TopUpTaxAfterQDMTT>
  </Jurisdiction>

  <!-- Switzerland - QDMTT Jurisdiction -->
  <Jurisdiction>
    <JurisdictionCode>CH</JurisdictionCode>
    <NumberOfCEs>3</NumberOfCEs>
    <GloBECalculation>
      <GloBEIncome currCode="EUR">35000000</GloBEIncome>
      <AdjustedCoveredTaxes currCode="EUR">4550000</AdjustedCoveredTaxes>
      <ETR>13.00</ETR>
      <TopUpTaxPercentage>2.00</TopUpTaxPercentage>
      <EligiblePayroll currCode="EUR">12000000</EligiblePayroll>
      <TangibleAssets currCode="EUR">5000000</TangibleAssets>
      <SBIE currCode="EUR">1566000</SBIE>
      <ExcessProfit currCode="EUR">33434000</ExcessProfit>
      <GrossTopUpTax currCode="EUR">668680</GrossTopUpTax>
    </GloBECalculation>
    <QDMTT>
      <QDMTTApplied>true</QDMTTApplied>
      <QDMTTAmount currCode="EUR">668680</QDMTTAmount>
      <QDMTTStatus>TransitionalQualified</QDMTTStatus>
    </QDMTT>
    <TopUpTaxAfterQDMTT currCode="EUR">0</TopUpTaxAfterQDMTT>
  </Jurisdiction>

  <!-- Ireland - QDMTT Jurisdiction -->
  <Jurisdiction>
    <JurisdictionCode>IE</JurisdictionCode>
    <NumberOfCEs>6</NumberOfCEs>
    <GloBECalculation>
      <GloBEIncome currCode="EUR">30000000</GloBEIncome>
      <AdjustedCoveredTaxes currCode="EUR">4170000</AdjustedCoveredTaxes>
      <ETR>13.90</ETR>
      <TopUpTaxPercentage>1.10</TopUpTaxPercentage>
      <EligiblePayroll currCode="EUR">22000000</EligiblePayroll>
      <TangibleAssets currCode="EUR">8000000</TangibleAssets>
      <SBIE currCode="EUR">2780000</SBIE>
      <ExcessProfit currCode="EUR">27220000</ExcessProfit>
      <GrossTopUpTax currCode="EUR">299420</GrossTopUpTax>
    </GloBECalculation>
    <QDMTT>
      <QDMTTApplied>true</QDMTTApplied>
      <QDMTTAmount currCode="EUR">299420</QDMTTAmount>
      <QDMTTStatus>TransitionalQualified</QDMTTStatus>
    </QDMTT>
    <TopUpTaxAfterQDMTT currCode="EUR">0</TopUpTaxAfterQDMTT>
  </Jurisdiction>

  <!-- UK - No Top-up Tax -->
  <Jurisdiction>
    <JurisdictionCode>GB</JurisdictionCode>
    <NumberOfCEs>12</NumberOfCEs>
    <SafeHarbour>
      <Type>TransitionalCbCR</Type>
      <TestApplied>SimplifiedETR</TestApplied>
      <TestResult>Pass</TestResult>
    </SafeHarbour>
    <TopUpTax currCode="EUR">0</TopUpTax>
  </Jurisdiction>

  <!-- Germany - No Top-up Tax -->
  <Jurisdiction>
    <JurisdictionCode>DE</JurisdictionCode>
    <NumberOfCEs>15</NumberOfCEs>
    <SafeHarbour>
      <Type>TransitionalCbCR</Type>
      <TestApplied>SimplifiedETR</TestApplied>
      <TestResult>Pass</TestResult>
    </SafeHarbour>
    <TopUpTax currCode="EUR">0</TopUpTax>
  </Jurisdiction>
</JurisdictionInfo>
```

### 6.2 IIR Summary Section

```xml
<!-- GIR IIR SUMMARY -->

<IIRSummary>
  <TotalGrossTopUpTax currCode="EUR">1612603</TotalGrossTopUpTax>
  <QDMTTOffsets>
    <Offset jurisdiction="NL" currCode="EUR">644503</Offset>
    <Offset jurisdiction="CH" currCode="EUR">668680</Offset>
    <Offset jurisdiction="IE" currCode="EUR">299420</Offset>
    <TotalQDMTTOffset currCode="EUR">1612603</TotalQDMTTOffset>
  </QDMTTOffsets>
  <NetIIRCharge currCode="EUR">0</NetIIRCharge>
</IIRSummary>
```

---

## Part 7: Common Issues and Solutions

### 7.1 Issue: QDMTT Calculation Differences

**Problem:** Local QDMTT return shows different amount than GIR calculation

**Cause:** Different accounting standards or adjustment methodologies

**Solution:**
- Document the reconciling items
- Use local QDMTT amount as offset (actual paid)
- Explain difference in GIR documentation
- No residual IIR if QDMTT ≥ GIR Top-up Tax

### 7.2 Issue: Filing Deadline Misalignment

**Problem:** Irish QDMTT due before full group data available

**Cause:** Ireland's 9-month deadline vs 18-month GIR deadline

**Solution:**
- Prepare Ireland estimates early
- File QDMTT return with best available data
- Amend if material changes post-filing
- Document estimation methodology

### 7.3 Issue: Currency Conversion

**Problem:** Swiss QDMTT paid in CHF; GIR reports in EUR

**Solution:**
- Convert at average annual rate for consistency
- Document rate source (ECB recommended)
- Retain CHF calculation for Swiss records
- EUR amount used for QDMTT offset in GIR

### 7.4 Issue: Partial QDMTT Coverage

**Problem:** Jurisdiction has QDMTT but not all entities subject

**Solution:**
- Apply QDMTT only to in-scope entities
- Residual Top-up Tax for non-QDMTT entities goes to IIR
- Clearly allocate in GIR Section 3

---

## Deliverable: Multi-QDMTT Coordination Template

```
MULTI-QDMTT COORDINATION TEMPLATE
=================================

Group: _________________________________
Fiscal Year: ___________________________
Prepared by: ____________ Date: ________

PART A: QDMTT JURISDICTION SUMMARY

| Jurisdiction | QDMTT? | # CEs | GloBE Income | ETR    | Top-up Tax |
|--------------|--------|-------|--------------|--------|------------|
| ____________ | Y / N  | _____ | €___________ | ____% | €_________ |
| ____________ | Y / N  | _____ | €___________ | ____% | €_________ |
| ____________ | Y / N  | _____ | €___________ | ____% | €_________ |
| ____________ | Y / N  | _____ | €___________ | ____% | €_________ |
| ____________ | Y / N  | _____ | €___________ | ____% | €_________ |
|              |        |       |              |        |            |
| TOTAL        |        | _____ |              |        | €_________ |

PART B: QDMTT FILING STATUS

| Jurisdiction | Local Return  | Filing    | Payment   | Confirmation |
|              | Name          | Deadline  | Made?     | Ref          |
|--------------|---------------|-----------|-----------|--------------|
| ____________ | _____________ | _________ | □ Y □ N   | ____________ |
| ____________ | _____________ | _________ | □ Y □ N   | ____________ |
| ____________ | _____________ | _________ | □ Y □ N   | ____________ |
| ____________ | _____________ | _________ | □ Y □ N   | ____________ |

PART C: QDMTT OFFSET CALCULATION

Total Gross Top-up Tax:                    €______________

Less QDMTT Offsets:
  [Jurisdiction 1]: _______________       (€______________)
  [Jurisdiction 2]: _______________       (€______________)
  [Jurisdiction 3]: _______________       (€______________)
  [Jurisdiction 4]: _______________       (€______________)
                                          ────────────────
  Total QDMTT Offsets:                    (€______________)
                                          ────────────────
NET IIR CHARGE:                           €______________
                                          ================

PART D: GIR RECONCILIATION

GIR Gross Top-up Tax:                      €______________
Sum of Local QDMTT Returns:                €______________
Difference (if any):                       €______________

Reconciling Items:
□ Accounting standard differences
□ Currency translation
□ Timing differences
□ Other: _________________

PART E: SIGN-OFF

□ All QDMTT jurisdictions identified
□ All local returns filed
□ All payments confirmed
□ GIR reflects correct offsets
□ Documentation retained

Prepared by: __________________ Date: ____________
Reviewed by: __________________ Date: ____________
Approved by: __________________ Date: ____________
```

---

## Section Summary

Multi-QDMTT scenarios require careful coordination:

1. **Rule Ordering** - QDMTT applies first, then IIR, then UTPR
2. **Pound-for-Pound Offset** - QDMTT paid reduces IIR charge
3. **Regime Variations** - Accounting standards, deadlines differ
4. **Filing Sequence** - Coordinate local QDMTT returns with GIR
5. **Documentation** - Track QDMTT payments for GIR offsets

The net effect for compliant groups is often zero IIR liability where QDMTTs collect the full Top-up Tax locally.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Rule Order** | QDMTT → IIR → UTPR |
| **Offset Effect** | QDMTT is pound-for-pound credit against IIR |
| **Policy Outcome** | Source countries retain taxing rights |
| **Regime Differences** | Accounting standards, deadlines vary |
| **Filing Coordination** | Local QDMTT returns before GIR |
| **GIR Reporting** | Show gross Top-up Tax and QDMTT offsets |
| **Net IIR** | Often zero when QDMTT collects full amount |
| **Documentation** | Retain QDMTT return and payment evidence |

---

## Sources

Key references for this section include:

- [OECD Pillars - Qualifying Domestic Minimum Top-Up Tax](https://oecdpillars.com/pillar-tab/qualifying-domestic-minimum-top-up-tax/)
- [Tax Foundation - Pillar Two Implementation in Europe 2025](https://taxfoundation.org/data/all/eu/pillar-two-implementation-europe/)
- [PwC - Pillar Two Guide for EMEA Multinational Enterprises](https://www.pwc.com/gx/en/services/tax/assets/pwc-pillar-two-guide-for-emea-multinational-enterprises.pdf)
- [OECD - Qualified Status under the Global Minimum Tax Q&A](https://www.oecd.org/tax/beps/qualified-status-under-the-global-minimum-tax-questions-and-answers.pdf)

---

*Section 10.4 Complete. Proceed to Section 10.5: Scenario 5 - Amendment Required.*
