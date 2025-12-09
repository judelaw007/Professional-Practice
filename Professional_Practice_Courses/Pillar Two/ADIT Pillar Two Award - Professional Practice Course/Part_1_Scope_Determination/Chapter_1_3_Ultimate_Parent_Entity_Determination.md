# Chapter 1.3: Ultimate Parent Entity Determination

## Learning Objective

After completing this chapter, you will be able to identify the Ultimate Parent Entity of an MNE group and understand the roles of intermediate parent entities in the GloBE framework.

---

## Defining the Ultimate Parent Entity

The **Ultimate Parent Entity (UPE)** is the entity at the top of the MNE group that:

1. Owns, directly or indirectly, a controlling interest in any other entity in the group, AND
2. Is not owned by another entity with a controlling interest in it *(Article 1.4.1)*

In simpler terms: the UPE is the entity that consolidates all other group entities and is not itself consolidated by another entity.

---

## Step-by-Step UPE Identification

### Step 1: Start with the Consolidating Entity

Identify which entity prepares the consolidated financial statements used for the revenue threshold test (Chapter 1.1). This is typically the UPE.

### Step 2: Verify No Higher-Level Consolidation

Confirm that this entity is not itself included in another entity's consolidated financial statements. Check:

- Is the entity a subsidiary of another company?
- Is there a parent company that consolidates this entity?
- Are there any trust, foundation, or fund structures above it?

### Step 3: Confirm Controlling Interest

The UPE must hold a **controlling interest** in at least one other entity. Controlling interest means *(Article 10.1)*:

- Ownership of more than 50% of voting rights, OR
- Control over the entity's board or management, OR
- Entitlement to more than 50% of profits

If the entity at the top holds less than a controlling interest in all subsidiaries, it may not qualify as a UPE—reassess the group structure.

---

## Common UPE Structures

### Listed Company as UPE

Most common scenario. A publicly listed company sits at the top, prepares consolidated financial statements, and is the UPE.

**Example:** GlobalTech Industries plc (listed on LSE) is the UPE of the GlobalTech group.

### Private Holding Company as UPE

A privately held company owns the operating group. The holding company prepares consolidated accounts and is the UPE.

### Trust or Foundation as UPE

Where a trust or foundation sits at the top of the structure and controls the group, it may be the UPE if it prepares consolidated financial statements *(Commentary, para. 18)*.

### Individual or Family Ownership

Where individuals or families own the group directly (without an interposed holding company), the highest entity that prepares consolidated financial statements is the UPE. The individuals themselves are not Constituent Entities.

---

## Intermediate Parent Entities

An **Intermediate Parent Entity (IPE)** is a Constituent Entity that owns a controlling interest in another Constituent Entity but is not the UPE *(Article 10.1)*.

IPEs are important because:

1. **IIR application:** If the UPE jurisdiction does not apply the IIR, an IPE in a jurisdiction that does apply the IIR may be required to apply the rule instead *(Article 2.1.2)*
2. **Filing obligations:** Some jurisdictions require local filing by IPEs
3. **Allocation:** Top-Up Tax allocation may flow through IPEs in the ownership chain

### Identifying IPEs

From your Constituent Entity register (Chapter 1.2), identify entities that:
- Are owned by another Constituent Entity (i.e., not the UPE)
- Own a controlling interest (>50%) in at least one other Constituent Entity

---

## Worked Example: GlobalTech's UPE and IPE Analysis

### Group Structure

```
GlobalTech Industries plc (UK) ← UPE
    │
    ├── GT Holdings Ltd (UK) 100% ← IPE
    │       │
    │       ├── GT Germany GmbH (Germany) 100%
    │       ├── GT France SAS (France) 100%
    │       │       └── [Belgium PE]
    │       └── GT Netherlands BV (Netherlands) 100%
    │               │
    │               ├── GT Ireland Ltd (Ireland) 100%
    │               └── GT Singapore Pte (Singapore) 100%
    │
    ├── GT US Holdings Inc (USA) 100% ← IPE
    │       │
    │       └── GT US Operating Inc (USA) 100%
    │
    └── GT Australia Pty (Australia) 100%
```

### Analysis

**UPE Identification:**

| Question | Answer |
|----------|--------|
| Which entity prepares consolidated financial statements? | GlobalTech Industries plc |
| Is it consolidated by another entity? | No—listed company with no parent |
| Does it hold controlling interest in other entities? | Yes—100% of GT Holdings Ltd, GT US Holdings Inc, GT Australia Pty |

**Conclusion:** GlobalTech Industries plc is the **UPE**.

**IPE Identification:**

| Entity | Owned by CE? | Owns >50% of another CE? | IPE? |
|--------|--------------|--------------------------|------|
| GT Holdings Ltd | Yes (UPE) | Yes (GT Germany, GT France, GT Netherlands) | **Yes** |
| GT Netherlands BV | Yes (GT Holdings) | Yes (GT Ireland, GT Singapore) | **Yes** |
| GT US Holdings Inc | Yes (UPE) | Yes (GT US Operating) | **Yes** |
| GT Germany GmbH | Yes (GT Holdings) | No | No |
| GT France SAS | Yes (GT Holdings) | No (PE is not a separate legal entity) | No |

**Result:** 3 Intermediate Parent Entities identified.

### Documentation

The tax team records in the CE register:
- UPE: GlobalTech Industries plc
- IPEs: GT Holdings Ltd, GT Netherlands BV, GT US Holdings Inc
- Direct ownership chain for each CE

---

## Multi-Parented MNE Groups

A **Multi-Parented MNE Group** exists where two or more entities that would otherwise be separate UPEs are stapled together or operate under a dual-listed company arrangement *(Article 6.5)*.

### Stapled Structures

Entities whose equity interests are:
- Stapled together and cannot be transferred independently, OR
- Listed and traded as a single unit

These are treated as a single MNE group, with one entity designated as the UPE for GloBE purposes.

### Dual-Listed Companies (DLC)

Two listed companies that operate as a single economic enterprise through contractual arrangements, but maintain separate legal identities and listings.

For GloBE purposes:
- Both companies and their subsidiaries form a single MNE group
- One must be designated as the UPE
- The combined group must meet the €750M threshold

### Identification Steps for Multi-Parented Groups

1. Identify whether a stapled or DLC arrangement exists
2. Determine combined group revenue for threshold test
3. Designate one entity as UPE (typically per existing group arrangements)
4. Map all subsidiaries of both "parents" as Constituent Entities

---

## UPE Jurisdiction and Its Significance

The UPE's jurisdiction determines:

| Factor | Why It Matters |
|--------|----------------|
| **IIR application** | If the UPE jurisdiction has implemented a Qualified IIR, the UPE applies the IIR first *(Article 2.1.1)* |
| **Filing obligations** | GIR filing typically occurs in the UPE jurisdiction |
| **UTPR exposure** | If UPE jurisdiction has no IIR, UTPR in other jurisdictions may apply |

**GlobalTech example:** The UK has implemented a Qualified IIR effective from 2024. GlobalTech Industries plc (UK UPE) will apply the IIR and be responsible for UK Multinational Top-Up Tax on low-taxed jurisdictions.

---

## Changes in UPE Status

### Acquisition of the UPE

If another entity acquires the UPE:
- The acquiring entity's group becomes the new MNE group
- The former UPE becomes a Constituent Entity (likely an IPE) in the new group
- Reassess scope at the new group level

### Demerger Creating New UPE

If the group demerges:
- Each resulting group has its own UPE
- Each group independently assesses the €750M threshold
- CE registers must be prepared for each new group

---

## Documentation Requirements

Add to your group structure documentation:

| Document | Content |
|----------|---------|
| **UPE confirmation memo** | Entity name, jurisdiction, basis for UPE status |
| **IPE schedule** | List of IPEs with ownership chain |
| **Group structure chart** | Visual representation showing UPE, IPEs, and all CEs |
| **IIR jurisdiction analysis** | Whether UPE jurisdiction has Qualified IIR |

---

## Key References

**OECD GloBE Model Rules:**
- Article 1.4.1 — Definition of Ultimate Parent Entity
- Article 2.1.1 — IIR application by UPE
- Article 2.1.2 — IIR application by IPE
- Article 6.5 — Multi-Parented MNE Groups

**OECD Commentary:**
- Paragraphs 15-24 — UPE identification guidance
- Paragraphs 18-20 — Trusts, foundations, and non-corporate UPEs

---

## Tools

This chapter establishes the ownership structure that determines how Top-Up Tax flows through the group. The UPE and IPE identification connects to:

| Tool | How This Chapter Connects |
|------|---------------------------|
| **GIR-001 GloBE Calculator** | Top-Up Tax calculated per jurisdiction flows up through IPEs to the UPE—the ownership chain determines allocation |
| **GIR-004 GIR Practice Form** | Section 1 requires UPE identification; ownership chains determine reporting structure |
| **GIR-005 DFE Assessment Tool** | If a Designated Filing Entity other than the UPE will file, the ownership chain analysis from this chapter is required input |

---

## Summary

Ultimate Parent Entity determination requires:

1. **Identify** the entity preparing consolidated financial statements
2. **Verify** it is not consolidated by another entity
3. **Confirm** it holds controlling interest in at least one CE
4. **Map** Intermediate Parent Entities in the ownership chain
5. **Assess** UPE jurisdiction for IIR implementation status
6. **Document** the UPE, IPEs, and ownership structure

---

## Next Step

Once you have identified the UPE and mapped IPEs, proceed to **Chapter 1.4: Excluded Entity Assessment** to determine whether any entities qualify for exclusion from GloBE scope.
