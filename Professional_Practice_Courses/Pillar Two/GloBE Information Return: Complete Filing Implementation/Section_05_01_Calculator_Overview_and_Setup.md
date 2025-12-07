# Section 5: GIR Completion Calculator - Sections 1-3

# 5.1 Calculator Overview and Setup

## Introduction

Preparing a GloBE Information Return requires calculating approximately **480 data points** spanning three sections. The calculations increase in complexity with each additional jurisdiction and Constituent Entity. A structured approach is essential.

This section explains:
- **GIR calculation architecture** aligned with the OECD structure
- **Key formulas** for ETR, SBIE, and Top-up Tax
- **Validation approaches** for error checking
- **How to practice** using demo tools on tools.mojitax.com

---

## Demo Tools vs Professional Tools

Before diving into the calculations, it's important to understand the difference between the demo tools you'll use for learning and the professional tools used in practice.

### Demo Tools (tools.mojitax.com)

This course integrates with **demo tools on tools.mojitax.com** for hands-on practice:

| Demo Tool | Tool ID | Purpose |
|-----------|---------|---------|
| GIR ETR Calculator | GIR-001 | Calculate jurisdictional ETR |
| GIR SBIE Calculator | GIR-002 | Calculate Substance-Based Income Exclusion |
| GIR Top-Up Tax Calculator | GIR-003 | Calculate complete Top-up Tax |
| Safe Harbour Qualification Tool | GIR-004 | Assess CbCR Safe Harbour eligibility |

**Demo tools are for learning.** They are:
- Simplified for educational focus
- Use sample data from course case studies
- Produce practice results (not for actual filing)
- Help you understand the calculation mechanics

### Professional Tools

In professional practice, you would use **enterprise Pillar Two software** such as:
- Big 4 firm proprietary solutions (e.g., KPMG Pillar Two Engine, PwC GloBE Calculator)
- Tax technology platforms (e.g., Thomson Reuters ONESOURCE, Vertex)
- ERP-integrated solutions (e.g., SAP Pillar Two modules)
- Specialist Pillar Two software providers

**Professional tools provide:**
- Full audit trails and version control
- Multi-user access with role-based permissions
- Integration with ERP and consolidation systems
- Automated XML generation and validation
- Compliance documentation and reporting

### When to Use Each

| Use Demo Tools When... | Use Professional Tools When... |
|------------------------|-------------------------------|
| Learning GIR calculations | Preparing actual GIR filings |
| Practicing with case study data | Working with real MNE data |
| Verifying your understanding | Generating XML for submission |
| Training team members | Documenting for audit purposes |

---

## Practice with Case Studies

As you learn the calculations in this section, practice using the **demo tools on tools.mojitax.com** with data from the course case studies:

| Case Study | Location | Demo Tools to Use |
|------------|----------|-------------------|
| GlobalTech First Filing | Appendix: Case Study 1 | GIR-001, GIR-002, GIR-003, GIR-004 |
| Complex Ownership | Appendix: Case Study 2 | GIR-001, GIR-002, GIR-003 |
| Data Gap Challenges | Appendix: Case Study 3 | GIR-001, GIR-002 |
| Multi-QDMTT Jurisdictions | Appendix: Case Study 4 | GIR-001, GIR-002, GIR-003 |

Each case study includes:
- **Sample_Data.md** - Input values to enter into demo tools
- **Expected_Outcomes.md** - Results to verify your calculations

---

## GIR Calculation Architecture

---

## 5.1.1 Calculator Architecture

The GIR Completion Calculator mirrors the three-section structure of the OECD GloBE Information Return, with additional supporting worksheets for data collection, validation, and output generation.

### GIR Structure Overview

```
┌─────────────────────────────────────────────────────────────────┐
│              GloBE Information Return Structure                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ SECTION 1: MNE GROUP INFORMATION (~50+ data points)    │     │
│  │                                                         │     │
│  │ 1.1 Filing Constituent Entity Identification           │     │
│  │ 1.2 Ultimate Parent Entity Information                 │     │
│  │ 1.3 Corporate Structure (all CEs)                      │     │
│  │ 1.4 High-Level Summary                                 │     │
│  └────────────────────────────────────────────────────────┘     │
│                              │                                  │
│                              ▼                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ SECTION 2: SAFE HARBOURS AND EXCLUSIONS (~40 points)   │     │
│  │                                                         │     │
│  │ 2.1 Transitional CbCR Safe Harbour Elections           │     │
│  │ 2.2 QDMTT Safe Harbour Elections                       │     │
│  │ 2.3 Transitional UTPR Safe Harbour Elections           │     │
│  │ 2.4 Excluded Jurisdictions                             │     │
│  └────────────────────────────────────────────────────────┘     │
│                              │                                  │
│                              ▼                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ SECTION 3: GloBE COMPUTATIONS (~400 data points)       │     │
│  │ [Repeats for each jurisdiction]                        │     │
│  │                                                         │     │
│  │ 3.1 GloBE Income Computation                           │     │
│  │ 3.2 Adjusted Covered Taxes                             │     │
│  │ 3.3 ETR Calculation                                    │     │
│  │ 3.4 Substance-Based Income Exclusion (SBIE)            │     │
│  │ 3.5 Top-up Tax Computation                             │     │
│  │ 3.6 Top-up Tax Allocation                              │     │
│  └────────────────────────────────────────────────────────┘     │
│                              │                                  │
│                              ▼                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ XML OUTPUT GENERATION                                   │     │
│  │                                                         │     │
│  │ Filing Info → General Section → Summary →              │     │
│  │ Jurisdiction Section → Subgroup (if applicable)        │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Calculator Worksheet Structure

The GIR Completion Calculator contains the following worksheets:

| Tab Name | Purpose | Section Reference |
|----------|---------|-------------------|
| **Instructions** | User guide, colour coding legend, quick start | N/A |
| **Setup** | Entity list, jurisdiction configuration, fiscal year | Configuration |
| **S1_Filing_CE** | Filing Constituent Entity identification | Section 1.1 |
| **S1_UPE** | Ultimate Parent Entity information | Section 1.2 |
| **S1_Corp_Structure** | Corporate structure for all CEs | Section 1.3 |
| **S1_Summary** | High-level summary by jurisdiction | Section 1.4 |
| **S2_Safe_Harbours** | Safe harbour elections and exclusions | Section 2 |
| **S3_GloBE_[JUR]** | GloBE Computation (one per jurisdiction) | Section 3 |
| **SBIE_Calculator** | Substance-Based Income Exclusion | Section 3.4 |
| **TopUp_Allocation** | Top-up Tax allocation (IIR/UTPR) | Section 3.6 |
| **Validation** | Data validation and error summary | Quality control |
| **XML_Output** | Data formatted for XML generation | Output |
| **Audit_Trail** | Change log and version control | Documentation |
| **Sample_Data** | Example data for testing | Testing |

### Data Flow Through the Calculator

```
┌─────────────────────────────────────────────────────────────────┐
│                    Calculator Data Flow                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT LAYER                                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                                                            │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐      │   │
│  │  │Financial│  │  Tax    │  │  SBIE   │  │ Entity  │      │   │
│  │  │  Data   │  │  Data   │  │  Data   │  │  Data   │      │   │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘      │   │
│  │       │            │            │            │            │   │
│  │       └────────────┴────────────┴────────────┘            │   │
│  │                         │                                  │   │
│  └─────────────────────────┼────────────────────────────────┘   │
│                            ▼                                    │
│  CALCULATION LAYER                                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                                                            │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │           GloBE Income Computation                   │  │   │
│  │  │  Financial Accounting Net Income + Adjustments      │  │   │
│  │  └─────────────────────────┬───────────────────────────┘  │   │
│  │                            ▼                               │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │         Adjusted Covered Taxes                       │  │   │
│  │  │  Current Tax + Deferred Tax Adjustments + 15% Cap   │  │   │
│  │  └─────────────────────────┬───────────────────────────┘  │   │
│  │                            ▼                               │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │              ETR Calculation                         │  │   │
│  │  │  Adjusted Covered Taxes ÷ GloBE Income = ETR        │  │   │
│  │  └─────────────────────────┬───────────────────────────┘  │   │
│  │                            ▼                               │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │         SBIE Calculation                             │  │   │
│  │  │  (Payroll × Rate) + (Tangible Assets × Rate)        │  │   │
│  │  └─────────────────────────┬───────────────────────────┘  │   │
│  │                            ▼                               │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │         Top-up Tax Computation                       │  │   │
│  │  │  (15% - ETR) × (GloBE Income - SBIE) = Top-up Tax   │  │   │
│  │  └─────────────────────────┬───────────────────────────┘  │   │
│  │                            ▼                               │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │         Top-up Tax Allocation                        │  │   │
│  │  │  QDMTT Credit → IIR Allocation → UTPR Allocation    │  │   │
│  │  └─────────────────────────────────────────────────────┘  │   │
│  │                                                            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  OUTPUT LAYER                                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                                                            │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐      │   │
│  │  │Section 1│  │Section 2│  │Section 3│  │   XML   │      │   │
│  │  │ Output  │  │ Output  │  │ Output  │  │  Ready  │      │   │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘      │   │
│  │                                                            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.1.2 Input Cell Identification

The calculator uses a standardized colour coding system to clearly distinguish input cells from calculations, reference data, and outputs. This ensures users know exactly where to enter data and avoids accidental overwriting of formulas.

### Colour Coding Legend

| Colour | Hex Code | Meaning | User Action |
|--------|----------|---------|-------------|
| ![#FFFF99](https://via.placeholder.com/15/FFFF99/FFFF99) **Light Yellow** | #FFFF99 | **INPUT REQUIRED** - Enter data here | Enter your data |
| ![#E2EFDA](https://via.placeholder.com/15/E2EFDA/E2EFDA) **Light Green** | #E2EFDA | **CALCULATION** - Formula cell | Do not edit |
| ![#DDEBF7](https://via.placeholder.com/15/DDEBF7/DDEBF7) **Light Blue** | #DDEBF7 | **REFERENCE DATA** - Lookup values | Do not edit |
| ![#FCE4D6](https://via.placeholder.com/15/FCE4D6/FCE4D6) **Light Orange** | #FCE4D6 | **CONDITIONAL INPUT** - May need entry | Enter if applicable |
| ![#F2F2F2](https://via.placeholder.com/15/F2F2F2/F2F2F2) **Light Grey** | #F2F2F2 | **LOCKED** - Protected cell | Cannot edit |
| ![#FF6B6B](https://via.placeholder.com/15/FF6B6B/FF6B6B) **Light Red** | #FF6B6B | **ERROR** - Validation failed | Review and correct |
| ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/FFFFFF) **White** | #FFFFFF | **OUTPUT/DISPLAY** - Result | Read only |

### Visual Example: Input Cell Identification

```
┌─────────────────────────────────────────────────────────────────┐
│  Example: GloBE Income Computation Worksheet                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Row  │  A                    │  B                │  C          │
│  ─────┼───────────────────────┼───────────────────┼─────────────│
│    5  │ Financial Accounting  │                   │             │
│       │ Net Income or Loss    │ [YELLOW INPUT]    │ €           │
│  ─────┼───────────────────────┼───────────────────┼─────────────│
│    6  │ Add: Excluded         │                   │             │
│       │ Dividends             │ [YELLOW INPUT]    │ €           │
│  ─────┼───────────────────────┼───────────────────┼─────────────│
│    7  │ Less: Included Equity │                   │             │
│       │ Gain or Loss          │ [YELLOW INPUT]    │ €           │
│  ─────┼───────────────────────┼───────────────────┼─────────────│
│   ... │ [Additional           │                   │             │
│       │  adjustments]         │ [YELLOW INPUT]    │ €           │
│  ─────┼───────────────────────┼───────────────────┼─────────────│
│   25  │ TOTAL GloBE INCOME    │ [GREEN CALC]      │ € [Formula] │
│  ─────┼───────────────────────┼───────────────────┼─────────────│
│                                                                  │
│  LEGEND:                                                         │
│  [YELLOW INPUT] = Enter your data here                          │
│  [GREEN CALC]   = Automatic calculation (do not edit)           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Cell Protection Strategy

The calculator implements cell protection to prevent accidental edits:

| Protection Level | Cells Affected | Unlock Method |
|------------------|----------------|---------------|
| **Locked** | All formula cells, reference data | Cannot unlock |
| **Editable** | All input cells (yellow, orange) | No password required |
| **Hidden Formulas** | Complex calculations | Formulas not visible |
| **Sheet Protected** | All worksheets | Password: "GIR2025" (for admin use) |

### Input Data Types and Formats

| Data Type | Format | Example | Validation |
|-----------|--------|---------|------------|
| **Currency** | Number, 2 decimals, € symbol | €1,234,567.89 | Numeric only |
| **Percentage** | Percentage, 4 decimals | 15.0000% | 0-100% range |
| **Date** | DD-MMM-YYYY | 31-Dec-2025 | Valid date |
| **Text** | Free text | "ABC Corporation Ltd" | Max 255 characters |
| **TIN** | Text with validation | "GB123456789" | Country-specific format |
| **Country Code** | 2-letter ISO code | "GB", "DE", "US" | Valid ISO 3166-1 |
| **Yes/No** | Dropdown | "Yes" or "No" | Selection only |
| **Code** | Alphanumeric | "QIIR", "UTPR" | Valid code list |

---

## 5.1.3 Validation and Error Checking Features

The calculator includes comprehensive validation to identify errors before they propagate through calculations or appear in the final XML output.

### Validation Types

**Type 1: Cell-Level Validation**

Immediate validation on data entry:

| Validation Rule | Description | Error Message |
|-----------------|-------------|---------------|
| Required field | Field cannot be blank | "This field is required" |
| Numeric only | Must be a number | "Enter a numeric value" |
| Positive value | Cannot be negative | "Value must be positive" |
| Valid range | Within specified limits | "Value outside valid range" |
| Valid code | From predefined list | "Invalid code selected" |
| Date format | Correct date format | "Invalid date format" |
| TIN format | Country-specific TIN | "Invalid TIN format for [country]" |

**Type 2: Cross-Field Validation**

Validation across related fields:

| Validation Rule | Fields Involved | Error Message |
|-----------------|-----------------|---------------|
| Ownership sum | Ownership % for an entity | "Ownership must equal 100%" |
| IC balance | Intercompany pairs | "Intercompany imbalance detected" |
| Date sequence | Period start/end | "End date must be after start date" |
| Entity reference | Entity lookups | "Entity not found in entity list" |
| Jurisdiction match | Entity jurisdiction | "Entity jurisdiction mismatch" |

**Type 3: Section-Level Validation**

Validation at section completion:

| Validation Rule | Section | Error Message |
|-----------------|---------|---------------|
| All CEs included | Section 1.3 | "Not all CEs have corporate structure data" |
| Safe harbour eligibility | Section 2 | "Safe harbour elected but criteria not met" |
| ETR calculation complete | Section 3 | "Missing data for ETR calculation" |
| SBIE data present | Section 3.4 | "SBIE elected but payroll/asset data missing" |
| Top-up Tax allocation | Section 3.6 | "Top-up Tax not fully allocated" |

**Type 4: GIR-Level Validation**

Final validation before XML generation:

| Validation Rule | Description | Error Message |
|-----------------|-------------|---------------|
| Section 1 complete | All required fields populated | "Section 1 incomplete" |
| Section 2 complete | All elections documented | "Section 2 incomplete" |
| Section 3 complete | All jurisdictions processed | "Section 3 incomplete for [jurisdiction]" |
| Total Top-up Tax | Reconciliation check | "Top-up Tax amounts do not reconcile" |
| XML schema compliance | Data format verification | "Data format incompatible with XML schema" |

### Validation Dashboard

The **Validation** worksheet provides a comprehensive error summary:

```
┌─────────────────────────────────────────────────────────────────┐
│                    VALIDATION DASHBOARD                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  OVERALL STATUS: ⚠️ WARNINGS PRESENT                             │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  SECTION SUMMARY:                                                │
│  ┌──────────────┬────────────┬────────────┬────────────┐       │
│  │ Section      │ Errors     │ Warnings   │ Status     │       │
│  ├──────────────┼────────────┼────────────┼────────────┤       │
│  │ Section 1    │ 0          │ 1          │ ⚠️         │       │
│  │ Section 2    │ 0          │ 0          │ ✅         │       │
│  │ Section 3    │ 2          │ 3          │ ❌         │       │
│  │ Overall      │ 2          │ 4          │ ❌         │       │
│  └──────────────┴────────────┴────────────┴────────────┘       │
│                                                                  │
│  ERROR DETAILS:                                                  │
│  ┌────┬──────────┬────────────────────────────────────────┐    │
│  │ #  │ Location │ Error Description                       │    │
│  ├────┼──────────┼────────────────────────────────────────┤    │
│  │ 1  │ S3_DE:C15│ Current Tax Expense is negative        │    │
│  │ 2  │ S3_US:D32│ SBIE payroll exceeds total payroll     │    │
│  └────┴──────────┴────────────────────────────────────────┘    │
│                                                                  │
│  WARNING DETAILS:                                                │
│  ┌────┬──────────┬────────────────────────────────────────┐    │
│  │ #  │ Location │ Warning Description                     │    │
│  ├────┼──────────┼────────────────────────────────────────┤    │
│  │ 1  │ S1:E25   │ TIN format not validated for SG        │    │
│  │ 2  │ S3_UK:C8 │ ETR unusually high (>40%)              │    │
│  │ 3  │ S3_DE:C45│ SBIE significantly reduces excess profit│    │
│  │ 4  │ S3_US:C50│ Prior period adjustment >€1M           │    │
│  └────┴──────────┴────────────────────────────────────────┘    │
│                                                                  │
│  [REFRESH VALIDATION]              [EXPORT ERROR LOG]           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Validation Status Indicators

| Indicator | Meaning | Action Required |
|-----------|---------|-----------------|
| ✅ **Green Check** | Validation passed | None |
| ⚠️ **Yellow Warning** | Potential issue | Review and confirm |
| ❌ **Red X** | Validation failed | Must resolve before filing |
| ⏳ **Pending** | Validation not yet run | Click Refresh |
| ℹ️ **Info** | Informational message | For reference only |

---

## 5.1.4 Key Formulas and Calculations

The calculator automates all GloBE computations. Understanding the key formulas helps validate results and troubleshoot issues.

### ETR Calculation

```
Jurisdictional ETR = Adjusted Covered Taxes ÷ GloBE Income

Where:
• GloBE Income = Financial Accounting Net Income + GloBE Adjustments
• Adjusted Covered Taxes = Current Tax + Deferred Tax Adjustment Amount

Result rounded to 4 decimal places (e.g., 14.2356%)
```

**Calculator Formula (Cell Reference Example):**
```
=IF(GloBE_Income>0, ROUND(Adjusted_Covered_Taxes/GloBE_Income, 4), "N/A")
```

### Top-up Tax Percentage

```
Top-up Tax Percentage = MAX(0, 15% - Jurisdictional ETR)

Examples:
• If ETR = 12%, Top-up Tax % = 15% - 12% = 3%
• If ETR = 18%, Top-up Tax % = MAX(0, 15% - 18%) = 0%
```

### Substance-Based Income Exclusion (SBIE)

```
SBIE = Payroll Carve-out + Tangible Asset Carve-out

Where:
• Payroll Carve-out = Eligible Payroll Costs × Payroll Rate
• Tangible Asset Carve-out = Eligible Tangible Asset NBV × Asset Rate
```

**Transitional Phase-In Rates:**

| Fiscal Year | Payroll Rate | Tangible Asset Rate |
|-------------|--------------|---------------------|
| 2024 | 10.0% | 8.0% |
| 2025 | 9.8% | 7.8% |
| 2026 | 9.6% | 7.6% |
| 2027 | 9.4% | 7.4% |
| 2028 | 9.2% | 7.2% |
| 2029 | 9.0% | 7.0% |
| 2030 | 8.2% | 6.6% |
| 2031 | 7.4% | 6.2% |
| 2032 | 6.6% | 5.8% |
| 2033+ | 5.0% | 5.0% |

**Calculator Formula:**
```
=VLOOKUP(Fiscal_Year, SBIE_Rates_Table, Payroll_Column, FALSE) * Eligible_Payroll
```

### Excess Profit

```
Excess Profit = GloBE Income - SBIE

If Excess Profit ≤ 0, no Top-up Tax applies for the jurisdiction
```

### Top-up Tax Amount

```
Top-up Tax = (Top-up Tax % × Excess Profit) + Additional Top-up Tax - QDMTT Credit

Where:
• Additional Top-up Tax = Recaptured amounts, prior period adjustments
• QDMTT Credit = Qualified Domestic Minimum Top-up Tax paid
```

### IIR Allocation

```
IIR Amount for Parent = Jurisdictional Top-up Tax × Parent's Allocable Share

Allocable Share = Ownership % in Low-Taxed CEs (adjusted for intermediate owners)
```

### UTPR Allocation

```
UTPR Amount for CE = UTPR Top-up Tax × UTPR Allocation Key

UTPR Allocation Key = 50% × (CE Employees / Total UTPR Employees)
                    + 50% × (CE Tangible Assets / Total UTPR Tangible Assets)
```

---

## 5.1.5 Sample Data for Testing

The calculator includes sample data to help you understand the data entry process and validate that formulas are working correctly.

### Accessing Sample Data

The **Sample_Data** worksheet contains a complete worked example for a fictional MNE group:

| Sample MNE Group | Details |
|------------------|---------|
| **Group Name** | GlobalCo Holdings plc |
| **UPE Jurisdiction** | United Kingdom |
| **Fiscal Year End** | 31 December 2025 |
| **Consolidated Revenue** | €3.2 billion |
| **Constituent Entities** | 45 entities |
| **Jurisdictions** | 12 countries |

### Sample Data Overview

**Sample Entities (Subset):**

| Entity Name | Jurisdiction | GloBE Status | Ownership |
|-------------|--------------|--------------|-----------|
| GlobalCo Holdings plc | UK | UPE | 100% |
| GlobalCo UK Ltd | UK | CE | 100% |
| GlobalCo GmbH | Germany | CE | 100% |
| GlobalCo Inc | United States | CE | 100% |
| GlobalCo Pte Ltd | Singapore | CE | 100% |
| GlobalCo BV | Netherlands | CE | 100% |
| GlobalCo SARL | Luxembourg | CE | 100% |
| GlobalCo IP Ltd | Ireland | CE | 100% |

**Sample Section 3 Data (Singapore - Low-Tax Jurisdiction):**

| Data Point | Sample Value |
|------------|--------------|
| Financial Accounting Net Income | €15,000,000 |
| GloBE Adjustments (net) | €500,000 |
| GloBE Income | €15,500,000 |
| Current Tax Expense | €1,200,000 |
| Deferred Tax Adjustment | €100,000 |
| Adjusted Covered Taxes | €1,300,000 |
| **Jurisdictional ETR** | **8.39%** |
| Eligible Payroll Costs | €3,000,000 |
| Eligible Tangible Assets | €8,000,000 |
| SBIE (2025 rates: 9.8%/7.8%) | €918,000 |
| Excess Profit | €14,582,000 |
| Top-up Tax % | 6.61% |
| **Jurisdictional Top-up Tax** | **€963,870** |

### Using Sample Data

**Step 1: Load Sample Data**

1. Open the calculator file
2. Navigate to the **Sample_Data** worksheet
3. Click the **[Load Sample Data]** button
4. Sample data populates all input worksheets

**Step 2: Review Populated Worksheets**

1. Navigate through each section worksheet
2. Observe how input cells are populated
3. Review calculated results in green cells
4. Check the Validation worksheet for any issues

**Step 3: Experiment with Changes**

1. Modify sample values to see calculation impacts
2. Try changing the Singapore GloBE Income to €20,000,000
3. Observe how ETR, SBIE, and Top-up Tax recalculate
4. Reset to original sample data using **[Reset Sample Data]**

**Step 4: Clear Sample Data**

1. Click **[Clear All Data]** before entering your own data
2. Confirm the clear operation
3. All input cells return to blank/default state

### Sample Data Validation Results

The sample data produces a clean validation result:

| Section | Errors | Warnings | Notes |
|---------|--------|----------|-------|
| Section 1 | 0 | 0 | All entity data complete |
| Section 2 | 0 | 0 | CbCR Safe Harbour elected for Ireland |
| Section 3 | 0 | 1 | Warning: Singapore ETR < 15% (expected) |
| Overall | 0 | 1 | Ready for XML generation |

---

## 5.1.6 Calculator Setup Procedures

Follow these steps to configure the calculator for your MNE group's GIR preparation.

### Step 1: Initial Configuration

**1.1 Open Calculator File**

- Open **GIR_Completion_Calculator_v2025.xlsx**
- Enable macros when prompted (required for validation functions)
- Navigate to the **Setup** worksheet

**1.2 Enter Fiscal Year Information**

| Field | Entry | Example |
|-------|-------|---------|
| Reporting Fiscal Year Start | DD-MMM-YYYY | 01-Jan-2025 |
| Reporting Fiscal Year End | DD-MMM-YYYY | 31-Dec-2025 |
| First Year Subject to GloBE? | Yes/No | Yes |
| Transition Year? | Yes/No | Yes |

**1.3 Select Currency**

| Field | Entry | Notes |
|-------|-------|-------|
| Group Presentation Currency | ISO code | EUR, USD, GBP, etc. |
| Decimal Places | 0, 2 | Typically 0 for rounding |

**1.4 Configure Jurisdictions**

Add all jurisdictions where the MNE group has Constituent Entities:

| Jurisdiction Code | Jurisdiction Name | Active | QDMTT? | IIR? | UTPR? |
|-------------------|-------------------|--------|--------|------|-------|
| GB | United Kingdom | Yes | Yes | Yes | Yes |
| DE | Germany | Yes | Yes | Yes | Yes |
| US | United States | Yes | No | No | No |
| SG | Singapore | Yes | No | No | No |
| NL | Netherlands | Yes | Yes | Yes | Yes |
| ... | ... | ... | ... | ... | ... |

### Step 2: Entity Master Setup

**2.1 Navigate to Setup > Entity List**

**2.2 Enter All Constituent Entities**

| Field | Required | Description |
|-------|----------|-------------|
| Entity ID | Yes | Unique identifier (e.g., CE001) |
| Legal Name | Yes | Full legal entity name |
| Jurisdiction | Yes | 2-letter country code |
| TIN | Yes* | Tax Identification Number (*or "NOTIN") |
| GloBE Status | Yes | UPE, CE, PE, Excluded, etc. |
| Parent Entity ID | Yes | Direct parent's Entity ID |
| Ownership % | Yes | Ownership by parent |
| Consolidation Method | Yes | Full, Proportionate, Equity |
| Active in Fiscal Year | Yes | Yes/No |

**2.3 Verify Entity Hierarchy**

After entering all entities, click **[Verify Hierarchy]** to confirm:
- All entities trace back to UPE
- Ownership percentages are valid
- No circular references exist

### Step 3: Worksheet Generation

**3.1 Generate Jurisdiction Worksheets**

Based on your jurisdiction configuration, the calculator creates Section 3 worksheets:

1. Click **[Generate Worksheets]** on the Setup page
2. The calculator creates one **S3_GloBE_[JUR]** worksheet per jurisdiction
3. Worksheets are pre-configured with entities in that jurisdiction

**3.2 Review Generated Worksheets**

| Worksheet | Created For |
|-----------|-------------|
| S3_GloBE_GB | United Kingdom - 5 entities |
| S3_GloBE_DE | Germany - 3 entities |
| S3_GloBE_US | United States - 12 entities |
| S3_GloBE_SG | Singapore - 2 entities |
| ... | ... |

### Step 4: Data Entry Mode Selection

Choose your data entry approach:

| Mode | Description | Recommended For |
|------|-------------|-----------------|
| **CE-by-CE** | Enter data for each CE separately | Full detail; first-time users |
| **Jurisdictional** | Enter aggregated jurisdictional data | Simplified reporting; experienced users |
| **Transitional Simplified** | Jurisdictional with reduced detail | Transition period; limited data availability |

To select mode:
1. Navigate to Setup > Data Entry Mode
2. Select your preferred mode
3. Worksheets adjust to display appropriate input fields

### Step 5: Ready for Data Entry

After completing setup:

✅ Fiscal year configured
✅ Currency selected
✅ All jurisdictions added
✅ All entities entered and verified
✅ Jurisdiction worksheets generated
✅ Data entry mode selected

**You are now ready to proceed to Section 5.2: Completing GIR Section 1**

---

## 5.1.7 Calculator Maintenance

### Version Control

The calculator maintains version information:

| Field | Location | Example |
|-------|----------|---------|
| Calculator Version | Instructions tab | v2025.1.0 |
| GIR Template Version | Instructions tab | January 2025 |
| XML Schema Version | Instructions tab | 1.0.0 |
| Last Updated | Instructions tab | 15-Nov-2025 |

### Backup Procedures

**Before Major Data Entry Sessions:**
1. Save current version with date: `GIR_Calculator_YYYYMMDD.xlsx`
2. Store in version-controlled location
3. Document backup in Audit_Trail worksheet

**After Completing Each Section:**
1. Save working copy
2. Create section checkpoint backup
3. Note completion in Audit_Trail

### Update Procedures

When calculator updates are released:

1. Download new calculator version
2. Open both old and new calculators
3. Use **[Import Prior Data]** function in new version
4. Verify data imported correctly
5. Run validation checks
6. Archive old version

### Troubleshooting Common Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Macros not working | Macros disabled | Enable macros in Excel settings |
| Formulas show #REF! | Missing named ranges | Click [Repair Formulas] on Setup |
| Validation not running | Protected view | Save locally and reopen |
| Slow performance | Large entity count | Enable calculation mode: Manual |
| Print issues | Page setup | Use [Reset Print Settings] |

---

## Summary: Calculator Setup Checklist

Before proceeding to data entry, confirm:

| # | Setup Step | Status |
|---|------------|--------|
| 1 | Calculator file opened with macros enabled | ☐ |
| 2 | Fiscal year start and end dates entered | ☐ |
| 3 | Group presentation currency selected | ☐ |
| 4 | All jurisdictions added with correct flags | ☐ |
| 5 | All Constituent Entities entered | ☐ |
| 6 | Entity hierarchy verified (no errors) | ☐ |
| 7 | Jurisdiction worksheets generated | ☐ |
| 8 | Data entry mode selected | ☐ |
| 9 | Sample data tested and cleared | ☐ |
| 10 | Backup copy saved | ☐ |

---

## Template References

| Template | Description | Format |
|----------|-------------|--------|
| GIR_Completion_Calculator_v2025.xlsx | Main calculator workbook | Excel |
| Calculator_Quick_Start_Guide.pdf | 2-page setup summary | PDF |
| Sample_Data_Package.xlsx | Extended sample data set | Excel |
| Validation_Error_Codes.pdf | Complete error code reference | PDF |

---

## Key Takeaways

1. **The calculator mirrors GIR structure** - Three sections with supporting worksheets for each GIR component

2. **Colour coding guides data entry** - Yellow = input required; Green = formula (don't edit); Blue = reference data

3. **Validation catches errors early** - Cell-level, cross-field, section-level, and GIR-level validation

4. **Sample data aids learning** - Load sample data to understand the calculator before entering real data

5. **Setup is critical** - Correct configuration of fiscal year, jurisdictions, and entities is essential

6. **Formulas are pre-built** - ETR, SBIE, Top-up Tax, and allocation calculations are automatic

7. **SBIE uses transitional rates** - Calculator applies correct phase-in rates based on fiscal year

8. **Version control matters** - Maintain backups and use the Audit_Trail worksheet

---

## Practice This Skill: GIR Practice Form

Before working with production calculators, practice data entry using the **GIR Practice Form (GIR-008)** on tools.mojitax.com.

| Tool | Tool ID | Purpose |
|------|---------|---------|
| GIR Practice Form | GIR-008 | Practice populating GIR Sections 1, 2, and 3 with sample data |

**Demo Tool vs Professional Tool**

This is a demo tool for learning purposes. In professional practice, you would use enterprise Pillar Two software or the official GIR Completion Calculator. The demo tool helps you understand form structure and field relationships.

**To Practice:**

1. Go to tools.mojitax.com and find **GIR Practice Form**
2. Start with **Case Study 1** (GlobalTech) sample data:
   - Practice Section 1: Enter MNE Group information
   - Practice Section 2: Enter Safe Harbour elections
   - Practice Section 3: Enter GloBE computations
3. The form provides real-time validation and guidance
4. Review completion percentage and cross-reference checks

Use all 5 case studies in the Appendices to practice different scenarios.

---

## Sources and References

- [OECD: GloBE Information Return (Pillar Two) XML Schema (January 2025)](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html)
- [OECD: Tax Challenges Arising from the Digitalisation of the Economy – GloBE Information Return (January 2025)](https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html)
- [OECD: Draft User Guide for the GloBE Information Return XML Schema](https://www.oecd.org/en/events/public-consultations/2024/07/draft-user-guide-for-the-globe-information-return-xml-schema.html)
- [KPMG: Pillar Two GloBE Information Return](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/07/pillar-two-globe-information-return.pdf)
- [oecdpillars.com: ETR Calculation and Top-Up Tax](https://oecdpillars.com/pillar-tab/etr-calculation-and-top-up-tax-2/)
- [PwC: Pillar Two Data Input Catalog (January 2025)](https://www.pwc.com/gx/en/services/tax/assets/pwc-pillar-two-data-input-catalog.pdf)
- [oecdpillars.com: A Review of Changes in the OECD's Updated January 2025 GloBE Information Return](https://oecdpillars.com/a-review-of-changes-in-the-oecds-updated-january-2025-globe-information-return/)

---

*This section provides the foundation for using the GIR Completion Calculator. The next section (5.2 Completing GIR Section 1: MNE Group Information) guides you through entering data for the first section of the GloBE Information Return.*
