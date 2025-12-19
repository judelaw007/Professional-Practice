# Chapter 4.6: Post-Filing Adjustments

## Learning Objective

After completing this chapter, you will be able to apply Article 4.6's asymmetric treatment rules for post-filing adjustments, distinguishing between increases (added to current year) and decreases (requiring prior-year recalculation) in Covered Taxes, and understand the immaterial exception, rate change rules, and recapture mechanisms.

## Introduction

Tax positions are rarely final when GloBE Information Returns are filed. Audits conclude years later; transfer pricing disputes are settled; uncertain positions are resolved; refunds are received. The GloBE framework must address how these post-filing developments affect ETR calculations that were completed using the best information available at the time. The solution—asymmetric treatment of increases versus decreases—reflects both practical and policy considerations. For increases in prior-year Covered Taxes, adding them to the current year is simple and works in the taxpayer's favour (improving current ETR). For decreases, however, simple current-year reduction would allow manipulation: groups could overstate Covered Taxes initially, then later obtain refunds while retaining the benefit of the original high ETR. Requiring recalculation for decreases prevents this gaming while ensuring accurate Top-Up Tax collection. The €1 million immaterial exception provides administrative relief for small adjustments that don't merit the compliance burden of prior-year recalculation.

## 1. The Asymmetric Treatment Principle

GloBE treats increases and decreases in prior-year Covered Taxes differently:

| Adjustment Type | Treatment | Rationale |
|-----------------|-----------|-----------|
| **Increase** in prior-year Covered Taxes | Add to **current year** Covered Taxes | Simplicity; no refund mechanism |
| **Decrease** in prior-year Covered Taxes | **Recalculate** prior year ETR and Top-Up Tax | Prevent avoidance via later reductions |

**Why asymmetric?** GloBE does not provide refunds of Top-Up Tax already paid. If a prior-year increase simply increased current-year Covered Taxes, but a decrease required recalculation, MNEs would face permanent overtaxation from increases but full correction for decreases. The asymmetry ensures fairness while maintaining anti-avoidance integrity.

## 2. Increases in Prior-Year Covered Taxes (Article 4.6.1)

### 2.1 The Rule

An increase to a Constituent Entity's Covered Taxes for a **prior fiscal year** is treated as an increase in Covered Taxes in the **current fiscal year**.

### 2.2 When This Applies

| Scenario | Example |
|----------|---------|
| Audit settlement | Tax authority assessment upheld |
| Amended return | Voluntary correction increasing tax |
| UTP resolution | Uncertain position resolved with payment |
| Self-assessment adjustment | Error discovered, additional tax paid |
| Transfer pricing adjustment | Unilateral TP increase by authority |

### 2.3 Practical Effect

```
FY 2024: Filed GIR with Covered Taxes €10,000,000
         ETR = 18% → No Top-Up Tax

FY 2026: Audit concludes; additional €500,000 tax for FY 2024

Treatment:
  Add €500,000 to FY 2026 Covered Taxes
  FY 2024 remains unchanged
  No amended GIR for FY 2024
```

### 2.4 No Refund Mechanism

If the FY 2024 ETR was below 15% and Top-Up Tax was paid, the additional €500,000 does NOT trigger a refund of that Top-Up Tax. The increase simply improves FY 2026's position.

**Consequence:** MNEs that paid Top-Up Tax in a prior year and later have increased Covered Taxes for that year receive no benefit. This creates an incentive to resolve tax positions promptly.

## 3. Decreases in Prior-Year Covered Taxes

### 3.1 The General Rule

A **decrease** in Covered Taxes for a prior fiscal year requires:
1. Recalculation of the prior year's ETR and Top-Up Tax
2. Any incremental Top-Up Tax is paid in the current year (as Additional Current Top-Up Tax)

### 3.2 The Recalculation Process

**Step 1:** Identify the fiscal year to which the decrease relates

**Step 2:** Recalculate that year's Adjusted Covered Taxes (with decrease applied)

**Step 3:** Recalculate that year's ETR

**Step 4:** Recalculate Top-Up Tax using Article 5.1-5.3

**Step 5:** Determine incremental Top-Up Tax (new vs. original)

**Step 6:** Include incremental amount as Additional Current Top-Up Tax per Article 5.2.3

### 3.3 Worked Example

```
FY 2024 (as originally filed):
  GloBE Income:           €50,000,000
  Adjusted Covered Taxes: €8,500,000
  ETR:                    17% (above 15%)
  Top-Up Tax:             €0

FY 2026: Tax refund of €1,200,000 relating to FY 2024

Recalculation of FY 2024:
  GloBE Income:           €50,000,000 (unchanged)
  Adjusted Covered Taxes: €8,500,000 - €1,200,000 = €7,300,000
  Revised ETR:            14.6% (below 15%)
  Top-Up Tax %:           15% - 14.6% = 0.4%
  Top-Up Tax:             0.4% × €50,000,000 = €200,000

Result:
  Additional Current Top-Up Tax in FY 2026: €200,000
  No amended GIR for FY 2024 required
```

## 4. Immaterial Decrease Exception

### 4.1 The €1 Million Threshold

If the aggregate decrease in Covered Taxes for a jurisdiction in a fiscal year is **less than €1 million**, the MNE may **elect** to:
- Treat the decrease as a reduction in current-year Covered Taxes
- Avoid prior-year recalculation

### 4.2 Election Requirements

| Requirement | Details |
|-------------|---------|
| Threshold | < €1,000,000 aggregate decrease for jurisdiction |
| Scope | Annual election |
| Application | Must be made consistently |

### 4.3 When to Use the Exception

**Use exception when:**
- Administrative burden of recalculation outweighs benefit
- Prior year already had ETR well above 15%
- Decrease is truly immaterial

**Do not use when:**
- Prior year ETR was close to 15% (decrease may trigger Top-Up Tax)
- Multiple small decreases may aggregate to material impact

### 4.4 Example

```
FY 2024 ETR: 22% (comfortably above 15%)
FY 2026: Refund of €400,000 relating to FY 2024

Option A: Recalculate FY 2024
  Revised ETR: Still above 15% → No Top-Up Tax
  Administrative burden: Moderate

Option B: Elect immaterial exception
  Reduce FY 2026 Covered Taxes by €400,000
  No recalculation required
  Administrative burden: Minimal

Decision: Use exception (same result, less effort)
```

## 5. Tax Rate Changes (Articles 4.6.2 and 4.6.3)

### 5.1 Rate Decreases (Article 4.6.2)

When a jurisdiction **reduces** its corporate tax rate below 15%:

**Issue:** Deferred tax liabilities created in prior years at the old rate will reverse at the new (lower) rate.

**Rule:** Recalculate the prior-year deferred tax expense based on the new rate.

**Example:**
```
Year 1: DTL created at 20% = €1,000,000 × 20% = €200,000
        Included in Year 1 Adjusted Covered Taxes

Year 2: Rate reduced to 10%
        DTL must be recomputed at 10%
        €1,000,000 × 10% = €100,000
        Difference: €200,000 - €100,000 = €100,000 reduction

Treatment:
  Recalculate Year 1 ETR with reduced deferred tax
  Any incremental Top-Up Tax → Additional Current Top-Up Tax in Year 2
```

### 5.2 Rate Increases (Article 4.6.3)

When a jurisdiction **increases** its corporate tax rate:

**General rule:** The increase is disregarded until the DTL unwinds and actual tax is paid.

**Treatment:** Additional tax paid when DTL reverses is treated as an increase in Covered Taxes for the **year the DTL was originally created**.

**Example:**
```
Year 1: DTL created at 20% = €1,000,000 × 20% = €200,000

Year 2: Rate increased to 25%

Year 3: DTL reverses; actual tax paid = €250,000

Treatment:
  Additional €50,000 (€250,000 - €200,000) treated as
  increase in Year 1 Covered Taxes
  Per Article 4.6.1, added to Year 3 Covered Taxes
```

## 6. Recapture Rules

### 6.1 Current Tax Recapture (Article 4.6.4)

**Rule:** If current tax expense included in Covered Taxes is **not paid within 3 years**, it must be recaptured.

**Threshold:** Only applies if unpaid amount exceeds **€1 million**.

**Process:**
1. At end of Year 3, assess unpaid current tax
2. If > €1 million unpaid, recalculate Year 1 ETR excluding unpaid amount
3. Any incremental Top-Up Tax → Additional Current Top-Up Tax

**Timeline:**
```
Year 1: Current tax expense €5,000,000 included in Covered Taxes
Year 4: Only €3,800,000 paid; €1,200,000 still unpaid

Recapture triggered:
  Recalculate Year 1 ETR excluding €1,200,000
  Incremental Top-Up Tax paid in Year 4
```

### 6.2 Deferred Tax Recapture (Article 4.4.4)

**Rule:** If DTL does not reverse within **5 years**, recapture applies.

**Distinction from current tax:**
| Aspect | Current Tax | Deferred Tax |
|--------|-------------|--------------|
| Recapture period | 3 years | 5 years |
| Threshold | €1 million | No threshold |
| Exceptions | None | Recapture Exception Accruals (REAs) |

The recapture rules address a fundamental concern: that Covered Taxes should represent taxes that are actually paid, not merely accrued. Without recapture, groups could record optimistic current tax accruals to inflate their ETR, then quietly fail to pay those taxes—or claim DTL benefits for liabilities that never reverse. The three-year period for current tax and five-year period for deferred tax provide reasonable windows for payment or reversal while acknowledging that tax positions take time to resolve. The €1 million threshold for current tax recapture provides administrative relief for minor variances, recognising that perfect matching between accruals and payments is often impractical. The absence of a threshold for DTL recapture reflects greater concern about permanent deferrals—DTLs that simply never reverse represent claimed benefits without corresponding tax payments.

## 7. Transfer Pricing Adjustments

### 7.1 General Principle

GloBE respects transfer pricing adjustments made by local tax authorities:
- Unilateral adjustments are generally accepted
- Corresponding adjustments ensure no double taxation

### 7.2 Unilateral Adjustment Treatment

When Country A's tax authority makes a TP adjustment:

**If Country A is higher-taxed:** Adjustment reduces Country A entity's expense → Increase Country A's GloBE Income → Corresponding decrease in Country B's GloBE Income

**If Country A is under-taxed (ETR < 15%):** No corresponding adjustment in Country B → Prevents artificial reduction of low-tax income

### 7.3 Post-Filing TP Adjustments

| Scenario | Treatment |
|----------|-----------|
| TP audit increases tax in Year 1 (discovered Year 3) | Add to Year 3 Covered Taxes (Art. 4.6.1) |
| TP audit decreases tax in Year 1 (discovered Year 3) | Recalculate Year 1 ETR; Additional Top-Up Tax in Year 3 |
| Bilateral APA applied retroactively | Adjust per APA terms; follow 4.6.1/recalculation rules |
| Self-initiated TP true-up | Complex—depends on timing and direction |

### 7.4 Self-Initiated TP True-Ups

**Issue:** Many MNEs make year-end TP true-ups after books close but before returns filed.

**GloBE treatment:**
- If true-up is made **before** GIR filed: Include in original GloBE computation
- If true-up is made **after** GIR filed: Apply post-filing adjustment rules

**Warning:** True-ups that increase income in low-tax jurisdictions may increase Top-Up Tax exposure.

## 8. Audit Settlement Scenarios

### 8.1 Tax Authority Audit Resulting in Additional Assessment

```
Scenario: German tax authority audits SG Germany GmbH for FY 2024
          Assessment issued in FY 2027: Additional tax €800,000

Treatment:
  Add €800,000 to FY 2027 Covered Taxes
  No recalculation of FY 2024
  No amended GIR
```

### 8.2 Tax Authority Audit Resulting in Refund

```
Scenario: Irish Revenue audits SG Ireland Ltd for FY 2024
          Refund issued in FY 2027: €600,000

Treatment (assuming > €1M threshold not met at jurisdiction level):
  If immaterial election made: Reduce FY 2027 Covered Taxes
  If no election: Recalculate FY 2024 ETR
```

### 8.3 Mutual Agreement Procedure (MAP) Resolution

```
Scenario: MAP resolves double taxation between UK and Germany
          UK receives additional tax €1,500,000
          Germany provides corresponding refund €1,500,000

Treatment:
  UK: Add €1,500,000 to current year Covered Taxes
  Germany:
    If ≥ €1M: Recalculate prior year
    If < €1M with election: Reduce current year Covered Taxes
```

## 9. Post-Filing Adjustment Timeline

```
YEAR 1 (GIR FILED)          YEAR 2                    YEAR 3                    YEAR 4
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
┌──────────────┐          ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│ GIR Filed    │          │ Audit Begins │          │ Assessment   │          │ 3-Year       │
│ FY 2024      │          │              │          │ Issued       │          │ Recapture    │
│              │          │              │          │              │          │ Check        │
└──────────────┘          └──────────────┘          └──────────────┘          └──────────────┘
                                                          │                         │
                                                          ▼                         ▼
                                               ┌──────────────────┐     ┌──────────────────┐
                                               │ If INCREASE:     │     │ Current tax not  │
                                               │ Add to Year 3    │     │ paid from Year 1 │
                                               │ Covered Taxes    │     │ > €1M?           │
                                               │                  │     │ → Recapture      │
                                               │ If DECREASE:     │     │                  │
                                               │ Recalculate      │     │                  │
                                               │ Year 1 ETR       │     │                  │
                                               └──────────────────┘     └──────────────────┘
```

## 10. Stratos Worked Example: Post-Filing Adjustments

**Scenario:** Stratos Group has three post-filing adjustments in FY 2027 relating to FY 2025:

### 10.1 Data

| Jurisdiction | Adjustment | Amount (€) | Type |
|--------------|------------|------------|------|
| Germany | Tax audit assessment | +750,000 | Increase |
| Singapore | TP adjustment (refund) | -1,400,000 | Decrease |
| Ireland | R&D credit error correction | +180,000 | Increase |

### 10.2 FY 2025 Original Position (for reference)

| Jurisdiction | GloBE Income | Covered Taxes | ETR |
|--------------|--------------|---------------|-----|
| Germany | €53,880,000 | €12,250,000 | 22.7% |
| Singapore | €4,000,000 | €352,500 | 8.8% |
| Ireland | €15,000,000 | €1,875,000 | 12.5% |

### 10.3 Treatment Analysis

**1. Germany (+€750,000 increase)**
```
Article 4.6.1 applies:
  Add €750,000 to FY 2027 German Covered Taxes
  No recalculation of FY 2025
```

**2. Singapore (-€1,400,000 decrease)**
```
Decrease > €1M → Cannot use immaterial exception
Must recalculate FY 2025 Singapore ETR:

Original:
  GloBE Income:    €4,000,000
  Covered Taxes:   €352,500
  ETR:             8.8%
  Top-Up Tax %:    6.2%
  Top-Up Tax:      €248,000

Revised:
  GloBE Income:    €4,000,000
  Covered Taxes:   €352,500 - €1,400,000 = NEGATIVE

Wait—this creates negative Covered Taxes.
Need to verify: The refund likely relates to tax paid in
FY 2025, reducing Covered Taxes.

Revised Covered Taxes: -€1,047,500 (negative)
Revised ETR: Negative ETR → Top-Up Tax % = 15%
Revised Top-Up Tax: 15% × €4,000,000 = €600,000

Original Top-Up Tax: €248,000
Incremental: €600,000 - €248,000 = €352,000

Additional Current Top-Up Tax in FY 2027: €352,000
```

**3. Ireland (+€180,000 increase)**
```
Article 4.6.1 applies:
  Add €180,000 to FY 2027 Irish Covered Taxes
  No recalculation of FY 2025
```

### 10.4 Summary Impact on FY 2027

| Item | Amount (€) |
|------|------------|
| Germany Covered Taxes adjustment | +750,000 |
| Ireland Covered Taxes adjustment | +180,000 |
| Singapore Additional Current Top-Up Tax | +352,000 |

**Note:** The Singapore refund results in additional Top-Up Tax because the original ETR (8.8%) was already below 15%. The refund pushes Covered Taxes negative, worsening the ETR significantly.

## 11. Post-Filing Adjustment Checklist

### 11.1 When Adjustment Identified

- [ ] Determine fiscal year to which adjustment relates
- [ ] Classify as increase or decrease in Covered Taxes
- [ ] Identify jurisdiction affected

### 11.2 For Increases

- [ ] Add to current year Covered Taxes (Article 4.6.1)
- [ ] Document adjustment in GIR workpapers
- [ ] No amended GIR required

### 11.3 For Decreases

- [ ] Calculate aggregate decrease for jurisdiction
- [ ] If < €1M: Consider immaterial election
- [ ] If ≥ €1M or no election: Recalculate prior year ETR
- [ ] Calculate incremental Top-Up Tax
- [ ] Include as Additional Current Top-Up Tax (Article 5.2.3)
- [ ] Document recalculation workpapers

### 11.4 For Rate Changes

- [ ] Identify affected deferred tax balances
- [ ] Apply Article 4.6.2 (decrease) or 4.6.3 (increase)
- [ ] Recalculate as required

### 11.5 For Recapture

- [ ] At Year 3 end: Review unpaid current tax by jurisdiction
- [ ] Trigger recapture if unpaid > €1M
- [ ] At Year 5 end: Review unreversed DTLs (excluding REAs)
- [ ] Trigger recapture as required

## 12. Common Pitfalls

### 12.1 Pitfall 1: Treating Decreases Like Increases

**Issue:** Adding decreases to current year Covered Taxes without recalculation

**Impact:** Understates Top-Up Tax; potential penalty exposure

**Solution:** Always recalculate prior year for decreases (unless immaterial election applies)

### 12.2 Pitfall 2: Ignoring Transfer Pricing Timing

**Issue:** Self-initiated TP true-ups made after GIR filed create unexpected adjustments

**Impact:** May increase or decrease Covered Taxes with complex consequences

**Solution:** Complete TP true-ups before GIR filing where possible

### 12.3 Pitfall 3: Missing Recapture Deadlines

**Issue:** Failing to monitor 3-year (current tax) and 5-year (deferred tax) periods

**Impact:** Missed recapture triggers; ETR errors

**Solution:** Implement tracking system for unpaid taxes and unreversed DTLs

### 12.4 Pitfall 4: Aggregating Jurisdictions Incorrectly

**Issue:** Applying €1M immaterial threshold at entity level instead of jurisdiction level

**Impact:** Incorrect use of exception

**Solution:** Aggregate all CEs in jurisdiction when assessing threshold

Post-filing adjustments create an ongoing compliance obligation that extends well beyond initial GIR preparation. Groups must establish monitoring systems to track audits, refunds, transfer pricing settlements, and payment status across all jurisdictions. The asymmetric treatment rules—seemingly straightforward in concept—create complexity in practice, particularly for groups with multiple simultaneous adjustments across different jurisdictions. The interplay with recapture rules adds another dimension: groups must track not only post-filing adjustments but also the underlying payment and reversal status of previously claimed taxes. Building robust tracking systems and maintaining clear documentation of each adjustment's treatment is essential. Groups should also consider the strategic implications: knowing that decreases trigger recalculation may influence decisions about whether to seek refunds, accept audit settlements, or pursue aggressive positions that might later be reversed.

