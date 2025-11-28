# Section 2: Quick Reference Overview

**Estimated Reading Time:** 45 minutes
**Pages:** 25-30

---

## Learning Objectives for This Section

By the end of this section, you will be able to:

- Describe the three-section structure of the GloBE Information Return
- Locate and download the official OECD XML schema and supporting documentation
- Identify key filing forms for your jurisdictions
- Reference a complete deadline calendar for 25+ jurisdictions
- Access the essential resources directory for immediate use

---

## 2.1 The GIR at a Glance

### Understanding the Three-Section Structure

The GloBE Information Return (GIR) is not a simple form—it is a comprehensive data submission comprising approximately **480 data points** organized into **three main sections**. Understanding this structure is essential before you begin data gathering.

**Important Note:** The GIR structure evolved from earlier OECD consultation documents (which had four sections). The current structure reflects the January 2025 OECD GIR Template.

---

### GIR Section Overview

| Section | Name | Data Points | Purpose |
|---------|------|-------------|---------|
| **Section 1** | MNE Group Information | ~50+ | Identify the filing entity, UPE, and corporate structure |
| **Section 2** | Jurisdictional Safe Harbours and Exclusions | Variable | Document safe harbour elections and excluded jurisdictions |
| **Section 3** | GloBE Computations | ~400+ | Calculate ETR, top-up tax, and allocations by jurisdiction |

---

### Section 1: MNE Group Information (~50+ Data Points)

Section 1 establishes **who you are** and **how your group is structured**. This section is filed once per GIR, regardless of how many jurisdictions you operate in.

**Section 1 Components:**

| Sub-Section | Content | Key Data Elements |
|-------------|---------|-------------------|
| **1.1 Filing Constituent Entity** | Entity submitting the GIR | Legal name, TIN, jurisdiction, address, fiscal year |
| **1.2 Ultimate Parent Entity** | Top-level parent identification | UPE name, TIN (or "NOTIN"), jurisdiction, GloBE status |
| **1.3 Corporate Structure** | All constituent entities | Entity list, ownership %, GloBE status, QIIR/UTPR indicators |
| **1.4 Summary Information** | High-level group metrics | ETR range by jurisdiction, total top-up tax |

**Critical Fields in Section 1:**

| Field | Description | Common Errors |
|-------|-------------|---------------|
| **Filing CE TIN** | Tax Identification Number of filing entity | Wrong jurisdiction TIN, missing TIN |
| **UPE GloBE Status** | Status of UPE under GloBE rules | Incorrect classification |
| **Ownership Percentage** | Ownership chain documentation | Rounding errors, missing intermediate entities |
| **QIIR/UTPR Indicators** | Which entities apply which rules | Incorrect rule assignment |

**Data Sources for Section 1:**
- Legal entity register / corporate secretarial records
- Group structure charts
- Shareholder registers
- Tax registration documents

---

### Section 2: Jurisdictional Safe Harbours and Exclusions (Variable Data Points)

Section 2 documents **where simplified reporting applies**. If you qualify for safe harbours, this section can significantly reduce your Section 3 reporting burden.

**Section 2 Components:**

| Sub-Section | Content | When Required |
|-------------|---------|---------------|
| **2.1 Safe Harbour Elections** | Transitional CbCR, QDMTT, UTPR safe harbours | When electing simplified treatment |
| **2.2 Jurisdictional Exclusions** | Jurisdictions excluded from full computation | When safe harbour tests are met |

**Safe Harbour Options:**

| Safe Harbour | Test Criteria | Effect on Reporting |
|-------------|---------------|---------------------|
| **Transitional CbCR - De Minimis** | Revenue < €10M AND Profit < €1M | Jurisdiction excluded from Section 3 |
| **Transitional CbCR - ETR Test** | Simplified ETR ≥ threshold (15%/16%/17%) | Jurisdiction excluded from Section 3 |
| **Transitional CbCR - Routine Profits** | Profit ≤ SBIE amount | Jurisdiction excluded from Section 3 |
| **QDMTT Safe Harbour** | Qualifying QDMTT in jurisdiction | Reduced IIR/UTPR calculations |

**ETR Thresholds by Fiscal Year:**

| Fiscal Year Beginning | ETR Threshold |
|----------------------|---------------|
| 2023 or 2024 | 15% |
| 2025 | 16% |
| 2026 | 17% |

**Important:** The Transitional CbCR Safe Harbour has a **"once out, always out"** rule. If you fail to qualify or choose not to apply the safe harbour in any year, you cannot use it in subsequent years for that jurisdiction.

**Data Sources for Section 2:**
- Country-by-Country Report (CbCR) data
- QDMTT calculations (if applicable)
- Safe harbour election documentation

---

### Section 3: GloBE Computations (~400+ Data Points)

Section 3 is the **substantive calculation section**. It contains approximately 400 data points, but the actual number scales with:
- Number of jurisdictions where you have operations
- Number of constituent entities in each jurisdiction
- Complexity of your GloBE calculations

**Section 3 Components:**

| Sub-Section | Content | Data Points (per jurisdiction) |
|-------------|---------|-------------------------------|
| **3.1 ETR Computation** | GloBE Income/Loss, Covered Taxes, ETR | 50-80 per jurisdiction |
| **3.2 Substance-Based Income Exclusion** | Payroll carve-out, Tangible asset carve-out | 20-30 per jurisdiction |
| **3.3 Top-Up Tax Computation** | Top-up tax percentage, Excess profit | 15-25 per jurisdiction |
| **3.4 Top-Up Tax Allocation** | IIR, UTPR, QDMTT allocation | 30-50 per jurisdiction |

**Section 3.1: ETR Computation Data**

| Data Element | Description | Source |
|-------------|-------------|--------|
| GloBE Income/Loss | Adjusted financial accounting income | Financial statements + GloBE adjustments |
| Covered Taxes | Taxes included in ETR calculation | Tax provisions + GloBE adjustments |
| Adjusted Covered Taxes | Covered Taxes after GloBE modifications | Calculated |
| ETR | Effective Tax Rate per GloBE rules | Covered Taxes ÷ GloBE Income |

**Section 3.2: Substance-Based Income Exclusion (SBIE)**

| Data Element | Description | Phase-In Rate (2024) |
|-------------|-------------|---------------------|
| Payroll Carve-Out | Eligible payroll costs × rate | 9.8% (reducing to 5%) |
| Tangible Asset Carve-Out | Eligible assets × rate | 7.8% (reducing to 5%) |
| Total SBIE | Sum of carve-outs | Calculated |

**SBIE Phase-In Schedule:**

| Fiscal Year | Payroll Rate | Tangible Asset Rate |
|------------|--------------|---------------------|
| 2024 | 9.8% | 7.8% |
| 2025 | 9.6% | 7.6% |
| 2026 | 9.4% | 7.4% |
| 2027 | 9.2% | 7.2% |
| 2028 | 9.0% | 7.0% |
| 2029 | 8.2% | 6.6% |
| 2030 | 7.4% | 6.2% |
| 2031 | 6.6% | 5.8% |
| 2032 | 5.8% | 5.4% |
| 2033+ | 5.0% | 5.0% |

**Section 3.3: Top-Up Tax Computation**

| Data Element | Formula |
|-------------|---------|
| Top-Up Tax Percentage | 15% - Jurisdictional ETR (if positive) |
| Excess Profit | GloBE Income - SBIE |
| Top-Up Tax | Excess Profit × Top-Up Tax Percentage |
| Additional Current Top-Up Tax | Adjustments from prior periods |

**Section 3.4: Top-Up Tax Allocation**

| Allocation Type | Description |
|----------------|-------------|
| IIR Allocation | Allocated to Parent Entity applying IIR |
| UTPR Allocation | Allocated to UTPR jurisdictions based on formula |
| QDMTT Offset | Reduces IIR/UTPR where QDMTT paid |

**Data Sources for Section 3:**
- Financial statements (consolidated and local)
- Tax provisions and deferred tax calculations
- Payroll records
- Fixed asset registers
- Prior year GloBE calculations
- CbCR data (for consistency checks)

---

### Data Flow: From Financial Statements to GIR

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DATA FLOW OVERVIEW                                │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FINANCIAL     │    │   TAX           │    │   HR/PAYROLL    │
│   STATEMENTS    │    │   PROVISIONS    │    │   SYSTEMS       │
│                 │    │                 │    │                 │
│ • P&L           │    │ • Current tax   │    │ • Payroll costs │
│ • Balance sheet │    │ • Deferred tax  │    │ • Headcount     │
│ • Consolidation │    │ • Tax returns   │    │ • By entity     │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         ▼                      ▼                      ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     GIR DATA POINT TRACKER                          │
│                     (~480 data points mapped to sources)            │
└─────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     GIR COMPLETION CALCULATOR                       │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │  SECTION 1   │  │  SECTION 2   │  │  SECTION 3   │              │
│  │  MNE Group   │  │  Safe        │  │  GloBE       │              │
│  │  Information │  │  Harbours    │  │  Computations│              │
│  │  (~50 pts)   │  │  (variable)  │  │  (~400 pts)  │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     XML GENERATION                                  │
│                     (OECD January 2025 Schema)                      │
└─────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     XML VALIDATION                                  │
│                     • Schema validation                             │
│                     • Business rule validation                      │
│                     • Jurisdiction-specific checks                  │
└─────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     FILING SUBMISSION                               │
│                     • Tax authority portal                          │
│                     • Confirmation receipt                          │
│                     • Audit file documentation                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### XML Schema Structure

The OECD XML schema (January 2025) organizes the GIR data into five main elements:

| XML Element | GIR Section | Description |
|------------|-------------|-------------|
| **FilingInfo** | Header | Filing CE, MNE Group, Fiscal Year identification |
| **GeneralSection** | Section 1.1-1.3 | Corporate structure information |
| **Summary** | Section 1.4 | High-level summary by jurisdiction |
| **JurisdictionSection** | Sections 2 & 3 | Safe harbours and GloBE computations |
| **CorporateStructure** | Section 1.3 | Detailed entity ownership information |

**Key XML Technical Requirements:**

| Requirement | Specification |
|-------------|---------------|
| Character Encoding | UTF-8 |
| Country Codes | ISO 3166-1 Alpha-2 (2-character) |
| Currency Codes | ISO 4217 (3-character) |
| TIN Format | Jurisdiction-specific (use "NOTIN" if none) |
| Date Format | YYYY-MM-DD |
| Decimal Precision | As specified per field |

---

## 2.2 Key Forms and Where to Find Them

### OECD Official Documentation

The following documents are essential for GIR preparation. All are available from the OECD website.

**Core Documents:**

| Document | Version | Direct Link |
|----------|---------|-------------|
| **GIR XML Schema User Guide** | January 2025 | [OECD Publication](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html) |
| **GIR XML Schema (PDF)** | January 2025 | [Direct PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/01/globe-information-return-pillar-two-xml-schema_3980638f/c594935a-en.pdf) |
| **GIR Status Message Schema** | July 2025 | [OECD Publication](https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html) |
| **GloBE Model Rules** | December 2021 | [OECD Pillar Two Portal](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/global-anti-base-erosion-model-rules-pillar-two.html) |
| **Administrative Guidance** | Consolidated 2025 | [OECD Pillar Two Portal](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/global-anti-base-erosion-model-rules-pillar-two.html) |

**Administrative Guidance Releases:**

| Release Date | Key Content |
|-------------|-------------|
| February 2023 | Initial AG on scope, computations |
| July 2023 | GIR template, safe harbours |
| December 2023 | Filing deadlines, penalty relief |
| June 2024 | Technical clarifications |
| January 2025 | Updated GIR, XML schema, MCAA |

---

### Jurisdiction-Specific Filing Forms

**United Kingdom (HMRC)**

| Form/Requirement | Purpose | Where to Access |
|-----------------|---------|-----------------|
| **GIR (XML)** | Main information return | HMRC Online Services |
| **Overseas Return Notification (ORN)** | Notify HMRC of foreign GIR filing | HMRC Online Services |
| **Self Assessment Return** | MTT/DTT liability declaration | HMRC Online Services |
| **Registration** | Register as filing entity | HMRC Pillar 2 Portal |

**UK Portal:** Access via Government Gateway → Business Tax Account → Pillar 2

---

**Germany (BZSt)**

| Form/Requirement | Purpose | Where to Access |
|-----------------|---------|-----------------|
| **Konzernspitzenanmeldung** | Group head notification | [BZSt Online Portal](https://www.bzst.de/EN/Businesses/Pillar_2/pillar_2_node.html) |
| **GIR (XML)** | Main information return | BZSt DIP Interface |
| **Minimum Tax Return** | Tax liability declaration | BZSt DIP Interface |

**German Portal:** BZSt Online-Portal (BOP) and DIP (Digitaler Posteingang) mass data interface

**Key German Deadlines:**
- Group head notification: February 28, 2025 (for FY beginning January 1, 2024)
- GIR submission: June 30, 2026 (first year)

---

**Netherlands**

| Form/Requirement | Purpose | Where to Access |
|-----------------|---------|-----------------|
| **GIR (XML)** | Main information return | Belastingdienst Portal |
| **IIR/UTPR Return** | Tax liability declaration | Belastingdienst Portal |

**Dutch Portal:** Belastingdienst (Dutch Tax Administration) business portal

---

**Australia (ATO)**

| Form/Requirement | Purpose | Where to Access |
|-----------------|---------|-----------------|
| **GIR** | Main information return | ATO Online Services |
| **Foreign Notification Form (FNF)** | Notify ATO of foreign GIR filing | ATO Online Services |
| **CGDMTR** | Combined Global and Domestic Minimum Tax Return | ATO Online Services |

**Australian Portal:** Online services for business / Online services for agents

**Australian Lodgment Structure:**
- GIR: Separate filing (OECD standard format)
- FNF + AIUTR + DMTR: Combined into CGDMTR for simplified lodgment

---

**Singapore (IRAS)**

| Form/Requirement | Purpose | Where to Access |
|-----------------|---------|-----------------|
| **GIR** | Main information return | myTax Portal |
| **GMT Return** | Global Minimum Tax return | myTax Portal |

**Singapore Portal:** IRAS myTax Portal

---

**Other Key Jurisdictions:**

| Jurisdiction | Filing Portal | Notes |
|-------------|---------------|-------|
| **France** | impots.gouv.fr | XML via mass data interface |
| **Belgium** | MyMinfin | Extended deadline to June 30, 2026 |
| **Switzerland** | OMTax | Registration by June 30, 2026 |
| **Japan** | e-Tax | IIR from April 2024; QDMTT from April 2026 |
| **South Korea** | Hometax | IIR from January 2024 |
| **Hong Kong** | eTAX | IIR/QDMTT from January 2025 |

---

### Designated Filing Entity Election Forms

If designating a DFE to file centrally, you need election documentation for each jurisdiction where constituent entities are located.

| Jurisdiction | Election Method | Timing |
|-------------|-----------------|--------|
| **UK** | Included in first GIR/ORN submission | With first filing |
| **Germany** | Group head notification | By February 28 following FY start |
| **Netherlands** | Notification to Belastingdienst | With first filing |
| **Australia** | Designated Local Entity nomination | With first filing |
| **France** | Notification to DGFiP | With first filing |

**Template Provided:** DFE Election Template Package (Word) - covers 10+ jurisdictions

---

### Amendment Forms

If you need to amend a previously filed GIR:

| Jurisdiction | Amendment Process | Deadline |
|-------------|-------------------|----------|
| **UK** | Amended GIR via HMRC portal | Within amendment window |
| **Germany** | Corrected XML via BZSt DIP | As soon as error discovered |
| **Netherlands** | Amended filing via Belastingdienst | Within statutory period |
| **Australia** | Amended GIR via ATO Online | Within amendment period |

**Template Provided:** Amendment Request Documentation (Word)

---

## 2.3 Critical Deadline Calendar

### Master Filing Deadline: June 30, 2026

For most MNE groups with a December 31, 2024 fiscal year end, the first GIR filing deadline is **June 30, 2026**.

This date is driven by:
1. **18-month rule** for first year (December 31, 2024 + 18 months = June 30, 2026)
2. **OECD Administrative Guidance** stating no filing due before June 30, 2026

---

### Complete Deadline Calendar by Jurisdiction

**For December 31, 2024 Fiscal Year End:**

| Jurisdiction | Registration Deadline | First GIR Due | Tax Return Due | Payment Due |
|-------------|----------------------|---------------|----------------|-------------|
| **United Kingdom** | June 30, 2025 | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Germany** | Feb 28, 2025 (notification) | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Netherlands** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **France** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Belgium** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Ireland** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Luxembourg** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Switzerland** | June 30, 2026 (OMTax) | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Austria** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Italy** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Spain** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Australia** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Singapore** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Japan** | N/A | Sep 30, 2025* | Sep 30, 2025* | Sep 30, 2025* |
| **South Korea** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Hong Kong** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Canada** | N/A | June 30, 2026 | June 30, 2026 | June 30, 2026 |
| **Liechtenstein** | Dec 31, 2025 | June 30, 2026 | June 30, 2026 | June 30, 2026 |

*Japan: Different fiscal year (April 1 start) - deadline 15 months after March 31, 2025 year-end

---

### Subsequent Year Deadlines

After the first year, the deadline reduces from 18 months to **15 months**.

**For December 31, 2025 Fiscal Year End:**

| Milestone | Date |
|-----------|------|
| Fiscal Year End | December 31, 2025 |
| Filing Deadline | March 31, 2027 (15 months) |

**For December 31, 2026 Fiscal Year End:**

| Milestone | Date |
|-----------|------|
| Fiscal Year End | December 31, 2026 |
| Filing Deadline | March 31, 2028 (15 months) |

---

### Non-December Year Ends

**For March 31, 2025 Fiscal Year End:**

| Jurisdiction | First GIR Due |
|-------------|---------------|
| All jurisdictions | September 30, 2026 (18 months) |

**For June 30, 2025 Fiscal Year End:**

| Jurisdiction | First GIR Due |
|-------------|---------------|
| All jurisdictions | December 31, 2026 (18 months) |

**For September 30, 2024 Fiscal Year End:**

| Jurisdiction | First GIR Due |
|-------------|---------------|
| All jurisdictions | June 30, 2026 (OECD minimum) |

Note: Even if the 18-month calculation would result in an earlier date, the OECD Administrative Guidance ensures no filing is required before June 30, 2026.

---

### Election Deadlines

Beyond the GIR filing deadline, watch for these election deadlines:

| Election | Deadline | Consequence of Missing |
|----------|----------|----------------------|
| **DFE Election** | With first GIR | Each CE must file locally |
| **Safe Harbour Election** | With first GIR | Full computation required |
| **UK Registration** | 6 months after first FY end | Late registration penalties |
| **Germany Group Head Notification** | Feb 28 following FY start | Administrative penalties |
| **Switzerland OMTax Registration** | June 30, 2026 | Filing complications |

---

### Amendment Windows

If errors are discovered after filing:

| Jurisdiction | Amendment Window | Process |
|-------------|------------------|---------|
| **UK** | Generally 4 years | Amended GIR + documentation |
| **Germany** | Until assessment final | Corrected XML submission |
| **Netherlands** | 5 years | Amended filing |
| **Australia** | Generally 4 years | Amended GIR via ATO Online |

---

### Calendar Export

**Deliverable:** Multi-Jurisdiction Deadline Calendar (Excel)

The Excel calendar included in this course provides:
- All deadlines by jurisdiction (sortable)
- Fiscal year end selector (adjusts all dates)
- iCal export for Outlook/Google Calendar
- Reminder configuration (30/60/90 days before)
- Status tracking columns

---

## 2.4 Essential Resources Directory Preview

This section provides a preview of the key resources you will need. The full Official Resource Directory (Section 13) contains 25+ jurisdictions with complete contact details.

---

### OECD Core Resources

| Resource | Description | Link |
|----------|-------------|------|
| **Pillar Two Main Portal** | Central hub for all GloBE documentation | [oecd.org/pillartwo](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/global-anti-base-erosion-model-rules-pillar-two.html) |
| **GIR XML Schema** | Official XML schema and user guide | [OECD Publication](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html) |
| **Status Message Schema** | Error reporting schema for tax authorities | [OECD Publication](https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html) |
| **GIR Reporting Requirements** | Compilation of additional requirements by jurisdiction | [OECD Compilation](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/globe-information-reporting-requirements.html) |
| **Administrative Guidance** | All AG releases (Feb 2023 - Jan 2025) | Via Pillar Two Main Portal |

---

### Government Filing Portals (Top 10 Jurisdictions)

| Jurisdiction | Portal Name | URL |
|-------------|-------------|-----|
| **United Kingdom** | HMRC Business Tax Account | [gov.uk/hmrc](https://www.gov.uk/guidance/report-pillar-2-top-up-taxes) |
| **Germany** | BZSt Online Portal | [bzst.de](https://www.bzst.de/EN/Businesses/Pillar_2/pillar_2_node.html) |
| **Netherlands** | Belastingdienst | belastingdienst.nl |
| **France** | impots.gouv.fr | impots.gouv.fr |
| **Belgium** | MyMinfin | myminfin.be |
| **Australia** | ATO Online Services | [ato.gov.au](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/in-detail/multinationals/global-and-domestic-minimum-tax) |
| **Singapore** | IRAS myTax Portal | iras.gov.sg |
| **Switzerland** | OMTax | estv.admin.ch |
| **Japan** | e-Tax | e-tax.nta.go.jp |
| **Canada** | CRA My Business Account | canada.ca/cra |

---

### XML Validation Tools

| Tool | Provider | Purpose |
|------|----------|---------|
| **OECD Schema Validator** | OECD | Official schema validation |
| **Jurisdiction Validators** | Various tax authorities | Country-specific validation |
| **Altova XMLSpy** | Altova | Commercial XML validation |
| **Oxygen XML Editor** | Syncro Soft | Commercial XML validation |
| **Free Online Validators** | Various | Basic schema checking |

**Note:** The course provides an XML Schema Validator Tool (Excel) that performs basic validation checks before submission.

---

### National Implementation Guidance

| Jurisdiction | Guidance Document | Status |
|-------------|-------------------|--------|
| **UK** | HMRC MTT/DTT Guidance Manual | Published (with updates) |
| **Germany** | BZSt FAQ and Procedures | Published |
| **Netherlands** | Belastingdienst Implementation Guidance | Published |
| **Australia** | ATO Pillar Two Guidance | Published (including PCG 2025/D3) |
| **Singapore** | IRAS GMT Implementation Guide | Published |
| **France** | DGFiP Pillar Two Instructions | Published |

---

### Third-Party Resources

| Resource | Provider | Description |
|----------|----------|-------------|
| **oecdpillars.com** | Independent | Analysis and tracking of Pillar Two developments |
| **Country Implementation Tracker** | WTS Global | Country-by-country status updates |
| **Pillar Two Country Tracker** | PwC | Implementation status by country |
| **Big 4 Publications** | Deloitte, EY, KPMG, PwC | Technical analysis and alerts |

---

### Professional Body Resources

| Organization | Resources |
|-------------|-----------|
| **CIOT (UK)** | Technical guidance, training |
| **AICPA (US)** | International tax resources |
| **CFE Tax Advisers Europe** | EU implementation analysis |
| **IFA** | Academic and practitioner resources |

---

### Help Desk Contacts (Preview)

| Jurisdiction | Contact Method | Typical Response Time |
|-------------|----------------|----------------------|
| **UK HMRC** | Online form / Phone | 5-10 business days |
| **Germany BZSt** | Email / Online form | 10-15 business days |
| **Netherlands** | Phone / Online | 5-10 business days |
| **Australia ATO** | Phone / Online services | 5-10 business days |
| **Singapore IRAS** | Email / myTax Portal | 5-10 business days |

**Full contact details including phone numbers, email addresses, and escalation procedures are provided in Section 13: Official Resource Directory.**

---

## Section 2 Summary: Quick Reference Checklist

Before proceeding, confirm you can answer these questions:

| Question | Where to Find Answer |
|----------|---------------------|
| How many sections does the GIR have? | Three (Section 1, 2, 3) |
| How many data points approximately? | ~480 total |
| Where is the official XML schema? | OECD Publication (January 2025) |
| When is your first GIR due? | Deadline Calendar (typically June 30, 2026) |
| Do you need to register first? | Check jurisdiction requirements (UK: Yes) |
| Which portal do you use? | Jurisdiction-specific (see Section 2.4) |

---

## Visual Reference: One-Page GIR Process Map

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          GIR FILING PROCESS MAP                             │
└─────────────────────────────────────────────────────────────────────────────┘

PHASE 1: PREPARATION (Months 1-3)
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   SCOPE     │   │    DATA     │   │    DATA     │   │   SAFE      │
│   ENTITY    │──▶│  INVENTORY  │──▶│ EXTRACTION  │──▶│  HARBOUR    │
│   LIST      │   │  (~480 pts) │   │  FROM ERPs  │   │   TESTING   │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘

PHASE 2: CALCULATION (Month 4)
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  SECTION 1  │   │  SECTION 2  │   │  SECTION 3  │   │  INTERNAL   │
│  MNE GROUP  │──▶│    SAFE     │──▶│   GloBE     │──▶│ VALIDATION  │
│    INFO     │   │  HARBOURS   │   │   COMPS     │   │             │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘

PHASE 3: XML AND VALIDATION (Month 5)
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│     XML     │   │   SCHEMA    │   │   ERROR     │   │   FINAL     │
│ GENERATION  │──▶│ VALIDATION  │──▶│ CORRECTION  │──▶│   REVIEW    │
│             │   │             │   │             │   │             │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘

PHASE 4: FILING (Month 6)
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   PORTAL    │   │     GIR     │   │   CONFIRM   │   │   ARCHIVE   │
│   ACCESS    │──▶│ SUBMISSION  │──▶│   RECEIPT   │──▶│   AUDIT     │
│             │   │             │   │             │   │    FILE     │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘

JURISDICTION-SPECIFIC REQUIREMENTS:
┌─────────────────────────────────────────────────────────────────────────────┐
│  UK: Registration → GIR/ORN → SA Return → Payment                          │
│  Germany: Group Head Notification → GIR → Minimum Tax Return               │
│  Australia: GIR → FNF/CGDMTR → Payment                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Next Steps

Before proceeding to Part 2 (Step-by-Step Implementation), complete the following:

- [ ] Review the three-section GIR structure
- [ ] Download the OECD XML Schema User Guide
- [ ] Identify your filing jurisdiction(s) and portal access requirements
- [ ] Note your registration deadlines (if applicable)
- [ ] Add key deadlines to your calendar (use provided Excel calendar)
- [ ] Bookmark the OECD Pillar Two Main Portal

**Continue to Section 3: Understanding the GIR Structure →**

---

## Sources and References

This section incorporates information from:

- [OECD GloBE Information Return (Pillar Two) XML Schema](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html)
- [OECD GIR Status Message XML Schema](https://www.oecd.org/en/publications/globe-information-return-pillar-two-status-message-xml-schema_449e3cc3-en.html)
- [OECD Pillar Two Main Portal](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/global-anti-base-erosion-model-rules-pillar-two.html)
- [BZSt Pillar 2 Portal (Germany)](https://www.bzst.de/EN/Businesses/Pillar_2/pillar_2_node.html)
- [HMRC Pillar 2 Guidance (UK)](https://www.gov.uk/guidance/report-pillar-2-top-up-taxes)
- [ATO Pillar Two Lodging and Obligations](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/in-detail/multinationals/global-and-domestic-minimum-tax/lodging-paying-and-other-obligations-for-pillar-two)
- [OECD Compilation of GloBE Information Reporting Requirements](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/globe-information-reporting-requirements.html)
- [oecdpillars.com - Pillar Two Administration](https://oecdpillars.com/pillar-tab/pillar-two-administration/)
- [WTS Global Country-by-Country Implementation Status](https://wts.com/wts.com/hot-topics/pillar-two/implementation-status/wtsglobal-pillar-two-country-by-country-implementation.pdf)

---

*End of Section 2*
