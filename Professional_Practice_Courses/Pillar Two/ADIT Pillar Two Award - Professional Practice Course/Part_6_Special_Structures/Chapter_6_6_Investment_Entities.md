# Chapter 6.6: Investment Entities

## Learning Objective

After completing this chapter, you will be able to identify when an entity qualifies as an Investment Fund, Real Estate Investment Vehicle (REIV), or Insurance Investment Entity, determine when such entities are excluded from GloBE scope, apply the separate ETR calculation under Article 7.4, and elect alternative treatments under Article 7.5 (Tax Transparency Election) or Article 7.6 (Taxable Distribution Method).

## 1. Why Special Rules for Investment Entities?

Investment structures create unique challenges for Pillar Two because of how they are taxed domestically:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE INVESTMENT ENTITY CHALLENGE                                     │
│                                                                     │
│ Traditional corporate structure:                                    │
│ → Entity earns income                                              │
│ → Entity pays corporate tax                                        │
│ → Dividends distributed to shareholders (possibly double-taxed)    │
│                                                                     │
│ Investment fund structure:                                          │
│ → Entity pools capital from investors                              │
│ → Entity often tax-exempt or tax-neutral                           │
│ → Investors taxed on distributions or allocations                  │
│ → Single layer of taxation at investor level                       │
│                                                                     │
│ THE GLOBE PROBLEM:                                                  │
│ → Entity has minimal/zero tax (by design)                          │
│ → Standard ETR calculation → 0% or very low ETR                    │
│ → Would create massive Top-Up Tax exposure                         │
│ → BUT investors are already appropriately taxed                    │
│                                                                     │
│ THE SOLUTION:                                                       │
│ → Exclude qualifying Investment Funds/REIVs that are UPEs          │
│ → Separate ETR calculation (no blending)                           │
│ → Alternative elections to align with domestic treatment           │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Definitions: Investment Entities *(Article 10.1)*

### 2.1 Investment Fund

An **Investment Fund** is an entity that meets ALL of the following criteria:

| Criterion | Description |
|-----------|-------------|
| **Pooling** | Designed to pool assets from a **number of investors** (some unrelated) |
| **Investment policy** | Invests in accordance with a **defined investment policy** |
| **Investor benefit** | Allows investors to reduce transaction, research, and analytical costs, or spread risk collectively |
| **Purpose** | Primarily designed to generate **investment income/gains** or protection against events |
| **Returns** | Investors have right to return from fund assets based on contributions |
| **Regulation** | Entity or its management is subject to **regulatory regime** in its jurisdiction |
| **Professional management** | Managed by **investment fund management professionals** on behalf of investors |

**Examples of Investment Funds:**
- Collective investment schemes
- Mutual funds
- Hedge funds (if meeting criteria)
- Private equity funds (if meeting criteria)
- Unit trusts

**NOT Investment Funds:**
- Group financing companies (fail pooling and investor benefit tests)
- Captive finance entities
- Treasury centres

### 2.2 Real Estate Investment Vehicle (REIV)

A **Real Estate Investment Vehicle (REIV)** is an entity that meets ALL of the following criteria:

| Criterion | Description |
|-----------|-------------|
| **Asset holding** | Holds **predominantly immovable property** |
| **Single taxation** | Taxation achieves **single level of taxation** (in entity's hands OR investor's hands) |
| **Timing** | With at most **one year of deferral** |
| **Widely held** | Entity is **widely held** |

**What "widely held" means:**
- Entity has many owners who are not connected persons
- REIV owned by widely held investment entities or pension funds with numerous beneficiaries is considered widely held

**Common examples:**
- Real Estate Investment Trusts (REITs)
- Listed property companies with distribution requirements
- Open-ended real estate funds

### 2.3 Insurance Investment Entity

An **Insurance Investment Entity** is an entity that:
- Would qualify as an Investment Fund or REIV, **but for** being wholly-owned by an insurance company
- Is established in relation to liabilities under insurance or annuity contracts
- Owner(s) must be regulated as insurance companies

```
INSURANCE INVESTMENT ENTITY VISUAL

Insurance Company (regulated)
        │
        │ 100% owns
        ▼
Insurance Investment Entity
├── Would otherwise be Investment Fund/REIV
├── Established for policy liabilities
└── Treated as Investment Entity for GloBE
```

## 3. When Are Investment Entities Excluded? *(Article 1.5)*

### 3.1 Article 1.5.1: Investment Fund or REIV as UPE

An **Investment Fund** or **REIV** that is the **Ultimate Parent Entity** of an MNE Group is an **Excluded Entity**:

```
┌─────────────────────────────────────────────────────────────────────┐
│ EXCLUDED ENTITY STATUS (Article 1.5.1)                              │
│                                                                     │
│ If Investment Fund or REIV is the UPE:                              │
│ → Excluded Entity                                                   │
│ → No GloBE ETR calculation                                          │
│ → No Top-Up Tax                                                     │
│ → No IIR obligation                                                 │
│                                                                     │
│ IMPORTANT: Revenue still counts for €750M threshold test            │
└─────────────────────────────────────────────────────────────────────┘
```

**Example: REIT as UPE**

```
REIT plc (UK) — WIDELY HELD
├── Is the UPE
├── Holds predominantly immovable property
├── Single level taxation (exempt with distribution requirement)
│
├── 100% PropCo France
├── 100% PropCo Germany
└── 100% PropCo Spain

Treatment:
→ REIT plc is an Excluded Entity (Article 1.5.1)
→ PropCo subsidiaries are still Constituent Entities
→ Subsidiaries subject to standard GloBE calculations
→ BUT no IIR at REIT level (excluded)
→ UTPR may apply at subsidiary level if undertaxed
```

### 3.2 Article 1.5.2: Entities Owned by Excluded Entities

An entity can also be an **Excluded Entity** if owned by Excluded Entities:

**Condition (a):** At least **95% owned** by Excluded Entity or Entities, AND:
- Operates **exclusively or almost exclusively** to hold assets or invest funds for the benefit of Excluded Entities, OR
- Only carries out activities **ancillary** to those of Excluded Entities

**Condition (b):** At least **85% owned** by Excluded Entities (excluding pension services entities), AND:
- **Substantially all** income is dividends or equity gains/losses excluded from GloBE Income

### 3.3 Article 1.5.3: Election NOT to Treat as Excluded

A Filing Constituent Entity may **elect** not to treat an entity as an Excluded Entity under Article 1.5.2. This is a **Five-Year Election**.

**When might you elect out?**
- To utilise losses in the entity
- To preserve SBIE capacity
- Strategic tax planning considerations

## 4. Investment Entities Within Scope: Separate ETR *(Article 7.4)*

### 4.1 When Article 7.4 Applies

If an Investment Entity is **not** an Excluded Entity, it is a Constituent Entity but subject to **special ETR calculation rules**:

```
┌─────────────────────────────────────────────────────────────────────┐
│ ARTICLE 7.4: SEPARATE ETR CALCULATION                               │
│                                                                     │
│ KEY PRINCIPLE:                                                      │
│ Investment Entities are NOT subject to jurisdictional blending.     │
│ Their ETR is calculated SEPARATELY from other CEs in the same       │
│ jurisdiction.                                                       │
│                                                                     │
│ REASON:                                                             │
│ Prevents low-taxed investment income from diluting the ETR of       │
│ operating companies, and vice versa.                                │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Article 7.4.2: Investment Entity Groups

Multiple Investment Entities and Insurance Investment Entities in the **same jurisdiction** form a **separate investment entity group**:

```
JURISDICTIONAL BLENDING EXAMPLE

Ireland Jurisdiction:
├── OpCo Ireland Ltd (trading company)
│   ├── GloBE Income: €20,000,000
│   └── Covered Taxes: €2,500,000 (12.5%)
│
├── InvestCo Ireland (Investment Entity)
│   ├── GloBE Income: €5,000,000
│   └── Covered Taxes: €100,000 (2%)
│
└── InsuranceInvest Ireland (Insurance Investment Entity)
    ├── GloBE Income: €3,000,000
    └── Covered Taxes: €60,000 (2%)

WITHOUT Article 7.4 (if blending applied):
Combined ETR = (€2,660,000) / (€28,000,000) = 9.50%
→ ALL entities subject to Top-Up Tax

WITH Article 7.4 (separate calculations):
1. OpCo Ireland: ETR = 12.5% → Top-Up Tax applies (2.5%)
2. Investment Entity Group: ETR = (€160,000) / (€8,000,000) = 2%
   → Separate Top-Up Tax calculation (13%)

Investment Entity Group does NOT drag down OpCo's ETR.
```

### 4.3 ETR Calculation for Investment Entities

The formula considers the MNE's **allocable share**:

```
Investment Entity ETR = Adjusted Covered Taxes / MNE's Allocable Share of GloBE Income

Where:
Allocable Share = (Total GloBE Income − Amounts attributable to other owners) / Total GloBE Income
```

### 4.4 Top-Up Tax Calculation Under Article 7.4

```
Step 1: Determine Investment Entity ETR (separate calculation)
Step 2: Top-Up Tax % = 15% − Investment Entity ETR
Step 3: Calculate MNE's allocable share of GloBE Income
Step 4: Deduct SBIE (based on Investment Entity's payroll/assets)
Step 5: Excess Profit = Allocable GloBE Income − SBIE
Step 6: Top-Up Tax = Excess Profit × Top-Up Tax %
```

## 5. Alternative Elections: Article 7.5 and 7.6

MNE Groups have two alternative elections to modify Investment Entity treatment:

### 5.1 Article 7.5: Tax Transparency Election

The **Tax Transparency Election** allows a Constituent Entity-owner to treat an Investment Entity as a **Tax Transparent Entity**:

```
┌─────────────────────────────────────────────────────────────────────┐
│ TAX TRANSPARENCY ELECTION (Article 7.5)                             │
│                                                                     │
│ EFFECT:                                                             │
│ → Investment Entity treated as transparent                          │
│ → GloBE Income/Loss allocated to CE-owner                          │
│ → Adjusted Covered Taxes also allocated to CE-owner                │
│ → Investment Entity blends with CE-owner's jurisdiction            │
│                                                                     │
│ PURPOSE:                                                            │
│ Align GloBE treatment with domestic tax treatment where             │
│ investor is taxed directly on fund income.                          │
│                                                                     │
│ ELECTION PARAMETERS:                                                │
│ → Five-Year Election                                                │
│ → Made at Constituent Entity level (owner)                          │
│ → Requires specified conditions to be met                           │
└─────────────────────────────────────────────────────────────────────┘
```

**When to consider Article 7.5 Election:**
- Owner's jurisdiction has high tax rate (≥15%)
- Want to blend Investment Entity income with high-taxed operating income
- Domestic tax already treats fund as transparent

**Example:**

```
BEFORE Article 7.5 Election:

German OpCo (owner)
├── GloBE Income: €50,000,000
├── Covered Taxes: €15,000,000
└── ETR: 30.00%

Investment Entity (Luxembourg)
├── GloBE Income: €10,000,000
├── Covered Taxes: €500,000
└── ETR: 5.00% → Top-Up Tax applies!

AFTER Article 7.5 Election:

Investment Entity treated as transparent → Income allocated to German OpCo

German OpCo (blended):
├── GloBE Income: €50,000,000 + €10,000,000 = €60,000,000
├── Covered Taxes: €15,000,000 + €500,000 = €15,500,000
└── ETR: 25.83% → No Top-Up Tax

Result: Article 7.5 eliminates Investment Entity's Top-Up Tax exposure
```

### 5.2 Article 7.6: Taxable Distribution Method Election

The **Taxable Distribution Method Election** provides a different approach:

```
┌─────────────────────────────────────────────────────────────────────┐
│ TAXABLE DISTRIBUTION METHOD (Article 7.6)                           │
│                                                                     │
│ EFFECT:                                                             │
│ → Exclude Investment Entity's GloBE Income from owner's ETR        │
│ → Instead, include DISTRIBUTIONS when made                          │
│ → Distributions taxable at owner level (must be ≥15%)              │
│ → Undistributed income tracked in special account                  │
│                                                                     │
│ PURPOSE:                                                            │
│ Align with domestic treatment where fund is tax-neutral and        │
│ investors taxed on distributions (deductible dividend regime).      │
│                                                                     │
│ ELECTION PARAMETERS:                                                │
│ → Five-Year Election                                                │
│ → Available where owner reasonably expected to be taxed at ≥15%    │
│   on distributions                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

**Undistributed Net GloBE Income Account:**

Under Article 7.6.4, the MNE must track **Undistributed Net GloBE Income**:

```
UNDISTRIBUTED INCOME TRACKING

Year 1: Investment Entity earns €10M GloBE Income
        No distribution
        Undistributed Account: €10M

Year 2: Investment Entity earns €8M GloBE Income
        Distributes €5M
        Undistributed Account: €10M + €8M − €5M = €13M

Year 3: Investment Entity earns €6M GloBE Income
        Distributes €12M
        Undistributed Account: €13M + €6M − €12M = €7M

Year 4: Investment Entity earns €4M GloBE Income
        No distribution
        Undistributed Account: €7M + €4M = €11M

Year 5 (4 years after Year 1):
→ Year 1 income (€10M) still undistributed? If YES:
→ TOP-UP TAX = Undistributed Year 1 Income × 15%
```

**The Four-Year Rule:**

If income is **not distributed within four years**, the MNE is subject to a Top-Up Tax of **15%** on the undistributed portion:

```
Four-Year Top-Up Tax = Undistributed Net GloBE Income (Year N-4) × 15%
```

**When to consider Article 7.6 Election:**
- Fund typically distributes income within 4 years
- Owner taxed at ≥15% on distributions
- Want to defer GloBE recognition until distribution
- Aligns with domestic deductible dividend treatment

## 6. Comparison: Default vs Article 7.5 vs Article 7.6

| Feature | Default (Art. 7.4) | Tax Transparency (Art. 7.5) | Taxable Distribution (Art. 7.6) |
|---------|-------------------|----------------------------|--------------------------------|
| **ETR calculation** | Separate | Blended with owner | Based on distributions |
| **GloBE Income location** | Investment Entity | CE-owner | CE-owner (when distributed) |
| **Covered Taxes** | Investment Entity | CE-owner | CE-owner (on distribution) |
| **Blending** | NO (separate group) | YES (with owner) | NO |
| **Undistributed income** | Taxed immediately | Taxed immediately (at owner) | Taxed after 4 years (15%) |
| **Best for** | Standalone analysis | High-tax owner | Distribution within 4 years |

## 7. Stratos Worked Example: Investment Entity Subsidiary

### 7.1 Background

Stratos Holdings plc establishes **Stratos Investment Holdings Ltd** in Luxembourg to manage treasury investments and hold minority stakes in portfolio companies.

### 7.2 Structure

```
Stratos Holdings plc (UK)
        │
        │ 100%
        ▼
Stratos Investment Holdings Ltd (Luxembourg)
├── Assets: €200,000,000 in diversified investments
├── GloBE Income: €12,000,000
├── Covered Taxes: €240,000 (Luxembourg exempt holding regime)
└── ETR: 2.00%
```

### 7.3 Step 1: Does Entity Qualify as Investment Entity?

| Investment Fund Criteria | Assessment |
|--------------------------|------------|
| Pools assets from multiple investors? | **NO** — 100% owned by Stratos |
| Defined investment policy? | Yes |
| Reduces transaction costs for investors? | **NO** — single investor |
| **Conclusion** | **NOT an Investment Fund** |

| REIV Criteria | Assessment |
|---------------|------------|
| Holds predominantly immovable property? | **NO** — diversified investments |
| **Conclusion** | **NOT an REIV** |

**Result:** Stratos Investment Holdings Ltd is **NOT** an Investment Entity under Article 10.1. It is a **regular Constituent Entity** subject to standard GloBE rules.

### 7.4 Alternative Scenario: If Entity Were an Investment Entity

Assume Stratos acquires a 60% stake in an existing **Investment Fund** that meets Article 10.1 criteria.

**Structure:**

```
Stratos Holdings plc (UK)
        │
        │ 60%
        ▼
InvestFund SICAV (Luxembourg)
├── Pools assets from multiple investors (Stratos 60%, others 40%)
├── Regulated by CSSF
├── Managed by professional fund manager
├── GloBE Income: €20,000,000
├── Covered Taxes: €400,000
└── ETR: 2.00%
```

### 7.5 Step 2: Is Entity an Excluded Entity?

| Test | Assessment |
|------|------------|
| Is InvestFund SICAV the UPE? | **NO** — Stratos plc is UPE |
| **Article 1.5.1 exclusion** | **Does not apply** |

**Result:** InvestFund SICAV is a Constituent Entity subject to GloBE.

### 7.6 Step 3: Default Treatment (Article 7.4)

**Separate ETR Calculation:**

```
InvestFund SICAV:
├── GloBE Income: €20,000,000
├── Stratos allocable share (60%): €12,000,000
├── Covered Taxes (allocable): €400,000 × 60% = €240,000
├── ETR: €240,000 / €12,000,000 = 2.00%
└── Top-Up Tax %: 15% − 2% = 13%

SBIE (assume minimal):
├── Payroll: €500,000 × 9.8% = €49,000
├── Assets: €0 (financial investments not tangible)
└── Total SBIE: €49,000

Excess Profit = €12,000,000 − €49,000 = €11,951,000
Top-Up Tax = €11,951,000 × 13% = €1,553,630

Stratos IIR liability on InvestFund: €1,553,630
```

### Step 4: Consider Article 7.5 Election (Tax Transparency)

If Stratos makes Article 7.5 election:

**Before Election — UK Position:**

| Entity | GloBE Income | Covered Taxes | ETR |
|--------|--------------|---------------|-----|
| Stratos Holdings plc | €80,000,000 | €20,000,000 | 25.00% |

**After Election — Blended:**

```
Stratos Holdings plc (blended):
├── Own GloBE Income: €80,000,000
├── + InvestFund allocable (60%): €12,000,000
├── Total GloBE Income: €92,000,000
│
├── Own Covered Taxes: €20,000,000
├── + InvestFund allocable: €240,000
├── Total Covered Taxes: €20,240,000
│
└── Blended UK ETR: €20,240,000 / €92,000,000 = 22.00%

ETR ≥ 15% → No Top-Up Tax (Article 7.5 election eliminates €1,553,630 exposure)
```

**Result:** Article 7.5 Election saves €1,553,630 in Top-Up Tax by blending low-taxed investment income with UK's 25% taxed operating income.

### Step 5: Consider Article 7.6 Election (Taxable Distribution Method)

If Stratos elects Article 7.6 instead:

**Year 1:**
- InvestFund GloBE Income: €12,000,000 (allocable to Stratos)
- No distribution made
- Undistributed Account: €12,000,000
- No immediate Top-Up Tax (but tracked)

**Year 2:**
- InvestFund distributes €8,000,000 to Stratos
- Stratos taxed at UK rate (25%) on dividend
- Undistributed Account: €12,000,000 − €8,000,000 + Year 2 income

**Year 5 (if Year 1 income still undistributed):**
- Remaining undistributed Year 1 income: €4,000,000
- Top-Up Tax = €4,000,000 × 15% = €600,000

**Result:** Article 7.6 defers Top-Up Tax but requires distribution within 4 years or 15% charge applies.

### 7.9 Stratos Decision Matrix

| Option | Top-Up Tax | Complexity | Best When |
|--------|------------|------------|-----------|
| **Default (Art. 7.4)** | €1,553,630 | Low | Separate analysis required |
| **Art. 7.5 Election** | €0 | Medium | UK ETR remains ≥15% after blending |
| **Art. 7.6 Election** | €0-600,000 | High | Distributions expected within 4 years |

**Recommendation for Stratos:** Article 7.5 Election appears optimal given UK's high tax rate (25%) provides sufficient headroom to absorb investment income without dropping below 15%.

## 8. Common Pitfalls

### 8.1 Pitfall 1: Assuming All Funds Are Investment Funds

**Error:** Treating a group treasury company as an Investment Fund.

**Correct approach:** Apply the Article 10.1 definition strictly. Group financing companies typically fail the "multiple unrelated investors" and "investor benefit" tests.

### 8.2 Pitfall 2: Confusing UPE Exclusion with Subsidiary Treatment

**Error:** Assuming subsidiaries of an excluded REIT are also excluded.

**Correct approach:** Article 1.5.1 excludes only the Investment Fund/REIV that is the **UPE**. Subsidiaries remain Constituent Entities subject to GloBE.

### 8.3 Pitfall 3: Forgetting Separate ETR Calculation

**Error:** Blending Investment Entity income with other CEs in the same jurisdiction.

**Correct approach:** Under Article 7.4, Investment Entities have **separate** ETR calculations. Do not blend with operating companies.

### 8.4 Pitfall 4: Missing the Four-Year Distribution Deadline

**Error:** Electing Article 7.6 without tracking undistributed income.

**Correct approach:** Maintain Undistributed Net GloBE Income Account. Ensure distributions within 4 years or face 15% charge.

### 8.5 Pitfall 5: Not Considering Election Benefits

**Error:** Accepting default treatment without evaluating Article 7.5 or 7.6 elections.

**Correct approach:** Model all three scenarios. High-taxed owners should strongly consider Article 7.5 to blend away low-taxed investment income.

### 8.6 Pitfall 6: Assuming SBIE Reduces Investment Entity Exposure

**Error:** Expecting significant SBIE for an Investment Entity.

**Correct approach:** Investment Entities typically have minimal payroll and **no tangible assets** (financial investments are not "tangible"). SBIE is usually negligible.

## 9. Investment Entity Assessment Checklist

Use this checklist when evaluating Investment Entities:

```
INVESTMENT ENTITY ASSESSMENT CHECKLIST
Entity: _________________________
Jurisdiction: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: ENTITY CLASSIFICATION
═══════════════════════════════════════════════════════════════════════

INVESTMENT FUND TEST (Article 10.1):
□ Designed to pool assets from multiple investors?            YES / NO
□ Some investors are unrelated?                               YES / NO
□ Invests per defined investment policy?                      YES / NO
□ Allows investors to reduce costs/spread risk?               YES / NO
□ Primarily generates investment income/gains?                YES / NO
□ Investors have right to returns based on contributions?     YES / NO
□ Entity/management subject to regulatory regime?             YES / NO
□ Managed by investment professionals?                        YES / NO

□ **ALL criteria met? → INVESTMENT FUND**                     YES / NO

REIV TEST (Article 10.1):
□ Holds predominantly immovable property?                     YES / NO
□ Achieves single level of taxation?                          YES / NO
□ With at most one year of deferral?                          YES / NO
□ Is widely held?                                             YES / NO

□ **ALL criteria met? → REIV**                                YES / NO

INSURANCE INVESTMENT ENTITY TEST:
□ Would qualify as Investment Fund/REIV but for ownership?    YES / NO
□ Wholly-owned by regulated insurance company?                YES / NO
□ Established for insurance/annuity contract liabilities?     YES / NO

□ **ALL criteria met? → INSURANCE INVESTMENT ENTITY**         YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION B: EXCLUDED ENTITY STATUS
═══════════════════════════════════════════════════════════════════════

□ Is entity the UPE of the MNE Group?                         YES / NO

   If YES and entity is Investment Fund or REIV:
   → **EXCLUDED ENTITY** under Article 1.5.1
   → No GloBE calculation required
   → STOP HERE (but check subsidiaries)

□ Is entity ≥95% owned by Excluded Entities?                  YES / NO
□ Does it operate exclusively for Excluded Entity benefit?    YES / NO

   If both YES: → May be Excluded under Article 1.5.2(a)

□ Is entity ≥85% owned by Excluded Entities?                  YES / NO
□ Is substantially all income excluded dividends/gains?       YES / NO

   If both YES: → May be Excluded under Article 1.5.2(b)

□ **CONCLUSION: Is entity an Excluded Entity?**               YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION C: DEFAULT ETR CALCULATION (ARTICLE 7.4)
═══════════════════════════════════════════════════════════════════════

□ Investment Entity GloBE Income:                       €__________________
□ MNE ownership %:                                      __________________%
□ Allocable GloBE Income:                               €__________________
□ Investment Entity Covered Taxes:                      €__________________
□ Allocable Covered Taxes:                              €__________________

□ Investment Entity ETR:                                __________________%

   If ETR ≥ 15%: No Top-Up Tax under default.

□ Top-Up Tax %:                                         __________________%
□ SBIE (typically minimal):                             €__________________
□ Excess Profit:                                        €__________________
□ **Default Top-Up Tax:**                               €__________________

═══════════════════════════════════════════════════════════════════════
SECTION D: ELECTION ANALYSIS
═══════════════════════════════════════════════════════════════════════

ARTICLE 7.5 (TAX TRANSPARENCY ELECTION):
□ CE-owner jurisdiction:                                ___________________
□ CE-owner standalone ETR:                              __________________%
□ Blended GloBE Income (owner + Investment Entity):     €__________________
□ Blended Covered Taxes:                                €__________________
□ Blended ETR:                                          __________________%

   If blended ETR ≥ 15%: Article 7.5 eliminates Top-Up Tax.

□ **Article 7.5 Top-Up Tax saving:**                    €__________________

ARTICLE 7.6 (TAXABLE DISTRIBUTION METHOD):
□ Expected distributions within 4 years?                      YES / NO
□ Owner taxed at ≥15% on distributions?                       YES / NO
□ Undistributed income risk amount:                     €__________________
□ Potential 4-year Top-Up Tax (15%):                    €__________________

□ **Article 7.6 viable?**                                     YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION E: RECOMMENDATION
═══════════════════════════════════════════════════════════════════════

□ Recommended approach:
   □ Default (Article 7.4) — Top-Up Tax: €__________________
   □ Tax Transparency Election (Article 7.5) — Top-Up Tax: €__________________
   □ Taxable Distribution Method (Article 7.6) — Top-Up Tax: €__________________

□ Election to be filed?                                       YES / NO
□ Five-Year Election period starts:                     ___________________

□ Documentation complete?                                     YES / NO
```
