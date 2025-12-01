# Section 10.2: Scenario 2 - Complex Ownership Structure

## Learning Objectives

By the end of this section, you will be able to:

- Identify and classify Partially-Owned Parent Entities (POPEs)
- Apply special rules for Minority-Owned Constituent Entities (MOCEs)
- Handle Joint Venture structures under GloBE rules
- Calculate ownership percentages in multi-tiered structures
- Correctly allocate Top-up Tax across complex ownership chains
- Report complex structures in GIR Sections 1 and 3

---

## Scenario Overview

### The Facts

**Meridian Industrial Group plc** is a UK-headquartered multinational with a complex ownership structure involving multiple tiers, joint ventures, and minority investments.

**Group Profile:**

| Attribute | Detail |
|-----------|--------|
| **Ultimate Parent Entity** | Meridian Industrial Group plc (UK) |
| **Fiscal Year End** | 31 December 2024 |
| **Consolidated Revenue** | €2.8 billion |
| **Total Constituent Entities** | 120 |
| **Joint Ventures** | 3 |
| **Minority-Owned Subgroups** | 1 |
| **Partially-Owned Parent Entities** | 2 |

### Complex Structure Diagram

```
MERIDIAN INDUSTRIAL GROUP - OWNERSHIP STRUCTURE
================================================

                    Meridian Industrial Group plc
                           (UK - UPE)
                          100% owned
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   Meridian Europe        Meridian APAC          Meridian Americas
      Holdings BV          Holdings Pte              Holdings Inc
    (Netherlands)          (Singapore)               (USA)
       100%                   100%                    100%
        │                      │                      │
        │                      │                      │
   ┌────┴────┐            ┌────┴────┐           ┌────┴────┐
   │         │            │         │           │         │
Meridian   Meridian    Meridian  Meridian    Meridian  Meridian
Germany    France       China     Japan       Canada    Mexico
  GmbH      SAS         Ltd        KK          Ltd      S de RL
  100%      100%        100%      100%         100%      100%


COMPLEX OWNERSHIP SITUATIONS:
=============================

1. PARTIALLY-OWNED PARENT ENTITY (POPE):

   Meridian Industrial Group plc (UPE)
              │
              ├── 70% ──────────────────────┐
              │                             │
              │                    ┌────────▼────────┐
              │                    │  Meridian Tech   │
              │                    │   Ventures BV    │◄── 30% External
              │                    │  (Netherlands)   │    Investors
              │                    │     [POPE]       │
              │                    └────────┬─────────┘
              │                             │
              │                    ┌────────┴─────────┐
              │                    │                  │
              │              Meridian AI        Meridian
              │               Ireland Ltd       Quantum GmbH
              │               (Ireland)         (Germany)
              │                 100%              100%


2. JOINT VENTURE (50% Equity Method):

   Meridian Industrial Group plc (UPE)
              │
              ├── 50% ──────────────────────┐
              │                             │
              │                    ┌────────▼────────┐
   Strategic Partner ──► 50%      │   MeridiaTech    │
      (External)                  │    JV LLC        │
                                  │     (USA)        │
                                  │  [JV - Equity    │
                                  │    Method]       │
                                  └────────┬─────────┘
                                           │
                                  ┌────────┴─────────┐
                                  │                  │
                              JV OpCo 1         JV OpCo 2
                              (Delaware)        (California)
                                100%              100%


3. MINORITY-OWNED SUBGROUP (≤30% but control):

   Meridian Industrial Group plc (UPE)
              │
              ├── 25% (but has control via ──────────────┐
              │    shareholder agreement)                │
              │                                 ┌────────▼────────┐
   Other Investors ──► 75%                      │  Meridian Green  │
                                               │   Energy Ltd     │
                                               │  (Ireland)       │
                                               │  [MOCE - Head]   │
                                               └────────┬─────────┘
                                                        │
                                               ┌────────┴─────────┐
                                               │                  │
                                           Green Wind        Solar Power
                                           Holdings Ltd      Holdings Ltd
                                           (Ireland)         (Netherlands)
                                             100%              100%
                                         [MOS member]      [MOS member]
```

---

## Part 1: Partially-Owned Parent Entity (POPE)

### 1.1 Identifying the POPE

**Definition (Article 10, OECD Model Rules):**

A Partially-Owned Parent Entity (POPE) is a Constituent Entity that:
1. Owns (directly or indirectly) an Ownership Interest in another Constituent Entity
2. Has more than 20% of its Ownership Interests in profits held by non-group persons

**Meridian Tech Ventures BV Analysis:**

```
POPE IDENTIFICATION - MERIDIAN TECH VENTURES BV
===============================================

Ownership Analysis:
  Meridian Industrial Group plc owns:        70%
  External investors own:                    30%

Threshold Test:
  External ownership (30%) > 20%?            YES

Subsidiary Ownership:
  Owns Meridian AI Ireland Ltd (100%)?       YES
  Owns Meridian Quantum GmbH (100%)?         YES

RESULT: Meridian Tech Ventures BV is a POPE
```

### 1.2 POPE Implications for IIR

When a POPE exists, the IIR operates differently:

**Standard IIR Flow (No POPE):**
```
UPE (UK) ────► Applies IIR to all low-taxed subsidiaries
               └── Collects 100% of Top-up Tax
```

**IIR Flow with POPE:**
```
UPE (UK) ────► Applies IIR to directly-owned low-taxed entities

POPE (NL) ───► Applies IIR to its low-taxed subsidiaries
               └── Collects Top-up Tax proportionate to external ownership
               └── UPE reduces its IIR by POPE's share
```

### 1.3 POPE Calculation Example

**Assume:** Meridian AI Ireland Ltd (100% owned by POPE) has a low ETR

```
POPE TOP-UP TAX ALLOCATION
==========================

Meridian AI Ireland Ltd:
  GloBE Income:                    €25,000,000
  Adjusted Covered Taxes:           €2,875,000
  ETR:                                  11.5%
  Top-up Tax %:                          3.5%
  SBIE:                             €1,500,000
  Excess Profit:                   €23,500,000
  Total Top-up Tax:                   €822,500

Allocation between POPE and UPE:

POPE (Meridian Tech Ventures BV):
  POPE's ownership of subsidiary:        100%
  External investors in POPE:             30%
  POPE's allocable share of Top-up Tax:
    €822,500 × 30% = €246,750

  ► POPE (if in IIR jurisdiction) would charge
    €246,750 to protect external investors

UPE (Meridian Industrial Group plc):
  UPE's indirect ownership:               70%
  UPE's allocable share:
    €822,500 × 70% = €575,750

  ► UPE charges €575,750 under UK IIR

TOTAL TOP-UP TAX: €246,750 + €575,750 = €822,500 ✓
```

### 1.4 GIR Reporting for POPE

**Section 1 - Corporate Structure:**

```xml
<!-- POPE REPORTING IN GIR -->

<CorporateStructure>
  <Entity>
    <Name>Meridian Tech Ventures BV</Name>
    <JurisdictionCode>NL</JurisdictionCode>
    <TIN issuedBy="NL">NL123456789B01</TIN>
    <EntityType>POPE</EntityType>
    <ParentEntity>
      <Name>Meridian Industrial Group plc</Name>
      <OwnershipPercentage>70.00</OwnershipPercentage>
    </ParentEntity>
    <ExternalOwnership>30.00</ExternalOwnership>
    <Subsidiaries>
      <Subsidiary>
        <Name>Meridian AI Ireland Ltd</Name>
        <OwnershipPercentage>100.00</OwnershipPercentage>
      </Subsidiary>
      <Subsidiary>
        <Name>Meridian Quantum GmbH</Name>
        <OwnershipPercentage>100.00</OwnershipPercentage>
      </Subsidiary>
    </Subsidiaries>
  </Entity>
</CorporateStructure>
```

**Section 3 - Entity Data with POPE Allocation:**

```xml
<!-- ENTITY DATA WITH POPE ALLOCATION -->

<EntityInfo>
  <Entity>
    <Name>Meridian AI Ireland Ltd</Name>
    <JurisdictionCode>IE</JurisdictionCode>
    <EntityType>CE</EntityType>
    <OwnershipChain>
      <Level1>
        <ParentName>Meridian Tech Ventures BV</ParentName>
        <ParentType>POPE</ParentType>
        <DirectOwnership>100.00</DirectOwnership>
      </Level1>
      <Level2>
        <ParentName>Meridian Industrial Group plc</ParentName>
        <ParentType>UPE</ParentType>
        <IndirectOwnership>70.00</IndirectOwnership>
      </Level2>
    </OwnershipChain>
    <GloBEData>
      <GloBEIncome currCode="EUR">25000000</GloBEIncome>
      <CoveredTaxes currCode="EUR">2875000</CoveredTaxes>
      <TopUpTaxTotal currCode="EUR">822500</TopUpTaxTotal>
      <TopUpTaxAllocation>
        <AllocatedToPOPE currCode="EUR">246750</AllocatedToPOPE>
        <AllocatedToUPE currCode="EUR">575750</AllocatedToUPE>
      </TopUpTaxAllocation>
    </GloBEData>
  </Entity>
</EntityInfo>
```

---

## Part 2: Joint Venture Structures

### 2.1 Joint Venture Definition

**Article 10, OECD Model Rules:**

A Joint Venture is an entity whose financial results are:
- Reported under the **equity method** in the Consolidated Financial Statements
- The UPE holds directly or indirectly **at least 50%** of its Ownership Interests

**Key Point:** Equity-accounted investments with <50% ownership are NOT Joint Ventures under GloBE—they are excluded from scope.

### 2.2 MeridiaTech JV Analysis

```
JOINT VENTURE CLASSIFICATION
============================

Entity: MeridiaTech JV LLC (USA)

Ownership:
  Meridian Industrial Group plc:     50%
  Strategic Partner (external):      50%

Accounting Treatment:
  Equity method in Meridian's consolidated FS?  YES

JV Test:
  At least 50% owned by UPE?                    YES (exactly 50%)

RESULT: MeridiaTech JV LLC is a JOINT VENTURE under GloBE
```

### 2.3 JV Treatment Under GloBE

Joint Ventures are treated as a **separate MNE group** for GloBE purposes:

```
JV TREATMENT UNDER GLOBE RULES
==============================

MeridiaTech JV LLC and its subsidiaries:
  ► Treated as a separate MNE Group
  ► MeridiaTech JV LLC is treated as the "UPE" of this group
  ► JV subsidiaries (JV OpCo 1, JV OpCo 2) are CEs of JV group

Implications:
  ► JV Group has its own jurisdictional ETR calculations
  ► JV Group has its own Top-up Tax calculations
  ► NO blending with main group's entities in same jurisdiction
  ► UPE (Meridian) applies IIR to its 50% share of JV Top-up Tax
```

### 2.4 JV GloBE Calculation

**Assume:** JV Group has low-taxed operations in Delaware

```
JV GROUP GLOBE CALCULATION
==========================

JV Group Entities:
  MeridiaTech JV LLC (USA - Delaware)
  JV OpCo 1 (USA - Delaware)
  JV OpCo 2 (USA - California)

Delaware Jurisdiction (low state tax):
  Aggregate GloBE Income:              €15,000,000
  Aggregate Covered Taxes:              €1,800,000
  Jurisdictional ETR:                       12.0%
  Top-up Tax %:                              3.0%
  SBIE:                                 €2,200,000
  Excess Profit:                       €12,800,000
  JV Group Top-up Tax:                    €384,000

California (normal taxation):
  Aggregate GloBE Income:               €8,000,000
  Aggregate Covered Taxes:              €2,080,000
  Jurisdictional ETR:                       26.0%
  Top-up Tax %:                              0.0%

TOTAL JV GROUP TOP-UP TAX: €384,000 (Delaware only)

Meridian's Share (50%):
  IIR Charge = €384,000 × 50% = €192,000

Strategic Partner's Share (50%):
  IIR Charge (if in IIR jurisdiction) = €192,000
  OR no charge if partner not in IIR jurisdiction
```

### 2.5 GIR Reporting for Joint Ventures

Joint Ventures are reported in a **separate section** of the GIR:

```xml
<!-- JOINT VENTURE REPORTING IN GIR -->

<JVGroupInfo>
  <JVGroup>
    <JVName>MeridiaTech JV LLC Group</JVName>
    <JVHeadEntity>
      <Name>MeridiaTech JV LLC</Name>
      <JurisdictionCode>US</JurisdictionCode>
      <TIN issuedBy="US">12-3456789</TIN>
    </JVHeadEntity>

    <OwnershipByUPE>50.00</OwnershipByUPE>

    <JVMembers>
      <Member>
        <Name>MeridiaTech JV LLC</Name>
        <Jurisdiction>US</Jurisdiction>
      </Member>
      <Member>
        <Name>JV OpCo 1</Name>
        <Jurisdiction>US</Jurisdiction>
      </Member>
      <Member>
        <Name>JV OpCo 2</Name>
        <Jurisdiction>US</Jurisdiction>
      </Member>
    </JVMembers>

    <JVJurisdictionData>
      <Jurisdiction>
        <JurisdictionCode>US</JurisdictionCode>
        <SubJurisdiction>Delaware</SubJurisdiction>
        <GloBEIncome currCode="EUR">15000000</GloBEIncome>
        <CoveredTaxes currCode="EUR">1800000</CoveredTaxes>
        <ETR>12.00</ETR>
        <TopUpTax currCode="EUR">384000</TopUpTax>
        <UPEShare currCode="EUR">192000</UPEShare>
      </Jurisdiction>
    </JVJurisdictionData>
  </JVGroup>
</JVGroupInfo>
```

---

## Part 3: Minority-Owned Constituent Entities (MOCEs)

### 3.1 MOCE Definition

**Article 10, OECD Model Rules:**

A Minority-Owned Constituent Entity (MOCE) is a Constituent Entity where:
- The UPE holds **30% or less** of the Ownership Interest
- But the UPE has a **Controlling Interest** (e.g., via shareholder agreement)

### 3.2 MOCE vs Standard CE

```
MOCE TREATMENT COMPARISON
=========================

Standard Constituent Entity:
  ► Blended with other CEs in jurisdiction for ETR
  ► Contributes to jurisdictional Top-up Tax

Minority-Owned Constituent Entity:
  ► Separate ETR calculation (not blended)
  ► Own Top-up Tax calculation
  ► UPE's share of Top-up Tax = Ownership % × Total Top-up Tax
  ► Prevents external owners bearing Top-up Tax cost
```

### 3.3 Minority-Owned Subgroup (MOS)

When a MOCE has subsidiaries, they form a **Minority-Owned Subgroup**:

```
MINORITY-OWNED SUBGROUP ANALYSIS
================================

Meridian Green Energy Ltd (Ireland) - MOCE Head
├── Green Wind Holdings Ltd (Ireland) - MOS Member
└── Solar Power Holdings Ltd (Netherlands) - MOS Member

UPE Ownership: 25% (but controlling interest via agreement)

MOS Treatment:
  ► Entire subgroup treated as separate "mini-group"
  ► Subgroup has own GloBE calculations
  ► Results excluded from main group's jurisdictional ETR
```

### 3.4 MOCE GloBE Calculation

```
MOCE SEPARATE CALCULATION
=========================

Meridian Green Energy Ltd (Ireland) - Standalone:
  GloBE Income:                    €12,000,000
  Adjusted Covered Taxes:           €1,440,000
  Entity ETR:                           12.0%
  Top-up Tax %:                          3.0%
  SBIE:                               €800,000
  Excess Profit:                   €11,200,000
  Entity Top-up Tax:                  €336,000

UPE's Allocable Share:
  €336,000 × 25% = €84,000

Note: The remaining €252,000 (75%) is NOT charged to UPE—
      it is borne by the other investors through the MOCE.

Green Wind Holdings Ltd (Ireland) - Within MOS:
  GloBE Income:                     €5,000,000
  Adjusted Covered Taxes:             €600,000
  Entity ETR:                           12.0%
  Top-up Tax %:                          3.0%
  SBIE:                               €350,000
  Excess Profit:                    €4,650,000
  Entity Top-up Tax:                  €139,500

UPE's Allocable Share:
  €139,500 × 25% = €34,875

Solar Power Holdings Ltd (Netherlands) - Within MOS:
  [Assume ETR > 15%, no Top-up Tax]

TOTAL UPE IIR CHARGE FOR MOS: €84,000 + €34,875 = €118,875
```

### 3.5 GIR Reporting for MOCEs

```xml
<!-- MINORITY-OWNED SUBGROUP REPORTING -->

<MinorityOwnedSubgroup>
  <MOSIdentification>
    <MOSHead>
      <Name>Meridian Green Energy Ltd</Name>
      <JurisdictionCode>IE</JurisdictionCode>
      <TIN issuedBy="IE">IE9876543X</TIN>
    </MOSHead>
    <UPEOwnership>25.00</UPEOwnership>
    <ControlBasis>ShareholderAgreement</ControlBasis>
  </MOSIdentification>

  <MOSMembers>
    <Member>
      <Name>Meridian Green Energy Ltd</Name>
      <Jurisdiction>IE</Jurisdiction>
      <Type>MOSHead</Type>
    </Member>
    <Member>
      <Name>Green Wind Holdings Ltd</Name>
      <Jurisdiction>IE</Jurisdiction>
      <Type>MOSMember</Type>
    </Member>
    <Member>
      <Name>Solar Power Holdings Ltd</Name>
      <Jurisdiction>NL</Jurisdiction>
      <Type>MOSMember</Type>
    </Member>
  </MOSMembers>

  <MOSJurisdictionData>
    <Jurisdiction>
      <JurisdictionCode>IE</JurisdictionCode>
      <NumberOfEntities>2</NumberOfEntities>
      <AggregateGloBEIncome currCode="EUR">17000000</AggregateGloBEIncome>
      <AggregateCoveredTaxes currCode="EUR">2040000</AggregateCoveredTaxes>
      <JurisdictionalETR>12.00</JurisdictionalETR>
      <TotalTopUpTax currCode="EUR">475500</TotalTopUpTax>
      <UPEAllocableShare currCode="EUR">118875</UPEAllocableShare>
    </Jurisdiction>
  </MOSJurisdictionData>
</MinorityOwnedSubgroup>
```

---

## Part 4: Ownership Percentage Calculations

### 4.1 Multi-Tiered Ownership

Calculating ownership through multiple tiers requires careful multiplication:

```
MULTI-TIERED OWNERSHIP CALCULATION
==================================

Example: UPE's indirect ownership of Meridian AI Ireland Ltd

Tier 1: UPE → Meridian Tech Ventures BV
        Ownership: 70%

Tier 2: Meridian Tech Ventures BV → Meridian AI Ireland Ltd
        Ownership: 100%

UPE's Indirect Ownership:
        70% × 100% = 70%

Top-up Tax Allocation:
        UPE bears: 70% of Top-up Tax
        POPE bears: 30% of Top-up Tax (for external investors)
```

### 4.2 Complex Ownership with Multiple Share Classes

When entities have multiple share classes with different rights:

```
MULTIPLE SHARE CLASS CALCULATION
================================

Scenario: OpCo Ltd has two share classes
  - Class A: Rights to 60% of profits
  - Class B: Rights to 40% of profits and 100% of capital

Investor 1 holds: 80% of Class A, 20% of Class B
Investor 2 holds: 20% of Class A, 80% of Class B

Ownership Interest Calculation:

For GloBE purposes, use average of:
  - Rights to profits
  - Rights to capital/reserves

Investor 1:
  Profit rights: (80% × 60%) + (20% × 40%) = 48% + 8% = 56%
  Capital rights: (20% × 100%) = 20%
  Average: (56% + 20%) / 2 = 38%

Investor 2:
  Profit rights: (20% × 60%) + (80% × 40%) = 12% + 32% = 44%
  Capital rights: (80% × 100%) = 80%
  Average: (44% + 80%) / 2 = 62%

Total: 38% + 62% = 100% ✓
```

### 4.3 Ownership Documentation Template

```
OWNERSHIP PERCENTAGE CALCULATION WORKSHEET
==========================================

Entity: _________________________________
Jurisdiction: ___________________________

DIRECT OWNERSHIP:
┌────────────────────────────┬──────────────┬─────────────┬────────────┐
│ Shareholder                │ Profit Rights│ Capital     │ Average %  │
│                            │     (%)      │ Rights (%)  │            │
├────────────────────────────┼──────────────┼─────────────┼────────────┤
│ 1. ____________________    │    _____%    │   _____%    │   _____%   │
│ 2. ____________________    │    _____%    │   _____%    │   _____%   │
│ 3. ____________________    │    _____%    │   _____%    │   _____%   │
│ External (non-group)       │    _____%    │   _____%    │   _____%   │
├────────────────────────────┼──────────────┼─────────────┼────────────┤
│ TOTAL                      │    100%      │   100%      │   100%     │
└────────────────────────────┴──────────────┴─────────────┴────────────┘

INDIRECT OWNERSHIP (trace to UPE):

Chain: UPE → [Entity 1] → [Entity 2] → This Entity

Calculation:
  ______% × ______% × ______% = ______% UPE indirect ownership

CLASSIFICATION:
□ Standard CE (≥50% UPE ownership, <20% external at any level)
□ POPE (>20% external ownership, owns other CEs)
□ MOCE (≤30% UPE ownership, but UPE has control)
□ JV (50%+ ownership, equity method accounting)

Prepared by: __________________ Date: ______________
```

---

## Part 5: Excluded Entity Handling

### 5.1 Entities Excluded from GloBE

Certain entities are excluded from the GloBE calculations:

| Entity Type | Exclusion Basis |
|-------------|-----------------|
| Governmental Entities | Public function |
| International Organisations | Treaty-based |
| Non-profit Organisations | No profit motive |
| Pension Funds | Retirement savings |
| Investment Funds (certain) | Regulated funds |
| Real Estate Investment Vehicles | REIT-type structures |

### 5.2 Excluded Entity in Meridian Group

**Assume:** Meridian holds 40% of a real estate investment trust (REIT)

```
EXCLUDED ENTITY ANALYSIS
========================

Entity: Meridian Property REIT (UK)
Structure: UK REIT

Exclusion Test:
  □ Is it a Real Estate Investment Vehicle?     YES
  □ Does it meet REIV definition?               YES
  □ Widely held (5+ unrelated investors)?       YES
  □ Subject to single taxation regime?          YES

RESULT: Excluded Entity - NOT a Constituent Entity

GIR Treatment:
  ► Not included in CE count
  ► Not included in jurisdictional calculations
  ► May need to be disclosed as excluded entity
```

### 5.3 GIR Disclosure of Excluded Entities

```xml
<!-- EXCLUDED ENTITIES DISCLOSURE -->

<ExcludedEntities>
  <ExcludedEntity>
    <Name>Meridian Property REIT</Name>
    <JurisdictionCode>GB</JurisdictionCode>
    <ExclusionBasis>RealEstateInvestmentVehicle</ExclusionBasis>
    <UPEOwnership>40.00</UPEOwnership>
  </ExcludedEntity>
</ExcludedEntities>
```

---

## Part 6: Complete GIR Summary

### 6.1 Consolidated Top-up Tax Summary

```
MERIDIAN INDUSTRIAL GROUP - TOP-UP TAX SUMMARY FY2024
=====================================================

MAIN GROUP (excluding JV and MOS):
----------------------------------
Jurisdictions with Top-up Tax:

Ireland (POPE subsidiaries):
  Meridian AI Ireland Ltd
    Total Top-up Tax:                  €822,500
    Allocated to POPE (30%):           €246,750
    Allocated to UPE (70%):            €575,750

  Meridian Quantum GmbH (Germany):
    [Assume ETR > 15%, no Top-up Tax]

Other low-tax jurisdictions:
  [Assume safe harbour applies or ETR > 15%]

Main Group UPE IIR Charge:             €575,750


JOINT VENTURE GROUP:
--------------------
MeridiaTech JV LLC Group:
  Delaware operations:
    Total JV Top-up Tax:               €384,000
    UPE's 50% share:                   €192,000


MINORITY-OWNED SUBGROUP:
------------------------
Meridian Green Energy MOS:
  Ireland entities:
    Total MOS Top-up Tax:              €475,500
    UPE's 25% share:                   €118,875


POPE IIR CHARGE (Netherlands):
------------------------------
  Meridian Tech Ventures BV:
    For external investors (30%):      €246,750


TOTAL UK IIR LIABILITY:
-----------------------
  Main Group UPE share:                €575,750
  JV Group UPE share:                  €192,000
  MOS UPE share:                       €118,875
                                      ──────────
  TOTAL UK MTT:                        €886,625
                                      ==========

TOTAL POPE IIR (Netherlands):          €246,750
```

### 6.2 GIR Filing Summary

```
GIR FILING CHECKLIST - COMPLEX OWNERSHIP
========================================

SECTION 1: GROUP INFORMATION
□ UPE details completed
□ All CEs listed (main group)
□ POPE identified and flagged
□ POPE's external ownership disclosed
□ JV Group separately identified
□ MOS separately identified
□ Excluded entities disclosed

SECTION 2: JURISDICTIONAL DATA
□ Main group jurisdictions (safe harbour where applicable)
□ POPE subsidiary jurisdictions (full calculation for Ireland)
□ JV Group jurisdictions (separate calculations)
□ MOS jurisdictions (separate calculations)
□ Top-up Tax correctly attributed

SECTION 3: ENTITY DATA
□ All main group CEs
□ POPE ownership chain disclosed
□ POPE subsidiaries with allocation
□ JV members (in JV section)
□ MOS members (in MOS section)
□ Excluded entities noted

SPECIAL SECTIONS:
□ JVGroupInfo section completed
□ MinorityOwnedSubgroup section completed
□ TopUpTaxAllocation showing POPE split

SIGN-OFF:
Prepared by: __________________ Date: ____________
Reviewed by: __________________ Date: ____________
Approved by: __________________ Date: ____________
```

---

## Deliverable: Complex Ownership Structure Workbook

### Template: Ownership Classification Matrix

```
OWNERSHIP CLASSIFICATION MATRIX
===============================

Group: _________________________________
Fiscal Year: ___________________________

ENTITY CLASSIFICATION:

| Entity Name            | Juris | UPE    | Parent  | Parent  | External | Class    |
|                        |       | Direct | Name    | Own %   | Own %    |          |
|------------------------|-------|--------|---------|---------|----------|----------|
| [UPE Name]             | ___   | -      | -       | -       | ____%    | UPE      |
| ______________________ | ___   | □ Y □ N| _______ | ____%   | ____%    | ________ |
| ______________________ | ___   | □ Y □ N| _______ | ____%   | ____%    | ________ |
| ______________________ | ___   | □ Y □ N| _______ | ____%   | ____%    | ________ |
| ______________________ | ___   | □ Y □ N| _______ | ____%   | ____%    | ________ |

Classification Key:
  CE = Standard Constituent Entity
  IPE = Intermediate Parent Entity
  POPE = Partially-Owned Parent Entity
  JV = Joint Venture
  JVCE = JV Constituent Entity
  MOCE = Minority-Owned Constituent Entity
  MOS = Minority-Owned Subgroup Member
  EXC = Excluded Entity

POPE SUMMARY:
| POPE Name              | UPE Own % | External % | # Subsidiaries | IIR Juris |
|------------------------|-----------|------------|----------------|-----------|
| ______________________ | _______%  | _______%   | _________      | ________  |

JV SUMMARY:
| JV Name                | UPE Own % | Partner %  | # JV CEs       | Equity Mtd|
|------------------------|-----------|------------|----------------|-----------|
| ______________________ | _______%  | _______%   | _________      | □ Y □ N   |

MOS SUMMARY:
| MOS Head Name          | UPE Own % | Control    | # MOS Members  | Juris     |
|------------------------|-----------|------------|----------------|-----------|
| ______________________ | _______%  | _________  | _________      | ________  |

EXCLUDED ENTITIES:
| Entity Name            | Jurisdiction | Exclusion Basis           | UPE Own % |
|------------------------|--------------|---------------------------|-----------|
| ______________________ | ____________ | _________________________ | _______%  |
```

---

## Section Summary

Complex ownership structures require careful analysis under the GloBE Rules:

1. **POPEs** - Split Top-up Tax between UPE and external investors
2. **Joint Ventures** - Treated as separate MNE groups with own calculations
3. **MOCEs/MOS** - Separate calculations prevent external owners bearing cost
4. **Multi-tiered Ownership** - Multiply percentages through chains
5. **Excluded Entities** - Identified and disclosed but not in calculations

Each structure type requires specific GIR reporting in dedicated sections.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **POPE Threshold** | >20% external ownership + owns other CEs |
| **POPE Effect** | POPE jurisdiction may apply IIR for external share |
| **JV Definition** | ≥50% owned, equity method accounting |
| **JV Treatment** | Separate MNE group; no blending |
| **MOCE Threshold** | ≤30% UPE ownership but controlling interest |
| **MOCE Treatment** | Separate ETR; UPE's share only |
| **Ownership Calculation** | Average of profit and capital rights |
| **GIR Reporting** | Separate sections for JV and MOS |

---

## Sources

Key references for this section include:

- [Macfarlanes - Split Ownership and Joint Ventures](https://www.macfarlanes.com/what-we-think/2022/unpacking-pillar-two-split-ownership-and-joint-ventures-jvs/)
- [OECD Pillars - Joint Ventures](https://oecdpillars.com/pillar-tab/pillar-two-joint-ventures/)
- [OECD Pillars - Minority-Owned Entities](https://oecdpillars.com/pillar-tab/minority-owned-entities/)
- [OECD Pillars - Income Inclusion Rule: UPE, POPEs](https://oecdpillars.com/pillar-tab/ascertain-the-parent-entity-liable-for-top-up-tax-under-the-income-inclusion-rule/)
- [Irish Revenue - Guidance on Pillar Two](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-04a/04a-01-02.pdf)

---

*Section 10.2 Complete. Proceed to Section 10.3: Scenario 3 - Data Gap Challenges.*
