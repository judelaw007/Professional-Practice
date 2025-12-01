# Section 13.3: XML Tools and Validators

## PART 4: ESSENTIAL RESOURCES

### Official Resource Directory

---

## Introduction

This section provides comprehensive guidance on XML validation tools and software for GloBE Information Return (GIR) preparation and submission. Accurate XML generation and validation is critical for successful GIR filing—rejected submissions delay compliance and may trigger penalties.

> **Key Requirement:** All GIR files must conform to the OECD January 2025 XML Schema. Pre-submission validation against this schema is essential.

---

## XML Validation Overview

### Why XML Validation Matters

| Issue | Consequence | Prevention |
|-------|-------------|------------|
| **Schema Non-Compliance** | File rejection by tax authority | Validate against OECD XSD before submission |
| **Missing Mandatory Elements** | Validation failure | Use element checklist |
| **Incorrect Data Types** | Processing errors | Test with sample data |
| **Character Encoding Errors** | Garbled data transmission | Ensure UTF-8 encoding |
| **Namespace Issues** | Complete file rejection | Verify namespace declarations |

### Validation Levels

| Level | Description | Checkpoint |
|-------|-------------|------------|
| **Well-Formedness** | XML syntax correct (tags closed, proper nesting) | Parser check |
| **Schema Validation** | Conforms to OECD XSD structure | XSD validation |
| **Business Rules** | Data logic correct (calculations, references) | Application validation |
| **Jurisdiction-Specific** | Meets local authority requirements | Portal validation |

---

## OECD Official XML Resources

### GIR XML Schema (January 2025)

| Attribute | Details |
|-----------|---------|
| **Document Title** | GloBE Information Return (Pillar Two) XML Schema: User Guide for Tax Administrations |
| **Publication Date** | 15 January 2025 |
| **Schema Version** | January 2025 |
| **Character Encoding** | UTF-8 |

**Direct Links:**
- **User Guide (PDF):** https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html
- **XML Schema Package (ZIP):** Available via above link

**Schema Contents:**

| File | Purpose |
|------|---------|
| `GIR_Schema.xsd` | Main schema definition |
| `GIR_Types.xsd` | Data type definitions |
| `GIR_Enumerations.xsd` | Enumerated values (country codes, etc.) |
| `isocbctypes_v1.0.xsd` | ISO standard types |

**Technical Specifications:**

| Specification | Requirement |
|--------------|-------------|
| **XML Version** | 1.0 |
| **Encoding** | UTF-8 |
| **Namespace** | As defined in schema |
| **Schema Language** | W3C XML Schema (XSD) 1.0 |

---

### GIR Status Message XML Schema (July 2025)

| Attribute | Details |
|-----------|---------|
| **Document Title** | GloBE Information Return (Pillar Two) Status Message XML Schema: User Guide for Tax Administrations |
| **Publication Date** | 30 July 2025 |
| **Purpose** | Standardised error reporting between tax authorities |

**Direct Link:** https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html

**Key Features:**
- File-level error reporting
- Record-level error reporting
- Agreed validation rules
- Status codes (Accepted, Rejected, Accepted with Errors)

**Validation Rules Categories:**

| Category | Description |
|----------|-------------|
| **File Errors** | Structure/format issues affecting entire file |
| **Record Errors** | Issues with specific data records |
| **Mandatory Element Errors** | Required elements missing |
| **Data Type Errors** | Values don't match expected format |
| **Reference Errors** | Invalid cross-references within file |

---

### OECD Validation Rule Types

| Rule Type | Description | Example |
|-----------|-------------|---------|
| **Validation** | MUST be present for ALL records; automated check possible | Entity identifier |
| **Mandatory** | Required when GloBE Rules require it; context-dependent | International Shipping Income (only if applicable) |
| **Optional (Mandatory)** | Optional element required in specific circumstances | Safe harbour elections |
| **Optional** | Truly optional; may be omitted | Additional comments |

---

## Free Online XML Validators

### General Purpose Validators

These tools validate XML against any XSD schema, including the OECD GIR schema:

#### 1. FreeFormatter.com

| Attribute | Details |
|-----------|---------|
| **URL** | https://www.freeformatter.com/xml-validator-xsd.html |
| **Cost** | Free |
| **Privacy** | Files processed on server |
| **Features** | Validates XML against XSD; detailed error messages |

**How to Use:**
1. Download OECD GIR XSD schema files
2. Paste or upload your GIR XML file
3. Paste or upload the XSD schema
4. Click "Validate XML against XSD Schema"
5. Review results for errors

**Limitations:**
- File size limits may apply
- Multiple schema files may require manual handling
- No business rule validation

---

#### 2. Liquid Technologies Online Validator

| Attribute | Details |
|-----------|---------|
| **URL** | https://www.liquid-technologies.com/online-xsd-validator |
| **Cost** | Free (online); paid desktop versions |
| **Privacy** | Files processed on server |
| **Features** | XSD validation; line-by-line error reporting |

**How to Use:**
1. Upload XML file and XSD schema
2. Run validation
3. Review error locations and messages

**Desktop Version (Liquid Studio):**
- Free Community Edition available
- Advanced XML editing features
- Visual schema viewer

---

#### 3. CoreFiling XML Schema Validator

| Attribute | Details |
|-----------|---------|
| **URL** | https://www.corefiling.com/opensource/schemavalidate/ |
| **Cost** | Free |
| **Background** | CoreFiling specialises in XML/XBRL for tax authorities |
| **Features** | Schema validation; open-source foundation |

**Relevance to Tax Reporting:**
CoreFiling has extensive experience with tax authority XML formats, including XBRL for financial reporting.

---

#### 4. ValidateXML.com

| Attribute | Details |
|-----------|---------|
| **URL** | https://validatexml.com/ |
| **Cost** | Free |
| **Privacy** | Browser-based (local processing) |
| **Features** | XSD/DTD validation; namespace awareness; privacy-focused |

**Advantages:**
- Local validation (no server upload)
- Detailed error reporting
- Multi-schema support

---

#### 5. W3Schools XML Validator

| Attribute | Details |
|-----------|---------|
| **URL** | https://www.w3schools.com/xml/xml_validator.asp |
| **Cost** | Free |
| **Features** | Basic well-formedness and syntax checking |

**Use Case:** Quick syntax check before full schema validation

---

### Validator Comparison Matrix

| Tool | XSD Validation | Privacy | Error Detail | Multi-Schema | Cost |
|------|---------------|---------|--------------|--------------|------|
| FreeFormatter.com | ✓ | Server | High | Manual | Free |
| Liquid Technologies | ✓ | Server | High | ✓ | Free/Paid |
| CoreFiling | ✓ | Server | Medium | ✓ | Free |
| ValidateXML.com | ✓ | Local | High | ✓ | Free |
| W3Schools | Basic | Server | Low | ✗ | Free |

---

## Desktop XML Validation Tools

### Professional XML Editors

#### 1. Altova XMLSpy

| Attribute | Details |
|-----------|---------|
| **Vendor** | Altova |
| **URL** | https://www.altova.com/xmlspy-xml-editor |
| **Cost** | Commercial (Professional: ~$399; Enterprise: ~$799) |
| **Trial** | 30-day free trial |
| **Platform** | Windows |

**Key Features:**
- Comprehensive XSD validation
- Smart Fix: Automatic error correction suggestions
- Visual schema editor
- Multi-document validation
- Schema caching for performance
- Graphical XML editing

**Validation Process:**
1. Open GIR XML file in XMLSpy
2. Assign OECD XSD schema (XML → Assign Schema)
3. Press F8 to validate
4. Review errors in Messages window
5. Use Smart Fix to correct issues

**Tax Reporting Experience:**
Altova has extensive experience with tax authority XML formats, including their dedicated CbC Reporting Solution.

---

#### 2. Oxygen XML Editor

| Attribute | Details |
|-----------|---------|
| **Vendor** | Syncro Soft |
| **URL** | https://www.oxygenxml.com/ |
| **Cost** | Commercial (~$198 - $688 depending on edition) |
| **Trial** | 30-day free trial |
| **Platform** | Windows, macOS, Linux |

**Key Features:**
- Comprehensive XML validation
- Schema-aware editing
- Visual schema designer
- Batch validation
- Cross-platform support

**Use for GIR:**
- Import OECD XSD schema
- Create/edit GIR XML
- Validate against schema
- Generate documentation

---

#### 3. Microsoft Visual Studio (with XML Tools)

| Attribute | Details |
|-----------|---------|
| **Vendor** | Microsoft |
| **URL** | https://visualstudio.microsoft.com/ |
| **Cost** | Free (Community Edition) to Commercial |
| **Platform** | Windows (primarily) |

**XML Validation Features:**
- Built-in XML editor with IntelliSense
- XSD schema validation
- Error highlighting
- Schema-based auto-completion

---

#### 4. Notepad++ with XML Tools Plugin

| Attribute | Details |
|-----------|---------|
| **Base Software** | Notepad++ (free, open source) |
| **Plugin** | XML Tools |
| **URL** | https://notepad-plus-plus.org/ |
| **Cost** | Free |
| **Platform** | Windows |

**Features:**
- XML syntax highlighting
- Well-formedness checking
- XSD validation (via plugin)
- XPath evaluation

**Installation:**
1. Install Notepad++
2. Plugins → Plugin Admin → Search "XML Tools"
3. Install and restart
4. Use Plugins → XML Tools → Validate

---

### Desktop Tools Comparison

| Tool | Platform | Cost | XSD Validation | Smart Fix | Tax Experience |
|------|----------|------|----------------|-----------|----------------|
| Altova XMLSpy | Windows | $399-$799 | ✓ | ✓ | Extensive |
| Oxygen XML | Cross-platform | $198-$688 | ✓ | Partial | Moderate |
| Visual Studio | Windows | Free-Commercial | ✓ | ✗ | Limited |
| Notepad++ | Windows | Free | ✓ (plugin) | ✗ | Limited |

---

## Command-Line Validation Tools

### For Technical Users and Automation

#### 1. xmllint (libxml2)

| Attribute | Details |
|-----------|---------|
| **Part of** | libxml2 library |
| **Cost** | Free, open source |
| **Platform** | Linux, macOS, Windows (via WSL or ports) |

**Installation:**
- **Linux (Ubuntu/Debian):** `sudo apt-get install libxml2-utils`
- **macOS:** Pre-installed or via Homebrew
- **Windows:** Available via Cygwin, WSL, or standalone builds

**Validation Command:**
```bash
xmllint --schema GIR_Schema.xsd your_gir_file.xml --noout
```

**Options:**
- `--schema <xsd>`: Specify XSD schema
- `--noout`: Suppress XML output (show only errors)
- `--valid`: Validate against DTD (not typically used for GIR)

**Automation Example:**
```bash
#!/bin/bash
# Validate all GIR files in directory
for file in *.xml; do
    echo "Validating: $file"
    xmllint --schema GIR_Schema.xsd "$file" --noout
done
```

---

#### 2. Apache Xerces

| Attribute | Details |
|-----------|---------|
| **Vendor** | Apache Software Foundation |
| **URL** | https://xerces.apache.org/ |
| **Cost** | Free, open source |
| **Platform** | Cross-platform (Java, C++) |

**Java Version (Xerces-J):**
- Full XSD 1.0 implementation
- Widely used in enterprise applications
- Can be integrated into custom validation tools

**Command-Line Usage (Java):**
```bash
java -cp xerces.jar:xml-apis.jar dom.Counter -v -s your_gir_file.xml
```

---

#### 3. Saxon (XSLT/XQuery Processor)

| Attribute | Details |
|-----------|---------|
| **Vendor** | Saxonica |
| **URL** | https://www.saxonica.com/ |
| **Cost** | Free (Home Edition) to Commercial |
| **Platform** | Cross-platform (Java) |

**XSD Validation:**
Saxon can validate XML against XSD schemas and provides detailed error messages.

---

### Command-Line Tools Comparison

| Tool | Schema Support | Integration | Learning Curve | Automation |
|------|---------------|-------------|----------------|------------|
| xmllint | XSD 1.0 | Shell scripts | Low | Excellent |
| Xerces | Full XSD | Java/.NET | Medium | Excellent |
| Saxon | XSD + Schematron | Java | Medium | Good |

---

## Jurisdiction-Specific Validation

### United Kingdom (HMRC)

| Attribute | Details |
|-----------|---------|
| **Portal** | HMRC Developer Hub |
| **Test Environment** | https://developer.service.hmrc.gov.uk/ |
| **API Guide** | https://developer.service.hmrc.gov.uk/guides/pillar2-service-guide/ |
| **Test Endpoint** | https://test-api.service.hmrc.gov.uk/organisations/pillar-two/ |

**Testing Process:**
1. Register on HMRC Developer Hub
2. Create sandbox test user and organisation
3. Generate test GIR XML file
4. Submit to test API endpoint
5. Review validation response

**HMRC Pillar 2 API Features:**
- GIR submission endpoint
- Overseas Return Notification endpoint
- UK Tax Return submission
- Error response handling

---

### Germany (BZSt)

| Attribute | Details |
|-----------|---------|
| **Portal** | BZSt Online Portal |
| **Validation** | ELMA5 interface |
| **Schema** | OECD schema with German extensions |

**Process:**
- Use BZSt-approved software or WTS CbCR-2-XML tool
- Validate against ELMA structure requirements
- Submit via electronic interface

---

### Australia (ATO)

| Attribute | Details |
|-----------|---------|
| **Portal** | ATO Business Portal |
| **Status** | GIR forms under development (as of October 2025) |
| **Contact** | Pillar2Project@ato.gov.au |

**Anticipated Process:**
- XML submission via ATO portal
- Schema aligned with OECD January 2025
- Validation feedback via portal

---

### Other Jurisdictions

Most jurisdictions accepting XML GIR files will use the OECD January 2025 schema with potential local extensions. Check jurisdiction-specific guidance (Section 13.1) for validation requirements.

---

## Commercial Pillar Two Software Solutions

### Enterprise GIR Compliance Platforms

These platforms provide end-to-end GIR preparation, validation, and filing:

#### 1. Deloitte Pillar Two Agent

| Attribute | Details |
|-----------|---------|
| **Vendor** | Deloitte |
| **URL** | https://www.deloitte.com/global/en/services/tax/services/tech-powered-compliance.html |
| **Deployment** | Cloud-based; co-sourcing/outsourcing model |

**Capabilities:**
- Data collection and aggregation
- Top-up tax calculations
- GIR XML generation
- QDMTT filing support
- Multi-jurisdiction compliance

**Access:** Available through Deloitte tax engagement

---

#### 2. PwC Pillar Two Engine (Beacon)

| Attribute | Details |
|-----------|---------|
| **Vendor** | PwC |
| **URL** | https://www.pwc.com/gx/en/services/tax/pillar-two-readiness.html |
| **Platform** | Cloud-based (Beacon platform) |

**Capabilities:**
- GIR XML generation
- QDMTT filing in local formats
- Reporting discrepancy identification
- Rule library updated by international tax specialists
- Provision, compliance, and modelling

**Output Formats:**
- GIR XML (OECD schema)
- Local tax forms in required formats

---

#### 3. CSC Corptax GMT

| Attribute | Details |
|-----------|---------|
| **Vendor** | CSC (Corporation Service Company) |
| **URL** | https://go.corptax.com/eye-on-pillar-2.html |
| **Platform** | Cloud-based |

**Capabilities:**
- QDMTT, notification, and GIR tracking across 60+ jurisdictions
- Schema-aligned XML generation
- Audit-ready reporting
- Ongoing schema updates throughout 2025
- Automated difference detection for schema changes

**Key Feature:** Broad jurisdictional support with unique deadline/format tracking

---

#### 4. Thomson Reuters ONESOURCE

| Attribute | Details |
|-----------|---------|
| **Vendor** | Thomson Reuters |
| **URL** | https://tax.thomsonreuters.com/onesource/ |
| **Platform** | Cloud-based (ONESOURCE+) |

**Capabilities:**
- Global minimum tax calculations
- Tax provision integration
- Compliance workflow automation
- Multi-jurisdiction support

---

#### 5. Longview Tax (insightsoftware)

| Attribute | Details |
|-----------|---------|
| **Vendor** | insightsoftware (acquired Longview) |
| **URL** | https://insightsoftware.com/ |
| **Platform** | Cloud/On-premise |

**Capabilities:**
- Tax provision and compliance
- Global tax data management
- Pillar Two calculations
- Reporting and analytics

---

### Commercial Software Comparison

| Vendor | GIR XML | QDMTT | Validation | Jurisdictions | Deployment |
|--------|---------|-------|------------|---------------|------------|
| Deloitte P2 Agent | ✓ | ✓ | Built-in | Multi | Cloud |
| PwC Beacon | ✓ | ✓ | Built-in | Multi | Cloud |
| CSC Corptax GMT | ✓ | ✓ | Built-in | 60+ | Cloud |
| Thomson Reuters | ✓ | ✓ | Built-in | Multi | Cloud |
| Longview Tax | ✓ | ✓ | Built-in | Multi | Cloud/On-prem |

---

## CbCR XML Validation (Reference)

### Relevance to GIR

Country-by-Country Reporting (CbCR) XML validation is relevant because:
1. **Transitional CbCR Safe Harbour** uses CbCR data
2. **Similar XML structure** and validation concepts
3. **Experience transfer** from CbCR to GIR compliance

### CbCR Validation Tools

#### Altova CbC Reporting Solution

| Attribute | Details |
|-----------|---------|
| **URL** | https://www.altova.com/cbc-reporting-solution |
| **Cost** | Commercial |
| **Jurisdictions** | Germany (BZSt), UK (HMRC), Switzerland, Singapore, and others |

**Features:**
- Built-in CbCR data validation
- Error flagging at multiple steps
- Automatic XML generation
- Country-specific validation rules

---

#### WTS CbCR-2-XML

| Attribute | Details |
|-----------|---------|
| **Vendor** | WTS Germany |
| **URL** | https://wts.com/de-en/tax-tools/cbcr-2-xml |
| **Focus** | Germany (BZSt via ELMA5) |

**Features:**
- XML structure per OECD requirements
- ELMA5 interface integration
- Real-time validation status
- Direct transmission to BZSt

---

#### TPcbc

| Attribute | Details |
|-----------|---------|
| **URL** | https://tax-model.com/taxsuite/tpcbc/ |
| **Jurisdictions** | 20+ OECD Member States |
| **Special Feature** | Direct filing to Dutch authorities |

**Validation:**
- Missing data detection
- Format validation
- Schema compliance

---

## XML Generation Best Practices

### Pre-Validation Checklist

| # | Check | Tool | Status |
|---|-------|------|--------|
| 1 | XML well-formed (syntax correct) | Any XML editor | ☐ |
| 2 | Encoding is UTF-8 | Text editor check | ☐ |
| 3 | Schema namespace declared correctly | Manual inspection | ☐ |
| 4 | Validates against OECD XSD | XSD validator | ☐ |
| 5 | All mandatory elements present | Schema documentation | ☐ |
| 6 | Data types correct (dates, numbers) | Validation tool | ☐ |
| 7 | Cross-references valid (entity IDs) | Business rule check | ☐ |
| 8 | Currency codes valid (ISO 4217) | Reference check | ☐ |
| 9 | Country codes valid (ISO 3166) | Reference check | ☐ |
| 10 | File size within limits | File properties | ☐ |

---

### Common XML Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| **Unexpected element** | Element not in schema or wrong location | Check schema structure; correct element placement |
| **Missing required element** | Mandatory element omitted | Add required element with valid value |
| **Invalid value for type** | Wrong data format (e.g., text in number field) | Correct data type; check format requirements |
| **Encoding error** | Non-UTF-8 characters | Convert file to UTF-8; remove invalid characters |
| **Namespace mismatch** | Incorrect or missing namespace | Verify namespace declaration matches schema |
| **Schema not found** | XSD file path incorrect | Correct schema location; ensure file accessible |
| **Duplicate element** | Element appears more than allowed | Remove duplicate; check maxOccurs in schema |
| **Empty required element** | Mandatory element has no value | Provide valid value |

---

### XML File Structure Reference

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GIR xmlns="urn:oecd:ties:gir:v1"
     xmlns:stf="urn:oecd:ties:stf:v4"
     xmlns:iso="urn:oecd:ties:isogirtypes:v1"
     version="1.0">

    <!-- Filing Information -->
    <FilingInfo>
        <!-- Reporting period, filing entity details -->
    </FilingInfo>

    <!-- Section 1: MNE Group Information -->
    <GeneralSection>
        <!-- UPE details, constituent entities, corporate structure -->
    </GeneralSection>

    <!-- Summary Section -->
    <Summary>
        <!-- High-level metrics, ETR ranges -->
    </Summary>

    <!-- Section 2 & 3: Jurisdictional Data -->
    <JurisdictionSection>
        <!-- Safe harbours, GloBE computations by jurisdiction -->
    </JurisdictionSection>

</GIR>
```

---

## Validation Workflow

### Recommended Process

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIR XML VALIDATION WORKFLOW                   │
└─────────────────────────────────────────────────────────────────┘

Step 1: PREPARATION
├── Download OECD January 2025 XSD schema package
├── Extract schema files to working directory
└── Ensure GIR XML file uses UTF-8 encoding

Step 2: WELL-FORMEDNESS CHECK
├── Open XML in editor (Notepad++, XMLSpy, etc.)
├── Check for syntax errors (unclosed tags, etc.)
└── Resolve any parsing errors

Step 3: SCHEMA VALIDATION
├── Load XSD schema into validation tool
├── Validate GIR XML against schema
├── Document all errors
└── Correct errors iteratively

Step 4: BUSINESS RULE VALIDATION
├── Verify calculation accuracy
├── Check cross-references (entity IDs, etc.)
├── Validate safe harbour elections
└── Confirm ETR/Top-up Tax calculations

Step 5: JURISDICTION-SPECIFIC VALIDATION
├── Check local authority requirements
├── Test in sandbox environment (if available)
└── Verify file format/naming conventions

Step 6: FINAL REVIEW
├── Complete validation checklist
├── Archive validated file with timestamp
└── Document validation results
└── Proceed to submission
```

---

## Testing Environments

### Available Test Environments

| Jurisdiction | Test Environment | Access |
|--------------|------------------|--------|
| **UK (HMRC)** | Developer Hub Sandbox | Register at developer.service.hmrc.gov.uk |
| **Germany (BZSt)** | Test portal available | Via BZSt registration |
| **Netherlands** | Pending | Check belastingdienst.nl |
| **Australia (ATO)** | Under development | Contact Pillar2Project@ato.gov.au |
| **Ireland** | ROS test environment | Via ROS registration |

### Test Environment Best Practices

1. **Use realistic test data** (anonymised production structure)
2. **Test full workflow** (generation → validation → submission → response)
3. **Document test results** for audit trail
4. **Test error scenarios** to understand rejection handling
5. **Verify response handling** in your systems

---

## Troubleshooting Guide

### Validation Error Resolution

| Symptom | Possible Cause | Resolution Steps |
|---------|---------------|------------------|
| "Schema not found" | Missing or incorrect XSD path | Verify schema files downloaded and path correct |
| "Invalid namespace" | Wrong namespace in XML | Check namespace matches schema exactly |
| "Unexpected child element" | Element in wrong location | Consult schema structure; reorder elements |
| "cvc-complex-type.2.4.a" | Missing required element | Add missing element per schema |
| "cvc-datatype-valid" | Invalid data format | Check data type (date format, number format, etc.) |
| "Empty element not allowed" | Required element has no value | Provide valid value or use "NOTIN" where permitted |

### Getting Help

| Resource | Use Case |
|----------|----------|
| **OECD User Guide** | Schema structure questions |
| **Tax authority help desk** | Jurisdiction-specific validation |
| **Software vendor support** | Tool-specific issues |
| **XML/Schema forums** | General XML validation questions |
| **Stack Overflow** | Technical XML/XSD issues |

---

## Tool Selection Guide

### Selection Criteria

| Criterion | Weight | Questions to Ask |
|-----------|--------|------------------|
| **Accuracy** | High | Does it fully support OECD XSD 1.0? |
| **Ease of Use** | Medium | Can non-technical staff use it? |
| **Integration** | Medium | Does it integrate with existing systems? |
| **Cost** | Medium | What's the total cost of ownership? |
| **Support** | Medium | Is vendor support available? |
| **Updates** | High | Will it be updated for schema changes? |
| **Automation** | Medium | Can validation be automated? |

### Recommended Tools by Use Case

| Use Case | Recommended Tool(s) |
|----------|---------------------|
| **Quick one-time validation** | FreeFormatter.com, ValidateXML.com |
| **Regular validation (technical user)** | xmllint, Notepad++ with XML Tools |
| **Enterprise compliance** | Altova XMLSpy, Commercial platforms |
| **Full Pillar Two workflow** | Deloitte P2 Agent, PwC Beacon, CSC Corptax |
| **Automation/CI pipeline** | xmllint, Xerces (Java) |

---

## Resource Links Summary

### OECD Resources

| Resource | URL |
|----------|-----|
| GIR XML Schema & User Guide | https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html |
| GIR Status Message Schema | https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html |
| Pillar Two Main Page | https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/global-anti-base-erosion-model-rules-pillar-two.html |

### Free Online Validators

| Tool | URL |
|------|-----|
| FreeFormatter | https://www.freeformatter.com/xml-validator-xsd.html |
| Liquid Technologies | https://www.liquid-technologies.com/online-xsd-validator |
| CoreFiling | https://www.corefiling.com/opensource/schemavalidate/ |
| ValidateXML | https://validatexml.com/ |
| W3Schools | https://www.w3schools.com/xml/xml_validator.asp |

### Desktop Tools

| Tool | URL |
|------|-----|
| Altova XMLSpy | https://www.altova.com/xmlspy-xml-editor |
| Oxygen XML | https://www.oxygenxml.com/ |
| Notepad++ | https://notepad-plus-plus.org/ |

### Commercial Platforms

| Vendor | URL |
|--------|-----|
| Deloitte Pillar Two | https://www.deloitte.com/global/en/services/tax/services/tech-powered-compliance.html |
| PwC Pillar Two | https://www.pwc.com/gx/en/services/tax/pillar-two-readiness.html |
| CSC Corptax | https://go.corptax.com/eye-on-pillar-2.html |
| Thomson Reuters ONESOURCE | https://tax.thomsonreuters.com/onesource/ |

---

## Document Version Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial XML tools and validators guide |

---

**Next Section:** [Section 13.4: National Implementation Guidance](Section_13_04_National_Implementation_Guidance.md)

---

*XML schemas and validation tools are subject to updates. Always verify you are using the current OECD schema version (January 2025 as of this publication) and check for jurisdiction-specific requirements before filing.*
