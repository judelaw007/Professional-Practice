# Section 3: Understanding the GIR Structure

## 3.2 GIR Section 1: MNE Group Information

**Estimated Reading Time:** 30 minutes
**Pages:** 12-15

---

## Learning Objectives for This Section

By the end of this section, you will be able to:

- Complete Filing Constituent Entity identification fields accurately
- Report Ultimate Parent Entity information including TIN requirements
- Document the complete corporate structure with ownership percentages
- Assign correct GloBE status categories to each Constituent Entity
- Identify QIIR and UTPR applicability for each entity
- Complete the High-Level Summary (Section 1.4) with ETR ranges

---

## Overview of GIR Section 1

GIR Section 1 (MNE Group Information) is the **foundation** of your GloBE Information Return. It establishes:
- **Who** is filing the return
- **Who** is the Ultimate Parent Entity
- **What** entities comprise the MNE Group
- **How** those entities are structured and owned
- **Where** the group operates (jurisdiction summary)

**Data Points:** Section 1 contains approximately **50+ base data points**, which expand based on:
- Number of Constituent Entities in the group
- Number of ownership changes during the fiscal year
- Complexity of the corporate structure

---

## Section 1 Sub-Components

| Sub-Section | Content | Data Points |
|-------------|---------|-------------|
| **1.1** | Filing Constituent Entity Identification | 10-15 fields |
| **1.2** | Ultimate Parent Entity Information | 8-12 fields |
| **1.3** | Corporate Structure Information | 20+ fields per entity |
| **1.4** | High-Level Summary of GloBE Information | 9 columns per jurisdiction |

---

## 3.2.1 Filing Constituent Entity Identification

The Filing Constituent Entity (Filing CE) is the entity responsible for submitting the GIR. This may be the Ultimate Parent Entity (UPE) or a Designated Filing Entity (DFE) appointed by the group.

### Filing CE Data Elements

| Field | Description | Format | Source |
|-------|-------------|--------|--------|
| **Legal Name** | Full registered legal name of the Filing CE | Text | Corporate records |
| **TIN (Filing Jurisdiction)** | Tax Identification Number in the jurisdiction where filing | Jurisdiction-specific | Tax registration |
| **TIN Issuing Jurisdiction** | 2-character country code | ISO 3166-1 Alpha-2 | Tax registration |
| **Jurisdiction of Tax Residence** | Country where Filing CE is tax resident | ISO 3166-1 Alpha-2 | Tax status |
| **Jurisdiction for GloBE Purposes** | Country where Filing CE is located under GloBE | ISO 3166-1 Alpha-2 | GloBE determination |
| **Address** | Registered address of Filing CE | Free text | Corporate records |
| **Filing Status** | UPE or Designated Filing Entity | Selection | DFE election |
| **DFE Election Date** | Date DFE status was elected (if applicable) | YYYY-MM-DD | Election documentation |

### TIN Requirements

The Tax Identification Number (TIN) is critical for GIR filing. Follow these rules:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TIN DETERMINATION FLOWCHART                          │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────────────────┐
                    │   Does the Filing CE have a TIN  │
                    │   in the Filing Jurisdiction?    │
                    └──────────────────┬───────────────┘
                                       │
                         ┌─────────────┴─────────────┐
                         │                           │
                        YES                          NO
                         │                           │
                         ▼                           ▼
              ┌──────────────────┐      ┌──────────────────────────────┐
              │  Report the TIN  │      │  Does the Filing CE have a   │
              │  as issued       │      │  functional equivalent?      │
              └──────────────────┘      │  (e.g., business registration│
                                        │   number, company number)    │
                                        └──────────────────┬───────────┘
                                                           │
                                             ┌─────────────┴─────────────┐
                                             │                           │
                                            YES                          NO
                                             │                           │
                                             ▼                           ▼
                                  ┌──────────────────┐      ┌──────────────────┐
                                  │ Report functional│      │ Report "NOTIN"   │
                                  │ equivalent       │      │                  │
                                  └──────────────────┘      └──────────────────┘
```

**Important TIN Rules:**

| Rule | Requirement |
|------|-------------|
| **No blank fields** | TIN field must not be left blank or contain only spaces |
| **No punctuation** | Do not include punctuation in TIN |
| **NOTIN** | Use "NOTIN" only if no TIN or functional equivalent exists |
| **Jurisdiction code** | Always report the TIN-issuing jurisdiction |

### Filing CE Example

```
EXAMPLE: Filing Constituent Entity Data Entry
─────────────────────────────────────────────────────────────────────────────

Legal Name:                    GlobalCo Holdings Limited
TIN (Filing Jurisdiction):     GB123456789
TIN Issuing Jurisdiction:      GB
Jurisdiction of Tax Residence: GB
Jurisdiction for GloBE:        GB
Address:                       100 Corporate Way, London EC2N 1AB, United Kingdom
Filing Status:                 Designated Filing Entity
DFE Election Date:             2025-01-15
```

### Common Filing CE Errors

| Error | Impact | Prevention |
|-------|--------|------------|
| Wrong TIN format | Validation failure | Verify against tax registration |
| Missing jurisdiction code | Schema validation error | Always include 2-character code |
| Incorrect Filing Status | Wrong filing obligations | Confirm DFE election status |
| Old address | Potential correspondence issues | Verify current registered address |

**Template Reference:** Filing CE Identification Guide (Excel) - provided in course deliverables

---

## 3.2.2 Ultimate Parent Entity Information

The Ultimate Parent Entity (UPE) is the entity at the top of the MNE group that prepares the Consolidated Financial Statements. Even if a DFE files the GIR, UPE information must be reported.

### UPE Data Elements

| Field | Description | Format | Notes |
|-------|-------------|--------|-------|
| **Legal Name** | Full registered legal name of UPE | Text | Must match Consolidated Financial Statements |
| **TIN** | Tax Identification Number of UPE | Jurisdiction-specific | Use "NOTIN" if not issued |
| **TIN Issuing Jurisdiction** | Jurisdiction that issued the TIN | ISO 3166-1 Alpha-2 | Required unless NOTIN |
| **Jurisdiction for GloBE** | Country where UPE is located under GloBE | ISO 3166-1 Alpha-2 | Per GloBE location rules |
| **GloBE Status** | UPE classification for GloBE purposes | Selection list | See status categories below |
| **QIIR Status** | Whether UPE jurisdiction has QIIR in force | Yes/No | Check jurisdiction rules |
| **UTPR Status** | Whether UTPR applies to UPE jurisdiction | Yes/No | Check jurisdiction rules |
| **QDMTT Status** | Whether UPE jurisdiction has QDMTT in force | Yes/No | Check jurisdiction rules |

### UPE GloBE Status Categories

The UPE must be assigned one of the following GloBE status categories:

| Status | Description | When to Use |
|--------|-------------|-------------|
| **Ultimate Parent Entity** | Standard UPE | Most cases |
| **Flow-Through UPE** | UPE that is fiscally transparent | Partnership structures, transparent trusts |
| **Tax Neutral UPE** | UPE subject to deductible dividend regime | Certain investment vehicles |
| **Reference Entity** | Entity treated as UPE for GloBE | Multi-parented groups |

### Accounting Information for UPE

The GIR requires disclosure of the accounting framework used for the UPE's Consolidated Financial Statements.

| Field | Description | Options |
|-------|-------------|---------|
| **Financial Accounting Standard** | Standard used for Consolidated Financial Statements | IFRS, US GAAP, Other Acceptable Standard, Authorised Standard |
| **Presentation Currency** | Currency of Consolidated Financial Statements | ISO 4217 code (e.g., EUR, USD, GBP) |
| **Reporting Fiscal Year Start** | First day of the fiscal year | YYYY-MM-DD |
| **Reporting Fiscal Year End** | Last day of the fiscal year | YYYY-MM-DD |

**Acceptable Financial Accounting Standards:**

| Standard | Description |
|----------|-------------|
| **IFRS** | International Financial Reporting Standards (as issued by IASB) |
| **US GAAP** | United States Generally Accepted Accounting Principles |
| **Japan GAAP** | Japanese Generally Accepted Accounting Principles |
| **China GAAP** | Chinese Accounting Standards for Business Enterprises |
| **Other** | Other Acceptable or Authorised Financial Accounting Standard (specify) |

### UPE Example

```
EXAMPLE: Ultimate Parent Entity Data Entry
─────────────────────────────────────────────────────────────────────────────

Legal Name:                    GlobalCo International plc
TIN:                           GB987654321
TIN Issuing Jurisdiction:      GB
Jurisdiction for GloBE:        GB
GloBE Status:                  Ultimate Parent Entity
QIIR Status:                   Yes (UK QIIR in force from 2024)
UTPR Status:                   Yes (UK UTPR in force from Dec 2024)
QDMTT Status:                  Yes (UK QDMTT in force from 2024)

Accounting Information:
─────────────────────
Financial Accounting Standard: IFRS
Presentation Currency:         GBP
Reporting Fiscal Year Start:   2024-01-01
Reporting Fiscal Year End:     2024-12-31
```

### UPE Jurisdiction Rules Status

The GIR requires disclosure of whether the UPE jurisdiction has implemented GloBE charging rules:

| UPE Jurisdiction Status | Options |
|------------------------|---------|
| **QIIR applicable** | QIIR applicable to both Low-Taxed CEs located in other jurisdictions and in the jurisdiction |
| **QIIR applicable (other only)** | QIIR applicable to Low-Taxed CEs located in other jurisdictions only |
| **QIIR not applicable** | No QIIR in force in UPE jurisdiction |
| **QDMTT applicable** | QDMTT in force in UPE jurisdiction |
| **UTPR applicable** | UTPR in force in UPE jurisdiction |

**Template Reference:** UPE Data Collection Form (Excel) - provided in course deliverables

---

## 3.2.3 Corporate Structure Information

Section 1.3 is the most extensive part of GIR Section 1. It requires identification of **every entity** in the MNE Group's corporate structure, their ownership relationships, and their GloBE status.

### Corporate Structure Data Elements (Per Entity)

| Field | Description | Format |
|-------|-------------|--------|
| **Entity Name** | Full legal name | Text |
| **TIN** | Tax Identification Number | Jurisdiction-specific or "NOTIN" |
| **TIN Issuing Jurisdiction** | Country that issued TIN | ISO 3166-1 Alpha-2 |
| **Jurisdiction for GloBE** | Country where entity is located for GloBE | ISO 3166-1 Alpha-2 |
| **GloBE Status** | Entity classification for GloBE purposes | Selection list |
| **Ownership Percentage** | Percentage owned by parent entity | Decimal (0.0000 to 1.0000) |
| **Owning Entity** | Entity that holds ownership interest | Entity reference |
| **QIIR Applicability** | Whether QIIR applies to this entity | Yes/No |
| **UTPR Applicability** | Whether UTPR could apply | Yes/No |
| **Changes in Structure** | Any changes during fiscal year | Date + description |

### GloBE Status Categories for Constituent Entities

Each Constituent Entity must be assigned one of the following GloBE status categories:

**Standard Constituent Entity Types:**

| Status | Description | Reporting Impact |
|--------|-------------|------------------|
| **Constituent Entity** | Standard CE included in GloBE calculations | Full Section 3 reporting |
| **Permanent Establishment** | PE treated as separate CE | Separate jurisdictional reporting |
| **Main Entity** | Entity with PE(s) | Must allocate income to PEs |
| **Partially-Owned Parent Entity (POPE)** | Parent entity less than 100% owned | May create separate subgroup |
| **Minority-Owned Constituent Entity (MOCE)** | CE with less than 30% direct/indirect ownership | Separate calculation rules |

**Flow-Through and Transparent Entities:**

| Status | Description | Reporting Impact |
|--------|-------------|------------------|
| **Tax Transparent Entity** | Fiscally transparent in owner jurisdiction | Income allocated to owners |
| **Reverse Hybrid Entity** | Not transparent in entity jurisdiction, transparent in owner jurisdiction | Special treatment |
| **Flow-Through Entity** | Fiscally transparent where created | Income flows to owners |
| **Hybrid Entity** | Mixed transparency treatment | Case-by-case analysis |

**Excluded Entity Types:**

| Status | Description | Reporting Impact |
|--------|-------------|------------------|
| **Governmental Entity** | Government-owned entity meeting exclusion criteria | Excluded from GloBE calculations |
| **International Organisation** | Qualifying international organization | Excluded from GloBE calculations |
| **Non-Profit Organisation** | Qualifying non-profit | Excluded from GloBE calculations |
| **Pension Fund** | Qualifying pension fund | Excluded from GloBE calculations |
| **Investment Fund (UPE)** | Investment fund that is UPE | Excluded (with conditions) |
| **Real Estate Investment Vehicle** | REIV meeting exclusion criteria | Excluded from GloBE calculations |

**Special Categories:**

| Status | Description | Reporting Impact |
|--------|-------------|------------------|
| **Joint Venture** | JV meeting Article 6.4 definition | Separate JV Group treatment |
| **JV Subsidiary** | Entity owned by JV | Part of JV Group |
| **Excluded Entities (aggregate)** | Aggregate reporting for excluded entities | No TIN required |
| **Non-Group Member (aggregate)** | Entities no longer in group | Aggregate reporting |
| **Stateless Constituent Entity** | CE with no jurisdiction of tax residence | Special location rules |

### Ownership Percentage Reporting

Ownership percentages must be reported in **decimal format** (not percentage):

| Ownership | Decimal Format | Example |
|-----------|---------------|---------|
| 100% | 1.0000 | Wholly-owned subsidiary |
| 75% | 0.7500 | 75% ownership |
| 51% | 0.5100 | Majority ownership |
| 30% | 0.3000 | Minority threshold |
| 25.5% | 0.2550 | Quarter ownership |

**Precision:** The XML schema allows up to 4 decimal places for ownership percentages.

### Multi-Tier Ownership Structures

For complex ownership structures, report each tier in the ownership chain:

```
EXAMPLE: Multi-Tier Ownership Structure
─────────────────────────────────────────────────────────────────────────────

         GlobalCo International plc (UPE)
                     │
                     │ 100%
                     ▼
         GlobalCo Holdings Ltd (UK)
                     │
          ┌──────────┼──────────┐
          │          │          │
         100%       80%        60%
          │          │          │
          ▼          ▼          ▼
    GlobalCo    GlobalCo    GlobalCo
    Germany     France      Singapore
    GmbH        SAS         Pte Ltd
                     │
                    100%
                     │
                     ▼
                GlobalCo
                Malaysia
                Sdn Bhd

ENTITY REPORTING:
─────────────────
Entity                     Owner                      Ownership
──────────────────────────────────────────────────────────────────
GlobalCo International plc (UPE)                     N/A
GlobalCo Holdings Ltd      GlobalCo International    1.0000
GlobalCo Germany GmbH      GlobalCo Holdings Ltd     1.0000
GlobalCo France SAS        GlobalCo Holdings Ltd     0.8000
GlobalCo Singapore Pte     GlobalCo Holdings Ltd     0.6000
GlobalCo Malaysia Sdn      GlobalCo France SAS       1.0000
```

### QIIR and UTPR Applicability Indicators

For each Constituent Entity, you must indicate whether:

**QIIR Applicability (Section 1.3.2.1.12-1.3.2.1.13):**

| Indicator | Meaning |
|-----------|---------|
| **QIIR applies in CE jurisdiction** | The CE's jurisdiction has implemented QIIR |
| **QIIR applicable to this CE** | A Parent Entity is required to apply QIIR for this CE |
| **UPE ownership > aggregate QIIR ownership** | UPE owns more than the sum of all QIIR-applying parent interests |

**UTPR Applicability (Section 1.3.2.1.14-1.3.2.1.16):**

| Indicator | Meaning |
|-----------|---------|
| **UTPR may apply** | UTPR is in force in a jurisdiction where the MNE has CEs |
| **UTPR jurisdiction identified** | Jurisdiction where UTPR top-up tax may be payable |
| **UTPR inapplicable** | Leave blank if no UTPR taxing rights exist |

**Note (January 2025 Update):** The Filing Constituent Entity will not complete UTPR rows where no jurisdiction has taxing rights under the Under-Taxed Profits Rule.

### Reporting Changes in Corporate Structure

If any changes occurred during the Reporting Fiscal Year, report each change separately:

| Change Type | Data to Report |
|-------------|----------------|
| **Acquisition** | Date of acquisition, acquired entity, ownership percentage acquired |
| **Disposal** | Date of disposal, disposed entity, ownership percentage disposed |
| **Restructuring** | Date of change, entities affected, new structure |
| **Wind-up** | Date of wind-up, entity wound up |

**January 2025 Guidance on Wind-Ups:**
When a Constituent Entity is wound up during the Reporting Fiscal Year:
1. Report the GloBE status on the day of change **before** the transaction in `PreGloBEStatus`
2. Report "Non-Group Member" in `GloBEStatus`
3. Report ownership interests held on the day of change before the transaction
4. Report the change date

### Corporate Structure Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 CORPORATE STRUCTURE REPORTING WORKFLOW                      │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: List All Entities
─────────────────────────
    ├── All Constituent Entities
    ├── All Permanent Establishments
    ├── All Joint Ventures and JV Subsidiaries
    ├── All Excluded Entities (by category)
    └── All entities that left the group during the year
              │
              ▼
Step 2: Assign GloBE Status
───────────────────────────
    ├── Determine entity type (CE, PE, Flow-through, Excluded, etc.)
    ├── Verify status based on OECD Model Rules definitions
    └── Document basis for status determination
              │
              ▼
Step 3: Document Ownership Chain
────────────────────────────────
    ├── Identify direct owner for each entity
    ├── Calculate ownership percentage
    ├── Verify decimal format (4 decimal places)
    └── Trace ownership to UPE
              │
              ▼
Step 4: Determine QIIR/UTPR Applicability
─────────────────────────────────────────
    ├── Check if entity jurisdiction has QIIR
    ├── Identify Parent Entities with QIIR obligation
    ├── Check if UTPR may apply
    └── Document taxing rights jurisdictions
              │
              ▼
Step 5: Record Changes
──────────────────────
    ├── Identify all ownership changes during FY
    ├── Document change dates
    ├── Report pre-change and post-change status
    └── Complete separate row for each change
```

**Template Reference:** Constituent Entity Database Template (Excel) - provided in course deliverables

---

## 3.2.4 Summary Information (Section 1.4)

Section 1.4 provides a **High-Level Summary** of the MNE Group's GloBE position by jurisdiction. This section enables tax authorities to quickly identify where top-up tax liabilities may arise.

### Section 1.4 Data Elements

The High-Level Summary contains **9 columns** for each jurisdiction:

| Column | Field | Description |
|--------|-------|-------------|
| **1.4.1** | Jurisdiction | 2-character country code where CEs are located |
| **1.4.2** | ETR Range | Effective Tax Rate band (2.5% increments) |
| **1.4.3** | Safe Harbour Applies | Yes/No - whether safe harbour reduces reporting |
| **1.4.4** | SBIE Reduces Top-Up Tax to Nil | Yes/No |
| **1.4.5** | QDMTT Applies | Yes/No - whether QDMTT is payable in jurisdiction |
| **1.4.6** | IIR Applies | Yes/No - whether IIR applies for this jurisdiction |
| **1.4.7** | UTPR Applies | Yes/No - whether UTPR applies for this jurisdiction |
| **1.4.8** | Top-Up Tax Band (QDMTT) | Amount range if QDMTT applies |
| **1.4.9** | Top-Up Tax Band (IIR/UTPR) | Amount range if IIR/UTPR applies |

### ETR Range Bands (Column 1.4.2)

ETR must be reported in **2.5% increments** from 0% to above 30%:

| ETR Range | Selection |
|-----------|-----------|
| Below 0% | "Below 0%" |
| 0% to 2.5% | "0% to 2.5%" |
| 2.5% to 5% | "2.5% to 5%" |
| 5% to 7.5% | "5% to 7.5%" |
| 7.5% to 10% | "7.5% to 10%" |
| 10% to 12.5% | "10% to 12.5%" |
| 12.5% to 15% | "12.5% to 15%" |
| 15% to 17.5% | "15% to 17.5%" |
| 17.5% to 20% | "17.5% to 20%" |
| 20% to 22.5% | "20% to 22.5%" |
| 22.5% to 25% | "22.5% to 25%" |
| 25% to 27.5% | "25% to 27.5%" |
| 27.5% to 30% | "27.5% to 30%" |
| Above 30% | "Above 30%" |
| Not applicable | "N/A" (safe harbour applies) |

### Top-Up Tax Amount Bands (Columns 1.4.8 and 1.4.9)

Top-up tax amounts are reported in bands:

| Top-Up Tax Band | Selection |
|-----------------|-----------|
| No Top-Up Tax | "No Top-Up Tax" |
| €0 to €1m | "€0 to €1m" |
| €1m to €5m | "€1m to €5m" |
| €5m to €10m | "€5m to €10m" |
| €10m to €25m | "€10m to €25m" |
| €25m to €50m | "€25m to €50m" |
| €50m to €100m | "€50m to €100m" |
| €100m to €250m | "€100m to €250m" |
| €250m or above | "€250m or above" |

### Section 1.4 Completion Logic

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SECTION 1.4 COMPLETION FLOWCHART                         │
└─────────────────────────────────────────────────────────────────────────────┘

For Each Jurisdiction Where the MNE Has Constituent Entities:
─────────────────────────────────────────────────────────────

                    ┌──────────────────────────────────┐
                    │  Does a Safe Harbour Apply?      │
                    │  (Transitional CbCR/QDMTT)       │
                    └──────────────────┬───────────────┘
                                       │
                         ┌─────────────┴─────────────┐
                        YES                          NO
                         │                           │
                         ▼                           │
              ┌──────────────────────┐               │
              │ 1.4.2: Select "N/A"  │               │
              │ 1.4.3: Select "Yes"  │               │
              │ 1.4.4-1.4.9: Skip    │               │
              └──────────────────────┘               │
                                                     │
                                       ┌─────────────┴─────────────┐
                                       │                           │
                                       ▼                           │
                         ┌──────────────────────────────┐          │
                         │  Calculate ETR from Section 3│          │
                         │  and select appropriate band │          │
                         └──────────────────┬───────────┘          │
                                            │                      │
                                            ▼                      │
                         ┌──────────────────────────────┐          │
                         │  Is ETR ≥ 15%?               │          │
                         └──────────────────┬───────────┘          │
                                            │                      │
                              ┌─────────────┴─────────────┐        │
                             YES                          NO       │
                              │                           │        │
                              ▼                           ▼        │
                   ┌──────────────────┐      ┌──────────────────┐  │
                   │ No Top-Up Tax    │      │ Calculate Top-Up │  │
                   │ 1.4.4: May be Yes│      │ Tax from Sec. 3  │  │
                   │ 1.4.8/1.4.9: "No │      │ Select QDMTT/    │  │
                   │  Top-Up Tax"     │      │ IIR/UTPR band    │  │
                   └──────────────────┘      └──────────────────┘  │
```

### Section 1.4 Example

```
EXAMPLE: High-Level Summary for GlobalCo International plc
─────────────────────────────────────────────────────────────────────────────

Jurisdiction │ ETR Range  │ Safe   │ SBIE   │ QDMTT │ IIR │ UTPR │ QDMTT    │ IIR/UTPR
             │            │ Harb.  │ = Nil  │       │     │      │ Band     │ Band
─────────────┼────────────┼────────┼────────┼───────┼─────┼──────┼──────────┼──────────
GB           │ 20%-22.5%  │ No     │ No     │ Yes   │ N/A │ N/A  │ No TUT   │ N/A
DE           │ 17.5%-20%  │ No     │ No     │ Yes   │ No  │ No   │ No TUT   │ No TUT
FR           │ 15%-17.5%  │ No     │ No     │ No    │ Yes │ No   │ N/A      │ No TUT
IE           │ 12.5%-15%  │ No     │ No     │ Yes   │ Yes │ No   │ €1m-€5m  │ No TUT
SG           │ N/A        │ Yes    │ N/A    │ N/A   │ N/A │ N/A  │ N/A      │ N/A
LU           │ 10%-12.5%  │ No     │ Yes    │ No    │ Yes │ No   │ N/A      │ No TUT
HK           │ 5%-7.5%    │ No     │ No     │ Yes   │ Yes │ No   │ €5m-€10m │ No TUT
```

### January 2025 Update: QDMTT-Only Jurisdictions

The January 2025 OECD guidance clarifies that **QDMTT-only jurisdictions** (jurisdictions that only have QDMTT without IIR or UTPR) receive:
- Section 1 (MNE Group Information) **except** the High-Level Summary (Section 1.4)

This means Section 1.4 is primarily for:
- UPE jurisdiction
- Jurisdictions with IIR taxing rights
- Jurisdictions with UTPR taxing rights

### Completion Timing for Section 1.4

**Complete Section 1.4 LAST** - after all Section 3 calculations are finalized.

The data in Section 1.4 depends on:
- ETR calculations from Section 3.1
- Top-up tax calculations from Section 3.3
- Safe harbour determinations from Section 2

**Template Reference:** Summary Dashboard (Excel) - provided in course deliverables

---

## Section 1 Completion Checklist

Before proceeding to Section 2, verify the following:

### Filing CE Checklist

- [ ] Legal name matches corporate records exactly
- [ ] TIN verified against tax registration (or "NOTIN" if none)
- [ ] TIN issuing jurisdiction code correct (2-character)
- [ ] Jurisdiction for GloBE purposes determined
- [ ] Filing status confirmed (UPE or DFE)
- [ ] DFE election documented (if applicable)

### UPE Checklist

- [ ] Legal name matches Consolidated Financial Statements
- [ ] TIN verified (or "NOTIN" if none issued)
- [ ] GloBE status category assigned
- [ ] QIIR/UTPR/QDMTT status of UPE jurisdiction confirmed
- [ ] Accounting standard documented (IFRS, US GAAP, etc.)
- [ ] Presentation currency recorded (ISO 4217 code)
- [ ] Reporting fiscal year dates correct (YYYY-MM-DD format)

### Corporate Structure Checklist

- [ ] All Constituent Entities listed
- [ ] All permanent establishments included
- [ ] All joint ventures and JV subsidiaries listed
- [ ] All excluded entities identified and categorized
- [ ] GloBE status assigned to every entity
- [ ] Ownership percentages calculated (decimal format)
- [ ] Ownership chain traced to UPE
- [ ] QIIR applicability determined for each entity
- [ ] UTPR applicability determined for each entity
- [ ] All changes during fiscal year documented with dates

### High-Level Summary Checklist (Complete After Section 3)

- [ ] All jurisdictions where CEs are located included
- [ ] ETR range bands selected based on Section 3 calculations
- [ ] Safe harbour elections reflected
- [ ] SBIE nil determination reflected
- [ ] QDMTT/IIR/UTPR applicability indicated
- [ ] Top-up tax bands selected based on Section 3 calculations

---

## Common Errors in Section 1

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Missing entities** | Incomplete filing, potential penalties | Use comprehensive entity register |
| **Wrong TIN format** | XML validation failure | Verify against tax registration |
| **Incorrect ownership %** | Wrong allocation calculations | Calculate from statutory records |
| **Wrong GloBE status** | Incorrect tax treatment | Document basis for each determination |
| **ETR range mismatch** | Inconsistency with Section 3 | Complete 1.4 after Section 3 |
| **Missing changes** | Audit risk | Reconcile to corporate secretarial records |
| **Wrong jurisdiction codes** | Validation errors | Use ISO 3166-1 Alpha-2 only |
| **Ownership decimal error** | Wrong calculations | Use decimal format (0.0000-1.0000) |

---

## Next Steps

You now understand how to complete GIR Section 1 (MNE Group Information). The following subsections will cover safe harbour elections and the detailed GloBE computations.

---

## Sources and References

This section incorporates information from:

- [OECD GloBE Information Return (Pillar Two) - July 2023](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-pillar-two_10977da1/91a49ec3-en.pdf)
- [OECD GloBE Information Return (Pillar Two) XML Schema - January 2025](https://www.oecd.org/en/publications/globe-information-return-pillar-two-xml-schema_c594935a-en.html)
- [oecdpillars.com - A Review of Changes in the OECD's Updated January 2025 GloBE Information Return](https://oecdpillars.com/a-review-of-changes-in-the-oecds-updated-january-2025-globe-information-return/)
- [oecdpillars.com - Key Aspects of the GloBE Information Return Guidance](https://oecdpillars.com/key-aspects-of-the-globe-information-return-guidance/)
- [oecdpillars.com - Identify Constituent and Excluded Entities](https://oecdpillars.com/pillar-tab/identify-constituent-and-excluded-entities/)
- [KPMG - Pillar Two: GloBE Information Return](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/07/pillar-two-globe-information-return.pdf)
- [EY - OECD/G20 Inclusive Framework releases document on Pillar Two GloBE Information Return](https://www.ey.com/en_gl/technical/tax-alerts/oecd-g20-inclusive-framework-releases-document-on-pillar-two-glo)
- [Loyens & Loeff - GloBE Information Return](https://www.loyensloeff.com/insights/news--events/news/globe-information-return/)
- [Forvis Mazars - OECD public consultation on the GloBE information return](https://www.forvismazars.com/uk/en/industries/financial-services/thought-leadership/globe-information-return-what-you-need-to-know)
- [Citco - Pillar 2 update: getting to grips with the GloBE Information Return](https://www.citco.com/insights/pillar-2-update-getting-to-grips-with-the-globe-information-return)
- [Wolters Kluwer - Overcoming challenges in preparing GloBE Information Return](https://www.wolterskluwer.com/en-au/expert-insights/overcoming-challenges-in-preparing-for-beps-pillar-two)

---

*End of Section 3.2*
