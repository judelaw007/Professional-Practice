# Section 4: Data Gathering and Extraction

## 4.1 Complete Data Point Inventory

**Estimated Reading Time:** 35 minutes
**Pages:** 12-15

---

## Learning Objectives for This Section

By the end of this section, you will be able to:

- Understand the complete data point inventory for GIR filing (~480 points)
- Identify data sources for each category of GIR data points
- Map data points to appropriate system owners and stakeholders
- Categorize data points by priority and complexity
- Develop a data collection strategy for your organization
- Recognize common data gaps and quality challenges

---

## Overview of GIR Data Requirements

The GloBE Information Return is a **complex, data-intensive filing** requiring approximately **480 data points** at the base level. The actual number of data points scales significantly based on:

- Number of constituent entities
- Number of jurisdictions
- Complexity of corporate structure
- Number of elections made
- Number of GloBE adjustments applicable

**Practical Example:** An MNE with 100 Constituent Entities operating in 30 jurisdictions could have **tens of thousands of individual data points** to collect and validate.

---

## Data Point Summary by GIR Section

| GIR Section | Category | Base Data Points | Notes |
|-------------|----------|-----------------|-------|
| **Section 1** | MNE Group Information | 50+ | Scales with number of entities |
| **Section 2** | Safe Harbours & Exclusions | ~40 | Per jurisdiction |
| **Section 3.1** | ETR Computation | ~50 | Per jurisdiction |
| **Section 3.2** | Deferred Tax & Loss Carrybacks | 50+ | Complex tracking required |
| **Section 3.3** | Transitional Provisions | 20+ | Time-limited |
| **Section 3.4** | Elections | ~40 | Many are one-time |
| **Section 3.5** | Miscellaneous Adjustments | ~120 | Article 3.2 adjustments |
| **Section 3.6** | International Shipping | ~20 | If applicable |
| **Section 3.7** | SBIE, Top-up Tax, QDMTT | ~40 | Per jurisdiction |
| **Section 3.8** | IIR & UTPR Allocation | ~20 | Payroll and asset data |
| | **TOTAL** | **~480** | Base (before scaling) |

---

## Section 1: MNE Group Information Data Points

### 1.1 Filing Constituent Entity Identification

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Legal Name | Full legal name of Filing CE | Legal/Corporate Secretary | Legal |
| TIN (Filing Jurisdiction) | Tax Identification Number | Tax Registration | Tax |
| TIN Issuing Jurisdiction | Country code | Tax Registration | Tax |
| Jurisdiction of Tax Residence | Tax residence country | Tax | Tax |
| Jurisdiction for GloBE | GloBE location country | GloBE Analysis | Tax |
| Registered Address | Business address | Corporate Records | Legal |
| Filing Status (UPE/DFE) | Entity filing type | GloBE Election | Tax |
| DFE Election Date | Date of election | Election Documentation | Tax |

### 1.2 Ultimate Parent Entity Information

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| UPE Legal Name | Full legal name | Corporate Records | Legal |
| UPE TIN | Tax Identification Number | Tax Registration | Tax |
| UPE Jurisdiction | Country for GloBE purposes | GloBE Analysis | Tax |
| UPE GloBE Status | UPE classification | GloBE Analysis | Tax |
| Accounting Standard | IFRS, US GAAP, etc. | Finance/Accounting | Finance |
| Presentation Currency | ISO currency code | Consolidation System | Finance |
| Fiscal Year Start | Start date | Corporate Records | Finance |
| Fiscal Year End | End date | Corporate Records | Finance |
| QIIR Status (UPE Jurisdiction) | Yes/No | Legislative Analysis | Tax |
| UTPR Status (UPE Jurisdiction) | Yes/No | Legislative Analysis | Tax |
| QDMTT Status (UPE Jurisdiction) | Yes/No | Legislative Analysis | Tax |

### 1.3 Corporate Structure (Per Entity)

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Entity Legal Name | Full legal name | Corporate Records | Legal |
| Entity TIN | Tax Identification Number | Tax Registration | Tax |
| TIN Issuing Jurisdiction | Country code | Tax Registration | Tax |
| Jurisdiction for GloBE | GloBE location | GloBE Analysis | Tax |
| GloBE Status | Entity classification | GloBE Analysis | Tax |
| Direct Owner | Parent entity | Corporate Structure | Legal |
| Ownership Percentage | Decimal (0.0000-1.0000) | Corporate Structure | Legal |
| QIIR Applicability | Yes/No | GloBE Analysis | Tax |
| UTPR Applicability | Yes/No | GloBE Analysis | Tax |
| Change Date (if any) | Date of ownership change | Corporate Records | Legal |
| Pre-Change Status | Status before change | GloBE Analysis | Tax |
| Post-Change Status | Status after change | GloBE Analysis | Tax |

### 1.4 High-Level Summary (Per Jurisdiction)

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Jurisdiction | Country code | Corporate Structure | Legal |
| ETR Range | 2.5% increment band | GloBE Calculation | Tax |
| Safe Harbour Applied | Yes/No | Safe Harbour Analysis | Tax |
| SBIE Reduces to Nil | Yes/No | SBIE Calculation | Tax |
| QDMTT Applies | Yes/No | QDMTT Analysis | Tax |
| IIR Applies | Yes/No | IIR Analysis | Tax |
| UTPR Applies | Yes/No | UTPR Analysis | Tax |
| Top-Up Tax Band (QDMTT) | Amount band | Top-up Tax Calc | Tax |
| Top-Up Tax Band (IIR/UTPR) | Amount band | Top-up Tax Calc | Tax |

---

## Section 2: Safe Harbours and Exclusions Data Points

### 2.1 Jurisdictional Characteristics

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Jurisdiction | Country code | Corporate Structure | Legal |
| Subgroup Type | UPE, POPE, JV, etc. | GloBE Analysis | Tax |
| QDMTT in Force | Yes/No | Legislative Tracker | Tax |
| IIR in Force | Yes/No | Legislative Tracker | Tax |
| UTPR in Force | Yes/No | Legislative Tracker | Tax |

### 2.2 Transitional CbCR Safe Harbour

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Safe Harbour Election | Yes/No | GloBE Election | Tax |
| Test Met | De Minimis/ETR/Routine Profits | Safe Harbour Calc | Tax |
| CbCR Revenue | Total revenue | CbCR Report | Tax |
| CbCR Profit/Loss | Profit before tax | CbCR Report | Tax |
| Simplified Covered Taxes | Tax expense (adjusted) | Tax Provision | Tax |
| Simplified ETR | Calculated rate | Safe Harbour Calc | Tax |
| SBIE Amount | Carve-out amount | SBIE Calculation | Tax |

### 2.3 QDMTT and UTPR Safe Harbours

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| QDMTT Safe Harbour Election | Yes/No | GloBE Election | Tax |
| QDMTT Switch-Off Applies | Yes/No | QDMTT Analysis | Tax |
| UTPR Safe Harbour Election | Yes/No | GloBE Election | Tax |
| UPE Nominal Tax Rate | Percentage | Legislative Research | Tax |

---

## Section 3: GloBE Computations Data Points

### 3.1 ETR Computation - GloBE Income

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Financial Accounting Net Income/Loss | FANIL per CE | Consolidation/ERP | Finance |
| **Article 3.2 Adjustments:** | | | |
| Covered Taxes Add-Back | Tax expense | Tax Provision | Tax |
| Excluded Dividends | Participation exemptions | Tax | Tax |
| Excluded Equity Gains/Losses | Qualifying gains/losses | Tax | Tax |
| Policy Disallowed Expenses | Fines, bribes, penalties | Finance/Legal | Finance |
| Prior Period Errors | Material corrections | Finance | Finance |
| Asymmetric FX Gains/Losses | Currency adjustments | Treasury/Finance | Finance |
| Stock-Based Compensation | If election made | HR/Equity Comp | HR |
| Intra-Group Transactions | Arm's length adjustments | Transfer Pricing | Tax |
| Asset Revaluation | Fair value adjustments | Finance | Finance |
| Pension Expense Adjustments | Actuarial differences | HR/Finance | Finance |
| International Shipping Income | If exclusion applies | Operations | Tax |
| **Net GloBE Income/Loss** | Calculated total | GloBE Calculation | Tax |

### 3.2 ETR Computation - Adjusted Covered Taxes

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| Current Tax Expense | Per financial statements | Tax Provision | Tax |
| **Article 4.1 Adjustments:** | | | |
| Taxes Not Relating to GloBE Income | Excluded taxes | Tax | Tax |
| Uncertain Tax Position Accruals | UTP reserves | Tax Provision | Tax |
| Taxes on Excluded Dividends | Related taxes | Tax | Tax |
| Taxes on Excluded Equity Gains | Related taxes | Tax | Tax |
| Covered Taxes Paid (Prior Periods) | Cash tax adjustments | Tax Compliance | Tax |
| **Deferred Tax Adjustments (Art. 4.4):** | | | |
| Deferred Tax Expense (DTL Increase) | DTL movements | Tax Provision | Tax |
| Deferred Tax Benefit (DTL Decrease) | DTL movements | Tax Provision | Tax |
| DTL 15% Cap Adjustment | Capped amount | GloBE Calculation | Tax |
| DTL Recapture Amount | 5-year reversal | DTL Tracking | Tax |
| **Adjusted Covered Taxes** | Calculated total | GloBE Calculation | Tax |

### 3.3 Deferred Tax Tracking Data Points

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| DTL Category | Type of timing difference | Tax Provision | Tax |
| DTL Opening Balance | Start of year | Tax Provision | Tax |
| DTL Closing Balance | End of year | Tax Provision | Tax |
| DTL Movement | Change during year | Tax Provision | Tax |
| DTL Original Year | Year first recognized | DTL Tracking | Tax |
| DTL Reversal Year | Year of reversal (if any) | DTL Tracking | Tax |
| Recapture Exception Status | REA Yes/No | GloBE Analysis | Tax |
| Unclaimed Accrual Election | Yes/No | GloBE Election | Tax |

### 3.4 SBIE Calculation Data Points

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| **Eligible Payroll Costs:** | | | |
| Salaries and Wages | Per CE | Payroll/HR | HR |
| Employee Benefits | Per CE | Payroll/HR | HR |
| Employer Payroll Taxes | Per CE | Payroll/HR | HR |
| Pension Contributions | Per CE | Payroll/HR | HR |
| Other Compensation | Per CE | Payroll/HR | HR |
| **Eligible Tangible Assets:** | | | |
| Property | Carrying value | Fixed Asset Register | Finance |
| Plant | Carrying value | Fixed Asset Register | Finance |
| Equipment | Carrying value | Fixed Asset Register | Finance |
| Right-of-Use Assets | Carrying value | Lease Accounting | Finance |
| Natural Resources | Carrying value | Fixed Asset Register | Finance |
| Land and Buildings | Carrying value | Fixed Asset Register | Finance |
| Opening Tangible Assets | Start of year | Fixed Asset Register | Finance |
| Closing Tangible Assets | End of year | Fixed Asset Register | Finance |
| Average Tangible Assets | Calculated | GloBE Calculation | Tax |

### 3.5 Top-Up Tax Allocation Data Points

| Data Point | Description | Source System | Owner |
|------------|-------------|---------------|-------|
| **IIR Allocation:** | | | |
| Ownership Interest (per parent) | Percentage | Corporate Structure | Legal |
| Allocable Share | Calculated | GloBE Calculation | Tax |
| IIR Top-Up Tax Amount | Allocated amount | GloBE Calculation | Tax |
| **UTPR Allocation:** | | | |
| Employee Headcount | Per jurisdiction | HR/Payroll | HR |
| Tangible Assets (Net Book Value) | Per jurisdiction | Fixed Asset Register | Finance |
| UTPR Allocation Key | Calculated | GloBE Calculation | Tax |
| UTPR Top-Up Tax Amount | Allocated amount | GloBE Calculation | Tax |

---

## Data Source Mapping

### Primary Data Sources

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       GIR DATA SOURCE ECOSYSTEM                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────┐
│                         FINANCIAL SYSTEMS                                  │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐           │
│  │   ERP SYSTEM    │  │  CONSOLIDATION  │  │  TAX PROVISION  │           │
│  │                 │  │     SYSTEM      │  │     SYSTEM      │           │
│  │ • Trial Balance │  │ • FANIL         │  │ • Current Tax   │           │
│  │ • GL Accounts   │  │ • Eliminations  │  │ • Deferred Tax  │           │
│  │ • Transactions  │  │ • Currency      │  │ • ETR Data      │           │
│  │ • Sub-ledgers   │  │ • Intercompany  │  │ • UTP Reserves  │           │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘           │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                      NON-FINANCIAL SYSTEMS                                 │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐           │
│  │  HR / PAYROLL   │  │  FIXED ASSETS   │  │   CORPORATE     │           │
│  │                 │  │    REGISTER     │  │   SECRETARY     │           │
│  │ • Payroll Costs │  │ • Asset Values  │  │ • Entity List   │           │
│  │ • Headcount     │  │ • Depreciation  │  │ • Ownership     │           │
│  │ • Benefits      │  │ • NBV           │  │ • TINs          │           │
│  │ • Pensions      │  │ • Locations     │  │ • Changes       │           │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘           │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                      EXISTING TAX FILINGS                                  │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐           │
│  │   CbCR DATA     │  │  TAX RETURNS    │  │  TRANSFER       │           │
│  │                 │  │                 │  │  PRICING        │           │
│  │ • Revenue       │  │ • Entity Tax    │  │ • Intercompany  │           │
│  │ • Profit/Loss   │  │ • Tax Paid      │  │ • Arm's Length  │           │
│  │ • Employees     │  │ • Carryforwards │  │ • Documentation │           │
│  │ • Assets        │  │ • Credits       │  │                 │           │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘           │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### Data Source Summary by Category

| Data Category | Primary Source | Secondary Source | Owner |
|---------------|----------------|------------------|-------|
| **Entity Identification** | Corporate Secretary | Legal Entity Management | Legal |
| **Ownership Structure** | Corporate Secretary | ERP Master Data | Legal |
| **Financial Accounting Data** | Consolidation System | ERP | Finance |
| **Current Tax Data** | Tax Provision System | Tax Compliance | Tax |
| **Deferred Tax Data** | Tax Provision System | Spreadsheets | Tax |
| **Payroll Costs** | HR/Payroll System | ERP | HR |
| **Tangible Assets** | Fixed Asset Register | ERP Sub-ledger | Finance |
| **CbCR Data** | CbCR Filing | Tax Compliance | Tax |
| **Legislative Status** | External Research | OECD/Jurisdiction Websites | Tax |

---

## Data Collection Priority Ranking

### Tier 1: Critical Path Data (Collect First)

| Priority | Data Category | Reason | Timeline |
|----------|---------------|--------|----------|
| **1** | Entity Master List | Foundation for all other data | Week 1-2 |
| **2** | Ownership Structure | Required for IIR allocation | Week 1-2 |
| **3** | Jurisdictional Presence | Determines scope of GIR | Week 1-2 |
| **4** | FANIL by CE | Starting point for GloBE Income | Week 2-4 |
| **5** | Current Tax Expense | Core to ETR calculation | Week 2-4 |

### Tier 2: High Priority Data (Collect Second)

| Priority | Data Category | Reason | Timeline |
|----------|---------------|--------|----------|
| **6** | CbCR Data | Required for safe harbour tests | Week 3-5 |
| **7** | Deferred Tax Data | Required for Adjusted Covered Taxes | Week 3-5 |
| **8** | Article 3.2 Adjustments | GloBE Income computation | Week 4-6 |
| **9** | Article 4.1 Adjustments | Covered Tax adjustments | Week 4-6 |
| **10** | Payroll Costs | SBIE calculation | Week 4-6 |

### Tier 3: Standard Priority Data (Collect Third)

| Priority | Data Category | Reason | Timeline |
|----------|---------------|--------|----------|
| **11** | Tangible Asset Values | SBIE calculation | Week 5-7 |
| **12** | Employee Headcount | UTPR allocation | Week 5-7 |
| **13** | DTL Tracking Detail | Recapture rule compliance | Week 5-7 |
| **14** | Election Documentation | Support for elections made | Week 6-8 |
| **15** | Change Documentation | Ownership changes, wind-ups | Week 6-8 |

### Tier 4: Final Data (Complete Last)

| Priority | Data Category | Reason | Timeline |
|----------|---------------|--------|----------|
| **16** | High-Level Summary | Depends on all calculations | Week 8-10 |
| **17** | Allocation Details | Depends on Top-up Tax calculation | Week 8-10 |
| **18** | Validation Checks | Cross-section reconciliation | Week 9-10 |

---

## Stakeholder Responsibility Matrix

### RACI Chart for GIR Data Collection

| Data Category | Tax | Finance | HR | Legal | IT |
|---------------|-----|---------|----|----|-----|
| Entity Master Data | C | I | I | **R/A** | S |
| Ownership Structure | C | I | I | **R/A** | S |
| Financial Statements | C | **R/A** | I | I | S |
| Tax Provision Data | **R/A** | C | I | I | S |
| Deferred Tax Tracking | **R/A** | C | I | I | S |
| Payroll Costs | C | C | **R/A** | I | S |
| Tangible Assets | C | **R/A** | I | I | S |
| CbCR Data | **R/A** | C | I | I | S |
| GloBE Calculations | **R/A** | C | I | I | S |
| GIR Filing | **R/A** | C | C | C | S |

**Key:** R = Responsible, A = Accountable, C = Consulted, I = Informed, S = Support

---

## Data Quality Requirements

### Validation Rules

| Data Point | Validation Rule | Error Handling |
|------------|-----------------|----------------|
| **TIN** | Valid format, no blanks | Use "NOTIN" if none |
| **Jurisdiction Code** | ISO 3166-1 Alpha-2 | Reject invalid codes |
| **Ownership %** | 0.0000 to 1.0000, 4 decimals | Round to 4 places |
| **Currency** | ISO 4217 codes | Reject invalid codes |
| **Dates** | YYYY-MM-DD format | Reject invalid formats |
| **Amounts** | Consistent currency, no symbols | Convert to reporting currency |
| **Percentages** | Decimal format (not %) | Convert % to decimal |

### Cross-Section Consistency Checks

| Check | Sections | Validation |
|-------|----------|------------|
| Entity Count | 1.3 ↔ 3.1 | Same entities in both sections |
| Jurisdiction List | 1.3 ↔ 2 ↔ 3 | Consistent across sections |
| ETR Summary | 1.4 ↔ 3.1 | ETR range matches calculation |
| Safe Harbour Status | 2 ↔ 3 | If safe harbour, no Section 3 |
| Ownership Chain | 1.3 ↔ 3.4 | IIR allocation matches ownership |

### Data Completeness Checklist

- [ ] All entities in consolidation are listed in Section 1.3
- [ ] All jurisdictions with entities are included
- [ ] All TINs collected (or "NOTIN" documented)
- [ ] All ownership percentages sum correctly
- [ ] All required elections documented
- [ ] All changes during fiscal year captured
- [ ] All DTL categories tracked for recapture

---

## Common Data Gaps

### Frequently Missing Data

| Data Gap | Impact | Mitigation |
|----------|--------|------------|
| **Entity TINs for foreign subsidiaries** | Filing rejection | Request from local advisors early |
| **Payroll costs by CE** | SBIE calculation incorrect | Work with HR to segment data |
| **Tangible assets by location** | SBIE/UTPR incorrect | Fixed asset register review |
| **DTL vintage tracking** | Recapture rule non-compliance | Establish tracking system |
| **Intra-group transaction detail** | GloBE adjustments incomplete | Transfer pricing documentation |
| **Historical ownership changes** | Corporate structure incomplete | Corporate secretarial records |

### Data Quality Challenges

| Challenge | Description | Solution |
|-----------|-------------|----------|
| **Multiple ERP Systems** | Inconsistent chart of accounts | Data mapping and normalization |
| **Different Currencies** | Manual conversion required | Automate currency conversion |
| **Timing Differences** | Local vs. group year-ends | Adjust for timing |
| **Missing Granularity** | Trial balance too aggregated | Sub-ledger analysis |
| **Manual Adjustments** | Spreadsheet-based data | Document and validate |

---

## Data Collection Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GIR DATA COLLECTION TIMELINE                             │
│                    (For FY Ending December 31)                              │
└─────────────────────────────────────────────────────────────────────────────┘

MONTH 1-2: Foundation Data
──────────────────────────
├── Entity master list finalized
├── Ownership structure documented
├── Jurisdictional presence mapped
├── Legislative status tracked
└── Data source inventory completed

MONTH 3-4: Financial Data
─────────────────────────
├── FANIL by CE extracted
├── Consolidation adjustments identified
├── Tax provision data collected
├── Deferred tax movements captured
└── CbCR data obtained

MONTH 5-6: Non-Financial Data
─────────────────────────────
├── Payroll costs by CE collected
├── Tangible asset values compiled
├── Employee headcount obtained
├── DTL tracking detail gathered
└── Article 3.2 adjustments calculated

MONTH 7-8: GloBE Calculations
─────────────────────────────
├── GloBE Income calculated
├── Adjusted Covered Taxes calculated
├── ETR determined by jurisdiction
├── Safe harbour tests applied
├── SBIE calculated
└── Top-up Tax computed

MONTH 9-10: Validation and Filing
─────────────────────────────────
├── Cross-section validation
├── Data quality review
├── XML generation and validation
├── Management review and sign-off
└── GIR submission
```

---

## Data Governance Framework

### Data Ownership

| Function | Data Owned | Responsibilities |
|----------|------------|------------------|
| **Tax** | GloBE calculations, elections, tax provision | Primary GIR owner, data integration |
| **Finance** | FANIL, consolidation, tangible assets | Financial data accuracy |
| **HR** | Payroll costs, headcount | Employee-related data |
| **Legal** | Entity master, ownership, TINs | Corporate structure accuracy |
| **IT** | System integration, data extraction | Technical support and automation |

### Data Change Control

| Process | Description | Approval Required |
|---------|-------------|-------------------|
| **Entity Addition** | New entity in scope | Legal + Tax |
| **Ownership Change** | Change in ownership % | Legal + Tax |
| **Election Change** | New or changed election | Tax Director |
| **Calculation Methodology** | Change in GloBE treatment | Tax + External Advisor |
| **Data Source Change** | New or changed data source | Tax + IT |

---

## Template Reference: Data Point Inventory

The complete Data Point Inventory Template (Excel) includes:

1. **Entity Master Sheet** - All entities with TINs, jurisdictions, status
2. **Data Source Mapping** - Each data point linked to source system
3. **Collection Schedule** - Timeline with owners and deadlines
4. **Validation Rules** - Automated checks for data quality
5. **Gap Tracker** - Log of missing data with resolution status
6. **Change Log** - Record of all data changes

---

## Practice This Skill: GIR Data Point Reference

Navigating the ~480 GIR data points can be challenging. Practice using the **GIR Data Point Reference (GIR-006)** on tools.mojitax.com.

| Tool | Tool ID | Purpose |
|------|---------|---------|
| GIR Data Point Reference | GIR-006 | Searchable reference of all GIR data points with field requirements |

**Demo Tool vs Professional Tool**

This is a demo tool for learning purposes. In professional practice, you would use integrated Pillar Two software with built-in field guidance and ERP mappings. The demo tool helps you understand data requirements.

**To Practice:**

1. Go to tools.mojitax.com and find **GIR Data Point Reference**
2. Try these searches:
   - Search "revenue" to find revenue-related fields
   - Filter by Section 3 to see GloBE computation fields
   - Search "ownership" to find entity relationship fields
3. For each field, review:
   - Field ID and name
   - Data type and format
   - Required vs optional status
   - Typical ERP source

Use this tool alongside **Case Study 3** (Data Gap Challenges) to identify which data points are missing and their requirements.

---

## Next Steps

Continue to the detailed section guidance:
- **Section 4.2:** Data Source Mapping and System Requirements
- **Section 4.3:** Data Collection Templates

---

## Sources and References

This section incorporates information from:

- [KPMG - Pillar Two: GloBE Information Return](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/07/pillar-two-globe-information-return.pdf)
- [Wolters Kluwer - Understanding data requirements and managing data for Pillar Two](https://www.wolterskluwer.com/en/expert-insights/understanding-beps-pillar-two-data)
- [Wolters Kluwer - Overcoming challenges in preparing GloBE Information Return](https://www.wolterskluwer.com/en-au/expert-insights/overcoming-challenges-in-preparing-for-beps-pillar-two)
- [PwC - Pillar Two Data Input Catalog](https://www.pwc.com/gx/en/services/tax/assets/pwc-pillar-two-data-input-catalog.pdf)
- [PwC - How will you meet your Pillar Two data challenge?](https://www.pwc.com/ca/en/today-s-issues/compliance-transformed/how-will-you-meet-your-pillar-two-data-challenge.html)
- [EY - How to alleviate BEPS 2.0 Pillar Two data challenges](https://www.ey.com/en_us/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges)
- [EY - OECD/G20 Inclusive Framework releases document on Pillar Two GloBE Information Return](https://www.ey.com/en_gl/technical/tax-alerts/oecd-g20-inclusive-framework-releases-document-on-pillar-two-glo)
- [oecdpillars.com - Pillar Two: 122 Data Points for Systems Implementation](https://oecdpillars.com/pillar-tab/pillar-two-data-points-for-systems-implementation/)
- [Citco - Key governance and reporting challenges for MNEs](https://www.citco.com/insights/key-governance-and-reporting-challenges-for-mnes)
- [Citco - Pillar 2 update: getting to grips with the GloBE Information Return](https://www.citco.com/insights/pillar-2-update-getting-to-grips-with-the-globe-information-return)
- [Loyens & Loeff - GloBE Information Return](https://www.loyensloeff.com/insights/news--events/news/globe-information-return/)
- [Tax Adviser - Pillar Two rules: roadmap to compliance](https://www.taxadvisermagazine.com/article/pillar-two-rules-roadmap-compliance)
- [BDO - What Pillar Two Means for Income Tax Accounting](https://www.bdo.com/insights/tax/what-pillar-two-means-for-income-tax-accounting)

---

*End of Section 4.1*
