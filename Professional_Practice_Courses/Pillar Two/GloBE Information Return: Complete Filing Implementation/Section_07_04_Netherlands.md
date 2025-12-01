# Section 7.4: Netherlands

## Learning Objectives

By the end of this section, you will be able to:
- Navigate the Mijn Belastingdienst Zakelijk portal for Pillar Two filings
- Obtain and use eHerkenning level 3 (EH3) for authentication
- Submit the GloBE Information Return (Top-up Tax Information Declaration)
- File the Top-up Tax Return (Aangifte minimumbelasting)
- Understand Dutch QDMTT and safe harbour provisions
- Apply the Netherlands Pillar Two Filing Checklist for compliance assurance

## Introduction

The Netherlands implemented Pillar Two through the Minimum Tax Act 2024 (Wet minimumbelasting 2024), effective for fiscal years beginning on or after 31 December 2023. The legislation implements EU Directive 2022/2523 and introduces:

- **Qualified Domestic Minimum Top-up Tax (QDMTT)** - Nationale bijheffing
- **Income Inclusion Rule (IIR)** - Inkomensinsluitingsregel
- **Undertaxed Profits Rule (UTPR)** - Regel voor onderbelaste winsten (effective for fiscal years beginning on or after 31 December 2024)

**Critical Point:** Dutch groups face two separate filing obligations with different deadlines: the GloBE Information Return (15/18 months) and the Top-up Tax Return (17/20 months). The portal system is still under development.

---

## 7.4.1 Dutch Pillar Two Framework

### Scope of the Wet minimumbelasting 2024

```
Dutch Minimum Tax Scope:
│
├── REVENUE THRESHOLD
│   ├── €750 million consolidated annual turnover
│   ├── In at least 2 of the 4 preceding fiscal years
│   └── Based on UPE consolidated financial statements
│
├── DUTCH NEXUS
│   ├── At least one Constituent Entity located in Netherlands
│   ├── Includes Dutch permanent establishments
│   └── Dutch branch of foreign entity = in scope
│
├── CHARGING MECHANISMS
│   ├── QDMTT: Effective 31 December 2023
│   ├── IIR: Effective 31 December 2023
│   └── UTPR: Effective 31 December 2024
│
└── DUTCH TAX RATE CONTEXT
    ├── Standard CIT rate: 25.8%
    ├── Generally above 15% minimum
    ├── Lower rates possible with:
    │   ├── Innovation box (9%)
    │   ├── Tonnage regime
    │   └── Liquidation loss provisions
    └── QDMTT applies only in specific low-ETR situations
```

### Key Dutch Terminology

| English Term | Dutch Term | Reference |
|-------------|------------|-----------|
| Minimum Tax Act 2024 | Wet minimumbelasting 2024 | Primary legislation |
| Top-up Tax | Bijheffing | General term |
| Qualified Domestic Top-up Tax | Nationale bijheffing (QDMTT) | Art. 2.1 |
| Income Inclusion Rule | Inkomensinsluitingsregel (IIR) | Art. 2.2 |
| Undertaxed Profits Rule | Regel voor onderbelaste winsten (UTPR) | Art. 2.3 |
| GloBE Information Return | Informatieaangifte | Art. 8.1 |
| Top-up Tax Return | Aangifte minimumbelasting | Art. 8.2 |
| Tax Administration | Belastingdienst | Filing authority |
| Business portal | Mijn Belastingdienst Zakelijk | Online portal |

---

## 7.4.2 Two Filing Obligations

### Overview of Dutch Filing Requirements

```
Dutch Pillar Two Filing Obligations:
│
├── 1. GloBE INFORMATION RETURN (Informatieaangifte)
│   ├── Filed to: Belastingdienst (Tax Inspector)
│   ├── Format: XML via Mijn Belastingdienst Zakelijk
│   ├── Deadline: 15 months after fiscal year end
│   ├── First-year deadline: 18 months (30 June 2026 for FY 2024)
│   ├── Content: Full GIR per OECD specification
│   └── Alternative: Notify where GIR filed if submitted elsewhere
│
└── 2. TOP-UP TAX RETURN (Aangifte minimumbelasting)
    ├── Filed to: Belastingdienst (Tax Inspector)
    ├── Format: Electronic via Mijn Belastingdienst Zakelijk
    ├── Deadline: 17 months after fiscal year end
    ├── First-year deadline: 20 months (31 August 2026 for FY 2024)
    ├── Content: Self-assessed top-up tax liability
    └── Nature: Self-assessment (like VAT returns)
```

### Filing Deadline Summary

| Filing | Standard Deadline | First-Year Deadline | First FY 2024 Date |
|--------|-------------------|---------------------|-------------------|
| GloBE Information Return | 15 months | 18 months | 30 June 2026 |
| Top-up Tax Return | 17 months | 20 months | 31 August 2026 |
| Payment | With return | With return | 31 August 2026 |

### Deadline Calculation Examples

```
Dutch Filing Deadline Calculations:

For Fiscal Year Ending 31 December 2024 (First Year):
├── GIR Deadline: 30 June 2026 (18 months)
├── Top-up Tax Return: 31 August 2026 (20 months)
└── Payment: 31 August 2026

For Fiscal Year Ending 31 December 2025 (Year 2):
├── GIR Deadline: 31 March 2027 (15 months)
├── Top-up Tax Return: 31 May 2027 (17 months)
└── Payment: 31 May 2027

For Fiscal Year Ending 30 June 2025:
├── GIR Deadline: 31 December 2026 (18 months, first year)
├── Top-up Tax Return: 28 February 2027 (20 months)
└── Payment: 28 February 2027
```

---

## 7.4.3 Portal Access and eHerkenning

### Mijn Belastingdienst Zakelijk

The Dutch Tax Administration operates Mijn Belastingdienst Zakelijk as the primary business portal:

- **Portal URL:** https://mijn.belastingdienst.nl/mbd-pmb/
- **English information:** https://www.belastingdienst.nl/wps/wcm/connect/en/business/
- **Pillar Two information:** https://www.belastingdienst.nl/wps/wcm/connect/en/business/content/minimum-tax

**Current Status:** As of the time of writing, the Top-up Tax Return system is still under development. Check the Belastingdienst website for the latest updates.

### eHerkenning Requirements

Access to Mijn Belastingdienst Zakelijk requires eHerkenning level 3 (EH3) or higher:

```
eHerkenning Authentication:
│
├── WHAT IS eHerkenning?
│   ├── Dutch government digital identity for businesses
│   ├── Similar to DigiD but for organisations
│   ├── Multiple assurance levels (1-4)
│   └── Required for tax portal access
│
├── LEVEL 3 (EH3) REQUIREMENT
│   ├── Minimum level for Belastingdienst access
│   ├── Second-highest assurance level
│   ├── Personal credential per individual
│   └── Cannot be shared or transferred
│
├── TWO EH3 OPTIONS
│   │
│   ├── OPTION A: Regular eHerkenning 3
│   │   ├── General-purpose credential
│   │   ├── Works with all government services
│   │   ├── Higher cost
│   │   └── Apply via eHerkenning suppliers
│   │
│   └── OPTION B: eHerkenning 3 Belastingdienst (Tax Service)
│       ├── Dedicated credential for tax matters
│       ├── Only works with Belastingdienst
│       ├── €24.20 annual government compensation
│       ├── Lower cost option
│       └── Sufficient for Pillar Two filings
│
└── FOREIGN ENTITIES (No KVK Number)
    ├── Can obtain eHerkenning using fiscal number
    ├── Alternative login method available
    └── Contact eHerkenning supplier for guidance
```

### Obtaining eHerkenning

```
eHerkenning Application Process:
│
├── STEP 1: Choose Supplier
│   ├── Visit: https://www.eherkenning.nl/en/applying-eherkenning
│   ├── Compare approved suppliers
│   ├── Select based on cost and service level
│   └── Popular suppliers: Digidentity, KPN, QuoVadis
│
├── STEP 2: Apply Online
│   ├── Complete application form
│   ├── Provide company information
│   ├── Identify authorised user(s)
│   └── Select assurance level (EH3 minimum)
│
├── STEP 3: Identity Verification
│   ├── In-person verification may be required
│   ├── Video identification available with some suppliers
│   ├── Passport or ID document required
│   └── Processing time: typically 1-2 weeks
│
├── STEP 4: Receive Credentials
│   ├── Receive authentication means (app/USB token/certificate)
│   ├── Set up personal PIN/password
│   └── Test login to portal
│
└── STEP 5: Access Portal
    ├── Navigate to Mijn Belastingdienst Zakelijk
    ├── Select "Inloggen met eHerkenning"
    ├── Choose your supplier
    └── Authenticate with credentials
```

### Alternative: DigiD for Sole Proprietors

Individual entrepreneurs (zzp'ers) may use personal DigiD instead of eHerkenning.

---

## 7.4.4 GloBE Information Return Filing

### Filing Requirements

```
Dutch GIR (Informatieaangifte) Requirements:
│
├── WHO MUST FILE
│   ├── Designated Dutch Constituent Entity
│   ├── OR any Dutch CE if no designation
│   └── Filing on behalf of entire group
│
├── EXEMPTION FROM DUTCH FILING
│   ├── GIR filed in another jurisdiction AND
│   ├── That jurisdiction exchanges GIR with Netherlands AND
│   └── Dutch notification submitted to Belastingdienst
│
├── FORMAT
│   ├── XML format per OECD GIR Schema v1.0
│   ├── Submit via Mijn Belastingdienst Zakelijk
│   └── Software developers: register via Ondersteuning Digitaal Berichtenverkeer
│
└── CONTENT
    ├── General section (group information)
    ├── Jurisdictional sections per OECD specification
    ├── All Constituent Entities worldwide
    └── Top-up tax calculations by jurisdiction
```

### Notification When GIR Filed Elsewhere

If the GIR is filed in another jurisdiction, Dutch entities must notify the Belastingdienst:

```
GIR Notification (when filed elsewhere):
│
├── WHEN REQUIRED
│   ├── GIR submitted in another jurisdiction
│   ├── That jurisdiction participates in GIR exchange
│   └── Netherlands will receive GIR via MCAA
│
├── CONTENT
│   ├── Identification of filing jurisdiction
│   ├── Date of GIR submission
│   ├── Filing entity identification
│   └── Dutch group entity details
│
├── DEADLINE
│   ├── Same as GIR deadline: 15 months (18 months first year)
│   └── 30 June 2026 for FY 2024
│
└── STATUS
    ├── Specific notification procedure to be announced
    └── Check Belastingdienst website for updates
```

---

## 7.4.5 Top-up Tax Return Filing

### Self-Assessment Nature

The Dutch Top-up Tax Return is a self-assessment (comparable to VAT returns):

```
Top-up Tax Return (Aangifte minimumbelasting):
│
├── NATURE
│   ├── Self-assessment filing
│   ├── Taxpayer calculates and declares liability
│   ├── No assessment raised by tax authorities
│   └── Payment due with return
│
├── CONTENT
│   ├── QDMTT liability (if applicable)
│   ├── IIR top-up tax liability
│   ├── UTPR top-up tax liability (from 2024)
│   ├── Allocation to Dutch entities
│   └── Supporting calculations
│
├── WHO MUST FILE
│   ├── Required only if top-up tax payable
│   ├── Dutch group entity or designated local entity
│   └── Single consolidated return for group
│
└── PAYMENT
    ├── Due simultaneously with return
    ├── 17 months after fiscal year end (20 months first year)
    └── Pay via bank transfer to Belastingdienst
```

### Filing Process

```
Top-up Tax Return Filing Process:
│
├── PREPARATION
│   ├── Calculate top-up tax liability
│   ├── Based on GIR data (file GIR first)
│   ├── Allocate to Dutch constituent entities
│   └── Prepare supporting documentation
│
├── ACCESS PORTAL
│   ├── Log in to Mijn Belastingdienst Zakelijk
│   ├── Use eHerkenning level 3
│   ├── Navigate to Minimum Tax section
│   └── (System under development - check for updates)
│
├── COMPLETE RETURN
│   ├── Enter liability amounts
│   ├── Provide entity allocation
│   ├── Complete all required fields
│   └── Review for accuracy
│
├── SUBMIT AND PAY
│   ├── Submit return electronically
│   ├── Receive confirmation
│   ├── Make payment (bank transfer)
│   └── Payment reference from return
│
└── ARCHIVE
    ├── Save confirmation
    ├── Retain supporting documentation
    └── Record in filing register
```

---

## 7.4.6 Dutch QDMTT and Safe Harbours

### QDMTT (Nationale bijheffing)

```
Dutch QDMTT Implementation:
│
├── PURPOSE
│   ├── Ensures 15% minimum ETR on Dutch profits
│   ├── Collected before IIR/UTPR apply
│   ├── Reduces exposure to foreign top-up taxes
│   └── Retains tax revenue in Netherlands
│
├── WHEN APPLICABLE
│   ├── Dutch jurisdictional ETR below 15%
│   ├── Rare given 25.8% standard CIT rate
│   ├── May apply with:
│   │   ├── Innovation box (9% rate)
│   │   ├── Tonnage regime
│   │   └── Significant liquidation losses
│   └── Top-up calculated per GloBE rules
│
└── EFFECT
    ├── Dutch QDMTT reduces IIR/UTPR exposure
    ├── Foreign jurisdictions cannot collect
    └── Tax stays in Netherlands
```

### Safe Harbour Provisions

```
Dutch Safe Harbour Rules:
│
├── QDMTT SAFE HARBOUR
│   ├── Applies when foreign jurisdiction has qualifying QDMTT
│   ├── Dutch group companies exempt from separate calculation
│   ├── Reduces administrative burden
│   ├── Top-up tax deemed nil for that jurisdiction
│   └── Requires OECD-approved QDMTT in other jurisdiction
│
├── TRANSITIONAL CbCR SAFE HARBOUR
│   ├── Based on Country-by-Country Report data
│   ├── Simplified calculations permitted
│   ├── Three tests: De minimis, Simplified ETR, Routine profits
│   ├── Reduces compliance burden in early years
│   └── Transitional period application
│
├── TRANSITIONAL UTPR SAFE HARBOUR
│   ├── Applies to UPEs in non-Pillar 2 jurisdictions
│   ├── If UPE jurisdiction has statutory rate ≥ 20%
│   ├── No UTPR top-up tax required
│   ├── Applies to fiscal years ending before 31 December 2026
│   └── Temporary relief measure
│
└── PERMANENT SAFE HARBOUR
    ├── Framework agreed at OECD/IF level
    ├── Delegation basis in Dutch law for future implementation
    └── Check for updates on implementation
```

---

## 7.4.7 Penalties and Compliance

### Penalty Framework

```
Dutch Pillar Two Penalties:
│
├── LATE TOP-UP TAX RETURN (Standard Penalty)
│   ├── Failure to file or late filing
│   ├── Considered a "default" (verzuim)
│   ├── Penalty: €136
│   └── Per return
│
├── SERIOUS VIOLATIONS (GIR)
│   ├── Intentional or grossly negligent failure
│   ├── Applies to GIR filing obligations
│   ├── Maximum penalty: €900,000
│   ├── Criminal offence possible
│   └── Includes incomplete or incorrect filings
│
├── INTEREST ON LATE PAYMENT
│   ├── Standard tax interest rate applies
│   ├── Runs from payment deadline
│   └── Calculated daily
│
└── TRANSITIONAL RELIEF
    ├── OECD suggests mitigating fines in early years
    ├── Reasonable efforts defence may apply
    └── First-time compliance issues treated favourably
```

### Penalty Comparison Table

| Violation | Penalty | Notes |
|-----------|---------|-------|
| Late Top-up Tax Return | €136 | Standard late filing penalty |
| Late payment | Interest | Standard tax interest rate |
| Intentional/negligent GIR failure | Up to €900,000 | Serious offence |
| Incorrect information (minor) | Discretionary | May be corrected |
| Non-cooperation with audit | Escalating | Case-by-case |

---

## 7.4.8 Amendment Procedures

### Correcting Filed Returns

```
Amendment Process:
│
├── GIR AMENDMENTS
│   ├── Submit corrected GIR via portal
│   ├── Reference original submission
│   ├── No specific time limit stated
│   └── Notify Belastingdienst of correction
│
├── TOP-UP TAX RETURN AMENDMENTS
│   ├── Self-assessment rules apply
│   ├── Voluntary correction possible
│   ├── May result in additional payment or refund
│   └── Standard Algemene wet inzake rijksbelastingen rules
│
├── AFTER ASSESSMENT
│   ├── Request amendment from inspector
│   ├── Objection procedure available
│   ├── Appeal to Tax Court if needed
│   └── Time limits per Dutch fiscal law
│
└── DOCUMENTATION
    ├── Retain original and amended versions
    ├── Document reason for amendment
    └── Maintain clear audit trail
```

---

## 7.4.9 Deliverable: Netherlands Pillar Two Filing Checklist

```
NETHERLANDS PILLAR TWO FILING CHECKLIST
Groepsnaam/Group Name: ________________________________
Boekjaar/Fiscal Year: ____ / ____ / ____  to  ____ / ____ / ____
Dutch Filing Entity: ____________________________
KVK Number: ____________________________

═══════════════════════════════════════════════════════════════════════════════

SECTION A: PORTAL ACCESS
─────────────────────────────────────────────────────────────────────────────
☐ A1. Confirmed group meets €750m revenue threshold (2 of 4 years)
☐ A2. Identified Dutch filing entity
☐ A3. eHerkenning level 3 obtained:
      ☐ Regular eHerkenning 3, OR
      ☐ eHerkenning 3 Belastingdienst (Tax Service)
☐ A4. eHerkenning supplier: _________________
☐ A5. Tested login to Mijn Belastingdienst Zakelijk
☐ A6. Authorised users identified and set up
☐ A7. Confirmed portal functionality for Minimum Tax available

Portal Access Confirmed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION B: GloBE INFORMATION RETURN (Informatieaangifte)
─────────────────────────────────────────────────────────────────────────────
☐ B1. Determined filing approach:
      ☐ File GIR in Netherlands (proceed to B2-B12)
      ☐ GIR filed elsewhere - submit notification (proceed to B13-B16)

FOR GIR FILED IN NETHERLANDS:
☐ B2. GIR filing deadline calculated: _________________
☐ B3. GIR data compilation complete per OECD specification
☐ B4. All Constituent Entities included worldwide
☐ B5. Dutch jurisdictional section completed
☐ B6. QDMTT calculations included (if applicable)
☐ B7. Safe harbour elections documented
☐ B8. XML file generated per OECD Schema v1.0
☐ B9. Three-tier validation completed:
      ☐ Tier 1: Well-formedness PASS
      ☐ Tier 2: Schema validation PASS
      ☐ Tier 3: Business rules PASS
☐ B10. Logged in to Mijn Belastingdienst Zakelijk
☐ B11. Uploaded GIR XML file
☐ B12. Submission confirmation received: _________________

FOR GIR FILED ELSEWHERE (Notification):
☐ B13. GIR filed in jurisdiction: _________________
☐ B14. GIR filing date: ____ / ____ / ____
☐ B15. Notification submitted to Belastingdienst
☐ B16. Notification confirmation received: _________________

GIR/Notification Filed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION C: TOP-UP TAX RETURN (Aangifte minimumbelasting)
─────────────────────────────────────────────────────────────────────────────
☐ C1. Filing deadline calculated: _________________
☐ C2. Top-up tax liability calculated:
      QDMTT (Nationale bijheffing): € _________________
      IIR (Inkomensinsluitingsregel): € _________________
      UTPR (Onderbelaste winsten): € _________________
      TOTAL: € _________________
☐ C3. Allocation to Dutch entities documented
☐ C4. If no liability due:
      ☐ Confirmed no return required, OR
      ☐ Nil return filed (if required)
☐ C5. Logged in to Mijn Belastingdienst Zakelijk
☐ C6. Completed Top-up Tax Return
☐ C7. Reviewed for accuracy
☐ C8. Submitted return electronically
☐ C9. Submission confirmation received: _________________

Top-up Tax Return Filed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION D: PAYMENT
─────────────────────────────────────────────────────────────────────────────
☐ D1. Total liability confirmed: € _________________
☐ D2. Payment deadline: ____ / ____ / ____
☐ D3. Belastingdienst payment details obtained
☐ D4. Payment reference prepared
☐ D5. Bank transfer initiated
☐ D6. Payment confirmation received
☐ D7. Verified payment reflected in portal

Payment Made By: _____________ Date: ____ / ____ / ____ Amount: € _________

═══════════════════════════════════════════════════════════════════════════════

SECTION E: POST-FILING
─────────────────────────────────────────────────────────────────────────────
☐ E1. All confirmation documents archived
☐ E2. Filing register updated
☐ E3. XML file and validation records retained
☐ E4. Source documentation retained (7+ years per Dutch law)
☐ E5. Next period deadlines calendared:
      GIR Deadline (Year 2): _________________
      Top-up Tax Return Deadline (Year 2): _________________
☐ E6. Management briefed on filing completion

Post-Filing Completed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

CERTIFICATION
─────────────────────────────────────────────────────────────────────────────
Hierbij bevestig ik dat alle Nederlandse Pillar Two aangifteverplichtingen
voor het bovengenoemde boekjaar naar behoren zijn vervuld.

I confirm that all Dutch Pillar Two filing obligations for the above
fiscal year have been properly fulfilled.

Prepared By: _____________________________________________ Date: ____ / ____ / ____

Reviewed By: _____________________________________________ Date: ____ / ____ / ____

Approved By: _____________________________________________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════
```

---

## Key Resources and Links

### Belastingdienst Portals and Services

| Resource | URL |
|----------|-----|
| Mijn Belastingdienst Zakelijk | https://mijn.belastingdienst.nl/mbd-pmb/ |
| Minimum Tax Information | https://www.belastingdienst.nl/wps/wcm/connect/en/business/content/minimum-tax |
| Login and Authorisation Guide | https://www.belastingdienst.nl/wps/wcm/connect/en/business/content/mijn-belastingdienst-zakelijk-login-and-authorisation |
| How eHerkenning Works | https://www.belastingdienst.nl/wps/wcm/connect/en/business/content/this-is-how-eherkenning-works |
| Applying for eHerkenning | https://www.belastingdienst.nl/wps/wcm/connect/en/business/content/how-to-apply-for-eherkenning |

### eHerkenning

| Resource | URL |
|----------|-----|
| eHerkenning Main Site | https://www.eherkenning.nl/en/ |
| Applying for eHerkenning | https://www.eherkenning.nl/en/applying-eherkenning |
| Supplier Comparison | https://www.eherkenning.nl/en/suppliers |

### Legislation

| Resource | Reference |
|----------|-----------|
| Wet minimumbelasting 2024 | Staatsblad 2023, 504 |
| EU Directive 2022/2523 | EUR-Lex |
| Dutch Tax Code | Algemene wet inzake rijksbelastingen |

### Professional Guidance

| Resource | Source |
|----------|--------|
| Filing Obligations Guide | Grant Thornton NL |
| Pillar Two Updates | Meijburg & Co |
| QDMTT Analysis | Various NL tax advisers |

---

## Summary

The Netherlands' implementation through the Wet minimumbelasting 2024 creates a two-part filing obligation:

1. **GloBE Information Return** - File by 30 June 2026 (FY 2024, 18 months)
2. **Top-up Tax Return** - File and pay by 31 August 2026 (FY 2024, 20 months)

Key considerations for practitioners:
- Obtain eHerkenning level 3 well in advance
- Monitor portal development (system under construction)
- Standard €136 penalty for late return, but up to €900,000 for serious GIR violations
- Dutch 25.8% CIT rate means QDMTT rarely applies
- Safe harbour provisions reduce compliance burden

---

## Section Review Questions

1. What are the two filing obligations under Dutch Pillar Two law?

2. What is the deadline for the Top-up Tax Return for fiscal year 2024?

3. What level of eHerkenning is required for Mijn Belastingdienst Zakelijk?

4. What is the maximum penalty for intentional failure to file the GIR?

5. Why is Dutch QDMTT rarely applicable?

6. What is the difference between the GIR deadline and the Top-up Tax Return deadline?

**Answers:** 1) GIR and Top-up Tax Return; 2) 31 August 2026 (20 months); 3) Level 3 (EH3); 4) €900,000; 5) Standard Dutch CIT rate is 25.8%, well above 15% minimum; 6) GIR is 15/18 months, Top-up Tax Return is 17/20 months.

---

*Section 7.4 Complete. Proceed to Section 7.5: Singapore for Singapore-specific filing procedures.*
