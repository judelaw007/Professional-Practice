# Chapter 5.3: Top-Up Tax Computation

## Learning Objective

After completing this chapter, you will be able to calculate the Top-up Tax Percentage, compute Jurisdictional Top-up Tax from Excess Profit, apply QDMTT offsets, and allocate Top-up Tax to Low-Taxed Constituent Entities.

---

## Key References

**OECD GloBE Model Rules:**
- Article 5.2.1 — Top-up Tax Percentage
- Article 5.2.2 — Jurisdictional Top-up Tax
- Article 5.2.3 — Additional Current Top-up Tax
- Article 5.2.4 — Allocation to Low-Taxed Constituent Entities
- Article 5.4.1 — ETR recalculation for prior periods

**Administrative Guidance:**
- February 2023: QDMTT offset mechanics
- December 2023: Additional Current Top-up Tax timing

**OECD Commentary:**
- Chapter 5, paragraphs 96-145 — Top-up Tax computation methodology

---

## The Complete Top-Up Tax Computation

The Top-up Tax computation follows a four-step process:

```
Step 1: Calculate Top-up Tax Percentage
        (15% − ETR)

Step 2: Calculate Jurisdictional Top-up Tax
        (Top-up Tax % × Excess Profit)

Step 3: Apply QDMTT Offset
        (Reduce by any Qualified Domestic Minimum Top-up Tax paid)

Step 4: Allocate to Low-Taxed Constituent Entities
        (In proportion to GloBE Income)
```

---

## Step 1: Top-Up Tax Percentage *(Article 5.2.1)*

The Top-up Tax Percentage is the difference between the 15% minimum rate and the jurisdictional ETR:

```
Top-up Tax Percentage = 15% − ETR
```

### Key Rules

| Scenario | Top-up Tax % | Result |
|----------|--------------|--------|
| ETR = 10% | 15% − 10% = 5% | Top-up Tax applies |
| ETR = 14.99% | 15% − 14.99% = 0.01% | Top-up Tax applies (small amount) |
| ETR = 15% | 15% − 15% = 0% | No Top-up Tax |
| ETR = 20% | N/A | Not calculated (ETR ≥ 15%) |
| ETR = negative | 15% − (−5%) = 20% | Top-up Tax % capped at 15% |

### Negative ETR Treatment

If the ETR is **negative** (Adjusted Covered Taxes are negative):

```
Top-up Tax Percentage = MIN(15%, 15% − ETR)
```

**Example:** ETR = −5%
- Formula gives: 15% − (−5%) = 20%
- But capped at: **15%**

The Top-up Tax Percentage cannot exceed 15% *(the maximum shortfall from zero to the minimum rate)*.

---

## Step 2: Jurisdictional Top-Up Tax *(Article 5.2.2)*

Apply the Top-up Tax Percentage to Excess Profit:

```
Jurisdictional Top-up Tax = Top-up Tax Percentage × Excess Profit
```

Where:
- **Excess Profit** = Net GloBE Income − SBIE (from Chapter 5.2)

### The Complete Formula Chain

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Net GloBE Income                     €15,000,000               │
│  Less: SBIE                          (€1,634,400)               │
│                                       ───────────               │
│  Excess Profit                        €13,365,600               │
│                                                                 │
│  Top-up Tax %                              3.2%                 │
│                                       ───────────               │
│  Jurisdictional Top-up Tax              €427,699                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 3: QDMTT Offset

If the jurisdiction has a **Qualified Domestic Minimum Top-up Tax (QDMTT)**, the QDMTT paid reduces the Jurisdictional Top-up Tax:

```
Net Top-up Tax = Jurisdictional Top-up Tax − QDMTT Paid
```

### QDMTT Priority Rule

QDMTT has **priority** over IIR and UTPR:
1. Jurisdiction collects its own QDMTT first
2. Any remaining Top-up Tax is collected via IIR or UTPR
3. If QDMTT covers full Top-up Tax, no IIR/UTPR applies

### Example: Ireland with QDMTT

Ireland has implemented a QDMTT. If Ireland collects the full Top-up Tax domestically:

| Item | Amount |
|------|--------|
| Jurisdictional Top-up Tax | €427,699 |
| QDMTT Paid (Ireland) | (€427,699) |
| **Net Top-up Tax (IIR/UTPR)** | **€0** |

**Result:** No Top-up Tax flows to parent entity under IIR—Ireland retains the tax.

---

## Step 4: Allocation to Low-Taxed Constituent Entities *(Article 5.2.4)*

The Jurisdictional Top-up Tax is allocated to Constituent Entities **in proportion to their GloBE Income**:

```
                                          CE's GloBE Income
Entity's Top-up Tax = Jurisdictional Top-up Tax × ─────────────────────────
                                                   Total Jurisdictional GloBE Income
```

### Why Allocation Matters

Allocation determines:
- Which entity triggers the IIR charge
- Which parent in the ownership chain pays the Top-up Tax
- Reporting requirements on the GIR

### Multi-Entity Jurisdiction Example

**Jurisdiction:** Singapore (two entities)

| Entity | GloBE Income | Share |
|--------|--------------|-------|
| SG Singapore Pte Ltd | €3,200,000 | 80% |
| SG Singapore Services Pte Ltd | €800,000 | 20% |
| **Total** | **€4,000,000** | **100%** |

**Jurisdictional Top-up Tax:** €197,916 (calculated below)

**Allocation:**

| Entity | Calculation | Allocated Top-up Tax |
|--------|-------------|---------------------|
| SG Singapore Pte Ltd | €197,916 × 80% | €158,333 |
| SG Singapore Services Pte Ltd | €197,916 × 20% | €39,583 |
| **Total** | | **€197,916** |

### Loss Entities

If a Constituent Entity has a **GloBE Loss**, it receives **no allocation**—losses are not included in the denominator for allocation purposes.

| Entity | GloBE Income/(Loss) | Included in Allocation? |
|--------|---------------------|------------------------|
| Entity A | €5,000,000 | Yes |
| Entity B | (€1,000,000) | No |
| Entity C | €2,000,000 | Yes |

**Allocation base:** €5,000,000 + €2,000,000 = €7,000,000

---

## Additional Current Top-Up Tax *(Article 5.2.3)*

Additional Current Top-up Tax arises in specific situations:

### When It Applies

| Trigger | Article | Treatment |
|---------|---------|-----------|
| **DTL Recapture** | 4.4.4 | DTL not reversed within 5 years → recalculate prior year ETR |
| **Post-filing decrease** | 4.6 | Prior year Covered Taxes reduced → recalculate prior year |
| **Transition adjustments** | 9.1 | Certain transition period corrections |

### Calculation

When Additional Current Top-up Tax is triggered:

1. **Recalculate** the prior year's ETR without the DTL or with adjusted Covered Taxes
2. **Determine** if the recalculated ETR is below 15%
3. **Compute** the additional Top-up Tax for that prior year
4. **Include** as Additional Current Top-up Tax in the **current** fiscal year

### Example: DTL Recapture

**FY 2024:** SG Germany GmbH claimed €400,000 DTL (at 15% cap) in Covered Taxes.

**FY 2029:** DTL has not reversed within 5 years → Recapture triggered.

**Original FY 2024 Calculation:**

| Item | Original | Recalculated |
|------|----------|--------------|
| Covered Taxes | €12,000,000 | €11,600,000 |
| GloBE Income | €50,000,000 | €50,000,000 |
| ETR | 24.0% | 23.2% |
| Top-up Tax | €0 | €0 |

**Result:** ETR remains above 15% even after recapture → No Additional Current Top-up Tax.

**Alternative scenario:** If recalculated ETR fell to 14.5%:
- Top-up Tax % = 0.5%
- Excess Profit (assume SBIE applied) = €40,000,000
- Additional Current Top-up Tax = €200,000 (payable in FY 2029)

---

## Stratos Worked Example: Complete Top-Up Tax Computation

### Jurisdiction 1: Singapore

**Data from previous chapters:**

| Item | Reference | Amount |
|------|-----------|--------|
| Net GloBE Income | Chapter 5.1 | €4,000,000 |
| Adjusted Covered Taxes | Chapter 5.1 | €392,206 |
| ETR | Chapter 5.1 | 9.81% |
| SBIE | Chapter 5.2 | €190,090 |
| Excess Profit | Chapter 5.2 | €3,809,910 |

**Step 1: Top-up Tax Percentage**

```
Top-up Tax % = 15% − 9.81% = 5.19%
```

**Step 2: Jurisdictional Top-up Tax**

```
Jurisdictional Top-up Tax = 5.19% × €3,809,910 = €197,734
```

**Step 3: QDMTT Offset**

Singapore has **not** implemented a QDMTT (as of FY 2025).

```
QDMTT Paid:                             €0
Net Top-up Tax:                         €197,734
```

**Step 4: Allocation**

Singapore has one entity (SG Singapore Pte Ltd):

```
Allocation: 100% to SG Singapore Pte Ltd = €197,734
```

### Singapore Summary

| Step | Description | Amount |
|------|-------------|--------|
| 1 | Top-up Tax % | 5.19% |
| 2 | Jurisdictional Top-up Tax | €197,734 |
| 3 | QDMTT Offset | €0 |
| 4 | **Net Top-up Tax** | **€197,734** |

---

### Jurisdiction 2: Ireland

**Data from previous chapters:**

| Item | Reference | Amount |
|------|-----------|--------|
| Net GloBE Income | Chapter 5.1 | €15,000,000 |
| Adjusted Covered Taxes | Chapter 5.1 | €1,770,000 |
| ETR | Chapter 5.1 | 11.80% |
| SBIE | Chapter 5.2 | €1,634,400 |
| Excess Profit | Chapter 5.2 | €13,365,600 |

**Step 1: Top-up Tax Percentage**

```
Top-up Tax % = 15% − 11.80% = 3.20%
```

**Step 2: Jurisdictional Top-up Tax**

```
Jurisdictional Top-up Tax = 3.20% × €13,365,600 = €427,699
```

**Step 3: QDMTT Offset**

Ireland **has** implemented a QDMTT. Assume Ireland collects the full Top-up Tax domestically:

```
QDMTT Paid (Ireland):                   €427,699
Net Top-up Tax (IIR/UTPR):              €0
```

**Step 4: Allocation**

Since QDMTT covers the full liability, no allocation to parent entities is required for IIR purposes.

### Ireland Summary

| Step | Description | Amount |
|------|-------------|--------|
| 1 | Top-up Tax % | 3.20% |
| 2 | Jurisdictional Top-up Tax | €427,699 |
| 3 | QDMTT Offset | (€427,699) |
| 4 | **Net Top-up Tax (IIR)** | **€0** |

**Result:** Ireland retains the Top-up Tax through QDMTT. No IIR charge to Stratos Holdings plc.

---

## Consolidated Top-Up Tax Summary

### Stratos Group FY 2025

| Jurisdiction | ETR | Top-up Tax % | Excess Profit | Jur. Top-up Tax | QDMTT | Net Top-up Tax |
|--------------|-----|--------------|---------------|-----------------|-------|----------------|
| Germany | 23.00% | N/A | N/A | €0 | N/A | €0 |
| Singapore | 9.81% | 5.19% | €3,809,910 | €197,734 | €0 | **€197,734** |
| Ireland | 11.80% | 3.20% | €13,365,600 | €427,699 | (€427,699) | €0 |
| **Total** | | | | **€625,433** | **(€427,699)** | **€197,734** |

### Where Does Stratos Pay?

| Amount | Recipient | Mechanism |
|--------|-----------|-----------|
| €197,734 | UK (Stratos Holdings plc) | **IIR** |
| €427,699 | Ireland | **QDMTT** (retained by Ireland) |

**Total Group Tax Liability:** €625,433

**Of which:**
- Paid to UK via IIR: €197,734
- Retained by Ireland via QDMTT: €427,699

---

## IIR vs UTPR Application

Once the Net Top-up Tax is determined, the charging mechanism applies:

### IIR First *(Article 2.1)*

The **IIR** applies at the Ultimate Parent Entity level:

```
If UPE is in an IIR jurisdiction:
    → UPE pays Top-up Tax on all low-taxed subsidiaries
```

**Stratos example:** UK has implemented IIR. Stratos Holdings plc pays €197,734 on Singapore.

### UTPR as Backstop *(Article 2.4)*

The **UTPR** applies if:
- No IIR covers the Top-up Tax, OR
- UPE is in a non-IIR jurisdiction

```
If UPE is NOT in an IIR jurisdiction:
    → UTPR jurisdictions collect Top-up Tax via denied deductions
```

---

## Computation Flowchart

```
START: Low-taxed jurisdiction identified (ETR < 15%)
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Step 1: Top-up Tax Percentage                     │
│         = 15% − ETR                               │
└───────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Step 2: Jurisdictional Top-up Tax                 │
│         = Top-up Tax % × Excess Profit            │
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
END: Top-up Tax collected
```

---

## Common Pitfalls

### Pitfall 1: Applying Top-up Tax % to Net GloBE Income

**Error:** Calculating Top-up Tax as Top-up Tax % × Net GloBE Income.

**Correct approach:** Apply Top-up Tax % to **Excess Profit** (Net GloBE Income − SBIE).

### Pitfall 2: Forgetting QDMTT Offset

**Error:** Reporting full Jurisdictional Top-up Tax without checking for QDMTT.

**Correct approach:** Always check if the jurisdiction has implemented QDMTT and reduce the IIR/UTPR liability accordingly.

### Pitfall 3: Allocating to Loss Entities

**Error:** Including entities with GloBE Losses in the allocation calculation.

**Correct approach:** Only entities with **positive** GloBE Income receive an allocation of Top-up Tax.

### Pitfall 4: Ignoring Additional Current Top-up Tax

**Error:** Failing to track DTL recapture and post-filing adjustments.

**Correct approach:** Monitor 5-year DTL reversal and 3-year current tax payment timelines; recalculate prior years when triggered.

### Pitfall 5: Double-Counting QDMTT

**Error:** Reducing Jurisdictional Top-up Tax by estimated QDMTT before it's actually paid.

**Correct approach:** Only offset QDMTT that is **actually paid** in the fiscal year.

---

## Top-Up Tax Calculation Worksheet

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

    If B3 ≤ 0%: STOP. No Top-up Tax.

SECTION C: JURISDICTIONAL TOP-UP TAX
C1  Excess Profit (A4)                           €__________________
C2  Top-up Tax Percentage (B3)                   __________________%
C3  JURISDICTIONAL TOP-UP TAX (C1 × C2)          €__________________

SECTION D: QDMTT OFFSET
D1  Does jurisdiction have QDMTT?                 YES / NO

    If NO: Skip to Section E

D2  QDMTT Paid                                   €__________________
D3  NET TOP-UP TAX (C3 − D2)                     €__________________

    If D3 ≤ 0: No IIR/UTPR liability.

SECTION E: ALLOCATION TO LTCEs
List entities with positive GloBE Income:

| Entity | GloBE Income | % Share | Allocated Top-up Tax |
|--------|--------------|---------|---------------------|
| ______ | €___________ | ______% | €__________________ |
| ______ | €___________ | ______% | €__________________ |
| ______ | €___________ | ______% | €__________________ |
| TOTAL  | €___________ | 100%    | €__________________ |

SECTION F: ADDITIONAL CURRENT TOP-UP TAX
F1  Any DTL recapture triggered?                  YES / NO
F2  Any post-filing adjustments?                  YES / NO

    If YES to either: Complete recalculation per Article 5.2.3

F3  Additional Current Top-up Tax                €__________________
F4  TOTAL TOP-UP TAX (D3 or C3 + F3)             €__________________

SECTION G: CHARGING MECHANISM
G1  UPE in IIR jurisdiction?                      YES / NO

    If YES: IIR applies → UPE pays Top-up Tax
    If NO:  UTPR applies → Allocated to UTPR jurisdictions
```

---

## Summary

The Top-up Tax computation brings together all prior calculations to determine the final liability. The key implementation steps are:

1. **Calculate Top-up Tax Percentage** — 15% minus jurisdictional ETR
2. **Apply to Excess Profit** — Not to full GloBE Income
3. **Check for QDMTT** — Offset any domestic minimum tax already paid
4. **Allocate to LTCEs** — In proportion to positive GloBE Income
5. **Monitor Additional Current Top-up Tax** — Track DTL recapture and post-filing adjustments
6. **Apply charging mechanism** — IIR first, UTPR as backstop

QDMTT-implementing jurisdictions retain their own Top-up Tax, eliminating IIR/UTPR collection.

---

## Integration with GIR Tools

The Top-up Tax calculation is **Step 3** of the GIR-001 GloBE Calculator workflow:

| GIR-001 Step | Function | Data Input |
|--------------|----------|------------|
| Step 1: ETR Calculation | Identifies low-taxed jurisdictions | GloBE Income + Covered Taxes |
| Step 2: SBIE Calculation | Computes substance carve-out | Payroll + Tangible Assets |
| **Step 3: Top-Up Tax** | Computes final liability | ETR + SBIE + QDMTT status |

**Workflow:**

1. GIR-001 automatically calculates Top-up Tax % from ETR
2. GIR-001 applies Top-up Tax % to Excess Profit
3. Enter QDMTT paid (if applicable) for offset
4. GIR-001 displays Net Top-up Tax and allocation by entity

Use **GIR-001 GloBE Calculator** at tools.mojitax.com to compute final Top-up Tax liabilities and verify your manual calculations.

---

## Next Step

You have learned how to compute the Jurisdictional Top-up Tax and apply QDMTT offsets. Proceed to **Chapter 5.4: Qualified Domestic Minimum Top-up Tax (QDMTT)** for detailed guidance on QDMTT criteria, safe harbours, and jurisdictional implementation status.
