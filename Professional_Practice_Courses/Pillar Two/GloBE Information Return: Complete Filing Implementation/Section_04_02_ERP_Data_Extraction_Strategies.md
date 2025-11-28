# Section 4.2: ERP Data Extraction Strategies

## Introduction

Extracting the ~480 data points required for the GloBE Information Return from enterprise systems represents one of the most significant technical challenges in Pillar Two compliance. Unlike traditional tax compliance, which typically relies on entity-level trial balances, GIR preparation requires multi-entity aggregation at the jurisdictional level, integration of financial and non-financial data, and granularity that many ERP systems were not designed to provide.

This section provides implementation-focused guidance for extracting GIR-relevant data from the major ERP platforms: SAP, Oracle, Microsoft Dynamics, and NetSuite. For each platform, you will find:

- **Relevant tables, modules, and data structures** for GIR data points
- **Extraction methodologies** and recommended approaches
- **GIR field mapping** to source system locations
- **Common challenges** and practical workarounds
- **Template references** for data extraction specifications

> **Critical Context**: Research indicates that Pillar Two compliance requires pulling data from approximately 150-250 data points per entity across multiple countries. Organizations using multiple ERPs or ledgers with different charts of accounts face additional data mapping complexity. The jurisdictional-level calculations required by GloBE Rules represent a substantial change from traditional single-entity income tax calculations.

---

## 4.2.1 SAP Extraction

SAP environments (both ECC and S/4HANA) contain most of the financial data required for GIR preparation, though extraction strategies differ significantly between legacy ECC systems and modern S/4HANA implementations.

### SAP's Pillar Two Solution Architecture

SAP has developed **SAP Profitability and Performance Management (PaPM)** as the primary technological solution for Pillar Two compliance. SAP PaPM combines functionalities of:

- **Data aggregator** - Collecting data from multiple SAP and non-SAP source systems
- **Calculation engine** - Performing GloBE computations
- **Simulation software** - Modeling scenarios and elections
- **Analysis tool** - Reporting and audit trail maintenance

> **Implementation Note**: While SAP PaPM is the recommended solution for organizations with SAP environments, smaller implementations may use manual extraction approaches with Excel-based calculators during the initial compliance years.

### Key Financial Tables in SAP

#### Universal Journal (S/4HANA)

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| **ACDOCA** | Universal Journal Entry Line Items | Primary source for all financial transactions; consolidates FI and CO data |
| **ACDOCP** | Plan Data (Universal Journal) | Budget and forecast data for planning scenarios |
| **ACDOCU** | Universal Journal Entry (Currencies) | Multi-currency amounts for currency conversion |

The **ACDOCA** table in SAP S/4HANA serves as the centralized repository for financial and controlling data. It consolidates information from various modules, enabling real-time reporting and eliminating the need to reconcile separate FI and CO ledgers.

**Key ACDOCA Fields for GIR Data Points:**

| Field | Description | GIR Data Point |
|-------|-------------|----------------|
| RBUKRS | Company Code | Entity identification |
| RACCT | Account Number | Income/expense classification |
| RHCUR | Local Currency | Local currency amounts |
| HSL | Amount in Local Currency | Financial statement values |
| TSL | Amount in Transaction Currency | Original transaction amounts |
| KSL | Amount in Controlling Area Currency | Group reporting currency |
| FISCYEARPER | Fiscal Year/Period | Period-level data |
| DRCRK | Debit/Credit Indicator | Amount direction |
| AWTYP | Reference Transaction | Transaction type identification |

#### Legacy Tables (ECC and S/4HANA Compatibility)

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| **BKPF** | Accounting Document Header | Document-level header information |
| **BSEG** | Accounting Document Segment | Line item details for transactions |
| **SKA1** | G/L Account Master (Chart of Accounts) | Account classification |
| **SKAT** | G/L Account Texts | Account descriptions |
| **T001** | Company Codes | Entity master data |
| **CSKS** | Cost Center Master Data | Cost center information |
| **ANLC** | Asset Value Fields | Fixed asset book values |
| **ANLA** | Asset Master Record | Asset master data |

**BKPF/BSEG Relationship:**
- **BKPF** stores header-level information (company code, document number, fiscal year)
- **BSEG** contains line item details (account number, amounts, tax information)
- Join on fields: MANDT, BUKRS, GJAHR, BELNR

> **S/4HANA Note**: In S/4HANA, ACDOCA replaces BSEG for reporting purposes. BSEG remains primarily as an open item registry and data entry view for manually posted FI documents.

### Tax-Specific Tables

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| **BSET** | Tax Data Document Segment | Tax amounts and tax codes |
| **T007A** | Tax Keys | Tax code definitions |
| **T007S** | Tax Code Texts | Tax code descriptions |
| **J_1BTXOF1** | Tax Official Table (Brazil) | Country-specific tax data |
| **FAGL_SPLINFO** | Splitting Information | Tax splitting details |
| **DFKKOP** | Open Items (Contract Accounting) | Tax position items |

### HR and Payroll Tables (for SBIE Calculations)

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| **PA0001** | HR Master - Organizational Assignment | Employee entity assignment |
| **PA0008** | HR Master - Basic Pay | Salary components |
| **PCL2** | Payroll Results Cluster | Payroll wage types |
| **T512T** | Wage Type Texts | Wage type descriptions |
| **HRP1001** | HR Infotype 1001 - Relationships | Organizational relationships |

### Fixed Asset Tables (for SBIE Calculations)

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| **ANLA** | Asset Master Record | Asset identification |
| **ANLB** | Depreciation Terms | Depreciation parameters |
| **ANLC** | Asset Value Fields | Book values and depreciation |
| **ANLZ** | Asset Time-Dependent Data | Asset location/cost center |
| **ANEK** | Document Header Asset Posting | Asset transaction headers |
| **ANEP** | Asset Line Items | Asset transaction details |

### SAP Transaction Codes for Data Extraction

| Transaction Code | Description | Use Case |
|------------------|-------------|----------|
| **SE16/SE16N** | Data Browser | Direct table queries |
| **FAGLL03** | G/L Account Line Item Display | Financial line items |
| **FBL3N** | G/L Account Line Items | General ledger inquiry |
| **S_ALR_87012284** | G/L Line Items | Financial statement data |
| **AW01N** | Asset Explorer | Fixed asset values |
| **SQ01** | SAP Query | Custom queries |
| **SQVI** | QuickViewer | Ad-hoc reporting |
| **SM30** | Table Maintenance | Master data views |

### CDS Views for Data Extraction

SAP S/4HANA provides Core Data Services (CDS) views as the recommended extraction method. The number of released CDS extractors has grown from approximately 500 in S/4HANA 2019 to approximately 4,700 in release 2025.

**Relevant CDS View Categories:**

| View Category | Example Views | GIR Application |
|---------------|---------------|-----------------|
| Financial Line Items | I_JournalEntry, I_GLAccountLineItem | Income/expense extraction |
| Asset Accounting | I_FixedAsset, I_AssetBookValue | SBIE tangible asset data |
| Cost Center | I_CostCenter | Cost center allocations |
| Consolidation | I_ConsolidationUnit | Group structure data |
| Legal Entity | I_CompanyCode | Entity master information |

### SAP-to-GIR Data Mapping Template

**Section 3: GloBE Income Computation Mapping**

| GIR Data Point | SAP Table | SAP Field | Extraction Logic |
|----------------|-----------|-----------|------------------|
| Revenue | ACDOCA | HSL | RACCT in revenue account range |
| Cost of Sales | ACDOCA | HSL | RACCT in COGS account range |
| Operating Expenses | ACDOCA | HSL | RACCT in OpEx account range |
| Interest Income | ACDOCA | HSL | RACCT in interest income range |
| Interest Expense | ACDOCA | HSL | RACCT in interest expense range |
| Tax Expense (Current) | BSET/ACDOCA | HSL | HKONT = current tax accounts |
| Tax Expense (Deferred) | ACDOCA | HSL | HKONT = deferred tax accounts |
| Depreciation | ANLC | AFABE | Calculated depreciation |
| Eligible Payroll Costs | PCL2/PA0008 | Various | Sum of eligible wage types |
| Tangible Asset Book Value | ANLC | KANSW | Net book value by asset class |

### SAP Extraction Methodology

**Approach 1: SAP PaPM Integration (Recommended)**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAP PaPM Architecture                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │   SAP    │  │ Non-SAP  │  │  Excel   │  │  Other   │       │
│  │ S/4HANA  │  │   ERP    │  │  Files   │  │ Sources  │       │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
│       │             │             │             │              │
│       └─────────────┼─────────────┼─────────────┘              │
│                     │             │                            │
│                     ▼             ▼                            │
│              ┌──────────────────────────┐                      │
│              │    SAP PaPM Data Layer    │                      │
│              │  - Data Aggregation       │                      │
│              │  - Data Transformation    │                      │
│              │  - Data Validation        │                      │
│              └────────────┬─────────────┘                      │
│                           │                                    │
│                           ▼                                    │
│              ┌──────────────────────────┐                      │
│              │  GloBE Calculation Engine │                      │
│              │  - ETR Computation        │                      │
│              │  - SBIE Calculation       │                      │
│              │  - Top-up Tax Allocation  │                      │
│              └────────────┬─────────────┘                      │
│                           │                                    │
│                           ▼                                    │
│              ┌──────────────────────────┐                      │
│              │       GIR Output          │                      │
│              │  - XML Generation         │                      │
│              │  - Validation Reports     │                      │
│              │  - Audit Trail            │                      │
│              └──────────────────────────┘                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Approach 2: Manual Extraction via CDS Views**

For organizations without SAP PaPM, extract data using CDS views or direct table queries:

1. **Create Custom CDS View** for Pillar Two data extraction
2. **Schedule Extraction Jobs** using SAP Process Orchestration or similar
3. **Export to Excel/CSV** for loading into GIR calculator
4. **Map Extracted Data** to GIR data point requirements

**Approach 3: SAP Analytics Cloud Integration**

Use SAP Analytics Cloud to:
- Connect to S/4HANA via live connection
- Build Pillar Two-specific data models
- Create extraction queries for GIR data points
- Export to calculation tools or SAP PaPM

### Common SAP Extraction Challenges

| Challenge | Root Cause | Solution |
|-----------|------------|----------|
| Multiple company codes | Decentralized SAP implementation | Create consolidated extraction queries across company codes |
| Non-standard chart of accounts | Organic growth, acquisitions | Build account mapping tables to standardize extraction |
| Missing granularity | Transactions posted at summary level | Implement sub-account analysis or use allocation methods |
| Currency conversion | Multiple transaction currencies | Extract in local and group currency; use SAP translation tables |
| Intercompany elimination | IC transactions in separate module | Include SAP Intercompany module (ICR) in extraction scope |
| Deferred tax data | Tax provision in external system | Integrate with tax provision system or manual upload |

### SAP-to-GIR Mapping Guide Template

**Template Reference: SAP_to_GIR_Mapping_Guide.xlsx**

| Tab | Contents |
|-----|----------|
| 1. Overview | Mapping methodology and instructions |
| 2. GL Accounts | Chart of accounts to GIR income line mapping |
| 3. Tax Accounts | Tax accounts to Covered Taxes mapping |
| 4. Asset Classes | Asset class to SBIE tangible asset mapping |
| 5. Wage Types | Wage type to SBIE payroll cost mapping |
| 6. Entity Mapping | Company code to CE mapping |
| 7. Extraction Jobs | Scheduled extraction specifications |
| 8. Validation Rules | Data validation queries |

---

## 4.2.2 Oracle Extraction

Oracle environments include Oracle E-Business Suite (EBS), Oracle Cloud ERP (Fusion), and Oracle Cloud EPM. Oracle has developed specific Pillar Two capabilities within its EPM Tax Reporting module.

### Oracle Cloud EPM Tax Reporting for Pillar Two

In January 2024, Oracle announced new capabilities in Oracle Fusion Cloud Enterprise Performance Management (EPM) specifically designed for OECD Pillar Two requirements. The solution provides end-to-end capabilities for:

- **Top-up tax calculations** including GloBE Rules
- **Covered tax computation** and allocation
- **Effective tax rate reconciliation**
- **Tax liability determination**
- **GloBE Information Return generation**

### Oracle EPM Pillar Two Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              Oracle Cloud EPM Tax Reporting                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Data Collection Layer                                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                                                            │  │
│  │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │  │
│  │   │   ERP   │ │Subledger│ │Financial│ │   HR    │       │  │
│  │   │         │ │         │ │ Consol  │ │         │       │  │
│  │   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘       │  │
│  │        │           │           │           │             │  │
│  │        └───────────┴───────────┴───────────┘             │  │
│  │                        │                                  │  │
│  │        ┌───────────────┴───────────────┐                 │  │
│  │        │   Tax Provision  │   CbCR     │                 │  │
│  │        └───────────────────────────────┘                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│  Pillar Two Processing Layer                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │  │
│  │  │GloBE Income │  │ Covered Tax │  │    SBIE     │      │  │
│  │  │ Automation  │  │ Automation  │  │ Calculation │      │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │  │
│  │                                                          │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │  │
│  │  │     ETR     │  │  Top-up Tax │  │ Allocation  │      │  │
│  │  │ Calculation │  │ Computation │  │   Engine    │      │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│  Output Layer                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │  │
│  │  │     GIR     │  │   Reports   │  │Task Manager │      │  │
│  │  │  XML Output │  │ & Dashboards│  │  Workflow   │      │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Oracle Cloud ERP (Fusion) Data Sources

**General Ledger Module**

| Table/View | Description | GIR Relevance |
|------------|-------------|---------------|
| GL_JE_HEADERS | Journal Entry Headers | Document header information |
| GL_JE_LINES | Journal Entry Lines | Transaction line items |
| GL_CODE_COMBINATIONS | Chart of Accounts Segments | Account structure |
| GL_BALANCES | Account Balances | Period-end balance extraction |
| GL_LEDGERS | Ledger Definitions | Legal entity ledgers |

**Subledger Accounting**

| Table/View | Description | GIR Relevance |
|------------|-------------|---------------|
| XLA_AE_HEADERS | Subledger Accounting Headers | Subledger transaction headers |
| XLA_AE_LINES | Subledger Accounting Lines | Detailed transaction lines |
| XLA_TRANSACTION_ENTITIES | Transaction Entity Details | Entity-level source data |

**Fixed Assets**

| Table/View | Description | GIR Relevance |
|------------|-------------|---------------|
| FA_ADDITIONS | Asset Additions | Asset master records |
| FA_BOOKS | Asset Book Records | Depreciation and book values |
| FA_DEPRN_PERIODS | Depreciation Periods | Period-level depreciation |
| FA_DISTRIBUTION_HISTORY | Asset Distribution | Asset location/assignment |

**Payroll (Oracle HCM Cloud)**

| Table/View | Description | GIR Relevance |
|------------|-------------|---------------|
| PAY_RUN_RESULTS | Payroll Run Results | Calculated payroll amounts |
| PAY_ELEMENT_ENTRIES | Element Entries | Payroll element assignments |
| PER_ALL_PEOPLE_F | Person Records | Employee master data |
| PER_ALL_ASSIGNMENTS_F | Assignments | Employee entity assignment |

### Oracle E-Business Suite (EBS) Data Sources

**General Ledger**

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| GL_JE_HEADERS | Journal Headers | Document information |
| GL_JE_LINES | Journal Lines | Transaction details |
| GL_BALANCES | Account Balances | Financial position |
| GL_CODE_COMBINATIONS | Account Combinations | Account structure |
| GL_SETS_OF_BOOKS | Set of Books | Legal entity definition |

**Fixed Assets**

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| FA_ADDITIONS_B | Asset Master | Asset identification |
| FA_BOOKS | Book Controls | Depreciation parameters |
| FA_DEPRN_SUMMARY | Depreciation Summary | Asset values |
| FA_ADJUSTMENTS | Asset Adjustments | Value changes |

**Payroll**

| Table | Description | GIR Relevance |
|-------|-------------|---------------|
| PAY_RUN_RESULTS | Run Results | Payroll calculations |
| PAY_ASSIGNMENT_ACTIONS | Assignment Actions | Payroll processing |
| PER_ALL_PEOPLE_F | Person Records | Employee data |

### Oracle-to-GIR Data Mapping

**GloBE Income Mapping**

| GIR Data Point | Oracle Fusion Source | Extraction Method |
|----------------|---------------------|-------------------|
| Revenue | GL_BALANCES | Natural account segment filter |
| Expenses | GL_BALANCES | Natural account segment filter |
| Intercompany Transactions | GL_BALANCES + IC Analysis | Intercompany segment filter |
| Tax Expense (Current) | GL_BALANCES | Tax account filter |
| Tax Expense (Deferred) | GL_BALANCES | Deferred tax account filter |
| Depreciation | FA_DEPRN_PERIODS | Sum by period and entity |
| Foreign Exchange | GL_JE_LINES | Currency gain/loss accounts |

**SBIE Data Mapping**

| GIR Data Point | Oracle Source | Extraction Method |
|----------------|---------------|-------------------|
| Eligible Payroll Costs | PAY_RUN_RESULTS | Filter by eligible element types |
| Eligible Employees | PER_ALL_ASSIGNMENTS_F | Active employees in jurisdiction |
| Tangible Assets | FA_BOOKS | Net book value by category |
| Asset Location | FA_DISTRIBUTION_HISTORY | Assignment to entities |

### Oracle EPM Pillar Two Automation

Oracle EPM Tax Reporting includes **Pillar Two Automation Rules** that simplify data processing:

**GloBE Income Automation**
- Users select a data source (Pre-tax or Tax)
- Application processes Global, Jurisdiction, and Entity Level Rules
- Results stored at entity level

**Covered Tax Automation**
- Automated allocation of covered taxes
- Deferred tax adjustment processing
- 15% cap application

**Task Manager Workflow**
- Assigns and monitors tasks from central dashboard
- Step-by-step process guidance
- Deadline tracking and notifications

### Oracle BI Publisher Reports for Extraction

Create custom reports using Oracle BI Publisher to extract GIR-relevant data:

```
Report: GloBE Income Extraction Report
Parameters:
  - Ledger: [Select Ledger(s)]
  - Period: [Fiscal Year/Period]
  - Entity: [Legal Entity or ALL]
  - Currency: [Group Currency]

Output Columns:
  - Legal Entity Code
  - Legal Entity Name
  - Jurisdiction
  - Account Category (Revenue/Expense/Tax)
  - Natural Account
  - Period Amount (Functional Currency)
  - Period Amount (Group Currency)
  - YTD Amount (Functional Currency)
  - YTD Amount (Group Currency)
```

### Oracle Extraction Challenges and Solutions

| Challenge | Root Cause | Solution |
|-----------|------------|----------|
| Multiple ledgers | Multi-OU implementation | Create extraction queries across ledgers with proper mapping |
| Flex segment complexity | Custom chart of accounts | Build segment value mapping to GIR categories |
| Subledger data access | Security restrictions | Configure data access sets for Pillar Two extracts |
| Cross-module integration | Siloed Oracle modules | Use Oracle Data Integrator (ODI) for unified extraction |
| HCM separate instance | Separate HCM Cloud tenant | API integration or manual extraction and upload |
| Historical data gaps | Recent Oracle Cloud migration | Hybrid extraction from legacy and cloud |

### Oracle-to-GIR Mapping Guide Template

**Template Reference: Oracle_to_GIR_Mapping_Guide.xlsx**

| Tab | Contents |
|-----|----------|
| 1. Overview | Mapping methodology and instructions |
| 2. GL Segments | Chart of accounts segment to GIR mapping |
| 3. Tax Segments | Tax-related segment values |
| 4. Asset Categories | Asset category to SBIE mapping |
| 5. Payroll Elements | Element type to eligible payroll mapping |
| 6. Entity Mapping | Legal entity to CE mapping |
| 7. BI Publisher Reports | Custom report specifications |
| 8. EPM Data Mapping | Oracle EPM to GIR data mapping |

---

## 4.2.3 Other ERP Systems

Organizations using Microsoft Dynamics 365, NetSuite, or other ERP platforms face similar data extraction challenges but typically lack dedicated Pillar Two modules. These organizations generally use one of two approaches:

1. **Specialized Pillar Two Software** - Third-party solutions that integrate with existing ERPs
2. **Manual Extraction** - Direct data export to Excel-based GIR calculators

### Third-Party Pillar Two Solutions

Several vendors offer ERP-agnostic Pillar Two solutions:

**Wolters Kluwer CCH Integrator**
- ERP agnostic with data capture from multiple sources
- Standard data upload formats plus custom file format capability
- Data populates into standardized schedules through mapping templates
- GIR XML output generation

**EY GloBE Engine**
- Cloud-based, scalable, ERP-agnostic solution
- Supports multi-source data integration
- GIR and local tax form generation in XML format
- Reporting discrepancy identification between GIR and QDMTT

**Tax Systems Pillar 2**
- Integration with various ERP platforms
- Automated calculation and compliance workflows
- GIR output generation

**Orbitax Global Minimum Tax**
- Data aggregation from multiple sources
- GloBE calculation engine
- Multi-jurisdiction filing support

### Microsoft Dynamics 365 Extraction

Microsoft Dynamics 365 Finance and Operations (D365 F&O) does not have native Pillar Two functionality but provides robust data extraction capabilities.

**Key Data Entities for Extraction**

| Entity | Description | GIR Relevance |
|--------|-------------|---------------|
| GeneralJournalAccountEntry | Journal entries | Financial transactions |
| LedgerJournalTable | Journal headers | Document information |
| MainAccount | Chart of accounts | Account structure |
| LegalEntity | Legal entity master | Entity identification |
| AssetBook | Fixed asset records | SBIE tangible assets |
| HcmWorker | Employee records | HR/payroll data |

**D365 Extraction Methods**

1. **Data Entities Export**
   - Use Data Management workspace
   - Create export projects for Pillar Two data
   - Schedule recurring exports

2. **OData Integration**
   - REST API access to D365 data
   - Real-time or batch extraction
   - Power BI or Excel integration

3. **Azure Data Lake**
   - Export D365 data to Azure Data Lake
   - Build extraction pipelines using Azure Data Factory
   - Transform and load to Pillar Two solution

4. **Power Platform**
   - Power Query connections to D365
   - Power Automate flows for scheduled extraction
   - Export to Excel or Pillar Two platforms

**D365-to-GIR Mapping**

| GIR Data Point | D365 Entity | D365 Field | Filter/Logic |
|----------------|-------------|------------|--------------|
| Revenue | GeneralJournalAccountEntry | AccountingCurrencyAmount | MainAccount in revenue range |
| Expenses | GeneralJournalAccountEntry | AccountingCurrencyAmount | MainAccount in expense range |
| Tax Expense | GeneralJournalAccountEntry | AccountingCurrencyAmount | MainAccount = tax accounts |
| Tangible Assets | AssetBook | NetBookValue | AssetType = tangible |
| Payroll Costs | HcmWorkerBenefit + PayrollEarning | Amount | Eligible categories |

### NetSuite Extraction

Oracle NetSuite is a cloud-based ERP commonly used by mid-market multinationals. While NetSuite lacks native Pillar Two functionality, it provides flexible data extraction capabilities.

**Key Record Types for Extraction**

| Record Type | Description | GIR Relevance |
|-------------|-------------|---------------|
| Transaction | All financial transactions | Journal entries, invoices, bills |
| Account | Chart of accounts | Account classification |
| Subsidiary | Legal entities | Entity identification |
| Fixed Asset | Asset records | SBIE tangible assets |
| Employee | Employee master | HR data for SBIE |
| Department/Class/Location | Segmentation | Additional classification |

**NetSuite Extraction Methods**

1. **Saved Searches**
   - Create custom saved searches for Pillar Two data
   - Schedule exports to CSV
   - Limited to 100,000 rows per export

2. **SuiteAnalytics Connect**
   - ODBC/JDBC connection to NetSuite data
   - SQL-based extraction queries
   - Connect BI tools or data warehouses

3. **SuiteTalk Web Services**
   - REST/SOAP API access
   - Programmatic data extraction
   - Integration with Pillar Two solutions

4. **SuiteScript**
   - Custom scripts for data extraction
   - Map Reduce scripts for large datasets
   - Scheduled script execution

**NetSuite-to-GIR Mapping**

| GIR Data Point | NetSuite Record | NetSuite Field | Filter/Logic |
|----------------|-----------------|----------------|--------------|
| Revenue | Transaction | amount | type = invoice/revenue |
| Expenses | Transaction | amount | type = bill/expense |
| Entity | Subsidiary | name, subsidiary | Active subsidiaries |
| Jurisdiction | Subsidiary | country | Tax residence |
| Tangible Assets | Fixed Asset | netBookValue | Asset type filter |
| Depreciation | Fixed Asset | currentFyDepreciation | Period depreciation |

### Generic ERP Extraction Framework

For organizations using other ERP systems (Sage, Infor, Workday Financials, etc.), follow this generic extraction framework:

**Step 1: Identify Data Sources**

| Data Category | Typical ERP Module | Alternative Sources |
|---------------|-------------------|---------------------|
| Financial Transactions | General Ledger | Trial balance exports |
| Tax Data | Tax Module | Tax provision software |
| Fixed Assets | Asset Management | Fixed asset register (Excel) |
| Payroll | HR/Payroll | Payroll system reports |
| Entity Structure | Master Data | Legal entity database |
| Intercompany | IC Module | Elimination schedules |

**Step 2: Map to GIR Requirements**

Create mapping documentation connecting:
- ERP account codes → GIR income/expense categories
- ERP entity codes → Constituent Entity identifiers
- ERP asset classes → SBIE tangible asset categories
- ERP payroll codes → SBIE eligible payroll costs

**Step 3: Build Extraction Queries**

```
Generic SQL Pattern for Financial Data:

SELECT
    entity_code AS ce_identifier,
    account_code,
    account_description,
    SUM(amount_local_currency) AS local_amount,
    SUM(amount_group_currency) AS group_amount,
    currency_code,
    fiscal_year,
    fiscal_period
FROM
    general_ledger_transactions
WHERE
    fiscal_year = [GloBE Fiscal Year]
    AND posting_status = 'Posted'
GROUP BY
    entity_code,
    account_code,
    account_description,
    currency_code,
    fiscal_year,
    fiscal_period
ORDER BY
    entity_code,
    account_code
```

**Step 4: Validate and Transform**

| Validation Check | Description | Action |
|------------------|-------------|--------|
| Completeness | All entities included | Reconcile to entity list |
| Balance | Debits = Credits | Investigate imbalances |
| Period Accuracy | Correct fiscal period | Verify cutoff procedures |
| Currency | Consistent currency treatment | Apply exchange rates |
| Intercompany | IC balanced | Check elimination entries |

**Step 5: Load to GIR Calculator**

Options for loading extracted data:
- Direct import to Excel-based calculator
- Upload to cloud-based Pillar Two platform
- API integration with calculation engine

### Multi-ERP Environment Challenges

Many large MNEs operate with multiple ERP systems across different entities or regions. This creates additional complexity for GIR data extraction.

**Common Multi-ERP Scenarios**

| Scenario | Challenge | Solution Approach |
|----------|-----------|-------------------|
| SAP in Europe, Oracle in US | Different data structures | Build unified data layer with consistent mapping |
| NetSuite for acquired entities | Chart of accounts differences | Create cross-walk mapping tables |
| Legacy systems for certain jurisdictions | Limited extraction capability | Manual extraction with enhanced validation |
| Local ERP for statutory reporting | Data reconciliation | Reconcile to group consolidation |

**Data Harmonization Framework**

```
┌─────────────────────────────────────────────────────────────────┐
│                Multi-ERP Data Harmonization                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Source Layer (Multiple ERPs)                                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐              │
│  │   SAP   │ │ Oracle  │ │ D365    │ │NetSuite │              │
│  │ (EMEA)  │ │ (APAC)  │ │ (AMER)  │ │(Acquis.)│              │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘              │
│       │           │           │           │                    │
│       ▼           ▼           ▼           ▼                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Extraction Layer                              │  │
│  │  - Source-specific extraction queries                     │  │
│  │  - Local currency amounts                                  │  │
│  │  - Source system account codes                            │  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │                                │
│                               ▼                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │            Transformation Layer                            │  │
│  │  - Account code mapping to unified chart                  │  │
│  │  - Entity code standardization                            │  │
│  │  - Currency conversion to group currency                  │  │
│  │  - Data quality validation                                 │  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │                                │
│                               ▼                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Unified Data Layer                            │  │
│  │  - Consistent data structure                              │  │
│  │  - GIR-ready format                                       │  │
│  │  - Single source of truth                                 │  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │                                │
│                               ▼                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              GIR Calculation Layer                         │  │
│  │  - ETR computation                                        │  │
│  │  - SBIE calculation                                       │  │
│  │  - Top-up tax determination                               │  │
│  │  - GIR XML generation                                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.2.4 Data Extraction Best Practices

### Pre-Extraction Preparation

**1. Document Data Requirements**
- Create comprehensive list of all ~480 GIR data points
- Map each data point to source system(s)
- Identify data owners for each source
- Establish data quality expectations

**2. Build Extraction Specifications**

| Specification Element | Description |
|-----------------------|-------------|
| Source System | ERP system name and version |
| Source Table/Entity | Specific tables or data entities |
| Key Fields | Fields required for extraction |
| Filter Criteria | Selection parameters (period, entity, status) |
| Transformation Rules | Data conversion or calculation logic |
| Output Format | File format and structure |
| Frequency | One-time vs. recurring extraction |
| Owner | Person responsible for extraction |

**3. Establish Data Validation Framework**

| Validation Type | Description | Example |
|-----------------|-------------|---------|
| Completeness | All expected records present | All 120 entities have data |
| Accuracy | Values match source system | TB total = Extract total |
| Consistency | Data logically consistent | Revenue > 0 for trading entities |
| Timeliness | Data as of correct date | Period-end balances |
| Uniqueness | No duplicate records | One record per entity/account |

### Extraction Execution Checklist

**Pre-Extraction**
- [ ] Confirm fiscal period is closed
- [ ] Verify source system access credentials
- [ ] Test extraction queries on sample data
- [ ] Confirm storage location for extracted files
- [ ] Notify data owners of extraction timing

**During Extraction**
- [ ] Execute extraction queries/jobs
- [ ] Monitor for errors or warnings
- [ ] Log extraction start/end times
- [ ] Capture record counts

**Post-Extraction**
- [ ] Validate record counts against expectations
- [ ] Reconcile totals to trial balance/control reports
- [ ] Check for null or unexpected values
- [ ] Document any data issues identified
- [ ] Archive extraction files with version control

### Data Quality Controls

**Control Point 1: Source System Validation**
- Reconcile extracted GL balances to trial balance
- Verify period-end status (closed vs. open)
- Check for unposted journals

**Control Point 2: Transformation Validation**
- Verify account mapping accuracy
- Check currency conversion calculations
- Validate intercompany elimination

**Control Point 3: Output Validation**
- Balance check (total income vs. control)
- Entity count validation
- Jurisdiction coverage verification

### Common Extraction Pitfalls to Avoid

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Extracting from open period | Data changes after extraction | Confirm period closed before extraction |
| Missing intercompany eliminations | Double-counting | Include elimination entries in scope |
| Incorrect currency conversion | ETR calculation errors | Use consistent FX rate source |
| Excluding statistical accounts | Incomplete SBIE data | Include all account types in scope |
| Manual data entry errors | Data integrity issues | Automate where possible; dual review |
| Version control gaps | Using outdated extracts | Implement file naming convention with timestamps |

---

## Summary: ERP Extraction Strategy Selection

| ERP Platform | Recommended Approach | Key Considerations |
|--------------|---------------------|---------------------|
| **SAP S/4HANA** | SAP PaPM for end-to-end solution; CDS views for manual extraction | Leverage ACDOCA as primary data source |
| **SAP ECC** | SAP PaPM or manual extraction via SE16/SQ01 | Use BKPF/BSEG for detailed transactions |
| **Oracle Cloud ERP** | Oracle EPM Tax Reporting for integrated solution | Data collection from ERP, HCM, and other sources |
| **Oracle EBS** | Oracle EPM Tax Reporting or BI Publisher extraction | Manual or API-based data feeds |
| **Microsoft D365** | Third-party Pillar Two solution with Data Management export | Data entities and OData for extraction |
| **NetSuite** | Third-party Pillar Two solution with SuiteAnalytics extraction | Saved searches for simple extracts |
| **Multi-ERP** | Unified data layer with consistent mapping | Data harmonization is critical |
| **Other ERP** | Generic extraction framework with manual processing | Focus on data quality and validation |

---

## Template References

| Template | Description | Format |
|----------|-------------|--------|
| SAP_to_GIR_Mapping_Guide.xlsx | SAP table and field mapping to GIR data points | Excel |
| Oracle_to_GIR_Mapping_Guide.xlsx | Oracle table and field mapping to GIR data points | Excel |
| D365_to_GIR_Mapping_Guide.xlsx | D365 entity and field mapping to GIR data points | Excel |
| NetSuite_to_GIR_Mapping_Guide.xlsx | NetSuite record mapping to GIR data points | Excel |
| Generic_ERP_Mapping_Template.xlsx | Blank template for other ERP systems | Excel |
| Data_Extraction_Specification.xlsx | Extraction job documentation template | Excel |
| Extraction_Validation_Checklist.xlsx | Pre/during/post extraction validation steps | Excel |

---

## Key Takeaways

1. **Platform-specific solutions exist** - SAP PaPM and Oracle EPM Tax Reporting provide dedicated Pillar Two functionality for organizations on those platforms

2. **ERP-agnostic solutions bridge gaps** - Third-party Pillar Two solutions (Wolters Kluwer, EY, Tax Systems) integrate with multiple ERP platforms

3. **Data volume is significant** - Approximately 150-250 data points per entity require extraction from multiple systems

4. **Multi-system integration is common** - Most MNEs need to extract from multiple source systems including ERP, consolidation, tax provision, HR, and fixed assets

5. **Data harmonization is critical** - Organizations with multiple ERPs must create a unified data layer with consistent mapping

6. **Validation is essential** - Robust data validation at each stage of extraction prevents calculation errors in GIR preparation

7. **Automation reduces risk** - Automated extraction reduces manual errors and enables consistent, repeatable processes

---

## Sources and References

- [SAP Global Minimum Tax Solutions](https://news.sap.com/2023/09/global-minimum-tax-rate-beps-2-0/)
- [SAP PaPM for BEPS 2.0](https://blogs.sap.com/2023/12/06/new-global-minimum-taxes-addressing-the-data-and-technology-challenge-with-sap-solutions./)
- [Oracle EPM Tax Reporting](https://www.oracle.com/performance-management/tax-reporting/)
- [Oracle and Deloitte Pillar Two Announcement](https://www.oracle.com/news/announcement/oracle-and-deloitte-help-multinational-organizations-prepare-for-oecd-pillar-two-requirements-2024-01-10/)
- [Oracle EPM Pillar Two Configuration](https://docs.oracle.com/en/cloud/saas/tax-reporting-cloud/agtrc/configuring_globe_income_and_covered_tax_automation.html)
- [EY Pillar Two Data Challenges](https://www.ey.com/en_us/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges)
- [Wolters Kluwer Pillar Two Data Requirements](https://www.wolterskluwer.com/en/expert-insights/understanding-beps-pillar-two-data)
- [EY GloBE Engine](https://www.ey.com/en_us/services/tax/globe-engine-global-minimum-tax-management-tool)
- [Wolters Kluwer CCH Integrator](https://www.wolterskluwer.com/en/solutions/cch-integrator/beps-pillar-two)
- [Alteryx Pillar 2 Data Challenges](https://www.alteryx.com/blog/pillar-2-compliance-addressing-data-challenges-of-global-tax-reforms)
- [SAP S/4HANA Finance Tables](https://sap2databricks.com/sap-finance)
- [BSEG vs ACDOCA Comparison](https://tablesinsap.com/bseg-vs-acdoca-understanding-the-key-differences/)

---

*This section provides ERP-specific guidance for extracting the ~480 data points required for GIR preparation. The next section (4.3 Data Collection Templates) provides the standardized templates for capturing this data regardless of source system.*
