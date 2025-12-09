# Chapter 1.4: Excluded Entity Assessment

## Learning Objective

After completing this chapter, you will be able to determine whether any Constituent Entities qualify as Excluded Entities under the GloBE Rules and document these exclusions appropriately.

---

## Why Excluded Entities Matter

Certain entities are excluded from GloBE calculations even though they may technically be Constituent Entities. Identifying these exclusions correctly is essential because:

- Excluded Entities are not included in the jurisdictional ETR calculation
- Their income and taxes are carved out from group computations
- Misclassification can lead to incorrect Top-Up Tax calculations

The five categories of Excluded Entities are defined in **Article 1.5** of the GloBE Model Rules.

---

## The Five Excluded Entity Categories

### Category 1: Governmental Entities

A **Governmental Entity** is excluded if it is *(Article 1.5.1(a))*:

1. A government, political subdivision, or local authority, OR
2. An agency or instrumentality wholly owned by a government, OR
3. A body performing government functions (regulatory, administrative, or other) with majority government control

**Key test:** Is the entity carrying on a trade or business, or primarily engaged in investing government assets?

- If **yes** (trading/investing) → NOT an Excluded Entity
- If **no** (government functions only) → Excluded Entity

### Category 2: International Organisations

An **International Organisation** qualifies for exclusion if it *(Article 1.5.1(b))*:

1. Is established by treaty or international agreement between governments
2. Has a headquarters agreement granting tax privileges
3. Has income that does not accrue to the benefit of private persons

**Practical examples:**
- United Nations and its agencies
- World Bank Group entities
- European Union institutions
- OECD

### Category 3: Non-Profit Organisations

A **Non-Profit Organisation (NPO)** is excluded if it *(Article 1.5.1(c))*:

1. Is established and operated exclusively for religious, charitable, scientific, artistic, cultural, athletic, educational, or other similar purposes
2. Has income substantially exempt from tax in its jurisdiction of residence
3. Has no shareholders or members with proprietary interests in its income or assets
4. Cannot distribute income or assets to private persons (except for charitable purposes or reasonable compensation)
5. Must distribute all assets to an NPO or government upon winding up

**All five conditions must be met** for NPO exclusion.

### Category 4: Pension Funds

A **Pension Fund** is excluded if it is *(Article 1.5.1(d))*:

1. Established to provide retirement benefits, and
2. Regulated in the jurisdiction where it is established or operates, and
3. Either:
   - Income is exempt from tax, OR
   - Taxation is deferred until benefits are paid

**Pension Services Entity:** An entity established exclusively to invest assets for, or provide services to, pension funds that are members of the same group is also excluded.

### Category 5: Investment Funds (UPE Only)

An **Investment Fund** qualifies for exclusion only if it is the **Ultimate Parent Entity** of the MNE group *(Article 1.5.1(e))*. The fund must:

1. Be designed to pool capital from unrelated investors
2. Invest in accordance with a defined investment policy
3. Allow investors to reduce transaction, research, and analytical costs
4. Be primarily established for investment rather than trading

**Investment Entity owned by Investment Fund:** An entity wholly owned (directly or indirectly) by an Investment Fund UPE is also excluded if it exclusively holds assets or invests funds on behalf of the fund.

---

## Five-Year Ownership Test for Investment Funds

An Investment Fund UPE qualifies for exclusion only if it meets the **five-year ownership test** *(Article 1.5.2)*:

At least **80% of the value** of ownership interests in the fund must be held by persons who are:
- Not connected with the fund manager, AND
- Either individuals or entities whose income from the fund is:
  - Subject to tax, OR
  - Held for pensioners or beneficiaries whose income is subject to tax

**Timeline:** The test is assessed at the end of the fiscal year, looking at ownership throughout the year.

**Failure consequence:** If the 80% test is failed, the Investment Fund loses excluded status, and the entire group becomes subject to GloBE calculations.

---

## Decision Flowchart: Is This Entity Excluded?

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

---

## Step-by-Step Excluded Entity Assessment

### Step 1: Review CE Register

Start with your Constituent Entity register from Chapter 1.2. For each CE, consider whether it may fall into one of the five excluded categories.

**Likely candidates:**
- Entities with "Pension," "Trust," "Foundation," or "Charity" in their name
- Entities with government ownership (full or partial)
- Holding companies owned by institutional investors

### Step 2: Gather Entity Documentation

For each potential exclusion, obtain:

| Category | Documentation Required |
|----------|----------------------|
| Government Entity | Charter, formation documents, ownership evidence, description of activities |
| International Org | Treaty/convention establishing the organisation, headquarters agreement |
| NPO | Formation documents, tax exemption certificate, constitutional documents showing charitable purposes |
| Pension Fund | Regulatory registration, tax status confirmation, fund rules |
| Investment Fund | Fund prospectus, investor register, fund manager agreements |

### Step 3: Apply Exclusion Tests

Work through each exclusion test systematically. Document your analysis for each criterion.

**For Investment Fund UPE exclusion:**
1. Confirm entity is the UPE (not a subsidiary)
2. Verify fund structure meets investment fund definition
3. Calculate ownership percentages for five-year test
4. Assess each investor's tax status

### Step 4: Document Conclusions

Prepare a memo for each excluded entity covering:
- Entity name and jurisdiction
- Applicable exclusion category
- Evidence supporting each criterion
- Date of assessment
- Review frequency

---

## Worked Example: GlobalTech's Excluded Entity Assessment

### Potential Exclusions Identified

From GlobalTech's 47 Constituent Entities, the tax team identifies three potential exclusions:

| Entity | Category | Initial Assessment |
|--------|----------|-------------------|
| GT Pension Trustees Ltd (UK) | Pension Fund | UK registered occupational pension scheme |
| GlobalTech Foundation (UK) | NPO | Charitable foundation making grants |
| Singapore Gov JV Pte Ltd | Government Entity | 51% owned by Singapore government agency |

### Analysis: GT Pension Trustees Ltd

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Provides retirement benefits | **Yes** | Defined benefit scheme for GlobalTech employees |
| Regulated | **Yes** | Registered with The Pensions Regulator (UK) |
| Tax status | **Yes** | Income exempt under UK registered pension scheme rules |

**Conclusion:** GT Pension Trustees Ltd is an **Excluded Entity** (Pension Fund).

### Analysis: GlobalTech Foundation

| NPO Criterion | Assessment | Evidence |
|---------------|------------|----------|
| Established for charitable purpose | **Yes** | Objects: advancement of education in technology |
| Income substantially exempt | **Yes** | UK charity, exempt from corporation tax |
| No proprietary shareholders | **Yes** | No share capital; trustees have no beneficial interest |
| No distribution to private persons | **Yes** | Constitution prohibits private benefit |
| Assets to charity on winding up | **Yes** | Constitution requires distribution to similar charities |

**Conclusion:** GlobalTech Foundation is an **Excluded Entity** (NPO).

### Analysis: Singapore Gov JV Pte Ltd

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Government ownership | **Partial** | 51% by government agency; 49% by GlobalTech |
| Trading activities | **Yes** | Operates technology park, generates commercial revenue |

**Conclusion:** Singapore Gov JV Pte Ltd is **NOT an Excluded Entity**.

The entity is engaged in commercial trading activities despite government majority ownership. It fails the "government functions only" test *(Commentary, para. 39)*.

This entity remains a Constituent Entity and will be included in GloBE calculations. However, as a joint arrangement with only 51% government ownership (and 49% owned by GlobalTech), the treatment depends on whether it meets the JV definition under Article 6.4—see Part 6.

### Result

GlobalTech has **2 Excluded Entities**:
- GT Pension Trustees Ltd (Pension Fund)
- GlobalTech Foundation (NPO)

**45 Constituent Entities remain in scope** for GloBE calculations.

---

## Common Assessment Challenges

### Challenge 1: Government Entity vs Commercial Entity

Government agencies that conduct commercial activities are not excluded. Key indicators of commercial activity:
- Revenue from goods or services sold at market prices
- Competition with private sector entities
- Profit-making objectives

*(Commentary, para. 38-42)*

### Challenge 2: NPO "Substantially Exempt" Test

The NPO exclusion requires income to be "substantially exempt" from tax—not entirely exempt. Incidental taxable income (e.g., from unrelated business activities) does not disqualify an NPO if the bulk of income is exempt.

**Practical threshold:** If 80%+ of income is tax-exempt, the "substantially exempt" test is generally met.

### Challenge 3: Pension Fund Subsidiaries

A subsidiary that provides services to the pension fund may also qualify for exclusion as a "Pension Services Entity" *(Article 1.5.1(d)(ii))* if:
- Established exclusively to hold assets or earn income for the pension fund
- All activities are connected with administering the pension fund's investments

Property holding subsidiaries of pension funds often qualify.

### Challenge 4: Investment Fund Investor Identification

The 80% ownership test requires identifying all investors and their tax status. For funds with numerous investors, this can be complex.

**Practical approach:**
- Obtain investor register from fund administrator
- Categorise investors: individuals, pension funds, taxable entities, tax-exempt entities
- Calculate percentage by value (not number) of investors meeting the test
- Document instances where investor status cannot be determined

---

## Excluded Entity Register

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

---

## Key References

**OECD GloBE Model Rules:**
- Article 1.5.1 — Definition of Excluded Entities (five categories)
- Article 1.5.2 — Five-year ownership test for Investment Funds

**OECD Commentary:**
- Paragraphs 36-50 — Detailed guidance on each exclusion category
- Paragraphs 38-42 — Government entity distinction from trading entities
- Paragraphs 47-50 — Investment fund ownership test mechanics

---

## Tools

This chapter completes the scope determination phase. The exclusions identified here affect calculations in later Parts:

| Tool | How This Chapter Connects |
|------|---------------------------|
| **GIR-001 GloBE Calculator** | Only CEs (not Excluded Entities) are input to GloBE calculations—your CE/Excluded Entity registers determine which entities require computation |
| **GIR-004 GIR Practice Form** | Section 1 of the GIR requires identification of Excluded Entities; your Excluded Entity register maps directly to this disclosure |

Accurate exclusion assessment ensures GloBE calculations are performed on the correct entity population.

---

## Summary

Excluded Entity assessment requires:

1. **Identify** potential exclusions from your CE register
2. **Gather** documentation for each exclusion category
3. **Apply** the specific tests for each category systematically
4. **Document** conclusions with supporting evidence
5. **Maintain** an Excluded Entity register with annual review
6. **Note** that Investment Fund exclusion applies only to UPEs meeting the 80% ownership test

---

## Next Step

You have now completed **Part 1: Scope Determination**. You should have:
- Confirmed the group meets the €750M revenue threshold (Chapter 1.1)
- Identified all Constituent Entities (Chapter 1.2)
- Determined the UPE and mapped IPEs (Chapter 1.3)
- Assessed and documented Excluded Entities (Chapter 1.4)

Proceed to **Part 1 Case Study: GlobalTech's Scope Assessment** to practice applying these concepts to a comprehensive scenario, then continue to **Part 2: The Charging Mechanism—IIR and UTPR**.
