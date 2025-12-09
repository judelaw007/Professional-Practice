# Chapter 2.1: Income Inclusion Rule Mechanics

## Learning Objective

After completing this chapter, you will be able to determine which entity in an MNE group is liable to apply the Income Inclusion Rule and calculate its Allocable Share of Top-Up Tax.

---

## How the IIR Works

The Income Inclusion Rule (IIR) is the **primary charging mechanism** under GloBE. It requires a parent entity to include its share of Top-Up Tax arising from low-taxed constituent entities in its own tax liability.

The IIR follows a **top-down approach**: the Ultimate Parent Entity (UPE) has first priority to apply the rule. If the UPE's jurisdiction does not have a Qualified IIR, the obligation cascades down to the next parent entity in the ownership chain.

---

## Step 1: Identify the Entity That Must Apply the IIR

### Primary Rule: UPE Applies the IIR

If the UPE's jurisdiction has implemented a **Qualified IIR**, the UPE is required to apply the IIR with respect to any Low-Taxed Constituent Entity (LTCE) in which it holds an Ownership Interest *(Article 2.1.1)*.

**Key point:** The UPE must apply the IIR if it owns an interest in the LTCE "at any time during the Fiscal Year"—the holding period does not matter for determining liability.

### Secondary Rule: IPE Applies the IIR

If the UPE's jurisdiction does **not** have a Qualified IIR, the obligation flows down to the next **Intermediate Parent Entity (IPE)** whose jurisdiction has a Qualified IIR *(Article 2.1.2)*.

The IPE applies the IIR only with respect to LTCEs it directly or indirectly owns—not for entities outside its ownership chain.

### Exception: IPE Excluded When UPE Applies

If the UPE applies a Qualified IIR, lower-tier IPEs are **excluded** from applying the IIR *(Article 2.1.3)*. This prevents double taxation within the same ownership chain.

---

## Decision Flowchart: Which Entity Applies the IIR?

```
                    ┌─────────────────────────────────┐
                    │ Does the UPE's jurisdiction     │
                    │ have a Qualified IIR?           │
                    └───────────────┬─────────────────┘
                                    │
                        ┌───────────┴───────────┐
                        │                       │
                       YES                      NO
                        │                       │
                        ▼                       ▼
            ┌───────────────────┐   ┌─────────────────────────┐
            │ UPE applies IIR   │   │ Move down ownership     │
            │ (Article 2.1.1)   │   │ chain to first IPE with │
            └───────────────────┘   │ Qualified IIR           │
                        │           └───────────┬─────────────┘
                        │                       │
                        ▼                       ▼
            ┌───────────────────┐   ┌───────────────────────────┐
            │ IPEs below UPE    │   │ IPE applies IIR for its   │
            │ are EXCLUDED      │   │ sub-group (Article 2.1.2) │
            │ (Article 2.1.3)   │   └───────────────────────────┘
            └───────────────────┘
```

---

## Step 2: Calculate the Allocable Share of Top-Up Tax

Once you identify which entity must apply the IIR, calculate its **Allocable Share** of the Top-Up Tax.

### The Formula

**Allocable Share = Top-Up Tax of LTCE × Inclusion Ratio** *(Article 2.2.1)*

### Calculating the Inclusion Ratio

The **Inclusion Ratio** represents the parent entity's proportionate interest in the LTCE's GloBE Income *(Article 2.2.2)*.

**Inclusion Ratio = (GloBE Income of LTCE − Amount attributable to other owners) ÷ GloBE Income of LTCE**

| Scenario | Inclusion Ratio |
|----------|-----------------|
| 100% ownership | 100% |
| 80% ownership (20% minority) | Approximately 80%* |
| Split ownership through multiple parents | Pro-rata based on each parent's share |

*The exact calculation uses GloBE Income allocation, not just ownership percentage. In most cases with straightforward structures, these align closely.

### Worked Example: Simple Ownership

**Scenario:** Stratos Group plc (UK UPE) owns 100% of SG Singapore Pte Ltd, which has a Top-Up Tax of €500,000.

| Item | Value |
|------|-------|
| Top-Up Tax of LTCE | €500,000 |
| Stratos's Inclusion Ratio | 100% |
| **Stratos's Allocable Share** | **€500,000** |

Stratos Group plc pays €500,000 of UK Multinational Top-Up Tax.

---

## Step 3: Handle Split Ownership Structures

When an LTCE is owned through multiple ownership chains, each parent entity calculates its own Allocable Share based on its Inclusion Ratio.

### Worked Example: Split Ownership

**Scenario:** SG Ireland IP Ltd (LTCE) is owned:
- 70% by SG Netherlands BV (held by Stratos Group plc)
- 30% by an external investor

| Data | Value |
|------|-------|
| SG Ireland IP Ltd GloBE Income | €10,000,000 |
| SG Ireland IP Ltd Top-Up Tax | €200,000 |
| GloBE Income attributable to external investor | €3,000,000 |

**Stratos's Inclusion Ratio:**

```
Inclusion Ratio = (€10,000,000 − €3,000,000) ÷ €10,000,000
                = €7,000,000 ÷ €10,000,000
                = 70%
```

**Stratos's Allocable Share:**

```
Allocable Share = €200,000 × 70% = €140,000
```

Stratos Group plc pays €140,000 of Top-Up Tax. The remaining €60,000 is not charged under the IIR (it would be addressed by UTPR or QDMTT depending on the external investor's structure).

---

## Partially-Owned Parent Entities (POPEs)

A **Partially-Owned Parent Entity (POPE)** is a Constituent Entity that:
1. Owns an Ownership Interest in another CE, AND
2. Has **more than 20%** of its profits held by third parties *(Article 10.1)*

### Special Rule: POPEs Must Also Apply IIR

Even when a UPE applies the IIR, a POPE must **separately** apply the IIR with respect to LTCEs it owns *(Article 2.1.4)*. This is an exception to the normal top-down exclusion rule.

**Why?** POPEs have significant third-party ownership, so the UPE cannot fully capture the Top-Up Tax through its own Inclusion Ratio. The POPE must apply the IIR to ensure the third parties' share is taxed.

### Exception: Wholly-Owned POPE Chain

If one POPE is wholly owned by another POPE, only the higher-tier POPE applies the IIR *(Article 2.1.5)*. This prevents multiple POPEs in a chain from each applying the IIR on the same income.

---

## IIR Offset Mechanism

When multiple entities in the ownership chain apply the IIR (e.g., a UPE and a POPE both applying to the same LTCE), the **IIR offset** prevents double taxation *(Article 2.3)*.

### How the Offset Works

The higher-tier parent entity **reduces** its Allocable Share by the amount already charged at the lower-tier entity *(Article 2.3.1 and 2.3.2)*.

### Worked Example: IIR Offset with POPE

**Scenario:**
- Stratos Group plc (UK UPE) owns 60% of SG Holdings BV (Netherlands POPE)
- SG Holdings BV owns 100% of SG Singapore Tech Pte Ltd (LTCE)
- SG Holdings BV has 40% third-party ownership → qualifies as POPE
- Netherlands has a Qualified IIR
- SG Singapore Tech Top-Up Tax: €300,000

**Step 1: POPE applies IIR**

SG Holdings BV (POPE) applies IIR under Article 2.1.4:
- Inclusion Ratio: 100% (wholly owns the LTCE)
- Allocable Share: €300,000 × 100% = **€300,000**

SG Holdings BV pays €300,000 under Netherlands IIR.

**Step 2: UPE calculates Allocable Share before offset**

Stratos Group plc calculates its Allocable Share:
- Stratos owns 60% of SG Holdings BV
- Stratos's indirect Inclusion Ratio in LTCE: 60%
- Allocable Share before offset: €300,000 × 60% = €180,000

**Step 3: Apply IIR offset**

Stratos reduces its Allocable Share by the portion already taxed at POPE level:
- Amount charged at POPE: €300,000
- Stratos's share of POPE's tax: 60% × €300,000 = €180,000
- **Offset amount: €180,000**

**Stratos's final Allocable Share: €180,000 − €180,000 = €0**

The IIR offset eliminates Stratos's Top-Up Tax liability because the full amount has been charged at the POPE level. No double taxation occurs.

---

## Multi-Tier Ownership Chains

In complex structures with multiple IPEs, trace the ownership from the UPE down to each LTCE. Each parent in the chain may have different Inclusion Ratios depending on ownership percentages at each level.

### Worked Example: Multi-Tier Chain

**Stratos Group Structure:**

```
Stratos Group plc (UK UPE) — 100%
    │
    └── SG Holdings Ltd (UK IPE) — 100%
            │
            └── SG Netherlands BV (Netherlands IPE) — 100%
                    │
                    └── SG Singapore Pte Ltd (LTCE)
                        Top-Up Tax: €400,000
```

**Analysis:**

| Level | Entity | Direct Ownership | Cumulative Inclusion Ratio |
|-------|--------|------------------|---------------------------|
| 1 | Stratos Group plc | 100% of SG Holdings | 100% |
| 2 | SG Holdings Ltd | 100% of SG Netherlands | 100% |
| 3 | SG Netherlands BV | 100% of SG Singapore | 100% |

**Which entity applies IIR?**

- UK has a Qualified IIR
- Stratos Group plc (UPE) applies IIR *(Article 2.1.1)*
- SG Holdings Ltd and SG Netherlands BV are **excluded** *(Article 2.1.3)*

**Stratos's Allocable Share:**

€400,000 × 100% = **€400,000**

All Top-Up Tax is charged at the UK UPE level. Lower-tier IPEs have no IIR liability.

---

## Jurisdiction Qualified IIR Status

The IIR application depends on which jurisdictions have implemented a **Qualified IIR**. A jurisdiction's IIR qualifies if it is consistent with the GloBE Model Rules as determined through the OECD Inclusive Framework peer review process.

**Major jurisdictions with Qualified IIR (as at 2025):**

| Jurisdiction | Status |
|--------------|--------|
| United Kingdom | Qualified IIR effective 2024 |
| EU Member States | Qualified IIR effective 2024 |
| Australia | Qualified IIR effective 2024 |
| Japan | Qualified IIR effective 2024 |
| South Korea | Qualified IIR effective 2024 |
| Canada | Qualified IIR effective 2024 |

**Key point:** Check the OECD's published list of qualified jurisdictions, as this is updated periodically following peer reviews.

---

## Stratos Example: Complete IIR Application

**Stratos Group Structure (simplified for IIR analysis):**

```
Stratos Group plc (UK) — UPE
    │
    ├── SG Holdings Ltd (UK) — 100%
    │       │
    │       └── SG Singapore Pte Ltd (Singapore) — 100%
    │               ETR: 12.3%
    │               Top-Up Tax: €2,100,000
    │
    └── SG Ireland Ltd (Ireland) — 100%
            ETR: 14.1%
            Top-Up Tax: €800,000
```

**IIR Application:**

| LTCE | Top-Up Tax | UPE Applies IIR? | Allocable Share |
|------|------------|------------------|-----------------|
| SG Singapore Pte Ltd | €2,100,000 | Yes (UK has Qualified IIR) | €2,100,000 |
| SG Ireland Ltd | €800,000 | Yes (UK has Qualified IIR) | €800,000 |

**Total UK Multinational Top-Up Tax for Stratos:** €2,900,000

**Note:** If Ireland had implemented a QDMTT, the €800,000 would be collected in Ireland first, and Stratos's IIR liability for Ireland would be reduced to zero. See Chapter 5.4 for QDMTT interaction.

---

## Common Pitfalls

### Pitfall 1: Assuming IPE Always Applies IIR

If the UPE's jurisdiction has a Qualified IIR, lower-tier IPEs are excluded. Don't calculate separate IIR liability for each entity in the chain.

### Pitfall 2: Forgetting POPE Rules

POPEs must apply the IIR even when the UPE does. Always check whether any intermediate holding company has >20% third-party ownership.

### Pitfall 3: Incorrect Inclusion Ratio

The Inclusion Ratio is based on GloBE Income allocation, not just legal ownership percentage. For complex structures with minority interests at multiple levels, trace the income attribution carefully.

### Pitfall 4: Ignoring the IIR Offset

When both UPE and POPE apply IIR, the offset prevents double taxation. Failing to apply the offset overstates the UPE's liability.

---

## Key References

**OECD GloBE Model Rules:**
- Article 2.1.1 — UPE application of IIR
- Article 2.1.2 — IPE application of IIR
- Article 2.1.3 — Exclusion for IPE when UPE applies Qualified IIR
- Article 2.1.4 — POPE application of IIR
- Article 2.1.5 — Exclusion for wholly-owned POPE chain
- Article 2.2.1 — Allocable Share definition
- Article 2.2.2 — Inclusion Ratio calculation
- Article 2.3 — IIR Offset Mechanism

**OECD Commentary:**
- Paragraphs 1-30 (Chapter 2) — Detailed guidance on IIR application and allocation

---

## Tools

The IIR determines **which entity pays** the Top-Up Tax calculated in earlier steps. This chapter connects to:

| Tool | How This Chapter Connects |
|------|---------------------------|
| **GIR-001 GloBE Calculator** | Step 3 of GIR-001 calculates the jurisdictional Top-Up Tax amount. You then apply the IIR allocation from this chapter to determine which entity bears that tax. |
| **GIR-004 GIR Practice Form** | Section 2 of the GIR requires disclosure of IIR amounts by entity. The Allocable Share calculations from this chapter feed directly into the GIR. |

Use GIR-001 to calculate the Top-Up Tax amount, then apply the IIR mechanics from this chapter to allocate that amount to the correct parent entity.

---

## Summary

Applying the Income Inclusion Rule requires:

1. **Identify** which entity applies the IIR (UPE first, then IPE if no UPE IIR)
2. **Check** for POPEs that must separately apply the IIR
3. **Calculate** each parent's Inclusion Ratio based on GloBE Income attribution
4. **Compute** the Allocable Share (Top-Up Tax × Inclusion Ratio)
5. **Apply** the IIR offset where multiple entities in the chain apply IIR
6. **Document** the allocation for GIR reporting

---

## Next Step

Once you understand when the IIR applies and how to calculate the Allocable Share, proceed to **Chapter 2.2: Undertaxed Profits Rule Application** to learn how UTPR acts as a backstop when the IIR does not fully capture Top-Up Tax.
