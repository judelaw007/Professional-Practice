# Chapter 6.5: Flow-Through UPEs

## Learning Objective

After completing this chapter, you will be able to identify when a UPE qualifies as a Flow-Through Entity, distinguish between Tax Transparent Entities and Reverse Hybrid Entities, apply the GloBE Income reduction mechanism under Article 7.1, and determine the correct location and ETR treatment for flow-through structures.

## 1. Why Special Rules for Flow-Through UPEs?

Flow-through entities at the top of an MNE Group create a fundamental problem for Pillar Two:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE FLOW-THROUGH UPE PROBLEM                                        │
│                                                                     │
│ Standard flow-through treatment:                                    │
│ → Income passes through to owners                                  │
│ → Owners (not entity) pay tax on that income                       │
│ → Entity itself has minimal or zero tax liability                  │
│                                                                     │
│ The GloBE problem:                                                  │
│ → UPE's owners are OUTSIDE the MNE Group scope                     │
│ → Cannot allocate income to owners (they're not Constituent Entities)│
│ → Income remains with UPE, but UPE pays little/no tax              │
│ → Result: Very low ETR → Substantial Top-Up Tax exposure           │
│                                                                     │
│ THE SOLUTION (Article 7.1):                                         │
│ → Reduce UPE's GloBE Income for income allocated to owners         │
│ → Corresponding reduction in Covered Taxes                          │
│ → Prevents distortion from taxation at owner level                 │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Definitions: Flow-Through Entities *(Article 10.2)*

### 2.1 Flow-Through Entity

A **Flow-Through Entity** is an entity that is **fiscally transparent** in the jurisdiction where it was created. Under the GloBE Rules, there are two types:

| Type | Description |
|------|-------------|
| **Tax Transparent Entity (TTE)** | Transparent to its owners — owners recognise income as if it arose directly to them |
| **Reverse Hybrid Entity (RHE)** | Transparent in jurisdiction of creation but **opaque** to owners |

### 2.2 Tax Transparent Entity (TTE) *(Article 10.2.1)*

An entity is a **Tax Transparent Entity** if:
- It is fiscally transparent in its jurisdiction of creation, **AND**
- The owner's jurisdiction also treats it as transparent

```
TAX TRANSPARENT ENTITY EXAMPLE

Jersey Limited Partnership
├── Created in: Jersey (transparent)
└── Owner: UK Company

UK tax treatment:
→ UK views Jersey LP as transparent
→ UK Company includes LP income in its own tax return
→ Jersey LP is a TTE with respect to UK Company owner
```

**Effect:** TTE's income and Covered Taxes flow up to its Constituent Entity-owner. The TTE does not have a separate GloBE calculation.

### 2.3 Reverse Hybrid Entity (RHE) *(Article 10.2.2)*

An entity is a **Reverse Hybrid Entity** if:
- It is fiscally transparent in its jurisdiction of creation, **BUT**
- The owner's jurisdiction treats it as **opaque** (a separate taxable entity)

```
REVERSE HYBRID ENTITY EXAMPLE

US LLC (disregarded for US tax)
├── Created in: US (transparent/disregarded)
└── Owner: Dutch BV

Dutch tax treatment:
→ Netherlands views US LLC as opaque (separate entity)
→ Dutch BV does NOT include LLC income in its return
→ US LLC is an RHE with respect to Dutch BV owner

CONSEQUENCE:
→ RHE treated as "Stateless Entity"
→ Separate ETR calculation (no jurisdictional blending)
→ Typically 0% ETR → Full Top-Up Tax exposure
```

### 2.4 Dual Classification

The same entity can be classified differently for different owners:

```
DUAL CLASSIFICATION EXAMPLE

Cayman LP
├── Owner A: US Corporation → TTE (US treats LP as transparent)
└── Owner B: French SA → RHE (France treats LP as opaque)

Treatment:
→ Income attributable to Owner A: Allocated to US Corporation
→ Income attributable to Owner B: Stays with Cayman LP (RHE treatment)
```

## 3. Location Rules for Flow-Through Entities

Where a Flow-Through Entity is "located" determines how it is treated for GloBE purposes:

| Entity Type | Location Rule |
|-------------|---------------|
| **Flow-through UPE** | Located where **created** |
| **Flow-through CE (with IIR obligation)** | Located where **created** |
| **Flow-through CE (no IIR obligation)** | **Stateless** — no location |
| **Reverse Hybrid Entity** | **Stateless** — separate calculation |

### 3.1 Stateless Treatment

A **Stateless Entity** is treated separately:
- Not part of any jurisdiction's ETR calculation
- No blending with other Constituent Entities
- Standalone ETR calculation
- If ETR < 15%, Top-Up Tax applies to that entity alone

## 4. Article 7.1: GloBE Income Reduction for Flow-Through UPEs

### 4.1 The Mechanism

When the UPE is a Flow-Through Entity, Article 7.1 allows the UPE to **reduce its GloBE Income** for income allocated to owners — but only where certain conditions are met.

```
┌─────────────────────────────────────────────────────────────────────┐
│ ARTICLE 7.1 INCOME REDUCTION MECHANISM                              │
│                                                                     │
│ Without Article 7.1:                                                │
│ ┌─────────────────────────────────────┐                            │
│ │ Flow-through UPE                    │                            │
│ │ GloBE Income: €10,000,000           │                            │
│ │ Covered Taxes: €0 (owners pay tax)  │                            │
│ │ ETR: 0%                             │◄──── Massive Top-Up Tax!   │
│ └─────────────────────────────────────┘                            │
│                                                                     │
│ With Article 7.1:                                                   │
│ ┌─────────────────────────────────────┐                            │
│ │ Flow-through UPE                    │                            │
│ │ GloBE Income: €10,000,000           │                            │
│ │ LESS: Income to qualifying owners   │                            │
│ │       (€9,000,000)                  │                            │
│ │ Adjusted GloBE Income: €1,000,000   │◄──── Reduced exposure      │
│ └─────────────────────────────────────┘                            │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Article 7.1.1: Conditions for Reduction

The UPE may reduce its GloBE Income by income attributable to an Ownership Interest held by a person that meets **any** of the following criteria:

| Paragraph | Condition | Examples |
|-----------|-----------|----------|
| **(a)** | Owner is subject to tax at a **nominal rate ≥ 15%** on the income | Corporate owner in 20% tax jurisdiction |
| **(b)** | Owner is an **Excluded Entity** or exempt for **legitimate policy reasons** | Pension funds, sovereign wealth funds, governmental entities |
| **(c)** | Owner holds **≤ 5% ownership interest** and receives income from instruments traded on a recognised exchange | Publicly traded units in a listed partnership |

### 4.3 Visual: Which Owners Qualify?

```
ARTICLE 7.1.1 QUALIFYING OWNERS

Owner Type                          Qualifies?     Reduction?
─────────────────────────────────────────────────────────────
Corporate (25% tax jurisdiction)    YES (a)        YES
Corporate (10% tax jurisdiction)    NO             NO
Pension fund (exempt)               YES (b)        YES
Sovereign wealth fund               YES (b)        YES
Government entity                   YES (b)        YES
Individual (30% marginal rate)      Depends        See below
Minority holder (≤5%, listed)       YES (c)        YES
Private equity fund (not exempt)    NO             NO
```

### 4.4 Individual Owners

For individuals, the nominal rate test (≥15%) is applied to the **owner's personal tax position**:
- If the individual is subject to tax at ≥15% on the flow-through income, reduction applies
- Tracking individual tax rates can be complex — document assumptions

## 5. Article 7.1.2: Covered Tax Reduction

When GloBE Income is reduced under Article 7.1.1, a **corresponding reduction** to Covered Taxes must also be made:

```
Covered Tax Reduction = Covered Taxes × (Income Reduction / Total GloBE Income)

EXAMPLE:
Flow-through UPE:
├── GloBE Income: €20,000,000
├── Covered Taxes: €400,000 (withholding taxes, etc.)
├── Income attributable to qualifying owners: €16,000,000 (80%)
│
├── Adjusted GloBE Income: €20,000,000 - €16,000,000 = €4,000,000
└── Adjusted Covered Taxes: €400,000 × (1 - 80%) = €80,000

Remaining ETR = €80,000 / €4,000,000 = 2.00%
```

**Why reduce Covered Taxes?** Any taxes paid by the UPE (e.g., withholding taxes) attributable to income allocated to owners should not be counted — otherwise the ETR calculation would be distorted.

## 6. Article 7.1.3: CFC Regime Consideration

If an owner is subject to a **Controlled Foreign Company (CFC) regime** that taxes the flow-through income:

- The CFC tax is treated as if levied on the owner
- The nominal rate condition (≥15%) may be satisfied by the CFC regime
- This prevents penalising structures where the owner's jurisdiction pulls income into tax via CFC rules

```
CFC REGIME EXAMPLE

Flow-through UPE (Cayman)
└── Owner: German GmbH

German CFC rules:
→ Germany imposes CFC taxation on Cayman UPE income
→ German CFC rate: 30%
→ Satisfies Article 7.1.1(a) — nominal rate ≥ 15%
→ UPE can reduce GloBE Income for German GmbH's share
```

## 7. Article 7.1.4: Extension to Permanent Establishments

If the Flow-through UPE conducts business through a **Permanent Establishment**:

- Article 7.1.4 extends the reduction mechanism to PEs
- Income allocated to qualifying owners through the PE can also be reduced
- This applies whether the PE is in the UPE's jurisdiction or a third country

```
PE EXTENSION EXAMPLE

Flow-through UPE (Delaware LP)
├── PE in UK (trading operations)
└── Owners: US corporations (25% tax)

Treatment:
→ UK PE income flows through to Delaware LP
→ Delaware LP allocates income to US corporate owners
→ US corporations pay US tax at 21%
→ Article 7.1.4 allows reduction for PE income allocated to qualifying owners
```

## 8. Worked Example: Standard Flow-Through UPE Analysis

### 8.1 Scenario

**Alpha Partners LP** is a Delaware limited partnership that serves as the UPE of a multinational group. The LP holds subsidiaries in Germany, Ireland, and Singapore.

### 8.2 Ownership Structure

```
ALPHA PARTNERS LP (Delaware)
├── 40% - Alpha Corp (US) — 21% US tax rate
├── 35% - PensionCo (US) — Tax-exempt pension fund
├── 15% - HedgeFund LP (Cayman) — Not subject to tax
└── 10% - Various individuals (publicly traded units)

Alpha Partners LP
├── 100% - Alpha Germany GmbH
├── 100% - Alpha Ireland Ltd
└── 100% - Alpha Singapore Pte
```

### 8.3 Step 1: Confirm Flow-Through UPE Status

| Criterion | Assessment |
|-----------|------------|
| Is LP fiscally transparent in Delaware? | Yes |
| Is LP the UPE of the MNE Group? | Yes |
| **Classification** | **Flow-through UPE** |
| **Location** | Delaware (jurisdiction of creation) |

### 8.4 Step 2: Identify Qualifying Owners Under Article 7.1.1

| Owner | Ownership | Article 7.1.1 Test | Qualifies? |
|-------|-----------|-------------------|------------|
| Alpha Corp (US) | 40% | (a) Nominal rate 21% ≥ 15% | **YES** |
| PensionCo | 35% | (b) Excluded Entity (pension fund) | **YES** |
| HedgeFund LP | 15% | Not subject to tax ≥ 15% | **NO** |
| Individuals | 10% | (c) ≤ 5% each, publicly traded | **YES** |

**Qualifying ownership:** 40% + 35% + 10% = **85%**
**Non-qualifying ownership:** 15%

### 8.5 Step 3: Calculate GloBE Income Reduction

**Alpha Partners LP financial data:**

| Item | Amount |
|------|--------|
| Gross GloBE Income | €50,000,000 |
| Covered Taxes (withholding) | €500,000 |

**Article 7.1 Reduction:**

```
Income Reduction = €50,000,000 × 85% = €42,500,000

Adjusted GloBE Income = €50,000,000 - €42,500,000 = €7,500,000

Covered Tax Reduction = €500,000 × 85% = €425,000

Adjusted Covered Taxes = €500,000 - €425,000 = €75,000
```

### 8.6 Step 4: Calculate ETR for Remaining Income

```
Remaining UPE ETR = €75,000 / €7,500,000 = 1.00%

ETR < 15% → Top-Up Tax applies to remaining 15% (HedgeFund LP share)
```

### 8.7 Step 5: Calculate Top-Up Tax

**SBIE for UPE (Delaware):**
- Assume minimal payroll and assets at UPE level
- SBIE = €0

**Top-Up Tax:**

```
Excess Profit = €7,500,000 - €0 = €7,500,000
Top-Up Tax % = 15% - 1% = 14%
UPE Top-Up Tax = €7,500,000 × 14% = €1,050,000
```

### 8.8 Step 6: Identify Who Bears Top-Up Tax

The Top-Up Tax on the UPE is attributable to the **non-qualifying owner** (HedgeFund LP):
- HedgeFund LP's share of income was not reduced
- IIR collection would depend on where qualified IIR applies in the chain
- If no IIR at UPE level (Delaware), UTPR may apply at subsidiary level

### 8.9 Summary: Alpha Partners LP Position

| Metric | Before Art. 7.1 | After Art. 7.1 |
|--------|----------------|----------------|
| GloBE Income | €50,000,000 | €7,500,000 |
| Covered Taxes | €500,000 | €75,000 |
| ETR | 1.00% | 1.00% |
| Excess Profit | €50,000,000 | €7,500,000 |
| **Top-Up Tax** | **€7,000,000** | **€1,050,000** |

**Observation:** Without Article 7.1, the full €50M income would be subject to Top-Up Tax at 14%, resulting in €7,000,000. Article 7.1 reduces this to €1,050,000 by excluding income attributable to qualifying owners.

## 9. Stratos Worked Example: Hypothetical Flow-Through Restructure

### 9.1 Background

Stratos Holdings plc (UK) is considering a restructure where a new **Stratos Partners LP** (Delaware) would become the UPE, with Stratos Holdings plc converting to a subsidiary.

### Proposed Structure

```
STRATOS PARTNERS LP (Delaware) — NEW UPE
├── 70% - Stratos Holdings plc (UK) — 25% UK tax
├── 20% - Institutional investors (pension funds)
└── 10% - Management (US individuals, 37% tax)
         │
         │ 100%
         ▼
    Stratos Holdings plc (UK)
         │
         ├── Stratos GmbH (Germany)
         ├── Stratos Asia Pte (Singapore)
         ├── Stratos Ireland Ltd (Ireland)
         └── Stratos Finance S.à r.l. (Luxembourg)
```

### Analysis: Article 7.1 Impact

| Owner | Ownership | Qualifies Under 7.1.1? | Basis |
|-------|-----------|----------------------|-------|
| Stratos Holdings plc | 70% | YES | (a) UK rate 25% ≥ 15% |
| Pension funds | 20% | YES | (b) Excluded Entities |
| Management | 10% | YES | (a) US rate 37% ≥ 15% |

**Result:** 100% of ownership qualifies under Article 7.1.1.

### GloBE Income Treatment

If all owners qualify, the Flow-through UPE can reduce its GloBE Income to **€0**:

```
Stratos Partners LP:
├── GloBE Income: €X (attributable to LP activities)
├── Reduction: €X × 100% = €X
└── Adjusted GloBE Income: €0

No Top-Up Tax at UPE level.
```

**However:** This only addresses tax at the **LP level**. The subsidiaries (Germany, Singapore, Ireland, Luxembourg) are still subject to standard GloBE calculations:
- Singapore: ETR 9.8% → Top-Up Tax applies (as before)
- Ireland: QDMTT applies (as before)
- Germany/Luxembourg: ETR ≥ 15% / De Minimis → No Top-Up Tax

### Key Insight

Converting to a Flow-through UPE does **not** eliminate Top-Up Tax on low-taxed subsidiaries. Article 7.1 only addresses the UPE's own GloBE Income position — it does not affect subsidiary ETR calculations.

## Interaction with IIR and UTPR

### IIR Application

A Flow-through UPE located in a jurisdiction with IIR must apply IIR on its subsidiaries:

```
SCENARIO: Flow-through UPE with IIR

Flow-through UPE (UK LP)
├── Treated as located in UK (jurisdiction of creation)
├── UK has IIR
└── UK LP must apply IIR on low-taxed subsidiaries

Top-Up Tax on subsidiaries:
→ Charged to UK LP via IIR
→ Even though LP is flow-through, it bears IIR liability
→ Economically passed through to partners
```

### UTPR Backstop

If the Flow-through UPE is in a jurisdiction **without IIR** (e.g., US pre-implementation):

```
SCENARIO: Flow-through UPE without IIR

Flow-through UPE (Delaware LP)
├── US has not implemented IIR (assumed)
├── Subsidiaries in Germany (IIR jurisdiction)
│
└── UTPR applies:
    → Germany can collect Top-Up Tax via UTPR
    → UTPR amount based on UTPR Percentage (employees/assets)
```

## 10. Comparison: Flow-Through UPE vs Standard UPE

| Feature | Standard UPE | Flow-through UPE |
|---------|--------------|------------------|
| **Taxation** | Entity-level tax | Pass-through to owners |
| **GloBE Income** | Full amount retained | Reduced under Art. 7.1 (if owners qualify) |
| **Location** | Jurisdiction of tax residence | Jurisdiction of creation |
| **ETR risk** | Based on entity's own taxes | Based on residual income (after reduction) |
| **IIR obligation** | Applies if jurisdiction has IIR | Applies if jurisdiction of creation has IIR |
| **Complexity** | Lower | Higher (owner-by-owner analysis) |

## 11. Common Pitfalls

### 11.1 Pitfall 1: Assuming Full Reduction Without Owner Analysis

**Error:** Reducing 100% of GloBE Income without confirming each owner meets Article 7.1.1 criteria.

**Correct approach:** Analyse **each** Ownership Interest separately. Only income attributable to qualifying owners can be reduced.

### 11.2 Pitfall 2: Ignoring Covered Tax Reduction

**Error:** Reducing GloBE Income but not making corresponding reduction to Covered Taxes.

**Correct approach:** Apply Article 7.1.2 to reduce Covered Taxes proportionally. Otherwise, ETR will be distorted.

### 11.3 Pitfall 3: Confusing Flow-Through UPE with Subsidiary Treatment

**Error:** Applying Article 7.1 to a flow-through entity that is not the UPE.

**Correct approach:** Article 7.1 applies **only** to the UPE. For other flow-through entities, standard allocation rules apply (income flows to Constituent Entity-owner).

### 11.4 Pitfall 4: Misidentifying Location

**Error:** Treating a Flow-through UPE as located where its owners are.

**Correct approach:** Flow-through UPE is located in the **jurisdiction where it was created** (e.g., Delaware for a Delaware LP).

### 11.5 Pitfall 5: Overlooking CFC Regime Impact

**Error:** Failing to consider whether owner's CFC regime satisfies the ≥15% test.

**Correct approach:** If owner is subject to CFC taxation on the flow-through income at ≥15%, the owner qualifies under Article 7.1.1(a).

### 11.6 Pitfall 6: Expecting UPE Restructure to Eliminate Subsidiary Top-Up Tax

**Error:** Restructuring to a flow-through UPE expecting to eliminate all Top-Up Tax.

**Correct approach:** Article 7.1 only addresses UPE-level income. Subsidiary ETR calculations remain unchanged. Low-taxed subsidiaries still face Top-Up Tax.

## 12. Flow-Through UPE Assessment Checklist

Use this checklist when evaluating a Flow-Through UPE:

```
FLOW-THROUGH UPE ASSESSMENT CHECKLIST
Entity: _________________________
Jurisdiction of Creation: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: FLOW-THROUGH STATUS CONFIRMATION
═══════════════════════════════════════════════════════════════════════

□ Is entity fiscally transparent in jurisdiction of creation?   YES / NO

   If NO: Not a Flow-through Entity. Standard UPE rules apply.

□ Is entity the UPE of the MNE Group?                           YES / NO

   If NO: Apply standard flow-through allocation rules (not Art. 7.1).

□ **CONCLUSION: Is this a Flow-through UPE?**                   YES / NO

□ Location for GloBE purposes: _________________________ (jurisdiction of creation)

═══════════════════════════════════════════════════════════════════════
SECTION B: OWNER ANALYSIS (ARTICLE 7.1.1)
═══════════════════════════════════════════════════════════════════════

For each owner, determine qualification:

OWNER 1:
□ Name: _________________________
□ Ownership %: _________________________
□ Jurisdiction: _________________________
□ Tax rate on flow-through income: _________%

□ Qualification test:
   □ (a) Nominal rate ≥ 15%?                                    YES / NO
   □ (b) Excluded Entity (pension fund, government, etc.)?      YES / NO
   □ (c) ≤ 5% ownership + publicly traded?                      YES / NO
   □ CFC regime applies at ≥ 15%?                               YES / NO

□ **OWNER 1 QUALIFIES?**                                        YES / NO

(Repeat for each owner)

SUMMARY OF OWNERS:
□ Total qualifying ownership:                                   _________%
□ Total non-qualifying ownership:                               _________%

═══════════════════════════════════════════════════════════════════════
SECTION C: GLOBE INCOME REDUCTION (ARTICLE 7.1.1)
═══════════════════════════════════════════════════════════════════════

□ UPE Gross GloBE Income:                               €__________________
□ Income attributable to qualifying owners:
   (Gross GloBE Income × Qualifying %)                  €__________________
□ **Income Reduction:**                                 €__________________

□ Adjusted GloBE Income:
   (Gross − Reduction)                                  €__________________

═══════════════════════════════════════════════════════════════════════
SECTION D: COVERED TAX REDUCTION (ARTICLE 7.1.2)
═══════════════════════════════════════════════════════════════════════

□ UPE Gross Covered Taxes:                              €__________________
□ Covered Tax Reduction:
   (Gross Covered Taxes × Qualifying %)                 €__________________
□ **Adjusted Covered Taxes:**                           €__________________

═══════════════════════════════════════════════════════════════════════
SECTION E: ETR AND TOP-UP TAX CALCULATION
═══════════════════════════════════════════════════════════════════════

□ Adjusted ETR:
   (Adjusted Covered Taxes ÷ Adjusted GloBE Income)     __________________%

   If ETR ≥ 15%: No Top-Up Tax for UPE. Proceed to subsidiaries.

□ Top-Up Tax %:
   (15% − Adjusted ETR)                                 __________________%

□ SBIE for UPE jurisdiction:                            €__________________

□ Excess Profit:
   (Adjusted GloBE Income − SBIE)                       €__________________

□ **UPE Top-Up Tax:**                                   €__________________

═══════════════════════════════════════════════════════════════════════
SECTION F: COLLECTION MECHANISM
═══════════════════════════════════════════════════════════════════════

□ Does UPE jurisdiction have IIR?                               YES / NO

   If YES: UPE applies IIR on low-taxed subsidiaries.
   If NO: UTPR may apply in subsidiary jurisdictions.

□ Does UPE jurisdiction have QDMTT?                             YES / NO

   If YES: QDMTT priority for UPE's own Top-Up Tax.

═══════════════════════════════════════════════════════════════════════
SECTION G: SUMMARY
═══════════════════════════════════════════════════════════════════════

□ UPE Gross GloBE Income:                               €__________________
□ Article 7.1 Reduction:                               (€__________________)
□ Adjusted GloBE Income:                                €__________________
□ Adjusted ETR:                                         __________________%
□ **UPE Top-Up Tax:**                                   €__________________

□ Attributable to non-qualifying owners (________%):    €__________________

□ Documentation of owner analysis complete?                     YES / NO
```
