# Section 6.3: XML Validation Procedures

## Introduction

Before submitting a GIR XML file, rigorous validation is essential to ensure acceptance by tax authorities and avoid rejection. The OECD has established a comprehensive validation framework including file-level checks, record-level validation, and business rules verification. Understanding and implementing these validation procedures prevents filing delays and potential penalties.

This section provides step-by-step guidance for validating GIR XML files, interpreting error messages, and ensuring compliance with both schema requirements and business rules.

**Learning Objectives:**
- Execute multi-level XML validation (well-formedness, schema, business rules)
- Use validation tools effectively (command line, GUI, online)
- Interpret and resolve validation error messages
- Understand the OECD Status Message Schema for error reporting
- Prepare for tax authority validation requirements

---

## 6.3.1 Validation Framework Overview

### Three Levels of Validation

GIR XML validation operates at three distinct levels:

```
GIR XML Validation Levels:
│
├── Level 1: Well-Formedness
│   ├── XML syntax correct
│   ├── Proper tag nesting
│   ├── Valid character encoding (UTF-8)
│   ├── Closing tags match opening tags
│   └── Reserved characters escaped
│
├── Level 2: Schema Validation
│   ├── Elements match schema definition
│   ├── Required elements present
│   ├── Data types correct
│   ├── Element sequence correct
│   ├── Cardinality rules met
│   └── Namespace declarations valid
│
└── Level 3: Business Rules Validation
    ├── Cross-field consistency
    ├── Mathematical accuracy
    ├── Logical coherence
    ├── Reference integrity
    └── Jurisdiction-specific rules
```

### OECD Validation Architecture

The OECD has established two complementary validation mechanisms:

| Component | Purpose | Publication Date |
|-----------|---------|------------------|
| **GIR XML Schema** | Defines structure and data types | January 2025 |
| **GIR Status Message Schema** | Reports validation errors | July 2025 |

---

## 6.3.2 Level 1: Well-Formedness Validation

### Definition

A well-formed XML document follows basic XML syntax rules regardless of any schema definition.

### Well-Formedness Requirements

```
Well-Formedness Checklist:
│
├── Single Root Element
│   └── Document has exactly one root element (<globe:GIR_OECD>)
│
├── Proper Tag Structure
│   ├── All tags properly closed
│   ├── Tags case-sensitive and matched
│   └── No overlapping elements
│
├── Character Encoding
│   ├── UTF-8 declaration present
│   ├── Special characters escaped
│   └── No invalid control characters
│
├── Attribute Formatting
│   ├── Attribute values in quotes
│   ├── No duplicate attributes
│   └── Valid attribute names
│
└── Reserved Character Escaping
    ├── & → &amp;
    ├── < → &lt;
    ├── > → &gt;
    ├── " → &quot;
    └── ' → &apos;
```

### Common Well-Formedness Errors

| Error | Example | Resolution |
|-------|---------|------------|
| Unclosed tag | `<globe:Name>GlobalCo` | Add `</globe:Name>` |
| Mismatched tags | `<Name>GlobalCo</NAME>` | Match case exactly |
| Unescaped ampersand | `<Name>Smith & Co</Name>` | Use `&amp;` |
| Missing quotes | `<TIN issuedBy=GB>` | Add quotes: `issuedBy="GB"` |
| Invalid characters | Control characters | Remove or encode |

### Well-Formedness Validation Commands

**Using xmllint:**

```bash
# Check well-formedness only (no schema)
xmllint --noout GlobalCo_GIR_2024.xml

# Output if well-formed:
# (no output, exit code 0)

# Output if malformed:
# GlobalCo_GIR_2024.xml:45: parser error : Opening and ending tag mismatch
```

**Using Python:**

```python
import xml.etree.ElementTree as ET

def check_wellformedness(filepath):
    try:
        ET.parse(filepath)
        print("Document is well-formed")
        return True
    except ET.ParseError as e:
        print(f"Well-formedness error: {e}")
        return False

check_wellformedness("GlobalCo_GIR_2024.xml")
```

---

## 6.3.3 Level 2: Schema Validation

### Definition

Schema validation verifies that the XML document conforms to the OECD GIR XML Schema definition (XSD).

### Schema Validation Checks

```
Schema Validation Requirements:
│
├── Element Validation
│   ├── All elements defined in schema
│   ├── Required elements present
│   ├── Optional elements correctly used
│   └── No unknown elements
│
├── Attribute Validation
│   ├── Required attributes present
│   ├── Attribute values valid
│   └── No unknown attributes
│
├── Data Type Validation
│   ├── Strings within max length
│   ├── Numbers correctly formatted
│   ├── Dates in ISO 8601 format
│   ├── Percentages as decimals (0-1)
│   └── Enumerations from valid list
│
├── Structure Validation
│   ├── Element sequence correct
│   ├── Cardinality respected (min/max)
│   ├── Nesting correct
│   └── Choice groups valid
│
└── Namespace Validation
    ├── Namespace declarations present
    ├── Prefixes correctly used
    └── Schema location valid
```

### Obtaining the Schema

```
Schema Sources:
├── OECD Website: https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html
├── File: GIR_v1.0.xsd
├── Associated files: CommonTypes_v1.0.xsd
└── Always use official OECD release
```

### Schema Validation Tools

#### Command Line: xmllint

```bash
# Schema validation with xmllint
xmllint --schema GIR_v1.0.xsd GlobalCo_GIR_2024.xml --noout

# Successful output:
# GlobalCo_GIR_2024.xml validates

# Failed output:
# GlobalCo_GIR_2024.xml:127: element ETR: Schemas validity error :
# Element '{urn:oecd:ties:gir:v1}ETR': '25.00' is not a valid value
# of the atomic type 'percentage'.
# GlobalCo_GIR_2024.xml fails to validate
```

#### GUI Tool: Altova XMLSpy

```
XMLSpy Validation Steps:
1. Open XML file in XMLSpy
2. Click XML menu → Validate (F8)
3. Review validation results in Messages window
4. Double-click errors to navigate to source
5. Use SmartFix to auto-correct where available
```

#### Online Validator

```
Online Validation Steps:
1. Navigate to xmlvalidation.com or similar
2. Paste XML content or upload file
3. Upload or reference XSD schema
4. Click Validate
5. Review error list

Note: Use with caution for sensitive data
```

#### Python with lxml

```python
from lxml import etree

def validate_schema(xml_file, xsd_file):
    # Load schema
    with open(xsd_file, 'rb') as f:
        schema_doc = etree.parse(f)
    schema = etree.XMLSchema(schema_doc)

    # Load and validate XML
    with open(xml_file, 'rb') as f:
        xml_doc = etree.parse(f)

    if schema.validate(xml_doc):
        print("Schema validation PASSED")
        return True
    else:
        print("Schema validation FAILED")
        for error in schema.error_log:
            print(f"  Line {error.line}: {error.message}")
        return False

validate_schema("GlobalCo_GIR_2024.xml", "GIR_v1.0.xsd")
```

---

### Common Schema Validation Errors

#### Error Category 1: Missing Required Elements

**Error Message:**
```
Element '{urn:oecd:ties:gir:v1}FilingConstituentEntity': Missing child element(s).
Expected is ( {urn:oecd:ties:gir:v1}TIN ).
```

**Resolution:**
```xml
<!-- Add missing TIN element -->
<globe:FilingConstituentEntity>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:TIN issuedBy="GB">12345678</globe:TIN>  <!-- Add this -->
    <globe:ResCountryCode>GB</globe:ResCountryCode>
</globe:FilingConstituentEntity>
```

#### Error Category 2: Invalid Data Type

**Error Message:**
```
Element '{urn:oecd:ties:gir:v1}ETR': '25.00' is not a valid value
of the atomic type 'percentage'.
```

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:ETR>25.00</globe:ETR>

<!-- CORRECT (decimal format 0-1) -->
<globe:ETR>0.2500</globe:ETR>
```

#### Error Category 3: Invalid Enumeration Value

**Error Message:**
```
Element '{urn:oecd:ties:gir:v1}AccountingStandard': 'GAAP' is not a
valid value of the atomic type.
```

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:AccountingStandard>GAAP</globe:AccountingStandard>

<!-- CORRECT (use valid enumeration) -->
<globe:AccountingStandard>US_GAAP</globe:AccountingStandard>
```

#### Error Category 4: Element Sequence Error

**Error Message:**
```
Element '{urn:oecd:ties:gir:v1}TIN': This element is not expected.
Expected is ( {urn:oecd:ties:gir:v1}Name ).
```

**Resolution:**
```xml
<!-- INCORRECT sequence -->
<globe:FilingConstituentEntity>
    <globe:TIN issuedBy="GB">12345678</globe:TIN>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
</globe:FilingConstituentEntity>

<!-- CORRECT sequence -->
<globe:FilingConstituentEntity>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:TIN issuedBy="GB">12345678</globe:TIN>
</globe:FilingConstituentEntity>
```

#### Error Category 5: Missing Required Attribute

**Error Message:**
```
Element '{urn:oecd:ties:gir:v1}GloBEIncome': The attribute 'currencyCode' is required.
```

**Resolution:**
```xml
<!-- INCORRECT -->
<globe:GloBEIncome>43500000.00</globe:GloBEIncome>

<!-- CORRECT -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

---

## 6.3.4 Level 3: Business Rules Validation

### Definition

Business rules validation verifies logical consistency and accuracy of data beyond schema compliance.

### Business Rules Categories

```
Business Rules Framework:
│
├── Cross-Field Consistency
│   ├── ETR = Covered Taxes ÷ GloBE Income
│   ├── Top-up % = 15% - ETR (if ETR < 15%)
│   ├── Excess Profit = GloBE Income - SBIE
│   ├── SBIE = Payroll Carve-out + Asset Carve-out
│   └── Final TUT = Initial TUT + Additional - QDMTT
│
├── Cross-Section Consistency
│   ├── Section 1 jurisdictions = Section 3 jurisdictions
│   ├── Section 1 CE count = Section 3 CE count
│   ├── Section 2 elections reduce Section 3 scope
│   └── ETR summary matches detailed calculations
│
├── Mathematical Accuracy
│   ├── Totals equal sum of components
│   ├── Percentages within valid range
│   ├── No negative values where prohibited
│   └── Rounding applied consistently
│
├── Reference Integrity
│   ├── Entity IDs unique within file
│   ├── Parent entity references valid
│   ├── Jurisdiction codes from ISO list
│   └── Message Reference ID unique
│
└── Temporal Consistency
    ├── Fiscal year dates valid
    ├── Timestamp within expected range
    ├── Prior year references valid
    └── Transition period compliance
```

### Calculator Business Rule Checks

**Tab:** `Business Rules Validation`

| Rule ID | Description | Formula/Check | Tolerance |
|---------|-------------|---------------|-----------|
| BR-001 | ETR calculation accuracy | ETR = CoveredTaxes ÷ GloBEIncome | 0.0001 |
| BR-002 | Top-up % accuracy | TopUp% = MAX(0.15 - ETR, 0) | 0.0001 |
| BR-003 | Excess Profit accuracy | ExcessProfit = MAX(GloBEIncome - SBIE, 0) | €1 |
| BR-004 | SBIE total accuracy | SBIE = PayrollCO + AssetCO | €1 |
| BR-005 | Initial TUT accuracy | InitialTUT = TopUp% × ExcessProfit | €1 |
| BR-006 | Final TUT accuracy | FinalTUT = MAX(InitialTUT + AddTUT - QDMTT, 0) | €1 |
| BR-007 | Ownership % ≤ 100% | SUM(ownership per CE) ≤ 100% | - |
| BR-008 | Percentages 0-1 | All percentages between 0 and 1 | - |
| BR-009 | Fiscal year valid | EndDate > StartDate | - |
| BR-010 | Message timestamp | Timestamp ≤ Current time | - |
| BR-011 | Jurisdiction count match | Section1Count = Section3Count | - |
| BR-012 | Safe harbour switch-off | If SH elected, no Section 3 data | - |
| BR-013 | QDMTT offset limit | QDMTT ≤ Pre-offset TUT | - |
| BR-014 | UTPR allocation 100% | SUM(UTPR %) = 100% | 0.01% |
| BR-015 | Transition rates correct | PayrollRate, AssetRate per year | - |

### Implementing Business Rules Validation

**VBA Business Rules Module:**

```vba
Function ValidateBusinessRules() As Boolean

    Dim allPassed As Boolean
    allPassed = True

    ' BR-001: ETR Calculation
    Dim jurisdiction As Range
    For Each jurisdiction In Sheets("Section3").Range("B5:B50")
        If jurisdiction.Value <> "" Then
            Dim globeIncome As Double
            Dim coveredTaxes As Double
            Dim reportedETR As Double
            Dim calculatedETR As Double

            globeIncome = jurisdiction.Offset(0, 10).Value
            coveredTaxes = jurisdiction.Offset(0, 11).Value
            reportedETR = jurisdiction.Offset(0, 12).Value

            If globeIncome > 0 Then
                calculatedETR = coveredTaxes / globeIncome
                If Abs(reportedETR - calculatedETR) > 0.0001 Then
                    LogError "BR-001", jurisdiction.Value, _
                        "ETR mismatch: Reported=" & reportedETR & _
                        ", Calculated=" & calculatedETR
                    allPassed = False
                End If
            End If
        End If
    Next jurisdiction

    ' BR-007: Ownership ≤ 100%
    Dim entity As Range
    For Each entity In Sheets("Section1").Range("B20:B200")
        If entity.Value <> "" Then
            Dim ownership As Double
            ownership = entity.Offset(0, 5).Value
            If ownership > 1 Then
                LogError "BR-007", entity.Value, _
                    "Ownership exceeds 100%: " & (ownership * 100) & "%"
                allPassed = False
            End If
        End If
    Next entity

    ' Additional rules...

    ValidateBusinessRules = allPassed

End Function
```

---

## 6.3.5 OECD Status Message Schema

### Purpose

The OECD GIR Status Message Schema provides a standardised format for tax authorities to report validation errors back to the filing entity or sending competent authority.

### Status Message Structure

```xml
<stm:GIRStatusMessage xmlns:stm="urn:oecd:ties:girstm:v1">
    <stm:MessageHeader>
        <stm:SendingCompetentAuthority>DE</stm:SendingCompetentAuthority>
        <stm:ReceivingCompetentAuthority>GB</stm:ReceivingCompetentAuthority>
        <stm:MessageRefId>DE2025STM000001</stm:MessageRefId>
        <stm:OriginalMessageRefId>GB2024GIR000001</stm:OriginalMessageRefId>
        <stm:Timestamp>2025-07-15T10:30:00Z</stm:Timestamp>
    </stm:MessageHeader>

    <stm:ValidationResult>
        <stm:Status>PartiallyAccepted</stm:Status>
        <stm:FileError>
            <stm:ErrorCode>FE001</stm:ErrorCode>
            <stm:ErrorDescription>File-level validation warning</stm:ErrorDescription>
        </stm:FileError>
        <stm:RecordError>
            <stm:RecordRefId>CE-DE-001</stm:RecordRefId>
            <stm:ErrorCode>RE015</stm:ErrorCode>
            <stm:ErrorDescription>ETR calculation discrepancy</stm:ErrorDescription>
            <stm:ElementPath>/JurisdictionSection/GloBEComputations/ETRComputation/ETR</stm:ElementPath>
        </stm:RecordError>
    </stm:ValidationResult>
</stm:GIRStatusMessage>
```

### Status Values

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| Accepted | File passed all validations | None |
| PartiallyAccepted | File accepted with warnings | Review warnings |
| Rejected | File rejected due to errors | Correct and resubmit |

### Error Code Categories

**File-Level Errors (FE):**

| Code | Description | Resolution |
|------|-------------|------------|
| FE001 | Invalid file structure | Regenerate XML |
| FE002 | Missing required header elements | Add missing elements |
| FE003 | Invalid namespace declaration | Correct namespace |
| FE004 | Schema validation failed | Run schema validation |
| FE005 | Encoding error | Use UTF-8 encoding |

**Record-Level Errors (RE):**

| Code | Description | Resolution |
|------|-------------|------------|
| RE001 | Invalid TIN format | Verify TIN with jurisdiction |
| RE002 | Invalid country code | Use ISO 3166-1 alpha-2 |
| RE003 | Missing mandatory field | Complete all required fields |
| RE004 | Invalid date format | Use YYYY-MM-DD |
| RE005 | Invalid percentage format | Use decimal 0-1 |
| RE010 | ETR calculation error | Recalculate ETR |
| RE011 | SBIE calculation error | Recalculate SBIE |
| RE012 | Top-up Tax calculation error | Recalculate Top-up Tax |
| RE015 | Cross-reference failure | Verify entity references |
| RE020 | Safe harbour eligibility error | Review safe harbour criteria |

---

## 6.3.6 Validation Workflow

### Complete Validation Procedure

```
GIR XML Validation Workflow:
│
├── Step 1: Pre-Validation Preparation
│   ├── Ensure Calculator validation complete
│   ├── Obtain latest OECD schema files
│   ├── Configure validation tools
│   └── Create backup of XML file
│
├── Step 2: Well-Formedness Check
│   ├── Run xmllint --noout
│   ├── Fix any syntax errors
│   ├── Re-run until clean
│   └── Document results
│
├── Step 3: Schema Validation
│   ├── Run xmllint --schema
│   ├── Review all errors
│   ├── Categorise by severity
│   ├── Fix errors in Calculator
│   ├── Regenerate XML
│   ├── Re-validate
│   └── Repeat until clean
│
├── Step 4: Business Rules Validation
│   ├── Run Calculator BR checks
│   ├── Verify mathematical accuracy
│   ├── Check cross-section consistency
│   ├── Validate reference integrity
│   ├── Correct any issues
│   └── Regenerate if needed
│
├── Step 5: Tax Authority Pre-Validation
│   ├── Use portal test environment
│   ├── Upload XML for validation
│   ├── Review any additional errors
│   ├── Address jurisdiction-specific issues
│   └── Document validation results
│
└── Step 6: Final Approval
    ├── Document all validation passes
    ├── Obtain sign-off
    ├── Archive validation evidence
    └── Proceed to submission
```

### Validation Log Template

**Tab:** `Validation Log`

| # | Date/Time | Validation Type | Tool | Result | Errors | Resolution | Validated By |
|---|-----------|----------------|------|--------|--------|------------|--------------|
| 1 | 2025-06-15 10:30 | Well-formedness | xmllint | FAIL | 2 | Fixed tags | [Name] |
| 2 | 2025-06-15 10:45 | Well-formedness | xmllint | PASS | 0 | N/A | [Name] |
| 3 | 2025-06-15 11:00 | Schema | xmllint | FAIL | 5 | Regenerated | [Name] |
| 4 | 2025-06-15 14:00 | Schema | xmllint | PASS | 0 | N/A | [Name] |
| 5 | 2025-06-15 14:30 | Business Rules | Calculator | PASS | 0 | N/A | [Name] |
| 6 | 2025-06-16 09:00 | Pre-validation | HMRC Portal | PASS | 0 | N/A | [Name] |

---

## 6.3.7 Jurisdiction-Specific Validation

### UK (HMRC) Requirements

```
UK Additional Validation:
├── Government Gateway credentials required
├── Test environment available
├── UK-specific business rules apply
├── Multinational Top-up Tax (MTT) alignment
└── Domestic Top-up Tax (DTT) checks
```

### EU Member States

```
EU Additional Validation:
├── National tax authority portals
├── EU Directive 2022/2523 alignment
├── Domestic legislation variations
├── Language requirements (some jurisdictions)
└── Additional domestic disclosures
```

### Other Major Jurisdictions

| Jurisdiction | Portal | Additional Requirements |
|--------------|--------|------------------------|
| Australia | ATO Online | BEPS notification |
| Canada | CRA My Business Account | French/English option |
| Japan | e-Tax | Japanese character support |
| Singapore | IRAS myTax Portal | GST registration link |
| South Korea | HomeTax | Korean language option |
| Switzerland | Cantonal coordination | Canton-specific requirements |

---

## 6.3.8 Automated Validation Scripts

### Batch Validation Script (Bash)

```bash
#!/bin/bash
# GIR XML Batch Validation Script

XML_FILE=$1
XSD_FILE="GIR_v1.0.xsd"
LOG_FILE="validation_log_$(date +%Y%m%d_%H%M%S).txt"

echo "GIR XML Validation Report" > $LOG_FILE
echo "=========================" >> $LOG_FILE
echo "File: $XML_FILE" >> $LOG_FILE
echo "Date: $(date)" >> $LOG_FILE
echo "" >> $LOG_FILE

# Step 1: Well-formedness
echo "Step 1: Well-formedness Check" >> $LOG_FILE
WELLFORMED=$(xmllint --noout $XML_FILE 2>&1)
if [ $? -eq 0 ]; then
    echo "  Result: PASSED" >> $LOG_FILE
else
    echo "  Result: FAILED" >> $LOG_FILE
    echo "  Errors: $WELLFORMED" >> $LOG_FILE
    exit 1
fi

# Step 2: Schema Validation
echo "" >> $LOG_FILE
echo "Step 2: Schema Validation" >> $LOG_FILE
SCHEMA_RESULT=$(xmllint --schema $XSD_FILE $XML_FILE --noout 2>&1)
if [ $? -eq 0 ]; then
    echo "  Result: PASSED" >> $LOG_FILE
else
    echo "  Result: FAILED" >> $LOG_FILE
    echo "  Errors:" >> $LOG_FILE
    echo "$SCHEMA_RESULT" >> $LOG_FILE
    exit 1
fi

echo "" >> $LOG_FILE
echo "Validation Complete: ALL CHECKS PASSED" >> $LOG_FILE

cat $LOG_FILE
```

### PowerShell Validation Script

```powershell
# GIR XML Validation Script (PowerShell)

param(
    [Parameter(Mandatory=$true)]
    [string]$XmlFile,

    [string]$XsdFile = "GIR_v1.0.xsd"
)

function Validate-GirXml {
    $results = @{
        WellFormed = $false
        SchemaValid = $false
        Errors = @()
    }

    # Well-formedness check
    try {
        $xml = [xml](Get-Content $XmlFile)
        $results.WellFormed = $true
        Write-Host "Well-formedness: PASSED" -ForegroundColor Green
    }
    catch {
        $results.Errors += "Well-formedness: $($_.Exception.Message)"
        Write-Host "Well-formedness: FAILED" -ForegroundColor Red
        return $results
    }

    # Schema validation
    try {
        $settings = New-Object System.Xml.XmlReaderSettings
        $settings.Schemas.Add($null, $XsdFile) | Out-Null
        $settings.ValidationType = [System.Xml.ValidationType]::Schema
        $settings.ValidationFlags = `
            [System.Xml.Schema.XmlSchemaValidationFlags]::ProcessIdentityConstraints -bor `
            [System.Xml.Schema.XmlSchemaValidationFlags]::ReportValidationWarnings

        $validationErrors = @()
        $settings.add_ValidationEventHandler({
            param($sender, $e)
            $validationErrors += $e.Message
        })

        $reader = [System.Xml.XmlReader]::Create($XmlFile, $settings)
        while ($reader.Read()) { }
        $reader.Close()

        if ($validationErrors.Count -eq 0) {
            $results.SchemaValid = $true
            Write-Host "Schema validation: PASSED" -ForegroundColor Green
        }
        else {
            $results.Errors += $validationErrors
            Write-Host "Schema validation: FAILED" -ForegroundColor Red
        }
    }
    catch {
        $results.Errors += "Schema validation: $($_.Exception.Message)"
    }

    return $results
}

$results = Validate-GirXml
if ($results.Errors.Count -gt 0) {
    Write-Host "`nErrors found:" -ForegroundColor Yellow
    $results.Errors | ForEach-Object { Write-Host "  - $_" }
}
```

---

## 6.3.9 Validation Checklist

Use this comprehensive checklist before submission:

**Well-Formedness (Level 1):**

| # | Check Item | Status |
|---|------------|--------|
| 1 | XML declaration present (UTF-8) | ☐ |
| 2 | Single root element | ☐ |
| 3 | All tags properly closed | ☐ |
| 4 | No mismatched tags | ☐ |
| 5 | Reserved characters escaped | ☐ |
| 6 | Attribute values in quotes | ☐ |
| 7 | xmllint --noout passes | ☐ |

**Schema Validation (Level 2):**

| # | Check Item | Status |
|---|------------|--------|
| 8 | Using correct schema version (v1.0) | ☐ |
| 9 | All required elements present | ☐ |
| 10 | Element sequence correct | ☐ |
| 11 | Data types valid | ☐ |
| 12 | Namespace declarations correct | ☐ |
| 13 | Percentages as decimals (0-1) | ☐ |
| 14 | Dates in ISO format (YYYY-MM-DD) | ☐ |
| 15 | Currency codes on monetary elements | ☐ |
| 16 | xmllint --schema passes | ☐ |

**Business Rules (Level 3):**

| # | Check Item | Status |
|---|------------|--------|
| 17 | ETR calculations accurate | ☐ |
| 18 | SBIE calculations accurate | ☐ |
| 19 | Top-up Tax calculations accurate | ☐ |
| 20 | Cross-section totals match | ☐ |
| 21 | Entity references valid | ☐ |
| 22 | Ownership percentages valid | ☐ |
| 23 | Safe harbour logic correct | ☐ |
| 24 | Allocation totals 100% | ☐ |

**Pre-Submission:**

| # | Check Item | Status |
|---|------------|--------|
| 25 | Tax authority test validation passed | ☐ |
| 26 | Validation log documented | ☐ |
| 27 | All errors resolved | ☐ |
| 28 | Sign-off obtained | ☐ |
| 29 | Backup copy created | ☐ |

---

## 6.3.10 Key Takeaways

### Validation Best Practices

1. **Validate Early and Often**
   - Run validation after each significant change
   - Don't wait until final generation
   - Catch errors before they compound

2. **Use Multiple Tools**
   - Different tools may catch different issues
   - Cross-validate with xmllint and GUI tool
   - Use tax authority pre-validation if available

3. **Understand Error Messages**
   - Schema errors indicate structural issues
   - Business rule errors indicate logic issues
   - Address root cause, not symptoms

4. **Document Everything**
   - Keep validation logs
   - Record error resolution steps
   - Maintain audit trail

5. **Test Before Production**
   - Use tax authority test environments
   - Validate with dummy data first
   - Confirm portal acceptance before deadline

---

## Section Summary

XML validation is a multi-level process essential for successful GIR submission. Key requirements include:

- **Three Validation Levels:** Well-formedness, Schema, Business Rules
- **Primary Tools:** xmllint, XMLSpy, Calculator built-in checks
- **Status Message Schema:** OECD standard for error reporting (July 2025)
- **Common Errors:** Data type issues, missing elements, calculation discrepancies
- **Jurisdiction Requirements:** Additional local validation may apply

Thorough validation before submission prevents rejection and filing delays.

---

## Navigation

**Previous:** [Section 6.2: Excel-to-XML Conversion](Section_06_02_Excel_to_XML_Conversion.md)

**Next:** [Section 6.4: Filing Procedures by Jurisdiction](Section_06_04_Filing_Procedures_by_Jurisdiction.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
