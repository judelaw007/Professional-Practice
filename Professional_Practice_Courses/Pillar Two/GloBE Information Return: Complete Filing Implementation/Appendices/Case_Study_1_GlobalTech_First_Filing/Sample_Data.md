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

**Input Data for GIR ETR Calculator (GIR-001):**

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

**Input Data for GIR SBIE Calculator (GIR-002):**

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

**Input Data for GIR Top-Up Tax Calculator (GIR-003):**

| Data Point | Value |
|------------|-------|
| GloBE Income | €32,800,000 |
| Adjusted Covered Taxes | €3,800,000 |
| Total SBIE (from GIR-002) | €3,188,000 |
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

**Input Data for Safe Harbour Qualification Tool (GIR-004):**

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

For reference when using GIR-002:

| Rate Type | FY2024 Rate |
|-----------|-------------|
| Payroll Carve-out | 9.8% |
| Asset Carve-out | 7.8% |
