# Chapter 4.5: Tax Allocation Between Entities

## Learning Objective

After completing this chapter, you will be able to allocate Covered Taxes between Constituent Entities using the Article 4.3 framework, including PE tax allocation, CFC tax push-down with passive income limitation, hybrid entity allocations, and distribution tax reallocation.

## 1. When Tax Allocation Is Required

Article 4.3 requires tax allocation in five scenarios:

| Scenario | Article | Direction of Allocation |
|----------|---------|------------------------|
| **PE income** | 4.3.2(a)-(b) | Main Entity → PE |
| **CFC regimes** | 4.3.2(c) | Parent → CFC subsidiary |
| **Hybrid entities** | 4.3.2(d) | Owner → Hybrid Entity |
| **Reverse hybrids** | 4.3.2(d) | Treated separately |
| **Distributions** | 4.3.2(e) | Recipient → Distributor |

**Core principle:** Tax follows income. If Income is allocated to Entity B for GloBE purposes, the tax on that income should also be in Entity B's Covered Taxes.

## 2. PE Tax Allocation (Article 4.3.2(a)-(b))

### 2.1 The Issue

When a Constituent Entity operates through a foreign PE:
- The PE is treated as a **separate Constituent Entity** for GloBE
- The PE's income is included in the PE's jurisdiction
- But the **Main Entity** may pay tax on the PE income in its home jurisdiction

### 2.2 The Allocation Mechanism

**Step 1:** Identify the PE's share of the Main Entity's taxable income
- Extract from corporate tax return workings
- Use the income attribution to the PE

**Step 2:** Calculate the Main Entity's tax liability on PE income
- If PE income is taxed at a separate rate: Use that rate
- If blended: Allocate proportionally based on PE income share

**Step 3:** Push down the allocated tax
- Remove from Main Entity's Covered Taxes
- Add to PE's Covered Taxes

### 2.3 Allocation Formula

```
Tax Allocated to PE = Main Entity's Tax × (PE Taxable Income ÷ Total Taxable Income)
```

### 2.4 Worked Example: UK Company with German PE

```
Stratos Holdings plc (UK):
  Total taxable income:       €50,000,000
  Income attributable to German PE: €8,000,000
  UK corporate tax at 25%:    €12,500,000

Tax Allocation:
  PE share = €8,000,000 ÷ €50,000,000 = 16%
  Tax to PE = €12,500,000 × 16% = €2,000,000

Result:
  UK Main Entity Covered Taxes:  €12,500,000 - €2,000,000 = €10,500,000
  German PE Covered Taxes:       +€2,000,000 (added to any German tax)
```

### 2.5 PE Loss Scenario (Article 4.3.4)

When a PE has a GloBE Loss:
- The loss may be treated as an expense of the Main Entity (per Article 3.4.5)
- Subsequent PE income is allocated to the Main Entity until the loss is recaptured
- Associated Covered Taxes are also allocated to the Main Entity

**Cap:** Tax allocated to Main Entity cannot exceed:
```
PE Income × Highest Corporate Rate in PE Jurisdiction
```

## 3. CFC Tax Push-Down (Article 4.3.2(c))

### 2.1 The Issue

When a Parent Entity pays CFC tax on a subsidiary's undistributed income:
- Parent records the CFC tax in its accounts
- But the income remains in the CFC's jurisdiction for GloBE

### 3.2 The Three-Step Push-Down

**Step 1:** Identify CFC tax in Parent's current tax expense
- UK CFC charge
- US Subpart F / GILTI (special rules apply)
- Other CFC regimes

**Step 2:** Determine the CFC to which the income relates
- Match CFC tax to specific subsidiary
- For blended regimes (GILTI), use allocation rules

**Step 3:** Push down the tax
- Remove from Parent's Covered Taxes
- Add to CFC's Covered Taxes
- Apply Passive Income Limitation (Article 4.3.3)

### 3.3 Allocation Diagram

```
BEFORE PUSH-DOWN:
┌─────────────────────────────────────┐
│ Parent Co (UK)                      │
│ ├── Own tax: €5,000,000             │
│ └── CFC tax on Sub: €400,000        │ ← Tax here
│     Total: €5,400,000               │
└─────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│ Sub Co (Singapore)                  │
│ ├── Local tax: €200,000             │
│ └── CFC tax: €0                     │
│     Income: €5,000,000              │ ← Income here
│     ETR: 4.0%                       │
└─────────────────────────────────────┘

AFTER PUSH-DOWN:
┌─────────────────────────────────────┐
│ Parent Co (UK)                      │
│ └── Own tax: €5,000,000             │
│     (CFC tax removed: -€400,000)    │
└─────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│ Sub Co (Singapore)                  │
│ ├── Local tax: €200,000             │
│ └── Pushed CFC tax: +€400,000       │ ← Tax pushed here
│     Total: €600,000                 │
│     Income: €5,000,000              │
│     ETR: 12.0%                      │ ← Higher ETR
└─────────────────────────────────────┘
```

## 4. Passive Income Limitation (Article 4.3.3)

### 4.1 Why the Limitation Exists

Without a cap, a high-tax parent could push down excessive CFC tax to eliminate all Top-Up Tax in a low-tax subsidiary—defeating the purpose of GloBE.

### 4.2 The Formula

For **passive income** only, the push-down is limited to the **lesser of:**

```
(a) Actual CFC tax on the passive income
(b) Top-Up Tax % × Passive Income taxed under CFC regime
```

Where:
- **Top-Up Tax %** = 15% − CFC's ETR (before push-down)
- **Passive Income** = Dividends, interest, royalties, rent, annuities, certain gains

### 4.3 Step-by-Step Application

**Step 1:** Calculate CFC's ETR before any push-down
```
Pre-push ETR = CFC's Local Tax ÷ CFC's GloBE Income
```

**Step 2:** Determine Top-Up Tax Percentage
```
Top-Up Tax % = 15% − Pre-push ETR
```

**Step 3:** Calculate the cap
```
Cap = Top-Up Tax % × Passive Income under CFC regime
```

**Step 4:** Apply limitation
```
Push-down Amount = MIN(Actual CFC Tax, Cap)
```

### 2.4 Worked Example

```
SG Singapore Pte Ltd:
  GloBE Income: €5,000,000
  Local Singapore tax: €250,000 (5% ETR)

  Passive income taxed under UK CFC: €2,000,000
  UK CFC tax on passive income: €500,000 (25%)

Step 1: Pre-push ETR = €250,000 ÷ €5,000,000 = 5%

Step 2: Top-Up Tax % = 15% − 5% = 10%

Step 3: Cap = 10% × €2,000,000 = €200,000

Step 4: Push-down = MIN(€500,000, €200,000) = €200,000

Result:
  Only €200,000 pushed to Singapore (not €500,000)
  Remaining €300,000 stays in UK Parent's Covered Taxes

  Singapore post-push ETR:
    (€250,000 + €200,000) ÷ €5,000,000 = 9.0%
    Still below 15% → Top-Up Tax still applies
```

### 4.5 What Constitutes Passive Income

| Category | Examples |
|----------|----------|
| Dividends | Portfolio dividends, deemed dividends |
| Interest | Loan interest, bond interest |
| Royalties | IP licensing fees |
| Rent | Property rental income |
| Annuities | Structured payments |
| Gains | Gains on assets producing above income |

**Note:** Active business income is NOT subject to the passive income limitation—full push-down is permitted.

## 5. Hybrid Entity Allocations (Article 4.3.2(d))

### 5.1 Tax Transparent Entity (Owner Taxed)

When the owner is taxed on the hybrid's income:
- Owner's tax on hybrid income → Push down to hybrid entity

**Same three-step process as CFC push-down:**
1. Identify owner's tax on hybrid income
2. Allocate to hybrid entity
3. Apply passive income limitation

### 5.2 Reverse Hybrid Entity (Entity Taxed)

When the entity is taxed but treated as transparent by owner:
- Tax stays with the entity
- No push-down required (entity already has the tax)

### 5.3 Allocation Example

```
US Parent owns 100% of Luxembourg SCS (hybrid):
  Luxembourg treats SCS as transparent → No Luxembourg tax
  US treats SCS as corporation → US taxes SCS income

US Parent:
  Tax on SCS income: €600,000

Allocation:
  Push €600,000 to Luxembourg SCS
  Apply passive income limitation if applicable

Result:
  Luxembourg SCS Covered Taxes: +€600,000
  US Parent Covered Taxes: -€600,000
```

## 6. Distribution Tax Allocation (Article 4.3.2(e))

### 6.1 The Rule

Withholding tax on dividends paid from one CE to another is allocated to the **distributing entity**, not the recipient.

### 6.2 Rationale

The distribution relates to profits of the distributor. Allocating the withholding tax to the distributor's Covered Taxes ensures the tax is matched with the income.

### 6.3 Allocation Mechanism

```
Recipient Entity (receives dividend):
  Gross dividend: €1,000,000
  Withholding tax: €150,000 (15%)
  Net received: €850,000

  Financial accounts show: WHT expense €150,000

GloBE Allocation:
  Remove €150,000 from Recipient's Covered Taxes
  Add €150,000 to Distributor's Covered Taxes
```

### 6.4 Deemed Distributions

Per Administrative Guidance (AG 2.6), the same rule applies to deemed distributions:
- If ownership interest is treated as equity for:
  - Tax purposes in the jurisdiction imposing tax, AND
  - Financial accounting purposes
- Then the tax is allocated to the distributing entity

### 6.5 Impact on ETR

**For Distributor:**
- Covered Taxes increase
- ETR increases
- Top-Up Tax exposure decreases

**For Recipient:**
- Covered Taxes decrease
- But dividend is likely excluded income under Article 3.2.1(b)
- Net effect: neutral (both numerator and denominator reduced)

## 7. Cross-Crediting Systems (June 2024 Guidance)

### 7.1 The Four-Step Formula

For jurisdictions with foreign tax credit systems allowing cross-crediting:

**Step 1:** Determine foreign-source income
- Income treated as foreign source under domestic rules

**Step 2:** Calculate tax on foreign-source income
- Apply allocation formula based on income categories

**Step 3:** Determine excess FTC limitation
- Compare FTCs allowed vs. used

**Step 4:** Allocate residual tax
- Push down based on entity-by-entity income shares

### 7.2 Basket Approach

If the jurisdiction uses multiple FTC baskets:
- Apply the four-step formula separately for each basket
- Common baskets: General, Passive, GILTI (US)

### 7.3 GILTI Exception

**Important:** The June 2024 formula does NOT apply to US GILTI.

GILTI uses the temporary allocation rule from February 2023:
- Allocate GILTI tax based on each CFC's share of tested income
- Apply passive income limitation separately

## 8. Deferred Tax Allocation

### 8.1 Five-Step Formula (June 2024 Guidance)

For deferred tax push-down to CFCs:

**Step 1:** Identify deferred tax attributable to CFC income

**Step 2:** Determine the CFC's share of deferred tax

**Step 3:** Calculate GloBE-adjusted deferred tax (15% cap)

**Step 4:** Apply passive income limitation

**Step 5:** Allocate to CFC's Adjusted Covered Taxes

### 8.2 Five-Year Election (Article 4.3.2)

An MNE can elect to **exclude** deferred tax allocations for a jurisdiction:
- Election is made on jurisdictional basis
- Deferred tax is excluded from both:
  - The CE receiving the allocation
  - The parent/main entity making the allocation
- Simplifies compliance but may affect ETR adversely

## 9. Tax Allocation Decision Flowchart

```
                           START
                             │
                             ▼
              ┌──────────────────────────────┐
              │  What type of tax requires   │
              │  allocation?                 │
              └──────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┬─────────────────┐
         │                   │                   │                 │
         ▼                   ▼                   ▼                 ▼
    ┌─────────┐        ┌─────────┐        ┌──────────┐      ┌───────────┐
    │ PE Tax  │        │ CFC Tax │        │ Hybrid   │      │ WHT on    │
    │         │        │         │        │ Entity   │      │ Dividend  │
    └─────────┘        └─────────┘        └──────────┘      └───────────┘
         │                   │                   │                 │
         ▼                   ▼                   ▼                 ▼
    ┌─────────┐        ┌─────────────┐    ┌──────────┐      ┌───────────┐
    │ Push to │        │ Is income   │    │ Push to  │      │ Push to   │
    │ PE      │        │ PASSIVE?    │    │ Hybrid   │      │ DISTRIB-  │
    │         │        └─────────────┘    │ Entity   │      │ UTOR      │
    └─────────┘              │            └──────────┘      └───────────┘
                    ┌────────┴────────┐          │
                   YES               NO          │
                    │                 │          │
                    ▼                 ▼          ▼
             ┌───────────┐    ┌───────────┐    Apply
             │ Apply     │    │ Full      │    Art. 4.3.3
             │ Art. 4.3.3│    │ push-down │    if passive
             │ Limitation│    │ permitted │
             └───────────┘    └───────────┘
```

## 10. Stratos Worked Example: Multi-Entity Tax Allocation

**Scenario:** Stratos Group has the following tax allocation requirements for FY 2025:

### 10.1 Entity Structure

```
Stratos Holdings plc (UK)
├── SG Germany GmbH (100%)
│   └── German Branch in Belgium (PE)
├── SG Singapore Pte Ltd (100%)
└── SG Ireland Ltd (100%)
    └── Pays dividend to UK parent
```

### 10.2 Data

| Item | Amount (€) | Notes |
|------|------------|-------|
| UK tax on Belgian PE income | 180,000 | Branch income taxed in UK |
| UK CFC charge on Singapore | 320,000 | Passive IP income |
| WHT on Irish dividend | 75,000 | 15% WHT on €500K dividend |
| Singapore passive income under CFC | 1,800,000 | IP royalties |
| Singapore local tax | 150,000 | On €4,000,000 GloBE Income |

### 10.3 Allocation Calculations

**1. Belgian PE Allocation (Article 4.3.2(a))**

```
UK tax on Belgian PE income: €180,000

Allocation:
  Remove from UK Covered Taxes: -€180,000
  Add to Belgian PE Covered Taxes: +€180,000
```

**2. Singapore CFC Push-Down (Article 4.3.2(c) with 4.3.3 limitation)**

```
Step 1: Singapore pre-push ETR
  Local tax: €150,000
  GloBE Income: €4,000,000
  ETR = 3.75%

Step 2: Top-Up Tax %
  15% - 3.75% = 11.25%

Step 3: Passive income cap
  €1,800,000 × 11.25% = €202,500

Step 4: Push-down amount
  MIN(€320,000, €202,500) = €202,500

Result:
  Push to Singapore: €202,500
  Remains in UK: €320,000 - €202,500 = €117,500

Singapore post-push ETR:
  (€150,000 + €202,500) ÷ €4,000,000 = 8.8%
```

**3. Irish Dividend WHT (Article 4.3.2(e))**

```
WHT paid by UK on Irish dividend: €75,000

Allocation:
  Remove from UK Covered Taxes: -€75,000
  Add to SG Ireland Covered Taxes: +€75,000
```

### 10.4 Summary Workpaper

| Entity | Before Allocation | PE Alloc | CFC Alloc | WHT Alloc | After Allocation |
|--------|------------------|----------|-----------|-----------|------------------|
| UK Parent | 5,000,000 | -180,000 | -202,500 | -75,000 | 4,542,500 |
| Belgian PE | 50,000 | +180,000 | — | — | 230,000 |
| SG Singapore | 150,000 | — | +202,500 | — | 352,500 |
| SG Ireland | 800,000 | — | — | +75,000 | 875,000 |
| **Group Total** | **6,000,000** | **0** | **0** | **0** | **6,000,000** |

**Note:** Total Covered Taxes remain unchanged—allocation only shifts taxes between jurisdictions.

## 11. Tax Allocation Checklist

### 11.1 Pre-Allocation

- [ ] Identify all CFC taxes in parent accounts
- [ ] Identify all PE income taxed by main entity
- [ ] Identify all hybrid entity structures
- [ ] Identify all intra-group dividends with WHT
- [ ] Extract passive vs. active income breakdown for CFC

### 11.2 Allocation Steps

- [ ] Calculate PE tax allocation (no limitation applies)
- [ ] Calculate CFC tax with passive income limitation
- [ ] Calculate hybrid entity allocation with limitation
- [ ] Allocate distribution WHT to distributor
- [ ] Consider deferred tax allocation (or five-year election)

### 11.3 Post-Allocation

- [ ] Verify group total Covered Taxes unchanged
- [ ] Update each entity's Adjusted Covered Taxes
- [ ] Document allocation methodology
- [ ] Maintain workpapers for each allocation type

## 12. Common Pitfalls
