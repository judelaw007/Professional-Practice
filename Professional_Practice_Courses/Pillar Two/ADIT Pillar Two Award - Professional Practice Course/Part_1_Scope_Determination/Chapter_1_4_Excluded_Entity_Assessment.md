# Chapter 1.4: Excluded Entity Assessment

## Learning Objective

After completing this chapter, you will be able to determine whether any Constituent Entities qualify as Excluded Entities under the GloBE Rules and document these exclusions appropriately.

## Introduction

Not every entity in a consolidated group was intended to be drawn into the Pillar Two net. The GloBE Rules carve out specific categories of entities whose exclusion reflects deliberate policy judgments about the appropriate scope of the global minimum tax. These exclusions recognise that certain entities—governments, international organisations, charities, pension funds, and certain investment vehicles—serve purposes that transcend ordinary commercial profit-seeking and warrant different treatment. Understanding these exclusions requires more than memorising categories; it requires appreciating why policymakers chose to draw these particular lines and how the exclusion tests implement those policy objectives.

## 1. Why Excluded Entities Matter

Certain entities are excluded from GloBE calculations even though they may technically be Constituent Entities. Identifying these exclusions correctly is essential because:

- Excluded Entities are not included in the jurisdictional ETR calculation
- Their income and taxes are carved out from group computations
- Misclassification can lead to incorrect Top-Up Tax calculations

The five categories of Excluded Entities are defined in **Article 1.5** of the GloBE Model Rules.

The consequences of misclassification flow in both directions. Incorrectly treating an entity as excluded when it is not removes its income from the ETR calculation—potentially understating the jurisdiction's effective rate and triggering unwarranted Top-Up Tax. Conversely, failing to identify a valid exclusion brings the entity's income (often tax-exempt by design) into GloBE calculations, artificially depressing the jurisdictional ETR and potentially creating Top-Up Tax liability where none should exist. Either error distorts the intended operation of the rules and invites adjustment upon audit.

## 2. The Five Excluded Entity Categories

### 2.1 Category 1: Governmental Entities

A **Governmental Entity** is excluded if it is *(Article 1.5.1(a))*:

1. A government, political subdivision, or local authority, OR
2. An agency or instrumentality wholly owned by a government, OR
3. A body performing government functions (regulatory, administrative, or other) with majority government control

**Key test:** Is the entity carrying on a trade or business, or primarily engaged in investing government assets?

- If **yes** (trading/investing) → NOT an Excluded Entity
- If **no** (government functions only) → Excluded Entity

The governmental entity exclusion reflects a fundamental principle of international tax: sovereigns do not tax each other. When a government entity performs public functions, subjecting it to the global minimum tax would effectively allow one jurisdiction's revenue claim to override another's sovereign activities. However, this deference to sovereignty has limits—when governments enter commercial markets, competing alongside private businesses, the rationale for exclusion falls away. A state-owned enterprise operating commercially should face the same minimum tax rules as its private competitors, ensuring a level playing field.

### 2.2 Category 2: International Organisations

An **International Organisation** qualifies for exclusion if it *(Article 1.5.1(b))*:

1. Is established by treaty or international agreement between governments
2. Has a headquarters agreement granting tax privileges
3. Has income that does not accrue to the benefit of private persons

**Practical examples:**
- United Nations and its agencies
- World Bank Group entities
- European Union institutions
- OECD

### 2.3 Category 3: Non-Profit Organisations

A **Non-Profit Organisation (NPO)** is excluded if it *(Article 1.5.1(c))*:

1. Is established and operated exclusively for religious, charitable, scientific, artistic, cultural, athletic, educational, or other similar purposes
2. Has income substantially exempt from tax in its jurisdiction of residence
3. Has no shareholders or members with proprietary interests in its income or assets
4. Cannot distribute income or assets to private persons (except for charitable purposes or reasonable compensation)
5. Must distribute all assets to an NPO or government upon winding up

**All five conditions must be met** for NPO exclusion.

The stringency of the NPO test reflects hard-won lessons from decades of tax abuse through purported charities. Legitimate non-profits serve vital social functions and enjoy tax exemption precisely because their activities generate public benefit rather than private wealth. But the NPO form has also been exploited to shelter commercial profits from taxation. The five-part test acts as a robust filter: only entities that genuinely operate for charitable purposes, with income that cannot enrich private parties, qualify for exclusion. Groups with charitable foundations should document compliance with each criterion carefully, as the burden falls on the taxpayer to establish exclusion eligibility.

### 2.4 Category 4: Pension Funds

A **Pension Fund** is excluded if it is *(Article 1.5.1(d))*:

1. Established to provide retirement benefits, and
2. Regulated in the jurisdiction where it is established or operates, and
3. Either:
   - Income is exempt from tax, OR
   - Taxation is deferred until benefits are paid

**Pension Services Entity:** An entity established exclusively to invest assets for, or provide services to, pension funds that are members of the same group is also excluded.

The pension fund exclusion recognises the unique social policy role that retirement savings vehicles play. Pension funds accumulate and invest capital over decades to provide retirement security for millions of workers—a function most governments actively encourage through tax incentives. Subjecting pension fund investment income to the global minimum tax would undermine these policy objectives, potentially reducing retirement benefits or discouraging pension saving. The exclusion extends to "pension services entities" because modern pension arrangements often involve subsidiary vehicles for regulatory, liability, or investment management reasons; excluding the main fund while taxing its service entities would frustrate the exclusion's purpose.

### 2.5 Category 5: Investment Funds (UPE Only)

An **Investment Fund** qualifies for exclusion only if it is the **Ultimate Parent Entity** of the MNE group *(Article 1.5.1(e))*. The fund must:

1. Be designed to pool capital from unrelated investors
2. Invest in accordance with a defined investment policy
3. Allow investors to reduce transaction, research, and analytical costs
4. Be primarily established for investment rather than trading

**Investment Entity owned by Investment Fund:** An entity wholly owned (directly or indirectly) by an Investment Fund UPE is also excluded if it exclusively holds assets or invests funds on behalf of the fund.

## 3. Ownership Test for Investment Funds

An Investment Fund UPE qualifies for exclusion only if it meets the **ownership test** *(Article 1.5.2)*:

At least **80% of the value** of ownership interests in the fund must be held by persons who are:
- Not connected with the fund manager, AND
- Either individuals or entities whose income from the fund is:
  - Subject to tax, OR
  - Held for pensioners or beneficiaries whose income is subject to tax

**Timeline:** The test is assessed at the end of the fiscal year, looking at ownership throughout the year.

**Failure consequence:** If the 80% test is failed, the Investment Fund loses excluded status, and the entire group becomes subject to GloBE calculations.

The investment fund exclusion is the most narrowly drawn of the five categories, available only where the fund sits at the very top of the structure. This limitation reflects the anti-avoidance concern that without it, any MNE could interpose an "investment fund" subsidiary to shelter profits from the minimum tax. By restricting exclusion to UPE-level funds—which typically have genuine, unrelated investors—the rules target authentic investment vehicles while preventing abuse. The 80% ownership test adds a further safeguard: a fund controlled by connected parties or tax-exempt investors who gain no benefit from the fund's tax status cannot claim exclusion. These layered requirements make investment fund exclusion genuinely difficult to achieve, as intended.

## 4. Decision Flowchart: Is This Entity Excluded?

```
                    ┌─────────────────────────────────────┐
                    │ Is the entity a Constituent Entity? │
                    └──────────────────┬──────────────────┘
                                       │
                           ┌───────────┴───────────┐
                           │                       │
                          YES                      NO
                           │                       │
                           ▼                       ▼
             ┌─────────────────────────┐   ┌─────────────────┐
             │ Does it fall into one   │   │ NOT IN SCOPE    │
             │ of the 5 categories?    │   │ (stop here)     │
             └───────────┬─────────────┘   └─────────────────┘
                         │
         ┌───────┬───────┼───────┬───────┐
         ▼       ▼       ▼       ▼       ▼
    Government  I/O     NPO   Pension  Inv Fund
         │       │       │       │       │
         ▼       ▼       ▼       ▼       ▼
   ┌──────────┐ ┌──────┐ ┌─────┐ ┌─────┐ ┌────────┐
   │Trading or│ │Treaty│ │All 5│ │Regu-│ │UPE AND │
   │investing?│ │basis?│ │tests│ │lated│ │80% test│
   └────┬─────┘ └──┬───┘ │met? │ │fund?│ │ met?   │
        │          │     └──┬──┘ └──┬──┘ └────┬───┘
   ┌────┴────┐     │        │       │         │
  YES       NO     │        │       │         │
   │         │     │        │       │         │
   ▼         ▼     ▼        ▼       ▼         ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ NOT  │ │EXCL- │ │EXCL- │ │EXCL- │ │EXCL- │ │EXCL- │
│EXCLUD│ │ UDED │ │ UDED │ │ UDED │ │ UDED │ │ UDED │
└──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘
```

## 5. Step-by-Step Excluded Entity Assessment

### 5.1 Step 1: Review CE Register

Start with your Constituent Entity register from Chapter 1.2. For each CE, consider whether it may fall into one of the five excluded categories.

**Likely candidates:**
- Entities with "Pension," "Trust," "Foundation," or "Charity" in their name
- Entities with government ownership (full or partial)
- Holding companies owned by institutional investors

### 5.2 Step 2: Gather Entity Documentation

For each potential exclusion, obtain:

| Category | Documentation Required |
|----------|----------------------|
| Government Entity | Charter, formation documents, ownership evidence, description of activities |
| International Org | Treaty/convention establishing the organisation, headquarters agreement |
| NPO | Formation documents, tax exemption certificate, constitutional documents showing charitable purposes |
| Pension Fund | Regulatory registration, tax status confirmation, fund rules |
| Investment Fund | Fund prospectus, investor register, fund manager agreements |

### 5.3 Step 3: Apply Exclusion Tests

Work through each exclusion test systematically. Document your analysis for each criterion.

**For Investment Fund UPE exclusion:**
1. Confirm entity is the UPE (not a subsidiary)
2. Verify fund structure meets investment fund definition
3. Calculate ownership percentages for five-year test
4. Assess each investor's tax status

### 5.4 Step 4: Document Conclusions

Prepare a memo for each excluded entity covering:
- Entity name and jurisdiction
- Applicable exclusion category
- Evidence supporting each criterion
- Date of assessment
- Review frequency

## 6. Worked Example: Stratos's Excluded Entity Assessment

### 6.1 Potential Exclusions Identified

From Stratos's 47 Constituent Entities, the tax team identifies three potential exclusions:

| Entity | Category | Initial Assessment |
|--------|----------|-------------------|
| SG Pension Trustees Ltd (UK) | Pension Fund | UK registered occupational pension scheme |
| Stratos Foundation (UK) | NPO | Charitable foundation making grants |
| Singapore Gov JV Pte Ltd | Government Entity | 51% owned by Singapore government agency |

### 6.2 Analysis: SG Pension Trustees Ltd

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Provides retirement benefits | **Yes** | Defined benefit scheme for Stratos employees |
| Regulated | **Yes** | Registered with The Pensions Regulator (UK) |
| Tax status | **Yes** | Income exempt under UK registered pension scheme rules |

**Conclusion:** SG Pension Trustees Ltd is an **Excluded Entity** (Pension Fund).

### 6.3 Analysis: Stratos Foundation

| NPO Criterion | Assessment | Evidence |
|---------------|------------|----------|
| Established for charitable purpose | **Yes** | Objects: advancement of education in technology |
| Income substantially exempt | **Yes** | UK charity, exempt from corporation tax |
| No proprietary shareholders | **Yes** | No share capital; trustees have no beneficial interest |
| No distribution to private persons | **Yes** | Constitution prohibits private benefit |
| Assets to charity on winding up | **Yes** | Constitution requires distribution to similar charities |

**Conclusion:** Stratos Foundation is an **Excluded Entity** (NPO).

### 6.4 Analysis: Singapore Gov JV Pte Ltd

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Government ownership | **Partial** | 51% by government agency; 49% by Stratos |
| Trading activities | **Yes** | Operates technology park, generates commercial revenue |

**Conclusion:** Singapore Gov JV Pte Ltd is **NOT an Excluded Entity**.

The entity is engaged in commercial trading activities despite government majority ownership. It fails the "government functions only" test *(Commentary, para. 39)*.

This entity remains a Constituent Entity and will be included in GloBE calculations. However, as a joint arrangement with only 51% government ownership (and 49% owned by Stratos), the treatment depends on whether it meets the JV definition under Article 10.1—see Part 6.

### 6.5 Result

Stratos has **2 Excluded Entities**:
- SG Pension Trustees Ltd (Pension Fund)
- Stratos Foundation (NPO)

**45 Constituent Entities remain in scope** for GloBE calculations.

## 7. Common Assessment Challenges

### 7.1 Challenge 1: Government Entity vs Commercial Entity

Government agencies that conduct commercial activities are not excluded. Key indicators of commercial activity:
- Revenue from goods or services sold at market prices
- Competition with private sector entities
- Profit-making objectives

*(Commentary, para. 38-42)*

### 7.2 Challenge 2: NPO "Substantially Exempt" Test

The NPO exclusion requires income to be "substantially exempt" from tax—not entirely exempt. Incidental taxable income (e.g., from unrelated business activities) does not disqualify an NPO if the bulk of income is exempt.

**Practical threshold:** If 80%+ of income is tax-exempt, the "substantially exempt" test is generally met.

### 7.3 Challenge 3: Pension Fund Subsidiaries

A subsidiary that provides services to the pension fund may also qualify for exclusion as a "Pension Services Entity" *(Article 1.5.1(d)(ii))* if:
- Established exclusively to hold assets or earn income for the pension fund
- All activities are connected with administering the pension fund's investments

Property holding subsidiaries of pension funds often qualify.

### 7.4 Challenge 4: Investment Fund Investor Identification

The 80% ownership test requires identifying all investors and their tax status. For funds with numerous investors, this can be complex.

**Practical approach:**
- Obtain investor register from fund administrator
- Categorise investors: individuals, pension funds, taxable entities, tax-exempt entities
- Calculate percentage by value (not number) of investors meeting the test
- Document instances where investor status cannot be determined

These challenges illustrate a broader truth about excluded entity assessment: the tests are deliberately rigorous because exclusion carries significant consequences. An excluded entity's income entirely escapes GloBE—unlike the de minimis exclusion or substance-based carve-outs discussed in later chapters, which merely reduce the base subject to Top-Up Tax. This "all or nothing" character means tax authorities have strong incentives to challenge claimed exclusions, and groups should approach the analysis with corresponding thoroughness. When exclusion status is uncertain, erring on the side of including the entity in GloBE calculations—while documenting the analysis—may be the prudent approach.

## 8. Excluded Entity Register

Maintain an Excluded Entity Register as a supplement to your CE register:

| Field | Description |
|-------|-------------|
| Entity name | Legal name |
| Jurisdiction | Country of tax residence |
| Exclusion category | Government / I/O / NPO / Pension / Investment Fund |
| Key criteria met | Summary of how each criterion is satisfied |
| Supporting documents | List of evidence on file |
| Assessment date | Date of initial determination |
| Review date | Date for next review |
| Assessor | Name of person completing assessment |

**Review frequency:** Annual review at fiscal year-end, plus upon any change in entity status, activities, or ownership.

The excluded entity analysis completes the scope determination phase. At this point, you should have a clear picture of which entities fall within the GloBE perimeter: starting with all Constituent Entities identified in Chapter 1.2, less any Excluded Entities identified here. These remaining entities—often numbering in the dozens or hundreds for large multinationals—form the population for all subsequent GloBE calculations: their income becomes GloBE Income, their taxes become Covered Taxes, and their jurisdiction-by-jurisdiction ETRs determine Top-Up Tax liability. The rigour applied at this foundational stage pays compound dividends throughout the compliance process; errors here propagate through every subsequent calculation and are far easier to correct now than after returns have been filed.
