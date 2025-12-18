# Chapter 2.3: Ordering Rules and Interaction

## Learning Objective

After completing this chapter, you will be able to apply the correct sequence of GloBE rules, determine which rule collects Top-Up Tax in any given scenario, and coordinate multiple rules to avoid double taxation.

## Introduction

The GloBE framework's three charging mechanisms—QDMTT, IIR, and UTPR—do not operate in isolation. Understanding their interaction is as important as understanding each rule individually, because applying them in the wrong order or failing to coordinate offsets leads to either under-collection or double taxation. The ordering rules represent a carefully negotiated compromise among the 140+ jurisdictions in the Inclusive Framework, balancing source countries' desire to retain taxing rights, parent countries' claims to include subsidiary income, and the need for a backstop that ensures no low-taxed profit escapes entirely. This chapter maps the complete interaction framework.

## 1. The Three-Layer Rule Order

The GloBE framework operates through a strict priority sequence. Understanding this order is essential—applying rules out of sequence leads to incorrect calculations.

### 1.1 Priority Sequence

| Priority | Rule | Where Tax Is Collected | Article Reference |
|----------|------|----------------------|-------------------|
| **1st** | QDMTT | Low-taxed jurisdiction (source) | Article 5.2.3 |
| **2nd** | IIR | Parent entity jurisdiction | Article 2.1 |
| **3rd** | UTPR | Other group jurisdictions | Article 2.4–2.6 |

**Key principle:** Each rule only applies to the **residual** Top-Up Tax not collected by higher-priority rules.

The priority sequence reflects both economic logic and political reality. QDMTT's first position honours the principle that source jurisdictions should have the first opportunity to tax income arising within their borders—even if that income was previously undertaxed due to domestic incentive regimes. This design also creates a powerful incentive for low-tax jurisdictions to implement their own QDMTT: by doing so, they capture the Top-Up Tax revenue rather than ceding it to parent jurisdictions via IIR or to other jurisdictions via UTPR. The IIR's second position reflects the parent's control over its subsidiaries, while UTPR's backstop role ensures comprehensive coverage even when the first two rules cannot fully collect.

## 2. Master Flowchart: Which Rule Applies?

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

## 3. Layer 1: QDMTT (First Priority)

### 3.1 What Is QDMTT?

A **Qualified Domestic Minimum Top-Up Tax (QDMTT)** is a domestic law that imposes Top-Up Tax in the low-taxed jurisdiction itself, using GloBE-consistent rules.

### 3.2 Why QDMTT Has Priority

QDMTT preserves the source jurisdiction's taxing right. Rather than allowing other jurisdictions to collect Top-Up Tax through IIR or UTPR, the low-taxed jurisdiction can collect it domestically.

### 3.3 QDMTT Offset

When a jurisdiction has a Qualified QDMTT, the Top-Up Tax collected under the QDMTT **reduces** the amount subject to IIR and UTPR *(Article 5.2.3)*.

**Formula:**

```
Residual Top-Up Tax = Jurisdictional Top-Up Tax − QDMTT Paid
```

### 3.4 Worked Example: QDMTT Offset

**Scenario:** SG Ireland Ltd has a jurisdictional Top-Up Tax of €800,000. Ireland has implemented a QDMTT.

| Item | Amount |
|------|--------|
| Ireland jurisdictional Top-Up Tax | €800,000 |
| Ireland QDMTT collected | €800,000 |
| **Residual for IIR/UTPR** | **€0** |

The QDMTT fully covers the Top-Up Tax. No IIR or UTPR applies to this jurisdiction.

QDMTT represents a strategic response by low-tax jurisdictions to the Pillar Two framework. Rather than lose the undertaxed profits to Top-Up Tax collected elsewhere, a jurisdiction can implement a QDMTT that brings its effective rate up to 15% and keeps the revenue domestically. Ireland's adoption of a QDMTT, for instance, means that the Top-Up Tax on Irish entities' previously undertaxed profits flows to the Irish exchequer rather than to parent jurisdictions like the UK or Netherlands. From an MNE perspective, the total tax paid is the same regardless of whether it flows through QDMTT, IIR, or UTPR—but the administrative pathway and the recipient jurisdiction differ significantly.

## 4. Layer 2: IIR (Second Priority)

### 4.1 When IIR Applies

After QDMTT, the IIR applies to any **residual** Top-Up Tax. The IIR is collected at the parent entity level, using the top-down approach from Chapter 2.1.

### 4.2 IIR Top-Down Cascade

| Step | Entity | Condition |
|------|--------|-----------|
| 1 | UPE | Applies IIR if UPE jurisdiction has Qualified IIR |
| 2 | IPE | Applies IIR only if UPE jurisdiction lacks Qualified IIR |
| 3 | POPE | Applies IIR separately (even if UPE applies IIR) for third-party ownership share |

### 4.3 IIR Offset Mechanism

When multiple entities in the ownership chain apply the IIR (e.g., UPE and POPE both applying), the **IIR offset** prevents double taxation *(Article 2.3)*.

**Rule:** The higher-tier parent reduces its Allocable Share by the amount charged at the lower-tier entity.

### 4.4 Worked Example: IIR After QDMTT

**Scenario:** SG Singapore Pte Ltd has a jurisdictional Top-Up Tax of €2,100,000. Singapore has no QDMTT. Stratos Group plc (UK UPE) owns 100%.

| Item | Amount |
|------|--------|
| Singapore jurisdictional Top-Up Tax | €2,100,000 |
| Singapore QDMTT | €0 (no QDMTT) |
| Residual for IIR | €2,100,000 |
| Stratos's Inclusion Ratio | 100% |
| **UK IIR liability** | **€2,100,000** |

The full Top-Up Tax is collected through UK IIR.

## 5. Layer 3: UTPR (Backstop)

### 5.1 When UTPR Applies

UTPR is the **backstop** mechanism. It only applies when:
1. There is residual Top-Up Tax after QDMTT, AND
2. The IIR does not fully collect the residual (e.g., no Qualified IIR at UPE/IPE level, or minority interests)

### 5.2 UTPR Scenarios

| Scenario | Why UTPR Applies |
|----------|------------------|
| UPE jurisdiction has no Qualified IIR | IIR cannot apply at UPE; UTPR is backstop |
| Split ownership (minority interests) | IIR only collects parent's share; UTPR collects minority's share |
| Low-taxed UPE jurisdiction | UPE jurisdiction itself is undertaxed |

### 5.3 Worked Example: UTPR as Backstop

**Scenario:** An MNE has a UPE in Country X (no Qualified IIR). Low-taxed subsidiary in Country Y has Top-Up Tax of €500,000. Country Y has no QDMTT.

| Item | Amount |
|------|--------|
| Country Y Top-Up Tax | €500,000 |
| QDMTT collected | €0 |
| IIR collected (no Qualified IIR at UPE) | €0 |
| **UTPR Top-Up Tax Amount** | **€500,000** |

The UTPR allocates €500,000 across jurisdictions with Qualified UTPR using the 50/50 employee/tangible asset formula (Chapter 2.2).

## 6. Interaction Matrix: All Rules Combined

### 6.1 Decision Matrix

| QDMTT in LTCE Jurisdiction? | Qualified IIR at UPE? | 100% Ownership? | Rules That Apply |
|----------------------------|----------------------|-----------------|------------------|
| Yes (full coverage) | Any | Any | QDMTT only |
| Yes (partial) | Yes | Yes | QDMTT + IIR |
| Yes (partial) | Yes | No | QDMTT + IIR + UTPR |
| No | Yes | Yes | IIR only |
| No | Yes | No | IIR + UTPR |
| No | No | Any | UTPR only |

### 6.2 Calculation Sequence

When multiple rules apply, follow this calculation order:

1. **Calculate jurisdictional Top-Up Tax** (Part 5 methodology)
2. **Subtract QDMTT** (if applicable) → Residual A
3. **Calculate IIR Allocable Share** on Residual A → Amount collected under IIR
4. **Calculate UTPR** on any remaining amount → Amount allocated to UTPR jurisdictions

## 7. Comprehensive Worked Example: Stratos Group

### 7.1 Scenario Overview

Stratos Group has two low-taxed jurisdictions:

| Jurisdiction | Top-Up Tax | QDMTT Status | UPE Ownership |
|--------------|------------|--------------|---------------|
| Singapore | €2,100,000 | No QDMTT | 100% |
| Ireland | €800,000 | Qualified QDMTT | 100% |

UK (UPE jurisdiction) has a Qualified IIR.

### 7.2 Step 1: Apply QDMTT (Layer 1)

**Singapore:**
- No QDMTT
- Residual: €2,100,000

**Ireland:**
- QDMTT: €800,000
- Residual: €800,000 − €800,000 = **€0**

### 7.3 Step 2: Apply IIR (Layer 2)

**Singapore:**
- Residual from Layer 1: €2,100,000
- UK has Qualified IIR → IIR applies
- Stratos's Inclusion Ratio: 100%
- IIR collected: €2,100,000 × 100% = **€2,100,000**
- Residual: €0

**Ireland:**
- Residual from Layer 1: €0
- No IIR applies (fully covered by QDMTT)

### 7.4 Step 3: Apply UTPR (Layer 3)

**Singapore:**
- Residual from Layer 2: €0
- No UTPR applies

**Ireland:**
- Residual from Layer 2: €0
- No UTPR applies

### 7.5 Summary

| Jurisdiction | Top-Up Tax | QDMTT | IIR (UK) | UTPR | Total Collected |
|--------------|------------|-------|----------|------|-----------------|
| Singapore | €2,100,000 | €0 | €2,100,000 | €0 | €2,100,000 |
| Ireland | €800,000 | €800,000 | €0 | €0 | €800,000 |
| **Total** | **€2,900,000** | **€800,000** | **€2,100,000** | **€0** | **€2,900,000** |

All Top-Up Tax is collected. No undertaxation remains.

## 8. Complex Scenario: Split Ownership with Multiple Rules

### 8.1 Scenario

Stratos owns 70% of a subsidiary in Country Z. Country Z has no QDMTT. Top-Up Tax is €1,000,000.

| Item | Amount |
|------|--------|
| Country Z Top-Up Tax | €1,000,000 |
| QDMTT | €0 |
| Stratos's Inclusion Ratio | 70% |
| IIR collected (UK) | €1,000,000 × 70% = €700,000 |
| Residual for UTPR | €1,000,000 − €700,000 = **€300,000** |

The €300,000 attributable to the 30% minority is not collected under IIR and becomes subject to UTPR allocation.

### 8.2 UTPR Allocation

The €300,000 is allocated across UTPR jurisdictions using the 50/50 formula. Assuming Stratos has operations in Germany, France, and the UK (all with Qualified UTPR):

| Jurisdiction | UTPR % | UTPR Allocated |
|--------------|--------|----------------|
| UK | 50% | €150,000 |
| Germany | 30% | €90,000 |
| France | 20% | €60,000 |
| **Total** | **100%** | **€300,000** |

### 8.3 Combined Result

| Rule | Amount | Where Collected |
|------|--------|-----------------|
| QDMTT | €0 | — |
| IIR | €700,000 | UK (at Stratos Group plc) |
| UTPR | €300,000 | UK €150K, Germany €90K, France €60K |
| **Total** | **€1,000,000** | Multiple jurisdictions |

## 9. Switch-Over Rule

### 9.1 Purpose

The **Switch-Over Rule (SOR)** addresses situations where tax treaties may prevent IIR application.

### 9.2 When SOR Applies

Some tax treaties require a jurisdiction to **exempt** income from foreign permanent establishments (PEs). This exemption could block the IIR from applying to low-taxed PE income.

The SOR allows the parent jurisdiction to **switch** from the exemption method to the **credit method** for PE income that is low-taxed.

### 9.3 Practical Effect

| Without SOR | With SOR |
|-------------|----------|
| Treaty requires exemption of PE income | Switch to credit method for low-taxed PE income |
| IIR cannot apply to exempt income | IIR can apply; foreign tax credit given for PE taxes |

### 9.4 When SOR Is Relevant

The SOR is most relevant when:
- The UPE jurisdiction uses exemption method for foreign PE income under treaties
- A PE is located in a low-taxed jurisdiction
- The UPE jurisdiction has implemented the SOR alongside its IIR

**Note:** Many jurisdictions implementing Pillar Two have adopted the SOR as part of their domestic IIR legislation to ensure comprehensive coverage.

The Switch-Over Rule addresses a technical conflict between tax treaties and Pillar Two's objectives. Many older tax treaties commit the residence country to exempt foreign PE income, preventing double taxation through the exemption method rather than the credit method. Without the SOR, these treaty obligations would block the IIR from applying to low-taxed PE income—creating a gap in coverage. The SOR effectively overrides the treaty's exemption requirement in Pillar Two contexts, switching to credit relief instead. This allows the residence jurisdiction to include the PE income and apply IIR, while still crediting any foreign tax actually paid. The SOR thus harmonises treaty obligations with minimum tax objectives, though its application requires careful attention to the specific treaties in question.

## 10. Coordination Mechanisms: Preventing Double Taxation

### 10.1 Mechanism 1: QDMTT Offset

QDMTT reduces Top-Up Tax before IIR/UTPR apply *(Article 5.2.3)*.

### 10.2 Mechanism 2: IIR Offset

When both UPE and POPE apply IIR, the UPE reduces its share by the POPE's charge *(Article 2.3)*.

### 10.3 Mechanism 3: UTPR Residual Only

UTPR only applies to amounts **not** collected under QDMTT or IIR.

### 10.4 Summary: No Double Taxation

| Coordination Point | Mechanism |
|-------------------|-----------|
| Between QDMTT and IIR | QDMTT reduces Top-Up Tax first |
| Between UPE IIR and POPE IIR | IIR offset (Article 2.3) |
| Between IIR and UTPR | UTPR applies to residual only |
| Between UTPR jurisdictions | Allocation formula divides once |

## 11. Timing and Sequencing

### 11.1 Calculation Sequence Dependencies

The rule order creates **sequencing dependencies** for calculations:

| Step | Must Wait For |
|------|---------------|
| QDMTT calculation | Jurisdictional Top-Up Tax (Part 5) |
| IIR calculation | QDMTT determination |
| UTPR calculation | IIR determination |

### 11.2 Practical Implication

MNE groups cannot finalise IIR or UTPR calculations until they know:
1. Which jurisdictions have implemented QDMTT
2. The amount of QDMTT collected in each jurisdiction

This requires coordination with local tax teams in QDMTT jurisdictions before completing group-level calculations.

## 12. Common Pitfalls

### 12.1 Pitfall 1: Applying IIR Before Considering QDMTT

Always check if the low-taxed jurisdiction has a QDMTT first. QDMTT reduces the amount subject to IIR.

### 12.2 Pitfall 2: Double-Counting Top-Up Tax

If both QDMTT and IIR apply, don't add them—the IIR only applies to the **residual** after QDMTT.

### 12.3 Pitfall 3: Forgetting the IIR Offset

When both UPE and POPE apply IIR, apply the offset. Without it, you'll overstate the UPE's liability.

### 12.4 Pitfall 4: Ignoring UTPR for Minority Interests

Even when IIR applies, split ownership means UTPR may still apply for the minority share not captured by IIR.

### 12.5 Pitfall 5: Assuming UTPR Never Applies

Many assume UTPR is rare. While less common than IIR, UTPR applies in all split-ownership scenarios where minority interests exist.

The ordering rules transform what could be a chaotic multi-jurisdictional grab for taxing rights into an orderly, predictable system. Each layer builds on the previous: QDMTT satisfies the source jurisdiction's claim, IIR satisfies the parent jurisdiction's claim on the residual, and UTPR catches anything remaining. The coordination mechanisms ensure that no single euro of low-taxed profit bears Top-Up Tax twice. This elegance comes at the cost of complexity—calculating the correct amounts requires knowing which jurisdictions have implemented which rules, the ownership percentages at each level, and the sequencing of multiple offset calculations. But the alternative—uncoordinated competing claims—would be far worse for both tax authorities and MNE groups.
