# Chapter 3.5: PE and Flow-Through Allocations

## Learning Objective

After completing this chapter, you will be able to allocate GloBE Income between main entities and permanent establishments, and apply the correct treatment for flow-through entities including tax transparent structures and reverse hybrids.

## Introduction

The GloBE framework's jurisdictional blending approach—calculating a single ETR for all entities in a given country—works smoothly when each entity is a distinct legal person taxed where it resides. Reality is messier. Multinational groups routinely operate through permanent establishments that have no separate legal identity but are taxed as if they did. They structure investments through partnerships, limited liability companies, and other vehicles that different countries classify differently for tax purposes. Some entities are transparent to their owners; others are opaque; still others are transparent in one jurisdiction but opaque in another. Without allocation rules to address these structures, the framework would either double-count income, miss income entirely, or attribute income to the wrong jurisdiction—undermining the minimum tax's fundamental purpose. Articles 3.4 and 3.5 provide the machinery to untangle these complexities, ensuring that every euro of GloBE Income lands in exactly one jurisdiction for ETR calculation purposes.

## Why Special Allocation Rules Are Needed

The GloBE Rules rely on financial accounting information, but:

| Structure | Challenge |
|-----------|-----------|
| **Permanent Establishments** | PEs are treated as separate CEs but may not have separate financial accounts |
| **Flow-Through Entities** | Income may be taxed at owner level, not entity level |
| **Reverse Hybrids** | Different jurisdictions may treat the same entity differently |

**Result:** Articles 3.4 and 3.5 provide allocation rules to ensure income is attributed to the correct jurisdiction for ETR calculation.

## Part A: Permanent Establishment Allocations

### PE as a Separate Constituent Entity

For GloBE purposes, a PE is treated as a **separate Constituent Entity** located in the jurisdiction where it operates *(Article 10.1)*.

**Key implication:** Each PE has its own:
- GloBE Income calculation
- Covered Taxes calculation
- ETR calculation
- Potential Top-Up Tax

### Three Types of PE *(Article 10.1)*

| Type | Definition | Reference |
|------|------------|-----------|
| **(a) Treaty PE** | PE under applicable tax treaty between main entity jurisdiction and PE jurisdiction | Art. 10.1(a) |
| **(b) Domestic Law PE** | PE under domestic law of PE jurisdiction (no treaty) | Art. 10.1(b) |
| **(c) Deemed PE** | Would be a PE under OECD Model if PE jurisdiction had a treaty with main entity jurisdiction | Art. 10.1(c) |

### Step 1: Determine PE's Financial Accounting Net Income *(Article 3.4.1)*

**Priority order:**

```
1. Use PE's separate financial accounts (if they exist)
         │
         ▼
2. If no separate accounts:
   Prepare notional standalone accounts using UPE's accounting standard
```

### Step 2: Adjust to Reflect Attributable Amounts *(Article 3.4.2)*

The PE's income must reflect only amounts **attributable to the PE** under:

| PE Type | Attribution Basis |
|---------|-------------------|
| Treaty PE *(Art. 10.1(a))* | Applicable tax treaty or PE jurisdiction domestic law |
| Domestic Law PE *(Art. 10.1(b))* | PE jurisdiction domestic law |
| Deemed PE *(Art. 10.1(c))* | Article 7 of OECD Model Tax Convention (arm's length) |

**Important:** The attribution is based on **what income is attributable**, not what income is actually taxed.

### Worked Example: PE Income Attribution

**Facts:**
- UK Co (main entity) has a PE in Country X
- UK-Country X tax treaty applies
- PE earns €1,000,000 in royalties
- Country X exempts 50% of royalties from tax

**PE Income for GloBE:**

| Item | Amount |
|------|--------|
| Royalties attributable to PE under treaty | €1,000,000 |
| Amount actually taxed in Country X | €500,000 |
| **GloBE Income of PE** | **€1,000,000** |

**Key point:** GloBE uses the €1,000,000 attributable under the treaty, regardless of the €500,000 actually taxed.

The decision to treat PEs as separate Constituent Entities reflects the economic reality that many PE operations are substantial businesses in their own right, even without separate legal personality. A manufacturing plant, a sales office, or a research facility operating as a PE may generate significant profits and employ hundreds of people. Tax treaties have long recognised this reality by giving the PE jurisdiction primary taxing rights over profits attributable to the PE. The GloBE framework honours this by treating the PE as a separate CE located in its operating jurisdiction, ensuring that the PE's ETR is measured there—not blended with the main entity's home jurisdiction. This prevents groups from sheltering PE profits in high-tax home countries while actually operating in low-tax environments. The three-tier PE definition (treaty, domestic law, deemed) ensures comprehensive coverage: if any framework creates PE status, the GloBE allocation rules apply.

## Step 3: Exclude PE Income from Main Entity *(Article 3.4.4)*

### The Rule

PE income is **not included** in the main entity's GloBE Income.

### The Exception: PE Loss Push-Down *(Article 3.4.5)*

If the PE has a **GloBE Loss**, special rules apply:

**Condition:** The PE loss is treated as an expense for domestic tax purposes in the main entity's jurisdiction.

**Treatment:**

| Step | Action |
|------|--------|
| 1 | PE Loss is treated as an **expense of the main entity** (not the PE) |
| 2 | PE's GloBE Loss for that year = €0 |
| 3 | Main entity's GloBE Income is reduced by the loss |
| 4 | Future PE profits are treated as **main entity income** until loss is recaptured |

### Worked Example: PE Loss Push-Down

**Year 1:**
- SG France SAS (main entity) has Belgium PE
- Belgium PE has GloBE Loss of €(500,000)
- France allows deduction for PE losses

| Entity | GloBE Income |
|--------|--------------|
| Belgium PE (before adjustment) | €(500,000) |
| Belgium PE (after Art. 3.4.5) | €0 |
| SG France SAS (before adjustment) | €2,000,000 |
| SG France SAS (after Art. 3.4.5) | €1,500,000 |

**Year 2:**
- Belgium PE earns GloBE Income of €300,000

| Entity | GloBE Income | Recapture |
|--------|--------------|-----------|
| Belgium PE | €0 | €300,000 allocated to France |
| SG France SAS | + €300,000 | Recaptured profit |
| Remaining to recapture | | €200,000 |

**Year 3:**
- Belgium PE earns GloBE Income of €400,000

| Entity | GloBE Income | Recapture |
|--------|--------------|-----------|
| Belgium PE | €200,000 | €200,000 completes recapture |
| SG France SAS | + €200,000 | Final recapture |
| Remaining | | €0 (fully recaptured) |

The PE loss push-down rule addresses a specific asymmetry that would otherwise arise. Many jurisdictions allow taxpayers to deduct foreign PE losses against domestic income—a policy designed to prevent economic double taxation of overall losses. Without the GloBE adjustment, a group could benefit twice: first by reducing its main entity's domestic tax through the PE loss deduction, and second by retaining a GloBE loss in the PE jurisdiction that might shield future profits. Article 3.4.5 closes this gap by following the tax: if the main entity jurisdiction grants the deduction, the GloBE loss moves there too. The recapture mechanism then ensures that future PE profits first replenish the main entity's GloBE Income before returning to the PE jurisdiction—maintaining symmetry over the full cycle. This creates administrative complexity but prevents the framework from inadvertently subsidising loss-making foreign operations.

## PE Income Allocation Methodology

### Step-by-Step Process

```
┌─────────────────────────────────────────────────────────────────┐
│        PE INCOME ALLOCATION — STEP-BY-STEP                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  STEP 1: Identify all PEs of the Main Entity                   │
│          └── Treaty PEs, Domestic Law PEs, Deemed PEs          │
│                           │                                     │
│                           ▼                                     │
│  STEP 2: For each PE, determine Financial Accounting           │
│          Net Income                                             │
│          ├── Option A: Use separate PE accounts                │
│          └── Option B: Prepare notional standalone accounts    │
│                           │                                     │
│                           ▼                                     │
│  STEP 3: Adjust for attributable income/expense                │
│          ├── Treaty PE: Per applicable treaty/domestic law     │
│          ├── Domestic PE: Per PE jurisdiction law              │
│          └── Deemed PE: Per OECD Model Art. 7                  │
│                           │                                     │
│                           ▼                                     │
│  STEP 4: Check for PE losses                                   │
│          ├── If PE has loss AND loss deductible for main       │
│          │   entity domestic tax: Apply Art. 3.4.5             │
│          └── Otherwise: PE retains loss                        │
│                           │                                     │
│                           ▼                                     │
│  STEP 5: Allocate Covered Taxes                                │
│          └── Taxes on PE income to PE jurisdiction             │
│                           │                                     │
│                           ▼                                     │
│  STEP 6: Calculate ETR for each jurisdiction separately        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Part B: Flow-Through Entity Treatment

### Flow-Through Entity Definitions *(Article 10.2)*

| Term | Definition |
|------|------------|
| **Flow-Through Entity** | Entity that is fiscally transparent in its jurisdiction of creation (unless tax resident elsewhere) |
| **Tax Transparent Entity** | Flow-through entity that is also treated as transparent by its owners' jurisdiction |
| **Reverse Hybrid Entity** | Flow-through entity that is treated as opaque (non-transparent) by its owners' jurisdiction |

### Visual Summary

```
                    FLOW-THROUGH ENTITY
                    (transparent in own jurisdiction)
                              │
              ┌───────────────┴───────────────┐
              │                               │
     TAX TRANSPARENT ENTITY          REVERSE HYBRID ENTITY
     (owner also treats as            (owner treats as
      transparent)                     opaque)
              │                               │
              ▼                               ▼
     Income flows to owner           Income stays at entity
     for GloBE purposes              for GloBE purposes
```

The flow-through entity rules represent one of the more technically complex areas of the GloBE framework because they must navigate the fundamental divergence in how different jurisdictions classify the same legal structures. A US LLC may be a corporation for German tax purposes but a disregarded entity for US purposes; a Luxembourg SCSp may be transparent to its UK owner but opaque to a French owner. Rather than imposing a uniform GloBE classification, Articles 3.5.1 and 3.5.2 work with existing tax classifications—but they must determine whose classification controls. The key insight is that transparency is determined from the perspective of both the entity's jurisdiction and the owner's jurisdiction: only when both agree the entity is transparent does income flow through. When they disagree—the reverse hybrid scenario—income stays at the entity level. This approach respects existing tax classifications while ensuring that every item of income lands somewhere for ETR calculation.

## Tax Transparent Entity Treatment *(Article 3.5.1)*

### The Rule

For a **Tax Transparent Entity**, the GloBE Income and Covered Taxes are allocated to the **Constituent Entity owners** in proportion to their ownership interests.

### When This Applies

The entity must be:
1. Fiscally transparent in its jurisdiction of creation, AND
2. Fiscally transparent in the jurisdiction of its owners

### Common Examples

| Structure | Typical Treatment |
|-----------|-------------------|
| US LLC owned by US corporation | Tax transparent (single-member or check-the-box) |
| UK LLP owned by UK companies | Tax transparent |
| German KG owned by German GmbH | Tax transparent |
| Luxembourg SCSp owned by Luxembourg entities | Tax transparent |

### Worked Example: Tax Transparent Entity

**Structure:**
```
SG Holdings Ltd (UK)
    │
    └── 100% ownership
            │
            ▼
    SG US LLC (Delaware)
    [Check-the-box disregarded entity]
```

**SG US LLC financials:**
- GloBE Income: €3,000,000
- Covered Taxes: €0 (disregarded for US tax)

**Allocation under Article 3.5.1:**

| Entity | GloBE Income | Covered Taxes |
|--------|--------------|---------------|
| SG US LLC | €0 | €0 |
| SG Holdings Ltd (UK) | + €3,000,000 | + €0 |

**Effect:** The US LLC income increases the UK jurisdiction's GloBE Income. The UK ETR calculation includes this €3M.

## Reverse Hybrid Entity Treatment *(Article 3.5.2)*

### The Rule

For a **Reverse Hybrid Entity**, the GloBE Income and Covered Taxes **remain at the entity level**.

### When This Applies

The entity is:
1. Fiscally transparent in its jurisdiction of creation, BUT
2. Treated as opaque (non-transparent) by the owners' jurisdiction

### Common Examples

| Structure | Why It's a Reverse Hybrid |
|-----------|--------------------------|
| US LLC owned by German GmbH | US: transparent; Germany: treats LLC as corporation |
| Luxembourg SCSp owned by French SA | Luxembourg: transparent; France: may treat as opaque |
| UK LP owned by Japanese KK | UK: transparent; Japan: treats LP as corporation |

### Worked Example: Reverse Hybrid Entity

**Structure:**
```
SG Japan KK (Japan)
    │
    └── 100% ownership
            │
            ▼
    SG US LLC (Delaware)
    [Japan treats as opaque corporation]
```

**SG US LLC financials:**
- GloBE Income: €2,500,000
- US Covered Taxes: €0 (not taxed at entity level)

**Treatment under Article 3.5.2:**

| Entity | GloBE Income | Covered Taxes | Jurisdiction |
|--------|--------------|---------------|--------------|
| SG US LLC | €2,500,000 | €0 | **USA** |
| SG Japan KK | €0 (from LLC) | €0 (from LLC) | Japan |

**Effect:** The LLC's income stays in the US jurisdiction for ETR purposes. US ETR = €0 ÷ €2,500,000 = **0%**. Top-Up Tax will arise.

### The Reverse Hybrid Problem

Reverse hybrids can create **stateless income** for GloBE purposes:

| Jurisdiction | Tax Treatment | GloBE Treatment |
|--------------|---------------|-----------------|
| Entity location (e.g., US) | Not taxed (transparent) | Income attributed here |
| Owner location (e.g., Japan) | Not taxed (waits for distribution) | No income attributed |

**Result:** Income sits in a jurisdiction with 0% ETR, triggering Top-Up Tax.

The reverse hybrid problem illustrates why the GloBE framework cannot simply defer to domestic tax classifications. A US LLC owned by a Japanese parent is the paradigmatic example: the US views the LLC as transparent and doesn't tax its income; Japan views the LLC as a corporation and doesn't tax its income until distribution. Without special rules, this income would be "stateless" for GloBE purposes—not included in any jurisdiction's ETR calculation. Article 3.5.2 resolves this by keeping income at the entity level when the owner's jurisdiction treats it as opaque. The consequence—often a 0% ETR in the entity's jurisdiction—is intentional. The framework is designed to surface undertaxation, and reverse hybrids that produce double non-taxation should indeed trigger Top-Up Tax. Groups using these structures must either accept the Top-Up Tax, restructure to eliminate the hybrid mismatch, or ensure the entity's jurisdiction imposes sufficient tax (perhaps through a QDMTT).

## UPE as a Flow-Through Entity *(Article 3.5.3)*

### Special Rules

When the **UPE itself** is a flow-through entity (e.g., a US LLC or UK LLP):

| Scenario | Treatment |
|----------|-----------|
| UPE is tax transparent to owners | GloBE Income may flow up to natural persons or non-MNE owners |
| UPE is reverse hybrid | GloBE Income stays at UPE level |

### Reduction for Non-CE Owners

If the UPE is tax transparent and some owners are **not Constituent Entities** (e.g., individuals, excluded entities), the GloBE Income is reduced by their share *(Article 3.5.3)*.

### Worked Example: UPE as Flow-Through

**Structure:**
```
Individual A (50%)  ←─┐
                      │
PE Fund LP (UK)  ─────┼──── SG Operating Ltd (UK)
[UK LLP - transparent]│
                      │
Individual B (50%)  ←─┘
```

**PE Fund LP financials:**
- GloBE Income from SG Operating: €10,000,000

**Allocation:**

| Owner | Share | CE? | GloBE Income Allocated |
|-------|-------|-----|----------------------|
| Individual A | 50% | No | €0 (excluded) |
| Individual B | 50% | No | €0 (excluded) |
| **PE Fund LP** | — | Yes (UPE) | €0 |

**Effect:** The 100% owned by individuals reduces the GloBE Income to €0. No Top-Up Tax arises because income flows to non-CE owners.

The UPE-as-flow-through rules address a conceptual challenge: how can there be a Constituent Entity that owns the group when that entity's income flows through to individual owners who are not themselves CEs? The framework resolves this by acknowledging that GloBE applies to MNE Groups, not to individuals or non-CE entities. Where a partnership or LLC sits atop a multinational structure and its owners are natural persons, the income attributable to those persons exits the GloBE calculation entirely—there is no Constituent Entity to which it can be allocated. This result respects the principle that Pillar Two targets undertaxation of corporate profits, not individual income. It also prevents the absurdity of taxing individuals under a corporate minimum tax framework. However, groups should not assume that flow-through status at the top of the structure eliminates all GloBE exposure: the reduction applies only to the extent of non-CE ownership, and any corporate owners down the chain remain subject to the full framework.

## Allocation in Ownership Chains

### Multiple Flow-Through Entities

When flow-through entities are stacked, determine transparency at each level:

```
SG Holdings Ltd (UK)
    │
    └── SG Luxembourg SCSp
            │ (Tax transparent to SG Holdings)
            │
            └── SG US LLC
                    (Tax transparent to SCSp)
```

**Analysis:**
1. SG US LLC: Transparent in US, transparent to Luxembourg SCSp owner
2. SG Luxembourg SCSp: Transparent in Luxembourg, transparent to UK owner
3. **Result:** Income flows up to SG Holdings Ltd (UK)

### Chain Resolution Rule

The **June 2024 Administrative Guidance** clarifies:

> *When a flow-through entity is owned by another flow-through entity, classification is determined by reference to the next owner up the chain who is NOT a flow-through entity.*

## Stratos Worked Example: PE and Flow-Through

### Structure

```
Stratos Group plc (UK)
    │
    ├── SG France SAS (France)
    │       └── Belgium PE
    │
    ├── SG Holdings Ltd (UK)
    │       └── SG US LLC (Delaware) [disregarded]
    │
    └── SG Japan KK (Japan)
            └── SG Singapore LP [reverse hybrid]
```

### Analysis: Belgium PE

**SG France SAS — Belgium PE Allocation**

| Item | France | Belgium PE |
|------|--------|------------|
| Total entity income | €8,500,000 | — |
| Less: PE attributable income | — | €1,200,000 |
| **Remaining main entity** | €7,300,000 | — |
| **PE GloBE Income** | — | €1,200,000 |

### Analysis: SG US LLC (Tax Transparent)

**SG US LLC — Flow-Through to UK**

| Item | USA | UK (SG Holdings) |
|------|-----|------------------|
| LLC GloBE Income | €2,800,000 | — |
| Less: Allocated to UK owner | (€2,800,000) | + €2,800,000 |
| **Remaining at LLC** | €0 | — |
| **Added to UK GloBE Income** | — | €2,800,000 |

**UK Covered Taxes on LLC income:**
- UK taxes SG Holdings on worldwide income including LLC
- UK corporate tax at 25% on €2,800,000 = €700,000
- This €700,000 goes into UK Covered Taxes

### Analysis: SG Singapore LP (Reverse Hybrid)

**SG Singapore LP — Stays in Singapore**

| Item | Singapore | Japan (SG Japan KK) |
|------|-----------|---------------------|
| LP GloBE Income | €1,500,000 | — |
| Singapore taxes (17% assumed) | €255,000 | — |
| Allocated to Japan? | No | — |
| **Singapore ETR** | 17% | — |

**Note:** Singapore LP remains a Singapore CE. Japan doesn't recognise the income until distribution.

### Summary Table

| Entity/PE | Jurisdiction | GloBE Income | Covered Taxes | ETR |
|-----------|--------------|--------------|---------------|-----|
| Stratos Group plc | UK | €45,600,000 | €10,944,000 | 24.0% |
| SG Holdings Ltd | UK | +€2,800,000* | +€700,000* | (combined) |
| SG France SAS | France | €7,300,000 | €1,825,000 | 25.0% |
| Belgium PE | Belgium | €1,200,000 | €300,000 | 25.0% |
| SG US LLC | USA | €0 | €0 | N/A |
| SG Japan KK | Japan | €22,300,000 | €6,690,000 | 30.0% |
| SG Singapore LP | Singapore | €1,500,000 | €255,000 | 17.0% |

*LLC income flows to UK; taxes paid by UK on that income.

## Documentation Requirements

### For PE Allocations

| Document | Purpose |
|----------|---------|
| PE separate accounts (if available) | Primary source for PE income |
| Transfer pricing documentation | Supports arm's length attribution |
| Tax treaty analysis | Confirms PE existence and attribution rules |
| Domestic law analysis | For domestic law PEs |
| Loss tracking schedule | For Article 3.4.5 recapture |

### For Flow-Through Entities

| Document | Purpose |
|----------|---------|
| Entity classification analysis | Transparent vs reverse hybrid |
| Ownership structure chart | Identifies CE vs non-CE owners |
| Tax treatment in each jurisdiction | Confirms classification |
| Allocation calculations | Shows income flow-through |

## 8. Common Pitfalls

### Pitfall 1: Double-Counting PE Income

**Error:** Including PE income in both PE and main entity GloBE Income.

**Correct:** Exclude PE income from main entity under Article 3.4.4.

### Pitfall 2: Ignoring PE Loss Recapture

**Error:** Pushing PE loss to main entity without tracking future recapture.

**Correct:** Maintain schedule to recapture future PE profits to main entity.

### Pitfall 3: Misclassifying Flow-Through Entities

**Error:** Assuming all LLCs/LPs are tax transparent.

**Correct:** Check treatment in **both** entity jurisdiction AND owner jurisdiction.

### Pitfall 4: Forgetting Reverse Hybrid Consequences

**Error:** Assuming income flows to owners as for tax transparent entities.

**Correct:** Reverse hybrid income stays at entity level—often creates low ETR jurisdiction.

### Pitfall 5: Missing Non-CE Owner Reduction

**Error:** Including full GloBE Income when UPE is flow-through with non-CE owners.

**Correct:** Reduce GloBE Income by share attributable to non-CE owners.

The PE and flow-through allocation rules reveal the GloBE framework's fundamental commitment to jurisdictional accuracy over simplicity. The drafters could have imposed uniform classifications—treating all PEs as part of their main entities, or mandating that all flow-throughs are transparent. Instead, they chose to work with the rich diversity of existing domestic and treaty classifications, creating a set of allocation rules that respect those classifications while ensuring comprehensive coverage. The result is a technically demanding area of compliance that requires groups to understand not just their own legal structures, but how each jurisdiction in their chain views every entity. For groups with complex PE networks or multi-tier flow-through structures, building and maintaining accurate classification databases is essential. The June 2024 Administrative Guidance on chain resolution provides welcome clarification, but the fundamental challenge remains: the GloBE calculation is only as accurate as the underlying entity classification analysis.

## Key References

**OECD GloBE Model Rules:**
- Article 3.4 — Permanent Establishment Income Allocation
- Article 3.5 — Flow-Through Entity Treatment
- Article 10.1 — PE Definition
- Article 10.2 — Flow-Through Entity Definitions

**Administrative Guidance:**
- June 2024 Guidance — Chain Resolution for Stacked Flow-Throughs
