# Chapter 5.3: Top-Up Tax Computation

## Learning Objective

After completing this chapter, you will be able to calculate the Top-Up Tax Percentage, compute Jurisdictional Top-Up Tax from Excess Profit, apply QDMTT offsets, and allocate Top-Up Tax to Low-Taxed Constituent Entities.

## Introduction

The Top-Up Tax computation translates the ETR shortfall identified in Chapter 5.1 into an actual tax liability. The process is straightforward in concept: multiply the gap between 15% and the actual ETR by the Excess Profit remaining after SBIE. Yet this mechanical calculation carries significant economic consequences. The resulting liability determines how much additional tax the MNE Group pays—and crucially, where that tax is collected. Jurisdictions that have implemented QDMTTs can intercept the Top-Up Tax, retaining the revenue domestically rather than ceding it to parent entity jurisdictions through the IIR or to UTPR jurisdictions. For groups with multiple low-taxed jurisdictions, the computation must be performed separately for each, and the resulting Top-Up Tax must be allocated to specific Constituent Entities within the jurisdiction—a step that matters for determining which parent in the ownership chain bears the IIR liability. Understanding these mechanics is essential for financial planning, provision calculations, and strategic responses to Pillar Two exposure.

## 1. The Complete Top-Up Tax Computation

The Top-Up Tax computation follows a four-step process:

```
Step 1: Calculate Top-Up Tax Percentage
        (15% − ETR)

Step 2: Calculate Jurisdictional Top-Up Tax
        (Top-Up Tax % × Excess Profit)

Step 3: Apply QDMTT Offset
        (Reduce by any Qualified Domestic Minimum Top-Up Tax paid)

Step 4: Allocate to Low-Taxed Constituent Entities
        (In proportion to GloBE Income)
```

## 2. Step 1: Top-Up Tax Percentage (Article 5.2.1)

The Top-Up Tax Percentage is the difference between the 15% minimum rate and the jurisdictional ETR:

```
Top-Up Tax Percentage = 15% − ETR
```

### 2.1 Key Rules

| Scenario | Top-Up Tax % | Result |
|----------|--------------|--------|
| ETR = 10% | 15% − 10% = 5% | Top-Up Tax applies |
| ETR = 14.99% | 15% − 14.99% = 0.01% | Top-Up Tax applies (small amount) |
| ETR = 15% | 15% − 15% = 0% | No Top-Up Tax |
| ETR = 20% | N/A | Not calculated (ETR ≥ 15%) |
| ETR = negative | 15% − (−5%) = 20% | Top-Up Tax % = 20% (no cap) |

### 2.2 Negative ETR Treatment

If the ETR is **negative** (Adjusted Covered Taxes are negative):

```
Top-Up Tax Percentage = 15% − ETR
```

**Example:** ETR = −5%
- Formula gives: 15% − (−5%) = **20%**

Per OECD Commentary paragraph 102, there is no cap—the Top-Up Tax Percentage equals 15% plus the absolute value of the negative ETR. This ensures the jurisdiction reaches a 15% effective rate on Excess Profit.

## 3. Step 2: Jurisdictional Top-Up Tax (Article 5.2.2)

Apply the Top-Up Tax Percentage to Excess Profit:

```
Jurisdictional Top-Up Tax = Top-Up Tax Percentage × Excess Profit
```

Where:
- **Excess Profit** = Net GloBE Income − SBIE (from Chapter 5.2)

### 3.1 The Complete Formula Chain

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Net GloBE Income                     €15,000,000               │
│  Less: SBIE                          (€1,675,200)               │
│                                       ───────────               │
│  Excess Profit                        €13,324,800               │
│                                                                 │
│  Top-Up Tax %                              3.2%                 │
│                                       ───────────               │
│  Jurisdictional Top-Up Tax              €426,394                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 4. Step 3: QDMTT Offset

If the jurisdiction has a **Qualified Domestic Minimum Top-Up Tax (QDMTT)**, the QDMTT paid reduces the Jurisdictional Top-Up Tax:

```
Net Top-Up Tax = Jurisdictional Top-Up Tax − QDMTT Paid
```

### 4.1 QDMTT Priority Rule

QDMTT has **priority** over IIR and UTPR:
1. Jurisdiction collects its own QDMTT first
2. Any remaining Top-Up Tax is collected via IIR or UTPR
3. If QDMTT covers full Top-Up Tax, no IIR/UTPR applies

### 4.2 Example: Ireland with QDMTT

Ireland has implemented a QDMTT. If Ireland collects the full Top-Up Tax domestically:

| Item | Amount |
|------|--------|
| Jurisdictional Top-Up Tax | €426,394 |
| QDMTT Paid (Ireland) | (€426,394) |
| **Net Top-Up Tax (IIR/UTPR)** | **€0** |

**Result:** No Top-Up Tax flows to parent entity under IIR—Ireland retains the tax.

The QDMTT priority rule reflects a fundamental policy choice in the GloBE architecture: allowing source jurisdictions to collect the minimum tax themselves before ceding revenue to residence jurisdictions. This design respects sovereign taxing rights while still achieving the minimum rate objective. For the MNE Group, QDMTT makes little difference to the total tax bill—the same Top-Up Tax is paid either way. But for competing jurisdictions, the difference is significant: Ireland collecting its own QDMTT retains revenue that would otherwise flow to the UK parent's treasury through the IIR. This dynamic has driven rapid QDMTT adoption, with most low-tax jurisdictions implementing or planning domestic minimum taxes. For compliance purposes, groups must track which jurisdictions have QDMTTs, verify that the QDMTT is actually "qualified" under GloBE rules (meaning it calculates liability consistently with GloBE principles), and offset the QDMTT paid against IIR liability.

## 5. Step 4: Allocation to Low-Taxed Constituent Entities (Article 5.2.4)

The Jurisdictional Top-Up Tax is allocated to Constituent Entities **in proportion to their GloBE Income**:

```
                                          CE's GloBE Income
Entity's Top-Up Tax = Jurisdictional Top-Up Tax × ─────────────────────────
                                                   Total Jurisdictional GloBE Income
```

### 5.1 Why Allocation Matters

Allocation determines:
- Which entity triggers the IIR charge
- Which parent in the ownership chain pays the Top-Up Tax
- Reporting requirements on the GIR

### 5.2 Multi-Entity Jurisdiction Example

**Jurisdiction:** Singapore (two entities)

| Entity | GloBE Income | Share |
|--------|--------------|-------|
| SG Singapore Pte Ltd | €3,200,000 | 80% |
| SG Singapore Services Pte Ltd | €800,000 | 20% |
| **Total** | **€4,000,000** | **100%** |

**Jurisdictional Top-Up Tax:** €197,916 (calculated below)

**Allocation:**

| Entity | Calculation | Allocated Top-Up Tax |
|--------|-------------|---------------------|
| SG Singapore Pte Ltd | €197,916 × 80% | €158,333 |
| SG Singapore Services Pte Ltd | €197,916 × 20% | €39,583 |
| **Total** | | **€197,916** |

### 5.3 Loss Entities

If a Constituent Entity has a **GloBE Loss**, it receives **no allocation**—losses are not included in the denominator for allocation purposes.

| Entity | GloBE Income/(Loss) | Included in Allocation? |
|--------|---------------------|------------------------|
| Entity A | €5,000,000 | Yes |
| Entity B | (€1,000,000) | No |
| Entity C | €2,000,000 | Yes |

**Allocation base:** €5,000,000 + €2,000,000 = €7,000,000

## 6. Additional Current Top-Up Tax (Article 5.2.3)

Additional Current Top-Up Tax arises in specific situations:

### 6.1 When It Applies

| Trigger | Article | Treatment |
|---------|---------|-----------|
| **DTL Recapture** | 4.4.4 | DTL not reversed within 5 years → recalculate prior year ETR |
| **Post-filing decrease** | 4.6 | Prior year Covered Taxes reduced → recalculate prior year |
| **Transition adjustments** | 9.1 | Certain transition period corrections |

### 6.2 Calculation

When Additional Current Top-Up Tax is triggered:

1. **Recalculate** the prior year's ETR without the DTL or with adjusted Covered Taxes
2. **Determine** if the recalculated ETR is below 15%
3. **Compute** the additional Top-Up Tax for that prior year
4. **Include** as Additional Current Top-Up Tax in the **current** fiscal year

### 6.3 Example: DTL Recapture

**FY 2024:** SG Germany GmbH claimed €400,000 DTL (at 15% cap) in Covered Taxes.

**FY 2029:** DTL has not reversed within 5 years → Recapture triggered.

**Original FY 2024 Calculation:**

| Item | Original | Recalculated |
|------|----------|--------------|
| Covered Taxes | €12,000,000 | €11,600,000 |
| GloBE Income | €50,000,000 | €50,000,000 |
| ETR | 24.0% | 23.2% |
| Top-Up Tax | €0 | €0 |

**Result:** ETR remains above 15% even after recapture → No Additional Current Top-Up Tax.

**Alternative scenario:** If recalculated ETR fell to 14.5%:
- Top-Up Tax % = 0.5%
- Excess Profit (assume SBIE applied) = €40,000,000
- Additional Current Top-Up Tax = €200,000 (payable in FY 2029)

## 7. Stratos Worked Example: Complete Top-Up Tax Computation

### 7.1 Jurisdiction 1: Singapore

**Data from previous chapters:**

| Item | Reference | Amount |
|------|-----------|--------|
| Net GloBE Income | Chapter 5.1 | €4,000,000 |
| Adjusted Covered Taxes | Chapter 5.1 | €392,206 |
| ETR | Chapter 5.1 | 9.81% |
| SBIE | Chapter 5.2 | €194,645 |
| Excess Profit | Chapter 5.2 | €3,805,355 |

**Step 1: Top-Up Tax Percentage**

```
Top-Up Tax % = 15% − 9.81% = 5.19%
```

**Step 2: Jurisdictional Top-Up Tax**

```
Jurisdictional Top-Up Tax = 5.19% × €3,805,355 = €197,498
```

**Step 3: QDMTT Offset**

Singapore has **not** implemented a QDMTT (as of FY 2025).

```
QDMTT Paid:                             €0
Net Top-Up Tax:                         €197,498
```

**Step 4: Allocation**

Singapore has one entity (SG Singapore Pte Ltd):

```
Allocation: 100% to SG Singapore Pte Ltd = €197,498
```

### 7.2 Singapore Summary

| Step | Description | Amount |
|------|-------------|--------|
| 1 | Top-Up Tax % | 5.19% |
| 2 | Jurisdictional Top-Up Tax | €197,498 |
| 3 | QDMTT Offset | €0 |
| 4 | **Net Top-Up Tax** | **€197,498** |

### 7.3 Jurisdiction 2: Ireland

**Data from previous chapters:**

| Item | Reference | Amount |
|------|-----------|--------|
| Net GloBE Income | Chapter 5.1 | €15,000,000 |
| Adjusted Covered Taxes | Chapter 5.1 | €1,770,000 |
| ETR | Chapter 5.1 | 11.80% |
| SBIE | Chapter 5.2 | €1,675,200 |
| Excess Profit | Chapter 5.2 | €13,324,800 |

**Step 1: Top-Up Tax Percentage**

```
Top-Up Tax % = 15% − 11.80% = 3.20%
```

**Step 2: Jurisdictional Top-Up Tax**

```
Jurisdictional Top-Up Tax = 3.20% × €13,324,800 = €426,394
```

**Step 3: QDMTT Offset**

Ireland **has** implemented a QDMTT. Assume Ireland collects the full Top-Up Tax domestically:

```
QDMTT Paid (Ireland):                   €426,394
Net Top-Up Tax (IIR/UTPR):              €0
```

**Step 4: Allocation**

Since QDMTT covers the full liability, no allocation to parent entities is required for IIR purposes.

### 7.4 Ireland Summary

| Step | Description | Amount |
|------|-------------|--------|
| 1 | Top-Up Tax % | 3.20% |
| 2 | Jurisdictional Top-Up Tax | €426,394 |
| 3 | QDMTT Offset | (€426,394) |
| 4 | **Net Top-Up Tax (IIR)** | **€0** |

**Result:** Ireland retains the Top-Up Tax through QDMTT. No IIR charge to Stratos Holdings plc.

## 8. Consolidated Top-Up Tax Summary

### 8.1 Stratos Group FY 2025

| Jurisdiction | ETR | Top-Up Tax % | Excess Profit | Jur. Top-Up Tax | QDMTT | Net Top-Up Tax |
|--------------|-----|--------------|---------------|-----------------|-------|----------------|
| Germany | 23.00% | N/A | N/A | €0 | N/A | €0 |
| Singapore | 9.81% | 5.19% | €3,805,355 | €197,498 | €0 | **€197,498** |
| Ireland | 11.80% | 3.20% | €13,324,800 | €426,394 | (€426,394) | €0 |
| **Total** | | | | **€623,892** | **(€426,394)** | **€197,498** |

### 8.2 Where Does Stratos Pay?

| Amount | Recipient | Mechanism |
|--------|-----------|-----------|
| €197,498 | UK (Stratos Holdings plc) | **IIR** |
| €426,394 | Ireland | **QDMTT** (retained by Ireland) |

**Total Group Tax Liability:** €623,892

**Of which:**
- Paid to UK via IIR: €197,498
- Retained by Ireland via QDMTT: €426,394

## 9. IIR vs UTPR Application

Once the Net Top-Up Tax is determined, the charging mechanism applies:

### 9.1 IIR First (Article 2.1)

The **IIR** applies at the Ultimate Parent Entity level:

```
If UPE is in an IIR jurisdiction:
    → UPE pays Top-Up Tax on all low-taxed subsidiaries
```

**Stratos example:** UK has implemented IIR. Stratos Holdings plc pays €197,498 on Singapore.

### 9.2 UTPR as Backstop (Article 2.4)

The **UTPR** applies if:
- No IIR covers the Top-Up Tax, OR
- UPE is in a non-IIR jurisdiction

```
If UPE is NOT in an IIR jurisdiction:
    → UTPR jurisdictions collect Top-Up Tax via denied deductions
```

## 10. Computation Flowchart

```
START: Low-taxed jurisdiction identified (ETR < 15%)
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Step 1: Top-Up Tax Percentage                     │
│         = 15% − ETR                               │
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Step 2: Jurisdictional Top-Up Tax                 │
│         = Top-Up Tax % × Excess Profit            │
│         (where Excess Profit = GloBE Income - SBIE)│
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Does jurisdiction have QDMTT?                     │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────┐
  YES       NO
   │         │
   ▼         │
┌────────────────────┐                              │
│ Step 3: QDMTT      │                              │
│ Offset             │                              │
│ Net = Jur. Top-up  │                              │
│       − QDMTT Paid │                              │
└────────────────────┘                              │
        │                                           │
        ▼                                           ▼
┌───────────────────────────────────────────────────┐
│ Step 4: Allocate to LTCEs                         │
│         (In proportion to GloBE Income)           │
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Apply IIR or UTPR                                 │
│ (Chapter 2.1 / 2.4)                               │
└───────────────────────────────────────────────────┘
        │
        ▼
END: Top-Up Tax collected
```

## 11. Common Pitfalls

### 11.1 Pitfall 1: Applying Top-Up Tax % to Net GloBE Income

**Error:** Calculating Top-Up Tax as Top-Up Tax % × Net GloBE Income.

**Correct approach:** Apply Top-Up Tax % to **Excess Profit** (Net GloBE Income − SBIE).

### 11.2 Pitfall 2: Forgetting QDMTT Offset

**Error:** Reporting full Jurisdictional Top-Up Tax without checking for QDMTT.

**Correct approach:** Always check if the jurisdiction has implemented QDMTT and reduce the IIR/UTPR liability accordingly.

### 11.3 Pitfall 3: Allocating to Loss Entities

**Error:** Including entities with GloBE Losses in the allocation calculation.

**Correct approach:** Only entities with **positive** GloBE Income receive an allocation of Top-Up Tax.

### 11.4 Pitfall 4: Ignoring Additional Current Top-Up Tax

**Error:** Failing to track DTL recapture and post-filing adjustments.

**Correct approach:** Monitor 5-year DTL reversal and 3-year current tax payment timelines; recalculate prior years when triggered.

### 11.5 Pitfall 5: Double-Counting QDMTT

**Error:** Reducing Jurisdictional Top-Up Tax by estimated QDMTT before it's actually paid.

**Correct approach:** Only offset QDMTT that is **actually paid** in the fiscal year.

## 12. Top-Up Tax Calculation Worksheet

Use this worksheet for each low-taxed jurisdiction:

```
TOP-UP TAX CALCULATION WORKSHEET
Jurisdiction: _________________________
Fiscal Year: _________________________

SECTION A: INPUTS
A1  Net GloBE Income (from Ch. 5.1)              €__________________
A2  ETR (from Ch. 5.1)                           __________________%
A3  SBIE (from Ch. 5.2)                          €__________________
A4  Excess Profit (A1 − A3)                      €__________________

SECTION B: TOP-UP TAX PERCENTAGE
B1  Minimum Rate                                  15%
B2  Jurisdictional ETR (A2)                      __________________%
B3  TOP-UP TAX PERCENTAGE (B1 − B2)              __________________%

    If B3 ≤ 0%: STOP. No Top-Up Tax.

SECTION C: JURISDICTIONAL TOP-UP TAX
C1  Excess Profit (A4)                           €__________________
C2  Top-Up Tax Percentage (B3)                   __________________%
C3  JURISDICTIONAL TOP-UP TAX (C1 × C2)          €__________________

SECTION D: QDMTT OFFSET
D1  Does jurisdiction have QDMTT?                 YES / NO

    If NO: Skip to Section E

D2  QDMTT Paid                                   €__________________
D3  NET TOP-UP TAX (C3 − D2)                     €__________________

    If D3 ≤ 0: No IIR/UTPR liability.

SECTION E: ALLOCATION TO LTCEs
List entities with positive GloBE Income:

| Entity | GloBE Income | % Share | Allocated Top-Up Tax |
|--------|--------------|---------|---------------------|
| ______ | €___________ | ______% | €__________________ |
| ______ | €___________ | ______% | €__________________ |
| ______ | €___________ | ______% | €__________________ |
| TOTAL  | €___________ | 100%    | €__________________ |

SECTION F: ADDITIONAL CURRENT TOP-UP TAX
F1  Any DTL recapture triggered?                  YES / NO
F2  Any post-filing adjustments?                  YES / NO

    If YES to either: Complete recalculation per Article 5.2.3

F3  Additional Current Top-Up Tax                €__________________
F4  TOTAL TOP-UP TAX (D3 or C3 + F3)             €__________________

SECTION G: CHARGING MECHANISM
G1  UPE in IIR jurisdiction?                      YES / NO

    If YES: IIR applies → UPE pays Top-Up Tax
    If NO:  UTPR applies → Allocated to UTPR jurisdictions
```

The Top-Up Tax computation brings together all the preceding analysis—GloBE Income, Covered Taxes, ETR calculation, and SBIE—into a final liability figure. For many groups, this number will be the most important outcome of the entire Pillar Two compliance process, directly affecting financial statements, cash flows, and strategic decisions. The QDMTT offset adds a layer of complexity that requires monitoring jurisdictional adoption and implementation timing. The allocation rules matter primarily for IIR purposes, determining which parent entity in potentially complex ownership structures bears the tax liability. Perhaps most importantly, the Top-Up Tax computation is not a one-time exercise: the Additional Current Top-Up Tax rules mean that groups must continue monitoring prior-year calculations for DTL recapture, post-filing adjustments, and other triggers that can create liability in subsequent years. Building systems that track these ongoing obligations is as important as performing the initial computation correctly.
