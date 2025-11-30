# Section 6.2: Excel-to-XML Conversion

## Introduction

Converting GIR data from the Excel-based Calculator to OECD-compliant XML format is a critical step in the filing process. The first GIR filings for calendar year 2024 are due by **June 30, 2026**, making XML generation capability essential for all in-scope MNE groups. This conversion must preserve data integrity, apply correct formatting standards, and produce a file that passes schema validation against the OECD GIR XML Schema (January 2025).

Whether using built-in Calculator functionality, commercial Pillar Two software, or custom tools, understanding the conversion process is essential for successful GIR submission. This section provides step-by-step guidance for converting Calculator data to XML, including mapping procedures, quality checks, and troubleshooting common conversion issues.

**Learning Objectives:**
- Execute Excel-to-XML conversion using multiple methods
- Apply the Calculator's XML export function with proper configuration
- Map Calculator fields to XML schema elements accurately
- Implement correct data formatting during conversion (percentages, dates, currencies)
- Apply proper character encoding (UTF-8) for international submissions
- Validate converted XML before submission
- Troubleshoot common conversion errors

---

## 6.2.1 Conversion Methods Overview

### Available Approaches

There are several methods for converting GIR Calculator data to XML:

```
Excel-to-XML Conversion Methods:
│
├── Method 1: Built-in Calculator Export
│   ├── Native XML generation button
│   ├── Pre-configured field mapping
│   ├── Automatic schema compliance
│   ├── Integrated validation
│   └── Recommended for most users
│
├── Method 2: Commercial Pillar Two Software
│   ├── Big 4 Solutions (PwC, Deloitte, EY, KPMG)
│   ├── CSC Corptax GMT
│   ├── Thomson Reuters ONESOURCE
│   ├── Wolters Kluwer CCH Integrator
│   ├── Tax-Model TaxSuite
│   └── Comprehensive multi-jurisdiction support
│
├── Method 3: General XML Tools
│   ├── Altova XMLSpy (commercial)
│   ├── Oxygen XML Editor (commercial)
│   ├── Microsoft XML Notepad (free)
│   ├── Visual Studio Code with XML extension (free)
│   └── Requires manual field mapping
│
├── Method 4: VBA-Based Export
│   ├── Custom macro development
│   ├── Direct XML DOM manipulation
│   ├── Tailored to Calculator structure
│   └── For organisations with specific requirements
│
└── Method 5: Tax Authority Portals
    ├── Online form entry (portal generates XML)
    ├── Jurisdiction-specific (limited availability)
    ├── UK HMRC digital portal
    ├── German ELSTER system
    └── Direct submission without local XML file
```

### Method Comparison Matrix

| Method | Complexity | Cost | Validation | Multi-Jurisdiction | Best For |
|--------|------------|------|------------|-------------------|----------|
| Calculator Export | Low | Included | Built-in | Manual per filing | Single jurisdiction filers |
| Big 4 Software | Low | High (licence + service) | Comprehensive | Automated | Large complex MNEs |
| CSC/Thomson/Wolters | Medium | High (licence) | Comprehensive | Automated | In-house tax teams |
| General XML Tools | High | Varies | Manual | Not supported | Technical specialists |
| VBA Export | High | Development time | Custom | Manual | Bespoke requirements |
| Tax Authority Portal | Low | Free | Automatic | N/A | Single jurisdiction only |

---

## 6.2.2 Commercial Pillar Two Software Solutions

### Big 4 Firm Solutions

As of 2025, all major accounting firms offer integrated Pillar Two compliance platforms with XML generation capabilities:

#### PwC Pillar Two Engine

```
PwC Pillar Two Engine Capabilities:
│
├── Core Features
│   ├── Produces GIR and QDMTT tax returns in XML format
│   ├── Identifies reporting discrepancies between GIR and QDMTT rules
│   ├── Incorporates GloBE Rules and country-specific localisation
│   └── Multi-jurisdiction filing support
│
├── XML Generation
│   ├── Direct XML output to OECD schema
│   ├── Built-in schema validation
│   ├── Country-specific format variants
│   └── Audit trail and version control
│
└── Delivery Model
    ├── Managed service (PwC-operated)
    ├── Co-sourcing (shared responsibility)
    └── Technology licence (client-operated)
```

#### Deloitte Pillar Two Agent

```
Deloitte Pillar Two Agent Capabilities:
│
├── Core Features
│   ├── Data collection and centralisation
│   ├── Top-up tax calculation
│   ├── GIR and QDMTT filing support
│   └── Workflow management
│
├── XML Generation
│   ├── Automated XML file creation
│   ├── Multi-format export
│   ├── Pre-filing validation
│   └── Status tracking
│
└── Delivery Model
    ├── Co-sourcing engagement
    ├── Outsourcing engagement
    └── Dedicated Deloitte tax team support
```

#### EY GloBE Technology Suite / GloBE Engine

```
EY GloBE Technology Suite Capabilities:
│
├── Core Features
│   ├── Web-based data ingestion
│   ├── Multiyear analysis support
│   ├── System-agnostic (handles various data formats)
│   ├── API connectivity to organisation systems
│   └── Provision and compliance support
│
├── XML Generation
│   ├── GloBE Information Return generation
│   ├── Local filing data points
│   ├── Schema-compliant output
│   └── Maintained by international tax professionals
│
└── Delivery Model
    ├── SaaS agreement (software licence)
    ├── Co-sourcing service
    └── Integrated Pillar Two journey support
```

#### KPMG BEPS 2.0 Automation Technology (KBAT)

```
KPMG KBAT Capabilities:
│
├── Core Features
│   ├── Integrated with KPMG Digital Gateway platform
│   ├── Data collection through to GIR production
│   ├── High-level and detailed modelling
│   ├── Safe harbour calculations
│   └── Scalable and transparent
│
├── XML Generation
│   ├── GIR XML production
│   ├── Local reporting packages
│   ├── Multi-jurisdiction support
│   └── Integrated validation
│
└── Delivery Model
    ├── KPMG Digital Gateway platform access
    ├── Modelling suite integration
    └── Advisory support available
```

### Specialist Tax Technology Vendors

| Vendor | Product | Key Features |
|--------|---------|--------------|
| CSC Corptax | GMT (Global Minimum Tax) | 60+ jurisdiction tracking, embedded XML generation, pre-filing validation, top-up tax estimation |
| Thomson Reuters | ONESOURCE Pillar Two | Global data management, automated calculations, multi-format filing |
| Wolters Kluwer | CCH Integrator | Workflow automation, multi-jurisdiction, integration with tax provision |
| Longview | Tax Platform | Data aggregation, calculation engine, reporting module |

---

## 6.2.3 Built-in Calculator XML Export

### Overview

The GIR Completion Calculator includes a built-in XML export function that automates the conversion process and is suitable for most single-jurisdiction filing requirements.

**Tab:** `XML Export`

### Pre-Export Checklist

Before generating XML, complete these mandatory checks:

| # | Check Item | Status | Action if Failed |
|---|------------|--------|------------------|
| 1 | All Level 1-4 validation checks passed | ☐ | Resolve errors per Section 5.5 |
| 2 | Reconciliations completed and balanced | ☐ | Complete reconciliation tabs |
| 3 | Sign-off obtained from reviewer | ☐ | Obtain required approvals |
| 4 | Correct fiscal year selected | ☐ | Verify FY start/end dates |
| 5 | Functional currency consistent | ☐ | Verify all amounts in correct currency |
| 6 | Entity data complete (TINs, addresses) | ☐ | Complete Section 1 data |
| 7 | Safe harbour elections documented | ☐ | Verify Section 2 entries |
| 8 | Top-up tax calculations reconciled | ☐ | Verify Section 3 totals |

### Step-by-Step Export Process

#### Step 1: Navigate to XML Export Tab

Open the `XML Export` tab in your GIR Completion Calculator.

```
Calculator Navigation:
├── Home Tab
├── Section 1 - MNE Information
├── Section 2 - Safe Harbours
├── Section 3 - GloBE Computations
├── Validation Summary
├── Reconciliation
└── XML Export  ←── Navigate here
```

#### Step 2: Configure Export Settings

Complete all configuration fields:

| Setting | Description | Example | Notes |
|---------|-------------|---------|-------|
| Output File Name | Name for XML file | GlobalCo_GIR_FY2024.xml | Alphanumeric, no spaces |
| Output Location | Folder path | C:\GIR_Files\2024\ | Must have write access |
| Schema Version | OECD schema version | 1.0 | January 2025 schema |
| Message Reference ID | Unique identifier | GB2024GIR000001ABC | Max 200 characters |
| Sending Authority | Filing jurisdiction | GB | ISO 3166-1 alpha-2 |
| Receiving Authority | Exchange recipient | Leave blank | Domestic filing only |
| Encoding | Character encoding | UTF-8 | Required for OECD schema |
| Include BOM | Byte Order Mark | No | Not recommended |

#### Step 3: Verify Field Mapping

The Calculator displays a mapping summary showing all fields to be exported:

```
Field Mapping Preview:
┌─────────────────────────────────────────────────────────────────────┐
│ Calculator Field              │ XML Element               │ Status  │
├─────────────────────────────────────────────────────────────────────┤
│ FCE_Name (Section1!B5)        │ FilingConstituentEntity   │ ✓ Ready │
│                               │   /Name                   │         │
│ FCE_TIN (Section1!C5)         │ FilingConstituentEntity   │ ✓ Ready │
│                               │   /TIN                    │         │
│ FCE_Jurisdiction (Section1!D5)│ FilingConstituentEntity   │ ✓ Ready │
│                               │   /ResCountryCode         │         │
│ GloBE_Income (S3.1!AK22)      │ ETRComputation            │ ✓ Ready │
│                               │   /GloBEIncome            │         │
│ Covered_Taxes (S3.1!X20)      │ ETRComputation            │ ✓ Ready │
│                               │   /AdjustedCoveredTaxes   │         │
│ ETR (S3.1!E5)                 │ ETRComputation/ETR        │ ✓ Ready │
│ [477 additional fields...]                                          │
├─────────────────────────────────────────────────────────────────────┤
│ TOTAL FIELDS: 483             │ READY: 483  │ WARNINGS: 0 │ ERRORS: 0│
└─────────────────────────────────────────────────────────────────────┘
```

**Status Indicators:**
- ✓ Ready: Field mapped and validated
- ⚠ Warning: Optional field empty or potential issue
- ✗ Error: Required field missing or invalid format

#### Step 4: Generate XML

Click the **[Generate XML]** button.

The Calculator will execute the following sequence:

```
XML Generation Sequence:
│
├── Phase 1: Data Extraction (2-5 seconds)
│   ├── Extract Section 1 data (52 fields)
│   ├── Extract Section 2 data (40 fields per jurisdiction)
│   ├── Extract Section 3 data (385 fields per jurisdiction)
│   └── Extract Corporate Structure data (variable)
│
├── Phase 2: Data Transformation (1-3 seconds)
│   ├── Convert percentages to decimals (0-1)
│   ├── Format dates to ISO 8601
│   ├── Apply monetary formatting (2 decimals)
│   ├── Encode special characters (UTF-8)
│   └── Validate country/currency codes
│
├── Phase 3: XML Construction (1-2 seconds)
│   ├── Create XML declaration and namespaces
│   ├── Build MessageHeader
│   ├── Build GIRBody structure
│   ├── Populate all elements
│   └── Close all tags
│
├── Phase 4: Validation (2-5 seconds)
│   ├── Well-formedness check
│   ├── Schema validation
│   ├── Namespace verification
│   └── Element completeness check
│
└── Phase 5: Output (1 second)
    ├── Save to specified location
    ├── Generate log file
    └── Display completion message
```

#### Step 5: Review Generation Log

```
XML Generation Log - GlobalCo_GIR_FY2024.xml
══════════════════════════════════════════════════════════════════════
Start Time: 2025-06-15 14:30:00 UTC
Schema Version: GIR v1.0 (January 2025)
──────────────────────────────────────────────────────────────────────
14:30:00.100 - Initialising XML generation...
14:30:00.250 - Extracting Section 1 data: 52 fields extracted
14:30:00.500 - Extracting Section 2 data: 3 jurisdictions, 120 fields
14:30:01.200 - Extracting Section 3 data: 3 jurisdictions, 1,155 fields
14:30:02.000 - Extracting Corporate Structure: 45 entities
14:30:02.500 - Applying data transformations...
14:30:03.000 - Building XML structure...
14:30:04.000 - Validating against OECD schema...
14:30:04.500 - Schema validation: PASSED
14:30:04.600 - Saving file: C:\GIR_Files\2024\GlobalCo_GIR_FY2024.xml
14:30:04.700 - File size: 847 KB
──────────────────────────────────────────────────────────────────────
GENERATION COMPLETE
Status: SUCCESS
Errors: 0
Warnings: 0
Duration: 4.7 seconds
──────────────────────────────────────────────────────────────────────
```

---

## 6.2.4 Data Transformation Rules

### Critical: Percentage Conversion

Calculator percentages must be converted to decimal format (0 to 1):

```
Percentage Transformation Rule:
│
├── OECD Schema Requirement
│   ├── Percentages represented as decimals
│   ├── Range: 0.0000 to 1.0000
│   ├── Maximum 4 decimal places
│   └── 0 = 0%, 1 = 100%
│
├── Calculator Handling
│   ├── Cells formatted as percentage → Stored as decimal (0.25 = 25%)
│   ├── Cells as whole numbers → Must divide by 100
│   └── Export function handles automatically
│
└── Transformation Examples
    ├── ETR 29.60% → 0.2960
    ├── Top-up Tax % 5.40% → 0.0540
    ├── Ownership 100% → 1.0000
    ├── Minority 23.5% → 0.2350
    └── SBIE rate 9.8% → 0.0980
```

**Transformation Function (VBA):**

```vba
Function ToXMLPercentage(cellValue As Variant) As String
    Dim decValue As Double

    If IsNumeric(cellValue) Then
        If cellValue > 1 Then
            ' Stored as whole number (e.g., 25 for 25%)
            decValue = cellValue / 100
        Else
            ' Already decimal (e.g., 0.25 for 25%)
            decValue = cellValue
        End If
        ToXMLPercentage = Format(decValue, "0.0000")
    Else
        ToXMLPercentage = "0.0000"
    End If
End Function
```

### Monetary Amount Formatting

```
Monetary Transformation Rule:
│
├── OECD Schema Requirement
│   ├── Decimal with exactly 2 decimal places
│   ├── No thousand separators (no commas)
│   ├── Period (.) as decimal separator
│   ├── Currency code attribute required
│   └── Negative values permitted (prefix with -)
│
├── Calculator Storage
│   ├── Internal: 43500000 (numeric)
│   ├── Display: €43,500,000.00
│   └── Export function strips formatting
│
└── Transformation Example
    Input:  €43,500,000.00 (display)
    Output: <globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

**Transformation Function (VBA):**

```vba
Sub AddMonetaryElement(xmlDoc As MSXML2.DOMDocument60, _
                       parent As MSXML2.IXMLDOMElement, _
                       elementName As String, _
                       amount As Double, _
                       currencyCode As String)

    Dim newElement As MSXML2.IXMLDOMElement
    Set newElement = xmlDoc.createElementNS("urn:oecd:ties:gir:v1", elementName)
    newElement.setAttribute "currencyCode", currencyCode

    ' Format with exactly 2 decimal places, no separators
    newElement.Text = Format(amount, "0.00")
    parent.appendChild newElement

End Sub
```

### Date Formatting

```
Date Transformation Rule:
│
├── OECD Schema Requirement
│   ├── ISO 8601 format: YYYY-MM-DD
│   ├── No time component for dates
│   ├── Leading zeros required (01, not 1)
│   └── Hyphen (-) separator only
│
├── Calculator Storage
│   ├── Excel serial date (e.g., 45657 = 31/12/2024)
│   ├── Display varies by locale (DD/MM/YYYY or MM/DD/YYYY)
│   └── Export function standardises format
│
└── Transformation Examples
    ├── 31/12/2024 → 2024-12-31
    ├── 01/01/2024 → 2024-01-01
    ├── 30/06/2026 → 2026-06-30
    └── Excel 45657 → 2024-12-31
```

**Transformation Function (VBA):**

```vba
Function ToXMLDate(dateValue As Variant) As String
    If IsDate(dateValue) Then
        ToXMLDate = Format(dateValue, "yyyy-mm-dd")
    Else
        ToXMLDate = ""
    End If
End Function
```

### DateTime Formatting (Timestamp)

```
DateTime Transformation Rule:
│
├── OECD Schema Requirement
│   ├── ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
│   ├── T separator between date and time
│   ├── Z suffix indicates UTC timezone
│   ├── 24-hour time format
│   └── Seconds required
│
└── Transformation Example
    Current time: 2:30:45 PM on 15 June 2025
    Output: 2025-06-15T14:30:45Z
```

**Transformation Function (VBA):**

```vba
Function ToXMLTimestamp() As String
    ' Returns current UTC timestamp
    ToXMLTimestamp = Format(Now, "yyyy-mm-dd") & "T" & _
                     Format(Now, "hh:mm:ss") & "Z"
End Function
```

### Country Code Standardisation

```
Country Code Transformation Rule:
│
├── OECD Schema Requirement
│   ├── ISO 3166-1 alpha-2 codes only
│   ├── Always uppercase
│   ├── Exactly 2 characters
│   └── Must be valid country code
│
├── Common Corrections
│   ├── "United Kingdom" → GB
│   ├── "UK" → GB
│   ├── "Germany" → DE
│   ├── "GER" → DE
│   ├── "USA" → US
│   └── "Switzerland" → CH
│
└── Calculator Handling
    ├── Lookup table converts names/variants
    ├── Validation rejects invalid codes
    └── Warning for unusual codes
```

### TIN Handling

```
TIN Transformation Rule:
│
├── OECD Schema Requirement
│   ├── TIN value as element content
│   ├── issuedBy attribute required (ISO country code)
│   ├── Maximum 200 characters
│   └── "NOTIN" if no TIN exists
│
├── Special Cases
│   ├── No TIN issued → <globe:TIN issuedBy="GB">NOTIN</globe:TIN>
│   ├── Remove spaces → "12 34 56 78" becomes "12345678"
│   ├── Preserve hyphens → "12-345-678" stays as entered
│   └── Stateless entity → Use creation jurisdiction
│
└── Transformation Example
    Input: TIN "12345678", Jurisdiction "GB"
    Output: <globe:TIN issuedBy="GB">12345678</globe:TIN>
```

---

## 6.2.5 Character Encoding Requirements

### UTF-8 Encoding Requirement

The OECD GIR XML Schema requires UTF-8 encoding. This is critical for international submissions containing non-ASCII characters.

```
UTF-8 Encoding Requirements:
│
├── XML Declaration
│   └── <?xml version="1.0" encoding="UTF-8"?>
│
├── Why UTF-8?
│   ├── Supports all international characters
│   ├── Compatible with all OECD member systems
│   ├── Handles currency symbols (€, £, ¥, ₹)
│   ├── Supports accented characters (é, ü, ñ, ø)
│   └── Required by OECD validation rules
│
├── Common Issues
│   ├── Excel default may be ANSI/Windows-1252
│   ├── Copy/paste can introduce encoding errors
│   ├── Some VBA functions default to ASCII
│   └── BOM (Byte Order Mark) may cause issues
│
└── Best Practices
    ├── Ensure Calculator saves in UTF-8
    ├── Verify encoding attribute in XML declaration
    ├── Test with international characters before submission
    └── Do not include BOM (Byte Order Mark)
```

### Special Character Encoding

XML requires certain characters to be encoded as entities:

| Character | Name | Encoded As | Example |
|-----------|------|------------|---------|
| & | Ampersand | `&amp;` | "A & B" → "A &amp; B" |
| < | Less than | `&lt;` | "x < y" → "x &lt; y" |
| > | Greater than | `&gt;` | "x > y" → "x &gt; y" |
| " | Double quote | `&quot;` | 'Say "Hello"' → 'Say &quot;Hello&quot;' |
| ' | Single quote | `&apos;` | "It's" → "It&apos;s" |

**Example Transformation:**

```xml
<!-- Entity name with special characters -->

<!-- INCORRECT - Will cause parsing error -->
<globe:Name>GlobalCo Holdings & Partners</globe:Name>

<!-- CORRECT - Ampersand encoded -->
<globe:Name>GlobalCo Holdings &amp; Partners</globe:Name>
```

**VBA Encoding Function:**

```vba
Function EncodeXMLString(inputText As String) As String
    Dim result As String
    result = inputText

    ' Order matters - ampersand must be first
    result = Replace(result, "&", "&amp;")
    result = Replace(result, "<", "&lt;")
    result = Replace(result, ">", "&gt;")
    result = Replace(result, """", "&quot;")
    result = Replace(result, "'", "&apos;")

    EncodeXMLString = result
End Function
```

---

## 6.2.6 File Naming Conventions

### Recommended Naming Structure

Consistent file naming ensures easy identification and version tracking:

```
File Naming Convention:
│
├── Recommended Format
│   └── [GroupName]_GIR_[FiscalYear]_[Version]_[Date].xml
│
├── Components
│   ├── GroupName: MNE group identifier (no spaces)
│   ├── GIR: Fixed identifier for GloBE Information Return
│   ├── FiscalYear: FY end year (e.g., FY2024)
│   ├── Version: Version number (v1, v2, FINAL)
│   └── Date: Generation date YYYYMMDD
│
└── Examples
    ├── GlobalCo_GIR_FY2024_v1_20250615.xml
    ├── GlobalCo_GIR_FY2024_v2_20250620.xml
    ├── GlobalCo_GIR_FY2024_FINAL_20250625.xml
    └── GlobalCo_GIR_FY2024_AMENDMENT1_20250815.xml
```

### Characters to Avoid

| Character | Issue | Alternative |
|-----------|-------|-------------|
| Space | May cause path issues | Use underscore (_) |
| & | XML entity conflict | Use "and" |
| < > | XML tag characters | Omit |
| : | Windows path separator | Use hyphen (-) |
| / \ | Path separators | Use hyphen (-) |
| * ? | Wildcards | Omit |
| " | Quote character | Omit |

### Jurisdiction-Specific Requirements

Some jurisdictions mandate specific naming conventions:

| Jurisdiction | Required Format | Example |
|--------------|-----------------|---------|
| UK (HMRC) | To be confirmed | Pending portal launch |
| Germany | To be confirmed | Pending ELSTER update |
| France | To be confirmed | Pending DGFiP guidance |
| Netherlands | To be confirmed | Pending portal update |

*Note: Check jurisdiction-specific guidance as portals become available in 2025-2026.*

---

## 6.2.7 Field Mapping Reference

### Section 1: MNE Group Information

| Calculator Location | Calculator Field | XML Path | Data Type |
|--------------------|------------------|----------|-----------|
| Section1!B5 | FCE_Name | /FilingInfo/FilingConstituentEntity/Name | String (1-200) |
| Section1!C5 | FCE_TIN | /FilingInfo/FilingConstituentEntity/TIN | TIN_Type |
| Section1!D5 | FCE_Jurisdiction | /FilingInfo/FilingConstituentEntity/ResCountryCode | ISO 3166-1 |
| Section1!E5 | FCE_Address | /FilingInfo/FilingConstituentEntity/Address/AddressFree | String |
| Section1!F5 | Filing_Role | /FilingInfo/FilingConstituentEntity/FilingRole | Enum |
| Section1!F10 | UPE_Name | /CorporateStructure/UPE/Name | String (1-200) |
| Section1!G10 | UPE_TIN | /CorporateStructure/UPE/TIN | TIN_Type |
| Section1!H10 | UPE_Jurisdiction | /CorporateStructure/UPE/ResCountryCode | ISO 3166-1 |
| Section1!I10 | Accounting_Standard | /FilingInfo/AccountingInfo/AccountingStandard | Enum |
| Section1!J10 | Functional_Currency | /FilingInfo/AccountingInfo/FunctionalCurrency | ISO 4217 |
| Section1!K5 | FY_Start | /FilingInfo/ReportingFiscalYear/StartDate | Date |
| Section1!L5 | FY_End | /FilingInfo/ReportingFiscalYear/EndDate | Date |

### Section 2: Safe Harbours and Exclusions

| Calculator Location | Calculator Field | XML Path | Data Type |
|--------------------|------------------|----------|-----------|
| Section2!B5 | Jurisdiction | /JurisdictionSection/JurisdictionCode | ISO 3166-1 |
| Section2!S5 | TransitionalSH_Elected | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH/Elected | Boolean |
| Section2!T5 | Qualifying_Test | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH/QualifyingTest | Enum |
| Section2!N5 | SimplifiedETR | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH/TestValue | Percentage |
| Section2!N50 | QDMTTSH_Elected | /JurisdictionSection/SafeHarbours/QDMTTSH/Elected | Boolean |
| Section2!O50 | QDMTT_Amount | /JurisdictionSection/SafeHarbours/QDMTTSH/Amount | Monetary |

### Section 3: GloBE Computations

| Calculator Location | Calculator Field | XML Path | Data Type |
|--------------------|------------------|----------|-----------|
| S3.1!AK22 | Net_GloBE_Income | /JurisdictionSection/GloBEComputations/ETRComputation/GloBEIncome | Monetary |
| S3.1!X20 | Adjusted_Covered_Taxes | /JurisdictionSection/GloBEComputations/ETRComputation/AdjustedCoveredTaxes | Monetary |
| S3.1!E5 | Jurisdictional_ETR | /JurisdictionSection/GloBEComputations/ETRComputation/JurisdictionalETR | Percentage |
| S3.2!R20 | Payroll_Carveout | /JurisdictionSection/GloBEComputations/SBIEComputation/PayrollCarveOut | Monetary |
| S3.2!AE20 | Asset_Carveout | /JurisdictionSection/GloBEComputations/SBIEComputation/TangibleAssetCarveOut | Monetary |
| S3.2!I5 | Total_SBIE | /JurisdictionSection/GloBEComputations/SBIEComputation/TotalSBIE | Monetary |
| S3.3!H5 | Excess_Profit | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/ExcessProfit | Monetary |
| S3.3!E5 | TopUp_Percentage | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/TopUpTaxPercentage | Percentage |
| S3.3!Q5 | QDMTT_Offset | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/QDMTTOffset | Monetary |
| S3.3!R5 | Final_TopUp_Tax | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/FinalTopUpTax | Monetary |
| S3.4!E5 | IIR_Allocation | /JurisdictionSection/TopUpTaxAllocation/IIRAllocation/AllocatedAmount | Monetary |
| S3.4!F5 | UTPR_Allocation | /JurisdictionSection/TopUpTaxAllocation/UTPRAllocation/AllocatedAmount | Monetary |

---

## 6.2.8 VBA-Based XML Generation

### Overview

For organisations requiring customised XML generation, VBA (Visual Basic for Applications) provides direct control over the conversion process.

### Complete VBA Export Module

```vba
' ═══════════════════════════════════════════════════════════════════════
' GIR XML Export Module
' Version: 1.0 (Compatible with OECD GIR Schema v1.0, January 2025)
' Requires: Microsoft XML, v6.0 reference
' ═══════════════════════════════════════════════════════════════════════

Option Explicit

' Namespace constants
Private Const NS_GLOBE As String = "urn:oecd:ties:gir:v1"
Private Const NS_STF As String = "urn:oecd:ties:gircommontypes:v1"

Public Sub ExportGIRToXML()

    On Error GoTo ErrorHandler

    Dim xmlDoc As MSXML2.DOMDocument60
    Dim rootElement As MSXML2.IXMLDOMElement
    Dim outputPath As String
    Dim startTime As Double

    startTime = Timer

    ' Initialize XML Document
    Set xmlDoc = New MSXML2.DOMDocument60
    xmlDoc.async = False
    xmlDoc.preserveWhiteSpace = False

    ' Add XML Declaration with UTF-8 encoding
    Dim xmlDecl As MSXML2.IXMLDOMProcessingInstruction
    Set xmlDecl = xmlDoc.createProcessingInstruction("xml", _
        "version=""1.0"" encoding=""UTF-8""")
    xmlDoc.appendChild xmlDecl

    ' Create Root Element with Namespaces
    Set rootElement = xmlDoc.createElementNS(NS_GLOBE, "globe:GIR_OECD")
    rootElement.setAttribute "xmlns:stf", NS_STF
    rootElement.setAttribute "xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance"
    rootElement.setAttribute "version", "1.0"
    xmlDoc.appendChild rootElement

    ' Build XML Structure
    Application.StatusBar = "Building MessageHeader..."
    Call BuildMessageHeader(xmlDoc, rootElement)

    Application.StatusBar = "Building GIRBody..."
    Call BuildGIRBody(xmlDoc, rootElement)

    ' Get output path
    outputPath = GetOutputPath()
    If outputPath = "" Then Exit Sub

    ' Save File
    Application.StatusBar = "Saving XML file..."
    xmlDoc.Save outputPath

    ' Success message
    Dim duration As Double
    duration = Round(Timer - startTime, 2)

    Application.StatusBar = ""
    MsgBox "XML exported successfully!" & vbCrLf & vbCrLf & _
           "File: " & outputPath & vbCrLf & _
           "Duration: " & duration & " seconds", _
           vbInformation, "GIR XML Export"

    Exit Sub

ErrorHandler:
    Application.StatusBar = ""
    MsgBox "Error during XML export: " & Err.Description, _
           vbCritical, "Export Error"

End Sub

Private Sub BuildMessageHeader(xmlDoc As MSXML2.DOMDocument60, _
                               parent As MSXML2.IXMLDOMElement)

    Dim header As MSXML2.IXMLDOMElement
    Set header = xmlDoc.createElementNS(NS_GLOBE, "globe:MessageHeader")

    ' Sending Competent Authority (ISO country code)
    AddElement xmlDoc, header, "globe:SendingCompetentAuthority", _
        UCase(Trim(Sheets("Section1").Range("D5").Value))

    ' Message Type (fixed)
    AddElement xmlDoc, header, "globe:MessageType", "GIR"

    ' Message Reference ID (unique)
    AddElement xmlDoc, header, "globe:MessageRefId", _
        Trim(Sheets("XMLExport").Range("B5").Value)

    ' Message Type Indicator (fixed)
    AddElement xmlDoc, header, "globe:MessageTypeIndic", "GIR"

    ' Reporting Period (fiscal year end date)
    AddElement xmlDoc, header, "globe:ReportingPeriod", _
        ToXMLDate(Sheets("Section1").Range("L5").Value)

    ' Timestamp (current UTC)
    AddElement xmlDoc, header, "globe:Timestamp", ToXMLTimestamp()

    parent.appendChild header

End Sub

Private Sub BuildGIRBody(xmlDoc As MSXML2.DOMDocument60, _
                         parent As MSXML2.IXMLDOMElement)

    Dim body As MSXML2.IXMLDOMElement
    Set body = xmlDoc.createElementNS(NS_GLOBE, "globe:GIRBody")

    ' FilingInfo
    Call BuildFilingInfo(xmlDoc, body)

    ' JurisdictionSections (loop through each jurisdiction)
    Call BuildJurisdictionSections(xmlDoc, body)

    ' CorporateStructure
    Call BuildCorporateStructure(xmlDoc, body)

    parent.appendChild body

End Sub

Private Sub BuildFilingInfo(xmlDoc As MSXML2.DOMDocument60, _
                            parent As MSXML2.IXMLDOMElement)

    Dim filingInfo As MSXML2.IXMLDOMElement
    Set filingInfo = xmlDoc.createElementNS(NS_GLOBE, "globe:FilingInfo")

    ' FilingConstituentEntity
    Dim fce As MSXML2.IXMLDOMElement
    Set fce = xmlDoc.createElementNS(NS_GLOBE, "globe:FilingConstituentEntity")

    AddElement xmlDoc, fce, "globe:Name", _
        EncodeXMLString(Sheets("Section1").Range("B5").Value)
    AddTINElement xmlDoc, fce, _
        Sheets("Section1").Range("C5").Value, _
        Sheets("Section1").Range("D5").Value
    AddElement xmlDoc, fce, "globe:ResCountryCode", _
        UCase(Sheets("Section1").Range("D5").Value)

    ' Address
    Dim addr As MSXML2.IXMLDOMElement
    Set addr = xmlDoc.createElementNS(NS_GLOBE, "globe:Address")
    AddElement xmlDoc, addr, "globe:AddressFree", _
        EncodeXMLString(Sheets("Section1").Range("E5").Value)
    fce.appendChild addr

    AddElement xmlDoc, fce, "globe:FilingRole", _
        Sheets("Section1").Range("F5").Value

    filingInfo.appendChild fce

    ' MNEGroup
    Dim mneGroup As MSXML2.IXMLDOMElement
    Set mneGroup = xmlDoc.createElementNS(NS_GLOBE, "globe:MNEGroup")
    AddElement xmlDoc, mneGroup, "globe:Name", _
        EncodeXMLString(Sheets("Section1").Range("F10").Value)
    AddElement xmlDoc, mneGroup, "globe:UPEJurisdiction", _
        UCase(Sheets("Section1").Range("H10").Value)
    filingInfo.appendChild mneGroup

    ' AccountingInfo
    Dim acctInfo As MSXML2.IXMLDOMElement
    Set acctInfo = xmlDoc.createElementNS(NS_GLOBE, "globe:AccountingInfo")
    AddElement xmlDoc, acctInfo, "globe:AccountingStandard", _
        Sheets("Section1").Range("I10").Value
    AddElement xmlDoc, acctInfo, "globe:FunctionalCurrency", _
        UCase(Sheets("Section1").Range("J10").Value)
    filingInfo.appendChild acctInfo

    ' ReportingFiscalYear
    Dim fy As MSXML2.IXMLDOMElement
    Set fy = xmlDoc.createElementNS(NS_GLOBE, "globe:ReportingFiscalYear")
    AddElement xmlDoc, fy, "globe:StartDate", _
        ToXMLDate(Sheets("Section1").Range("K5").Value)
    AddElement xmlDoc, fy, "globe:EndDate", _
        ToXMLDate(Sheets("Section1").Range("L5").Value)
    filingInfo.appendChild fy

    parent.appendChild filingInfo

End Sub

' ═══════════════════════════════════════════════════════════════════════
' Helper Functions
' ═══════════════════════════════════════════════════════════════════════

Private Sub AddElement(xmlDoc As MSXML2.DOMDocument60, _
                       parent As MSXML2.IXMLDOMElement, _
                       elementName As String, _
                       elementValue As String)

    Dim newElement As MSXML2.IXMLDOMElement
    Set newElement = xmlDoc.createElementNS(NS_GLOBE, elementName)
    newElement.Text = elementValue
    parent.appendChild newElement

End Sub

Private Sub AddMonetaryElement(xmlDoc As MSXML2.DOMDocument60, _
                               parent As MSXML2.IXMLDOMElement, _
                               elementName As String, _
                               amount As Double, _
                               currencyCode As String)

    Dim newElement As MSXML2.IXMLDOMElement
    Set newElement = xmlDoc.createElementNS(NS_GLOBE, elementName)
    newElement.setAttribute "currencyCode", UCase(currencyCode)
    newElement.Text = Format(amount, "0.00")
    parent.appendChild newElement

End Sub

Private Sub AddTINElement(xmlDoc As MSXML2.DOMDocument60, _
                          parent As MSXML2.IXMLDOMElement, _
                          tinValue As String, _
                          issuedBy As String)

    Dim tinElement As MSXML2.IXMLDOMElement
    Set tinElement = xmlDoc.createElementNS(NS_GLOBE, "globe:TIN")
    tinElement.setAttribute "issuedBy", UCase(issuedBy)

    If Trim(tinValue) = "" Then
        tinElement.Text = "NOTIN"
    Else
        tinElement.Text = Replace(Trim(tinValue), " ", "")
    End If

    parent.appendChild tinElement

End Sub

Private Function ToXMLPercentage(cellValue As Variant) As String
    Dim decValue As Double

    If IsNumeric(cellValue) Then
        If cellValue > 1 Then
            decValue = cellValue / 100
        Else
            decValue = cellValue
        End If
        ToXMLPercentage = Format(decValue, "0.0000")
    Else
        ToXMLPercentage = "0.0000"
    End If
End Function

Private Function ToXMLDate(dateValue As Variant) As String
    If IsDate(dateValue) Then
        ToXMLDate = Format(dateValue, "yyyy-mm-dd")
    Else
        ToXMLDate = ""
    End If
End Function

Private Function ToXMLTimestamp() As String
    ToXMLTimestamp = Format(Now, "yyyy-mm-dd") & "T" & _
                     Format(Now, "hh:mm:ss") & "Z"
End Function

Private Function EncodeXMLString(inputText As String) As String
    Dim result As String
    result = CStr(inputText)

    ' Ampersand must be encoded first
    result = Replace(result, "&", "&amp;")
    result = Replace(result, "<", "&lt;")
    result = Replace(result, ">", "&gt;")
    result = Replace(result, """", "&quot;")
    result = Replace(result, "'", "&apos;")

    EncodeXMLString = result
End Function

Private Function GetOutputPath() As String
    Dim fd As FileDialog
    Set fd = Application.FileDialog(msoFileDialogSaveAs)

    With fd
        .Title = "Save GIR XML File"
        .InitialFileName = "GIR_" & Format(Now, "yyyymmdd") & ".xml"
        .FilterIndex = 1
        If .Show = -1 Then
            GetOutputPath = .SelectedItems(1)
        Else
            GetOutputPath = ""
        End If
    End With
End Function
```

---

## 6.2.9 Post-Conversion Validation

### Immediate Post-Conversion Checks

After generating XML, perform these validation steps immediately:

#### Step 1: File Integrity Check

```
File Integrity Checklist:
☐ File created at expected location
☐ File size > 0 bytes (not empty)
☐ File extension is .xml
☐ File opens without error in text editor
☐ XML declaration present at start
☐ No binary characters visible
```

#### Step 2: Well-Formedness Check

```
Well-Formedness Checklist:
☐ XML declaration correct (<?xml version="1.0" encoding="UTF-8"?>)
☐ Single root element (globe:GIR_OECD)
☐ All opening tags have closing tags
☐ Tags properly nested (no overlap)
☐ Attribute values in quotes
☐ No unencoded special characters
```

#### Step 3: Schema Validation

```bash
# Using xmllint (Linux/Mac/Windows with tools installed)
xmllint --schema GIRMAIN_v1.0.xsd GlobalCo_GIR_FY2024.xml --noout

# Expected output if valid:
# GlobalCo_GIR_FY2024.xml validates

# Expected output if invalid:
# GlobalCo_GIR_FY2024.xml:127: element JurisdictionalETR: Schemas validity
# error : '25.00' is not a valid value of the atomic type 'Percentage_Type'
```

#### Step 4: Content Reconciliation

| Check | Calculator Value | XML Value | Match? |
|-------|-----------------|-----------|--------|
| Total GloBE Income (all jurisdictions) | € | € | ☐ |
| Total Covered Taxes (all jurisdictions) | € | € | ☐ |
| Total Top-up Tax | € | € | ☐ |
| Number of jurisdictions | | | ☐ |
| Number of constituent entities | | | ☐ |

---

## 6.2.10 Troubleshooting Common Conversion Issues

### Issue 1: Namespace Errors

**Error Message:** `Element '{urn:oecd:ties:gir:v1}GloBEIncome': This element is not expected.`

**Cause:** Missing or incorrect namespace prefix.

**Resolution:**
```xml
<!-- INCORRECT - Missing namespace prefix -->
<GloBEIncome>43500000.00</GloBEIncome>

<!-- CORRECT - With namespace prefix -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

---

### Issue 2: Empty Required Elements

**Error Message:** `Element 'TIN' cannot be empty.`

**Cause:** Required field blank in Calculator.

**Resolution:**
```xml
<!-- INCORRECT - Empty element -->
<globe:TIN issuedBy="GB"></globe:TIN>

<!-- CORRECT - Use NOTIN when no TIN exists -->
<globe:TIN issuedBy="GB">NOTIN</globe:TIN>
```

---

### Issue 3: Invalid Percentage Format

**Error Message:** `Value '25.00' is not valid for type 'percentage'.`

**Cause:** Percentage as whole number instead of decimal.

**Resolution:**
```xml
<!-- INCORRECT - Whole number -->
<globe:JurisdictionalETR>25.00</globe:JurisdictionalETR>

<!-- CORRECT - Decimal format -->
<globe:JurisdictionalETR>0.2500</globe:JurisdictionalETR>
```

---

### Issue 4: Invalid Date Format

**Error Message:** `Value '31/12/2024' is not a valid date.`

**Cause:** Local date format instead of ISO 8601.

**Resolution:**
```xml
<!-- INCORRECT - UK/EU format -->
<globe:EndDate>31/12/2024</globe:EndDate>

<!-- INCORRECT - US format -->
<globe:EndDate>12-31-2024</globe:EndDate>

<!-- CORRECT - ISO 8601 -->
<globe:EndDate>2024-12-31</globe:EndDate>
```

---

### Issue 5: Missing Currency Code Attribute

**Error Message:** `Attribute 'currencyCode' is required.`

**Cause:** Monetary element without currency attribute.

**Resolution:**
```xml
<!-- INCORRECT - Missing currencyCode -->
<globe:GloBEIncome>43500000.00</globe:GloBEIncome>

<!-- CORRECT - With currencyCode -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

---

### Issue 6: Character Encoding Issues

**Error Message:** `Invalid character in element content` or garbled text.

**Cause:** Non-UTF-8 characters or unencoded special characters.

**Resolution:**
```xml
<!-- INCORRECT - Unencoded ampersand -->
<globe:Name>GlobalCo Holdings & Partners</globe:Name>

<!-- CORRECT - Encoded ampersand -->
<globe:Name>GlobalCo Holdings &amp; Partners</globe:Name>

<!-- INCORRECT - Wrong encoding declaration -->
<?xml version="1.0" encoding="windows-1252"?>

<!-- CORRECT - UTF-8 encoding -->
<?xml version="1.0" encoding="UTF-8"?>
```

---

### Issue 7: Element Sequence Errors

**Error Message:** `Element 'ETR' is not expected at this position.`

**Cause:** Elements in wrong order (XML schema requires specific sequence).

**Resolution:**
```xml
<!-- INCORRECT - Wrong order -->
<globe:ETRComputation>
    <globe:JurisdictionalETR>0.2960</globe:JurisdictionalETR>
    <globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
    <globe:AdjustedCoveredTaxes currencyCode="EUR">12875000.00</globe:AdjustedCoveredTaxes>
</globe:ETRComputation>

<!-- CORRECT - Schema-defined order -->
<globe:ETRComputation>
    <globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
    <globe:AdjustedCoveredTaxes currencyCode="EUR">12875000.00</globe:AdjustedCoveredTaxes>
    <globe:JurisdictionalETR>0.2960</globe:JurisdictionalETR>
</globe:ETRComputation>
```

---

## 6.2.11 Conversion Quality Checklist

Use this comprehensive checklist for every XML conversion:

### Pre-Conversion Checks

| # | Check Item | Status | Notes |
|---|------------|--------|-------|
| 1 | All Calculator validation checks passed (Levels 1-4) | ☐ | |
| 2 | All data entered and reviewed | ☐ | |
| 3 | Reconciliations completed and balanced | ☐ | |
| 4 | Required approvals obtained | ☐ | |
| 5 | Export settings configured correctly | ☐ | |
| 6 | Output location accessible (write permission) | ☐ | |
| 7 | Unique Message Reference ID assigned | ☐ | |
| 8 | Correct fiscal year dates confirmed | ☐ | |

### During Conversion Checks

| # | Check Item | Status | Notes |
|---|------------|--------|-------|
| 9 | Conversion completes without errors | ☐ | |
| 10 | Generation log shows no warnings | ☐ | |
| 11 | File created at expected location | ☐ | |
| 12 | File size reasonable (not empty or unexpectedly small) | ☐ | |
| 13 | No timeout or interruption during generation | ☐ | |

### Post-Conversion Checks

| # | Check Item | Status | Notes |
|---|------------|--------|-------|
| 14 | Well-formedness check passes | ☐ | |
| 15 | Schema validation passes (GIRMAIN_v1.0.xsd) | ☐ | |
| 16 | All required elements present | ☐ | |
| 17 | Data types correctly formatted | ☐ | |
| 18 | Percentages in decimal format (0-1) | ☐ | |
| 19 | Dates in ISO 8601 format | ☐ | |
| 20 | Currency codes on all monetary amounts | ☐ | |
| 21 | Country codes are ISO 3166-1 alpha-2 | ☐ | |
| 22 | Monetary totals reconcile to Calculator | ☐ | |
| 23 | Jurisdiction count matches Calculator | ☐ | |
| 24 | Entity count matches Calculator | ☐ | |
| 25 | Visual inspection of key elements completed | ☐ | |
| 26 | Test upload to portal (if sandbox available) | ☐ | |
| 27 | Backup copy created in secure location | ☐ | |
| 28 | Generation log saved with XML file | ☐ | |

---

## 6.2.12 Key Takeaways

### Conversion Best Practices Summary

1. **Validate Before Converting**
   - Complete all Calculator validations first
   - Address all errors before XML generation
   - Conversion cannot fix underlying data issues

2. **Understand Data Transformations**
   - Percentages: Always decimal 0-1 (0.25 = 25%)
   - Dates: Always ISO 8601 (YYYY-MM-DD)
   - Monetary: Two decimals with currency code attribute
   - Special characters: Must be XML-encoded
   - TINs: Use "NOTIN" if no TIN exists

3. **Apply UTF-8 Encoding**
   - Required for OECD schema compliance
   - Handles international characters correctly
   - Verify encoding attribute in XML declaration
   - Do not include BOM (Byte Order Mark)

4. **Follow File Naming Conventions**
   - Use consistent, descriptive names
   - Include group name, fiscal year, version, date
   - Avoid spaces and special characters
   - Maintain version control

5. **Validate Thoroughly**
   - Schema validation immediately after generation
   - Reconcile totals against Calculator
   - Test in sandbox environment if available
   - Keep validation logs with files

6. **Use Appropriate Tools**
   - Built-in Calculator export for simple needs
   - Commercial software for complex multi-jurisdiction groups
   - VBA for customised requirements
   - Multiple validation tools for assurance

---

## Section Summary

Excel-to-XML conversion is a critical step requiring careful attention to data transformation and schema compliance. Key requirements include:

- **First Filing Deadline:** June 30, 2026 for calendar year 2024
- **Conversion Methods:** Built-in Calculator export, commercial Pillar Two software (Big 4, specialist vendors), VBA custom, or direct portal entry
- **Data Transformations:** Percentage decimals (0-1), ISO 8601 dates, monetary formatting (2 decimals + currency code), UTF-8 character encoding
- **Field Mapping:** ~480 Calculator fields map directly to XML elements via defined paths
- **Validation:** Schema validation mandatory; reconciliation to Calculator essential
- **Troubleshooting:** Common errors relate to percentages, dates, namespaces, and character encoding

The GIR Completion Calculator's built-in export function handles most transformations automatically, but understanding the underlying process is essential for troubleshooting, quality assurance, and working with external systems.

---

## Official Resources

- **OECD GIR XML Schema and User Guide:** https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html
- **OECD GIR Template (January 2025):** https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html

---

## Navigation

**Previous:** [Section 6.1: Understanding the OECD XML Schema](Section_06_01_Understanding_the_OECD_XML_Schema.md)

**Next:** [Section 6.3: XML Validation Procedures](Section_06_03_XML_Validation_Procedures.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
