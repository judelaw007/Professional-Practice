# GIR-004: GIR Practice Form

## Tool Specification Document (v2 - Consolidated)

**Version:** 2.0
**Status:** Draft
**Last Updated:** 2024-12-08
**Consolidates:** Previous GIR-006 (Data Point Reference) + GIR-008 (Practice Form)

---

## 1. Tool Metadata

| Attribute | Value |
|-----------|-------|
| Tool ID | GIR-004 |
| Tool Name | GIR Practice Form |
| Category | Pillar Two / Form Practice |
| Complexity | High |
| Estimated Dev Time | 7-10 days |
| Dependencies | GIR-001 (for calculation verification) |
| Related Tools | GIR-001 (GloBE Calculator), GIR-006 (Audit Checklist) |
| Course Section | Section 4.1 (Data Points) + Section 5.1 (Calculator Overview) |

---

## 2. Purpose & Learning Objectives

### 2.1 Purpose

The GIR Practice Form is a comprehensive interactive tool that combines form practice with integrated data point reference. Learners can practice populating all three GIR sections while receiving contextual guidance on each field's requirements, data sources, and common issues.

### 2.2 Learning Objectives

Upon using this tool, learners will be able to:

1. **Navigate** the GIR form structure across all three sections
2. **Enter** data correctly in the appropriate format for each field
3. **Understand** field dependencies and cross-references between sections
4. **Look up** any of the ~480 GIR data points via integrated search
5. **Validate** data entries against format requirements
6. **Identify** common data collection challenges and sources
7. **Build confidence** before using actual tax authority filing portals

### 2.3 Why This Tool is Consolidated

The Data Point Reference (old GIR-006) and Practice Form (old GIR-008) are naturally complementary:
- When filling out a form field, users need to know what data to enter
- The reference provides context; the form provides practice
- Integrating them provides a seamless learning experience
- Users don't need to switch between tools while practicing

### 2.4 Integration Design

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIR PRACTICE FORM WITH INTEGRATED REFERENCE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────┐  ┌─────────────────────────────────┐  │
│  │                                 │  │                                 │  │
│  │     FORM ENTRY AREA             │  │    CONTEXTUAL HELP PANEL        │  │
│  │     (Sections 1-3)              │  │    (Data Point Reference)       │  │
│  │                                 │  │                                 │  │
│  │  Click any field to see        │──▶│  • Field definition            │  │
│  │  contextual help               │  │  • Data type & format          │  │
│  │                                 │  │  • ERP source mapping          │  │
│  │                                 │  │  • Common issues               │  │
│  │                                 │  │  • Related fields              │  │
│  │                                 │  │                                 │  │
│  └─────────────────────────────────┘  └─────────────────────────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🔍 SEARCH DATA POINTS: [________________________] [ Search ]       │   │
│  │  Browse: [All Sections ▼] [All Types ▼] [Required Only ☐]          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Tool Structure

### 3.1 Main Navigation Tabs

| Tab | Content | Field Count |
|-----|---------|-------------|
| Section 1: General Information | Group, filing entity, elections | ~50 fields |
| Section 2: Corporate Structure | Entity details (per CE) | ~85 fields per entity |
| Section 3: GloBE Computation | Calculations (per jurisdiction) | ~350+ fields |
| Data Point Search | Searchable reference of all ~480 data points | Reference |

### 3.2 Contextual Help Panel (Always Visible)

When user clicks/focuses on any form field, the help panel displays:
- Field name and ID
- Data type and format requirements
- Whether required/optional/conditional
- Typical ERP/source system mapping
- Common issues and solutions
- Related fields in other sections

---

## 4. Section 1: General Information Fields

### 4.1 MNE Group Identification

| Field ID | Field Name | Type | Required | Format | Help Text |
|----------|------------|------|----------|--------|-----------|
| S1.1.1 | MNE Group Name | Text | Yes | Max 200 chars | Legal name of the MNE group |
| S1.1.2 | UPE Legal Name | Text | Yes | Max 200 chars | Ultimate Parent Entity legal name |
| S1.1.3 | UPE Jurisdiction | Code | Yes | ISO 3166-1 | Country of UPE incorporation |
| S1.1.4 | UPE Tax ID | Text | Conditional | Varies | Tax identification number (use "NOTIN" if none) |
| S1.1.5 | LEI | Text | Optional | 20 chars | Legal Entity Identifier if available |

### 4.2 Reporting Period

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S1.2.1 | Fiscal Year Start | Date | Yes | YYYY-MM-DD |
| S1.2.2 | Fiscal Year End | Date | Yes | YYYY-MM-DD |
| S1.2.3 | Reporting Currency | Code | Yes | ISO 4217 (EUR, USD, GBP) |
| S1.2.4 | First Filing Year | Boolean | Yes | Yes/No |
| S1.2.5 | Consolidated Revenue | Numeric | Yes | Currency, 2 decimals |

### 4.3 Filing Entity Details

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S1.3.1 | DFE Name | Text | Yes | Max 200 chars |
| S1.3.2 | DFE Jurisdiction | Code | Yes | ISO 3166-1 |
| S1.3.3 | DFE Tax ID | Text | Yes | Jurisdiction format |
| S1.3.4 | Filing Type | Code | Yes | ORIGINAL / AMENDED |
| S1.3.5 | Amendment Reason | Text | Conditional | Required if AMENDED |

---

## 5. Section 2: Corporate Structure Fields (Per Entity)

### 5.1 Entity Identification

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S2.1.1 | Entity Name | Text | Yes | Max 200 chars |
| S2.1.2 | Entity Internal ID | Text | Yes | Reference ID |
| S2.1.3 | Jurisdiction | Code | Yes | ISO 3166-1 |
| S2.1.4 | Entity Tax ID | Text | Conditional | Jurisdiction format |
| S2.1.5 | Date of Incorporation | Date | Optional | YYYY-MM-DD |

### 5.2 Ownership Information

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S2.2.1 | Direct Parent Entity | Reference | Yes | Entity ID |
| S2.2.2 | Ownership Percentage | Numeric | Yes | 0-100%, 2 decimals |
| S2.2.3 | Ownership Type | Code | Yes | DIRECT / INDIRECT |
| S2.2.4 | Controlling Interest | Boolean | Yes | Yes/No |

### 5.3 Entity Classification

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S2.3.1 | Entity Type | Code | Yes | UPE / CE / PE / JV / MOCE |
| S2.3.2 | Is Excluded Entity | Boolean | Yes | Yes/No |
| S2.3.3 | Exclusion Reason | Code | Conditional | If Excluded = Yes |
| S2.3.4 | POPE Status | Boolean | Optional | Yes/No |
| S2.3.5 | Investment Entity | Boolean | Optional | Yes/No |

---

## 6. Section 3: GloBE Computation Fields (Per Jurisdiction)

### 6.1 GloBE Income Calculation

| Field ID | Field Name | Type | Required | Calculated |
|----------|------------|------|----------|------------|
| S3.2.1 | Financial Accounting Net Income | Numeric | Yes | No |
| S3.2.2 | Net Taxes Included in Income | Numeric | Yes | No |
| S3.2.3 | Excluded Dividends | Numeric | Optional | No |
| S3.2.4 | Excluded Equity Gains/Losses | Numeric | Optional | No |
| S3.2.5 | Policy Disallowed Expenses | Numeric | Optional | No |
| S3.2.6 | Stock Compensation Adjustment | Numeric | Optional | No |
| S3.2.7 | Other GloBE Adjustments | Numeric | Optional | No |
| **S3.2.8** | **GloBE Income** | **Numeric** | **Yes** | **Auto-calculated** |

### 6.2 Adjusted Covered Taxes

| Field ID | Field Name | Type | Required | Calculated |
|----------|------------|------|----------|------------|
| S3.3.1 | Current Tax Expense | Numeric | Yes | No |
| S3.3.2 | Deferred Tax Expense | Numeric | Yes | No |
| S3.3.3 | Total Tax Expense | Numeric | Yes | Auto |
| S3.3.4 | UTP Adjustment | Numeric | Optional | No |
| S3.3.5 | Non-Covered Tax Adjustment | Numeric | Optional | No |
| **S3.3.6** | **Adjusted Covered Taxes** | **Numeric** | **Yes** | **Auto-calculated** |

### 6.3 SBIE Calculation

| Field ID | Field Name | Type | Required | Calculated |
|----------|------------|------|----------|------------|
| S3.4.1 | Eligible Payroll Costs | Numeric | Yes | No |
| S3.4.2 | Payroll Carve-out Rate | Numeric | Auto | FY-based (9.8% for 2024) |
| S3.4.3 | Payroll SBIE | Numeric | Yes | Auto |
| S3.4.4 | Eligible Tangible Assets (NBV) | Numeric | Yes | No |
| S3.4.5 | Asset Carve-out Rate | Numeric | Auto | FY-based (7.8% for 2024) |
| S3.4.6 | Asset SBIE | Numeric | Yes | Auto |
| **S3.4.7** | **Total SBIE** | **Numeric** | **Yes** | **Auto-calculated** |

### 6.4 Top-up Tax Calculation

| Field ID | Field Name | Type | Required | Calculated |
|----------|------------|------|----------|------------|
| S3.5.1 | GloBE Income | Numeric | From S3.2.8 | Reference |
| S3.5.2 | Adjusted Covered Taxes | Numeric | From S3.3.6 | Reference |
| S3.5.3 | **Jurisdictional ETR** | Numeric | Yes | Auto (Taxes/Income) |
| S3.5.4 | Minimum Rate | Numeric | Constant | 15.00% |
| S3.5.5 | **Top-up Tax %** | Numeric | Yes | Auto (15% - ETR) |
| S3.5.6 | Total SBIE | Numeric | From S3.4.7 | Reference |
| S3.5.7 | **Excess Profit** | Numeric | Yes | Auto (Income - SBIE) |
| S3.5.8 | **Gross Top-up Tax** | Numeric | Yes | Auto |
| S3.5.9 | QDMTT Amount | Numeric | Optional | No |
| S3.5.10 | **Net Top-up Tax** | Numeric | Yes | Auto (Gross - QDMTT) |

---

## 7. Integrated Data Point Reference

### 7.1 Search Functionality

| Feature | Description |
|---------|-------------|
| Keyword Search | Search by field name, description, or XML element |
| Section Filter | Filter by Section 1, 2, 3, or subsections |
| Type Filter | Filter by Text, Numeric, Date, Code, Boolean |
| Required Filter | Show Required Only, Optional Only, or All |
| Results Display | List with click-to-navigate to form field |

### 7.2 Data Point Detail Panel

When a field is selected, display:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FIELD: S3.2.8 - GloBE Income                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DEFINITION                                                                 │
│  The net GloBE Income for the jurisdiction after all adjustments per       │
│  Article 3.1 of the GloBE Model Rules.                                     │
│                                                                             │
│  TECHNICAL DETAILS                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Data Type:     Numeric (Currency)                                    │   │
│  │ Format:        2 decimal places                                      │   │
│  │ Required:      Yes                                                   │   │
│  │ Calculated:    Yes (sum of S3.2.1 through S3.2.7)                   │   │
│  │ XML Element:   <GloBEIncome>                                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ERP SOURCE MAPPING                                                         │
│  • SAP: Sum of GL accounts in profit/loss + adjustment schedules           │
│  • Oracle: Financial statement income + manual adjustments                  │
│  • Generic: Trial balance net income + GloBE adjustment workpaper          │
│                                                                             │
│  COMMON ISSUES                                                              │
│  ⚠️ Ensure excluded dividends are properly added back                      │
│  ⚠️ Stock compensation timing differences often overlooked                 │
│  ⚠️ Must match consolidated accounts after eliminations                    │
│                                                                             │
│  RELATED FIELDS                                                             │
│  • S3.5.1 (used in ETR calculation)                                        │
│  • S3.5.7 (used in Excess Profit calculation)                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 Sample Data Points Database

| DP ID | Field Name | Section | Type | Required |
|-------|------------|---------|------|----------|
| DP-001 | MNE Group Name | 1.1 | Text | Yes |
| DP-002 | UPE Legal Name | 1.1 | Text | Yes |
| DP-003 | UPE Jurisdiction | 1.1 | Code | Yes |
| DP-010 | Entity Name | 2.1 | Text | Yes |
| DP-011 | Entity Jurisdiction | 2.1 | Code | Yes |
| DP-020 | Ownership Percentage | 2.2 | Numeric | Yes |
| DP-301 | Financial Accounting Income | 3.2 | Numeric | Yes |
| DP-302 | GloBE Income | 3.2 | Numeric | Calculated |
| DP-310 | Current Tax Expense | 3.3 | Numeric | Yes |
| DP-320 | Adjusted Covered Taxes | 3.3 | Numeric | Calculated |
| DP-340 | Jurisdictional ETR | 3.5 | Numeric | Calculated |
| DP-350 | Eligible Payroll | 3.4 | Numeric | Yes |
| DP-351 | Eligible Assets | 3.4 | Numeric | Yes |
| DP-352 | Total SBIE | 3.4 | Numeric | Calculated |
| DP-360 | Net Top-up Tax | 3.5 | Numeric | Calculated |

---

## 8. Validation & Cross-Reference Checks

### 8.1 Field-Level Validation

| Validation | Rule | Error Message |
|------------|------|---------------|
| Required fields | Cannot be empty | "This field is required" |
| Numeric format | Must be valid number | "Please enter a valid number" |
| Date format | Must be YYYY-MM-DD | "Please enter date as YYYY-MM-DD" |
| Code values | Must match allowed list | "Please select a valid option" |
| Percentage range | 0-100 for ownership | "Percentage must be between 0 and 100" |

### 8.2 Cross-Reference Validation

| Check ID | Description | Sections | Validation |
|----------|-------------|----------|------------|
| XR-001 | ETR Calculation | S3.2, S3.3, S3.5 | ETR = Covered Taxes / GloBE Income |
| XR-002 | SBIE Total | S3.4 | Total = Payroll SBIE + Asset SBIE |
| XR-003 | Excess Profit | S3.2, S3.4, S3.5 | Excess = GloBE Income - SBIE |
| XR-004 | Top-up Tax | S3.5 | Top-up = Excess Profit × Top-up % |
| XR-005 | Ownership Sum | S2.2 | Direct ownership should trace to 100% |
| XR-006 | Entity Count | S2, S3 | Entities in S2 should match jurisdictions in S3 |

### 8.3 Validation Status Display

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  VALIDATION STATUS                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✅ XR-001: ETR Calculation              PASS (11.59% = €3.8M / €32.8M)    │
│  ✅ XR-002: SBIE Total                   PASS (€3,188,000 = €1.86M + €1.33M)│
│  ✅ XR-003: Excess Profit                PASS (€29,612,000)                 │
│  ✅ XR-004: Top-up Tax                   PASS (€1,009,769)                  │
│  ✅ XR-005: Ownership Sum                PASS (All entities 100% owned)     │
│  ✅ XR-006: Entity Count                 PASS (7 entities, 3 jurisdictions) │
│                                                                             │
│  Overall: 6 PASS | 0 WARNING | 0 FAIL                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. User Interface Specifications

### 9.1 Main Layout Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIR-004: GIR Practice Form                                                 │
│  Practice completing GIR sections with integrated data point reference      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Load Case Study: [Case Study 1: GlobalTech ▼]  [ Load Data ]        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [ Section 1: General ]  [ Section 2: Structure ]  [ Section 3: GloBE ]    │
│  ════════════════════════════════════════════════════════════════════════  │
│                                                                             │
│  ┌────────────────────────────────────┐  ┌──────────────────────────────┐  │
│  │ SECTION 1: GENERAL INFORMATION     │  │ FIELD HELP                   │  │
│  │                                    │  │                              │  │
│  │ 1.1 MNE Group Identification       │  │ S1.1.2 - UPE Legal Name     │  │
│  │ ─────────────────────────────────  │  │                              │  │
│  │                                    │  │ The legal name of the       │  │
│  │ MNE Group Name:                    │  │ Ultimate Parent Entity as   │  │
│  │ [GlobalTech Manufacturing Group__] │  │ registered in its           │  │
│  │                                    │  │ jurisdiction.               │  │
│  │ UPE Legal Name: ← SELECTED         │  │                              │  │
│  │ [GlobalTech Manufacturing Ltd____] │  │ Type: Text (Max 200 chars)  │  │
│  │                                    │  │ Required: Yes               │  │
│  │ UPE Jurisdiction:                  │  │                              │  │
│  │ [United Kingdom ▼]                 │  │ ERP Source:                 │  │
│  │                                    │  │ • Legal entity master data  │  │
│  │ UPE Tax ID:                        │  │ • Company registration      │  │
│  │ [1234567890________________]       │  │                              │  │
│  │                                    │  │ Common Issues:              │  │
│  │ ─────────────────────────────────  │  │ ⚠️ Must match exactly with  │  │
│  │ 1.2 Reporting Period               │  │    tax registration         │  │
│  │ ...                                │  │                              │  │
│  └────────────────────────────────────┘  └──────────────────────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 🔍 Search Data Points: [________________] [All Sections ▼] [Search] │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ COMPLETION: Section 1: 85% | Section 2: 60% | Section 3: 45%       │   │
│  │ [ Validate All ]  [ Export JSON ]  [ Export PDF ]  [ Clear Form ]   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 9.2 Section 3 Jurisdiction View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SECTION 3: GloBE COMPUTATION                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Jurisdiction: [Ireland ▼]  (4 entities)    [ Add Jurisdiction ]           │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 3.2 GloBE INCOME CALCULATION                                         │   │
│  │                                                                      │   │
│  │ Financial Accounting Net Income:     € [28,000,000.00____]          │   │
│  │ Net Taxes Included in Income:        € [3,500,000.00_____]          │   │
│  │ Excluded Dividends:                  € [0.00______________]          │   │
│  │ Policy Disallowed Expenses:          € [(200,000.00)_____]          │   │
│  │ Stock Compensation Adjustment:       € [1,200,000.00_____]          │   │
│  │ Other Adjustments:                   € [300,000.00_______]          │   │
│  │                                      ─────────────────────           │   │
│  │ GloBE Income (Calculated):           € 32,800,000.00      ✅        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 3.5 TOP-UP TAX SUMMARY                                               │   │
│  │                                                                      │   │
│  │ GloBE Income:              € 32,800,000                              │   │
│  │ Adjusted Covered Taxes:    € 3,800,000                               │   │
│  │ Jurisdictional ETR:        11.59%                    🔴 LOW-TAXED   │   │
│  │ Top-up Tax %:              3.41%                                     │   │
│  │ SBIE:                      € 3,188,000                               │   │
│  │ Excess Profit:             € 29,612,000                              │   │
│  │ ════════════════════════════════════════════════════════════════    │   │
│  │ NET TOP-UP TAX:            € 1,009,769                               │   │
│  │ ════════════════════════════════════════════════════════════════    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 10. Case Study Pre-Load Feature

### 10.1 Available Case Studies

| ID | Name | Description | Entities | Jurisdictions |
|----|------|-------------|----------|---------------|
| CS1 | GlobalTech Manufacturing | Standard first filing | 7 | 3 |
| CS2 | Complex Ownership | POPEs, JVs, MOCEs | 120 | 15 |
| CS3 | Data Gap Challenges | Estimation scenarios | 45 | 12 |
| CS4 | Multi-QDMTT | Multiple QDMTT jurisdictions | 60 | 8 |
| CS5 | Amendment Required | Post-filing correction | 50 | 10 |

### 10.2 Pre-Load Behavior

When user selects a case study:
1. Prompt: "This will replace current form data. Continue?"
2. Load all sample data from case study
3. Mark fields as "pre-loaded" (different background color)
4. Run validation to show expected results
5. User can modify fields to practice variations

---

## 11. Test Cases

### 11.1 Case Study 1: GlobalTech - Complete Form Data

**Section 1 Input (General Information):**
| Field | Value |
|-------|-------|
| UPE Legal Name | GlobalTech Manufacturing Ltd |
| UPE Jurisdiction | United Kingdom |
| UPE Tax ID (UTR) | 1234567890 |
| Fiscal Year Start | 1 January 2024 |
| Fiscal Year End | 31 December 2024 |
| Accounting Standard | IFRS |
| Consolidated Revenue | €1,350,000,000 |
| Reporting Currency | EUR |
| DFE Name | GlobalTech Manufacturing Ltd |
| DFE Jurisdiction | United Kingdom |
| First Filing Year | Yes |

**Section 2 Input (Corporate Structure):**
| Entity Name | Jurisdiction | Entity Type | Ownership % | Tax ID |
|-------------|--------------|-------------|-------------|--------|
| GlobalTech Manufacturing Ltd | United Kingdom | UPE | 100% | GB1234567890 |
| GT IP Holdings Ltd | Ireland | CE | 100% | IE1234567A |
| GT Services Ireland Ltd | Ireland | CE | 100% | IE2345678B |
| GT Technology Ireland Ltd | Ireland | CE | 100% | IE3456789C |
| GT Sales Ireland Ltd | Ireland | CE | 100% | IE4567890D |
| GT Trading AG | Switzerland | CE | 100% | CHE-123.456.789 |
| GT Finance AG | Switzerland | CE | 100% | CHE-234.567.890 |

**Section 3 Input (Ireland - 4 entities):**
| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Number of CEs | 4 |
| Financial Accounting Net Income | €28,000,000 |
| Net Taxes Included in Income | €3,500,000 |
| Excluded Dividends | €0 |
| Policy Disallowed Expenses | (€200,000) |
| Stock-based Compensation Adjustment | €1,200,000 |
| Other Adjustments | €300,000 |
| **GloBE Income (calculated)** | **€32,800,000** |
| Current Tax Expense | €3,200,000 |
| Deferred Tax Expense | €800,000 |
| UTP Adjustment | (€150,000) |
| Non-Covered Tax Adjustment | (€50,000) |
| **Adjusted Covered Taxes (calculated)** | **€3,800,000** |
| Eligible Payroll | €19,000,000 |
| Tangible Assets NBV | €17,000,000 |

**Section 3 Input (Switzerland - 2 entities):**
| Field | Value |
|-------|-------|
| Jurisdiction | Switzerland |
| Number of CEs | 2 |
| Financial Accounting Net Income | €16,500,000 |
| GloBE Adjustments (net) | €1,500,000 |
| **GloBE Income (calculated)** | **€18,000,000** |
| Total Tax Expense | €2,700,000 |
| Tax Adjustments | (€180,000) |
| **Adjusted Covered Taxes (calculated)** | **€2,520,000** |
| Eligible Payroll | €8,500,000 |
| Tangible Assets NBV | €4,200,000 |

**Expected Validation Results (Ireland):**
| Check | Expected | Status |
|-------|----------|--------|
| ETR Calculation | 11.59% (€3.8M / €32.8M) | ✅ PASS |
| SBIE Total | €3,188,000 (€1,862,000 + €1,326,000) | ✅ PASS |
| Excess Profit | €29,612,000 (€32.8M - €3.188M) | ✅ PASS |
| Top-up Tax % | 3.41% (15% - 11.59%) | ✅ PASS |
| Top-up Tax | €1,009,769 | ✅ PASS |

**Expected Validation Results (Switzerland):**
| Check | Expected | Status |
|-------|----------|--------|
| ETR Calculation | 14.00% (€2.52M / €18M) | ✅ PASS |
| SBIE Total | €1,160,600 (€833,000 + €327,600) | ✅ PASS |
| Excess Profit | €16,839,400 (€18M - €1.16M) | ✅ PASS |
| Top-up Tax % | 1.00% (15% - 14%) | ✅ PASS |
| Top-up Tax | €168,394 | ✅ PASS |

### 11.2 Data Point Search Tests

| Search Query | Expected Results |
|--------------|------------------|
| "UPE name" | S1.1.2 - UPE Legal Name |
| "GloBE Income" | S3.2.8 - GloBE Income |
| "ETR" | S3.5.3 - Jurisdictional ETR |
| "payroll" | S3.4.1 - Eligible Payroll Costs, S3.4.3 - Payroll SBIE |

---

## 12. Export Options

### 12.1 Available Exports

| Format | Contents | Use Case |
|--------|----------|----------|
| PDF | Completed form with validation status | Print/review |
| JSON | Structured data for integration | System testing |
| Excel | Editable spreadsheet format | Further analysis |

### 12.2 Export Includes

- All entered field values
- Calculated field results
- Validation status summary
- Timestamp and session ID

---

## 13. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard Navigation | Tab through fields, arrow keys in dropdowns |
| Screen Reader | ARIA labels on all fields, help panel accessible |
| Color Contrast | 4.5:1 minimum |
| Focus Indicators | Visible focus ring on all interactive elements |
| Error Announcement | Validation errors announced to screen readers |

---

## 14. Technical Notes

### 14.1 Data Model

```typescript
interface GIRFormSession {
  id: string;
  caseStudyId: string | null;
  section1: GeneralInformation;
  section2: CorporateStructure[];
  section3: JurisdictionComputation[];
  validationResults: ValidationResult[];
  completionStatus: CompletionStatus;
  createdAt: Date;
  updatedAt: Date;
}

interface DataPointReference {
  id: string;
  fieldId: string;
  name: string;
  section: string;
  type: 'TEXT' | 'NUMERIC' | 'DATE' | 'CODE' | 'BOOLEAN';
  required: 'YES' | 'NO' | 'CONDITIONAL';
  format: string;
  description: string;
  erpMapping: string[];
  commonIssues: string[];
  relatedFields: string[];
  xmlElement: string;
}
```

### 14.2 Local Storage

- Form progress saved automatically every 30 seconds
- User can restore previous session on return
- Clear button removes all local data

---

## 15. Limitations & Scope

### 15.1 In Scope

- ✅ All three GIR sections with representative fields
- ✅ Integrated data point reference (searchable)
- ✅ Calculated fields with auto-computation
- ✅ Cross-reference validation
- ✅ Case study pre-load
- ✅ Export options (PDF, JSON, Excel)

### 15.2 Out of Scope

- ❌ Full ~480 data points (representative subset)
- ❌ XML generation (practice only)
- ❌ Connection to tax authority portals
- ❌ Multi-user collaboration
- ❌ Submission functionality

---

## 16. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-07 | — | Initial separate specs (GIR-006, GIR-008) |
| 2.0 | 2024-12-08 | — | Consolidated into GIR-004 with integrated reference |

---

## 17. Migration Notes

### 17.1 Relationship to Previous Tools

| Previous Tool | Status | Integration |
|---------------|--------|-------------|
| GIR-006 (Data Point Reference) | Merged | → Help panel + search feature |
| GIR-008 (GIR Practice Form) | Merged | → Main form functionality |

### 17.2 Feature Mapping

| Old GIR-006 Feature | New Location in GIR-004 |
|---------------------|-------------------------|
| Data point search | Bottom search bar |
| Section filter | Filter dropdown in search |
| Data point details | Contextual help panel (right side) |
| ERP mapping info | Help panel "ERP Source" section |
| Common issues | Help panel "Common Issues" section |

| Old GIR-008 Feature | New Location in GIR-004 |
|---------------------|-------------------------|
| Section tabs | Main navigation (unchanged) |
| Form fields | Left/center panel |
| Validation | Validation status panel |
| Case study pre-load | Top toolbar |
| Export | Bottom toolbar |

---

*End of GIR-004 GIR Practice Form Specification*
