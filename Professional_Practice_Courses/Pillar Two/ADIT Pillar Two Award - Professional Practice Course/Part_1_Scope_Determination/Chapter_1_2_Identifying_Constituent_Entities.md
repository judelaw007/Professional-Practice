# Chapter 1.2: Identifying Constituent Entities

## Learning Objective

After completing this chapter, you will be able to identify which entities within an MNE group qualify as Constituent Entities for GloBE purposes and document the classification for each entity.

## Introduction

Once an MNE group crosses the revenue threshold, the next critical question becomes: which entities within the group structure are subject to GloBE calculations? This is not merely an administrative mapping exercise—it fundamentally determines where Top-Up Tax liabilities can arise and which jurisdictions' effective tax rates must be computed. The concept of "Constituent Entity" reflects a deliberate design choice to anchor the GloBE Rules in existing financial reporting frameworks, using the consolidation perimeter as the natural boundary of the MNE group. This approach leverages the substantial body of accounting standards on control and consolidation, avoiding the need to create an entirely new definition of what constitutes a group member for tax purposes.

## 1. The Starting Point: Consolidation Perimeter

A **Constituent Entity** is any entity that is included in the consolidated financial statements of the MNE group, plus any entity that is excluded solely due to size or materiality grounds *(Article 1.3.1)*.

Begin your identification process with the group's consolidation schedule—this is typically found in the notes to the consolidated financial statements or maintained separately by group finance.

The inclusion of entities "excluded solely due to size or materiality" is an important anti-avoidance feature. Without this provision, groups could avoid bringing low-taxed entities into GloBE calculations simply by keeping them below consolidation materiality thresholds—a relatively easy manipulation. By treating such entities as Constituent Entities regardless, the rules ensure that genuine commercial decisions about consolidation materiality do not create opportunities to shelter profits from the minimum tax.

## 2. Step-by-Step Identification Process

### 2.1 Step 1: Obtain the Consolidation Schedule

Request from group finance:
- List of all entities included in consolidated financial statements
- List of entities excluded on materiality/size grounds
- Ownership percentage for each entity
- Consolidation method used (full, proportionate, equity)

### 2.2 Step 2: Classify Each Entity

For each entity on the list, determine its classification:

| Classification | Criteria | GloBE Treatment |
|----------------|----------|-----------------|
| **Fully consolidated subsidiary** | >50% ownership, full consolidation | Constituent Entity |
| **Proportionately consolidated** | Joint arrangement, proportionate consolidation | Constituent Entity |
| **Equity method investee** | Significant influence (typically 20-50%) | Generally NOT a Constituent Entity* |
| **Excluded on materiality** | Below consolidation threshold | Constituent Entity (if would otherwise consolidate) |

*Equity method investees may be Constituent Entities if they are Joint Ventures meeting specific criteria—see Joint Arrangements section below.

### 2.3 Step 3: Identify Permanent Establishments

Permanent establishments (PEs) are treated as **separate Constituent Entities** from their main entity *(Article 1.3.2)*.

For each entity, determine:
- Does it have PEs in other jurisdictions?
- Are these PEs reflected in the financial statements?

A PE exists for GloBE purposes if it is treated as a PE under an applicable tax treaty, or if the jurisdiction taxes the entity on a net basis due to business presence *(Commentary, para. 28)*.

The treatment of PEs as separate Constituent Entities reflects a fundamental principle of international tax: taxing rights follow where economic activity occurs. A German subsidiary with a French PE creates profit in both jurisdictions; if the PE's income were simply pooled with its German head office, France's taxation of the PE profits would be obscured in a blended German ETR. By separating the PE, Pillar Two ensures that each jurisdiction's taxing rights—and the effective rate of tax imposed—are measured accurately. This mirrors the approach long taken in tax treaties, where PE profits are attributed and taxed as if the PE were a distinct enterprise.

### 2.4 Step 4: Identify Flow-Through Entities

A flow-through entity is tax transparent—its income is taxed in the hands of its owners rather than at entity level *(Article 10.1)*.

Common examples:
- Partnerships (in most jurisdictions)
- LLCs (if elected flow-through treatment)
- Certain trusts

Flow-through entities are Constituent Entities, but their income may be allocated to their owners for ETR calculation purposes—this is addressed in Part 3.

Flow-through treatment creates one of the more conceptually challenging areas of the GloBE framework. The entity exists for consolidated financial statement purposes—it has assets, liabilities, and income—but the tax on that income may be paid by its owners rather than by the entity itself. The GloBE Rules must therefore "push up" this income and the associated tax to the owner level to avoid either double-counting or missing the income entirely. For groups using US LLCs, UK LLPs, or similar structures, mapping these flow-through relationships is essential to accurate ETR computation.

## 3. Decision Flowchart: Is This Entity a Constituent Entity?

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

## 4. Ownership Thresholds and Consolidation Methods

### 4.1 Controlling Interest (>50%)

Entities over which the UPE has control are fully consolidated and are Constituent Entities. Control is determined by:
- Majority voting rights, OR
- Power to govern financial and operating policies through other means

### 4.2 Joint Arrangements (IFRS 11)

**Joint operations:** Assets and liabilities recognised directly—underlying entity is a Constituent Entity.

**Joint ventures:** Equity method applies by default, but may be a Constituent Entity if meeting the JV definition under Article 10.1 (where the UPE holds directly or indirectly 50% or more ownership interest in an equity method entity)—see Part 6.

### 4.3 Significant Influence (20-50%)

Associates accounted for under the equity method are generally **not** Constituent Entities. Their profits are not included in GloBE Income; instead, dividends received from them may be excluded under Article 3.2.1(b).

The distinction between controlled entities and equity method investees represents a policy choice about the reach of the minimum tax. Where an MNE group has control, it can direct the activities and tax affairs of the subsidiary—Pillar Two therefore holds the parent responsible for ensuring minimum taxation. But where the group holds only significant influence, it cannot unilaterally determine the investee's tax position. Extending Top-Up Tax liability to profits over which the MNE lacks control would be both practically difficult and arguably unfair. The exclusion of equity method associates from CE status thus reflects the limits of what can reasonably be expected of a minority investor.

## 5. Worked Example: Stratos's Constituent Entity Mapping

### 5.1 Background

Following the scope assessment in Chapter 1.1, Stratos's tax team must now identify all Constituent Entities. Stratos's group structure includes 52 legal entities across 12 jurisdictions.

### 5.2 Data Extraction

The team obtains the consolidation schedule from the FY 2024 annual report:

| Entity | Jurisdiction | Ownership | Consolidation Method | PE? |
|--------|--------------|-----------|---------------------|-----|
| Stratos Group plc | UK | — | UPE | No |
| SG Holdings Ltd | UK | 100% | Full | No |
| SG Germany GmbH | Germany | 100% | Full | No |
| SG France SAS | France | 100% | Full | Yes (Belgium) |
| SG Singapore Pte | Singapore | 100% | Full | No |
| SG Ireland Ltd | Ireland | 100% | Full | No |
| SG Netherlands BV | Netherlands | 100% | Full | No |
| SG US Inc | USA | 100% | Full | No |
| SG Australia Pty | Australia | 100% | Full | No |
| TechStart Ltd | Ireland | 100% | Full (from Jul 2024) | No |
| Asian JV Ltd | Hong Kong | 40% | Equity | No |
| SG Pension Trustees | UK | 100% | Excluded (materiality) | No |
| ... | ... | ... | ... | ... |

*(52 entities total; extract shown for illustration)*

### 5.3 Classification Analysis

| Entity | Classification | Reasoning |
|--------|---------------|-----------|
| Stratos Group plc | **CE** (UPE) | Ultimate Parent Entity |
| SG Holdings Ltd | **CE** | 100% owned, fully consolidated |
| SG Germany GmbH | **CE** | 100% owned, fully consolidated |
| SG France SAS | **CE** | 100% owned, fully consolidated |
| SG France SAS - Belgium PE | **CE** (separate) | PE treated as separate CE |
| SG Singapore Pte | **CE** | 100% owned, fully consolidated |
| Asian JV Ltd | **Not CE** | 40% equity method—not controlled |
| SG Pension Trustees | **CE** | Excluded on materiality, but would otherwise consolidate |

### 5.4 Result

Stratos identifies **47 Constituent Entities**:
- 45 fully consolidated subsidiaries
- 1 PE (Belgium PE of SG France SAS)
- 1 entity excluded on materiality grounds

5 entities are **not** Constituent Entities (equity method associates).

### 5.5 Documentation

The tax team prepares a CE register recording:
- Entity name and jurisdiction
- Ownership percentage
- Consolidation method
- CE classification (Yes/No)
- Reasoning for classification
- Date of assessment

## 6. Special Cases

### 6.1 Entities Joining Mid-Year

When an entity is acquired during the fiscal year:
- It becomes a Constituent Entity from the **acquisition date**
- GloBE calculations for that entity cover the post-acquisition period only *(Article 6.2.1)*

**Stratos example:** TechStart Ltd was acquired on 1 July 2024. It is a Constituent Entity for FY 2024, but GloBE Income and Covered Taxes are calculated for the period 1 July to 31 December 2024 only.

### 6.2 Entities Leaving Mid-Year

When an entity is disposed of during the fiscal year:
- It ceases to be a Constituent Entity from the **disposal date**
- GloBE calculations cover the pre-disposal period only

### 6.3 Dormant Entities

Dormant entities that remain in the consolidation schedule are Constituent Entities, even if they have no activity. They will typically qualify for the de minimis exclusion (Part 5) but must still be identified and tracked.

### 6.4 Stapled Structures

In stapled structures where two or more entities are contractually bound and traded as a single unit, the structure may constitute a single MNE group. Each stapled entity is a Constituent Entity *(Article 6.5)*.

These special cases illustrate a recurring theme in the GloBE framework: the rules attempt to align tax outcomes with economic substance rather than legal form. When an entity joins a group mid-year, only the period of group membership creates obligations—but the acquiring group cannot escape responsibility by delaying technical completion until year-end. Similarly, stapled structures that function economically as single enterprises are treated as such, preventing artificial separation of what is, in commercial reality, one business. This substance-over-form orientation runs throughout Pillar Two and should guide practitioners in resolving ambiguous situations.

## 7. Documentation Requirements

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

The Constituent Entity register is not merely a compliance checklist—it forms the foundation upon which all subsequent GloBE calculations are built. An error in CE identification propagates through the entire framework: miss a CE, and its income escapes the jurisdictional ETR; incorrectly include an equity method associate, and you may compute Top-Up Tax on profits the group cannot control. For complex groups with hundreds of entities, this register becomes a critical piece of tax governance infrastructure, requiring clear ownership, regular review, and integration with M&A processes to ensure new acquisitions are captured promptly. The investment in maintaining an accurate register pays dividends throughout the GloBE compliance cycle.
