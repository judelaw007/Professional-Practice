# GIR-006: Data Point Reference - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-006 |
| Tool Name | GIR Data Point Reference |
| Category | Pillar Two |
| Form Type | Reference |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 3.2 - GIR Data Requirements |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Provide a searchable reference of all GIR data points across Sections 1-3 of the GloBE Information Return. This tool helps learners look up specific field requirements, understand data sourcing from ERP systems, and identify common issues associated with each data element.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Navigate the GIR data structure across all three sections
- Identify required vs. optional data fields
- Understand the data type and format requirements for each field
- Map GIR data points to typical ERP/accounting system sources
- Recognize common data collection challenges and issues
- Efficiently locate specific fields when completing GIR forms

### 2.3 Prerequisites
Learners should understand:
- The overall structure of the GIR (Sections 1, 2, 3)
- Basic GloBE concepts (Constituent Entities, Jurisdictions, Top-up Tax)
- Common ERP/financial system terminology

### 2.4 GIR Structure Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIR DATA STRUCTURE                           │
└─────────────────────────────────────────────────────────────────┘

SECTION 1: General Information (~45 data points)
├── Group identification
├── Filing entity details
├── Reporting period information
├── Elections and notifications
└── Contact information

SECTION 2: Corporate Structure (~85 data points per entity)
├── Constituent Entity details
├── Ownership information
├── Entity classifications
├── Excluded Entity status
└── PE and JV information

SECTION 3: Computation of GloBE Liability (~350+ data points)
├── 3.1 Jurisdictional data
├── 3.2 GloBE Income/Loss
├── 3.3 Adjusted Covered Taxes
├── 3.4 SBIE calculations
├── 3.5 Top-up Tax calculations
├── 3.6 Safe Harbour elections
└── 3.7 Allocations and adjustments
```

---

## 3. Input Fields

### 3.1 Search Term

| Property | Value |
|----------|-------|
| Field ID | `search_term` |
| Label | Search |
| Data Type | String |
| Required | **No** (can browse without search) |
| Max Length | 100 characters |
| UI Element | Search input with magnifying glass icon |
| Placeholder Text | "Search data points (e.g., 'revenue', 'ETR', 'entity name')" |
| Help Text | "Enter keywords to find matching data points. Search covers field names, descriptions, and XML element names." |

**Search Behavior:**
- Case-insensitive matching
- Partial word matching (e.g., "rev" matches "Revenue")
- Multiple keywords treated as AND (all must match)
- Searches across: Field Name, Description, XML Element, Common Issues

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Max length | Length > 100 | "Search term cannot exceed 100 characters" |

---

### 3.2 Filter by Section

| Property | Value |
|----------|-------|
| Field ID | `section_filter` |
| Label | Section |
| Data Type | String (dropdown) |
| Required | **No** |
| Default Value | "All Sections" |
| UI Element | Dropdown select |
| Help Text | "Filter results to a specific GIR section" |

**Dropdown Options:**
| Value | Display Text | Description |
|-------|--------------|-------------|
| ALL | All Sections | Show all data points |
| S1 | Section 1: General Information | Group and filing entity details |
| S2 | Section 2: Corporate Structure | Entity-level information |
| S3 | Section 3: GloBE Computation | Calculations and liability |
| S3.1 | Section 3.1: Jurisdictional | Jurisdiction-level aggregates |
| S3.2 | Section 3.2: GloBE Income | Income calculations |
| S3.3 | Section 3.3: Covered Taxes | Tax calculations |
| S3.4 | Section 3.4: SBIE | Substance exclusion |
| S3.5 | Section 3.5: Top-up Tax | Top-up tax computation |

---

### 3.3 Filter by Data Type

| Property | Value |
|----------|-------|
| Field ID | `type_filter` |
| Label | Data Type |
| Data Type | String (dropdown) |
| Required | **No** |
| Default Value | "All Types" |
| UI Element | Dropdown select |
| Help Text | "Filter by the type of data required" |

**Dropdown Options:**
| Value | Display Text | Description |
|-------|--------------|-------------|
| ALL | All Types | Show all data types |
| TEXT | Text | Free text fields |
| NUMERIC | Numeric | Numbers and amounts |
| DATE | Date | Date fields |
| CODE | Code | Enumerated code values |
| BOOLEAN | Boolean | Yes/No fields |
| IDENTIFIER | Identifier | IDs and references |

---

### 3.4 Filter by Required Status

| Property | Value |
|----------|-------|
| Field ID | `required_filter` |
| Label | Required Status |
| Data Type | String (dropdown) |
| Required | **No** |
| Default Value | "All" |
| UI Element | Dropdown select |
| Help Text | "Filter by whether the field is mandatory or optional" |

**Dropdown Options:**
| Value | Display Text |
|-------|--------------|
| ALL | All Fields |
| REQUIRED | Required Only |
| OPTIONAL | Optional Only |
| CONDITIONAL | Conditional |

---

### 3.5 Results Per Page

| Property | Value |
|----------|-------|
| Field ID | `results_per_page` |
| Label | Show |
| Data Type | Integer |
| Required | **No** |
| Default Value | 25 |
| UI Element | Dropdown select |
| Options | 10, 25, 50, 100 |

---

## 4. Output Fields

### 4.1 Results Summary

| Property | Value |
|----------|-------|
| Field ID | `results_summary` |
| Label | Results |
| Data Type | String |
| Display Format | "Showing X-Y of Z data points" |
| UI Element | Text above results table |

---

### 4.2 Data Point Results Table

| Property | Value |
|----------|-------|
| Field ID | `results_table` |
| Label | Data Points |
| Data Type | Array of data point objects |
| UI Element | Sortable, paginated table |

**Table Columns:**
| Column | Field | Width | Sortable |
|--------|-------|-------|----------|
| Field ID | field_id | 100px | Yes |
| Field Name | field_name | 200px | Yes |
| Section | section | 80px | Yes |
| Data Type | data_type | 80px | Yes |
| Required | required | 80px | Yes |
| Description | description | Flex | No |

---

### 4.3 Data Point Detail Panel

When a user clicks on a data point row, expand to show full details:

| Property | Value |
|----------|-------|
| Field ID | `detail_panel` |
| Label | Field Details |
| Data Type | Object |
| UI Element | Expandable panel below row |

**Detail Panel Fields:**
| Field | Description |
|-------|-------------|
| Field ID | Unique identifier for the field |
| Field Name | Human-readable name |
| XML Element | Technical XML element name |
| Section | GIR section location |
| Data Type | Text, Numeric, Date, Code, etc. |
| Required | Required, Optional, or Conditional |
| Format | Expected format (e.g., ISO date, 2 decimal places) |
| Max Length | Maximum character/digit length |
| Valid Values | For code fields, list of valid options |
| Description | Full description of the field |
| Typical ERP Source | Common source system/module |
| Common Issues | Known data quality challenges |
| Related Fields | Links to related data points |
| Example | Sample value |

---

## 5. Data Model

### 5.1 Data Point Object Structure

```
DataPoint = {
    field_id: String,           // e.g., "S1.1.1"
    field_name: String,         // e.g., "MNE Group Name"
    xml_element: String,        // e.g., "MNEGroupName"
    section: String,            // e.g., "S1"
    subsection: String,         // e.g., "S1.1"
    data_type: Enum,            // TEXT | NUMERIC | DATE | CODE | BOOLEAN | IDENTIFIER
    required: Enum,             // REQUIRED | OPTIONAL | CONDITIONAL
    condition: String,          // Condition for CONDITIONAL fields
    format: String,             // Format specification
    max_length: Integer,        // Maximum length
    min_value: Number,          // For NUMERIC: minimum value
    max_value: Number,          // For NUMERIC: maximum value
    decimal_places: Integer,    // For NUMERIC: decimal precision
    valid_values: Array,        // For CODE: list of valid codes
    description: String,        // Full description
    erp_source: String,         // Typical ERP source
    common_issues: Array,       // Known issues
    related_fields: Array,      // Related field IDs
    example: String             // Example value
}
```

### 5.2 Sample Data Points

```
SAMPLE_DATA_POINTS = [
    // SECTION 1: General Information
    {
        field_id: "S1.1.1",
        field_name: "MNE Group Name",
        xml_element: "MNEGroupName",
        section: "S1",
        subsection: "S1.1",
        data_type: "TEXT",
        required: "REQUIRED",
        format: "Free text",
        max_length: 200,
        description: "The legal name of the MNE Group as used in consolidated financial statements",
        erp_source: "Group consolidation system / Legal entity master",
        common_issues: [
            "Inconsistent naming across subsidiaries",
            "Use of abbreviations vs full legal name",
            "Name changes during reporting period"
        ],
        related_fields: ["S1.1.2", "S1.1.3"],
        example: "GlobalTech Manufacturing Group plc"
    },
    {
        field_id: "S1.1.2",
        field_name: "UPE Jurisdiction",
        xml_element: "UPEJurisdiction",
        section: "S1",
        subsection: "S1.1",
        data_type: "CODE",
        required: "REQUIRED",
        format: "ISO 3166-1 alpha-2",
        max_length: 2,
        valid_values: ["GB", "US", "DE", "FR", "NL", "IE", "CH", "..."],
        description: "The jurisdiction where the Ultimate Parent Entity is located, using ISO country code",
        erp_source: "Legal entity master / Group structure database",
        common_issues: [
            "Confusion between incorporation and tax residence",
            "Dual-resident entities"
        ],
        related_fields: ["S1.1.1", "S2.1.3"],
        example: "GB"
    },
    {
        field_id: "S1.2.1",
        field_name: "Reporting Fiscal Year Start",
        xml_element: "FiscalYearStart",
        section: "S1",
        subsection: "S1.2",
        data_type: "DATE",
        required: "REQUIRED",
        format: "YYYY-MM-DD (ISO 8601)",
        description: "First day of the fiscal year for which the GIR is being filed",
        erp_source: "Financial calendar / Consolidation settings",
        common_issues: [
            "Short period years for new acquisitions",
            "Fiscal year changes during period"
        ],
        related_fields: ["S1.2.2"],
        example: "2024-01-01"
    },

    // SECTION 2: Corporate Structure
    {
        field_id: "S2.1.1",
        field_name: "Constituent Entity Name",
        xml_element: "CEName",
        section: "S2",
        subsection: "S2.1",
        data_type: "TEXT",
        required: "REQUIRED",
        format: "Free text",
        max_length: 200,
        description: "Legal name of the Constituent Entity",
        erp_source: "Legal entity master / Consolidation system",
        common_issues: [
            "Name variations across systems",
            "Historical name changes not updated",
            "Trading names vs legal names"
        ],
        related_fields: ["S2.1.2", "S2.1.3"],
        example: "GT Services Ireland Ltd"
    },
    {
        field_id: "S2.1.4",
        field_name: "Entity Tax Identification Number",
        xml_element: "CETIN",
        section: "S2",
        subsection: "S2.1",
        data_type: "IDENTIFIER",
        required: "CONDITIONAL",
        condition: "Required if entity has a TIN in its jurisdiction",
        format: "Jurisdiction-specific format",
        max_length: 50,
        description: "The tax identification number assigned to the entity by its tax jurisdiction",
        erp_source: "Tax master data / Legal entity register",
        common_issues: [
            "TIN format varies by jurisdiction",
            "Multiple TINs for different tax types",
            "Pending TIN applications"
        ],
        related_fields: ["S2.1.3"],
        example: "IE1234567T"
    },

    // SECTION 3: GloBE Computation
    {
        field_id: "S3.2.1",
        field_name: "GloBE Income",
        xml_element: "GloBEIncome",
        section: "S3",
        subsection: "S3.2",
        data_type: "NUMERIC",
        required: "REQUIRED",
        format: "Decimal with 2 places",
        decimal_places: 2,
        description: "The GloBE Income or Loss for the jurisdiction after all required adjustments per Article 3.1-3.5",
        erp_source: "GloBE calculation workbook / Tax provision system",
        common_issues: [
            "Timing differences with accounting income",
            "Intercompany elimination issues",
            "Currency translation adjustments"
        ],
        related_fields: ["S3.2.2", "S3.2.3", "S3.5.1"],
        example: "32800000.00"
    },
    {
        field_id: "S3.3.1",
        field_name: "Adjusted Covered Taxes",
        xml_element: "AdjustedCoveredTaxes",
        section: "S3",
        subsection: "S3.3",
        data_type: "NUMERIC",
        required: "REQUIRED",
        format: "Decimal with 2 places",
        decimal_places: 2,
        description: "Total Adjusted Covered Taxes for the jurisdiction after all adjustments per Article 4.1-4.6",
        erp_source: "Tax provision system / Tax return workpapers",
        common_issues: [
            "Deferred tax timing differences",
            "Non-covered tax identification",
            "UTP exclusions"
        ],
        related_fields: ["S3.3.2", "S3.3.3", "S3.5.1"],
        example: "3800000.00"
    },
    {
        field_id: "S3.4.1",
        field_name: "Eligible Payroll Costs",
        xml_element: "EligiblePayroll",
        section: "S3",
        subsection: "S3.4",
        data_type: "NUMERIC",
        required: "REQUIRED",
        format: "Decimal with 2 places",
        decimal_places: 2,
        description: "Total eligible employee compensation costs for the jurisdiction per Article 5.3.3",
        erp_source: "Payroll system / HR information system",
        common_issues: [
            "Contractor vs employee classification",
            "Capitalized payroll allocation",
            "Multi-jurisdiction employees"
        ],
        related_fields: ["S3.4.2", "S3.4.3"],
        example: "19000000.00"
    },
    {
        field_id: "S3.5.1",
        field_name: "Jurisdictional ETR",
        xml_element: "JurisdictionalETR",
        section: "S3",
        subsection: "S3.5",
        data_type: "NUMERIC",
        required: "REQUIRED",
        format: "Percentage with 4 decimal places",
        decimal_places: 4,
        min_value: 0,
        max_value: 100,
        description: "The Effective Tax Rate for the jurisdiction, calculated as Adjusted Covered Taxes / GloBE Income",
        erp_source: "GloBE calculation workbook",
        common_issues: [
            "Rounding differences",
            "Negative ETR scenarios",
            "ETR exceeding 100%"
        ],
        related_fields: ["S3.2.1", "S3.3.1", "S3.5.2"],
        example: "11.5854"
    },
    {
        field_id: "S3.5.3",
        field_name: "Top-up Tax Amount",
        xml_element: "TopUpTax",
        section: "S3",
        subsection: "S3.5",
        data_type: "NUMERIC",
        required: "REQUIRED",
        format: "Decimal with 2 places",
        decimal_places: 2,
        min_value: 0,
        description: "The calculated Top-up Tax for the jurisdiction",
        erp_source: "GloBE calculation workbook",
        common_issues: [
            "QDMTT offset calculation",
            "IIR vs UTPR allocation",
            "Minority interest adjustments"
        ],
        related_fields: ["S3.5.1", "S3.5.2", "S3.5.4"],
        example: "1009769.00"
    }
]
```

### 5.3 Data Point Count by Section

| Section | Description | Approximate Data Points |
|---------|-------------|------------------------|
| S1 | General Information | 45 |
| S2 | Corporate Structure | 85 (per entity × entities) |
| S3.1 | Jurisdictional Summary | 30 |
| S3.2 | GloBE Income | 65 |
| S3.3 | Covered Taxes | 55 |
| S3.4 | SBIE | 25 |
| S3.5 | Top-up Tax | 45 |
| S3.6 | Safe Harbour | 20 |
| S3.7 | Allocations | 35 |
| **Total** | | **~480** |

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  GIR Data Point Reference                                  [?]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ SEARCH & FILTER                                          │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  🔍 [Search data points...                    ] [Search] │   │
│  │                                                          │   │
│  │  Section: [All Sections     ▼]  Type: [All Types    ▼]  │   │
│  │  Required: [All Fields      ▼]  Show: [25           ▼]  │   │
│  │                                                          │   │
│  │  [Clear Filters]                                         │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ RESULTS                                                  │   │
│  │ Showing 1-25 of 156 data points matching "revenue"       │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │ ┌─────┬────────────────┬─────┬────────┬─────┬─────────┐ │   │
│  │ │ ID  │ Field Name     │Sect.│ Type   │Req. │ Desc... │ │   │
│  │ ├─────┼────────────────┼─────┼────────┼─────┼─────────┤ │   │
│  │ │S3.2.│Revenue -       │ S3  │NUMERIC │ REQ │ Total...│ │   │
│  │ │ 1   │Unrelated Party │     │        │     │         │ │   │
│  │ ├─────┴────────────────┴─────┴────────┴─────┴─────────┤ │   │
│  │ │ ▼ EXPANDED DETAIL VIEW                              │ │   │
│  │ │ ──────────────────────────────────────────────────── │ │   │
│  │ │ Field ID:      S3.2.1                               │ │   │
│  │ │ XML Element:   UnrelatedPartyRevenue                │ │   │
│  │ │ Data Type:     Numeric (2 decimal places)           │ │   │
│  │ │ Required:      Yes                                  │ │   │
│  │ │ Description:   Total revenue from transactions      │ │   │
│  │ │                with unrelated parties...            │ │   │
│  │ │                                                     │ │   │
│  │ │ Typical ERP Source:                                 │ │   │
│  │ │   GL Revenue accounts / Sales ledger                │ │   │
│  │ │                                                     │ │   │
│  │ │ Common Issues:                                      │ │   │
│  │ │   • Intercompany revenue misclassification          │ │   │
│  │ │   • Deferred revenue timing                         │ │   │
│  │ │   • Currency translation                            │ │   │
│  │ │                                                     │ │   │
│  │ │ Example: 156000000.00                               │ │   │
│  │ └─────────────────────────────────────────────────────┘ │   │
│  │                                                          │   │
│  │ │S3.2.│Revenue -       │ S3  │NUMERIC │ REQ │ Total...│ │   │
│  │ │ 2   │Related Party   │     │        │     │         │ │   │
│  │ │     │                │     │        │     │         │ │   │
│  │ │S3.2.│CbCR Revenue    │ S3  │NUMERIC │COND │ Revenue│ │   │
│  │ │ 10  │                │     │        │     │  from...│ │   │
│  │ └─────────────────────────────────────────────────────┘ │   │
│  │                                                          │   │
│  │  [← Previous]  Page 1 of 7  [Next →]                    │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Search Behavior

| Action | Result |
|--------|--------|
| Type in search box | Results filter in real-time (debounced 300ms) |
| Clear search | Show all results (with other filters applied) |
| No matches | Display "No data points found matching your search" |

### 6.3 Row Expansion

- Click row to expand/collapse detail panel
- Only one row expanded at a time (clicking new row closes previous)
- Expanded state indicated by arrow icon rotation

### 6.4 Responsive Behavior

| Viewport | Layout |
|----------|--------|
| Desktop (>992px) | Full table with all columns |
| Tablet (768-992px) | Hide Description column, show in detail only |
| Mobile (<768px) | Card layout instead of table |

---

## 7. User Flow

### 7.1 Search Flow

```
Step 1: User navigates to Data Point Reference
        → Page loads with all data points (first 25)
        → Search box and filters visible

Step 2: User enters search term
        → e.g., types "payroll"
        → Results filter in real-time as user types

Step 3: User optionally applies filters
        → Selects Section: S3.4 (SBIE)
        → Selects Required: Required Only

Step 4: User reviews results
        → Sees filtered list of matching data points
        → Can sort by clicking column headers

Step 5: User clicks on a data point row
        → Detail panel expands below row
        → Shows full field specification
        → Shows ERP source and common issues

Step 6: User navigates to related fields
        → Clicks on related field link
        → Page scrolls/navigates to that field
```

### 7.2 Browse Flow

```
Step 1: User wants to explore Section 2 fields
        → Selects Section filter: S2 - Corporate Structure

Step 2: System shows all Section 2 data points
        → Approximately 85 fields displayed

Step 3: User pages through results
        → Uses pagination controls
        → Or changes "Show" to 50 or 100 per page

Step 4: User finds field of interest
        → Expands to see full details
        → Notes ERP source for data collection
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Expected Behavior |
|----------|-------------------|
| Search returns no results | Display "No data points found. Try different keywords or clear filters." |
| Empty search with filters | Show all data points matching filters |
| Very long search term | Truncate display, search still functions |
| Special characters in search | Escape and treat as literal characters |
| Multiple spaces in search | Normalize to single space |

### 8.2 Error States

| Condition | Display |
|-----------|---------|
| Data load failure | "Unable to load data point reference. Please refresh the page." |
| Search timeout | "Search taking too long. Try a more specific term." |

---

## 9. Test Cases

### 9.1 Search Functional Test Cases

| Test ID | Description | Search Term | Filters | Expected Results |
|---------|-------------|-------------|---------|------------------|
| TC-001 | Basic search | "revenue" | None | All fields containing "revenue" |
| TC-002 | Section filter | "tax" | S3.3 | Only Covered Taxes section fields |
| TC-003 | Required filter | "" | Required | All required fields |
| TC-004 | Combined filters | "entity" | S2, TEXT | Text fields in Section 2 containing "entity" |
| TC-005 | No results | "xyzabc123" | None | "No data points found" message |
| TC-006 | Case insensitive | "GLOBE" | None | Same results as "globe" |

### 9.2 Data Integrity Test Cases

| Test ID | Description | Expected |
|---------|-------------|----------|
| DI-001 | All sections represented | S1, S2, S3 all have data points |
| DI-002 | Required fields have no condition | Required fields have condition = null |
| DI-003 | Code fields have valid values | All CODE type fields have valid_values array |
| DI-004 | Numeric fields have format | All NUMERIC fields have decimal_places |

### 9.3 UI Test Cases

| Test ID | Description | Action | Expected Result |
|---------|-------------|--------|-----------------|
| UI-001 | Row expansion | Click row | Detail panel expands |
| UI-002 | Row collapse | Click expanded row | Detail panel collapses |
| UI-003 | Pagination | Click "Next" | Shows next page of results |
| UI-004 | Sort by column | Click "Field Name" header | Results sorted alphabetically |
| UI-005 | Clear filters | Click "Clear Filters" | All filters reset to defaults |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | Tab through filters, Enter to search, Arrow keys in table |
| Screen reader | ARIA labels on all controls, table semantics |
| Color contrast | Minimum 4.5:1 for text |
| Focus indicator | Visible focus ring on all interactive elements |
| Expandable rows | Announced as expandable/expanded state |

---

## 11. Technical Notes

### 11.1 Data Source

The data point reference is pre-loaded from a static JSON file containing all ~480 data points. This file is generated from the official OECD GIR XML Schema documentation.

**Data File:** `gir_data_points.json`
**Size:** Approximately 150KB
**Update Frequency:** Updated with each OECD schema revision

### 11.2 Performance

- Initial load: < 500ms
- Search response: < 100ms (client-side filtering)
- No server requests after initial load

### 11.3 Browser Support

- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Validate actual GIR data
- Generate GIR XML
- Connect to ERP systems for data extraction
- Provide jurisdiction-specific field variations
- Include all possible schema extensions
- Update in real-time with schema changes
- Store user preferences or bookmarks
- Export data point lists

This tool is for **learning purposes only** to help understand GIR data requirements.

---

## 13. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-07 | Initial specification |

---

## 14. Appendix: Data Point Categories

### Section 1: General Information

| Subsection | Description | Key Fields |
|------------|-------------|------------|
| S1.1 | Group Identification | MNE name, UPE jurisdiction, LEI |
| S1.2 | Reporting Period | Fiscal year start/end, currency |
| S1.3 | Filing Entity | DFE details, election status |
| S1.4 | Elections | Safe harbour, SBIE elections |
| S1.5 | Contact | Filing contact details |

### Section 2: Corporate Structure

| Subsection | Description | Key Fields |
|------------|-------------|------------|
| S2.1 | Entity Details | Name, TIN, jurisdiction, address |
| S2.2 | Ownership | Parent entity, ownership %, type |
| S2.3 | Classification | CE type, excluded entity status |
| S2.4 | Special Entities | PE, JV, investment entity flags |

### Section 3: GloBE Computation

| Subsection | Description | Key Fields |
|------------|-------------|------------|
| S3.1 | Jurisdictional | Aggregate income, taxes by jurisdiction |
| S3.2 | GloBE Income | Income components, adjustments |
| S3.3 | Covered Taxes | Tax expense, adjustments, UTPs |
| S3.4 | SBIE | Payroll, tangible assets, carve-outs |
| S3.5 | Top-up Tax | ETR, top-up %, excess profit, tax |
| S3.6 | Safe Harbour | Test results, elections |
| S3.7 | Allocations | IIR allocation, minority interests |

---

## 15. Appendix: Common ERP Sources by Field Type

| Field Category | Typical ERP Source |
|----------------|-------------------|
| Entity Information | Legal Entity Master, SAP Org Structure |
| Revenue Data | GL Revenue Accounts, Sales Ledger |
| Tax Expense | Tax Provision System (Corptax, ONESOURCE) |
| Payroll Costs | Payroll System (ADP, Workday) |
| Fixed Assets | Asset Module, Property Register |
| Ownership | Consolidation System, Treasury |
| Intercompany | IC Reconciliation, Transfer Pricing |
