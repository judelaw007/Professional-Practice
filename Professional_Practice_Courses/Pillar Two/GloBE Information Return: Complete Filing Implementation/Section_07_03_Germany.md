# Section 7.3: Germany

## Learning Objectives

By the end of this section, you will be able to:
- Navigate the BZSt online portal for Pillar Two filings
- Complete the Group Head Notification (Gruppenträgermeldung) by the required deadline
- Submit the GloBE Information Return via the DIP mass data interface
- File the Minimum Tax Return (Mindeststeueranmeldung) to the competent Finanzamt
- Understand German-specific requirements including QDMTT and language considerations
- Apply the German Pillar Two Filing Checklist for compliance assurance

## Introduction

Germany implemented Pillar Two through the Minimum Tax Act (Mindeststeuergesetz, MinStG), effective for fiscal years beginning after 30 December 2023. The legislation implements the EU Minimum Tax Directive (2022/2523) and introduces three charging mechanisms:

- **Primary Top-up Tax (Primärergänzungssteuer)** - Income Inclusion Rule (IIR)
- **Secondary Top-up Tax (Sekundärergänzungssteuer)** - Undertaxed Profits Rule (UTPR), effective for fiscal years beginning after 30 December 2024
- **National Top-up Tax (Nationale Ergänzungssteuer)** - Qualified Domestic Minimum Top-up Tax (QDMTT)

**Critical Point:** German groups face three separate filing obligations: Group Head Notification, GloBE Information Return, and Minimum Tax Return. The Group Head Notification deadline for calendar year-end groups was **28 February 2025**.

---

## 7.3.1 German Pillar Two Framework

### Scope of the MinStG

```
MinStG Scope (Section 1):
│
├── REVENUE THRESHOLD
│   ├── €750 million consolidated revenue
│   ├── In at least 2 of the 4 preceding fiscal years
│   └── Based on UPE consolidated financial statements
│
├── GERMAN NEXUS
│   ├── At least one Constituent Entity located in Germany
│   ├── Includes German permanent establishments
│   └── German branch of foreign entity = in scope
│
└── EXCLUSIONS
    ├── Investment funds meeting specific criteria
    ├── Pension funds
    ├── Government entities
    └── International organisations
```

### Key German Terminology

| English Term | German Term | MinStG Reference |
|-------------|-------------|------------------|
| Minimum Tax Act | Mindeststeuergesetz | MinStG |
| Minimum Tax Group | Mindeststeuergruppe | § 3 MinStG |
| Group Head | Gruppenträger | § 3 MinStG |
| Primary Top-up Tax (IIR) | Primärergänzungssteuer | § 7-55 MinStG |
| Secondary Top-up Tax (UTPR) | Sekundärergänzungssteuer | § 56-64 MinStG |
| National Top-up Tax (QDMTT) | Nationale Ergänzungssteuer | § 90-94 MinStG |
| Group Head Notification | Gruppenträgermeldung | § 3 MinStG |
| GloBE Information Return | Mindeststeuer-Bericht | § 75 MinStG |
| Minimum Tax Return | Mindeststeueranmeldung | § 95 MinStG |
| Federal Central Tax Office | Bundeszentralamt für Steuern | BZSt |

### Determining the Group Head (Gruppenträger)

The Group Head is determined using a "top-down" approach per § 3(3) MinStG:

```
Group Head Determination (§ 3(3) MinStG):
│
├── STEP 1: Is UPE located in Germany?
│   ├── YES → UPE is Group Head
│   └── NO → Proceed to Step 2
│
├── STEP 2: Is there a German entity controlling all other German CEs?
│   ├── YES → Controlling entity is Group Head
│   └── NO → Proceed to Step 3
│
├── STEP 3: Has UPE designated a Group Head?
│   ├── YES → Designated entity is Group Head
│   └── NO → Proceed to Step 4
│
└── STEP 4: Default rule
    └── Economically most significant German CE = Group Head
        (Based on revenue, assets, or employees)
```

---

## 7.3.2 Three Filing Obligations

### Overview of German Filing Requirements

```
German Pillar Two Filing Obligations:
│
├── 1. GROUP HEAD NOTIFICATION (Gruppenträgermeldung)
│   ├── Filed to: BZSt (Federal Central Tax Office)
│   ├── Format: Electronic via BZSt online portal
│   ├── Deadline: 2 months after fiscal year end
│   ├── First deadline: 28 February 2025 (calendar year groups)
│   └── One-time notification (update only if changes occur)
│
├── 2. GloBE INFORMATION RETURN (Mindeststeuer-Bericht)
│   ├── Filed to: BZSt
│   ├── Format: XML via DIP mass data interface
│   ├── Deadline: 15 months after fiscal year end (18 months first year)
│   ├── First deadline: 30 June 2026 (for FY 2024)
│   └── Annual filing requirement
│
└── 3. MINIMUM TAX RETURN (Mindeststeueranmeldung)
│   ├── Filed to: Competent state Finanzamt
│   ├── Format: Electronic via ELSTER
│   ├── Deadline: Same as GIR deadline
│   ├── First deadline: 30 June 2026 (for FY 2024)
│   └── Self-assessment return (Steueranmeldung)
```

### Filing Deadline Summary

| Filing | First-Year Deadline | Standard Deadline | Filed To |
|--------|--------------------|--------------------|----------|
| Group Head Notification | 28 Feb 2025 (CY groups) | 2 months after FY end | BZSt |
| GloBE Information Return | 30 June 2026 | 15 months after FY end | BZSt |
| Minimum Tax Return | 30 June 2026 | Same as GIR | Finanzamt |

---

## 7.3.3 BZSt Portal Registration and Access

### Portal Overview

The Federal Central Tax Office (Bundeszentralamt für Steuern, BZSt) operates the online portal for Pillar Two filings:

- **Portal URL:** https://online.portal.bzst.de
- **English Version:** https://online.portal.bzst.de/EN/Home/home_node.html
- **Pillar 2 Information:** https://www.bzst.de/EN/Businesses/Pillar_2/pillar_2_node.html

### Certificate Requirements

Access to the BZSt online portal requires a valid digital certificate:

```
BZSt Portal Authentication Options:
│
├── OPTION 1: ELSTER Certificate (Recommended for German entities)
│   ├── Obtain via: https://www.elster.de
│   ├── Registration: "Mein ELSTER" account
│   ├── Timeline: Approximately 1 week (activation code by post)
│   └── Cost: Free
│
├── OPTION 2: BZSt Certificate
│   ├── Obtain via: BZSt online portal registration
│   ├── Required for: Entities without ELSTER access
│   ├── Timeline: 6-8 weeks for processing
│   └── Cost: Free
│
└── AUTHENTICATION PROCESS
    ├── Log in to BZSt online portal with certificate
    ├── Navigate to Pillar 2 section
    └── Access filing functions
```

### Step-by-Step Portal Registration

```
BZSt Portal Registration Process:
│
├── STEP 1: Obtain Certificate
│   ├── German entities: Register at www.elster.de
│   ├── Foreign entities: Apply for BZSt certificate
│   ├── Complete online application form
│   └── Wait for activation credentials (1-8 weeks)
│
├── STEP 2: Activate Certificate
│   ├── Receive activation ID by email
│   ├── Receive activation code by postal mail
│   ├── Enter both codes to activate
│   └── Download certificate file (.pfx)
│
├── STEP 3: Access BZSt Online Portal
│   ├── Navigate to: https://online.portal.bzst.de
│   ├── Select certificate login option
│   ├── Upload certificate file
│   ├── Enter certificate password
│   └── Complete login
│
├── STEP 4: Activate Mass Data Interface (DIP)
│   ├── Required for GIR XML submission
│   ├── Submit "Application for activation of mass data interface"
│   ├── Receive BZSt-Number by letter
│   ├── Receive BZSt-Secret by email
│   └── Configure software for DIP connection
│
└── STEP 5: Test Connection
    ├── Verify portal access
    ├── Test DIP interface (if applicable)
    └── Confirm filing capability
```

### Language Considerations

**Important:** German is the primary language for tax administration:

| Component | Language Availability |
|-----------|----------------------|
| BZSt website | German and English |
| ELSTER registration | German only |
| Portal interface | German (partial English) |
| Filing forms | German |
| GIR XML Schema | English (OECD standard) |
| Official guidance | German (some English translations) |
| Help desk support | German |

**Practical Tip:** Non-German speakers should engage German tax advisers for portal navigation and filing. The GIR XML format follows the OECD English-language schema.

---

## 7.3.4 Group Head Notification

### Purpose and Content

The Group Head Notification identifies the Minimum Tax Group and its responsible entity:

```
Group Head Notification Content (§ 3 MinStG):
│
├── GROUP HEAD IDENTIFICATION
│   ├── Name and legal form
│   ├── Address (registered office)
│   ├── German tax number (Steuernummer)
│   ├── Tax identification number if applicable
│   └── Contact person details (name, phone, email)
│
├── ULTIMATE PARENT ENTITY (UPE) IDENTIFICATION
│   ├── Name and legal form
│   ├── Address
│   ├── Country of tax residence
│   └── Tax identification number (if available)
│
├── GROUP HEAD CHARACTERISATION
│   ├── Basis for Group Head status:
│   │   ├── UPE located in Germany
│   │   ├── Controlling German entity
│   │   ├── UPE designation
│   │   └── Economically most significant CE
│   └── Documentation of determination
│
└── AUTHORISED REPRESENTATIVE (if applicable)
    ├── Tax adviser details
    ├── Power of attorney reference
    └── Contact information
```

### Filing Process

```
Group Head Notification Filing:
│
├── ACCESS
│   ├── Log in to BZSt online portal
│   ├── Navigate to Pillar 2 section
│   └── Select "Gruppenträgermeldung"
│
├── COMPLETE FORM
│   ├── Enter all required information
│   ├── Attach supporting documentation if required
│   └── Review for completeness
│
├── SUBMIT
│   ├── Submit electronically
│   ├── Receive confirmation/reference number
│   └── Archive submission confirmation
│
└── UPDATES
    ├── Notify BZSt of any changes
    ├── Submit updated notification
    └── No annual re-filing required if unchanged
```

### Deadline Calculation

```
Group Head Notification Deadline:

Deadline = Fiscal Year End + 2 months

Examples:
┌─────────────────────────────┬──────────────────────────┐
│ Fiscal Year End             │ Notification Deadline    │
├─────────────────────────────┼──────────────────────────┤
│ 31 December 2024            │ 28 February 2025         │
│ 31 March 2025               │ 31 May 2025              │
│ 30 June 2025                │ 31 August 2025           │
│ 30 September 2025           │ 30 November 2025         │
└─────────────────────────────┴──────────────────────────┘

Note: For non-calendar year groups, first notification deadline
is generally 28 February 2026 (unless short fiscal year applies).
```

---

## 7.3.5 GloBE Information Return (Mindeststeuer-Bericht)

### Filing Requirements

The GIR must be filed electronically via the DIP mass data interface:

```
German GIR Requirements:
│
├── FORMAT
│   ├── OECD GIR XML Schema v1.0
│   ├── Transmitted via DIP interface
│   └── No manual portal upload option
│
├── CONTENT
│   ├── General section (group information)
│   ├── Jurisdictional sections (per OECD specification)
│   ├── All Constituent Entities worldwide
│   └── Top-up tax calculations by jurisdiction
│
├── SUBMISSION
│   ├── Group Head submits on behalf of entire group
│   ├── Single consolidated filing
│   └── Electronic transmission only
│
└── DEADLINE
    ├── First year: 18 months after fiscal year end
    ├── Subsequent years: 15 months after fiscal year end
    └── Minimum deadline: 30 June 2026 (§ 96 MinStG)
```

### DIP Mass Data Interface

```
DIP Interface Technical Requirements:
│
├── ACTIVATION
│   ├── One-time registration required
│   ├── Submit activation application via BZSt portal
│   ├── Receive BZSt-Number and BZSt-Secret
│   └── Configure software with credentials
│
├── TECHNICAL SPECIFICATIONS
│   ├── REST API interface
│   ├── OAuth 2.0 authentication
│   ├── Maximum file size: 1 GB
│   ├── Maximum upload time: 15 minutes
│   └── Access tokens expire in seconds (request new for each call)
│
├── XML REQUIREMENTS
│   ├── OECD GIR XML Schema v1.0
│   ├── UTF-8 encoding
│   ├── Validate before submission
│   └── Schema available at BZSt website
│
└── DOCUMENTATION
    ├── Communication Manual: BZSt website
    ├── Technical specifications: Developer documentation
    └── Support: service-pillar2@bzst.bund.de
```

### Step-by-Step GIR Filing

```
German GIR Filing Process:
│
├── PREPARATION
│   ├── Complete GIR data compilation per OECD specification
│   ├── Generate XML file using validated software
│   ├── Perform three-tier validation locally
│   └── Obtain internal approval
│
├── DIP CONFIGURATION
│   ├── Ensure DIP interface activated
│   ├── Configure software with BZSt credentials
│   ├── Test connection in sandbox environment
│   └── Verify authentication working
│
├── SUBMISSION
│   ├── Request fresh access token
│   ├── Upload XML file via DIP interface
│   ├── Await processing confirmation
│   └── Receive submission reference
│
├── CONFIRMATION
│   ├── Download submission confirmation
│   ├── Verify file hash matches submitted file
│   ├── Archive all documentation
│   └── Record in filing register
│
└── POST-SUBMISSION
    ├── Monitor for BZSt queries
    ├── Respond to validation errors if any
    └── File Minimum Tax Return separately
```

---

## 7.3.6 Minimum Tax Return (Mindeststeueranmeldung)

### Filing Requirements

The Minimum Tax Return is a self-assessment (Steueranmeldung) filed to the competent state Finanzamt:

```
Minimum Tax Return Requirements (§ 95 MinStG):
│
├── NATURE
│   ├── Self-assessment return (Steueranmeldung)
│   ├── Group Head calculates and declares tax due
│   └── Equivalent to tax assessment
│
├── CONTENT
│   ├── Primary Top-up Tax (IIR) liability
│   ├── Secondary Top-up Tax (UTPR) liability
│   ├── National Top-up Tax (QDMTT) liability
│   ├── Allocation to German Constituent Entities
│   └── Supporting calculations
│
├── FILED TO
│   ├── Competent state Finanzamt
│   ├── Based on Group Head location
│   └── NOT to BZSt (unlike GIR)
│
└── FORMAT
    ├── Electronic submission via ELSTER
    ├── Officially prescribed data format
    └── Transmitted through official interface
```

### Determining the Competent Finanzamt

```
Competent Finanzamt Determination:
│
├── Based on Group Head's registered location
├── Same Finanzamt as for corporation tax
└── Germany has approximately 650 local Finanzämter

Example:
Group Head located in Munich → Finanzamt München
Group Head located in Frankfurt → Finanzamt Frankfurt am Main
```

### Filing Deadline

The Minimum Tax Return deadline is linked to the GIR deadline:

```
§ 96 MinStG: Deadline Synchronisation

The Minimum Tax Return deadline does not expire before
the GIR filing deadline.

Result: Both GIR and Minimum Tax Return due by 30 June 2026
(for fiscal year 2024).
```

---

## 7.3.7 German QDMTT (Nationale Ergänzungssteuer)

### Overview

Germany has implemented a Qualified Domestic Minimum Top-up Tax:

```
German QDMTT (§§ 90-94 MinStG):
│
├── PURPOSE
│   ├── Ensures 15% minimum taxation in Germany
│   ├── Collected domestically before IIR/UTPR apply
│   └── Reduces foreign top-up tax exposure
│
├── CALCULATION
│   ├── German jurisdictional ETR calculated
│   ├── If below 15%, top-up tax applies
│   ├── Based on GloBE income and covered taxes
│   └── Applies to all German Constituent Entities
│
├── QDMTT SAFE HARBOUR (§ 81 MinStG)
│   ├── Where German QDMTT applies, deems:
│   ├── IIR top-up = nil for Germany
│   ├── UTPR top-up = nil for Germany
│   └── Protects against double top-up taxation
│
└── PAYMENT
    ├── Part of Minimum Tax Return liability
    ├── Paid to Finanzamt
    └── Same deadline as return
```

### QDMTT Impact on Filing

```
QDMTT Filing Implications:
│
├── GIR CONTENT
│   ├── German jurisdictional section required
│   ├── Report German QDMTT calculations
│   └── Document QDMTT Safe Harbour if claimed
│
├── MINIMUM TAX RETURN
│   ├── Separate line for QDMTT liability
│   ├── Combined with IIR/UTPR amounts
│   └── Single payment covers all components
│
└── SAFE HARBOUR ELECTIONS
    ├── Transitional safe harbours available
    ├── CbCR-based simplified calculations
    └── Reduced compliance burden where applicable
```

---

## 7.3.8 Penalties and Compliance

### Penalty Framework

```
German MinStG Penalties:
│
├── LATE GIR FILING (§ 98 MinStG)
│   ├── Administrative offence (Ordnungswidrigkeit)
│   ├── Intentional or reckless failure to file
│   ├── Maximum penalty: €30,000
│   └── Applies to incomplete or late submission
│
├── LATE GROUP HEAD NOTIFICATION
│   ├── Administrative sanctions apply
│   ├── Late filing still possible and advisable
│   └── Penalty mitigation for voluntary correction
│
├── LATE MINIMUM TAX RETURN
│   ├── General Fiscal Code (AO) penalties apply
│   ├── Late filing surcharge (Verspätungszuschlag)
│   ├── Up to 10% of tax due (max €25,000)
│   └── Plus interest on late payment
│
└── INTEREST ON LATE PAYMENT
    ├── Standard fiscal interest rate applies
    ├── Currently 0.5% per month (6% p.a.)
    └── Runs from payment deadline
```

### Penalty Mitigation

| Factor | Mitigation Effect |
|--------|-------------------|
| Voluntary late filing | May reduce penalty significantly |
| Technical difficulties | Potential full relief |
| First-time non-compliance | Discretionary reduction |
| Cooperation with authorities | Favourable consideration |
| Reasonable excuse | Potential full relief |

---

## 7.3.9 Amendment Procedures

### Correcting Filed Returns

```
Amendment Process:
│
├── GIR AMENDMENTS
│   ├── Submit corrected XML via DIP interface
│   ├── Reference original submission
│   ├── BZSt processes as amendment
│   └── No specific time limit in MinStG
│
├── MINIMUM TAX RETURN AMENDMENTS
│   ├── General Fiscal Code rules apply
│   ├── Taxpayer correction within 1 month
│   ├── Subsequent amendment via formal request
│   └── Finanzamt may issue amended assessment
│
├── GROUP HEAD NOTIFICATION UPDATES
│   ├── Submit updated notification if changes occur
│   ├── No annual renewal required
│   └── Update within reasonable timeframe
│
└── DOCUMENTATION
    ├── Retain original and amended versions
    ├── Document reason for amendment
    └── Maintain clear audit trail
```

---

## 7.3.10 Deliverable: German Pillar Two Filing Checklist

```
GERMAN PILLAR TWO FILING CHECKLIST
Unternehmensgruppe/Group Name: ________________________________
Geschäftsjahr/Fiscal Year: ____ / ____ / ____  to  ____ / ____ / ____
Gruppenträger/Group Head: ____________________________
BZSt Reference: ____________________________

═══════════════════════════════════════════════════════════════════════════════

SECTION A: PORTAL ACCESS AND REGISTRATION
─────────────────────────────────────────────────────────────────────────────
☐ A1. Confirmed group meets €750m revenue threshold (2 of 4 years)
☐ A2. Identified Group Head (Gruppenträger) per § 3 MinStG
☐ A3. Documented Group Head determination basis
☐ A4. Valid ELSTER or BZSt certificate obtained
☐ A5. BZSt online portal access confirmed
☐ A6. DIP mass data interface activated (for GIR submission)
☐ A7. Received BZSt-Number: _________________
☐ A8. Received BZSt-Secret (stored securely)
☐ A9. Software configured for DIP interface
☐ A10. Test submission completed successfully

Portal Access Confirmed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION B: GROUP HEAD NOTIFICATION (Gruppenträgermeldung)
─────────────────────────────────────────────────────────────────────────────
☐ B1. Calculated notification deadline: _________________
☐ B2. Group Head identification prepared:
      ☐ Name and legal form
      ☐ Address
      ☐ German tax number (Steuernummer)
      ☐ Contact person details
☐ B3. UPE identification prepared:
      ☐ Name and legal form
      ☐ Address and country
      ☐ Tax identification number
☐ B4. Group Head characterisation documented
☐ B5. Authorised representative details (if applicable)
☐ B6. Logged in to BZSt online portal
☐ B7. Completed notification form
☐ B8. Submitted notification electronically
☐ B9. Confirmation reference received: _________________
☐ B10. Confirmation document archived

Notification Filed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION C: GloBE INFORMATION RETURN (Mindeststeuer-Bericht)
─────────────────────────────────────────────────────────────────────────────
☐ C1. GIR filing deadline calculated: _________________
☐ C2. GIR data compilation complete per OECD specification
☐ C3. All Constituent Entities included
☐ C4. Jurisdictional sections completed (including Germany)
☐ C5. QDMTT calculations included for Germany
☐ C6. Safe harbour elections documented
☐ C7. XML file generated per OECD Schema v1.0
☐ C8. Three-tier validation completed:
      ☐ Tier 1: Well-formedness PASS
      ☐ Tier 2: Schema validation PASS
      ☐ Tier 3: Business rules PASS
☐ C9. Internal review and sign-off obtained
☐ C10. DIP interface connection verified
☐ C11. Access token obtained
☐ C12. XML file uploaded via DIP
☐ C13. Submission confirmation received: _________________
☐ C14. File hash verified and recorded
☐ C15. Confirmation document archived

GIR Filed By: _____________ Date: ____ / ____ / ____ Time: ______

═══════════════════════════════════════════════════════════════════════════════

SECTION D: MINIMUM TAX RETURN (Mindeststeueranmeldung)
─────────────────────────────────────────────────────────────────────────────
☐ D1. Filing deadline confirmed: _________________
☐ D2. Competent Finanzamt identified: _________________
☐ D3. Tax liabilities calculated:
      Primary Top-up Tax (IIR): € _________________
      Secondary Top-up Tax (UTPR): € _________________
      National Top-up Tax (QDMTT): € _________________
      TOTAL: € _________________
☐ D4. Allocation to German CEs documented
☐ D5. ELSTER access confirmed for Finanzamt filing
☐ D6. Minimum Tax Return completed
☐ D7. Return submitted electronically via ELSTER
☐ D8. Submission confirmation received: _________________
☐ D9. Confirmation document archived

Minimum Tax Return Filed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION E: PAYMENT
─────────────────────────────────────────────────────────────────────────────
☐ E1. Total liability confirmed: € _________________
☐ E2. Payment deadline: ____ / ____ / ____
☐ E3. Bank transfer details obtained from Finanzamt
☐ E4. Payment reference prepared (Verwendungszweck)
☐ E5. Payment made
☐ E6. Payment confirmation received
☐ E7. Payment confirmed in tax account

Payment Made By: _____________ Date: ____ / ____ / ____ Amount: € _________

═══════════════════════════════════════════════════════════════════════════════

SECTION F: POST-FILING
─────────────────────────────────────────────────────────────────────────────
☐ F1. All confirmation documents archived
☐ F2. Filing register updated
☐ F3. XML file and hash retained
☐ F4. Source documentation retained (10+ years)
☐ F5. Next period deadlines set in calendar
☐ F6. Management briefed on filing completion

Post-Filing Completed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

CERTIFICATION
─────────────────────────────────────────────────────────────────────────────
Hiermit bestätige ich, dass alle Pillar Two Meldepflichten für das
oben genannte Geschäftsjahr ordnungsgemäß erfüllt wurden.

I confirm that all German Pillar Two filing obligations for the above
fiscal year have been properly fulfilled.

Prepared By: _____________________________________________ Date: ____ / ____ / ____

Reviewed By: _____________________________________________ Date: ____ / ____ / ____

Approved By: _____________________________________________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════
```

---

## Key Resources and Links

### BZSt Portals and Services

| Resource | URL |
|----------|-----|
| BZSt Online Portal | https://online.portal.bzst.de |
| BZSt Pillar 2 Main Page | https://www.bzst.de/EN/Businesses/Pillar_2/pillar_2_node.html |
| Pillar 2 Procedure | https://www.bzst.de/EN/Businesses/Pillar_2/Procedure/procedure_node.html |
| Pillar 2 FAQ | https://www.bzst.de/EN/Businesses/Pillar_2/FAQ/faq_node.html |
| XML Schema and Compendia | https://www.bzst.de/EN/Businesses/Pillar_2/Compendia/compendia_node.html |
| DIP Interface Application | https://online.portal.bzst.de (after login) |
| ELSTER Portal | https://www.elster.de |

### Legislation and Guidance

| Resource | Reference |
|----------|-----------|
| Minimum Tax Act (English) | https://www.bundesfinanzministerium.de/Content/EN/Downloads/Taxation/minimum-tax-act.pdf |
| MinStG (German) | BGBl. 2023 I Nr. 397 |
| EU Directive 2022/2523 | EUR-Lex |
| OECD GloBE Model Rules | OECD Tax website |

### Contact Information

| Contact | Details |
|---------|---------|
| BZSt Pillar 2 Hotline | +49 228 406 4045 |
| Email | service-pillar2@bzst.bund.de |
| General BZSt | +49 228 406 0 |

---

## Summary

Germany's Pillar Two implementation through the MinStG requires careful coordination of three separate filing obligations:

1. **Group Head Notification** - Identify the responsible entity (deadline: 2 months after FY end)
2. **GloBE Information Return** - Submit via BZSt DIP interface (deadline: 15/18 months after FY end)
3. **Minimum Tax Return** - Self-assessment to Finanzamt (deadline: same as GIR)

Key considerations for practitioners:
- Obtain ELSTER/BZSt certificate well in advance (up to 8 weeks)
- Activate DIP interface before first GIR submission
- Navigate German language requirements (engage local advisers)
- Coordinate GIR and Minimum Tax Return filings
- Maximum penalty of €30,000 for late GIR filing

---

## Section Review Questions

1. What are the three filing obligations under the German MinStG?

2. What is the deadline for the Group Head Notification for a calendar year-end group?

3. Where is the Minimum Tax Return filed - BZSt or Finanzamt?

4. What is the maximum penalty for late GIR filing under § 98 MinStG?

5. What certificate is required to access the BZSt online portal?

6. From what date is the German UTPR (Sekundärergänzungssteuer) effective?

**Answers:** 1) Group Head Notification, GIR, Minimum Tax Return; 2) 28 February 2025; 3) Finanzamt; 4) €30,000; 5) ELSTER or BZSt certificate; 6) Fiscal years beginning after 30 December 2024.

---

*Section 7.3 Complete. Proceed to Section 7.4: Netherlands for Dutch-specific filing procedures.*
