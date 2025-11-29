# Section 6: XML Generation and Validation

## 6.1 Understanding the OECD XML Schema

### Introduction

The OECD has developed a standardised XML Schema to facilitate both the domestic filing and international exchange of GloBE Information Return (GIR) data. Published in January 2025 alongside the updated GIR template, this schema provides a common electronic format that ensures consistency across jurisdictions and enables automated processing by tax authorities.

Understanding the XML schema structure is essential for successful GIR submission, as errors in schema compliance are the most common cause of file rejection. This section provides a comprehensive guide to the OECD GIR XML Schema architecture, data types, and structural requirements.

**Learning Objectives:**
- Understand the hierarchical structure of the GIR XML Schema
- Identify mandatory and optional elements at each level
- Apply correct data types and formatting requirements
- Navigate the relationship between GIR paper template and XML structure
- Prepare for schema-compliant XML generation

---

### 6.1.1 Schema Overview and Purpose

#### Dual Purpose Design

The GIR XML Schema serves two primary purposes:

```
GIR XML Schema Purposes:
│
├── Domestic Filing
│   ├── Filing with local tax authority
│   ├── Submission via jurisdiction's portal
│   ├── Local validation rules may apply
│   └── Additional domestic elements permitted
│
└── International Exchange
    ├── Exchange between Competent Authorities
    ├── Standardised format for interoperability
    ├── Multilateral exchange agreements (MCAA)
    └── Status message response framework
```

#### Schema Publication History

| Date | Publication | Key Content |
|------|-------------|-------------|
| July 2023 | Initial GIR Template | Paper-based template structure |
| July 2024 | Draft XML Schema | Public consultation |
| January 2025 | Final XML Schema | Schema and User Guide |
| January 2025 | GIR MCAA | Exchange agreement framework |
| July 2025 | Status Message Schema | Error reporting framework |

---

### 6.1.2 Document Structure Hierarchy

#### Top-Level Architecture

The GIR XML document follows a strict hierarchical structure:

```
GIR XML Document Structure:

<?xml version="1.0" encoding="UTF-8"?>
<globe:GIR_OECD xmlns:globe="urn:oecd:ties:gir:v1"
               xmlns:stf="urn:oecd:ties:gircommontypes:v1"
               version="1.0">
    │
    ├── <globe:MessageHeader>
    │   ├── SendingCompetentAuthority
    │   ├── ReceivingCompetentAuthority
    │   ├── MessageType
    │   ├── MessageRefId
    │   ├── MessageTypeIndic
    │   ├── ReportingPeriod
    │   └── Timestamp
    │
    └── <globe:GIRBody>
        ├── <globe:FilingInfo>
        │   ├── FilingConstituentEntity
        │   ├── MNEGroup
        │   ├── AccountingInfo
        │   └── ReportingFiscalYear
        │
        ├── <globe:GeneralSection> (optional)
        │   ├── Corporate structure overview
        │   └── Recipient jurisdiction indicators
        │
        ├── <globe:Summary> (optional, repeatable)
        │   ├── JurisdictionSummary
        │   ├── ETRRange
        │   └── TopUpTaxRange
        │
        ├── <globe:JurisdictionSection> (optional, repeatable)
        │   ├── JurisdictionInfo
        │   ├── SafeHarbourElections
        │   ├── GloBEComputations
        │   └── TopUpTaxAllocation
        │
        └── <globe:CorporateStructure>
            ├── UPE
            ├── ConstituentEntities
            ├── Subgroups
            └── Excluded Entities
</globe:GIR_OECD>
```

---

### 6.1.3 MessageHeader Element

#### Structure and Requirements

The MessageHeader contains metadata about the GIR transmission:

```xml
<globe:MessageHeader>
    <globe:SendingCompetentAuthority>GB</globe:SendingCompetentAuthority>
    <globe:ReceivingCompetentAuthority>DE</globe:ReceivingCompetentAuthority>
    <globe:MessageType>GIR</globe:MessageType>
    <globe:MessageRefId>GB2024GIR000001</globe:MessageRefId>
    <globe:MessageTypeIndic>GIR</globe:MessageTypeIndic>
    <globe:ReportingPeriod>2024-12-31</globe:ReportingPeriod>
    <globe:Timestamp>2025-06-30T14:30:00Z</globe:Timestamp>
</globe:MessageHeader>
```

#### Element Specifications

| Element | Type | Required | Description |
|---------|------|----------|-------------|
| SendingCompetentAuthority | ISO 3166-1 alpha-2 | Yes | Jurisdiction sending the GIR |
| ReceivingCompetentAuthority | ISO 3166-1 alpha-2 | Conditional | For exchange only |
| MessageType | String | Yes | Fixed value: "GIR" |
| MessageRefId | String (max 200) | Yes | Unique identifier per message |
| MessageTypeIndic | Enumeration | Yes | Fixed value: "GIR" |
| ReportingPeriod | Date (YYYY-MM-DD) | Yes | Last day of fiscal year |
| Timestamp | DateTime (ISO 8601) | Yes | File creation timestamp |

#### MessageRefId Guidelines

```
MessageRefId Format Recommendations:
├── Must be unique per filing jurisdiction
├── Suggested format: [JurisdCode][Year][Type][Sequence]
├── Example: GB2024GIR000001
├── Maximum length: 200 characters
├── Alphanumeric characters only recommended
└── Used for tracking and amendments
```

---

### 6.1.4 GIRBody Element

#### FilingInfo Section

The FilingInfo element identifies the filing entity and MNE Group:

```xml
<globe:FilingInfo>
    <globe:FilingConstituentEntity>
        <globe:Name>GlobalCo Holdings plc</globe:Name>
        <globe:TIN issuedBy="GB">12345678</globe:TIN>
        <globe:ResCountryCode>GB</globe:ResCountryCode>
        <globe:Address>
            <globe:AddressFree>100 Main Street, London, EC1A 1BB</globe:AddressFree>
        </globe:Address>
        <globe:FilingRole>FCE</globe:FilingRole>
    </globe:FilingConstituentEntity>

    <globe:MNEGroup>
        <globe:Name>GlobalCo Group</globe:Name>
        <globe:UPEJurisdiction>GB</globe:UPEJurisdiction>
    </globe:MNEGroup>

    <globe:AccountingInfo>
        <globe:AccountingStandard>IFRS</globe:AccountingStandard>
        <globe:FunctionalCurrency>EUR</globe:FunctionalCurrency>
    </globe:AccountingInfo>

    <globe:ReportingFiscalYear>
        <globe:StartDate>2024-01-01</globe:StartDate>
        <globe:EndDate>2024-12-31</globe:EndDate>
    </globe:ReportingFiscalYear>
</globe:FilingInfo>
```

#### FilingInfo Element Specifications

| Element | Sub-Element | Type | Required |
|---------|-------------|------|----------|
| FilingConstituentEntity | Name | String (max 200) | Yes |
| | TIN | TIN Type | Yes |
| | ResCountryCode | ISO 3166-1 | Yes |
| | Address | Address Type | Yes |
| | FilingRole | Enumeration | Yes |
| MNEGroup | Name | String (max 200) | Yes |
| | UPEJurisdiction | ISO 3166-1 | Yes |
| AccountingInfo | AccountingStandard | Enumeration | Yes |
| | FunctionalCurrency | ISO 4217 | Yes |
| ReportingFiscalYear | StartDate | Date | Yes |
| | EndDate | Date | Yes |

#### FilingRole Enumeration

| Value | Description |
|-------|-------------|
| FCE | Filing Constituent Entity (default) |
| UPE | Ultimate Parent Entity filing |
| DFE | Designated Filing Entity |
| LFE | Local Filing Entity |

#### AccountingStandard Enumeration

| Value | Description |
|-------|-------------|
| IFRS | International Financial Reporting Standards |
| US_GAAP | United States GAAP |
| OTHER | Other authorised standard |

---

### 6.1.5 JurisdictionSection Element

#### Structure Overview

The JurisdictionSection is the most detailed element, containing Sections 2 and 3 data:

```xml
<globe:JurisdictionSection>
    <globe:JurisdictionCode>DE</globe:JurisdictionCode>

    <!-- Section 2: Safe Harbours -->
    <globe:SafeHarbours>
        <globe:TransitionalCbCRSH>
            <globe:Elected>true</globe:Elected>
            <globe:QualifyingTest>SimplifiedETR</globe:QualifyingTest>
            <globe:SimplifiedETR>0.2500</globe:SimplifiedETR>
        </globe:TransitionalCbCRSH>
    </globe:SafeHarbours>

    <!-- Section 3: GloBE Computations (if safe harbour not elected) -->
    <globe:GloBEComputations>
        <globe:ETRComputation>
            <globe:GloBEIncome>43500000.00</globe:GloBEIncome>
            <globe:AdjustedCoveredTaxes>12875000.00</globe:AdjustedCoveredTaxes>
            <globe:ETR>0.2960</globe:ETR>
        </globe:ETRComputation>

        <globe:SBIEComputation>
            <globe:PayrollCarveOut>3797500.00</globe:PayrollCarveOut>
            <globe:TangibleAssetCarveOut>9796800.00</globe:TangibleAssetCarveOut>
            <globe:TotalSBIE>13594300.00</globe:TotalSBIE>
        </globe:SBIEComputation>

        <globe:TopUpTaxComputation>
            <globe:ExcessProfit>29905700.00</globe:ExcessProfit>
            <globe:TopUpTaxPercentage>0.0000</globe:TopUpTaxPercentage>
            <globe:InitialTopUpTax>0.00</globe:InitialTopUpTax>
            <globe:QDMTTOffset>0.00</globe:QDMTTOffset>
            <globe:FinalTopUpTax>0.00</globe:FinalTopUpTax>
        </globe:TopUpTaxComputation>
    </globe:GloBEComputations>
</globe:JurisdictionSection>
```

#### Conditional Logic

```
JurisdictionSection Conditional Requirements:
│
├── If TransitionalCbCRSH.Elected = true
│   └── GloBEComputations: NOT REQUIRED
│
├── If QDMTTSH.Elected = true
│   └── GloBEComputations: NOT REQUIRED (Switch-off rule)
│
├── If Exclusion.Type = "NO_CES" or "EXCLUDED_ONLY"
│   └── JurisdictionSection: NOT REQUIRED
│
└── Otherwise
    └── Full GloBEComputations: REQUIRED
```

---

### 6.1.6 CorporateStructure Element

#### Constituent Entity Information

```xml
<globe:CorporateStructure>
    <globe:UPE>
        <globe:Name>GlobalCo Holdings plc</globe:Name>
        <globe:TIN issuedBy="GB">12345678</globe:TIN>
        <globe:ResCountryCode>GB</globe:ResCountryCode>
        <globe:GloBEStatus>UPE</globe:GloBEStatus>
    </globe:UPE>

    <globe:ConstituentEntity>
        <globe:EntityId>CE-DE-001</globe:EntityId>
        <globe:Name>GlobalCo Germany GmbH</globe:Name>
        <globe:TIN issuedBy="DE">DE123456789</globe:TIN>
        <globe:ResCountryCode>DE</globe:ResCountryCode>
        <globe:GloBEStatus>CE</globe:GloBEStatus>
        <globe:OwnershipInfo>
            <globe:ParentEntityId>UPE-GB-001</globe:ParentEntityId>
            <globe:OwnershipPercentage>1.0000</globe:OwnershipPercentage>
        </globe:OwnershipInfo>
    </globe:ConstituentEntity>

    <!-- Additional CEs... -->
</globe:CorporateStructure>
```

#### GloBE Status Codes

| Code | Description | XML Value |
|------|-------------|-----------|
| UPE | Ultimate Parent Entity | UPE |
| POPE | Partially-Owned Parent Entity | POPE |
| IPE | Intermediate Parent Entity | IPE |
| CE | Standard Constituent Entity | CE |
| PE | Permanent Establishment | PE |
| FTE | Flow-Through Entity | FTE |
| JV | Joint Venture | JV |
| JVSUB | JV Subsidiary | JVSUB |
| EXCL | Excluded Entity | EXCL |
| GOV | Governmental Entity | GOV |
| INTORG | International Organisation | INTORG |
| NPO | Non-Profit Organisation | NPO |
| PENSION | Pension Fund | PENSION |
| INVFUND | Investment Fund | INVFUND |

---

### 6.1.7 Data Types and Formatting

#### Standard Data Types

The schema defines specific data types for consistent formatting:

**Monetary Amount Type:**

```xml
<!-- MonetaryAmount_Type -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>

Specifications:
├── Decimal with 2 decimal places
├── Currency code attribute (ISO 4217)
├── No thousand separators
├── Negative values permitted (prefix with -)
└── Maximum: 999,999,999,999,999.99
```

**Percentage Type:**

```xml
<!-- Percentage_Type -->
<globe:ETR>0.2960</globe:ETR>
<globe:OwnershipPercentage>1.0000</globe:OwnershipPercentage>

Specifications:
├── Decimal format (0 to 1 representing 0% to 100%)
├── Up to 4 decimal places
├── 0.25 = 25%
├── 0.9876 = 98.76%
├── Maximum value: 1.0000
└── Minimum value: 0.0000
```

**TIN Type:**

```xml
<!-- TIN_Type -->
<globe:TIN issuedBy="GB">12345678</globe:TIN>

Specifications:
├── String value (jurisdiction-specific format)
├── issuedBy attribute (ISO 3166-1 alpha-2)
├── NOTIN value permitted if no TIN assigned
├── Maximum length: 200 characters
└── Alphanumeric characters
```

**Date Type:**

```xml
<!-- Date_Type -->
<globe:EndDate>2024-12-31</globe:EndDate>

Specifications:
├── ISO 8601 format: YYYY-MM-DD
├── No time component
└── Valid calendar date required
```

**DateTime Type:**

```xml
<!-- DateTime_Type -->
<globe:Timestamp>2025-06-30T14:30:00Z</globe:Timestamp>

Specifications:
├── ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
├── UTC timezone indicator (Z)
├── 24-hour time format
└── Seconds required
```

---

### 6.1.8 Namespace and Schema References

#### XML Namespace Declarations

```xml
<?xml version="1.0" encoding="UTF-8"?>
<globe:GIR_OECD
    xmlns:globe="urn:oecd:ties:gir:v1"
    xmlns:stf="urn:oecd:ties:gircommontypes:v1"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="urn:oecd:ties:gir:v1 GIR_v1.0.xsd"
    version="1.0">
```

#### Namespace Definitions

| Prefix | Namespace URI | Purpose |
|--------|---------------|---------|
| globe | urn:oecd:ties:gir:v1 | Primary GIR elements |
| stf | urn:oecd:ties:gircommontypes:v1 | Common type definitions |
| xsi | http://www.w3.org/2001/XMLSchema-instance | Schema validation |

#### Schema Version

| Attribute | Value | Notes |
|-----------|-------|-------|
| version | 1.0 | January 2025 release |

---

### 6.1.9 Cardinality and Optionality

#### Element Occurrence Rules

| Element | Min | Max | Notes |
|---------|-----|-----|-------|
| MessageHeader | 1 | 1 | Always required |
| GIRBody | 1 | 1 | Always required |
| FilingInfo | 1 | 1 | Always required |
| GeneralSection | 0 | 1 | Optional overview |
| Summary | 0 | unbounded | One per jurisdiction (optional) |
| JurisdictionSection | 0 | unbounded | One per jurisdiction with data |
| CorporateStructure | 1 | 1 | Always required |
| ConstituentEntity | 1 | unbounded | At least one CE required |
| UPE | 1 | unbounded | At least one UPE (may have multiple POPEs) |

#### Conditional Requirements Summary

```
Conditional Element Requirements:
│
├── JurisdictionSection
│   ├── Required IF: ETR < 15% AND no safe harbour
│   ├── Required IF: QDMTT paid (for offset reporting)
│   └── Not Required IF: Safe harbour OR exclusion
│
├── GloBEComputations
│   ├── Required IF: No safe harbour elected
│   └── Not Required IF: Safe harbour switch-off applies
│
├── SafeHarbours
│   ├── Required IF: Safe harbour claimed
│   └── Not Required IF: Full calculations performed
│
└── TopUpTaxAllocation
    ├── Required IF: FinalTopUpTax > 0
    └── Not Required IF: No Top-up Tax due
```

---

### 6.1.10 Mapping GIR Template to XML Structure

#### Section-by-Section Mapping

| GIR Template Section | XML Element Path |
|---------------------|------------------|
| **Section 1.1** - FCE Information | /GIRBody/FilingInfo/FilingConstituentEntity |
| **Section 1.2** - UPE Information | /GIRBody/CorporateStructure/UPE |
| **Section 1.3** - Corporate Structure | /GIRBody/CorporateStructure/ConstituentEntity |
| **Section 1.4** - Summary | /GIRBody/Summary |
| **Section 2.1** - Transitional CbCR SH | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH |
| **Section 2.2** - QDMTT SH | /JurisdictionSection/SafeHarbours/QDMTTSH |
| **Section 3.1** - ETR Computation | /JurisdictionSection/GloBEComputations/ETRComputation |
| **Section 3.2** - SBIE | /JurisdictionSection/GloBEComputations/SBIEComputation |
| **Section 3.3** - Top-Up Tax | /JurisdictionSection/GloBEComputations/TopUpTaxComputation |
| **Section 3.4** - Allocation | /JurisdictionSection/TopUpTaxAllocation |

#### Calculator to XML Field Mapping

| Calculator Tab | Calculator Field | XML Element |
|---------------|-----------------|-------------|
| Section 1 | FCE_Name (B5) | FilingConstituentEntity/Name |
| Section 1 | FCE_TIN (C5) | FilingConstituentEntity/TIN |
| Section 1 | UPE_Jurisdiction (F5) | MNEGroup/UPEJurisdiction |
| Section 3.1 | GloBE_Income (AK22) | ETRComputation/GloBEIncome |
| Section 3.1 | Covered_Taxes (X20) | ETRComputation/AdjustedCoveredTaxes |
| Section 3.1 | ETR (E5) | ETRComputation/ETR |
| Section 3.2 | Payroll_Carveout (R20) | SBIEComputation/PayrollCarveOut |
| Section 3.2 | Asset_Carveout (AE20) | SBIEComputation/TangibleAssetCarveOut |
| Section 3.3 | Final_TUT (Q5) | TopUpTaxComputation/FinalTopUpTax |

---

### 6.1.11 Common Schema Compliance Issues

#### Issue 1: Invalid Percentage Format

**Problem:** Entering percentage as whole number instead of decimal.

```xml
<!-- INCORRECT -->
<globe:ETR>25.00</globe:ETR>  <!-- Interpreted as 2500%! -->

<!-- CORRECT -->
<globe:ETR>0.2500</globe:ETR>  <!-- 25.00% -->
```

**Resolution:** Always use decimal format (0-1) for percentages.

---

#### Issue 2: Missing Mandatory Elements

**Problem:** Omitting required elements from file.

```xml
<!-- INCORRECT - Missing TIN -->
<globe:FilingConstituentEntity>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:ResCountryCode>GB</globe:ResCountryCode>
</globe:FilingConstituentEntity>

<!-- CORRECT -->
<globe:FilingConstituentEntity>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:TIN issuedBy="GB">12345678</globe:TIN>
    <globe:ResCountryCode>GB</globe:ResCountryCode>
</globe:FilingConstituentEntity>
```

**Resolution:** Validate against schema before submission; use NOTIN if no TIN issued.

---

#### Issue 3: Incorrect Date Format

**Problem:** Using local date formats instead of ISO 8601.

```xml
<!-- INCORRECT -->
<globe:EndDate>31/12/2024</globe:EndDate>
<globe:EndDate>12-31-2024</globe:EndDate>

<!-- CORRECT -->
<globe:EndDate>2024-12-31</globe:EndDate>
```

**Resolution:** Always use YYYY-MM-DD format.

---

#### Issue 4: Currency Code Missing

**Problem:** Monetary amounts without currency attribute.

```xml
<!-- INCORRECT -->
<globe:GloBEIncome>43500000.00</globe:GloBEIncome>

<!-- CORRECT -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

**Resolution:** Include currencyCode attribute on all monetary elements.

---

#### Issue 5: Invalid Jurisdiction Code

**Problem:** Using non-standard country codes.

```xml
<!-- INCORRECT -->
<globe:ResCountryCode>UK</globe:ResCountryCode>
<globe:ResCountryCode>GER</globe:ResCountryCode>

<!-- CORRECT -->
<globe:ResCountryCode>GB</globe:ResCountryCode>
<globe:ResCountryCode>DE</globe:ResCountryCode>
```

**Resolution:** Use ISO 3166-1 alpha-2 codes only.

---

### 6.1.12 Schema Validation Tools

#### Validation Approaches

```
XML Schema Validation Methods:
│
├── Built-in Calculator Validation
│   ├── Pre-generation schema check
│   ├── Element completeness validation
│   └── Data type verification
│
├── Standalone XML Validators
│   ├── XMLSpy (Altova)
│   ├── Oxygen XML Editor
│   ├── Visual Studio Code with XML extension
│   └── Online validators (xmlvalidation.com)
│
├── Command Line Tools
│   ├── xmllint (Linux/Mac)
│   ├── msxsl (Windows)
│   └── Saxon
│
└── Tax Authority Portals
    ├── Pre-submission validation
    ├── Test environment submission
    └── Production validation
```

#### Validation Command Example

```bash
# Using xmllint (Linux/Mac)
xmllint --schema GIR_v1.0.xsd myfile.xml --noout

# Expected output if valid:
# myfile.xml validates

# Expected output if invalid:
# myfile.xml:45: element ETR: Schemas validity error
```

---

### 6.1.13 Key Takeaways

#### Schema Implementation Summary

1. **Structure Follows Template**
   - XML hierarchy mirrors GIR paper template
   - Same three-section logic (MNE Info, Safe Harbours, Computations)
   - Calculator field mapping is direct

2. **Data Types are Critical**
   - Percentages: Decimal 0-1 (not whole numbers)
   - Dates: ISO 8601 (YYYY-MM-DD)
   - Monetary: Two decimal places with currency code
   - Country codes: ISO 3166-1 alpha-2

3. **Conditional Logic Matters**
   - Safe harbour elections eliminate computation requirements
   - Switch-off rules reduce XML content
   - Exclusions can eliminate entire jurisdiction sections

4. **Validate Before Submit**
   - Schema validation catches structural errors
   - Use multiple validation tools
   - Tax authority pre-submission validation recommended

5. **Namespace Awareness**
   - Correct namespace declarations required
   - Version attribute must match schema release
   - Schema location helps validation tools

---

## Section Summary

The OECD GIR XML Schema provides a standardised format for electronic GIR filing and exchange. Key characteristics include:

- **Hierarchical Structure:** MessageHeader → GIRBody → FilingInfo/JurisdictionSection/CorporateStructure
- **Five Main Elements:** FilingInfo, GeneralSection, Summary, JurisdictionSection, CorporateStructure
- **Strict Data Types:** Percentage (0-1), Date (YYYY-MM-DD), Currency (with code attribute)
- **Conditional Requirements:** Safe harbour elections reduce required elements
- **Validation Essential:** Schema compliance required for acceptance

Understanding this schema structure is foundational for generating compliant XML files, covered in Section 6.2.

---

## Navigation

**Previous:** [Section 5.5: Calculator Validation and Reconciliation](Section_05_05_Calculator_Validation_and_Reconciliation.md)

**Next:** [Section 6.2: Generating Compliant XML Files](Section_06_02_Generating_Compliant_XML_Files.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
