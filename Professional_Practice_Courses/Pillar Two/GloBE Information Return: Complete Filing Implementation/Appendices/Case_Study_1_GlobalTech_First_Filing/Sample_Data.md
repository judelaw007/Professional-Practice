# Case Study 1: GlobalTech Manufacturing - Sample Data

## Ireland - Full GloBE Calculation Data

### Constituent Entities

| Entity | Activity | Employees |
|--------|----------|-----------|
| GT IP Holdings Ltd | IP holding | 15 |
| GT Services Ireland Ltd | Shared services | 85 |
| GT Technology Ireland Ltd | R&D | 65 |
| GT Sales Ireland Ltd | Sales support | 12 |

### GloBE Income Calculation

**Input Data for GloBE Calculator - Step 1: ETR (GIR-001):**

| Data Point | Amount (EUR) |
|------------|--------------|
| Financial Accounting Net Income (aggregate) | 28,000,000 |
| Net taxes included in income | 3,500,000 |
| Excluded dividends add-back | 0 |
| Excluded equity gains add-back | 0 |
| Policy disallowed expenses | (200,000) |
| Stock-based compensation adjustment | 1,200,000 |
| Other adjustments | 300,000 |
| **GloBE Income (calculated)** | **32,800,000** |

### Adjusted Covered Taxes Calculation

| Data Point | Amount (EUR) |
|------------|--------------|
| Current Tax Expense | 3,200,000 |
| Deferred Tax Expense | 800,000 |
| **Total Tax Expense** | **4,000,000** |
| Less: Taxes related to uncertain positions | (150,000) |
| Less: Non-Covered Taxes | (50,000) |
| **Adjusted Covered Taxes** | **3,800,000** |

### SBIE Calculation Data

**Input Data for GloBE Calculator - Step 2: SBIE (GIR-001):**

| Data Point | Amount (EUR) |
|------------|--------------|
| **Fiscal Year** | 2024 |

**Eligible Payroll Costs by Entity:**

| Entity | Payroll (EUR) |
|--------|---------------|
| GT IP Holdings Ltd | 2,500,000 |
| GT Services Ireland Ltd | 8,200,000 |
| GT Technology Ireland Ltd | 6,800,000 |
| GT Sales Ireland Ltd | 1,500,000 |
| **Total Eligible Payroll** | **19,000,000** |

**Tangible Assets (Net Book Value) by Entity:**

| Entity | NBV (EUR) |
|--------|-----------|
| GT IP Holdings Ltd | 500,000 |
| GT Services Ireland Ltd | 3,200,000 |
| GT Technology Ireland Ltd | 12,500,000 |
| GT Sales Ireland Ltd | 800,000 |
| **Total Tangible Assets** | **17,000,000** |

### Top-Up Tax Calculation

**Input Data for GloBE Calculator - Step 3: Top-Up Tax (GIR-001):**

| Data Point | Value |
|------------|-------|
| GloBE Income | €32,800,000 |
| Adjusted Covered Taxes | €3,800,000 |
| Total SBIE (from Step 2) | €3,188,000 |
| QDMTT Amount | €0 (not applicable) |

---

## Switzerland - Full GloBE Calculation Data

### Constituent Entities

| Entity | Activity | Canton |
|--------|----------|--------|
| GT Trading AG | Principal trading | Zug |
| GT Finance AG | Group treasury | Zug |

### GloBE Income Calculation

| Data Point | Amount (EUR) |
|------------|--------------|
| Financial Accounting Net Income | 16,500,000 |
| GloBE adjustments (net) | 1,500,000 |
| **GloBE Income** | **18,000,000** |

### Adjusted Covered Taxes

| Data Point | Amount (EUR) |
|------------|--------------|
| Total Tax Expense | 2,700,000 |
| Adjustments | (180,000) |
| **Adjusted Covered Taxes** | **2,520,000** |

### SBIE Data

| Data Point | Amount (EUR) |
|------------|--------------|
| Total Eligible Payroll | 8,500,000 |
| Total Tangible Assets (NBV) | 4,200,000 |

---

## Safe Harbour Qualification Data

**Input Data for Safe Harbour Qualifier (GIR-002):**

Test whether UK qualifies for Transitional CbCR Safe Harbour:

| Data Point | Value |
|------------|-------|
| Fiscal Year | 2024 |
| CbCR Revenue | €320,000,000 |
| CbCR Profit Before Tax | €48,000,000 |
| Simplified Covered Taxes | €11,040,000 |
| SBIE Amount | €15,000,000 |

---

## SBIE Rates for FY2024

For reference when using GIR-001 Step 2:

| Rate Type | FY2024 Rate |
|-----------|-------------|
| Payroll Carve-out | 9.8% |
| Asset Carve-out | 7.8% |

---

## Filing Deadline Data

**Input Data for Filing Deadline Calculator (GIR-003):**

| Data Point | Value |
|------------|-------|
| UPE Jurisdiction | United Kingdom |
| Fiscal Year End Date | 31 December 2024 |
| Is First GIR Filing Year? | Yes |
| Jurisdiction Filing In | United Kingdom |
| Has Transition Year Extension? | Yes (first year eligible) |

---

## Designated Filing Entity Assessment Data

**Input Data for DFE Assessment Tool (GIR-005):**

**Candidate Entities for DFE Role:**

| Entity | Jurisdiction | Pillar Two Status | Tax Team Size | Systems Capability | Current GIR Filer? |
|--------|--------------|-------------------|---------------|--------------------|--------------------|
| GlobalTech Manufacturing Ltd | UK | IIR Effective 2024 | 8 FTE | ERP integrated | No (first year) |
| GlobalTech Europe BV | Netherlands | IIR Effective 2024 | 3 FTE | Local system | No |
| GlobalTech GmbH | Germany | IIR Effective 2024 | 4 FTE | SAP | No |
| GT IP Holdings Ltd | Ireland | IIR Effective 2024 | 1 FTE | Limited | No |

**Additional DFE Assessment Factors:**

| Factor | GlobalTech Manufacturing Ltd (UK) | GlobalTech Europe BV (NL) |
|--------|-----------------------------------|---------------------------|
| Is UPE? | Yes | No |
| Group Revenue Visibility | Full consolidated view | Regional only |
| Existing Tax Authority Relationships | Strong (UK HMRC) | Moderate |
| Language Capability | English (GIR language) | Dutch/English |
| Time Zone Coverage | GMT (central) | CET |
| External Advisor Support | Big 4 engaged | Local firm |

---

## GIR Practice Form Data

**Input Data for GIR Practice Form (GIR-004):**

Use the data below to practice populating the GIR form sections. The integrated data point reference (search bar) can be used to look up field definitions.

**Sample Data Point Searches:**

| Search Query | Expected Section | Purpose |
|--------------|------------------|---------|
| "UPE name" | Section 1 | Identify field for GlobalTech Manufacturing Ltd |
| "Fiscal year" | Section 1 | Determine reporting period fields |
| "Constituent Entity" | Section 2 | Find CE listing requirements |
| "GloBE Income" | Section 3 | Locate income computation fields |
| "Adjusted Covered Taxes" | Section 3 | Find tax computation fields |
| "SBIE" | Section 3 | Locate substance exclusion fields |
| "Top-up Tax" | Section 3 | Find top-up tax allocation fields |
| "Safe Harbour" | Section 3 | Identify safe harbour election fields |

### Section 1: General Information

| Field | Value |
|-------|-------|
| UPE Legal Name | GlobalTech Manufacturing Ltd |
| UPE Jurisdiction | United Kingdom |
| UPE Tax ID (UTR) | 1234567890 |
| Reporting Fiscal Year | 2024 |
| Fiscal Year Start | 1 January 2024 |
| Fiscal Year End | 31 December 2024 |
| Accounting Standard | IFRS |
| Consolidated Revenue | €1,350,000,000 |
| Designated Filing Entity | GlobalTech Manufacturing Ltd |
| DFE Jurisdiction | United Kingdom |
| First GIR Filing? | Yes |
| Currency | EUR |

### Section 2: Corporate Structure (Sample Entities)

| Entity Name | Jurisdiction | Entity Type | Ownership % | Tax ID |
|-------------|--------------|-------------|-------------|--------|
| GlobalTech Manufacturing Ltd | UK | UPE | 100% | GB1234567890 |
| GT IP Holdings Ltd | Ireland | CE | 100% | IE1234567A |
| GT Services Ireland Ltd | Ireland | CE | 100% | IE2345678B |
| GT Technology Ireland Ltd | Ireland | CE | 100% | IE3456789C |
| GT Sales Ireland Ltd | Ireland | CE | 100% | IE4567890D |
| GT Trading AG | Switzerland | CE | 100% | CHE-123.456.789 |
| GT Finance AG | Switzerland | CE | 100% | CHE-234.567.890 |

### Section 3: GloBE Computation (Ireland)

| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Number of CEs | 4 |
| Financial Accounting Net Income | €28,000,000 |
| GloBE Adjustments (net) | €4,800,000 |
| GloBE Income | €32,800,000 |
| Adjusted Covered Taxes | €3,800,000 |
| ETR | 11.59% |
| Eligible Payroll | €19,000,000 |
| Tangible Assets NBV | €17,000,000 |
| Payroll SBIE | €1,862,000 |
| Asset SBIE | €1,326,000 |
| Total SBIE | €3,188,000 |
| Excess Profit | €29,612,000 |
| Top-up Tax Percentage | 3.41% |
| Top-up Tax Amount | €1,009,769 |
| QDMTT Applied | €0 |
| IIR Top-up Tax | €1,009,769 |

---

## Audit File Checklist Data

**Input Data for Audit File Checklist (GIR-006):**

| Data Point | Value |
|------------|-------|
| Entity/Group Name | GlobalTech Manufacturing Ltd |
| Fiscal Year | 2024 |
| Number of Jurisdictions | 20 |
| Filing Entity | GlobalTech Manufacturing Ltd |
| GIR Filing Status | Draft - First Filing |
| Audit Date | [Current Date] |

**Sections to Include:**
- ☑ Section 1: General Information
- ☑ Section 2: Corporate Structure
- ☑ Section 3: GloBE Computation
- ☑ Elections Documentation
- ☑ Safe Harbour Documentation
- ☑ System & Process Controls

**Key Documentation Items to Track:**

| Category | Sample Items |
|----------|--------------|
| Section 1 | UPE incorporation certificate, Group org chart, DFE appointment letter |
| Section 2 | Entity listing with TINs, Ownership schedules, Entity classification memos |
| Section 3 | GloBE Income workpapers, Covered Tax calculations, SBIE schedules |
| Elections | Policy choice memorandum (none for first year) |
| Safe Harbour | CbCR report, Safe Harbour analysis by jurisdiction |
| Controls | Data collection process, Review sign-off procedures |
