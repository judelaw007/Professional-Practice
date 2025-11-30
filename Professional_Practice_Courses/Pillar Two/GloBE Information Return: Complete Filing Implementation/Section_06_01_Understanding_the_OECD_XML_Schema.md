# Section 6: XML Generation and Validation

## 6.1 Understanding the OECD XML Schema

### Introduction

The OECD Inclusive Framework on BEPS published the GloBE Information Return (GIR) XML Schema on **January 15, 2025**, providing a standardised electronic format for both domestic filing and international exchange of GIR data. This schema, approved by the Inclusive Framework in October 2024, enables tax administrations worldwide to process GIR submissions consistently and facilitates automatic exchange under the GIR Multilateral Competent Authority Agreement (MCAA).

Understanding the XML schema structure is essential for successful GIR submission. Schema validation errors are the most common cause of file rejection, and practitioners must be familiar with element hierarchies, data types, and formatting requirements to generate compliant files.

**Learning Objectives:**
- Navigate the hierarchical structure of the GIR XML Schema
- Identify mandatory and optional elements across schema sections
- Apply correct data types and formatting (percentages, dates, currencies)
- Map GIR paper template fields to XML element paths
- Understand the relationship between domestic filing and international exchange schemas
- Prepare for schema-compliant XML generation

---

### 6.1.1 Schema Publication and Purpose

#### Official Publication Details

| Document | Publication Date | Source |
|----------|------------------|--------|
| GIR XML Schema (ZIP) | January 15, 2025 | OECD Publishing |
| GIR XML Schema User Guide | January 15, 2025 | 170+ page PDF |
| GIR MCAA (Multilateral Agreement) | January 15, 2025 | Exchange framework |
| GIR Status Message XML Schema | July 30, 2025 | Error reporting framework |

**Official Download Links:**
- Schema and User Guide: https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html
- Status Message Schema: https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html

#### Dual Purpose Design

The GIR XML Schema serves two primary purposes:

```
GIR XML Schema Purposes:
│
├── PURPOSE 1: Domestic Filing
│   ├── Filing with local tax authority portals
│   ├── Standardised format for electronic submission
│   ├── Local validation rules may supplement schema
│   ├── Jurisdiction-specific portal requirements
│   └── Used by Filing Constituent Entities (FCEs)
│
└── PURPOSE 2: International Exchange
    ├── Automatic exchange between Competent Authorities
    ├── Under GIR MCAA or bilateral agreements
    ├── Standardised format ensures interoperability
    ├── Status Message Schema enables error reporting
    └── Exchange within 3-6 months of filing
```

**Key Insight:** While the schema was primarily designed for international exchange between tax administrations, jurisdictions are encouraged to adopt it for domestic filings to ensure consistency. The UK, Germany, France, and other major jurisdictions have confirmed adoption of the OECD schema.

---

### 6.1.2 GIR MCAA and Exchange Framework

#### Multilateral Competent Authority Agreement

The GIR MCAA, published January 15, 2025, enables automatic exchange of GIR information between participating jurisdictions without requiring bilateral negotiations.

**Current MCAA Signatories (as of September 2025):**

| Jurisdiction | Signature Date |
|--------------|----------------|
| Austria | August 6, 2024 |
| Belgium | August 6, 2024 |
| Denmark | August 6, 2024 |
| France | August 6, 2024 |
| Germany | September 30, 2025 |
| Ireland | August 6, 2024 |
| Italy | August 6, 2024 |
| Japan | August 6, 2024 |
| Korea | August 6, 2024 |
| Liechtenstein | September 30, 2025 |
| Luxembourg | August 6, 2024 |
| Netherlands | August 26, 2025 |
| New Zealand | August 6, 2024 |
| Norway | September 30, 2025 |
| Portugal | August 6, 2024 |
| Slovakia | August 6, 2024 |
| Spain | August 6, 2024 |
| United Kingdom | August 6, 2024 |

*Note: The OECD maintains updated signatory lists online. Additional jurisdictions expected to sign before first exchange deadline.*

#### Exchange Timelines

```
GIR Exchange Timeline:
│
├── Filing Deadline
│   ├── First Year: 18 months after fiscal year end
│   ├── Subsequent Years: 15 months after fiscal year end
│   └── Example: FY 2024 → June 30, 2026
│
├── Exchange Deadline (Sending CA → Receiving CA)
│   ├── First Year: 6 months after filing deadline
│   ├── Subsequent Years: 3 months after filing deadline
│   └── Example: FY 2024 → December 31, 2026 (first year)
│
└── Status Message Response
    ├── File-level errors: Immediate feedback
    ├── Record-level errors: Within processing period
    └── Enables correction and resubmission
```

---

### 6.1.3 Document Structure Hierarchy

#### Top-Level XML Architecture

The GIR XML document follows a strict hierarchical structure as defined in the User Guide:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<globe:GIR_OECD xmlns:globe="urn:oecd:ties:gir:v1"
                xmlns:stf="urn:oecd:ties:gircommontypes:v1"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="urn:oecd:ties:gir:v1 GIRMAIN_v1.0.xsd"
                version="1.0">
    │
    ├── <globe:MessageHeader>
    │   ├── SendingCompetentAuthority
    │   ├── ReceivingCompetentAuthority (for exchange)
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
        │   └── RecipientJurisdictions (for exchange)
        │
        ├── <globe:Summary> (optional, repeatable)
        │   ├── JurisdictionCode
        │   ├── ETRRange
        │   └── TopUpTaxRange
        │
        ├── <globe:JurisdictionSection> (optional, repeatable)
        │   ├── JurisdictionCode
        │   ├── SafeHarbours
        │   ├── GloBEComputations
        │   └── TopUpTaxAllocation
        │
        └── <globe:CorporateStructure>
            ├── UPE (one or more)
            ├── ConstituentEntity (one or more)
            ├── JV (optional)
            ├── JVSubsidiary (optional)
            └── ExcludedEntity (optional)
</globe:GIR_OECD>
```

#### Namespace Declarations

| Prefix | Namespace URI | Purpose |
|--------|---------------|---------|
| globe | urn:oecd:ties:gir:v1 | Primary GIR elements |
| stf | urn:oecd:ties:gircommontypes:v1 | Common type definitions (StringMin1Max200_Type, etc.) |
| xsi | http://www.w3.org/2001/XMLSchema-instance | Schema validation |

**Schema Version:** 1.0 (January 2025 release)

---

### 6.1.4 MessageHeader Element

#### Structure and Requirements

The MessageHeader contains metadata identifying the GIR transmission:

```xml
<globe:MessageHeader>
    <globe:SendingCompetentAuthority>GB</globe:SendingCompetentAuthority>
    <globe:ReceivingCompetentAuthority>DE</globe:ReceivingCompetentAuthority>
    <globe:MessageType>GIR</globe:MessageType>
    <globe:MessageRefId>GB2024GIR000001ABC</globe:MessageRefId>
    <globe:MessageTypeIndic>GIR</globe:MessageTypeIndic>
    <globe:ReportingPeriod>2024-12-31</globe:ReportingPeriod>
    <globe:Timestamp>2025-06-30T14:30:00Z</globe:Timestamp>
</globe:MessageHeader>
```

#### Element Specifications

| Element | Data Type | Required | Max Length | Description |
|---------|-----------|----------|------------|-------------|
| SendingCompetentAuthority | ISO 3166-1 alpha-2 | Yes | 2 | Jurisdiction sending the GIR |
| ReceivingCompetentAuthority | ISO 3166-1 alpha-2 | Conditional | 2 | Required for exchange only |
| MessageType | String | Yes | 50 | Fixed value: "GIR" |
| MessageRefId | String | Yes | 200 | Unique identifier per message |
| MessageTypeIndic | Enumeration | Yes | 10 | Only allowable entry: "GIR" |
| ReportingPeriod | Date (YYYY-MM-DD) | Yes | 10 | Last day of fiscal year |
| Timestamp | DateTime (ISO 8601) | Yes | 25 | UTC format: YYYY-MM-DDTHH:MM:SSZ |

#### MessageRefId Guidelines

```
MessageRefId Best Practices:
│
├── Uniqueness
│   ├── Must be unique per filing jurisdiction
│   ├── Should be unique across all filings by MNE Group
│   └── Used for amendment tracking and audit trail
│
├── Format Recommendations
│   ├── Suggested: [JurisdCode][Year][Type][Sequence][Random]
│   ├── Example: GB2024GIR000001ABC
│   ├── Maximum: 200 characters
│   └── Alphanumeric characters recommended
│
├── Practical Examples
│   ├── First filing: GB2024GIR000001INIT
│   ├── Correction: GB2024GIR000001CORR01
│   └── Amendment: GB2024GIR000001AMD01
│
└── Avoid
    ├── Special characters (may cause encoding issues)
    ├── Spaces (not permitted)
    └── Predictable sequences (security consideration)
```

---

### 6.1.5 FilingInfo Section

#### Structure Overview

The FilingInfo element identifies the filing entity, MNE Group, accounting standards, and fiscal year:

```xml
<globe:FilingInfo>
    <globe:FilingConstituentEntity>
        <globe:Name>GlobalCo Holdings plc</globe:Name>
        <globe:TIN issuedBy="GB">12345678</globe:TIN>
        <globe:ResCountryCode>GB</globe:ResCountryCode>
        <globe:Address>
            <globe:AddressFree>100 Main Street, London, EC1A 1BB, United Kingdom</globe:AddressFree>
        </globe:Address>
        <globe:FilingRole>UPE</globe:FilingRole>
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

#### Element Specifications

| Element | Sub-Element | Data Type | Required | Description |
|---------|-------------|-----------|----------|-------------|
| FilingConstituentEntity | Name | StringMin1Max200_Type | Yes | Full legal name (1-200 chars) |
| | TIN | TIN_Type | Yes | Tax ID with issuedBy attribute |
| | ResCountryCode | ISO 3166-1 alpha-2 | Yes | Residence jurisdiction |
| | Address | Address_Type | Yes | AddressFree or structured |
| | FilingRole | Enumeration | Yes | UPE, DFE, FCE, or LFE |
| MNEGroup | Name | StringMin1Max200_Type | Yes | Group name |
| | UPEJurisdiction | ISO 3166-1 alpha-2 | Yes | UPE residence jurisdiction |
| AccountingInfo | AccountingStandard | Enumeration | Yes | IFRS, US_GAAP, or OTHER |
| | FunctionalCurrency | ISO 4217 | Yes | 3-letter currency code |
| ReportingFiscalYear | StartDate | Date | Yes | YYYY-MM-DD format |
| | EndDate | Date | Yes | YYYY-MM-DD format |

#### FilingRole Enumeration Values

| Value | Description | When to Use |
|-------|-------------|-------------|
| UPE | Ultimate Parent Entity | UPE filing directly |
| DFE | Designated Filing Entity | Appointed entity filing on behalf of group |
| FCE | Filing Constituent Entity | Standard constituent entity filing locally |
| LFE | Local Filing Entity | Entity meeting local filing obligation |

#### AccountingStandard Enumeration Values

| Value | Description |
|-------|-------------|
| IFRS | International Financial Reporting Standards |
| US_GAAP | United States Generally Accepted Accounting Principles |
| OTHER | Other authorised accounting standard (with documentation) |

---

### 6.1.6 ID and TIN Types

#### ID Type Structure

The ID Type defines identifying information for Constituent Entities, JVs, and JV Subsidiaries. It is reused throughout the schema:

```xml
<globe:ID>
    <globe:EntityId>CE-DE-001</globe:EntityId>
    <globe:Name>GlobalCo Germany GmbH</globe:Name>
    <globe:TIN issuedBy="DE">123456789</globe:TIN>
    <globe:INType>EIN</globe:INType>
    <globe:IN>HRB 12345</globe:IN>
    <globe:ResCountryCode>DE</globe:ResCountryCode>
    <globe:Address>
        <globe:AddressFree>Hauptstrasse 1, 10115 Berlin, Germany</globe:AddressFree>
    </globe:Address>
</globe:ID>
```

#### TIN Type Specifications

The TIN Type indicates the Tax Identification Number with its issuing jurisdiction:

```xml
<!-- Standard TIN -->
<globe:TIN issuedBy="GB">12345678</globe:TIN>

<!-- No TIN Issued -->
<globe:TIN issuedBy="GB">NOTIN</globe:TIN>

<!-- Stateless Entity -->
<globe:TIN issuedBy="XX">STATELESS123</globe:TIN>
```

**TIN Type Rules:**

| Attribute/Value | Type | Required | Description |
|-----------------|------|----------|-------------|
| issuedBy | ISO 3166-1 alpha-2 | Yes | Jurisdiction issuing the TIN |
| Value | String (max 200) | Yes | TIN value or "NOTIN" if none assigned |

**Special Cases:**
- **NOTIN:** Use when the jurisdiction has not issued a TIN and no functional equivalent exists
- **Stateless Entities:** Report the TIN used for Covered Taxes in the jurisdiction where the entity was created
- **Functional Equivalent:** Where no TIN exists, use business/company registration number

#### UPE ID Type

The UPE ID Type is used specifically for Ultimate Parent Entity identification:

```xml
<globe:UPE>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:TIN issuedBy="GB">12345678</globe:TIN>
    <globe:INType>CRN</globe:INType>
    <globe:IN>12345678</globe:IN>
    <globe:ResCountryCode>GB</globe:ResCountryCode>
    <globe:Address>
        <globe:AddressFree>100 Main Street, London, EC1A 1BB</globe:AddressFree>
    </globe:Address>
    <globe:GloBEStatus>UPE</globe:GloBEStatus>
    <globe:EntityId>UPE-GB-001</globe:EntityId>
</globe:UPE>
```

---

### 6.1.7 JurisdictionSection Element

#### Structure Overview

The JurisdictionSection element contains Sections 2 and 3 data for each jurisdiction:

```xml
<globe:JurisdictionSection>
    <globe:JurisdictionCode>DE</globe:JurisdictionCode>

    <!-- Section 2: Safe Harbours and Exclusions -->
    <globe:SafeHarbours>
        <globe:TransitionalCbCRSH>
            <globe:Elected>true</globe:Elected>
            <globe:QualifyingTest>SimplifiedETR</globe:QualifyingTest>
            <globe:TestValue>0.1850</globe:TestValue>
        </globe:TransitionalCbCRSH>
    </globe:SafeHarbours>

    <!-- Section 3: GloBE Computations (if safe harbour not elected) -->
    <globe:GloBEComputations>
        <globe:ETRComputation>
            <globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
            <globe:AdjustedCoveredTaxes currencyCode="EUR">12875000.00</globe:AdjustedCoveredTaxes>
            <globe:JurisdictionalETR>0.2960</globe:JurisdictionalETR>
        </globe:ETRComputation>

        <globe:SBIEComputation>
            <globe:PayrollCarveOut currencyCode="EUR">3797500.00</globe:PayrollCarveOut>
            <globe:TangibleAssetCarveOut currencyCode="EUR">9796800.00</globe:TangibleAssetCarveOut>
            <globe:TotalSBIE currencyCode="EUR">13594300.00</globe:TotalSBIE>
        </globe:SBIEComputation>

        <globe:TopUpTaxComputation>
            <globe:ExcessProfit currencyCode="EUR">29905700.00</globe:ExcessProfit>
            <globe:TopUpTaxPercentage>0.0000</globe:TopUpTaxPercentage>
            <globe:JurisdictionalTopUpTax currencyCode="EUR">0.00</globe:JurisdictionalTopUpTax>
            <globe:QDMTTOffset currencyCode="EUR">0.00</globe:QDMTTOffset>
            <globe:FinalTopUpTax currencyCode="EUR">0.00</globe:FinalTopUpTax>
        </globe:TopUpTaxComputation>
    </globe:GloBEComputations>

    <!-- Top-Up Tax Allocation (if applicable) -->
    <globe:TopUpTaxAllocation>
        <globe:IIRAllocation>
            <globe:AllocatedAmount currencyCode="EUR">0.00</globe:AllocatedAmount>
            <globe:AllocatingEntity>UPE-GB-001</globe:AllocatingEntity>
        </globe:IIRAllocation>
    </globe:TopUpTaxAllocation>
</globe:JurisdictionSection>
```

#### Conditional Logic

```
JurisdictionSection Conditional Requirements:
│
├── SCENARIO 1: Transitional CbCR Safe Harbour Elected
│   ├── SafeHarbours element: REQUIRED
│   ├── TransitionalCbCRSH.Elected: true
│   ├── GloBEComputations: NOT REQUIRED (switch-off applies)
│   └── TopUpTaxAllocation: NOT REQUIRED
│
├── SCENARIO 2: QDMTT Safe Harbour Elected
│   ├── SafeHarbours element: REQUIRED
│   ├── QDMTTSH.Elected: true
│   ├── GloBEComputations: NOT REQUIRED (switch-off applies)
│   └── TopUpTaxAllocation: NOT REQUIRED
│
├── SCENARIO 3: Exclusion Applies
│   ├── Exclusion.Type: "NO_CES" (no constituent entities)
│   ├── JurisdictionSection: May be omitted entirely
│   └── Or minimal section with exclusion indicator
│
├── SCENARIO 4: ETR ≥ 15% (No Top-Up Tax Due)
│   ├── Full GloBEComputations: REQUIRED
│   ├── TopUpTaxComputation.FinalTopUpTax: 0.00
│   └── TopUpTaxAllocation: NOT REQUIRED
│
└── SCENARIO 5: ETR < 15% (Top-Up Tax Due)
    ├── Full GloBEComputations: REQUIRED
    ├── TopUpTaxComputation: Calculated values
    └── TopUpTaxAllocation: REQUIRED
```

---

### 6.1.8 CorporateStructure Element

#### Entity Information

The CorporateStructure element captures all entities in the MNE Group:

```xml
<globe:CorporateStructure>
    <!-- Ultimate Parent Entity -->
    <globe:UPE>
        <globe:Name>GlobalCo Holdings plc</globe:Name>
        <globe:TIN issuedBy="GB">12345678</globe:TIN>
        <globe:ResCountryCode>GB</globe:ResCountryCode>
        <globe:Address>
            <globe:AddressFree>100 Main Street, London, EC1A 1BB</globe:AddressFree>
        </globe:Address>
        <globe:GloBEStatus>UPE</globe:GloBEStatus>
        <globe:EntityId>UPE-GB-001</globe:EntityId>
    </globe:UPE>

    <!-- Constituent Entities -->
    <globe:ConstituentEntity>
        <globe:EntityId>CE-DE-001</globe:EntityId>
        <globe:Name>GlobalCo Germany GmbH</globe:Name>
        <globe:TIN issuedBy="DE">DE123456789</globe:TIN>
        <globe:ResCountryCode>DE</globe:ResCountryCode>
        <globe:Address>
            <globe:AddressFree>Hauptstrasse 1, 10115 Berlin</globe:AddressFree>
        </globe:Address>
        <globe:GloBEStatus>CE</globe:GloBEStatus>
        <globe:OwnershipInfo>
            <globe:ParentEntityId>UPE-GB-001</globe:ParentEntityId>
            <globe:OwnershipPercentage>1.0000</globe:OwnershipPercentage>
        </globe:OwnershipInfo>
    </globe:ConstituentEntity>

    <!-- Excluded Entity -->
    <globe:ExcludedEntity>
        <globe:EntityId>EXCL-GB-001</globe:EntityId>
        <globe:Name>GlobalCo Pension Fund</globe:Name>
        <globe:ResCountryCode>GB</globe:ResCountryCode>
        <globe:GloBEStatus>PENSION</globe:GloBEStatus>
        <globe:ExclusionReason>PensionFund</globe:ExclusionReason>
    </globe:ExcludedEntity>
</globe:CorporateStructure>
```

#### GloBE Status Codes

| Code | Full Name | Description |
|------|-----------|-------------|
| UPE | Ultimate Parent Entity | Top-tier entity owning/controlling the group |
| POPE | Partially-Owned Parent Entity | Parent with > 20% minority ownership |
| IPE | Intermediate Parent Entity | Entity applying IIR in ownership chain |
| CE | Constituent Entity | Standard entity included in consolidation |
| PE | Permanent Establishment | Deemed separate entity for GloBE |
| FTE | Flow-Through Entity | Tax-transparent entity |
| JV | Joint Venture | 50% or less owned, equity method |
| JVSUB | JV Subsidiary | Entity owned through a JV |
| EXCL | Excluded Entity | Generic excluded entity |
| GOV | Governmental Entity | Excluded government body |
| INTORG | International Organisation | Excluded international organisation |
| NPO | Non-Profit Organisation | Excluded charity/non-profit |
| PENSION | Pension Fund | Excluded pension fund |
| INVFUND | Investment Fund | Excluded investment fund (if UPE) |
| REITS | Real Estate Investment Trust | Excluded REIT (if UPE) |

---

### 6.1.9 Data Types and Formatting

#### Percentage Type

**CRITICAL:** Percentages must be entered as decimals between 0 and 1, NOT as whole numbers.

```xml
<!-- Percentage_Type -->
<globe:JurisdictionalETR>0.2960</globe:JurisdictionalETR>
<globe:OwnershipPercentage>1.0000</globe:OwnershipPercentage>
<globe:TopUpTaxPercentage>0.0540</globe:TopUpTaxPercentage>

Specifications:
├── Format: Decimal (0 to 1)
├── 0.00 = 0%
├── 0.25 = 25%
├── 0.9876 = 98.76%
├── 1.0000 = 100%
├── Decimal places: Up to 4
├── Maximum characters: 6 (including decimal point)
├── Minimum value: 0.0000
└── Maximum value: 1.0000
```

**Common Error Prevention:**

| Intended Value | INCORRECT Entry | CORRECT Entry |
|----------------|-----------------|---------------|
| 25% | 25.00 | 0.2500 |
| 14.5% | 14.50 | 0.1450 |
| 29.6% | 29.60 | 0.2960 |
| 100% | 100.00 | 1.0000 |

#### Monetary Amount Type

```xml
<!-- MonetaryAmount_Type -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
<globe:AdjustedCoveredTaxes currencyCode="GBP">12875000.00</globe:AdjustedCoveredTaxes>

Specifications:
├── Format: Decimal with 2 decimal places
├── Currency attribute: REQUIRED (ISO 4217)
├── No thousand separators (no commas)
├── Negative values: Permitted (prefix with -)
├── Maximum: 999999999999999.99
├── Rounding: Round to nearest full number for GIR reporting
└── Note: Use unrounded values for actual GloBE calculations
```

**Currency Code Examples:**

| Currency | ISO 4217 Code |
|----------|---------------|
| Euro | EUR |
| British Pound | GBP |
| US Dollar | USD |
| Japanese Yen | JPY |
| Swiss Franc | CHF |
| Australian Dollar | AUD |

#### Date Type

```xml
<!-- Date_Type -->
<globe:EndDate>2024-12-31</globe:EndDate>
<globe:StartDate>2024-01-01</globe:StartDate>

Specifications:
├── Format: ISO 8601 (YYYY-MM-DD)
├── No time component
├── Must be valid calendar date
├── Leading zeros required
└── Examples: 2024-01-01, 2024-12-31
```

**Common Format Errors:**

| INCORRECT | CORRECT | Issue |
|-----------|---------|-------|
| 31/12/2024 | 2024-12-31 | Wrong separator/order |
| 12-31-2024 | 2024-12-31 | US format not accepted |
| 2024/12/31 | 2024-12-31 | Wrong separator |
| 24-12-31 | 2024-12-31 | Two-digit year |

#### DateTime Type

```xml
<!-- DateTime_Type -->
<globe:Timestamp>2025-06-30T14:30:00Z</globe:Timestamp>

Specifications:
├── Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
├── T separator between date and time
├── Z suffix indicates UTC timezone
├── 24-hour time format
├── Seconds required
└── Example: 2025-06-30T09:15:00Z
```

#### Country Code Type

```xml
<!-- ISO 3166-1 alpha-2 -->
<globe:ResCountryCode>GB</globe:ResCountryCode>
<globe:SendingCompetentAuthority>DE</globe:SendingCompetentAuthority>

Specifications:
├── Format: 2-letter ISO 3166-1 alpha-2
├── Always uppercase
└── Common codes: GB (not UK), DE, FR, US, JP, AU
```

**Frequently Confused Codes:**

| Country | INCORRECT | CORRECT |
|---------|-----------|---------|
| United Kingdom | UK | GB |
| Germany | GER | DE |
| Netherlands | NL | NL (correct) |
| Switzerland | SW | CH |
| Japan | JPN | JP |
| Australia | AUS | AU |

---

### 6.1.10 Cardinality and Optionality

#### Element Occurrence Rules

| Element | Minimum | Maximum | Notes |
|---------|---------|---------|-------|
| MessageHeader | 1 | 1 | Always required |
| GIRBody | 1 | 1 | Always required |
| FilingInfo | 1 | 1 | Always required |
| GeneralSection | 0 | 1 | Optional overview |
| Summary | 0 | Unbounded | One per jurisdiction (optional) |
| JurisdictionSection | 0 | Unbounded | One per jurisdiction with data |
| CorporateStructure | 1 | 1 | Always required |
| UPE | 1 | Unbounded | At least one UPE (may have multiple POPEs) |
| ConstituentEntity | 1 | Unbounded | At least one CE required |
| JV | 0 | Unbounded | Only if JVs exist |
| JVSubsidiary | 0 | Unbounded | Only if JV subsidiaries exist |
| ExcludedEntity | 0 | Unbounded | Only if excluded entities exist |

#### Summary of Required vs Optional Elements

```
Element Requirement Overview:
│
├── ALWAYS REQUIRED
│   ├── MessageHeader (with all sub-elements)
│   ├── GIRBody
│   ├── FilingInfo (with all sub-elements)
│   ├── CorporateStructure
│   ├── At least one UPE
│   └── At least one ConstituentEntity
│
├── CONDITIONALLY REQUIRED
│   ├── ReceivingCompetentAuthority (for exchange only)
│   ├── JurisdictionSection (if ETR < 15% or QDMTT)
│   ├── GloBEComputations (if no safe harbour)
│   ├── TopUpTaxAllocation (if Top-up Tax > 0)
│   └── SafeHarbours (if safe harbour claimed)
│
└── OPTIONAL
    ├── GeneralSection
    ├── Summary (per jurisdiction)
    ├── JV
    ├── JVSubsidiary
    └── ExcludedEntity
```

---

### 6.1.11 Mapping GIR Template to XML Structure

#### Section-by-Section Mapping

| GIR Template Section | XML Element Path |
|---------------------|------------------|
| **Section 1.1** - Filing CE Information | /GIRBody/FilingInfo/FilingConstituentEntity |
| **Section 1.2** - UPE Information | /GIRBody/CorporateStructure/UPE |
| **Section 1.3** - Constituent Entities | /GIRBody/CorporateStructure/ConstituentEntity |
| **Section 1.4** - Summary by Jurisdiction | /GIRBody/Summary |
| **Section 2.1** - Transitional CbCR Safe Harbour | /JurisdictionSection/SafeHarbours/TransitionalCbCRSH |
| **Section 2.2** - QDMTT Safe Harbour | /JurisdictionSection/SafeHarbours/QDMTTSH |
| **Section 2.3** - Exclusions | /JurisdictionSection/Exclusions |
| **Section 3.1** - ETR Computation | /JurisdictionSection/GloBEComputations/ETRComputation |
| **Section 3.2** - SBIE Computation | /JurisdictionSection/GloBEComputations/SBIEComputation |
| **Section 3.3** - Top-Up Tax Computation | /JurisdictionSection/GloBEComputations/TopUpTaxComputation |
| **Section 3.4** - Top-Up Tax Allocation | /JurisdictionSection/TopUpTaxAllocation |

#### Calculator Field to XML Element Mapping

| Calculator Tab | Calculator Field | XML Element |
|---------------|-----------------|-------------|
| Section 1 | FCE_Name | FilingConstituentEntity/Name |
| Section 1 | FCE_TIN | FilingConstituentEntity/TIN |
| Section 1 | UPE_Jurisdiction | MNEGroup/UPEJurisdiction |
| Section 1 | Accounting_Standard | AccountingInfo/AccountingStandard |
| Section 1 | Functional_Currency | AccountingInfo/FunctionalCurrency |
| Section 3.1 | GloBE_Income | ETRComputation/GloBEIncome |
| Section 3.1 | Adjusted_Covered_Taxes | ETRComputation/AdjustedCoveredTaxes |
| Section 3.1 | Jurisdictional_ETR | ETRComputation/JurisdictionalETR |
| Section 3.2 | Payroll_Carveout | SBIEComputation/PayrollCarveOut |
| Section 3.2 | Asset_Carveout | SBIEComputation/TangibleAssetCarveOut |
| Section 3.2 | Total_SBIE | SBIEComputation/TotalSBIE |
| Section 3.3 | Excess_Profit | TopUpTaxComputation/ExcessProfit |
| Section 3.3 | TopUp_Tax_Percentage | TopUpTaxComputation/TopUpTaxPercentage |
| Section 3.3 | Final_TopUp_Tax | TopUpTaxComputation/FinalTopUpTax |

---

### 6.1.12 GIR Status Message Schema

#### Purpose and Structure

The GIR Status Message XML Schema, published July 30, 2025, enables Competent Authorities to report errors in received GIR files:

```
GIR Status Message Schema:
│
├── FILE-LEVEL ERRORS
│   ├── Schema validation failures
│   ├── Namespace or version errors
│   ├── Missing mandatory elements
│   ├── Malformed XML structure
│   └── Encryption/signature issues
│
└── RECORD-LEVEL ERRORS
    ├── Invalid data values
    ├── Business rule violations
    ├── Cross-reference errors
    ├── Calculation inconsistencies
    └── Missing conditional elements
```

#### Status Message Structure

```xml
<girstatus:GIRStatusMessage>
    <girstatus:MessageHeader>
        <girstatus:SendingCompetentAuthority>DE</girstatus:SendingCompetentAuthority>
        <girstatus:ReceivingCompetentAuthority>GB</girstatus:ReceivingCompetentAuthority>
        <girstatus:MessageRefId>DE2025STATUS000001</girstatus:MessageRefId>
        <girstatus:OriginalMessageRefId>GB2024GIR000001</girstatus:OriginalMessageRefId>
        <girstatus:Timestamp>2025-07-15T10:30:00Z</girstatus:Timestamp>
    </girstatus:MessageHeader>

    <girstatus:ValidationResult>
        <girstatus:Status>PartiallyAccepted</girstatus:Status>
        <girstatus:FileError>
            <girstatus:ErrorCode>FE001</girstatus:ErrorCode>
            <girstatus:ErrorMessage>Schema validation warning</girstatus:ErrorMessage>
        </girstatus:FileError>
        <girstatus:RecordError>
            <girstatus:RecordId>CE-DE-003</girstatus:RecordId>
            <girstatus:ErrorCode>RE015</girstatus:ErrorCode>
            <girstatus:ErrorMessage>Invalid ETR percentage format</girstatus:ErrorMessage>
        </girstatus:RecordError>
    </girstatus:ValidationResult>
</girstatus:GIRStatusMessage>
```

#### Status Values

| Status | Description |
|--------|-------------|
| Accepted | File processed without errors |
| PartiallyAccepted | Some records accepted, some rejected |
| Rejected | Entire file rejected due to errors |

---

### 6.1.13 Common Schema Compliance Issues

#### Issue 1: Invalid Percentage Format

**Problem:** Entering percentage as whole number instead of decimal.

```xml
<!-- INCORRECT - Interpreted as 2500%! -->
<globe:JurisdictionalETR>25.00</globe:JurisdictionalETR>

<!-- CORRECT - 25.00% -->
<globe:JurisdictionalETR>0.2500</globe:JurisdictionalETR>
```

**Resolution:** Always use decimal format (0-1) for percentages. The number 0 represents 0%, and the number 1 represents 100%.

---

#### Issue 2: Missing Currency Code Attribute

**Problem:** Monetary amounts without required currency attribute.

```xml
<!-- INCORRECT - Missing currencyCode -->
<globe:GloBEIncome>43500000.00</globe:GloBEIncome>

<!-- CORRECT - With currencyCode -->
<globe:GloBEIncome currencyCode="EUR">43500000.00</globe:GloBEIncome>
```

**Resolution:** Include currencyCode attribute on ALL monetary elements using ISO 4217 codes.

---

#### Issue 3: Invalid Country Code

**Problem:** Using non-standard or incorrect country codes.

```xml
<!-- INCORRECT -->
<globe:ResCountryCode>UK</globe:ResCountryCode>
<globe:ResCountryCode>GER</globe:ResCountryCode>

<!-- CORRECT -->
<globe:ResCountryCode>GB</globe:ResCountryCode>
<globe:ResCountryCode>DE</globe:ResCountryCode>
```

**Resolution:** Use ISO 3166-1 alpha-2 codes only. GB for United Kingdom, DE for Germany.

---

#### Issue 4: Incorrect Date Format

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

#### Issue 5: Missing Mandatory TIN

**Problem:** Omitting required TIN element.

```xml
<!-- INCORRECT - Missing TIN -->
<globe:FilingConstituentEntity>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:ResCountryCode>GB</globe:ResCountryCode>
</globe:FilingConstituentEntity>

<!-- CORRECT - With TIN -->
<globe:FilingConstituentEntity>
    <globe:Name>GlobalCo Holdings plc</globe:Name>
    <globe:TIN issuedBy="GB">12345678</globe:TIN>
    <globe:ResCountryCode>GB</globe:ResCountryCode>
</globe:FilingConstituentEntity>
```

**Resolution:** Always include TIN element. Use "NOTIN" if no TIN has been issued.

---

#### Issue 6: MessageTypeIndic Value Error

**Problem:** Using incorrect value for MessageTypeIndic.

```xml
<!-- INCORRECT -->
<globe:MessageTypeIndic>GLOBE</globe:MessageTypeIndic>
<globe:MessageTypeIndic>RETURN</globe:MessageTypeIndic>

<!-- CORRECT - Only allowable entry -->
<globe:MessageTypeIndic>GIR</globe:MessageTypeIndic>
```

**Resolution:** The only allowable entry in this field is "GIR".

---

### 6.1.14 Schema Validation Approaches

#### Validation Methods

```
XML Schema Validation Methods:
│
├── LEVEL 1: Built-in Calculator Validation
│   ├── Pre-generation schema check
│   ├── Element completeness validation
│   ├── Data type verification
│   └── Basic cross-reference checks
│
├── LEVEL 2: Standalone XML Validators
│   ├── XMLSpy (Altova) - Commercial
│   ├── Oxygen XML Editor - Commercial
│   ├── Visual Studio Code (XML extension) - Free
│   ├── Notepad++ (XML Tools plugin) - Free
│   └── Online: xmlvalidation.com, freeformatter.com
│
├── LEVEL 3: Command Line Tools
│   ├── xmllint (Linux/Mac) - Free
│   ├── msxsl (Windows) - Free
│   └── Saxon - Free/Commercial
│
└── LEVEL 4: Tax Authority Portals
    ├── Pre-submission validation
    ├── Test/sandbox environment
    └── Production environment validation
```

#### Command Line Validation Example

```bash
# Using xmllint (Linux/Mac)
xmllint --schema GIRMAIN_v1.0.xsd myfile.xml --noout

# Expected output if valid:
# myfile.xml validates

# Expected output if invalid:
# myfile.xml:45: element JurisdictionalETR: Schemas validity error :
# '25.00' is not a valid value of the atomic type 'Percentage_Type'
```

#### Recommended Validation Sequence

```
Pre-Submission Validation Sequence:
│
├── Step 1: Well-Formedness Check
│   └── Verify basic XML structure (opening/closing tags)
│
├── Step 2: Schema Validation
│   └── Validate against GIRMAIN_v1.0.xsd
│
├── Step 3: Business Rule Validation
│   └── Cross-check calculations and references
│
├── Step 4: Tax Authority Test Submission
│   └── Use sandbox/test environment if available
│
└── Step 5: Production Submission
    └── Final submission with monitoring
```

---

### 6.1.15 Key Takeaways

#### Schema Implementation Checklist

1. **Structure Follows Template**
   - XML hierarchy mirrors GIR paper template
   - Same three-section logic (MNE Info, Safe Harbours, Computations)
   - Calculator field mapping is direct and documented

2. **Data Types are Critical**
   - Percentages: Decimal 0-1 (NOT whole numbers)
   - Dates: ISO 8601 (YYYY-MM-DD)
   - Monetary: Two decimal places with currency code attribute
   - Country codes: ISO 3166-1 alpha-2 (GB not UK)
   - MessageTypeIndic: Only "GIR" is valid

3. **Conditional Logic Matters**
   - Safe harbour elections eliminate computation requirements
   - Switch-off rules reduce XML content
   - Exclusions can eliminate entire jurisdiction sections
   - TopUpTaxAllocation only required if Top-up Tax > 0

4. **Validate Before Submit**
   - Schema validation catches structural errors
   - Use multiple validation tools
   - Test in sandbox environment before production
   - Monitor for Status Message responses

5. **MCAA Awareness**
   - Understand exchange timelines (3-6 months post-filing)
   - Status Message Schema enables error feedback
   - Growing list of MCAA signatories

---

## Section Summary

The OECD GIR XML Schema (January 2025) provides a standardised electronic format for GIR filing and international exchange. Key characteristics include:

- **Dual Purpose:** Domestic filing and international exchange under GIR MCAA
- **Hierarchical Structure:** MessageHeader → GIRBody → FilingInfo/JurisdictionSection/CorporateStructure
- **Strict Data Types:** Percentage (0-1 decimal), Date (YYYY-MM-DD), Currency (with ISO 4217 code attribute)
- **170+ Page User Guide:** Comprehensive documentation available from OECD
- **Status Message Schema:** Enables structured error reporting between Competent Authorities
- **Growing MCAA Network:** 18+ jurisdictions as of September 2025

**Critical Points:**
- Percentages must be decimals (0.25 = 25%, NOT 25.00)
- Currency codes required on all monetary amounts
- Country codes use ISO 3166-1 alpha-2 (GB, not UK)
- MessageTypeIndic only accepts "GIR" as valid entry
- Schema validation essential before submission

Understanding this schema structure is foundational for generating compliant XML files, which is covered in detail in Section 6.2.

---

## Official Resources

- **GIR XML Schema and User Guide:** https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html
- **GIR Status Message Schema:** https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html
- **Updated GIR Template (January 2025):** https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html

---

## Navigation

**Previous:** [Section 5.5: Calculator Validation and Reconciliation](Section_05_05_Calculator_Validation_and_Reconciliation.md)

**Next:** [Section 6.2: Excel-to-XML Conversion](Section_06_02_Excel_to_XML_Conversion.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
