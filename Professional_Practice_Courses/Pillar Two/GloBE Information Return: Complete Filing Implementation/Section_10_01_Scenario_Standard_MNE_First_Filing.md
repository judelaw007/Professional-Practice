# Section 10.1: Scenario 1 - Standard MNE First Filing

## Learning Objectives

By the end of this section, you will be able to:

- Complete a full GIR for a standard multinational enterprise group
- Populate all three GIR sections with appropriate data
- Navigate the January 2025 XML schema requirements
- Coordinate filing across multiple jurisdictions
- Apply lessons learned to client engagements

---

## Scenario Overview

### The Facts

**GlobalTech Manufacturing Ltd** is a UK-headquartered multinational enterprise group specialising in precision engineering components for the automotive and aerospace industries.

**Group Profile:**

| Attribute | Detail |
|-----------|--------|
| **Ultimate Parent Entity** | GlobalTech Manufacturing Ltd (UK) |
| **Headquarters** | Manchester, United Kingdom |
| **Fiscal Year End** | 31 December |
| **First In-Scope Year** | FY2024 |
| **Consolidated Revenue (FY2023)** | €1.2 billion |
| **Consolidated Revenue (FY2024)** | €1.35 billion |
| **Number of Constituent Entities** | 75 |
| **Jurisdictions** | 20 |
| **Accounting Standard** | IFRS |
| **GIR Filing Deadline** | 30 June 2026 (18-month transitional) |

### Group Structure

```
GLOBALTECH MANUFACTURING GROUP STRUCTURE
========================================

                    GlobalTech Manufacturing Ltd
                         (UK - UPE)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   GT Holdings            GT Europe            GT Americas
   Europe BV              GmbH                 Inc
   (Netherlands)          (Germany)            (USA)
        │                     │                     │
   ┌────┴────┐           ┌────┴────┐          ┌────┴────┐
   │         │           │         │          │         │
GT France  GT Spain   GT Poland  GT Czech  GT Canada GT Mexico
  SAS       SL         Sp.z.o.o   s.r.o      Ltd      S de RL
   │                                                     │
GT Italy                                            GT Brazil
  Srl                                                Ltda
```

### Jurisdictional Presence

| Jurisdiction | # of CEs | Primary Activity | ETR Estimate |
|--------------|----------|------------------|--------------|
| United Kingdom | 8 | HQ, R&D, Manufacturing | 23% |
| Germany | 12 | Manufacturing, Sales | 29% |
| Netherlands | 5 | Holding, Treasury | 25% |
| France | 6 | Manufacturing, Sales | 25% |
| Spain | 4 | Manufacturing | 25% |
| Italy | 3 | Sales, Distribution | 24% |
| Poland | 5 | Manufacturing | 19% |
| Czech Republic | 3 | Manufacturing | 19% |
| Ireland | 4 | IP Holding, Services | 12.5% |
| Switzerland | 2 | Trading, Finance | 14% |
| USA | 8 | Sales, Manufacturing | 21% |
| Canada | 3 | Sales, Distribution | 26% |
| Mexico | 4 | Manufacturing | 30% |
| Brazil | 3 | Manufacturing, Sales | 34% |
| China | 2 | Manufacturing | 25% |
| Singapore | 1 | Regional HQ | 17% |
| Japan | 1 | Sales | 30% |
| Australia | 1 | Sales | 30% |

**Total: 75 Constituent Entities across 20 jurisdictions**

---

## Phase 1: Pre-Filing Preparation

### Step 1.1: Confirm Scope and Timeline

**Scope Confirmation:**

```
SCOPE CONFIRMATION CHECKLIST
============================

□ Consolidated revenue exceeds €750 million threshold
  FY2023: €1.2 billion ✓
  FY2024: €1.35 billion ✓

□ First fiscal year in scope identified
  FY2024 (year beginning 1 January 2024) ✓

□ Filing deadline calculated
  Standard: 15 months = 31 March 2026
  Transitional (first year): 18 months = 30 June 2026 ✓

□ All Constituent Entities identified
  75 entities across 20 jurisdictions ✓

□ Excluded entities identified
  None (no pension funds, investment entities, etc.) ✓
```

### Step 1.2: Designate Filing Entity

GlobalTech Manufacturing Ltd (UK) will file as the Ultimate Parent Entity. No separate DFE designation is required as the UPE is in a GloBE-implementing jurisdiction.

**Filing Entity Details:**

| Field | Value |
|-------|-------|
| Legal Name | GlobalTech Manufacturing Ltd |
| Jurisdiction | United Kingdom |
| Role | Ultimate Parent Entity (UPE) |
| Tax ID (UTR) | 1234567890 |
| Company Registration | 01234567 |
| Contact | tax.department@globaltech.com |

### Step 1.3: Assess Safe Harbour Eligibility

**Transitional CbCR Safe Harbour Assessment:**

| Jurisdiction | Revenue | PBT | ETR Est. | De Minimis? | ETR ≥15%? | Safe Harbour? |
|--------------|---------|-----|----------|-------------|-----------|---------------|
| UK | €320m | €48m | 23% | No | Yes | **Yes** |
| Germany | €280m | €35m | 29% | No | Yes | **Yes** |
| Netherlands | €45m | €12m | 25% | No | Yes | **Yes** |
| France | €180m | €22m | 25% | No | Yes | **Yes** |
| Spain | €95m | €11m | 25% | No | Yes | **Yes** |
| Italy | €55m | €5m | 24% | No | Yes | **Yes** |
| Poland | €85m | €9m | 19% | No | Yes | **Yes** |
| Czech Republic | €40m | €4m | 19% | No | Yes | **Yes** |
| **Ireland** | €120m | €28m | 12.5% | No | **No** | **No** |
| **Switzerland** | €65m | €18m | 14% | No | **No** | **No** |
| USA | €150m | €18m | 21% | No | Yes | **Yes** |
| Canada | €35m | €3m | 26% | No | Yes | **Yes** |
| Mexico | €60m | €6m | 30% | No | Yes | **Yes** |
| Brazil | €25m | €2m | 34% | No | Yes | **Yes** |
| China | €30m | €3m | 25% | No | Yes | **Yes** |
| Singapore | €8m | €0.8m | 17% | **Yes** | Yes | **Yes** |
| Japan | €12m | €1.2m | 30% | No | Yes | **Yes** |
| Australia | €7m | €0.5m | 30% | **Yes** | Yes | **Yes** |

**Key Finding:** Ireland and Switzerland fail the Simplified ETR test (ETR <15%). Full GloBE calculations required for these jurisdictions.

---

## Phase 2: Data Collection

### Step 2.1: Section 1 - Group Information Data

**Ultimate Parent Entity Details:**

```
SECTION 1 DATA COLLECTION
=========================

1.1 FILING ENTITY INFORMATION

Filing Entity Role: Ultimate Parent Entity
Legal Name: GlobalTech Manufacturing Ltd
Trade Name: GlobalTech Group
Jurisdiction of Incorporation: GB (United Kingdom)
Jurisdiction of Tax Residence: GB (United Kingdom)
Tax Identification Number: 1234567890 (UTR)
Address:
  Street: 100 Innovation Way
  City: Manchester
  Postal Code: M1 1AA
  Country: United Kingdom

1.2 MNE GROUP IDENTIFICATION

MNE Group Name: GlobalTech Manufacturing Group
Reporting Fiscal Year: 2024
Fiscal Year Start: 2024-01-01
Fiscal Year End: 2024-12-31

1.3 ACCOUNTING INFORMATION

Accounting Standard: IFRS
Consolidated Revenue (EUR): 1,350,000,000
Currency: EUR
Exchange Rate Source: ECB average annual rate
```

**Corporate Structure Information:**

```
CONSTITUENT ENTITY LISTING (Summary)
====================================

Total Constituent Entities: 75
Entities by Type:
  - Ultimate Parent Entity: 1
  - Intermediate Parent Entities: 5
  - Operating Entities: 62
  - Holding/Finance Entities: 7
  - Permanent Establishments: 0

Excluded Entities: 0
Joint Ventures: 0
Minority-Owned CEs: 0
```

### Step 2.2: Section 2 - Jurisdictional Data

**Full GloBE Calculation Jurisdictions (Ireland & Switzerland):**

#### Ireland - Detailed Calculation

```
IRELAND - GLOBE CALCULATION
===========================

CONSTITUENT ENTITIES:
1. GT IP Holdings Ltd (IP holding)
2. GT Services Ireland Ltd (Shared services)
3. GT Technology Ireland Ltd (R&D)
4. GT Sales Ireland Ltd (Sales support)

STEP 1: GLOBE INCOME

Financial Accounting Net Income (aggregate)    €28,000,000

GloBE Adjustments:
  + Net taxes included in income               €3,500,000
  + Excluded dividends add-back                        €0
  + Excluded equity gains add-back                     €0
  - Policy disallowed expenses                  (€200,000)
  + Stock-based compensation adjustment         €1,200,000
  +/- Other adjustments                          €300,000
                                              ────────────
GloBE Income                                   €32,800,000

STEP 2: ADJUSTED COVERED TAXES

Current Tax Expense                             €3,200,000
Deferred Tax Expense                              €800,000
                                              ────────────
Total Tax Expense                               €4,000,000

Adjustments:
  - Taxes related to uncertain positions         (€150,000)
  - Non-Covered Taxes                            (€50,000)
                                              ────────────
Adjusted Covered Taxes                          €3,800,000

STEP 3: EFFECTIVE TAX RATE

ETR = €3,800,000 / €32,800,000 = 11.59%

STEP 4: TOP-UP TAX PERCENTAGE

Top-up Tax % = 15% - 11.59% = 3.41%

STEP 5: SUBSTANCE-BASED INCOME EXCLUSION

Eligible Payroll Costs:
  GT IP Holdings Ltd                            €2,500,000
  GT Services Ireland Ltd                       €8,200,000
  GT Technology Ireland Ltd                     €6,800,000
  GT Sales Ireland Ltd                          €1,500,000
                                              ────────────
  Total Eligible Payroll                       €19,000,000
  × Payroll Carve-out Rate (9.8%)              ×     9.8%
                                              ────────────
  Payroll SBIE                                  €1,862,000

Tangible Assets (NBV):
  GT IP Holdings Ltd                              €500,000
  GT Services Ireland Ltd                       €3,200,000
  GT Technology Ireland Ltd                    €12,500,000
  GT Sales Ireland Ltd                            €800,000
                                              ────────────
  Total Tangible Assets                        €17,000,000
  × Asset Carve-out Rate (7.8%)                ×     7.8%
                                              ────────────
  Asset SBIE                                    €1,326,000

Total SBIE                                      €3,188,000

STEP 6: EXCESS PROFIT

GloBE Income                                   €32,800,000
Less: SBIE                                     (€3,188,000)
                                              ────────────
Excess Profit                                  €29,612,000

STEP 7: TOP-UP TAX

Top-up Tax = €29,612,000 × 3.41% = €1,009,769

Rounded: €1,010,000
```

#### Switzerland - Detailed Calculation

```
SWITZERLAND - GLOBE CALCULATION
===============================

CONSTITUENT ENTITIES:
1. GT Trading AG (Principal trading)
2. GT Finance AG (Treasury operations)

STEP 1: GLOBE INCOME

Financial Accounting Net Income (aggregate)    €18,000,000

GloBE Adjustments:
  + Net taxes included in income               €2,520,000
  - Policy disallowed expenses                  (€100,000)
  +/- Other adjustments                          €180,000
                                              ────────────
GloBE Income                                   €20,600,000

STEP 2: ADJUSTED COVERED TAXES

Current Tax Expense                             €2,200,000
Deferred Tax Expense                              €400,000
                                              ────────────
Total Tax Expense                               €2,600,000

Adjustments:
  - Taxes related to uncertain positions          (€80,000)
                                              ────────────
Adjusted Covered Taxes                          €2,520,000

STEP 3: EFFECTIVE TAX RATE

ETR = €2,520,000 / €20,600,000 = 12.23%

STEP 4: TOP-UP TAX PERCENTAGE

Top-up Tax % = 15% - 12.23% = 2.77%

STEP 5: SUBSTANCE-BASED INCOME EXCLUSION

Eligible Payroll Costs:
  GT Trading AG                                 €4,500,000
  GT Finance AG                                 €2,800,000
                                              ────────────
  Total Eligible Payroll                        €7,300,000
  × Payroll Carve-out Rate (9.8%)              ×     9.8%
                                              ────────────
  Payroll SBIE                                    €715,400

Tangible Assets (NBV):
  GT Trading AG                                 €1,200,000
  GT Finance AG                                   €600,000
                                              ────────────
  Total Tangible Assets                         €1,800,000
  × Asset Carve-out Rate (7.8%)                ×     7.8%
                                              ────────────
  Asset SBIE                                      €140,400

Total SBIE                                        €855,800

STEP 6: EXCESS PROFIT

GloBE Income                                   €20,600,000
Less: SBIE                                      (€855,800)
                                              ────────────
Excess Profit                                  €19,744,200

STEP 7: TOP-UP TAX

Top-up Tax = €19,744,200 × 2.77% = €546,912

Rounded: €547,000
```

**Note:** Switzerland enacted a QDMTT effective 2024. The QDMTT is expected to collect this Top-up Tax domestically. The GIR will show QDMTT offset.

### Step 2.3: Section 3 - Entity Data

**Section 3 requires entity-level detail for jurisdictions with Top-up Tax exposure (Ireland, Switzerland) and summary data for safe harbour jurisdictions.**

```
SECTION 3 ENTITY DATA - IRELAND
===============================

Entity 1: GT IP Holdings Ltd
──────────────────────────────
Entity Type: Constituent Entity
Tax Residence: Ireland
TIN: IE1234567A
Ownership: 100% (direct)
GloBE Income: €15,200,000
Covered Taxes: €1,750,000
Entity ETR: 11.51%
Eligible Payroll: €2,500,000
Tangible Assets: €500,000
SBIE: €284,000
Excess Profit: €14,916,000
Top-up Tax Allocation: €508,626

Entity 2: GT Services Ireland Ltd
──────────────────────────────────
Entity Type: Constituent Entity
Tax Residence: Ireland
TIN: IE2345678B
Ownership: 100% (indirect via GT Holdings Europe BV)
GloBE Income: €8,500,000
Covered Taxes: €1,020,000
Entity ETR: 12.00%
Eligible Payroll: €8,200,000
Tangible Assets: €3,200,000
SBIE: €1,053,200
Excess Profit: €7,446,800
Top-up Tax Allocation: €253,921

Entity 3: GT Technology Ireland Ltd
────────────────────────────────────
Entity Type: Constituent Entity
Tax Residence: Ireland
TIN: IE3456789C
Ownership: 100% (indirect)
GloBE Income: €7,800,000
Covered Taxes: €858,000
Entity ETR: 11.00%
Eligible Payroll: €6,800,000
Tangible Assets: €12,500,000
SBIE: €1,641,400
Excess Profit: €6,158,600
Top-up Tax Allocation: €210,003

Entity 4: GT Sales Ireland Ltd
───────────────────────────────
Entity Type: Constituent Entity
Tax Residence: Ireland
TIN: IE4567890D
Ownership: 100% (indirect)
GloBE Income: €1,300,000
Covered Taxes: €172,000
Entity ETR: 13.23%
Eligible Payroll: €1,500,000
Tangible Assets: €800,000
SBIE: €209,400
Excess Profit: €1,090,600
Top-up Tax Allocation: €37,450

TOTAL IRELAND TOP-UP TAX: €1,010,000
```

---

## Phase 3: GIR Completion

### Step 3.1: Section 1 - Completing the GIR

**Section 1: MNE Group Information**

```xml
<!-- GIR SECTION 1: GROUP INFORMATION -->

<GIRBody>
  <FilingInfo>
    <FilingCE>
      <ResCountryCode>GB</ResCountryCode>
      <TIN issuedBy="GB">1234567890</TIN>
      <Name>GlobalTech Manufacturing Ltd</Name>
      <Address>
        <Street>100 Innovation Way</Street>
        <City>Manchester</City>
        <PostCode>M1 1AA</PostCode>
        <CountryCode>GB</CountryCode>
      </Address>
    </FilingCE>

    <MNEGroup>
      <Name>GlobalTech Manufacturing Group</Name>
    </MNEGroup>

    <AccountingInfo>
      <AccountingStandard>IFRS</AccountingStandard>
      <ConsolidatedRevenue currCode="EUR">1350000000</ConsolidatedRevenue>
    </AccountingInfo>

    <ReportingFY>
      <StartDate>2024-01-01</StartDate>
      <EndDate>2024-12-31</EndDate>
    </ReportingFY>

    <FilingObligationMet>
      <JurisdictionCode>GB</JurisdictionCode>
    </FilingObligationMet>
  </FilingInfo>
```

**Elections Made:**

| Election | Applied | Scope |
|----------|---------|-------|
| Transitional Simplified Reporting | Yes | Group-wide |
| Stock-Based Compensation | Yes | Ireland entities |
| GloBE Loss Election | No | N/A |
| Realisation Basis | No | N/A |

### Step 3.2: Section 2 - Jurisdictional Reporting

**Safe Harbour Jurisdictions (16 jurisdictions):**

```xml
<!-- SECTION 2: SAFE HARBOUR JURISDICTIONS -->

<JurisdictionInfo>
  <!-- United Kingdom - Safe Harbour -->
  <Jurisdiction>
    <JurisdictionCode>GB</JurisdictionCode>
    <NumberOfCEs>8</NumberOfCEs>
    <SafeHarbour>
      <Type>TransitionalCbCR</Type>
      <TestApplied>SimplifiedETR</TestApplied>
      <CbCRRevenue currCode="EUR">320000000</CbCRRevenue>
      <CbCRPBT currCode="EUR">48000000</CbCRPBT>
      <SimplifiedCoveredTaxes currCode="EUR">11040000</SimplifiedCoveredTaxes>
      <SimplifiedETR>23.00</SimplifiedETR>
      <TransitionRate>15.00</TransitionRate>
      <TestResult>Pass</TestResult>
    </SafeHarbour>
    <TopUpTax currCode="EUR">0</TopUpTax>
  </Jurisdiction>

  <!-- Germany - Safe Harbour -->
  <Jurisdiction>
    <JurisdictionCode>DE</JurisdictionCode>
    <NumberOfCEs>12</NumberOfCEs>
    <SafeHarbour>
      <Type>TransitionalCbCR</Type>
      <TestApplied>SimplifiedETR</TestApplied>
      <CbCRRevenue currCode="EUR">280000000</CbCRRevenue>
      <CbCRPBT currCode="EUR">35000000</CbCRPBT>
      <SimplifiedCoveredTaxes currCode="EUR">10150000</SimplifiedCoveredTaxes>
      <SimplifiedETR>29.00</SimplifiedETR>
      <TransitionRate>15.00</TransitionRate>
      <TestResult>Pass</TestResult>
    </SafeHarbour>
    <TopUpTax currCode="EUR">0</TopUpTax>
  </Jurisdiction>

  <!-- Singapore - De Minimis Safe Harbour -->
  <Jurisdiction>
    <JurisdictionCode>SG</JurisdictionCode>
    <NumberOfCEs>1</NumberOfCEs>
    <SafeHarbour>
      <Type>TransitionalCbCR</Type>
      <TestApplied>DeMinimis</TestApplied>
      <CbCRRevenue currCode="EUR">8000000</CbCRRevenue>
      <CbCRPBT currCode="EUR">800000</CbCRPBT>
      <TestResult>Pass</TestResult>
    </SafeHarbour>
    <TopUpTax currCode="EUR">0</TopUpTax>
  </Jurisdiction>

  <!-- [Additional safe harbour jurisdictions follow same pattern] -->
</JurisdictionInfo>
```

**Full Calculation Jurisdictions:**

```xml
<!-- SECTION 2: FULL CALCULATION JURISDICTIONS -->

<JurisdictionInfo>
  <!-- Ireland - Full GloBE Calculation -->
  <Jurisdiction>
    <JurisdictionCode>IE</JurisdictionCode>
    <NumberOfCEs>4</NumberOfCEs>
    <SafeHarbour>
      <Applied>false</Applied>
    </SafeHarbour>
    <GloBECalculation>
      <GloBEIncome currCode="EUR">32800000</GloBEIncome>
      <AdjustedCoveredTaxes currCode="EUR">3800000</AdjustedCoveredTaxes>
      <ETR>11.59</ETR>
      <TopUpTaxPercentage>3.41</TopUpTaxPercentage>
      <EligiblePayroll currCode="EUR">19000000</EligiblePayroll>
      <TangibleAssets currCode="EUR">17000000</TangibleAssets>
      <SBIE currCode="EUR">3188000</SBIE>
      <ExcessProfit currCode="EUR">29612000</ExcessProfit>
      <TopUpTax currCode="EUR">1010000</TopUpTax>
      <QDMTTOffset currCode="EUR">0</QDMTTOffset>
      <IIRTopUpTax currCode="EUR">1010000</IIRTopUpTax>
    </GloBECalculation>
  </Jurisdiction>

  <!-- Switzerland - Full GloBE Calculation with QDMTT -->
  <Jurisdiction>
    <JurisdictionCode>CH</JurisdictionCode>
    <NumberOfCEs>2</NumberOfCEs>
    <SafeHarbour>
      <Applied>false</Applied>
    </SafeHarbour>
    <GloBECalculation>
      <GloBEIncome currCode="EUR">20600000</GloBEIncome>
      <AdjustedCoveredTaxes currCode="EUR">2520000</AdjustedCoveredTaxes>
      <ETR>12.23</ETR>
      <TopUpTaxPercentage>2.77</TopUpTaxPercentage>
      <EligiblePayroll currCode="EUR">7300000</EligiblePayroll>
      <TangibleAssets currCode="EUR">1800000</TangibleAssets>
      <SBIE currCode="EUR">855800</SBIE>
      <ExcessProfit currCode="EUR">19744200</ExcessProfit>
      <TopUpTax currCode="EUR">547000</TopUpTax>
      <QDMTTOffset currCode="EUR">547000</QDMTTOffset>
      <IIRTopUpTax currCode="EUR">0</IIRTopUpTax>
    </GloBECalculation>
    <QDMTT>
      <QDMTTApplied>true</QDMTTApplied>
      <QDMTTAmount currCode="EUR">547000</QDMTTAmount>
      <QDMTTJurisdictionStatus>TransitionalQualified</QDMTTJurisdictionStatus>
    </QDMTT>
  </Jurisdiction>
</JurisdictionInfo>
```

### Step 3.3: Section 3 - Entity Detail

**For Ireland entities (full calculation required):**

```xml
<!-- SECTION 3: ENTITY DATA - IRELAND -->

<EntityInfo>
  <Entity>
    <Name>GT IP Holdings Ltd</Name>
    <JurisdictionCode>IE</JurisdictionCode>
    <TIN issuedBy="IE">IE1234567A</TIN>
    <EntityType>CE</EntityType>
    <OwnershipPercentage>100.00</OwnershipPercentage>
    <GloBEData>
      <GloBEIncome currCode="EUR">15200000</GloBEIncome>
      <CoveredTaxes currCode="EUR">1750000</CoveredTaxes>
      <EligiblePayroll currCode="EUR">2500000</EligiblePayroll>
      <TangibleAssets currCode="EUR">500000</TangibleAssets>
      <SBIE currCode="EUR">284000</SBIE>
      <TopUpTaxAllocation currCode="EUR">508626</TopUpTaxAllocation>
    </GloBEData>
  </Entity>

  <Entity>
    <Name>GT Services Ireland Ltd</Name>
    <JurisdictionCode>IE</JurisdictionCode>
    <TIN issuedBy="IE">IE2345678B</TIN>
    <EntityType>CE</EntityType>
    <OwnershipPercentage>100.00</OwnershipPercentage>
    <GloBEData>
      <GloBEIncome currCode="EUR">8500000</GloBEIncome>
      <CoveredTaxes currCode="EUR">1020000</CoveredTaxes>
      <EligiblePayroll currCode="EUR">8200000</EligiblePayroll>
      <TangibleAssets currCode="EUR">3200000</TangibleAssets>
      <SBIE currCode="EUR">1053200</SBIE>
      <TopUpTaxAllocation currCode="EUR">253921</TopUpTaxAllocation>
    </GloBEData>
  </Entity>

  <!-- Additional entities follow same pattern -->
</EntityInfo>
```

---

## Phase 4: Validation and Filing

### Step 4.1: XML Validation

**Validation Checklist:**

```
XML VALIDATION CHECKLIST
========================

SCHEMA VALIDATION
□ XML validates against January 2025 GIR Schema
□ All mandatory elements populated
□ Data types correct (dates, currencies, percentages)
□ TIN formats valid for each jurisdiction
□ ISO country codes used correctly

BUSINESS RULE VALIDATION
□ Sum of entity Top-up Tax = Jurisdictional Top-up Tax
□ ETR calculation: Covered Taxes / GloBE Income = stated ETR
□ SBIE = (Payroll × rate) + (Assets × rate)
□ Excess Profit = GloBE Income - SBIE
□ Top-up Tax = Excess Profit × Top-up Tax %

CONSISTENCY CHECKS
□ Filing Entity TIN matches registration
□ Fiscal year dates correct
□ Currency codes consistent (EUR)
□ All CEs accounted for (75 entities)
□ All jurisdictions covered (20 jurisdictions)

SAFE HARBOUR VALIDATION
□ CbCR data matches filed CbCR
□ Simplified ETR calculated correctly
□ Transition rate correct for FY2024 (15%)
□ Test results (Pass/Fail) accurate
```

### Step 4.2: Filing Across Jurisdictions

**Filing Strategy:**

GlobalTech Manufacturing Ltd files the GIR with HMRC (UK). Under the GIR MCAA, HMRC exchanges the relevant jurisdictional data with other competent authorities.

**Filing Timeline:**

| Milestone | Date | Action |
|-----------|------|--------|
| FY End | 31 December 2024 | Fiscal year closes |
| Data Collection | January - June 2025 | Gather all CE data |
| GIR Preparation | July - December 2025 | Complete GIR sections |
| Internal Review | January - February 2026 | Quality control |
| Management Approval | March 2026 | Sign-off |
| Filing | April - May 2026 | Submit to HMRC |
| **Deadline** | **30 June 2026** | **Transitional 18-month deadline** |

**Filing Submission:**

```
FILING SUBMISSION DETAILS
=========================

Filing Authority: HMRC (United Kingdom)
Submission Method: XML via MTT Online Service
Filing Date: [Insert actual date]
Confirmation Reference: [HMRC Reference]

Jurisdictions Covered by Exchange:
□ Germany (via GIR MCAA)
□ Netherlands (via GIR MCAA)
□ France (via GIR MCAA)
□ Ireland (via GIR MCAA)
□ Switzerland (via GIR MCAA)
□ [All other GIR MCAA jurisdictions]

Local Filing Requirements:
□ UK MTT Self-Assessment Return - filed separately
□ Switzerland QDMTT Return - filed locally
```

### Step 4.3: Local Compliance

**UK Multinational Top-up Tax (MTT) Return:**

In addition to the GIR, GlobalTech Manufacturing Ltd must file a UK MTT Self-Assessment return reporting the IIR Top-up Tax charge.

```
UK MTT SELF-ASSESSMENT SUMMARY
==============================

IIR Charge - Ireland:
  Top-up Tax on Irish CEs              €1,010,000
  Converted to GBP (rate 0.86)         £868,600

IIR Charge - Switzerland:
  Top-up Tax on Swiss CEs              €547,000
  Less: QDMTT offset                  (€547,000)
  Net IIR Charge                              €0

Total UK MTT Liability:                £868,600

Payment Deadline: Aligned with GIR deadline
```

---

## Phase 5: Documentation and Retention

### Step 5.1: Filing Package

**Complete Documentation Set:**

```
GLOBALTECH GIR FILING PACKAGE - FY2024
======================================

Volume 1: Filed Returns
├── GIR XML file (submitted)
├── GIR PDF summary
├── HMRC filing confirmation
├── UK MTT Self-Assessment
└── Switzerland QDMTT return

Volume 2: Section 1 Support
├── Corporate structure chart
├── Constituent Entity register
├── Ownership percentages
└── Filing Entity confirmation

Volume 3: Section 2 - Safe Harbour
├── CbCR qualification checklist (per jurisdiction)
├── Simplified ETR calculations (16 jurisdictions)
├── De Minimis calculations (2 jurisdictions)
├── Transition rate confirmation
└── Safe harbour summary

Volume 4: Section 2 - Full Calculations
├── Ireland GloBE workpaper
├── Switzerland GloBE workpaper
├── SBIE calculations (Ireland, Switzerland)
├── Covered Taxes analysis
└── Top-up Tax allocation

Volume 5: Section 3 Support
├── Entity data schedules (Ireland - 4 entities)
├── Entity data schedules (Switzerland - 2 entities)
├── TIN verification
└── Ownership documentation

Volume 6: Governance
├── Management approval memo
├── Sign-off chain documentation
├── Board paper (if applicable)
└── Advisor review notes
```

### Step 5.2: Lessons Learned

**Key Observations from First Filing:**

| Area | Observation | Recommendation |
|------|-------------|----------------|
| **Data Collection** | Ireland entities had delayed data | Build 2-month buffer |
| **Safe Harbour** | 16 of 18 jurisdictions qualified | Review Ireland/CH annually |
| **QDMTT** | Switzerland QDMTT offset eliminated IIR | Monitor QDMTT jurisdictions |
| **XML Validation** | Three validation errors on first attempt | Test with sandbox first |
| **Timeline** | Started preparation too late | Begin July of filing year |

---

## Deliverable: Complete Worked Example Files

### Summary Output

```
GLOBALTECH MANUFACTURING GROUP
GIR FILING SUMMARY - FY2024
===========================

FILING DETAILS
--------------
Filing Entity: GlobalTech Manufacturing Ltd
Filing Jurisdiction: United Kingdom
Reporting Period: 1 January 2024 - 31 December 2024
Filing Deadline: 30 June 2026
Actual Filing Date: [TBD]

GROUP SUMMARY
-------------
Total Constituent Entities: 75
Total Jurisdictions: 20
Consolidated Revenue: €1,350,000,000

SAFE HARBOUR APPLICATION
------------------------
Jurisdictions with Safe Harbour: 16
  - Simplified ETR Test: 14
  - De Minimis Test: 2
Jurisdictions requiring Full Calculation: 2
  - Ireland (ETR 11.59%)
  - Switzerland (ETR 12.23%)

TOP-UP TAX SUMMARY
------------------
                        Gross Top-up    QDMTT        Net IIR
                        Tax             Offset       Charge
                        ─────────────   ─────────    ─────────
Ireland                 €1,010,000      €0           €1,010,000
Switzerland             €547,000        (€547,000)   €0
                        ─────────────   ─────────    ─────────
TOTAL                   €1,557,000      (€547,000)   €1,010,000

UK MTT LIABILITY
----------------
IIR Charge (EUR): €1,010,000
IIR Charge (GBP): £868,600

ELECTIONS MADE
--------------
☑ Transitional Simplified Reporting
☑ Stock-Based Compensation Election (Ireland)
☐ GloBE Loss Election
☐ Realisation Basis Election

PREPARED BY: _________________________ DATE: ____________

REVIEWED BY: _________________________ DATE: ____________

APPROVED BY: _________________________ DATE: ____________
```

---

## Section Summary

This worked example demonstrates the complete GIR filing process for a standard MNE group:

1. **Scoping** - 75 entities across 20 jurisdictions; first year FY2024
2. **Safe Harbour Assessment** - 16 jurisdictions qualify; 2 require full calculation
3. **Full GloBE Calculations** - Ireland (ETR 11.59%) and Switzerland (ETR 12.23%)
4. **Top-up Tax** - €1.01m in Ireland; Switzerland offset by QDMTT
5. **GIR Completion** - All three sections populated per January 2025 schema
6. **Filing** - Via HMRC with MCAA exchange to partner jurisdictions
7. **Documentation** - Comprehensive filing package for retention

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Safe Harbour Value** | 16 of 18 jurisdictions avoided full calculations |
| **Low-Tax Jurisdictions** | Ireland/Switzerland required detailed work |
| **QDMTT Impact** | Swiss QDMTT eliminated IIR charge for that jurisdiction |
| **Filing Coordination** | Single GIR filing with MCAA exchange |
| **Net Liability** | €1.01m IIR charge (Ireland only) |
| **First Year Extended Deadline** | 18 months provides additional preparation time |
| **Documentation** | Comprehensive package essential for audit defence |

---

## Sources

Key references for this section include:

- [OECD GloBE Information Return XML Schema (January 2025)](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html)
- [OECD GloBE Information Return Guidance (January 2025)](https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html)
- [HMRC MTT Administration Manual](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt52100)

---

*Section 10.1 Complete. Proceed to Section 10.2: Scenario 2 - Complex Ownership Structure.*
