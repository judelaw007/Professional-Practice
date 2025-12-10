# Chapter 6.1: Mergers and Demergers

## Learning Objective

After completing this chapter, you will be able to assess the impact of mergers and demergers on the €750 million revenue threshold, apply the retrospective combination rule for mergers, determine when demerged groups remain in scope, and handle partial-year treatment for entities entering or leaving an MNE Group.

---

## Key References

**OECD GloBE Model Rules:**
- Article 1.1.1 — €750 million revenue threshold
- Article 6.1.1 — Merger impact on revenue threshold
- Article 6.1.2 — Demerger impact on revenue threshold
- Article 6.2.1 — Entities joining an MNE Group
- Article 6.2.2 — Treatment of share acquisitions as asset transfers
- Article 10.1 — Definition of GloBE Reorganisation

**OECD Commentary:**
- Chapter 6, paragraphs 1-45 — Corporate restructurings and threshold calculations

**Administrative Guidance:**
- December 2023: Revenue definition for threshold purposes
- June 2024: Partial year calculations

---

## The Revenue Threshold Challenge

The standard €750 million threshold test looks at **revenue in 2 of 4 preceding fiscal years**. But what happens when:
- Two groups merge mid-year?
- A group demerges into separate entities?
- An acquisition occurs that brings new entities into scope?

**The problem:** Without special rules, groups could structure transactions to avoid or delay Pillar Two application.

**The solution:** Article 6.1 provides special rules that reconstruct history for mergers and test forward for demergers.

---

## Merger Rules *(Article 6.1.1)*

### The Retrospective Combination Rule

When two MNE Groups merge to form a single consolidated group, the **combined group's revenue is reconstructed as if it had always existed in its post-merger form**.

```
┌─────────────────────────────────────────────────────────────────────┐
│ MERGER: RETROSPECTIVE COMBINATION                                   │
│                                                                     │
│ For the purpose of the €750M threshold test:                        │
│                                                                     │
│ → Add together the revenues of BOTH groups                         │
│ → For EACH of the four preceding fiscal years                      │
│ → As if the merger had occurred at the start of the first year     │
│                                                                     │
│ This prevents groups avoiding Pillar Two by merging                │
│ two sub-threshold groups into an in-scope group                    │
└─────────────────────────────────────────────────────────────────────┘
```

### When the Combination Rule Applies

The rule applies when an MNE Group acquires **all or substantially all** of the members of another consolidated group.

| Scenario | Combination Rule Applies? |
|----------|---------------------------|
| Group A acquires 100% of Group B | **Yes** — combine historical revenues |
| Group A acquires 80% of Group B (full consolidation) | **Yes** — substantially all |
| Group A acquires a single entity from Group B | **No** — standard rules apply |
| Merger of equals forming new Group C | **Yes** — combine both groups |

### Example: Merger Brings Groups Into Scope

**Pre-Merger:**

| Group | FY-4 Revenue | FY-3 Revenue | FY-2 Revenue | FY-1 Revenue | In Scope? |
|-------|--------------|--------------|--------------|--------------|-----------|
| Alpha Group | €400M | €420M | €450M | €480M | No (< €750M) |
| Beta Group | €380M | €350M | €400M | €420M | No (< €750M) |

**Merger occurs on 1 July FY 2025.**

**Post-Merger Reconstruction:**

| Combined | FY-4 | FY-3 | FY-2 | FY-1 | ≥ €750M? |
|----------|------|------|------|------|----------|
| Alpha + Beta | €780M | €770M | €850M | €900M | **Yes** |

**Result:** The combined group **immediately** falls within Pillar Two scope for FY 2025 because the reconstructed revenues exceed €750M in at least 2 of the 4 preceding years.

### Critical Insight: No Grace Period

A common misconception is that merged groups have time before Pillar Two applies. **This is incorrect.**

```
IMPORTANT: The retrospective combination rule means a merger can trigger
IMMEDIATE Pillar Two application if the combined historical revenues
exceed €750M in 2 of 4 preceding years.

There is no transition period or phase-in for mergers.
```

---

## Demerger Rules *(Article 6.1.2)*

### The Forward-Looking Test

When a group demerges, each resulting group is tested **forward** rather than retrospectively.

```
┌─────────────────────────────────────────────────────────────────────┐
│ DEMERGER: FORWARD-LOOKING TEST                                      │
│                                                                     │
│ A demerged group meets the revenue threshold if:                    │
│                                                                     │
│ YEAR 1 (first full FY after demerger):                              │
│   → Revenue ≥ €750M in that year                                   │
│                                                                     │
│ YEARS 2-4 (subsequent fiscal years):                                │
│   → Revenue ≥ €750M in at least 2 of the years since demerger      │
│                                                                     │
│ This prevents automatic exit from Pillar Two via demerger          │
└─────────────────────────────────────────────────────────────────────┘
```

### Demerger Testing Mechanics

**Scenario:** MegaCorp (in scope) demerges into NewCo A and NewCo B on 30 June 2025.

**Year 1 Test (FY 2026 — first full FY after demerger):**

| Entity | FY 2026 Revenue | In Scope? |
|--------|-----------------|-----------|
| NewCo A | €820M | **Yes** (single year test) |
| NewCo B | €600M | **No** (below threshold) |

**Subsequent Years Test (FY 2027-2028):**

| Entity | FY 2026 | FY 2027 | FY 2028 | Years ≥ €750M | In Scope? |
|--------|---------|---------|---------|---------------|-----------|
| NewCo A | €820M | €790M | €850M | 3 of 3 | **Yes** |
| NewCo B | €600M | €680M | €760M | 1 of 3 | **No** |

**NewCo B exits scope** because it does not have revenue ≥ €750M in at least 2 years post-demerger.

### Anti-Avoidance Consideration

A group cannot avoid Pillar Two by demerging and then immediately re-merging. The combination rules would apply to reconstruct revenues.

---

## Partial Year Treatment *(Article 6.2.1)*

### Entities Joining Mid-Year

When an entity joins an MNE Group during a fiscal year, the GloBE rules apply **only to the portion of income and taxes consolidated in the UPE's financial statements**.

```
Entity joins on 1 July (mid-year):
→ Include 6 months of GloBE Income
→ Include 6 months of Adjusted Covered Taxes
→ Include 6 months of payroll costs for SBIE
→ Tangible assets: see special rule below
```

### Tangible Assets for Partial Year

For SBIE purposes, tangible assets are **not prorated** like payroll. Instead:

- **Joining entity:** Use asset value at **joining date** (not year-end average)
- **Leaving entity:** Use asset value at **leaving date**

*(Article 6.2.1(e))*

### Example: Mid-Year Acquisition

**Stratos acquires TechStart Ltd on 1 July 2025.**

| Item | Full Year | Consolidated (6 months) |
|------|-----------|-------------------------|
| TechStart GloBE Income | €12,000,000 | €6,000,000 |
| TechStart Covered Taxes | €1,440,000 | €720,000 |
| TechStart Payroll | €3,600,000 | €1,800,000 |
| TechStart Tangible Assets | €8,000,000 | **€8,000,000** (at joining date) |

**For Stratos's FY 2025 GloBE calculations:**
- Add €6,000,000 to Irish jurisdictional GloBE Income
- Add €720,000 to Irish Adjusted Covered Taxes
- Add €1,800,000 to Irish payroll for SBIE
- Add €8,000,000 to Irish tangible assets for SBIE

---

## Deferred Tax Attributes *(Article 6.2.1(f))*

### General Rule: Carry Over

When an entity joins an MNE Group, existing deferred tax attributes (DTAs, DTLs) are generally **respected**:

```
Acquired entity's DTAs and DTLs:
→ Carry over to the acquiring MNE Group
→ Treated as if they arose while under common control
→ Subject to the same 15% rate cap
```

### Exception: GloBE Loss Election

The **GloBE Loss Election** (an alternative to the standard DTA approach) is a **jurisdictional attribute** that **cannot be transferred** to another MNE Group.

| Attribute | Transferable? | Treatment |
|-----------|---------------|-----------|
| Accounting DTAs | Yes | Carry over |
| Accounting DTLs | Yes | Carry over |
| Tax loss carryforwards | Yes | Subject to local rules |
| GloBE Loss Election DTA | **No** | Lost on change of control |

### Practical Implication

If the selling group used the GloBE Loss Election, the acquiring group **cannot continue** using that election. The acquiring group must:
1. Determine whether to make its own GloBE Loss Election for that jurisdiction, OR
2. Apply the standard DTA approach

---

## Accounting Treatment: Merger vs Acquisition Accounting

The accounting treatment of a business combination affects GloBE calculations:

### Merger Accounting (Pooling of Interests)

| Feature | Treatment |
|---------|-----------|
| Asset values | Historical cost maintained |
| No fair value step-up | No GloBE adjustment needed |
| Retained earnings | Combined from both entities |

### Acquisition Accounting (Purchase Method)

| Feature | Treatment |
|---------|-----------|
| Asset values | Revalued to fair value |
| Fair value step-up | Creates new tax basis differences |
| Goodwill | May arise (excluded from GloBE calculations) |
| Deferred taxes | Recalculated on new basis differences |

**Impact on GloBE:**

Under acquisition accounting, the fair value step-up creates new temporary differences. These affect:
- Future depreciation/amortisation (GloBE Income adjustments)
- Deferred tax calculations (Covered Tax adjustments)

---

## Decision Flowchart: Merger/Demerger Impact

```
START: Corporate restructuring occurs
        │
        ▼
┌───────────────────────────────────────────────────┐
│ What type of transaction?                         │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────────────────┐
MERGER              DEMERGER
   │                     │
   ▼                     ▼
┌──────────────────┐  ┌──────────────────────────────┐
│ Is it acquisition │  │ Apply forward-looking test:  │
│ of ALL/SUBSTAN-  │  │                              │
│ TIALLY ALL of    │  │ Year 1: Revenue ≥ €750M?    │
│ another group?   │  │ Years 2-4: 2+ years ≥ €750M? │
└──────────────────┘  └──────────────────────────────┘
        │                     │
   ┌────┴────┐           ┌────┴────┐
  YES       NO         PASS      FAIL
   │         │           │         │
   ▼         ▼           ▼         ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│COMBINE │ │Standard│ │Demerged│ │Demerged│
│revenues│ │rules   │ │group   │ │group   │
│retro-  │ │apply   │ │IN SCOPE│ │exits   │
│spective│ │        │ │        │ │scope   │
└────────┘ └────────┘ └────────┘ └────────┘
   │
   ▼
┌───────────────────────────────────────────────────┐
│ Combined revenues ≥ €750M in 2 of 4 prior years? │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────┐
  YES       NO
   │         │
   ▼         ▼
┌────────┐ ┌────────┐
│Combined│ │Combined│
│group   │ │group   │
│IN SCOPE│ │NOT in  │
│IMMEDI- │ │scope   │
│ATELY   │ │(yet)   │
└────────┘ └────────┘
```

---

## Stratos Worked Example: Acquisition of TechStart

### Background

Stratos Holdings plc is considering acquiring TechStart Group, an Irish technology company with operations in Ireland and Germany.

**Pre-Acquisition Data:**

| Group | FY-4 Revenue | FY-3 Revenue | FY-2 Revenue | FY-1 Revenue |
|-------|--------------|--------------|--------------|--------------|
| Stratos Group | €850M | €900M | €920M | €950M |
| TechStart Group | €45M | €52M | €58M | €65M |

**Question 1: Does acquiring TechStart affect Stratos's scope status?**

### Analysis

**Step 1: Is this a combination of two consolidated groups?**

TechStart Group has multiple entities under a common parent. Stratos is acquiring 100% of TechStart.

**Answer:** Yes — combination rule applies.

**Step 2: Calculate combined historical revenues:**

| Year | Stratos | TechStart | Combined |
|------|---------|-----------|----------|
| FY-4 | €850M | €45M | €895M |
| FY-3 | €900M | €52M | €952M |
| FY-2 | €920M | €58M | €978M |
| FY-1 | €950M | €65M | €1,015M |

**Step 3: Apply €750M threshold:**

All four combined years exceed €750M. Stratos was already in scope, and the acquisition doesn't change this.

**Conclusion:** No impact on scope status (Stratos remains in scope).

---

### Question 2: How is TechStart's partial year handled?

**Acquisition Date:** 1 July 2025 (mid-year)

**TechStart Ireland (the main entity being acquired):**

| Item | Full Year | 6-Month Period |
|------|-----------|----------------|
| GloBE Income | €8,500,000 | €4,250,000 |
| Adjusted Covered Taxes | €1,062,500 | €531,250 |
| Payroll (eligible) | €2,400,000 | €1,200,000 |
| Tangible Assets (NBV) | €5,000,000 | €5,000,000* |

*Assets at joining date, not prorated.

**Impact on Stratos's Ireland Jurisdiction:**

| Item | Pre-Acquisition | TechStart (6 mo.) | Post-Acquisition Total |
|------|-----------------|-------------------|------------------------|
| GloBE Income | €15,000,000 | €4,250,000 | **€19,250,000** |
| Covered Taxes | €1,770,000 | €531,250 | **€2,301,250** |
| Payroll | €8,400,000 | €1,200,000 | **€9,600,000** |
| Tangible Assets | €12,000,000 | €5,000,000 | **€17,000,000** |

**Revised Ireland ETR:**

```
ETR = €2,301,250 ÷ €19,250,000 = 11.95%
```

**Revised Ireland SBIE (FY 2025 rates):**

```
Payroll: €9,600,000 × 9.8% = €940,800
Assets:  €17,000,000 × 7.8% = €1,326,000
Total SBIE: €2,266,800
```

**Revised Excess Profit and Top-up Tax:**

```
Excess Profit = €19,250,000 − €2,266,800 = €16,983,200
Top-up Tax % = 15% − 11.95% = 3.05%
Top-up Tax = €16,983,200 × 3.05% = €517,988
```

---

### Question 3: What about TechStart's deferred tax attributes?

**TechStart Ireland has:**
- DTA on tax losses: €400,000 (at 12.5% rate)
- DTL on IP amortisation: €250,000 (at 12.5% rate)

**Treatment:**

| Attribute | Amount | Transferable? | Treatment in Stratos |
|-----------|--------|---------------|---------------------|
| DTA on losses | €400,000 | Yes | Carry over; future reversal reduces Covered Taxes |
| DTL on IP | €250,000 | Yes | Carry over; future reversal increases Covered Taxes |

**If TechStart had a GloBE Loss Election:**

The GloBE Loss Election DTA would **not** transfer. Stratos would need to decide whether to:
- Make its own GloBE Loss Election for Ireland (if losses exist), OR
- Use the standard accounting DTA approach

---

## Common Pitfalls

### Pitfall 1: Assuming Mergers Provide Transition Time

**Error:** Believing that a newly merged group has time before Pillar Two applies.

**Correct approach:** Apply the retrospective combination rule. A merger can trigger **immediate** Pillar Two application if combined historical revenues exceed €750M in 2 of 4 prior years.

### Pitfall 2: Prorating Tangible Assets for Partial Year

**Error:** Prorating tangible asset values for SBIE when an entity joins mid-year.

**Correct approach:** Use the asset value at the **joining date** (not prorated). Only payroll is prorated based on the consolidation period.

### Pitfall 3: Transferring GloBE Loss Election

**Error:** Assuming an acquired entity's GloBE Loss Election continues under the new MNE Group.

**Correct approach:** The GloBE Loss Election is a jurisdictional attribute that **cannot be transferred**. The acquiring group must make its own election decision.

### Pitfall 4: Ignoring Acquisition Accounting Impact

**Error:** Not considering how fair value step-ups under acquisition accounting affect deferred taxes.

**Correct approach:** Under acquisition accounting, new temporary differences arise. These affect future GloBE Income and Covered Tax calculations through changed depreciation/amortisation and deferred tax movements.

### Pitfall 5: Incorrect Demerger Testing

**Error:** Applying the retrospective combination rule to demergers.

**Correct approach:** Demergers use the **forward-looking test**. Test Year 1 revenue alone, then test 2+ years in Years 2-4.

---

## Merger/Demerger Assessment Checklist

Use this checklist when a corporate restructuring occurs:

```
MERGER/DEMERGER IMPACT ASSESSMENT
Transaction: _________________________
Date: _________________________
Type: MERGER / DEMERGER / ACQUISITION

═══════════════════════════════════════════════════════════════════════
SECTION A: SCOPE IMPACT (€750M THRESHOLD)
═══════════════════════════════════════════════════════════════════════

□ If MERGER/ACQUISITION of substantially all of another group:
   □ List acquiring group revenues for FY-4 to FY-1:
     FY-4: €__________ FY-3: €__________ FY-2: €__________ FY-1: €__________
   □ List target group revenues for FY-4 to FY-1:
     FY-4: €__________ FY-3: €__________ FY-2: €__________ FY-1: €__________
   □ Calculate COMBINED revenues:
     FY-4: €__________ FY-3: €__________ FY-2: €__________ FY-1: €__________
   □ Combined ≥ €750M in 2+ years?   YES / NO
   □ Result: IN SCOPE / NOT IN SCOPE

□ If DEMERGER:
   □ Year 1 (first full FY): Demerged group revenue €__________
     ≥ €750M?   YES / NO
   □ If NO in Year 1: Not in scope (continue monitoring)
   □ If YES in Year 1: In scope for Year 1
   □ Years 2-4: Revenue ≥ €750M in 2+ years?   YES / NO
   □ Result: IN SCOPE / EXITS SCOPE

═══════════════════════════════════════════════════════════════════════
SECTION B: PARTIAL YEAR TREATMENT (Entities Joining/Leaving)
═══════════════════════════════════════════════════════════════════════

□ Transaction date: _______________
□ Months consolidated: _____ out of 12

□ Joining Entity Calculations:
   □ GloBE Income (period consolidated):       €__________________
   □ Covered Taxes (period consolidated):      €__________________
   □ Payroll (period consolidated):            €__________________
   □ Tangible Assets (at joining date):        €__________________

□ Leaving Entity Calculations:
   □ GloBE Income (period to leaving):         €__________________
   □ Covered Taxes (period to leaving):        €__________________
   □ Payroll (period to leaving):              €__________________
   □ Tangible Assets (at leaving date):        €__________________

═══════════════════════════════════════════════════════════════════════
SECTION C: DEFERRED TAX ATTRIBUTES
═══════════════════════════════════════════════════════════════════════

□ Does target have DTAs?                        YES / NO
   □ If YES, amount and nature: _________________________________

□ Does target have DTLs?                        YES / NO
   □ If YES, amount and nature: _________________________________

□ Did target have GloBE Loss Election?          YES / NO
   □ If YES: Election does NOT transfer. Acquiring group must decide:
     □ Make own GloBE Loss Election for jurisdiction?  YES / NO
     □ Use standard DTA approach?                      YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION D: ACCOUNTING TREATMENT
═══════════════════════════════════════════════════════════════════════

□ Accounting method: MERGER ACCOUNTING / ACQUISITION ACCOUNTING

□ If ACQUISITION ACCOUNTING:
   □ Fair value step-up on assets?              YES / NO
   □ Amount of step-up: €__________________
   □ New deferred tax liabilities created?      YES / NO
   □ Amount: €__________________
   □ Impact on future GloBE calculations documented?   YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION E: SUMMARY
═══════════════════════════════════════════════════════════════════════

□ Scope status post-transaction:               IN SCOPE / NOT IN SCOPE
□ GloBE calculations required for transaction year?    YES / NO
□ Special elections needed?                    YES / NO
□ Documentation complete?                      YES / NO
```

---

## Summary

Mergers and demergers require careful analysis under Pillar Two:

| Transaction | Rule | Key Test |
|-------------|------|----------|
| **Merger** | Retrospective combination | Combined revenues ≥ €750M in 2 of 4 prior years |
| **Demerger** | Forward-looking test | Year 1: Revenue ≥ €750M; Years 2-4: 2+ years ≥ €750M |
| **Partial year** | Consolidation period | Income/taxes/payroll prorated; assets at joining/leaving date |
| **DT attributes** | Carry over (mostly) | GloBE Loss Election does NOT transfer |

**Critical warning:** Mergers can trigger **immediate** Pillar Two application. There is no grace period.

---

## Integration with GIR Tools

Merger and demerger transactions affect GIR calculations and reporting:

| Impact Area | Tool | Action Required |
|-------------|------|-----------------|
| **Scope assessment** | Manual | Apply combination/forward-looking rules before GIR preparation |
| **Partial year data** | GIR-001 GloBE Calculator | Enter prorated GloBE Income and Covered Taxes |
| **SBIE adjustment** | GIR-001 Step 2 | Enter prorated payroll; assets at transaction date |
| **GIR filing** | GIR-004 GIR Practice Form | Report partial-year entities with dates |

**GIR Reporting Note:** The GloBE Information Return requires disclosure of:
- Entities joining the MNE Group (with joining date)
- Entities leaving the MNE Group (with leaving date)
- Partial-year calculations methodology

---

## Next Step

You have learned how mergers and demergers affect the €750 million threshold and partial-year treatment. Proceed to **Chapter 6.2: Acquisitions and Disposals** for detailed guidance on entity-level transactions, basis step-up elections, and asset vs. share deal treatment.
