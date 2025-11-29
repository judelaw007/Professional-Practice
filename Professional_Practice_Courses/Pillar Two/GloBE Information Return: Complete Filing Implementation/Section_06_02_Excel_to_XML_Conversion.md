# Section 6.2: Excel-to-XML Conversion

## Introduction

Converting GIR data from the Excel-based Calculator to OECD-compliant XML format is a critical step in the filing process. This conversion must preserve data integrity, apply correct formatting standards, and produce a file that passes schema validation. Whether using built-in Calculator functionality, commercial software, or custom tools, understanding the conversion process is essential for successful GIR submission.

This section provides step-by-step guidance for converting Calculator data to XML, including mapping procedures, quality checks, and troubleshooting common conversion issues.

**Learning Objectives:**
- Execute Excel-to-XML conversion using multiple methods
- Map Calculator fields to XML schema elements
- Apply correct data formatting during conversion
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
│   └── Integrated validation
│
├── Method 2: Commercial Pillar Two Software
│   ├── Tax-Model TaxSuite
│   ├── PwC Pillar Two Engine
│   ├── CSC Corptax GMT
│   ├── Thomson Reuters ONESOURCE
│   └── Wolters Kluwer CCH Integrator
│
├── Method 3: General XML Tools
│   ├── Altova XMLSpy
│   ├── Oxygen XML Editor
│   ├── Microsoft XML Notepad
│   └── Excel Power Query to XML
│
├── Method 4: VBA-Based Export
│   ├── Custom macro development
│   ├── Direct XML DOM manipulation
│   └── Tailored to Calculator structure
│
└── Method 5: Tax Authority Portals
    ├── Online form entry
    ├── Portal generates XML
    └── Jurisdiction-specific (limited availability)
```

### Method Comparison

| Method | Complexity | Cost | Validation | Best For |
|--------|------------|------|------------|----------|
| Calculator Export | Low | Included | Built-in | Most users |
| Commercial Software | Low | High (licence) | Comprehensive | Large MNEs |
| General XML Tools | Medium | Varies | Manual | Technical users |
| VBA Export | High | Development time | Custom | Bespoke needs |
| Tax Authority Portal | Low | Free | Automatic | Single jurisdiction |

---

## 6.2.2 Built-in Calculator XML Export

### Overview

The GIR Completion Calculator includes a built-in XML export function that automates the conversion process.

**Tab:** `XML Export`

### Pre-Export Checklist

Before generating XML, complete these checks:

| # | Check Item | Status | Action if Failed |
|---|------------|--------|------------------|
| 1 | All validation checks passed | ☐ | Resolve errors in Section 5.5 |
| 2 | Reconciliations completed | ☐ | Complete reconciliation tabs |
| 3 | Sign-off obtained | ☐ | Obtain required approvals |
| 4 | Correct fiscal year selected | ☐ | Verify fiscal year setting |
| 5 | Currency consistently EUR | ☐ | Convert non-EUR amounts |

### Step-by-Step Export Process

**Step 1: Navigate to XML Export Tab**

Open the `XML Export` tab in your GIR Completion Calculator.

**Step 2: Configure Export Settings**

| Setting | Description | Example |
|---------|-------------|---------|
| Output File Name | Name for XML file | GlobalCo_GIR_2024.xml |
| Output Location | Folder path | C:\GIR_Files\2024\ |
| Schema Version | OECD schema version | 1.0 |
| Message Reference ID | Unique identifier | GB2024GIR000001 |
| Sending Authority | Filing jurisdiction | GB |
| Receiving Authority | Exchange recipient (if applicable) | Leave blank for domestic |

**Step 3: Verify Field Mapping**

The Calculator displays a mapping summary:

```
Field Mapping Preview:
┌─────────────────────────────────────────────────────────────────┐
│ Calculator Field          │ XML Element              │ Status  │
├─────────────────────────────────────────────────────────────────┤
│ FCE_Name (Section1!B5)    │ FilingConstituentEntity  │ ✓ Ready │
│                           │   /Name                  │         │
│ FCE_TIN (Section1!C5)     │ FilingConstituentEntity  │ ✓ Ready │
│                           │   /TIN                   │         │
│ GloBE_Income (S3.1!AK22)  │ ETRComputation           │ ✓ Ready │
│                           │   /GloBEIncome           │         │
│ ETR (S3.1!E5)             │ ETRComputation/ETR       │ ✓ Ready │
│ [Additional mappings...]                                        │
└─────────────────────────────────────────────────────────────────┘
```

**Step 4: Generate XML**

Click the **[Generate XML]** button.

The Calculator will:
1. Extract data from all sections
2. Apply formatting transformations
3. Build XML structure
4. Validate against schema
5. Save to specified location

**Step 5: Review Generation Log**

```
XML Generation Log:
├── 14:30:00 - Starting XML generation
├── 14:30:01 - Extracting Section 1 data (52 fields)
├── 14:30:02 - Extracting Section 2 data (40 fields)
├── 14:30:05 - Extracting Section 3 data (385 fields)
├── 14:30:08 - Applying data transformations
├── 14:30:10 - Building XML structure
├── 14:30:12 - Schema validation: PASSED
├── 14:30:12 - File saved: GlobalCo_GIR_2024.xml
└── 14:30:12 - Generation complete - 0 errors, 0 warnings
```

---

## 6.2.3 Data Transformation Rules

### Percentage Conversion

Calculator percentages must be converted to decimal format:

```
Percentage Transformation:
├── Calculator displays: 25.00%
├── Calculator stores: 0.25 or 25.00 (varies by cell)
├── XML requires: 0.2500
│
├── Transformation Formula:
│   IF cell is stored as percentage → Direct use
│   IF cell is stored as whole number → Divide by 100
│
└── Example Mappings:
    ├── ETR 29.60% → 0.2960
    ├── Top-up % 2.52% → 0.0252
    └── Ownership 100% → 1.0000
```

**Calculator Transformation Code:**

```vba
Function ToXMLPercentage(cellValue As Variant) As String
    Dim decValue As Double

    If IsNumeric(cellValue) Then
        If cellValue > 1 Then
            ' Stored as whole number (e.g., 25 for 25%)
            decValue = cellValue / 100
        Else
            ' Stored as decimal (e.g., 0.25 for 25%)
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
Monetary Transformation:
├── Calculator displays: €43,500,000.00
├── Calculator stores: 43500000
├── XML requires: 43500000.00 (no separators, 2 decimals)
│
├── Transformation Rules:
│   1. Remove thousand separators
│   2. Ensure 2 decimal places
│   3. Use period (.) as decimal separator
│   4. Add currency code attribute
│
└── Example:
    Calculator: €43,500,000.00
    XML: <globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

### Date Formatting

```
Date Transformation:
├── Calculator displays: 31/12/2024 or 12/31/2024
├── Calculator stores: Excel serial date (45657)
├── XML requires: 2024-12-31 (ISO 8601)
│
├── Transformation Formula:
│   Format(dateValue, "yyyy-mm-dd")
│
└── Examples:
    ├── 31/12/2024 → 2024-12-31
    ├── 01/01/2024 → 2024-01-01
    └── 30/06/2026 → 2026-06-30
```

### TIN Handling

```
TIN Transformation:
├── Calculator stores: "12345678" with jurisdiction "GB"
├── XML requires: <globe:TIN issuedBy="GB">12345678</globe:TIN>
│
├── Special Cases:
│   ├── No TIN issued → <globe:TIN issuedBy="GB">NOTIN</globe:TIN>
│   ├── TIN with spaces → Remove spaces before export
│   └── TIN with special chars → Preserve as entered
│
└── Validation: Check against jurisdiction TIN patterns
```

### Country Code Standardisation

```
Country Code Transformation:
├── Calculator may have: "United Kingdom", "UK", "GB"
├── XML requires: ISO 3166-1 alpha-2 code only
│
├── Lookup Table:
│   ├── United Kingdom → GB
│   ├── Germany → DE
│   ├── United States → US
│   ├── Netherlands → NL
│   └── [Full ISO code list...]
│
└── Validation: Reject non-standard codes
```

---

## 6.2.4 Field Mapping Reference

### Section 1 Mapping

| Calculator Location | Calculator Field | XML Path | Data Type |
|--------------------|------------------|----------|-----------|
| Section1!B5 | FCE_Name | /FilingInfo/FilingConstituentEntity/Name | String |
| Section1!C5 | FCE_TIN | /FilingInfo/FilingConstituentEntity/TIN | TIN |
| Section1!D5 | FCE_Jurisdiction | /FilingInfo/FilingConstituentEntity/ResCountryCode | ISO Code |
| Section1!E5 | FCE_Address | /FilingInfo/FilingConstituentEntity/Address/AddressFree | String |
| Section1!F10 | UPE_Name | /CorporateStructure/UPE/Name | String |
| Section1!G10 | UPE_TIN | /CorporateStructure/UPE/TIN | TIN |
| Section1!H10 | UPE_Jurisdiction | /CorporateStructure/UPE/ResCountryCode | ISO Code |
| Section1!I10 | Accounting_Standard | /FilingInfo/AccountingInfo/AccountingStandard | Enum |
| Section1!J10 | Functional_Currency | /FilingInfo/AccountingInfo/FunctionalCurrency | ISO 4217 |
| Section1!K5 | FY_Start | /FilingInfo/ReportingFiscalYear/StartDate | Date |
| Section1!L5 | FY_End | /FilingInfo/ReportingFiscalYear/EndDate | Date |

### Section 2 Mapping

| Calculator Location | Calculator Field | XML Path | Data Type |
|--------------------|------------------|----------|-----------|
| Section2!B5 | Jurisdiction | /JurisdictionSection/JurisdictionCode | ISO Code |
| Section2!S5 | TransitionalSH_Elected | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH/Elected | Boolean |
| Section2!T5 | Qualifying_Test | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH/QualifyingTest | Enum |
| Section2!N5 | SimplifiedETR | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH/SimplifiedETR | Percentage |
| Section2!N50 | QDMTTSH_Elected | /JurisdictionSection/SafeHarbours/QDMTTSH/Elected | Boolean |
| Section2!O50 | QDMTT_Amount | /JurisdictionSection/SafeHarbours/QDMTTSH/Amount | Monetary |

### Section 3 Mapping

| Calculator Location | Calculator Field | XML Path | Data Type |
|--------------------|------------------|----------|-----------|
| S3.1!AK22 | Net_GloBE_Income | /JurisdictionSection/GloBEComputations/ETRComputation/GloBEIncome | Monetary |
| S3.1!X20 | Adjusted_Covered_Taxes | /JurisdictionSection/GloBEComputations/ETRComputation/AdjustedCoveredTaxes | Monetary |
| S3.1!E5 | Jurisdictional_ETR | /JurisdictionSection/GloBEComputations/ETRComputation/ETR | Percentage |
| S3.2!R20 | Payroll_Carveout | /JurisdictionSection/GloBEComputations/SBIEComputation/PayrollCarveOut | Monetary |
| S3.2!AE20 | Asset_Carveout | /JurisdictionSection/GloBEComputations/SBIEComputation/TangibleAssetCarveOut | Monetary |
| S3.2!I5 | Total_SBIE | /JurisdictionSection/GloBEComputations/SBIEComputation/TotalSBIE | Monetary |
| S3.3!H5 | Excess_Profit | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/ExcessProfit | Monetary |
| S3.3!E5 | TopUp_Percentage | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/TopUpTaxPercentage | Percentage |
| S3.3!Q5 | Final_TopUp_Tax | /JurisdictionSection/GloBEComputations/TopUpTaxComputation/FinalTopUpTax | Monetary |

---

## 6.2.5 VBA-Based XML Generation

### Overview

For organisations requiring customised XML generation, VBA (Visual Basic for Applications) provides direct control over the conversion process.

### Sample VBA Export Module

```vba
' GIR XML Export Module
' Requires: Microsoft XML, v6.0 reference

Option Explicit

Public Sub ExportGIRToXML()

    Dim xmlDoc As MSXML2.DOMDocument60
    Dim rootElement As MSXML2.IXMLDOMElement
    Dim outputPath As String

    ' Initialize XML Document
    Set xmlDoc = New MSXML2.DOMDocument60
    xmlDoc.async = False
    xmlDoc.preserveWhiteSpace = True

    ' Add XML Declaration
    Dim xmlDecl As MSXML2.IXMLDOMProcessingInstruction
    Set xmlDecl = xmlDoc.createProcessingInstruction("xml", _
        "version=""1.0"" encoding=""UTF-8""")
    xmlDoc.appendChild xmlDecl

    ' Create Root Element with Namespaces
    Set rootElement = xmlDoc.createElementNS( _
        "urn:oecd:ties:gir:v1", "globe:GIR_OECD")
    rootElement.setAttribute "xmlns:stf", "urn:oecd:ties:gircommontypes:v1"
    rootElement.setAttribute "version", "1.0"
    xmlDoc.appendChild rootElement

    ' Build MessageHeader
    Call BuildMessageHeader(xmlDoc, rootElement)

    ' Build GIRBody
    Call BuildGIRBody(xmlDoc, rootElement)

    ' Save File
    outputPath = GetOutputPath()
    xmlDoc.Save outputPath

    MsgBox "XML exported successfully to: " & outputPath

End Sub

Private Sub BuildMessageHeader(xmlDoc As MSXML2.DOMDocument60, _
                               parent As MSXML2.IXMLDOMElement)

    Dim header As MSXML2.IXMLDOMElement
    Set header = xmlDoc.createElementNS("urn:oecd:ties:gir:v1", _
        "globe:MessageHeader")

    ' Sending Competent Authority
    AddElement xmlDoc, header, "globe:SendingCompetentAuthority", _
        Sheets("Section1").Range("D5").Value

    ' Message Type
    AddElement xmlDoc, header, "globe:MessageType", "GIR"

    ' Message Reference ID
    AddElement xmlDoc, header, "globe:MessageRefId", _
        Sheets("XMLExport").Range("B5").Value

    ' Message Type Indicator
    AddElement xmlDoc, header, "globe:MessageTypeIndic", "GIR"

    ' Reporting Period
    AddElement xmlDoc, header, "globe:ReportingPeriod", _
        Format(Sheets("Section1").Range("L5").Value, "yyyy-mm-dd")

    ' Timestamp
    AddElement xmlDoc, header, "globe:Timestamp", _
        Format(Now, "yyyy-mm-dd") & "T" & Format(Now, "hh:mm:ss") & "Z"

    parent.appendChild header

End Sub

Private Sub BuildGIRBody(xmlDoc As MSXML2.DOMDocument60, _
                         parent As MSXML2.IXMLDOMElement)

    Dim body As MSXML2.IXMLDOMElement
    Set body = xmlDoc.createElementNS("urn:oecd:ties:gir:v1", _
        "globe:GIRBody")

    ' FilingInfo
    Call BuildFilingInfo(xmlDoc, body)

    ' JurisdictionSections (loop through jurisdictions)
    Call BuildJurisdictionSections(xmlDoc, body)

    ' CorporateStructure
    Call BuildCorporateStructure(xmlDoc, body)

    parent.appendChild body

End Sub

Private Sub AddElement(xmlDoc As MSXML2.DOMDocument60, _
                       parent As MSXML2.IXMLDOMElement, _
                       elementName As String, _
                       elementValue As String)

    Dim newElement As MSXML2.IXMLDOMElement
    Set newElement = xmlDoc.createElementNS("urn:oecd:ties:gir:v1", elementName)
    newElement.Text = elementValue
    parent.appendChild newElement

End Sub

Private Sub AddMonetaryElement(xmlDoc As MSXML2.DOMDocument60, _
                               parent As MSXML2.IXMLDOMElement, _
                               elementName As String, _
                               amount As Double, _
                               currencyCode As String)

    Dim newElement As MSXML2.IXMLDOMElement
    Set newElement = xmlDoc.createElementNS("urn:oecd:ties:gir:v1", elementName)
    newElement.setAttribute "currencyCode", currencyCode
    newElement.Text = Format(amount, "0.00")
    parent.appendChild newElement

End Sub

Private Function ToXMLPercentage(value As Variant) As String
    If IsNumeric(value) Then
        If value > 1 Then
            ToXMLPercentage = Format(value / 100, "0.0000")
        Else
            ToXMLPercentage = Format(value, "0.0000")
        End If
    Else
        ToXMLPercentage = "0.0000"
    End If
End Function
```

---

## 6.2.6 Commercial Software Integration

### Data Export for Commercial Tools

Many organisations use commercial Pillar Two software. The Calculator supports data export in formats compatible with major platforms.

**Tab:** `Data Export`

### Export Formats Available

| Format | Target Software | File Extension |
|--------|----------------|----------------|
| CSV - Standard | Multiple platforms | .csv |
| CSV - Tax-Model | Tax-Model TaxSuite | .csv |
| JSON | API-based tools | .json |
| Excel - Mapped | Manual import | .xlsx |
| Direct API | Where supported | N/A |

### CSV Export Structure

```csv
"Section","Field","Jurisdiction","EntityID","Value","DataType"
"S1","FCE_Name","GB","","GlobalCo Holdings plc","String"
"S1","FCE_TIN","GB","","12345678","TIN"
"S3","GloBE_Income","DE","CE-DE-001","12000000.00","Monetary"
"S3","ETR","DE","","0.2960","Percentage"
...
```

### API Integration Example

```json
{
  "girData": {
    "filingInfo": {
      "fce": {
        "name": "GlobalCo Holdings plc",
        "tin": "12345678",
        "jurisdiction": "GB"
      },
      "fiscalYear": {
        "start": "2024-01-01",
        "end": "2024-12-31"
      }
    },
    "jurisdictions": [
      {
        "code": "DE",
        "etrComputation": {
          "globeIncome": 43500000.00,
          "coveredTaxes": 12875000.00,
          "etr": 0.2960
        }
      }
    ]
  }
}
```

---

## 6.2.7 XML Validation After Conversion

### Post-Conversion Validation Steps

After generating XML, perform these validation checks:

**Step 1: Schema Validation**

```
Schema Validation Checklist:
☐ XML well-formed (proper syntax)
☐ All required elements present
☐ Element sequence correct
☐ Data types valid
☐ Namespace declarations correct
☐ No schema violations
```

**Step 2: Content Validation**

```
Content Validation Checklist:
☐ All monetary amounts have currency codes
☐ Percentages in decimal format (0-1)
☐ Dates in ISO 8601 format
☐ Country codes are ISO 3166-1 alpha-2
☐ TINs include issuedBy attribute
☐ Message Reference ID is unique
```

**Step 3: Reconciliation Check**

```
Reconciliation Validation:
☐ XML totals match Calculator totals
☐ Jurisdiction count matches
☐ Entity count matches
☐ Top-up Tax total matches
☐ No data lost in conversion
```

### Validation Tool Usage

**Using xmllint (Command Line):**

```bash
# Validate against OECD schema
xmllint --schema GIR_v1.0.xsd GlobalCo_GIR_2024.xml --noout

# Pretty print for review
xmllint --format GlobalCo_GIR_2024.xml > formatted_output.xml
```

**Using Calculator Built-in Validation:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click [Validate XML] | Validation runs |
| 2 | Review results | All checks PASS |
| 3 | Address any errors | Fix and re-validate |
| 4 | Export validation report | PDF documentation |

---

## 6.2.8 Troubleshooting Common Conversion Issues

### Issue 1: Namespace Errors

**Error Message:** `Element '{urn:oecd:ties:gir:v1}GloBEIncome': This element is not expected.`

**Cause:** Incorrect namespace declaration or missing namespace prefix.

**Resolution:**
```xml
<!-- INCORRECT -->
<GloBEIncome>43500000.00</GloBEIncome>

<!-- CORRECT -->
<globe:GloBEIncome>43500000.00</globe:GloBEIncome>
```

### Issue 2: Empty Required Elements

**Error Message:** `Element 'TIN' cannot be empty.`

**Cause:** Required field left blank in Calculator.

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:TIN issuedBy="GB"></globe:TIN>

<!-- CORRECT (if no TIN) -->
<globe:TIN issuedBy="GB">NOTIN</globe:TIN>
```

### Issue 3: Invalid Percentage Format

**Error Message:** `Value '25.00' is not valid for type 'percentage'.`

**Cause:** Percentage exported as whole number instead of decimal.

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:ETR>25.00</globe:ETR>

<!-- CORRECT -->
<globe:ETR>0.2500</globe:ETR>
```

### Issue 4: Date Format Errors

**Error Message:** `Value '31/12/2024' is not a valid date.`

**Cause:** Local date format used instead of ISO 8601.

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:EndDate>31/12/2024</globe:EndDate>

<!-- CORRECT -->
<globe:EndDate>2024-12-31</globe:EndDate>
```

### Issue 5: Missing Currency Code

**Error Message:** `Attribute 'currencyCode' is required.`

**Cause:** Monetary element missing currency attribute.

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:GloBEIncome>43500000.00</globe:GloBEIncome>

<!-- CORRECT -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

### Issue 6: Character Encoding Issues

**Error Message:** `Invalid character in element content.`

**Cause:** Special characters not properly encoded.

**Resolution:**
```xml
<!-- Special characters must be encoded -->
& → &amp;
< → &lt;
> → &gt;
" → &quot;
' → &apos;

<!-- Example -->
<!-- INCORRECT -->
<globe:Name>GlobalCo Holdings & Partners</globe:Name>

<!-- CORRECT -->
<globe:Name>GlobalCo Holdings &amp; Partners</globe:Name>
```

### Issue 7: Element Sequence Errors

**Error Message:** `Element 'ETR' is not expected at this position.`

**Cause:** Elements in wrong order.

**Resolution:** Follow exact sequence defined in schema:
```xml
<!-- CORRECT sequence for ETRComputation -->
<globe:ETRComputation>
    <globe:GloBEIncome>...</globe:GloBEIncome>
    <globe:AdjustedCoveredTaxes>...</globe:AdjustedCoveredTaxes>
    <globe:ETR>...</globe:ETR>
</globe:ETRComputation>
```

---

## 6.2.9 Conversion Quality Checklist

Use this checklist for every XML conversion:

**Pre-Conversion:**

| # | Check Item | Status |
|---|------------|--------|
| 1 | Calculator validation completed | ☐ |
| 2 | All data entered and reviewed | ☐ |
| 3 | Export settings configured correctly | ☐ |
| 4 | Output location accessible | ☐ |
| 5 | Unique Message Reference ID assigned | ☐ |

**During Conversion:**

| # | Check Item | Status |
|---|------------|--------|
| 6 | Conversion completes without errors | ☐ |
| 7 | Generation log shows no warnings | ☐ |
| 8 | File created at expected location | ☐ |
| 9 | File size reasonable (not empty) | ☐ |

**Post-Conversion:**

| # | Check Item | Status |
|---|------------|--------|
| 10 | Schema validation passes | ☐ |
| 11 | All required elements present | ☐ |
| 12 | Data types correctly formatted | ☐ |
| 13 | Monetary totals reconcile | ☐ |
| 14 | Jurisdiction count matches | ☐ |
| 15 | Entity count matches | ☐ |
| 16 | Visual inspection of key elements | ☐ |
| 17 | Test upload to portal (if available) | ☐ |
| 18 | Backup copy created | ☐ |

---

## 6.2.10 Key Takeaways

### Conversion Best Practices

1. **Validate Before Converting**
   - Complete all Calculator validations first
   - Address errors before XML generation
   - Conversion cannot fix bad data

2. **Understand Data Transformations**
   - Percentages: Always decimal (0-1)
   - Dates: Always ISO 8601 (YYYY-MM-DD)
   - Monetary: Two decimals with currency code
   - Special characters: Must be encoded

3. **Use Schema Validation**
   - Validate against OECD schema immediately
   - Multiple validation passes recommended
   - Don't skip validation for "small" changes

4. **Maintain Reconciliation Trail**
   - Verify XML totals match Calculator
   - Document any discrepancies
   - Keep conversion logs

5. **Test Before Production**
   - Use tax authority test environments where available
   - Validate in multiple tools
   - Review XML visually for obvious issues

---

## Section Summary

Excel-to-XML conversion is a critical step requiring careful attention to data transformation and schema compliance. Key requirements include:

- **Conversion Methods:** Built-in export, commercial software, VBA custom, or portal entry
- **Data Transformations:** Percentage decimals, ISO dates, monetary formatting, character encoding
- **Field Mapping:** Calculator cells map directly to XML elements via defined paths
- **Validation:** Schema validation mandatory before submission
- **Troubleshooting:** Common errors relate to namespaces, data types, and element sequence

The GIR Completion Calculator's built-in export function handles most transformations automatically, but understanding the underlying process is essential for troubleshooting and quality assurance.

---

## Navigation

**Previous:** [Section 6.1: Understanding the OECD XML Schema](Section_06_01_Understanding_the_OECD_XML_Schema.md)

**Next:** [Section 6.3: Pre-Submission Validation](Section_06_03_Pre_Submission_Validation.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
