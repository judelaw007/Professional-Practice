# Chapter 5.1: ETR Calculation Mechanics

## Learning Objective

After completing this chapter, you will be able to calculate the jurisdictional Effective Tax Rate (ETR) by applying the Article 5.1 formula, understand jurisdictional blending, and handle special cases including loss scenarios and negative covered taxes.

---

## Key References

**OECD GloBE Model Rules:**
- Article 5.1.1 — ETR formula
- Article 5.1.2 — Jurisdictional Net GloBE Income
- Article 5.1.3 — Adjusted Covered Taxes for ETR
- Article 5.1.4 — ETR rounding (four decimal places)

**Administrative Guidance:**
- February 2023: Negative tax expense treatment
- December 2023: Loss carry-forward interaction clarification

**OECD Commentary:**
- Chapter 5, paragraphs 1-25 — ETR calculation methodology

---

## The ETR Formula

The ETR calculation is the pivotal step that determines whether a jurisdiction is subject to Top-Up Tax. Article 5.1.1 provides the formula:

```
                    Adjusted Covered Taxes
ETR = ───────────────────────────────────────────
          Jurisdictional Net GloBE Income
```

**Express as a percentage, rounded to four decimal places** *(Article 5.1.4)*

If ETR < 15%: The jurisdiction is **low-taxed** and Top-Up Tax applies
If ETR ≥ 15%: **No Top-Up Tax** for that jurisdiction

### The Two Components

| Component | Definition | Source |
|-----------|------------|--------|
| **Adjusted Covered Taxes** | Covered Taxes after all adjustments from Part 4 (current tax adjustments, DTAA, tax allocations) | Article 5.1.3 |
| **Jurisdictional Net GloBE Income** | Sum of GloBE Income for all CEs in the jurisdiction, minus GloBE Losses | Article 5.1.2 |

---

## Jurisdictional Blending: The Core Principle

The GloBE rules use **jurisdictional blending**, not global blending. This is a fundamental design choice that determines how ETRs are calculated.

### What Jurisdictional Blending Means

All Constituent Entities in the **same jurisdiction** are combined for ETR purposes:

```
                    Sum of Adjusted Covered Taxes (all CEs in jurisdiction)
Jurisdictional ETR = ─────────────────────────────────────────────────────────
                      Sum of Net GloBE Income (all CEs in jurisdiction)
```

### Why This Matters

**Scenario:** A jurisdiction has two entities—one high-taxed, one low-taxed.

| Entity | GloBE Income | Covered Taxes | Entity ETR |
|--------|--------------|---------------|------------|
| Entity A | €10,000,000 | €2,000,000 | 20.0% |
| Entity B | €5,000,000 | €500,000 | 10.0% |
| **Jurisdiction Total** | **€15,000,000** | **€2,500,000** | **16.67%** |

**Result:** The high-taxed Entity A "shelters" the low-taxed Entity B. The **jurisdictional ETR** (16.67%) exceeds 15%, so **no Top-Up Tax** applies—even though Entity B individually would have triggered Top-Up Tax.

### Practical Implication

When assessing Top-Up Tax exposure:
- Do **not** calculate ETR per entity
- Calculate ETR per **jurisdiction** (aggregate all CEs in that country)
- A single high-taxed entity can eliminate Top-Up Tax for the entire jurisdiction

---

## Calculating Jurisdictional Net GloBE Income

Article 5.1.2 defines Jurisdictional Net GloBE Income as:

```
Jurisdictional Net GloBE Income = Σ(GloBE Income of all CEs) − Σ(GloBE Losses of all CEs)
```

### Step-by-Step Process

**Step 1:** Identify all Constituent Entities in the jurisdiction

**Step 2:** For each CE, determine GloBE Income or Loss (from Part 3 calculations)

**Step 3:** Sum all positive GloBE Income amounts

**Step 4:** Sum all GloBE Loss amounts (as positive numbers)

**Step 5:** Subtract total losses from total income

### Worked Example: Germany Jurisdiction

**Stratos entities in Germany:**

| Entity | GloBE Income/(Loss) |
|--------|---------------------|
| SG Germany GmbH | €53,880,000 |
| SG Germany Services GmbH | (€2,100,000) |
| SG Germany IP KG | €4,500,000 |

**Calculation:**

```
Step 1: Total GloBE Income = €53,880,000 + €4,500,000 = €58,380,000
Step 2: Total GloBE Losses = €2,100,000
Step 3: Jurisdictional Net GloBE Income = €58,380,000 − €2,100,000 = €56,280,000
```

**Key point:** The loss from SG Germany Services GmbH reduces the jurisdictional denominator, which **increases** the ETR (beneficial outcome).

---

## Handling Special Cases

### Case 1: Net GloBE Loss (Negative Denominator)

If Jurisdictional Net GloBE Income is **negative** (total losses exceed total income):

**Rule:** No ETR calculation is required. The jurisdiction is not subject to Top-Up Tax for that fiscal year.

**Rationale:** You cannot have a meaningful tax rate when there is no net income to tax.

**Example:**

| Entity | GloBE Income/(Loss) |
|--------|---------------------|
| Entity X | €3,000,000 |
| Entity Y | (€8,000,000) |
| **Net** | **(€5,000,000)** |

**Result:**
- Jurisdictional Net GloBE Income = (€5,000,000)
- **No ETR calculation**
- **No Top-Up Tax** for this fiscal year
- Loss may be carried forward (see GloBE Loss Election, Chapter 4.4)

### Case 2: Zero GloBE Income

If Jurisdictional Net GloBE Income equals exactly **zero**:

**Rule:** No ETR calculation is possible (division by zero). No Top-Up Tax applies.

### Case 3: Negative Adjusted Covered Taxes

Adjusted Covered Taxes can be **negative** when:
- Refunds exceed current tax expense
- Deferred tax credits exceed deferred tax expense
- Tax allocations result in net outflows

**Treatment:**

| Scenario | Covered Taxes | GloBE Income | ETR | Result |
|----------|---------------|--------------|-----|--------|
| Negative numerator | (€500,000) | €10,000,000 | -5.0% | **Low-taxed** (ETR < 15%) |
| Both negative | (€500,000) | (€2,000,000) | N/A | **No calculation** (negative denominator) |

**Key insight:** A negative ETR is possible and means the jurisdiction is definitely low-taxed.

### Case 4: Very Small GloBE Income

When GloBE Income is small, even modest Covered Taxes can produce very high ETRs.

**Example:**

| Item | Amount |
|------|--------|
| GloBE Income | €100,000 |
| Covered Taxes | €80,000 |
| **ETR** | **80.0%** |

**Practical note:** Small jurisdictions with minimal activity often have high ETRs due to fixed minimum taxes or registration fees. The De Minimis Exclusion (Chapter 5.5) addresses this.

---

## The Complete ETR Calculation Process

### ETR Calculation Flowchart

```
START
  │
  ▼
┌─────────────────────────────────────┐
│ Step 1: Aggregate all CEs in        │
│         jurisdiction                 │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│ Step 2: Calculate Jurisdictional    │
│         Net GloBE Income            │
│         (Income − Losses)           │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│ Is Net GloBE Income ≤ 0?            │
└─────────────────────────────────────┘
  │
  ├── YES ──► No ETR calculation required
  │           No Top-Up Tax
  │           (END)
  │
  NO
  │
  ▼
┌─────────────────────────────────────┐
│ Step 3: Aggregate Adjusted Covered  │
│         Taxes for jurisdiction      │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│ Step 4: Calculate ETR               │
│         ETR = Taxes ÷ Income        │
│         Round to 4 decimal places   │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│ Is ETR < 15%?                       │
└─────────────────────────────────────┘
  │
  ├── YES ──► LOW-TAXED JURISDICTION
  │           Proceed to SBIE and
  │           Top-Up Tax calculation
  │
  NO
  │
  ▼
NO TOP-UP TAX for this jurisdiction
(END)
```

---

## Stratos Worked Example: Complete ETR Calculation

Using data from Case Study 4, calculate ETRs for Stratos's three key jurisdictions.

### Data Summary (from Part 4)

| Jurisdiction | Adjusted GloBE Income | Adjusted Covered Taxes |
|--------------|----------------------|------------------------|
| Germany | €53,880,000 | €12,393,000 |
| Singapore | €4,000,000 | €392,206 |
| Ireland | €15,000,000 | €1,770,000 |

### Step 1: Germany ETR

```
                    €12,393,000
ETR (Germany) = ─────────────────── = 0.22999... = 23.00%
                    €53,880,000
```

**Result:** 23.00% > 15% → **No Top-Up Tax**

### Step 2: Singapore ETR

```
                      €392,206
ETR (Singapore) = ─────────────── = 0.09805... = 9.81%
                     €4,000,000
```

**Result:** 9.81% < 15% → **Low-taxed jurisdiction** → Proceed to SBIE

### Step 3: Ireland ETR

```
                     €1,770,000
ETR (Ireland) = ─────────────────── = 0.11800 = 11.80%
                    €15,000,000
```

**Result:** 11.80% < 15% → **Low-taxed jurisdiction** → Proceed to SBIE

### ETR Summary

| Jurisdiction | GloBE Income | Covered Taxes | ETR | Status |
|--------------|--------------|---------------|-----|--------|
| Germany | €53,880,000 | €12,393,000 | 23.00% | No Top-Up Tax |
| Singapore | €4,000,000 | €392,206 | 9.81% | **Low-taxed** |
| Ireland | €15,000,000 | €1,770,000 | 11.80% | **Low-taxed** |

---

## Multi-Entity Jurisdictions: Blending in Practice

### Scenario: UK Jurisdiction with Multiple Entities

Stratos has three entities in the UK:

| Entity | GloBE Income/(Loss) | Covered Taxes |
|--------|---------------------|---------------|
| Stratos Holdings plc | €8,500,000 | €2,125,000 |
| SG UK Services Ltd | €2,200,000 | €550,000 |
| SG UK Trading Ltd | (€1,500,000) | €0 |

### Calculation

**Step 1: Jurisdictional Net GloBE Income**
```
€8,500,000 + €2,200,000 − €1,500,000 = €9,200,000
```

**Step 2: Jurisdictional Adjusted Covered Taxes**
```
€2,125,000 + €550,000 + €0 = €2,675,000
```

**Step 3: ETR Calculation**
```
             €2,675,000
ETR (UK) = ───────────── = 29.08%
             €9,200,000
```

**Result:** 29.08% > 15% → **No Top-Up Tax** for UK jurisdiction

**Analysis:**
- SG UK Trading Ltd has a loss and zero taxes
- Without blending, its individual ETR would be undefined (0 ÷ negative)
- With jurisdictional blending, the loss reduces the denominator, and the profitable entities' taxes cover the jurisdiction

---

## Common Pitfalls

### Pitfall 1: Calculating ETR Per Entity Instead of Per Jurisdiction

**Error:** Computing separate ETRs for each subsidiary and assessing Top-Up Tax entity-by-entity.

**Correct approach:** Aggregate all CEs in the jurisdiction first, then calculate a single jurisdictional ETR.

### Pitfall 2: Ignoring Loss Entities in ETR Calculation

**Error:** Excluding loss-making entities from the jurisdictional aggregation.

**Correct approach:** Include all CEs—losses reduce the denominator, which affects the blended ETR.

### Pitfall 3: Attempting ETR Calculation with Negative Denominator

**Error:** Dividing by a negative number and treating the result as meaningful.

**Correct approach:** If Jurisdictional Net GloBE Income ≤ 0, stop—no ETR calculation is required.

### Pitfall 4: Inconsistent Rounding

**Error:** Rounding ETR to two decimal places (e.g., 14.99% becomes 15.0%).

**Correct approach:** Round to **four decimal places** per Article 5.1.4. An ETR of 14.9999% is still below 15% and triggers Top-Up Tax.

### Pitfall 5: Forgetting QRTC GloBE Income Adjustment

**Error:** Using GloBE Income from Case Study 3 without the QRTC addition.

**Correct approach:** If QRTCs were identified in Part 4, the corresponding addition to GloBE Income (Article 3.2.10) must be reflected in the denominator.

---

## ETR Calculation Worksheet

Use this worksheet for each jurisdiction:

```
ETR CALCULATION WORKSHEET
Jurisdiction: _________________________
Fiscal Year: _________________________

SECTION A: CONSTITUENT ENTITIES
List all CEs in this jurisdiction:

| # | Entity Name | GloBE Income/(Loss) | Adj. Covered Taxes |
|---|-------------|---------------------|-------------------|
| 1 | ___________ | €__________________ | €________________ |
| 2 | ___________ | €__________________ | €________________ |
| 3 | ___________ | €__________________ | €________________ |
| 4 | ___________ | €__________________ | €________________ |

SECTION B: AGGREGATION
B1  Total GloBE Income (positive amounts)    €__________________
B2  Total GloBE Losses (as positive number)  €__________________
B3  Jurisdictional Net GloBE Income (B1-B2)  €__________________

    If B3 ≤ 0: STOP. No ETR calculation. No Top-Up Tax.

B4  Total Adjusted Covered Taxes             €__________________

SECTION C: ETR CALCULATION
C1  ETR = B4 ÷ B3                            ___________________%
    (Round to 4 decimal places)

C2  Is ETR < 15%?                            YES / NO

    If YES: Low-taxed jurisdiction → Proceed to SBIE (Chapter 5.2)
    If NO:  No Top-Up Tax for this jurisdiction

SECTION D: VERIFICATION
D1  Data sources verified?                   ☐ GloBE Income (Part 3)
                                             ☐ Covered Taxes (Part 4)
D2  All CEs included?                        ☐ Yes
D3  QRTC adjustments applied to both         ☐ Yes / ☐ N/A
    numerator AND denominator?
```

---

## Why Global Blending Was Rejected

The OECD considered two approaches:

| Approach | Description | Outcome |
|----------|-------------|---------|
| **Global blending** | Calculate one ETR for the entire MNE group worldwide | Rejected |
| **Jurisdictional blending** | Calculate separate ETR per jurisdiction | **Adopted** |

### Why Jurisdictional Blending?

Global blending would have:
- Allowed high-tax jurisdictions to shelter low-tax jurisdictions across borders
- Significantly narrowed the scope of GloBE (fewer jurisdictions would be "low-taxed")
- Created opportunities for tax planning through strategic profit shifting

Jurisdictional blending ensures:
- Each jurisdiction is assessed independently
- Low-tax jurisdictions cannot be sheltered by high-tax jurisdictions in other countries
- The 15% minimum applies jurisdiction-by-jurisdiction

### Within-Jurisdiction Blending Is Permitted

Blending **within** a jurisdiction is intentional:
- Reflects economic reality (entities in the same country face similar tax environments)
- Simplifies compliance (one calculation per jurisdiction, not per entity)
- Allows temporary losses to offset profitable entities

---

## Summary

The ETR calculation is the gateway to Top-Up Tax determination. The key implementation steps are:

1. **Identify all CEs in the jurisdiction** — Include every Constituent Entity, regardless of profitability
2. **Calculate Jurisdictional Net GloBE Income** — Sum income, subtract losses
3. **Check for negative denominator** — If Net GloBE Income ≤ 0, stop; no Top-Up Tax
4. **Aggregate Adjusted Covered Taxes** — Sum across all CEs in the jurisdiction
5. **Apply the formula** — ETR = Covered Taxes ÷ Net GloBE Income
6. **Round to four decimal places** — Precision matters at the 15% threshold
7. **Assess result** — ETR < 15% = low-taxed; ETR ≥ 15% = no Top-Up Tax

Jurisdictional blending means high-tax entities can shelter low-tax entities within the same country, but not across borders.

---

## Integration with GIR Tools

The ETR calculation is **Step 1** of the GIR-001 GloBE Calculator workflow:

| GIR-001 Step | Function | Data Input |
|--------------|----------|------------|
| **Step 1: ETR Calculation** | Computes jurisdictional ETR | GloBE Income + Covered Taxes |
| Step 2: SBIE Calculation | Applies substance carve-out | Payroll + Tangible Assets |
| Step 3: Top-Up Tax | Computes final liability | ETR + SBIE results |

**Workflow:**

1. Enter Jurisdictional Net GloBE Income (from Part 3, adjusted for QRTCs)
2. Enter Adjusted Covered Taxes (from Part 4)
3. GIR-001 calculates ETR automatically
4. If ETR < 15%, proceed to Step 2 (SBIE)

Use **GIR-001 GloBE Calculator** at tools.mojitax.com to verify your manual ETR calculations before proceeding to SBIE.

---

## Next Step

You have learned how to calculate the jurisdictional ETR and identify low-taxed jurisdictions. Proceed to **Chapter 5.2: Substance-Based Income Exclusion (SBIE)** to learn how to reduce the Top-Up Tax base through payroll and tangible asset carve-outs.
