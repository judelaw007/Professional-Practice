# Chapter 1.3: Ultimate Parent Entity Determination

## Learning Objective

After completing this chapter, you will be able to identify the Ultimate Parent Entity of an MNE group and understand the roles of intermediate parent entities in the GloBE framework.

## Introduction

The Ultimate Parent Entity stands at the apex of the Pillar Two architecture—both literally, as the top of the group structure, and functionally, as the entity bearing primary responsibility for ensuring minimum taxation throughout the group. The UPE concept reflects a fundamental policy choice: rather than imposing compliance obligations on every entity in a multinational group, the GloBE Rules concentrate responsibility at the ultimate controlling entity. This entity has visibility over the entire group's operations, the authority to restructure or relocate activities, and the capacity to absorb Top-Up Tax liabilities. The UPE's jurisdiction therefore becomes strategically significant, as it determines which country first applies the Income Inclusion Rule and collects any resulting Top-Up Tax.

## 1. Defining the Ultimate Parent Entity

The **Ultimate Parent Entity (UPE)** is the entity at the top of the MNE group that:

1. Owns, directly or indirectly, a controlling interest in any other entity in the group, AND
2. Is not owned by another entity with a controlling interest in it *(Article 1.5.1)*

In simpler terms: the UPE is the entity that consolidates all other group entities and is not itself consolidated by another entity.

This dual requirement—owning a controlling interest downward while not being controlled from above—ensures there can be only one UPE per MNE group. The concept draws on familiar corporate law notions of control but applies them in a tax context where the consequences of UPE status are substantial. Identifying the UPE is rarely complex for straightforward corporate structures, but groups involving trusts, foundations, private equity sponsors, or dual-listed arrangements require careful analysis of where ultimate control truly resides.

## 2. Step-by-Step UPE Identification

### 2.1 Step 1: Start with the Consolidating Entity

Identify which entity prepares the consolidated financial statements used for the revenue threshold test (Chapter 1.1). This is typically the UPE.

### 2.2 Step 2: Verify No Higher-Level Consolidation

Confirm that this entity is not itself included in another entity's consolidated financial statements. Check:

- Is the entity a subsidiary of another company?
- Is there a parent company that consolidates this entity?
- Are there any trust, foundation, or fund structures above it?

### 2.3 Step 3: Confirm Controlling Interest

The UPE must hold a **controlling interest** in at least one other entity. Controlling interest means *(Article 10.1)*:

- Ownership of more than 50% of voting rights, OR
- Control over the entity's board or management, OR
- Entitlement to more than 50% of profits

If the entity at the top holds less than a controlling interest in all subsidiaries, it may not qualify as a UPE—reassess the group structure.

## 3. Common UPE Structures

### 3.1 Listed Company as UPE

Most common scenario. A publicly listed company sits at the top, prepares consolidated financial statements, and is the UPE.

**Example:** Stratos Group plc (listed on LSE) is the UPE of the Stratos group.

### 3.2 Private Holding Company as UPE

A privately held company owns the operating group. The holding company prepares consolidated accounts and is the UPE.

### 3.3 Trust or Foundation as UPE

Where a trust or foundation sits at the top of the structure and controls the group, it may be the UPE if it prepares consolidated financial statements *(Commentary, para. 18)*.

### 3.4 Individual or Family Ownership

Where individuals or families own the group directly (without an interposed holding company), the highest entity that prepares consolidated financial statements is the UPE. The individuals themselves are not Constituent Entities.

The variety of structures that can serve as UPEs reflects the global diversity of corporate ownership. Listed companies are most straightforward—public markets and regulatory requirements ensure transparent structures. But privately held groups, family offices, and trust-based structures require deeper analysis. The key insight is that the GloBE Rules follow accounting consolidation: if an entity prepares consolidated financial statements that capture the entire group, and no higher entity consolidates it, that entity is the UPE regardless of the legal form of its owners above. Individuals and families sitting above the UPE are not drawn into the GloBE framework—the rules tax corporate profits, not personal wealth.

## 4. Intermediate Parent Entities

An **Intermediate Parent Entity (IPE)** is a Constituent Entity that owns a controlling interest in another Constituent Entity but is not the UPE *(Article 10.1)*.

IPEs are important because:

1. **IIR application:** If the UPE jurisdiction does not apply the IIR, an IPE in a jurisdiction that does apply the IIR may be required to apply the rule instead *(Article 2.1.2)*
2. **Filing obligations:** Some jurisdictions require local filing by IPEs
3. **Allocation:** Top-Up Tax allocation may flow through IPEs in the ownership chain

### 4.1 Identifying IPEs

From your Constituent Entity register (Chapter 1.2), identify entities that:
- Are owned by another Constituent Entity (i.e., not the UPE)
- Own a controlling interest (>50%) in at least one other Constituent Entity

IPEs serve as critical backstops in the GloBE architecture. The designers of Pillar Two recognised that not all countries would implement the rules simultaneously—and some might never do so. If the UPE's jurisdiction fails to apply a Qualified IIR, the Top-Up Tax that should have been collected there would be lost without a fallback mechanism. IPEs provide that fallback: an IPE in a jurisdiction with a Qualified IIR steps into the UPE's shoes and applies the IIR to low-taxed subsidiaries beneath it in the ownership chain. This cascading mechanism ensures broad coverage even with imperfect global adoption, though it significantly complicates compliance for groups with IPEs in multiple jurisdictions.

## 5. Worked Example: Stratos's UPE and IPE Analysis

### 5.1 Group Structure

```
Stratos Group plc (UK) ← UPE
    │
    ├── SG Holdings Ltd (UK) 100% ← IPE
    │       │
    │       ├── SG Germany GmbH (Germany) 100%
    │       ├── SG France SAS (France) 100%
    │       │       └── [Belgium PE]
    │       └── SG Netherlands BV (Netherlands) 100%
    │               │
    │               ├── SG Ireland Ltd (Ireland) 100%
    │               └── SG Singapore Pte (Singapore) 100%
    │
    ├── SG US Holdings Inc (USA) 100% ← IPE
    │       │
    │       └── SG US Operating Inc (USA) 100%
    │
    └── SG Australia Pty (Australia) 100%
```

### 5.2 Analysis

**UPE Identification:**

| Question | Answer |
|----------|--------|
| Which entity prepares consolidated financial statements? | Stratos Group plc |
| Is it consolidated by another entity? | No—listed company with no parent |
| Does it hold controlling interest in other entities? | Yes—100% of SG Holdings Ltd, SG US Holdings Inc, SG Australia Pty |

**Conclusion:** Stratos Group plc is the **UPE**.

**IPE Identification:**

| Entity | Owned by CE? | Owns >50% of another CE? | IPE? |
|--------|--------------|--------------------------|------|
| SG Holdings Ltd | Yes (UPE) | Yes (SG Germany, SG France, SG Netherlands) | **Yes** |
| SG Netherlands BV | Yes (SG Holdings) | Yes (SG Ireland, SG Singapore) | **Yes** |
| SG US Holdings Inc | Yes (UPE) | Yes (SG US Operating) | **Yes** |
| SG Germany GmbH | Yes (SG Holdings) | No | No |
| SG France SAS | Yes (SG Holdings) | No (PE is not a separate legal entity) | No |

**Result:** 3 Intermediate Parent Entities identified.

### 5.3 Documentation

The tax team records in the CE register:
- UPE: Stratos Group plc
- IPEs: SG Holdings Ltd, SG Netherlands BV, SG US Holdings Inc
- Direct ownership chain for each CE

## 6. Multi-Parented MNE Groups

A **Multi-Parented MNE Group** exists where two or more entities that would otherwise be separate UPEs are stapled together or operate under a dual-listed company arrangement *(Article 6.5)*.

### 6.1 Stapled Structures

Entities whose equity interests are:
- Stapled together and cannot be transferred independently, OR
- Listed and traded as a single unit

These are treated as a single MNE group, with one entity designated as the UPE for GloBE purposes.

### 6.2 Dual-Listed Companies (DLC)

Two listed companies that operate as a single economic enterprise through contractual arrangements, but maintain separate legal identities and listings.

For GloBE purposes:
- Both companies and their subsidiaries form a single MNE group
- One must be designated as the UPE
- The combined group must meet the €750 million threshold

### 6.3 Identification Steps for Multi-Parented Groups

1. Identify whether a stapled or DLC arrangement exists
2. Determine combined group revenue for threshold test
3. Designate one entity as UPE (typically per existing group arrangements)
4. Map all subsidiaries of both "parents" as Constituent Entities

Multi-parented structures represent some of the most complex scenarios in Pillar Two. These arrangements—often created for historical, regulatory, or commercial reasons entirely unrelated to tax—must now be squeezed into a framework designed around single-parent hierarchies. The requirement to designate one entity as UPE for GloBE purposes creates practical challenges: both "parents" may have legitimate claims to primacy, and the designation affects which jurisdiction first applies the IIR. Groups with dual-listed or stapled structures should engage with their advisors early to establish clear protocols for GloBE compliance, as the designation may have significant tax and administrative consequences.

## 7. UPE Jurisdiction and Its Significance

The UPE's jurisdiction determines:

| Factor | Why It Matters |
|--------|----------------|
| **IIR application** | If the UPE jurisdiction has implemented a Qualified IIR, the UPE applies the IIR first *(Article 2.1.1)* |
| **Filing obligations** | GIR filing typically occurs in the UPE jurisdiction |
| **UTPR exposure** | If UPE jurisdiction has no IIR, UTPR in other jurisdictions may apply |

**Stratos example:** The UK has implemented a Qualified IIR effective from 2024. Stratos Group plc (UK UPE) will apply the IIR and be responsible for UK Multinational Top-Up Tax on low-taxed jurisdictions.

The UPE's jurisdiction thus becomes a matter of genuine strategic importance. Under the GloBE framework, the first jurisdiction to apply a Qualified IIR collects the Top-Up Tax—creating a form of tax competition in reverse. Countries that implement Pillar Two early and comprehensively capture revenue that might otherwise be collected by UTPR-applying jurisdictions further down the chain. For groups, this means the UPE's location affects not just where compliance occurs but which tax authority receives any Top-Up Tax payments. While relocating a UPE purely for Pillar Two reasons would be an extreme measure, groups should understand these dynamics when evaluating holding structures for other purposes.

## 8. Changes in UPE Status

### 8.1 Acquisition of the UPE

If another entity acquires the UPE:
- The acquiring entity's group becomes the new MNE group
- The former UPE becomes a Constituent Entity (likely an IPE) in the new group
- Reassess scope at the new group level

### 8.2 Demerger Creating New UPE

If the group demerges:
- Each resulting group has its own UPE
- Each group independently assesses the €750 million threshold
- CE registers must be prepared for each new group

## 9. Documentation Requirements

Add to your group structure documentation:

| Document | Content |
|----------|---------|
| **UPE confirmation memo** | Entity name, jurisdiction, basis for UPE status |
| **IPE schedule** | List of IPEs with ownership chain |
| **Group structure chart** | Visual representation showing UPE, IPEs, and all CEs |
| **IIR jurisdiction analysis** | Whether UPE jurisdiction has Qualified IIR |

Identifying the UPE and mapping IPEs is not a one-time exercise but an ongoing governance obligation. Corporate acquisitions, disposals, and restructurings can change UPE status—sometimes dramatically, as when a standalone group is acquired and becomes a subsidiary of a larger multinational. Groups should build UPE monitoring into their M&A due diligence processes and transaction planning, ensuring that Pillar Two implications are considered alongside the traditional tax structuring analysis. The interplay between UPE status, IPE exposure, and jurisdictional IIR/UTPR implementation creates a complex compliance landscape that rewards proactive planning over reactive firefighting.
