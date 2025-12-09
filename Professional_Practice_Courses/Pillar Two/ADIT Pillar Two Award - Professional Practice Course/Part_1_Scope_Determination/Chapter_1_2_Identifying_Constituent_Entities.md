# Chapter 1.2: Identifying Constituent Entities

## Learning Objective

After completing this chapter, you will be able to identify which entities within an MNE group qualify as Constituent Entities for GloBE purposes and document the classification for each entity.

---

## The Starting Point: Consolidation Perimeter

A **Constituent Entity** is any entity that is included in the consolidated financial statements of the MNE group, plus any entity that is excluded solely due to size or materiality grounds *(Article 1.3.1)*.

Begin your identification process with the group's consolidation schedule—this is typically found in the notes to the consolidated financial statements or maintained separately by group finance.

---

## Step-by-Step Identification Process

### Step 1: Obtain the Consolidation Schedule

Request from group finance:
- List of all entities included in consolidated financial statements
- List of entities excluded on materiality/size grounds
- Ownership percentage for each entity
- Consolidation method used (full, proportionate, equity)

### Step 2: Classify Each Entity

For each entity on the list, determine its classification:

| Classification | Criteria | GloBE Treatment |
|----------------|----------|-----------------|
| **Fully consolidated subsidiary** | >50% ownership, full consolidation | Constituent Entity |
| **Proportionately consolidated** | Joint arrangement, proportionate consolidation | Constituent Entity |
| **Equity method investee** | Significant influence (typically 20-50%) | Generally NOT a Constituent Entity* |
| **Excluded on materiality** | Below consolidation threshold | Constituent Entity (if would otherwise consolidate) |

*Equity method investees may be Constituent Entities if they are Joint Ventures meeting specific criteria—see Chapter 1.2.4 below.

### Step 3: Identify Permanent Establishments

Permanent establishments (PEs) are treated as **separate Constituent Entities** from their main entity *(Article 1.3.2)*.

For each entity, determine:
- Does it have PEs in other jurisdictions?
- Are these PEs reflected in the financial statements?

A PE exists for GloBE purposes if it is treated as a PE under an applicable tax treaty, or if the jurisdiction taxes the entity on a net basis due to business presence *(Commentary, para. 28)*.

### Step 4: Identify Flow-Through Entities

A flow-through entity is tax transparent—its income is taxed in the hands of its owners rather than at entity level *(Article 10.1)*.

Common examples:
- Partnerships (in most jurisdictions)
- LLCs (if elected flow-through treatment)
- Certain trusts

Flow-through entities are Constituent Entities, but their income may be allocated to their owners for ETR calculation purposes—this is addressed in Part 3.

---

## Decision Flowchart: Is This Entity a Constituent Entity?

```
                    ┌─────────────────────────────────┐
                    │ Is the entity included in the   │
                    │ UPE's consolidated financial    │
                    │ statements?                     │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                   YES                              NO
                    │                               │
                    ▼                               ▼
        ┌───────────────────┐         ┌─────────────────────────┐
        │ CONSTITUENT       │         │ Was it excluded solely  │
        │ ENTITY            │         │ due to size/materiality?│
        └───────────────────┘         └───────────┬─────────────┘
                                                  │
                                      ┌───────────┴───────────┐
                                      │                       │
                                     YES                      NO
                                      │                       │
                                      ▼                       ▼
                          ┌───────────────────┐   ┌───────────────────┐
                          │ CONSTITUENT       │   │ NOT A CONSTITUENT │
                          │ ENTITY            │   │ ENTITY            │
                          └───────────────────┘   └───────────────────┘
```

---

## Ownership Thresholds and Consolidation Methods

### Controlling Interest (>50%)

Entities over which the UPE has control are fully consolidated and are Constituent Entities. Control is determined by:
- Majority voting rights, OR
- Power to govern financial and operating policies through other means

### Joint Arrangements (IFRS 11)

**Joint operations:** Assets and liabilities recognised directly—underlying entity is a Constituent Entity.

**Joint ventures:** Equity method applies by default, but may be a Constituent Entity if meeting the JV definition under Article 6.4 (ownership between 50% and 100% by parties outside the MNE group)—see Part 6.

### Significant Influence (20-50%)

Associates accounted for under the equity method are generally **not** Constituent Entities. Their profits are not included in GloBE Income; instead, dividends received from them may be excluded under Article 3.2.1(b).

---

## Worked Example: GlobalTech's Constituent Entity Mapping

### Background

Following the scope assessment in Chapter 1.1, GlobalTech's tax team must now identify all Constituent Entities. GlobalTech's group structure includes 52 legal entities across 12 jurisdictions.

### Data Extraction

The team obtains the consolidation schedule from the FY 2024 annual report:

| Entity | Jurisdiction | Ownership | Consolidation Method | PE? |
|--------|--------------|-----------|---------------------|-----|
| GlobalTech plc | UK | — | UPE | No |
| GT Holdings Ltd | UK | 100% | Full | No |
| GT Germany GmbH | Germany | 100% | Full | No |
| GT France SAS | France | 100% | Full | Yes (Belgium) |
| GT Singapore Pte | Singapore | 100% | Full | No |
| GT Ireland Ltd | Ireland | 100% | Full | No |
| GT Netherlands BV | Netherlands | 100% | Full | No |
| GT US Inc | USA | 100% | Full | No |
| GT Australia Pty | Australia | 100% | Full | No |
| TechStart Ltd | Ireland | 100% | Full (from Jul 2024) | No |
| Asian JV Ltd | Hong Kong | 40% | Equity | No |
| GT Pension Trustees | UK | 100% | Excluded (materiality) | No |
| ... | ... | ... | ... | ... |

*(52 entities total; extract shown for illustration)*

### Classification Analysis

| Entity | Classification | Reasoning |
|--------|---------------|-----------|
| GlobalTech plc | **CE** (UPE) | Ultimate Parent Entity |
| GT Holdings Ltd | **CE** | 100% owned, fully consolidated |
| GT Germany GmbH | **CE** | 100% owned, fully consolidated |
| GT France SAS | **CE** | 100% owned, fully consolidated |
| GT France SAS - Belgium PE | **CE** (separate) | PE treated as separate CE |
| GT Singapore Pte | **CE** | 100% owned, fully consolidated |
| Asian JV Ltd | **Not CE** | 40% equity method—not controlled |
| GT Pension Trustees | **CE** | Excluded on materiality, but would otherwise consolidate |

### Result

GlobalTech identifies **47 Constituent Entities**:
- 45 fully consolidated subsidiaries
- 1 PE (Belgium PE of GT France SAS)
- 1 entity excluded on materiality grounds

5 entities are **not** Constituent Entities (equity method associates).

### Documentation

The tax team prepares a CE register recording:
- Entity name and jurisdiction
- Ownership percentage
- Consolidation method
- CE classification (Yes/No)
- Reasoning for classification
- Date of assessment

---

## Special Cases

### Entities Joining Mid-Year

When an entity is acquired during the fiscal year:
- It becomes a Constituent Entity from the **acquisition date**
- GloBE calculations for that entity cover the post-acquisition period only *(Article 6.2.1)*

**GlobalTech example:** TechStart Ltd was acquired on 1 July 2024. It is a Constituent Entity for FY 2024, but GloBE Income and Covered Taxes are calculated for the period 1 July to 31 December 2024 only.

### Entities Leaving Mid-Year

When an entity is disposed of during the fiscal year:
- It ceases to be a Constituent Entity from the **disposal date**
- GloBE calculations cover the pre-disposal period only

### Dormant Entities

Dormant entities that remain in the consolidation schedule are Constituent Entities, even if they have no activity. They will typically qualify for the de minimis exclusion (Part 5) but must still be identified and tracked.

### Stapled Structures

In stapled structures where two or more entities are contractually bound and traded as a single unit, the structure may constitute a single MNE group. Each stapled entity is a Constituent Entity *(Article 6.5)*.

---

## Documentation Requirements

Maintain a **Constituent Entity Register** containing:

| Field | Description |
|-------|-------------|
| Entity name | Legal name |
| Jurisdiction | Country of tax residence |
| Entity identifier | Local registration number, LEI if available |
| Ownership % | Direct and indirect ownership by UPE |
| Consolidation method | Full, proportionate, equity, or excluded |
| CE classification | Yes / No |
| Classification rationale | Brief explanation |
| Effective date | Date entity entered/exited CE status |
| PE indicator | Yes / No; if Yes, list PE jurisdictions |

**Update frequency:** Review and update the register at each fiscal year-end and upon any acquisition, disposal, or restructuring.

---

## Key References

**OECD GloBE Model Rules:**
- Article 1.3.1 — Definition of Constituent Entity
- Article 1.3.2 — PE as separate Constituent Entity
- Article 6.2.1 — Entities joining and leaving an MNE group

**OECD Commentary:**
- Paragraphs 25-35 — Detailed guidance on Constituent Entity identification
- Paragraphs 28-30 — PE identification criteria

---

## Tools

While this chapter does not require a dedicated calculation tool, the Constituent Entity register you create here is **essential input** for tools used in later Parts:

| Tool | How This Chapter Connects |
|------|---------------------------|
| **GIR-001 GloBE Calculator** | You will run GloBE calculations for each CE identified here—the register determines which entities require computation |
| **GIR-004 GIR Practice Form** | Section 1 of the GIR requires disclosure of all CEs; your register maps directly to this section |

Accurate CE identification prevents errors in GIR completion and ensures no entity is missed from Top-Up Tax calculations.

---

## Summary

Identifying Constituent Entities requires:

1. **Obtain** the consolidation schedule from group finance
2. **Classify** each entity based on consolidation method and ownership
3. **Identify** PEs as separate Constituent Entities
4. **Document** classifications in a CE register with supporting rationale
5. **Update** the register for acquisitions, disposals, and restructurings

---

## Next Step

Once you have identified all Constituent Entities, proceed to **Chapter 1.3: Ultimate Parent Entity Determination** to confirm the filing entity and ownership chain.
