# Chapter 8.1: STTR Design and Mechanics

## Learning Objective

After completing this chapter, you will be able to identify payments subject to the Subject to Tax Rule (STTR), calculate the adjusted nominal tax rate and STTR specified rate, apply the mark-up proxy to exclude low-risk transactions, and understand how STTR interacts with existing tax treaties and the GloBE Rules.

---

## Key References

**OECD Documents:**
- STTR Model Treaty Provision (July 2023)
- STTR Commentary (July 2023)
- Multilateral Convention to Implement the STTR (October 2023)
- OECD "Subject to Tax Rule in a Nutshell" (2023)

**Key Thresholds:**
- STTR minimum rate: **9%**
- Mark-up threshold: **8.5%** of costs
- Materiality threshold: **€1 million** (or €250,000 for smaller economies)

---

## Overview: STTR Within Pillar Two

The Subject to Tax Rule (STTR) is a **treaty-based rule** that complements the GloBE Rules. While the GloBE Rules operate through domestic legislation (IIR, UTPR, QDMTT), the STTR operates through **tax treaty modifications**.

```
┌─────────────────────────────────────────────────────────────────────┐
│ PILLAR TWO: TWO COMPLEMENTARY MECHANISMS                            │
│                                                                     │
│ ┌─────────────────────────────────┐ ┌─────────────────────────────┐ │
│ │       GloBE RULES               │ │       STTR                  │ │
│ │                                 │ │                             │ │
│ │ • Domestic legislation          │ │ • Treaty-based rule         │ │
│ │ • 15% minimum ETR               │ │ • 9% minimum nominal rate   │ │
│ │ • Jurisdictional blending       │ │ • Payment-by-payment        │ │
│ │ • All MNE income                │ │ • Specific covered payments │ │
│ │ • IIR/UTPR/QDMTT collection    │ │ • Source country collection │ │
│ │                                 │ │                             │ │
│ │ Applies to: All in-scope MNEs   │ │ Applies to: Treaty partners │ │
│ │ (€750M+ revenue)                │ │ (developing country request)│ │
│ └─────────────────────────────────┘ └─────────────────────────────┘ │
│                                                                     │
│ INTERACTION: STTR applies FIRST; STTR tax is creditable under GloBE │
└─────────────────────────────────────────────────────────────────────┘
```

### Why STTR Exists

The STTR addresses a specific concern of **developing countries**:

| Concern | STTR Response |
|---------|---------------|
| Developing countries often serve as **source** jurisdictions for payments | STTR grants source countries the right to "tax back" undertaxed payments |
| Existing treaties may limit withholding tax rates | STTR overrides treaty limits for covered payments |
| GloBE Rules primarily benefit **residence** jurisdictions (via IIR) | STTR ensures source countries capture some minimum tax |

---

## STTR Scope: Covered Income

### What Payments Are Covered?

The STTR applies to specific categories of **intra-group payments** when paid to connected persons in a jurisdiction with a nominal tax rate below 9%.

```
STTR COVERED INCOME TYPES

┌─────────────────────────────────────────────────────────────────────┐
│ CATEGORY 1: INTEREST                                                │
│                                                                     │
│ • All interest payments between connected persons                   │
│ • No mark-up threshold applies                                      │
│ • Subject only to materiality threshold                             │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ CATEGORY 2: ROYALTIES                                               │
│                                                                     │
│ • Payments for use of intellectual property                         │
│ • Patents, trademarks, copyrights, know-how                         │
│ • No mark-up threshold applies                                      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ CATEGORY 3: OTHER COVERED PAYMENTS                                  │
│                                                                     │
│ • Distribution rights payments                                      │
│ • Equipment rental (industrial, commercial, scientific)             │
│ • Service fees (intra-group services)                              │
│ • Insurance and reinsurance premiums                                │
│                                                                     │
│ Note: Mark-up threshold (8.5%) applies to these payments            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ NOT COVERED                                                         │
│                                                                     │
│ • Dividends                                                         │
│ • Capital gains                                                     │
│ • Business profits (other than above categories)                    │
│ • Payments to unconnected persons                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### Connected Persons Definition

The STTR applies only to payments between **connected persons**:

| Test | Threshold |
|------|-----------|
| **Direct ownership** | >50% of voting rights or capital |
| **Indirect ownership** | >50% through chain of entities |
| **Common control** | Both entities >50% owned by same person(s) |
| **De facto control** | Control as a matter of fact and circumstance |

**Example:**
```
Stratos Holdings plc (UK)
        │
        └── 100% owns SG Ireland Ltd
                    │
                    └── Pays royalties to SG Luxembourg S.à r.l.
                        (also 100% owned by Stratos)

Result: SG Ireland and SG Luxembourg are CONNECTED PERSONS
        → Royalty payment is within STTR scope
```

---

## The 9% Nominal Rate Threshold

### Adjusted Nominal Rate

The STTR applies when the **adjusted nominal tax rate** in the recipient jurisdiction is below **9%**.

```
ADJUSTED NOMINAL RATE CALCULATION

Step 1: Identify STATUTORY rate applicable to recipient
        → General corporate rate OR
        → Special rate for specific income type

Step 2: Adjust for PREFERENTIAL ADJUSTMENTS
        → Permanent reductions in taxable base
        → Special deductions or exemptions
        → IP box regimes with reduced rates

Step 3: Determine ADJUSTED NOMINAL RATE
        → Statutory rate × (1 - preferential adjustment %)

Step 4: Compare to 9% THRESHOLD
        → If < 9%: STTR potentially applies
        → If ≥ 9%: STTR does not apply
```

### Examples of Adjusted Nominal Rates

| Jurisdiction | Statutory Rate | Preferential Regime | Adjusted Nominal Rate | STTR Applies? |
|--------------|----------------|--------------------|-----------------------|---------------|
| Ireland | 12.5% | None | **12.5%** | No |
| Luxembourg | 24.94% | IP box (80% exemption) | **4.99%** | **Yes** |
| Netherlands | 25.8% | Innovation box (9% rate) | **9%** | Borderline |
| Singapore | 17% | Pioneer status (0%) | **0%** | **Yes** |
| Switzerland | 14% | Patent box (90% relief) | **1.4%** | **Yes** |
| UK | 25% | Patent box (10% rate) | **10%** | No |

### Preferential Adjustments

The adjusted nominal rate accounts for **preferential adjustments** that permanently reduce the tax base:

| Adjustment Type | Treatment |
|-----------------|-----------|
| **IP box/Patent box** | Apply reduced effective rate |
| **Participation exemption** | Not a preferential adjustment (applies to dividends, excluded from STTR) |
| **Accelerated depreciation** | Not preferential (timing difference) |
| **R&D super deduction** | Preferential if permanent |
| **Notional interest deduction** | Preferential adjustment |
| **Tax holidays** | Apply 0% rate for holiday period |

---

## STTR Specified Rate Calculation

When the STTR applies, the **source country** may impose additional tax up to the **specified rate**.

### Formula

```
STTR SPECIFIED RATE = 9% − Adjusted Nominal Rate − Existing Treaty WHT Rate

Where:
• 9% = STTR minimum rate
• Adjusted Nominal Rate = Rate in recipient jurisdiction
• Existing Treaty WHT = Withholding tax rate permitted under other treaty articles
```

### Worked Example: Royalty Payment

**Scenario:** SG Germany GmbH (source) pays €5 million royalties to SG Singapore Pte Ltd (recipient).

| Item | Value |
|------|-------|
| Singapore statutory rate | 17% |
| Singapore applies pioneer status to IP income | 0% effective rate |
| **Adjusted nominal rate** | **0%** |
| Germany-Singapore treaty WHT on royalties | 0% |
| | |
| **STTR specified rate** | 9% − 0% − 0% = **9%** |
| | |
| Royalty payment | €5,000,000 |
| **STTR tax (Germany collects)** | €5,000,000 × 9% = **€450,000** |

### Worked Example: Interest Payment with Existing WHT

**Scenario:** SG Ireland Ltd (source) pays €2 million interest to a Luxembourg financing entity.

| Item | Value |
|------|-------|
| Luxembourg statutory rate | 24.94% |
| Luxembourg applies participation exemption financing rules | 0% on intra-group interest |
| **Adjusted nominal rate** | **0%** |
| Ireland-Luxembourg treaty WHT on interest | 0% |
| | |
| **STTR specified rate** | 9% − 0% − 0% = **9%** |
| | |
| Interest payment | €2,000,000 |
| **STTR tax (Ireland collects)** | €2,000,000 × 9% = **€180,000** |

### Interaction with Existing WHT

If the existing treaty already permits withholding tax, the STTR **tops up** to 9%:

**Example:** Source country treaty permits 5% WHT on royalties; recipient nominal rate is 2%.

```
STTR specified rate = 9% − 2% − 5% = 2%

Result: Source country can impose:
• 5% under existing treaty Article
• 2% additional under STTR
• Total: 7% (not 9%, because treaty already permits 5%)

Wait — let's recalculate:
The STTR allows collection of the DIFFERENCE between 9% and the sum of:
- Adjusted nominal rate (2%)
- Existing WHT under treaty (5%)

STTR specified rate = 9% − 2% − 5% = 2%

Source country total collection:
• 5% (existing treaty) + 2% (STTR) = 7%

Note: If treaty already permits 5% WHT, total tax is 5% + 2% = 7%
      This is because the payment is subject to 5% + 2% = 7% total
      The remaining 2% is subject to nominal rate (2%), so total = 9%
```

Actually, let me clarify the STTR mechanism more precisely:

```
STTR COLLECTION MECHANISM

The STTR specified rate represents the ADDITIONAL tax the source
country may impose BEYOND what it can already collect under the treaty.

If:
• Adjusted nominal rate in recipient = 2%
• Existing treaty WHT permitted = 5%
• Combined: 2% + 5% = 7%

STTR allows source country to top up to 9%:
• STTR specified rate = 9% − 2% − 5% = 2%

Source country collects:
• 5% under treaty + 2% under STTR = 7%

Recipient bears:
• 2% domestic tax + 7% source WHT = 9% total

The 9% minimum is achieved through combination of:
1. Recipient jurisdiction tax
2. Source jurisdiction WHT under treaty
3. Source jurisdiction STTR top-up
```

---

## Mark-up Proxy: Substantial Activities Test

### Purpose

The **mark-up threshold** excludes low-margin payments from the STTR, serving as a proxy for **substantial activities**. If the recipient earns only a modest return, the BEPS risk is considered limited.

### Application

```
MARK-UP THRESHOLD

Applies to: Service fees, equipment rental, distribution rights
Does NOT apply to: Interest, royalties

Test: Is the gross income > (Costs + 8.5% of Costs)?

If YES: Mark-up exceeds threshold → STTR may apply
If NO:  Mark-up within threshold → STTR does NOT apply
```

### Calculation

```
MARK-UP THRESHOLD CALCULATION

Step 1: Identify GROSS INCOME from covered payment
        → Total payment received

Step 2: Identify ATTRIBUTABLE COSTS
        → Direct costs of earning the income
        → Indirect costs reasonably attributable

Step 3: Calculate THRESHOLD AMOUNT
        → Costs + (Costs × 8.5%)
        → = Costs × 1.085

Step 4: Apply TEST
        → If Gross Income > Threshold: STTR may apply
        → If Gross Income ≤ Threshold: STTR does not apply
```

### Worked Example: Service Fee

**Scenario:** SG Singapore Pte Ltd provides management services to SG Ireland Ltd.

| Item | Amount |
|------|--------|
| Service fee received | €1,200,000 |
| Direct costs (personnel, travel) | €800,000 |
| Indirect costs (allocated overhead) | €200,000 |
| **Total attributable costs** | **€1,000,000** |
| | |
| **Threshold calculation** | €1,000,000 × 1.085 = €1,085,000 |
| | |
| **Test:** Is €1,200,000 > €1,085,000? | **Yes** |
| **Mark-up:** (€1,200,000 − €1,000,000) / €1,000,000 | **20%** |
| | |
| **Result:** Mark-up (20%) exceeds 8.5% → **STTR may apply** |

### Worked Example: Low-Margin Service

**Scenario:** Same service, but lower fee.

| Item | Amount |
|------|--------|
| Service fee received | €1,050,000 |
| Total attributable costs | €1,000,000 |
| | |
| **Threshold calculation** | €1,000,000 × 1.085 = €1,085,000 |
| | |
| **Test:** Is €1,050,000 > €1,085,000? | **No** |
| **Mark-up:** (€1,050,000 − €1,000,000) / €1,000,000 | **5%** |
| | |
| **Result:** Mark-up (5%) within 8.5% → **STTR does NOT apply** |

### Summary: Mark-up Threshold

| Payment Type | Mark-up Threshold Applies? |
|--------------|---------------------------|
| Interest | **No** |
| Royalties | **No** |
| Service fees | **Yes** (8.5%) |
| Equipment rental | **Yes** (8.5%) |
| Distribution rights | **Yes** (8.5%) |
| Insurance premiums | **Yes** (8.5%) |

---

## Materiality Threshold

### De Minimis Exclusion

The STTR includes a **materiality threshold** to exclude small payments:

| Source Country GDP | Materiality Threshold |
|-------------------|----------------------|
| ≥ €40 billion | **€1,000,000** per year |
| < €40 billion | **€250,000** per year |

### Application

The threshold applies to the **aggregate** of all covered payments from the source country to connected persons in the recipient jurisdiction during the fiscal year.

**Example:**
```
SG Germany GmbH makes the following payments to SG Singapore Pte Ltd:

• Royalties: €400,000
• Service fees: €300,000
• Interest: €200,000
• Total covered income: €900,000

Germany GDP: > €40 billion → Threshold: €1,000,000

Result: Total (€900,000) < Threshold (€1,000,000)
        → STTR does NOT apply to any payments
```

---

## Treaty Interaction

### STTR and Existing Treaty Articles

The STTR operates as a **new article** inserted into existing bilateral tax treaties. It does not replace existing provisions but adds an additional taxing right.

```
TREATY STRUCTURE WITH STTR

Existing Treaty Articles:
├── Article 11: Interest (e.g., 10% WHT limit)
├── Article 12: Royalties (e.g., 5% WHT limit)
├── Article 13: Service fees (often no WHT)
│
NEW STTR Article:
└── Article XX: Subject to Tax Rule
    → Allows source country to impose additional tax
    → Up to STTR specified rate
    → On covered income taxed below 9% in recipient country
```

### Priority Rules

```
STTR PRIORITY AND INTERACTION

1. EXISTING TREATY RIGHTS PRESERVED
   → Source country retains any existing WHT rights
   → STTR tops up to 9%, not replaces

2. STTR vs GloBE RULES
   → STTR applies FIRST (treaty level)
   → STTR tax is CREDITABLE under GloBE Rules
   → Reduces GloBE Top-up Tax liability

3. STTR vs QDMTT
   → STTR tax reduces income for QDMTT purposes
   → No double counting

EXAMPLE:
Payment: €10 million royalty
STTR tax collected by source: €900,000 (9%)

For GloBE purposes:
• Recipient includes €10 million income
• Credits €900,000 STTR as covered tax
• ETR increased by STTR credit
```

### GloBE Interaction Example

**Before STTR:**
```
Recipient jurisdiction (Singapore, 0% on IP income):
GloBE Income: €10,000,000
Covered Taxes: €0
ETR: 0%
Top-up Tax %: 15%
Top-up Tax: €10,000,000 × 15% = €1,500,000 (to UPE jurisdiction)
```

**After STTR:**
```
Source jurisdiction collects STTR: €900,000

Recipient jurisdiction (Singapore):
GloBE Income: €10,000,000
Covered Taxes: €900,000 (STTR credit)
ETR: 9%
Top-up Tax %: 6%
Top-up Tax: €10,000,000 × 6% = €600,000 (to UPE jurisdiction)

Total tax on payment:
• STTR (source): €900,000
• GloBE Top-up (UPE): €600,000
• Total: €1,500,000 (15% effective rate achieved)
```

---

## STTR Impact Assessment Framework

### Step-by-Step Assessment

```
STTR IMPACT ASSESSMENT FRAMEWORK

For each intercompany payment:

┌─────────────────────────────────────────────────────────────────────┐
│ STEP 1: IS THE PAYMENT COVERED INCOME?                              │
│                                                                     │
│ □ Interest                           → YES (proceed)               │
│ □ Royalties                          → YES (proceed)               │
│ □ Service fees                       → YES (proceed)               │
│ □ Equipment rental                   → YES (proceed)               │
│ □ Distribution rights                → YES (proceed)               │
│ □ Insurance premiums                 → YES (proceed)               │
│ □ Dividends                          → NO (STTR does not apply)    │
│ □ Other                              → NO (STTR does not apply)    │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 2: ARE THE PARTIES CONNECTED?                                  │
│                                                                     │
│ □ >50% common ownership?             → YES (connected)             │
│ □ Common control?                    → YES (connected)             │
│ □ Neither                            → NO (STTR does not apply)    │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 3: DOES THE MATERIALITY THRESHOLD APPLY?                       │
│                                                                     │
│ Total covered payments to recipient jurisdiction: €__________       │
│ Source country GDP ≥ €40B?           → Threshold: €1,000,000       │
│ Source country GDP < €40B?           → Threshold: €250,000         │
│                                                                     │
│ Total < Threshold?                   → NO (STTR does not apply)    │
│ Total ≥ Threshold?                   → YES (proceed)               │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 4: DOES THE MARK-UP THRESHOLD APPLY? (Services/Rental only)    │
│                                                                     │
│ For interest/royalties: SKIP (no mark-up test)                      │
│                                                                     │
│ For services/rental:                                                │
│ Gross income: €__________                                           │
│ Attributable costs: €__________                                     │
│ Threshold (costs × 1.085): €__________                              │
│                                                                     │
│ Gross income ≤ Threshold?            → NO (STTR does not apply)    │
│ Gross income > Threshold?            → YES (proceed)               │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 5: WHAT IS THE ADJUSTED NOMINAL RATE?                          │
│                                                                     │
│ Recipient jurisdiction statutory rate: _______%                     │
│ Preferential adjustment (if any): _______%                          │
│ Adjusted nominal rate: _______%                                     │
│                                                                     │
│ Adjusted nominal rate ≥ 9%?          → NO (STTR does not apply)    │
│ Adjusted nominal rate < 9%?          → YES (proceed)               │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 6: CALCULATE STTR SPECIFIED RATE                               │
│                                                                     │
│ STTR specified rate = 9% − Adjusted nominal rate − Existing WHT     │
│                                                                     │
│ = 9% − _______% − _______% = _______%                               │
│                                                                     │
│ STTR TAX = Payment amount × Specified rate                          │
│          = €__________ × _______% = €__________                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stratos Worked Example: STTR Assessment

### Background

Stratos Holdings plc assesses STTR exposure on intercompany payments for FY 2025.

### Intercompany Payment Matrix

| Payer | Recipient | Payment Type | Amount (€) | Notes |
|-------|-----------|--------------|------------|-------|
| SG Germany | SG Singapore | Royalties | 2,500,000 | IP licence |
| SG Ireland | SG Luxembourg | Interest | 3,000,000 | Intercompany loan |
| SG Germany | SG Ireland | Service fees | 1,800,000 | Shared services |
| SG UK | SG Singapore | Distribution rights | 800,000 | Product distribution |

### Assessment 1: Royalties (Germany → Singapore)

| Step | Assessment |
|------|------------|
| **1. Covered income?** | Royalties → **Yes** |
| **2. Connected persons?** | Both 100% owned by Stratos → **Yes** |
| **3. Materiality?** | €2.5M > €1M (Germany GDP > €40B) → **Exceeds** |
| **4. Mark-up threshold?** | N/A for royalties |
| **5. Adjusted nominal rate?** | Singapore 17%, but 0% under pioneer status → **0%** |
| **6. STTR specified rate?** | 9% − 0% − 0% (no treaty WHT) = **9%** |

**STTR Tax:** €2,500,000 × 9% = **€225,000** (collected by Germany)

### Assessment 2: Interest (Ireland → Luxembourg)

| Step | Assessment |
|------|------------|
| **1. Covered income?** | Interest → **Yes** |
| **2. Connected persons?** | Both 100% owned by Stratos → **Yes** |
| **3. Materiality?** | €3M > €1M (Ireland GDP > €40B) → **Exceeds** |
| **4. Mark-up threshold?** | N/A for interest |
| **5. Adjusted nominal rate?** | Luxembourg 24.94% general, but IP financing regime 0% → **0%** |
| **6. STTR specified rate?** | 9% − 0% − 0% = **9%** |

**STTR Tax:** €3,000,000 × 9% = **€270,000** (collected by Ireland)

### Assessment 3: Service Fees (Germany → Ireland)

| Step | Assessment |
|------|------------|
| **1. Covered income?** | Service fees → **Yes** |
| **2. Connected persons?** | Both 100% owned by Stratos → **Yes** |
| **3. Materiality?** | €1.8M > €1M → **Exceeds** |
| **4. Mark-up threshold?** | Gross: €1.8M; Costs: €1.5M; Threshold: €1.6275M → **Exceeds 8.5%** |
| **5. Adjusted nominal rate?** | Ireland 12.5% → **≥ 9%** |
| **6. STTR?** | **Does NOT apply** (rate ≥ 9%) |

**STTR Tax:** €0

### Assessment 4: Distribution Rights (UK → Singapore)

| Step | Assessment |
|------|------------|
| **1. Covered income?** | Distribution rights → **Yes** |
| **2. Connected persons?** | Both 100% owned by Stratos → **Yes** |
| **3. Materiality?** | €800,000 < €1M → **Below threshold** |
| **4. STTR?** | **Does NOT apply** (materiality not met) |

**STTR Tax:** €0

### Summary: Stratos STTR Exposure

| Payment | Payer | Recipient | STTR Tax (€) | Collecting Jurisdiction |
|---------|-------|-----------|--------------|------------------------|
| Royalties | Germany | Singapore | **225,000** | Germany |
| Interest | Ireland | Luxembourg | **270,000** | Ireland |
| Services | Germany | Ireland | 0 | — |
| Distribution | UK | Singapore | 0 | — |
| **Total** | | | **€495,000** | |

### GloBE Impact

The STTR taxes increase Covered Taxes in the recipient jurisdictions:

| Jurisdiction | Pre-STTR Covered Taxes | STTR Credit | Post-STTR Covered Taxes |
|--------------|----------------------|-------------|------------------------|
| Singapore | €392,206 | +€225,000 | **€617,206** |
| Luxembourg | €212,500 | +€270,000 | **€482,500** |

**Singapore ETR Impact:**
- Pre-STTR: €392,206 / €4,000,000 = 9.81%
- Post-STTR: €617,206 / €4,000,000 = **15.43%** (above 15% minimum!)

**Result:** Singapore no longer generates GloBE Top-up Tax after STTR credit.

---

## Common Pitfalls

### Pitfall 1: Ignoring Preferential Regimes

**Error:** Assuming the statutory rate is the adjusted nominal rate.

**Correct approach:** Identify all preferential adjustments (IP boxes, tax holidays, notional deductions) that reduce the effective rate on the specific payment.

### Pitfall 2: Applying Mark-up Test to Interest/Royalties

**Error:** Excluding interest or royalty payments because the mark-up is below 8.5%.

**Correct approach:** The mark-up threshold does **not apply** to interest and royalties. These payments are subject to STTR regardless of the margin.

### Pitfall 3: Forgetting Materiality Aggregation

**Error:** Testing each payment individually against the materiality threshold.

**Correct approach:** Aggregate **all** covered payments from the source country to connected persons in the recipient jurisdiction. Test the total against the threshold.

### Pitfall 4: Double-Counting STTR in GloBE

**Error:** Not crediting STTR tax as Covered Taxes under GloBE.

**Correct approach:** STTR taxes paid are creditable under the GloBE Rules. They increase Covered Taxes and thus increase the ETR in the recipient jurisdiction.

### Pitfall 5: Assuming STTR Applies to All Treaties

**Error:** Calculating STTR exposure without confirming the treaty has been modified.

**Correct approach:** STTR only applies if the relevant bilateral treaty has been amended (via MLI or bilateral negotiation) to include the STTR provision. Check implementation status.

---

## STTR Assessment Checklist

```
STTR ASSESSMENT CHECKLIST
MNE Group: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: IDENTIFY INTERCOMPANY PAYMENTS
═══════════════════════════════════════════════════════════════════════

List all intercompany payments between connected group entities:

| # | Payer | Recipient | Type | Amount (€) |
|---|-------|-----------|------|------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

═══════════════════════════════════════════════════════════════════════
SECTION B: FILTER FOR STTR SCOPE
═══════════════════════════════════════════════════════════════════════

For each payment:

□ Is payment type covered? (Interest/Royalty/Service/Rental/Distribution)
□ Are parties connected? (>50% common ownership)
□ Is relevant treaty modified to include STTR?

═══════════════════════════════════════════════════════════════════════
SECTION C: AGGREGATE BY RECIPIENT JURISDICTION
═══════════════════════════════════════════════════════════════════════

| Recipient Jurisdiction | Total Covered Payments (€) | Materiality Threshold (€) | Exceeds? |
|------------------------|---------------------------|--------------------------|----------|
| | | | |
| | | | |

═══════════════════════════════════════════════════════════════════════
SECTION D: APPLY MARK-UP TEST (Services/Rental Only)
═══════════════════════════════════════════════════════════════════════

| Payment | Gross (€) | Costs (€) | Threshold (€) | Mark-up % | Applies? |
|---------|-----------|-----------|---------------|-----------|----------|
| | | | | | |

═══════════════════════════════════════════════════════════════════════
SECTION E: DETERMINE ADJUSTED NOMINAL RATES
═══════════════════════════════════════════════════════════════════════

| Recipient Jurisdiction | Statutory Rate | Preferential Regime | Adjusted Rate | < 9%? |
|------------------------|----------------|--------------------|--------------:|-------|
| | | | | |

═══════════════════════════════════════════════════════════════════════
SECTION F: CALCULATE STTR TAX
═══════════════════════════════════════════════════════════════════════

| Payment | Amount (€) | Adj. Nom. Rate | Treaty WHT | Specified Rate | STTR Tax (€) |
|---------|------------|----------------|------------|----------------|--------------|
| | | | | | |

TOTAL STTR EXPOSURE: €__________________

═══════════════════════════════════════════════════════════════════════
SECTION G: GloBE IMPACT
═══════════════════════════════════════════════════════════════════════

| Recipient Jurisdiction | Pre-STTR ETR | STTR Credit (€) | Post-STTR ETR |
|------------------------|--------------|-----------------|---------------|
| | | | |

□ STTR credits recorded as Covered Taxes in GloBE calculation
```

---

## Summary

The Subject to Tax Rule (STTR) is a treaty-based mechanism that:

| Aspect | STTR Rule |
|--------|-----------|
| **Minimum rate** | 9% (nominal, not ETR) |
| **Covered payments** | Interest, royalties, services, rental, distribution rights |
| **Excluded** | Dividends, capital gains |
| **Connected persons** | >50% common ownership |
| **Materiality** | €1M (or €250K for smaller economies) |
| **Mark-up threshold** | 8.5% (services/rental only; not interest/royalties) |
| **Collection** | Source country (payor jurisdiction) |
| **GloBE interaction** | STTR tax is creditable as Covered Tax |

**Key points:**
- STTR is **treaty-based** — requires treaty modification to apply
- Designed to benefit **developing countries** (source jurisdictions)
- **Complements** GloBE Rules — applies first, then credits to GloBE
- Adjusted nominal rate accounts for **preferential regimes**
- **Mark-up threshold** excludes low-margin services (8.5%)

---

## Integration with GloBE Calculations

When preparing GloBE calculations, account for STTR:

```
GloBE CALCULATION WITH STTR

Step 1: Identify potential STTR exposure
        → Use STTR Assessment Framework

Step 2: Calculate STTR taxes payable
        → By source jurisdiction

Step 3: Credit STTR to recipient jurisdiction
        → Add to Covered Taxes in GloBE Income calculation

Step 4: Recalculate ETR
        → Higher ETR due to STTR credit

Step 5: Calculate Top-up Tax
        → Reduced (or eliminated) by STTR credit

EXAMPLE:
Pre-STTR: Singapore ETR 9.81% → 5.19% Top-up Tax
Post-STTR: Singapore ETR 15.43% → 0% Top-up Tax (ETR ≥ 15%)
```

---

## Next Step

You have learned the design and mechanics of the Subject to Tax Rule. Proceed to **Chapter 8.2: STTR Implementation** to understand the Multilateral Convention approach, bilateral treaty modification process, and current jurisdiction adoption status.
