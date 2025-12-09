# 5.2 Completing GIR Section 1: MNE Group Information

## Introduction

GIR Section 1 establishes the foundation of your GloBE Information Return by capturing essential information about your MNE Group: who is filing, what is the group structure, and what are the high-level GloBE results by jurisdiction.

Section 1 comprises four subsections with approximately **50+ data points**:

| Subsection | Description | Data Points |
|------------|-------------|-------------|
| **1.1** | Filing Constituent Entity Identification | ~8 fields |
| **1.2** | Ultimate Parent Entity Information | ~6 fields |
| **1.3** | Corporate Structure | ~15+ fields per entity |
| **1.4** | High-Level Summary | ~9 fields per jurisdiction |

This section provides step-by-step guidance for completing each subsection using the GIR Completion Calculator. Follow the instructions carefully—errors in Section 1 propagate throughout the GIR and can invalidate downstream calculations.

> **Important**: Section 1 information is shared with **all implementing jurisdictions** where the MNE Group has Constituent Entities. The High-Level Summary in Section 1.4 enables every implementing jurisdiction to identify where the MNE Group has Top-up Tax liability. Ensure accuracy and completeness.

---

## 5.2.1 Filing Constituent Entity Data

The Filing Constituent Entity (FCE) is the entity responsible for submitting the GIR. Section 1.1 identifies the FCE and provides general accounting information about the MNE Group.

### Who Can Be the Filing Constituent Entity?

| FCE Type | Definition | When Applicable |
|----------|------------|-----------------|
| **Ultimate Parent Entity (UPE)** | The entity at the top of the ownership chain | UPE files for entire group |
| **Designated Filing Entity (DFE)** | Entity designated by UPE to file on behalf of group | UPE designates another entity |
| **Designated Local Entity (DLE)** | Entity designated to file in a specific jurisdiction | Local filing requirement |
| **Constituent Entity** | Any CE filing its own return | No exchange agreement in place |

### Section 1.1 Data Entry: Filing Constituent Entity Identification

Navigate to the **S1_Filing_CE** worksheet in the calculator.

**Field-by-Field Completion Guide:**

| Row | Field | Description | Input Required | Example |
|-----|-------|-------------|----------------|---------|
| 1.1.1 | **Legal Name** | Full legal name of the FCE | Yes | "GlobalCo Holdings plc" |
| 1.1.2 | **Jurisdiction** | 2-letter ISO country code where FCE is located | Yes | "GB" |
| 1.1.3 | **TIN** | Tax Identification Number for Covered Taxes purposes | Yes | "GB123456789" |
| 1.1.4 | **Address** | Registered address of the FCE | Yes | "100 Finance Street, London EC2V 8AA" |
| 1.1.5 | **Is FCE the UPE?** | Whether the FCE is also the Ultimate Parent Entity | Yes (dropdown) | "Yes" or "No" |
| 1.1.6 | **FCE Role** | Type of Filing Constituent Entity | Yes (dropdown) | "UPE", "DFE", "DLE", "CE" |
| 1.1.7 | **Designated By** | If DFE or DLE, identify who designated the entity | Conditional | "GlobalCo Holdings plc" |
| 1.1.8 | **Contact Details** | Contact person name, email, phone | Optional | "John Smith, j.smith@globalco.com" |

**TIN Entry Guidance:**

| Scenario | TIN Entry | Notes |
|----------|-----------|-------|
| TIN available | Enter full TIN | Format varies by jurisdiction |
| No TIN (legitimate) | Enter "NOTIN" | Explain in supporting documentation |
| Functional equivalent | Enter equivalent | Business registration number acceptable |

**Calculator Interface - Section 1.1:**

```
┌─────────────────────────────────────────────────────────────────┐
│  S1_Filing_CE - Filing Constituent Entity Identification         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1.1 FILING CONSTITUENT ENTITY                                   │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  1.1.1 Legal Name                                                │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ [YELLOW INPUT]  GlobalCo Holdings plc                     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  1.1.2 Jurisdiction (ISO Code)                                   │
│  ┌──────────────────┐                                           │
│  │ [YELLOW INPUT] GB│ ◄── Select from dropdown                  │
│  └──────────────────┘                                           │
│                                                                  │
│  1.1.3 Tax Identification Number (TIN)                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ [YELLOW INPUT]  GB123456789                               │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ⚠️ TIN format validation: ✓ Valid UK format                    │
│                                                                  │
│  1.1.4 Registered Address                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ [YELLOW INPUT]  100 Finance Street, London EC2V 8AA       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  1.1.5 Is FCE the Ultimate Parent Entity?                        │
│  ┌──────────────────┐                                           │
│  │ [YELLOW INPUT] Yes│ ◄── Yes/No dropdown                      │
│  └──────────────────┘                                           │
│                                                                  │
│  1.1.6 Filing Role                                               │
│  ┌───────────────────────────────────────┐                      │
│  │ [YELLOW INPUT] Ultimate Parent Entity │ ◄── Role dropdown    │
│  └───────────────────────────────────────┘                      │
│                                                                  │
│  Section Validation: ✅ Complete                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Section 1.2 Data Entry: Ultimate Parent Entity Information

If the FCE is not the UPE, Section 1.2 captures UPE details. Navigate to the **S1_UPE** worksheet.

**Field-by-Field Completion Guide:**

| Row | Field | Description | Input Required | Example |
|-----|-------|-------------|----------------|---------|
| 1.2.1 | **UPE Legal Name** | Full legal name of the UPE | Yes | "GlobalCo Holdings plc" |
| 1.2.2 | **UPE Jurisdiction** | 2-letter ISO code where UPE is located | Yes | "GB" |
| 1.2.3 | **UPE TIN** | TIN used for Covered Taxes purposes | Yes | "GB123456789" |
| 1.2.4 | **QIIR Jurisdiction** | Jurisdiction requiring UPE to apply QIIR (Article 10.3.5) | Conditional | "GB" |
| 1.2.5 | **Accounting Standard** | Financial reporting standard used | Yes (dropdown) | "IFRS", "US GAAP", etc. |
| 1.2.6 | **Fiscal Year End** | Last day of the Reporting Fiscal Year | Yes | "31-Dec-2025" |

**Accounting Standard Options:**

| Code | Standard | When to Select |
|------|----------|----------------|
| IFRS | International Financial Reporting Standards | IFRS consolidated statements |
| USGAAP | US Generally Accepted Accounting Principles | US GAAP consolidated statements |
| UKGAAP | UK Generally Accepted Accounting Practice | UK GAAP consolidated statements |
| LOCALGAAP | Local GAAP | Other local standards |
| OTHER | Other acceptable standard | With explanation |

**Special Case: UPE is an Excluded Entity**

If the UPE is an Excluded Entity (e.g., government entity, pension fund, investment fund as UPE):

- Report UPE information in Section 1.2
- Note: TIN information is not required for Excluded Entity UPEs
- The POPE (Partially-Owned Parent Entity) or highest CE in the chain files the GIR

### General Accounting Information

The calculator automatically captures or derives:

| Data Point | Source | Purpose |
|------------|--------|---------|
| Reporting Fiscal Year | Setup worksheet | Period for GIR |
| Consolidated Revenue | Section 3 aggregation | €750M threshold verification |
| Consolidation Standard | Section 1.2.5 | Consistency check |
| First GloBE Year | Setup worksheet | Transition rules applicability |

### Common Errors and Prevention - Section 1.1/1.2

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Incorrect FCE jurisdiction** | GIR filed in wrong jurisdiction | Verify FCE tax residence, not just registration |
| **Invalid TIN format** | Filing rejection | Use jurisdiction-specific TIN format validation |
| **Missing QIIR jurisdiction** | Incomplete IIR allocation | Identify if UPE's jurisdiction has QIIR |
| **Wrong accounting standard** | Computation inconsistencies | Confirm standard used for consolidated FS |
| **FCE role mismatch** | Filing authority issues | Ensure DFE/DLE has proper designation |

---

## 5.2.2 Corporate Structure Data Entry

Section 1.3 is the most detailed part of Section 1, requiring information about **every Constituent Entity** in the MNE Group. For a 50-entity group, this section contains 750+ individual data points.

### Section 1.3 Overview

| Subsection | Content | Frequency |
|------------|---------|-----------|
| **1.3.1** | Group-level information | Once per GIR |
| **1.3.2** | CE and JV information | Per entity |
| **1.3.3** | Changes in corporate structure | Per change event |

### Entity Classification for GloBE Purposes

Before entering entity data, classify each entity according to GloBE status:

**Primary Classifications:**

| Status Code | Classification | Description |
|-------------|----------------|-------------|
| **UPE** | Ultimate Parent Entity | Top of ownership chain |
| **POPE** | Partially-Owned Parent Entity | Parent with minority shareholders above threshold |
| **IPE** | Intermediate Parent Entity | Parent entity below UPE |
| **CE** | Constituent Entity | Standard group member |
| **PE** | Permanent Establishment | Branch or PE of a CE |
| **FLOWTHROUGH** | Flow-Through Entity | Tax transparent in creation jurisdiction |
| **REVERSEHYBRID** | Reverse Hybrid Entity | Transparent in owner's jurisdiction, opaque in own |
| **STATELESS** | Stateless CE | Not tax resident anywhere |
| **INVENTENTITY** | Investment Entity | Investment Fund or REIV as CE |
| **INSRINVENT** | Insurance Investment Entity | Insurance company investment entity |
| **MINORITY** | Minority-Owned CE | CE with ownership < threshold |
| **EXCLUDED** | Excluded Entity | Government, pension fund, etc. |
| **JV** | Joint Venture | 50%+ owned but not consolidated |
| **JVSUB** | JV Subsidiary | Subsidiary of JV |

**Excluded Entity Sub-Classifications:**

| Code | Type | Eligibility Criteria |
|------|------|---------------------|
| GOVTENTITY | Government Entity | Government or political subdivision |
| INTLORG | International Organization | Recognized international organization |
| NONPROFIT | Non-Profit Organization | Qualifying NPO |
| PENSION | Pension Fund | Qualifying pension fund |
| INVFUND_UPE | Investment Fund (UPE) | Investment fund that is the UPE |
| REIV_UPE | Real Estate Investment Vehicle (UPE) | REIV that is the UPE |
| PENSIONSERV | Pension Services Entity | Services to pension fund |
| EXCLUDED_85 | 85% Excluded Entity Owned | 85%+ owned by excluded entities |

### Section 1.3.2 Data Entry: Constituent Entity Information

Navigate to the **S1_Corp_Structure** worksheet in the calculator.

**Field-by-Field Completion Guide for Each CE:**

| Row | Field | Description | Input Required | Example |
|-----|-------|-------------|----------------|---------|
| 1.3.2.1.1 | **CE Legal Name** | Full legal name | Yes | "GlobalCo GmbH" |
| 1.3.2.1.2 | **CE Jurisdiction** | 2-letter ISO code for tax residence | Yes | "DE" |
| 1.3.2.1.3 | **CE TIN** | TIN in jurisdiction of residence | Yes | "DE123456789" |
| 1.3.2.1.4 | **GloBE Status** | Classification per table above | Yes (dropdown) | "CE" |
| 1.3.2.1.5 | **Entity Type** | Legal form | Optional | "GmbH" |
| 1.3.2.1.6 | **Parent Entity** | Direct parent's legal name | Yes | "GlobalCo Holdings plc" |
| 1.3.2.1.7 | **Ownership %** | Direct ownership by parent | Yes | "100%" |
| 1.3.2.1.8 | **Indirect Ownership** | Ultimate ownership by UPE | Calculated | "100%" |
| 1.3.2.1.9 | **Consolidation Method** | How entity is consolidated | Yes (dropdown) | "Full" |
| 1.3.2.1.10 | **Fiscal Year End** | Entity's fiscal year end | Yes | "31-Dec-2025" |

**QIIR Indicator Fields (for Parent Entities only):**

| Row | Field | When to Complete |
|-----|-------|------------------|
| 1.3.2.1.11 | **QIIR Applicable?** | If jurisdiction has QIIR and entity is POPE/IPE |
| 1.3.2.1.12 | **QIIR Jurisdiction** | Jurisdiction where QIIR applies |
| 1.3.2.1.13 | **Aggregate QIIR Ownership** | Sum of ownership by QIIR parent entities |
| 1.3.2.1.14 | **UPE Ownership > QIIR Aggregate?** | Whether UPE ownership exceeds QIIR aggregate |

**UTPR Indicator Fields:**

| Row | Field | When to Complete |
|-----|-------|------------------|
| 1.3.2.1.15 | **UTPR Applicable?** | If jurisdiction has UTPR and UTPR allocation applies |
| 1.3.2.1.16 | **UTPR Jurisdiction** | Jurisdiction where UTPR applies |
| 1.3.2.1.17 | **UTPR Allocation Key** | Entity's UTPR allocation (employees + assets formula) |

> **Note (January 2025 Update)**: Articles 1.3.2.1.14 to 1.3.2.1.16 regarding UTPR applicability are not completed where no jurisdiction has taxing rights under the UTPR.

### Calculator Interface - Corporate Structure:

```
┌─────────────────────────────────────────────────────────────────┐
│  S1_Corp_Structure - Corporate Structure (Entity List)           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Entity #: 1 of 45                    [◄ Prev] [Next ►]         │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  1.3.2.1.1 Legal Name                                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ [YELLOW INPUT]  GlobalCo GmbH                             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  1.3.2.1.2 Jurisdiction        1.3.2.1.3 TIN                    │
│  ┌──────────┐                  ┌────────────────────────────┐   │
│  │ [INPUT] DE│                  │ [INPUT] DE123456789        │   │
│  └──────────┘                  └────────────────────────────┘   │
│                                                                  │
│  1.3.2.1.4 GloBE Status                                          │
│  ┌─────────────────────────────┐                                │
│  │ [INPUT] Constituent Entity ▼│                                │
│  └─────────────────────────────┘                                │
│                                                                  │
│  1.3.2.1.6 Parent Entity       1.3.2.1.7 Ownership %            │
│  ┌────────────────────────┐    ┌────────────┐                   │
│  │ GlobalCo Holdings plc ▼│    │ [INPUT] 100│ %                 │
│  └────────────────────────┘    └────────────┘                   │
│                                                                  │
│  1.3.2.1.9 Consolidation Method                                  │
│  ┌─────────────────────────────┐                                │
│  │ [INPUT] Full               ▼│                                │
│  └─────────────────────────────┘                                │
│                                                                  │
│  QIIR INDICATORS (Parent Entities Only)                          │
│  ─────────────────────────────────────                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ QIIR: Yes   ▼│ │ Jur: DE      │ │ Agg Own: 100%│            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                  │
│  UTPR INDICATORS                                                 │
│  ───────────────                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ UTPR: Yes   ▼│ │ Jur: DE      │ │ Alloc: 5.2%  │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                  │
│  Entity Validation: ✅ Complete                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Ownership Chain Documentation

The calculator automatically builds the ownership chain based on parent entity references. Verify the chain is correct:

**Example Ownership Chain:**

```
GlobalCo Holdings plc (UPE - UK)
├── GlobalCo UK Ltd (CE - UK) [100%]
├── GlobalCo GmbH (CE - DE) [100%]
│   └── GlobalCo Austria GmbH (CE - AT) [100%]
├── GlobalCo Inc (CE - US) [100%]
│   ├── GlobalCo Delaware LLC (CE - US) [100%]
│   └── GlobalCo Canada Inc (CE - CA) [100%]
├── GlobalCo Pte Ltd (IPE - SG) [100%]
│   ├── GlobalCo Malaysia Sdn Bhd (CE - MY) [100%]
│   └── GlobalCo HK Ltd (CE - HK) [100%]
├── GlobalCo BV (IPE - NL) [100%]
│   └── GlobalCo Luxembourg SARL (CE - LU) [100%]
└── GlobalCo IP Ltd (CE - IE) [100%]
```

### Joint Venture and JV Subsidiary Processing

JVs require special handling in Section 1.3:

| Scenario | GIR Treatment |
|----------|---------------|
| JV owned 50%+ (not consolidated) | Report as JV Group separate from main group |
| JV owned < 50% | Not a CE; exclude from GIR |
| JV Subsidiaries | Report under JV Group section |
| JV with multiple owners in group | Avoid double-counting |

**JV Data Entry Fields:**

| Field | Description |
|-------|-------------|
| JV Name | Legal name of Joint Venture |
| JV Jurisdiction | Tax residence of JV |
| JV TIN | TIN of JV |
| JV Parent Entity | Which group entity owns the JV interest |
| JV Ownership % | Ownership interest in JV |
| JV Subsidiaries | List of subsidiaries under the JV |

### Section 1.3.3: Changes in Corporate Structure

Report changes that occurred during the Reporting Fiscal Year:

| Change Type | Reporting Requirement |
|-------------|----------------------|
| **Acquisition** | New CE added during year |
| **Disposal** | CE sold/disposed during year |
| **Merger** | CE merged into another CE |
| **Liquidation** | CE wound up during year |
| **Restructuring** | Change in ownership chain |
| **Status Change** | Change in GloBE status |

**Change Event Data Entry:**

| Field | Description | Example |
|-------|-------------|---------|
| Change Type | Type of corporate change | "Acquisition" |
| Entity Affected | CE subject to change | "NewCo Ltd" |
| Change Date | Date of change | "01-Jul-2025" |
| Status Before | GloBE status before change | "Non-group Member" |
| Status After | GloBE status after change | "Constituent Entity" |
| Details | Explanation of change | "Acquired 100% of NewCo Ltd" |

> **January 2025 Update**: Where a CE is wound up during the Reporting Fiscal Year, report the relevant status for GloBE purposes on the day of the change before the transaction in 1.3.3.4 and "Non-group Member" in 1.3.3.5. Then identify the entities holding ownership interests.

### Excluded Entity Processing

For Excluded Entities, complete:

| Field | Description |
|-------|-------------|
| Entity Name | Legal name |
| Jurisdiction | Tax residence |
| Exclusion Type | Reason for exclusion (dropdown) |
| Exclusion Basis | Article reference (1.5.1 or 1.5.2) |
| Documentation | Supporting documentation reference |

**85% Excluded Entity Ownership Test:**

If claiming exclusion under 85% ownership by Excluded Entities:

1. Identify all owners and their status
2. Calculate aggregate excluded entity ownership
3. Verify ≥ 85% threshold is met
4. Confirm substantially all income is excluded dividends or equity gains/losses
5. Document the exclusion basis

### Multi-Tier Structure Handling

For complex structures with multiple tiers:

**Step 1: Start at UPE Level**
- Enter UPE as first entity
- Complete all UPE fields

**Step 2: Enter Direct Subsidiaries**
- For each direct subsidiary of UPE
- Reference UPE as parent entity
- Enter direct ownership percentage

**Step 3: Continue Down Each Branch**
- For each subsidiary, enter its subsidiaries
- Always reference immediate parent
- Calculator computes ultimate ownership

**Step 4: Verify Ownership Chain**
- Click [Verify Hierarchy]
- Resolve any circular references
- Confirm 100% ownership where applicable

### Worked Example: 50-Entity MNE Group

**Scenario**: GlobalCo Holdings plc is a UK-headquartered MNE with operations in 12 jurisdictions.

**Entity Summary:**

| Jurisdiction | # Entities | Key Entities |
|--------------|------------|--------------|
| United Kingdom | 5 | GlobalCo Holdings plc (UPE), GlobalCo UK Ltd |
| Germany | 3 | GlobalCo GmbH, GlobalCo Service GmbH |
| United States | 12 | GlobalCo Inc, GlobalCo Delaware LLC |
| Singapore | 4 | GlobalCo Pte Ltd (IPE), GlobalCo Services Pte |
| Netherlands | 3 | GlobalCo BV (IPE), GlobalCo Finance BV |
| Ireland | 3 | GlobalCo IP Ltd, GlobalCo Ireland Ltd |
| Luxembourg | 2 | GlobalCo Luxembourg SARL |
| France | 4 | GlobalCo SAS, GlobalCo France SARL |
| Australia | 3 | GlobalCo Australia Pty Ltd |
| Japan | 4 | GlobalCo KK |
| Hong Kong | 4 | GlobalCo HK Ltd |
| Canada | 3 | GlobalCo Canada Inc |
| **Total** | **50** | |

**Data Entry Approach:**

1. **Batch Entry by Jurisdiction**
   - Enter all UK entities first
   - Then Germany, US, etc.
   - Maintains logical grouping

2. **Validate Each Batch**
   - After each jurisdiction, run validation
   - Fix errors before proceeding

3. **Final Verification**
   - Click [Verify All Entities]
   - Review ownership chain diagram
   - Confirm entity count matches expectation

**Expected Validation Results:**

| Check | Expected Result |
|-------|-----------------|
| Entity Count | 50 entities |
| UPE Identified | GlobalCo Holdings plc |
| All entities have parent | ✅ |
| Ownership chains complete | ✅ |
| No circular references | ✅ |
| All TINs valid format | ✅ (or NOTIN with documentation) |

---

## 5.2.3 Summary Table Completion

Section 1.4 provides a high-level summary of GloBE results by jurisdiction. This section enables all implementing jurisdictions to identify where the MNE Group has Top-up Tax liability without requiring access to detailed Section 3 computations.

### Section 1.4 Overview

The High-Level Summary contains approximately **9 fields per jurisdiction**:

| Field | Description |
|-------|-------------|
| Jurisdiction | ISO country code |
| ETR Range | Effective Tax Rate in 2.5% increments |
| Safe Harbour Applied | Whether transitional safe harbour applies |
| Exclusion Applied | Whether exclusion applies |
| QDMTT Applies | Whether QDMTT is applicable |
| SBIE Exceeds Income | Whether SBIE reduces excess profit to nil |
| Top-up Tax Range | Range of Top-up Tax amount |
| IIR/UTPR Indicator | Which charging rule applies |
| Taxing Rights Jurisdiction | Jurisdiction(s) with taxing rights |

### ETR Range Bands

The GIR reports ETR in **2.5% increments from 0% to 30%**, with amounts above 30% reported as "Above 30%":

| Range Code | ETR Range | Indicates |
|------------|-----------|-----------|
| ETR_00_025 | 0% to 2.5% | Very low tax |
| ETR_025_05 | 2.5% to 5% | Low tax |
| ETR_05_075 | 5% to 7.5% | Low tax |
| ETR_075_10 | 7.5% to 10% | Low tax |
| ETR_10_125 | 10% to 12.5% | Below minimum |
| ETR_125_15 | 12.5% to 15% | Below minimum |
| ETR_15_175 | 15% to 17.5% | At or above minimum |
| ETR_175_20 | 17.5% to 20% | Above minimum |
| ETR_20_225 | 20% to 22.5% | Above minimum |
| ETR_225_25 | 22.5% to 25% | Above minimum |
| ETR_25_275 | 25% to 27.5% | Above minimum |
| ETR_275_30 | 27.5% to 30% | Above minimum |
| ETR_ABOVE_30 | Above 30% | Well above minimum |
| ETR_NA | Not Applicable | GloBE Loss or excluded |
| ETR_NOTCALC | Not Calculated | Safe harbour applied |

### Top-up Tax Range Bands

Top-up Tax amounts are also reported in bands:

| Range Code | Amount Range (€) |
|------------|-----------------|
| TUT_NIL | €0 (nil) |
| TUT_0_1M | €0 to €1 million |
| TUT_1M_5M | €1 million to €5 million |
| TUT_5M_10M | €5 million to €10 million |
| TUT_10M_25M | €10 million to €25 million |
| TUT_25M_50M | €25 million to €50 million |
| TUT_50M_100M | €50 million to €100 million |
| TUT_ABOVE_100M | Above €100 million |

### Section 1.4 Data Entry

Navigate to the **S1_Summary** worksheet in the calculator.

**Automatic Population:**

The calculator automatically populates Section 1.4 based on Section 3 computations:

| Field | Auto-Populated From |
|-------|---------------------|
| Jurisdiction | S3_GloBE_[JUR] worksheets |
| ETR | ETR calculation in Section 3 |
| Safe Harbour | Section 2 elections |
| QDMTT | Section 2 QDMTT status |
| SBIE Excess | SBIE vs. GloBE Income comparison |
| Top-up Tax Range | Section 3 Top-up Tax calculation |
| Taxing Rights | IIR/UTPR allocation |

**Manual Entry Required:**

| Field | When Manual Entry Needed |
|-------|-------------------------|
| ETR Range | If using Transitional Simplified Reporting |
| Safe Harbour | If not using calculator Section 2 |
| Special circumstances | Unusual situations not captured automatically |

### Calculator Interface - Section 1.4 Summary:

```
┌─────────────────────────────────────────────────────────────────┐
│  S1_Summary - High-Level Summary by Jurisdiction                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Jurisdiction Summary (Auto-populated from Section 3)            │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  ┌─────┬──────────┬────────────┬───────┬────────┬───────────┐  │
│  │ Jur │ ETR Range│ Safe Harb. │ QDMTT │ Top-up │ Taxing    │  │
│  │     │          │            │       │ Range  │ Rights    │  │
│  ├─────┼──────────┼────────────┼───────┼────────┼───────────┤  │
│  │ GB  │ 20-22.5% │ No         │ Yes   │ Nil    │ N/A       │  │
│  │ DE  │ 25-27.5% │ No         │ Yes   │ Nil    │ N/A       │  │
│  │ US  │ 17.5-20% │ No         │ No    │ Nil    │ N/A       │  │
│  │ SG  │ 7.5-10%  │ No         │ No    │ €1M-5M │ GB (IIR)  │  │
│  │ NL  │ 22.5-25% │ No         │ Yes   │ Nil    │ N/A       │  │
│  │ IE  │ 12.5-15% │ CbCR SH    │ No    │ N/Calc │ N/A       │  │
│  │ LU  │ 22.5-25% │ No         │ Yes   │ Nil    │ N/A       │  │
│  │ FR  │ 25-27.5% │ No         │ Yes   │ Nil    │ N/A       │  │
│  │ AU  │ 27.5-30% │ No         │ Yes   │ Nil    │ N/A       │  │
│  │ JP  │ 27.5-30% │ No         │ No    │ Nil    │ N/A       │  │
│  │ HK  │ 10-12.5% │ No         │ No    │ €1M-5M │ GB (IIR)  │  │
│  │ CA  │ 25-27.5% │ No         │ Yes   │ Nil    │ N/A       │  │
│  └─────┴──────────┴────────────┴───────┴────────┴───────────┘  │
│                                                                  │
│  Summary Statistics:                                             │
│  • Jurisdictions with ETR < 15%: 3 (SG, IE, HK)                 │
│  • Jurisdictions with Safe Harbour: 1 (IE)                      │
│  • Total Top-up Tax Range: €2M - €10M                           │
│  • Taxing Rights: GB (IIR) for SG, HK                           │
│                                                                  │
│  [GREEN CALC] = Auto-calculated from Section 3                   │
│                                                                  │
│  Section Validation: ✅ Complete                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### When ETR Is Not Calculated

The FCE will not complete the ETR high-level summary if:

| Scenario | ETR Reporting | Reason |
|----------|---------------|--------|
| GloBE Loss in jurisdiction | ETR_NA | Cannot calculate ETR with negative denominator |
| Safe Harbour applied | ETR_NOTCALC | Full computation not required |
| Excluded jurisdiction | ETR_NA | Not subject to GloBE |
| De minimis exclusion | ETR_NA | Revenue and profit below thresholds |

### QDMTT-Only Jurisdictions

Per the January 2025 update, QDMTT-only jurisdictions receive Section 1 information **except** for the High-Level Summary in Section 1.4.

| Information Shared | QDMTT-Only Jurisdiction |
|--------------------|------------------------|
| Section 1.1 (FCE) | ✅ Yes |
| Section 1.2 (UPE) | ✅ Yes |
| Section 1.3 (Corporate Structure) | ✅ Yes |
| Section 1.4 (High-Level Summary) | ❌ No |

### Validation Check Interpretation

The calculator validates Section 1.4 completeness:

| Validation Check | Meaning | Resolution |
|------------------|---------|------------|
| ✅ ETR range populated | ETR correctly categorized | None |
| ⚠️ ETR < 15% | Jurisdiction may be low-taxed | Review Section 3 calculation |
| ❌ ETR missing | ETR not calculated | Complete Section 3 or enter Safe Harbour |
| ⚠️ Top-up Tax > €0 | Tax liability exists | Verify IIR/UTPR allocation |
| ✅ Taxing rights identified | Charging mechanism clear | None |

---

## 5.2.4 Section 1 Completion Checklist

Before proceeding to Section 2, verify Section 1 is complete:

### Filing Constituent Entity (1.1)

| # | Checkpoint | Status |
|---|------------|--------|
| 1 | FCE legal name entered correctly | ☐ |
| 2 | FCE jurisdiction is correct (tax residence) | ☐ |
| 3 | FCE TIN is valid format or "NOTIN" documented | ☐ |
| 4 | FCE role correctly identified | ☐ |
| 5 | If DFE/DLE, designation documented | ☐ |

### Ultimate Parent Entity (1.2)

| # | Checkpoint | Status |
|---|------------|--------|
| 6 | UPE legal name entered correctly | ☐ |
| 7 | UPE jurisdiction is correct | ☐ |
| 8 | UPE TIN is valid (unless Excluded Entity) | ☐ |
| 9 | QIIR jurisdiction identified if applicable | ☐ |
| 10 | Accounting standard selected | ☐ |
| 11 | Fiscal year end date correct | ☐ |

### Corporate Structure (1.3)

| # | Checkpoint | Status |
|---|------------|--------|
| 12 | All Constituent Entities entered | ☐ |
| 13 | All entities have valid GloBE status | ☐ |
| 14 | All entities have parent entity reference | ☐ |
| 15 | Ownership percentages sum correctly | ☐ |
| 16 | Ownership chain verified (no errors) | ☐ |
| 17 | QIIR indicators complete for parent entities | ☐ |
| 18 | UTPR indicators complete where applicable | ☐ |
| 19 | JVs and JV subsidiaries separately reported | ☐ |
| 20 | Excluded entities documented with basis | ☐ |
| 21 | Changes in structure during year reported | ☐ |

### High-Level Summary (1.4)

| # | Checkpoint | Status |
|---|------------|--------|
| 22 | All jurisdictions listed | ☐ |
| 23 | ETR ranges correctly assigned | ☐ |
| 24 | Safe harbour elections reflected | ☐ |
| 25 | QDMTT status indicated | ☐ |
| 26 | Top-up Tax ranges assigned | ☐ |
| 27 | Taxing rights jurisdictions identified | ☐ |
| 28 | Summary validates against Section 3 | ☐ |

### Section 1 Overall Validation

| # | Checkpoint | Status |
|---|------------|--------|
| 29 | No critical errors in validation dashboard | ☐ |
| 30 | All warnings reviewed and explained | ☐ |
| 31 | Section 1 sign-off obtained | ☐ |

---

## Summary: Section 1 Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                  Section 1 Data Flow Summary                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT REQUIRED                                                  │
│  ─────────────                                                   │
│  • FCE identification and role                                  │
│  • UPE identification and accounting basis                      │
│  • All CE details with GloBE status                             │
│  • Ownership chain information                                  │
│  • QIIR and UTPR indicators                                     │
│  • Changes in corporate structure                               │
│                                                                  │
│  AUTO-CALCULATED                                                 │
│  ───────────────                                                 │
│  • Ultimate ownership percentages                               │
│  • Ownership chain hierarchy                                    │
│  • ETR ranges (from Section 3)                                  │
│  • Top-up Tax ranges (from Section 3)                           │
│  • Taxing rights allocation                                     │
│                                                                  │
│  OUTPUT TO OTHER SECTIONS                                        │
│  ────────────────────────                                        │
│  • Entity list → Section 3 worksheets                           │
│  • Jurisdiction list → Section 2, Section 3                     │
│  • Ownership data → IIR/UTPR allocation                         │
│  • Summary data → XML output                                    │
│                                                                  │
│  SHARED WITH ALL JURISDICTIONS                                   │
│  ─────────────────────────────                                   │
│  • Section 1.1, 1.2, 1.3 → All implementing jurisdictions       │
│  • Section 1.4 → All except QDMTT-only jurisdictions            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

1. **Section 1 establishes the GIR foundation** - FCE, UPE, corporate structure, and summary

2. **TIN requirements are strict** - Enter valid TIN or "NOTIN" with documentation

3. **Entity classification is critical** - Correct GloBE status affects all downstream calculations

4. **Ownership chains must be complete** - Every entity needs a parent reference to UPE

5. **QIIR and UTPR indicators determine charging mechanism** - Complete for all parent entities

6. **Section 1.4 is shared with all jurisdictions** - Enables identification of Top-up Tax liability

7. **ETR is reported in 2.5% bands** - Not exact percentage

8. **January 2025 updates affect corporate structure reporting** - Especially for wound-up entities

9. **Validation before proceeding** - Complete Section 1 checklist before moving to Section 2

---

## Sources and References

- [OECD: GloBE Information Return (Pillar Two) - July 2023](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-pillar-two_10977da1/91a49ec3-en.pdf)
- [oecdpillars.com: A Review of Changes in the OECD's Updated January 2025 GloBE Information Return](https://oecdpillars.com/a-review-of-changes-in-the-oecds-updated-january-2025-globe-information-return/)
- [oecdpillars.com: Key Aspects of the GloBE Information Return Guidance](https://oecdpillars.com/key-aspects-of-the-globe-information-return-guidance/)
- [KPMG: Pillar Two GloBE Information Return](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/07/pillar-two-globe-information-return.pdf)
- [Citco: Pillar 2 Update - Getting to Grips with the GloBE Information Return](https://www.citco.com/insights/pillar-2-update-getting-to-grips-with-the-globe-information-return)
- [oecdpillars.com: Identify Constituent and Excluded Entities](https://oecdpillars.com/pillar-tab/identify-constituent-and-excluded-entities/)
- [oecdpillars.com: Investment Funds and Pillar Two](https://oecdpillars.com/pillar-tab/investment-funds-and-pillar-two/)
- [Macfarlanes: Unpacking Pillar Two - Treatment of Flow-Through Entities](https://www.macfarlanes.com/what-we-think/2022/unpacking-pillar-two-treatment-of-flow-through-entities/)
- [EY: OECD/G20 Inclusive Framework Releases Document on Pillar Two GloBE Information Return](https://www.ey.com/en_gl/technical/tax-alerts/oecd-g20-inclusive-framework-releases-document-on-pillar-two-glo)
- [Loyens & Loeff: GloBE Information Return](https://www.loyensloeff.com/insights/news--events/news/globe-information-return/)

---

*This section provides comprehensive guidance for completing GIR Section 1: MNE Group Information. The following subsections will cover safe harbour elections and detailed GloBE computations.*
