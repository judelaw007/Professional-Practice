# Chapter 2.3: Ordering Rules and Interaction

## Learning Objective

After completing this chapter, you will be able to apply the correct sequence of GloBE rules, determine which rule collects Top-Up Tax in any given scenario, and coordinate multiple rules to avoid double taxation.

---

## The Three-Layer Rule Order

The GloBE framework operates through a strict priority sequence. Understanding this order is essential—applying rules out of sequence leads to incorrect calculations.

### Priority Sequence

| Priority | Rule | Where Tax Is Collected | Article Reference |
|----------|------|----------------------|-------------------|
| **1st** | QDMTT | Low-taxed jurisdiction (source) | Article 5.2.3 |
| **2nd** | IIR | Parent entity jurisdiction | Article 2.1 |
| **3rd** | UTPR | Other group jurisdictions | Article 2.4–2.6 |

**Key principle:** Each rule only applies to the **residual** Top-Up Tax not collected by higher-priority rules.

---

## Master Flowchart: Which Rule Applies?

```
                        ┌─────────────────────────────┐
                        │ Top-Up Tax calculated for   │
                        │ Low-Taxed Jurisdiction      │
                        │ (Chapter 5 calculation)     │
                        └─────────────┬───────────────┘
                                      │
                                      ▼
                        ┌─────────────────────────────┐
                        │ Does the low-taxed          │
                        │ jurisdiction have a QDMTT?  │
                        └─────────────┬───────────────┘
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                         YES                      NO
                          │                       │
                          ▼                       │
              ┌───────────────────────┐           │
              │ QDMTT APPLIES FIRST   │           │
              │ Collected locally     │           │
              │ Reduces Top-Up Tax    │           │
              └───────────┬───────────┘           │
                          │                       │
                          ▼                       │
              ┌───────────────────────┐           │
              │ Is there residual     │           │
              │ Top-Up Tax remaining? │◄──────────┘
              └───────────┬───────────┘
                          │
                ┌─────────┴─────────┐
                │                   │
               YES                  NO
                │                   │
                ▼                   ▼
    ┌─────────────────────┐   ┌─────────────────┐
    │ Does UPE/IPE        │   │ NO FURTHER      │
    │ jurisdiction have   │   │ TAX DUE         │
    │ Qualified IIR?      │   │ (QDMTT covered) │
    └─────────┬───────────┘   └─────────────────┘
              │
      ┌───────┴───────┐
      │               │
     YES              NO
      │               │
      ▼               ▼
┌─────────────┐  ┌─────────────────────────┐
│ IIR APPLIES │  │ Does any group          │
│ Collected   │  │ jurisdiction have       │
│ at parent   │  │ Qualified UTPR?         │
│ level       │  └───────────┬─────────────┘
└──────┬──────┘              │
       │             ┌───────┴───────┐
       ▼             │               │
┌─────────────┐     YES              NO
│ Residual    │      │               │
│ after IIR?  │      ▼               ▼
└──────┬──────┘ ┌──────────────┐ ┌──────────────┐
       │        │ UTPR APPLIES │ │ NO MECHANISM │
       │        │ Backstop     │ │ TO COLLECT   │
       │        │ collection   │ │ (undertaxed) │
       │        └──────────────┘ └──────────────┘
       │
   ┌───┴───┐
   │       │
  YES      NO
   │       │
   ▼       ▼
┌──────┐ ┌──────────┐
│ UTPR │ │ COMPLETE │
│      │ │ (IIR     │
│      │ │ covered) │
└──────┘ └──────────┘
```

---

## Layer 1: QDMTT (First Priority)

### What Is QDMTT?

A **Qualified Domestic Minimum Top-Up Tax (QDMTT)** is a domestic law that imposes Top-Up Tax in the low-taxed jurisdiction itself, using GloBE-consistent rules.

### Why QDMTT Has Priority

QDMTT preserves the source jurisdiction's taxing right. Rather than allowing other jurisdictions to collect Top-Up Tax through IIR or UTPR, the low-taxed jurisdiction can collect it domestically.

### QDMTT Offset

When a jurisdiction has a Qualified QDMTT, the Top-Up Tax collected under the QDMTT **reduces** the amount subject to IIR and UTPR *(Article 5.2.3)*.

**Formula:**

```
Residual Top-Up Tax = Jurisdictional Top-Up Tax − QDMTT Paid
```

### Worked Example: QDMTT Offset

**Scenario:** SG Ireland Ltd has a jurisdictional Top-Up Tax of €800,000. Ireland has implemented a QDMTT.

| Item | Amount |
|------|--------|
| Ireland jurisdictional Top-Up Tax | €800,000 |
| Ireland QDMTT collected | €800,000 |
| **Residual for IIR/UTPR** | **€0** |

The QDMTT fully covers the Top-Up Tax. No IIR or UTPR applies to this jurisdiction.

---

## Layer 2: IIR (Second Priority)

### When IIR Applies

After QDMTT, the IIR applies to any **residual** Top-Up Tax. The IIR is collected at the parent entity level, using the top-down approach from Chapter 2.1.

### IIR Top-Down Cascade

| Step | Entity | Condition |
|------|--------|-----------|
| 1 | UPE | Applies IIR if UPE jurisdiction has Qualified IIR |
| 2 | IPE | Applies IIR only if UPE jurisdiction lacks Qualified IIR |
| 3 | POPE | Applies IIR separately (even if UPE applies IIR) for third-party ownership share |

### IIR Offset Mechanism

When multiple entities in the ownership chain apply the IIR (e.g., UPE and POPE both applying), the **IIR offset** prevents double taxation *(Article 2.3)*.

**Rule:** The higher-tier parent reduces its Allocable Share by the amount charged at the lower-tier entity.

### Worked Example: IIR After QDMTT

**Scenario:** SG Singapore Pte Ltd has a jurisdictional Top-Up Tax of €2,100,000. Singapore has no QDMTT. Stratos Group plc (UK UPE) owns 100%.

| Item | Amount |
|------|--------|
| Singapore jurisdictional Top-Up Tax | €2,100,000 |
| Singapore QDMTT | €0 (no QDMTT) |
| Residual for IIR | €2,100,000 |
| Stratos's Inclusion Ratio | 100% |
| **UK IIR liability** | **€2,100,000** |

The full Top-Up Tax is collected through UK IIR.

---

## Layer 3: UTPR (Backstop)

### When UTPR Applies

UTPR is the **backstop** mechanism. It only applies when:
1. There is residual Top-Up Tax after QDMTT, AND
2. The IIR does not fully collect the residual (e.g., no Qualified IIR at UPE/IPE level, or minority interests)

### UTPR Scenarios

| Scenario | Why UTPR Applies |
|----------|------------------|
| UPE jurisdiction has no Qualified IIR | IIR cannot apply at UPE; UTPR is backstop |
| Split ownership (minority interests) | IIR only collects parent's share; UTPR collects minority's share |
| Low-taxed UPE jurisdiction | UPE jurisdiction itself is undertaxed |

### Worked Example: UTPR as Backstop

**Scenario:** An MNE has a UPE in Country X (no Qualified IIR). Low-taxed subsidiary in Country Y has Top-Up Tax of €500,000. Country Y has no QDMTT.

| Item | Amount |
|------|--------|
| Country Y Top-Up Tax | €500,000 |
| QDMTT collected | €0 |
| IIR collected (no Qualified IIR at UPE) | €0 |
| **UTPR Top-Up Tax Amount** | **€500,000** |

The UTPR allocates €500,000 across jurisdictions with Qualified UTPR using the 50/50 employee/tangible asset formula (Chapter 2.2).

---

## Interaction Matrix: All Rules Combined

### Decision Matrix

| QDMTT in LTCE Jurisdiction? | Qualified IIR at UPE? | 100% Ownership? | Rules That Apply |
|----------------------------|----------------------|-----------------|------------------|
| Yes (full coverage) | Any | Any | QDMTT only |
| Yes (partial) | Yes | Yes | QDMTT + IIR |
| Yes (partial) | Yes | No | QDMTT + IIR + UTPR |
| No | Yes | Yes | IIR only |
| No | Yes | No | IIR + UTPR |
| No | No | Any | UTPR only |

### Calculation Sequence

When multiple rules apply, follow this calculation order:

1. **Calculate jurisdictional Top-Up Tax** (Part 5 methodology)
2. **Subtract QDMTT** (if applicable) → Residual A
3. **Calculate IIR Allocable Share** on Residual A → Amount collected under IIR
4. **Calculate UTPR** on any remaining amount → Amount allocated to UTPR jurisdictions

---

## Comprehensive Worked Example: Stratos Group

### Scenario Overview

Stratos Group has two low-taxed jurisdictions:

| Jurisdiction | Top-Up Tax | QDMTT Status | UPE Ownership |
|--------------|------------|--------------|---------------|
| Singapore | €2,100,000 | No QDMTT | 100% |
| Ireland | €800,000 | Qualified QDMTT | 100% |

UK (UPE jurisdiction) has a Qualified IIR.

### Step 1: Apply QDMTT (Layer 1)

**Singapore:**
- No QDMTT
- Residual: €2,100,000

**Ireland:**
- QDMTT: €800,000
- Residual: €800,000 − €800,000 = **€0**

### Step 2: Apply IIR (Layer 2)

**Singapore:**
- Residual from Layer 1: €2,100,000
- UK has Qualified IIR → IIR applies
- Stratos's Inclusion Ratio: 100%
- IIR collected: €2,100,000 × 100% = **€2,100,000**
- Residual: €0

**Ireland:**
- Residual from Layer 1: €0
- No IIR applies (fully covered by QDMTT)

### Step 3: Apply UTPR (Layer 3)

**Singapore:**
- Residual from Layer 2: €0
- No UTPR applies

**Ireland:**
- Residual from Layer 2: €0
- No UTPR applies

### Summary

| Jurisdiction | Top-Up Tax | QDMTT | IIR (UK) | UTPR | Total Collected |
|--------------|------------|-------|----------|------|-----------------|
| Singapore | €2,100,000 | €0 | €2,100,000 | €0 | €2,100,000 |
| Ireland | €800,000 | €800,000 | €0 | €0 | €800,000 |
| **Total** | **€2,900,000** | **€800,000** | **€2,100,000** | **€0** | **€2,900,000** |

All Top-Up Tax is collected. No undertaxation remains.

---

## Complex Scenario: Split Ownership with Multiple Rules

### Scenario

Stratos owns 70% of a subsidiary in Country Z. Country Z has no QDMTT. Top-Up Tax is €1,000,000.

| Item | Amount |
|------|--------|
| Country Z Top-Up Tax | €1,000,000 |
| QDMTT | €0 |
| Stratos's Inclusion Ratio | 70% |
| IIR collected (UK) | €1,000,000 × 70% = €700,000 |
| Residual for UTPR | €1,000,000 − €700,000 = **€300,000** |

The €300,000 attributable to the 30% minority is not collected under IIR and becomes subject to UTPR allocation.

### UTPR Allocation

The €300,000 is allocated across UTPR jurisdictions using the 50/50 formula. Assuming Stratos has operations in Germany, France, and the UK (all with Qualified UTPR):

| Jurisdiction | UTPR % | UTPR Allocated |
|--------------|--------|----------------|
| UK | 50% | €150,000 |
| Germany | 30% | €90,000 |
| France | 20% | €60,000 |
| **Total** | **100%** | **€300,000** |

### Combined Result

| Rule | Amount | Where Collected |
|------|--------|-----------------|
| QDMTT | €0 | — |
| IIR | €700,000 | UK (at Stratos Group plc) |
| UTPR | €300,000 | UK €150K, Germany €90K, France €60K |
| **Total** | **€1,000,000** | Multiple jurisdictions |

---

## Switch-Over Rule

### Purpose

The **Switch-Over Rule (SOR)** addresses situations where tax treaties may prevent IIR application.

### When SOR Applies

Some tax treaties require a jurisdiction to **exempt** income from foreign permanent establishments (PEs). This exemption could block the IIR from applying to low-taxed PE income.

The SOR allows the parent jurisdiction to **switch** from the exemption method to the **credit method** for PE income that is low-taxed.

### Practical Effect

| Without SOR | With SOR |
|-------------|----------|
| Treaty requires exemption of PE income | Switch to credit method for low-taxed PE income |
| IIR cannot apply to exempt income | IIR can apply; foreign tax credit given for PE taxes |

### When SOR Is Relevant

The SOR is most relevant when:
- The UPE jurisdiction uses exemption method for foreign PE income under treaties
- A PE is located in a low-taxed jurisdiction
- The UPE jurisdiction has implemented the SOR alongside its IIR

**Note:** Many jurisdictions implementing Pillar Two have adopted the SOR as part of their domestic IIR legislation to ensure comprehensive coverage.

---

## Coordination Mechanisms: Preventing Double Taxation

### Mechanism 1: QDMTT Offset

QDMTT reduces Top-Up Tax before IIR/UTPR apply *(Article 5.2.3)*.

### Mechanism 2: IIR Offset

When both UPE and POPE apply IIR, the UPE reduces its share by the POPE's charge *(Article 2.3)*.

### Mechanism 3: UTPR Residual Only

UTPR only applies to amounts **not** collected under QDMTT or IIR.

### Summary: No Double Taxation

| Coordination Point | Mechanism |
|-------------------|-----------|
| Between QDMTT and IIR | QDMTT reduces Top-Up Tax first |
| Between UPE IIR and POPE IIR | IIR offset (Article 2.3) |
| Between IIR and UTPR | UTPR applies to residual only |
| Between UTPR jurisdictions | Allocation formula divides once |

---

## Timing and Sequencing

### Calculation Sequence Dependencies

The rule order creates **sequencing dependencies** for calculations:

| Step | Must Wait For |
|------|---------------|
| QDMTT calculation | Jurisdictional Top-Up Tax (Part 5) |
| IIR calculation | QDMTT determination |
| UTPR calculation | IIR determination |

### Practical Implication

MNE groups cannot finalise IIR or UTPR calculations until they know:
1. Which jurisdictions have implemented QDMTT
2. The amount of QDMTT collected in each jurisdiction

This requires coordination with local tax teams in QDMTT jurisdictions before completing group-level calculations.

---

## Common Pitfalls

### Pitfall 1: Applying IIR Before Considering QDMTT

Always check if the low-taxed jurisdiction has a QDMTT first. QDMTT reduces the amount subject to IIR.

### Pitfall 2: Double-Counting Top-Up Tax

If both QDMTT and IIR apply, don't add them—the IIR only applies to the **residual** after QDMTT.

### Pitfall 3: Forgetting the IIR Offset

When both UPE and POPE apply IIR, apply the offset. Without it, you'll overstate the UPE's liability.

### Pitfall 4: Ignoring UTPR for Minority Interests

Even when IIR applies, split ownership means UTPR may still apply for the minority share not captured by IIR.

### Pitfall 5: Assuming UTPR Never Applies

Many assume UTPR is rare. While less common than IIR, UTPR applies in all split-ownership scenarios where minority interests exist.

---

## Key References

**OECD GloBE Model Rules:**
- Article 2.1 — IIR application (UPE, IPE, POPE)
- Article 2.3 — IIR offset mechanism
- Article 2.4–2.6 — UTPR application and allocation
- Article 5.2.3 — QDMTT offset against Top-Up Tax

**OECD Administrative Guidance:**
- QDMTT Safe Harbour — Deems Top-Up Tax nil where Qualified QDMTT applies
- Transitional UTPR Safe Harbour — UPE jurisdictions with ≥20% rate exempt through 2025/2026

---

## Tools

The ordering rules determine how Top-Up Tax calculated in earlier Parts is distributed across collection mechanisms:

| Tool | How This Chapter Connects |
|------|---------------------------|
| **GIR-001 GloBE Calculator** | Step 3 calculates jurisdictional Top-Up Tax. Apply the ordering rules from this chapter to determine how that amount is split between QDMTT, IIR, and UTPR. |
| **GIR-004 GIR Practice Form** | Sections 2 (IIR) and 3 (UTPR) of the GIR require separate disclosure of amounts collected under each rule. The ordering analysis determines these amounts. |

---

## Summary

Applying the ordering rules requires:

1. **Start with QDMTT** — Check if the low-taxed jurisdiction has a Qualified QDMTT; if so, reduce Top-Up Tax accordingly
2. **Apply IIR next** — Determine if UPE/IPE jurisdiction has Qualified IIR; calculate Allocable Share on residual
3. **Apply UTPR last** — If residual remains after IIR (e.g., minority interests, no Qualified IIR), allocate via UTPR
4. **Coordinate** — Use offset mechanisms (QDMTT offset, IIR offset) to prevent double taxation
5. **Sequence calculations** — Wait for QDMTT determinations before finalising IIR/UTPR

---

## Next Step

You now understand how the GloBE charging mechanisms interact:
- How IIR collects Top-Up Tax at the parent level (Chapter 2.1)
- How UTPR acts as a backstop (Chapter 2.2)
- How the rules interact in the correct order (this chapter)

Proceed to **Chapter 2.4: Top-Up Tax Allocation Calculations** to learn detailed computation methods for allocating Top-Up Tax across entities and jurisdictions.
