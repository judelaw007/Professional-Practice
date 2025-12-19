# Chapter 5.4: Qualified Domestic Minimum Top-Up Tax (QDMTT)

## Learning Objective

After completing this chapter, you will be able to identify jurisdictions with a Qualified Domestic Minimum Top-Up Tax (QDMTT), understand the QDMTT priority rule, apply the QDMTT Safe Harbour, and determine when QDMTT eliminates IIR/UTPR liability.

## Introduction

The Qualified Domestic Minimum Top-Up Tax represents one of the most significant strategic responses by source countries to the GloBE framework. When the OECD designed the charging mechanism with IIR applying before UTPR, it created an inherent tension: jurisdictions that had deliberately maintained low effective tax rates—often to attract foreign investment—faced the prospect of seeing that "undertaxed" income picked up and taxed by parent jurisdictions or sister entities elsewhere in the MNE group. The QDMTT emerged as a mechanism to address this concern, allowing source jurisdictions to collect the Top-Up Tax themselves before any foreign collecting jurisdiction could apply IIR or UTPR.

This chapter examines how QDMTT fundamentally alters the dynamics of global minimum tax compliance. Understanding QDMTT is essential not only for technical calculation purposes but also for appreciating how jurisdictions are strategically positioning themselves within the Pillar Two landscape. The rapid adoption of QDMTT by investment hubs, low-tax jurisdictions, and traditional tax competition venues demonstrates that the GloBE framework has catalysed a significant shift in international tax policy—with source countries reclaiming taxing rights they might otherwise have ceded to residence jurisdictions.

## 1. What Is QDMTT?

A **Qualified Domestic Minimum Top-Up Tax (QDMTT)** is a domestic tax that a jurisdiction imposes on its own low-taxed entities to bring them up to the 15% minimum rate—before any IIR or UTPR can apply.

### 1.1 The Core Concept

```
┌──────────────────────────────────────────────────────────────────┐
│                         WITHOUT QDMTT                            │
│                                                                  │
│   Low-taxed subsidiary          →    Parent jurisdiction         │
│   (e.g., Singapore 10%)                collects Top-Up Tax       │
│                                        under IIR                 │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                          WITH QDMTT                              │
│                                                                  │
│   Low-taxed subsidiary          →    Source jurisdiction         │
│   (e.g., Ireland 11.8%)                collects QDMTT            │
│                                                                  │
│   Parent jurisdiction           →    No Top-Up Tax (already      │
│                                        covered by QDMTT)         │
└──────────────────────────────────────────────────────────────────┘
```

### 1.2 Why Jurisdictions Implement QDMTT

| Reason | Explanation |
|--------|-------------|
| **Preserve taxing rights** | Retain the Top-Up Tax revenue domestically rather than losing it to parent jurisdictions |
| **Simplify compliance** | Single calculation under domestic law rather than multiple GloBE calculations |
| **Protect incentives** | Coordinate with existing tax incentives while meeting minimum tax requirements |
| **Competitive positioning** | Demonstrate commitment to global tax framework while maintaining investment attractiveness |

The strategic calculus underlying QDMTT adoption reflects a fundamental shift in how jurisdictions approach tax competition. Previously, a country like Ireland could offer a 12.5% corporate rate as a competitive advantage, accepting that MNEs would benefit from the lower rate. Under GloBE, that advantage partially disappears because the parent jurisdiction captures the difference between the local rate and 15%. By implementing QDMTT, Ireland ensures that if additional tax must be paid on its constituent entities, that revenue stays within Ireland rather than flowing to the UK, Germany, or wherever the Ultimate Parent Entity resides. This represents a pragmatic adaptation: if the global minimum tax floor eliminates the competitive advantage of rates below 15%, at least the jurisdiction can retain the revenue.

## 2. QDMTT Priority Rule

QDMTT applies **first** in the rule order:

```
1. QDMTT (source jurisdiction) — Applies first
        ↓
2. IIR (parent jurisdiction) — Applies to remaining Top-Up Tax
        ↓
3. UTPR (sister jurisdictions) — Backstop for uncollected Top-Up Tax
```

### 2.1 Practical Effect

| Scenario | QDMTT | IIR/UTPR |
|----------|-------|----------|
| QDMTT covers 100% of Top-Up Tax | Full liability | €0 |
| QDMTT covers 80% of Top-Up Tax | 80% | 20% |
| No QDMTT in jurisdiction | €0 | Full liability |

### 2.2 Stratos Example: Ireland

| Item | Amount |
|------|--------|
| Jurisdictional Top-Up Tax | €426,394 |
| Ireland QDMTT | (€426,394) |
| **IIR Liability (UK)** | **€0** |

Ireland retains the full Top-Up Tax through its QDMTT. No IIR charge to Stratos Holdings plc.

The priority given to QDMTT in the rule order represents a deliberate policy choice by the Inclusive Framework. By allowing source jurisdictions to collect the Top-Up Tax first, the framework respects the principle that countries have primary taxing rights over income generated within their borders. This ordering also reduces potential for double taxation disputes: if the source jurisdiction collects through QDMTT, there is no residual amount for IIR or UTPR to collect, eliminating the need for complex crediting mechanisms between jurisdictions. For MNE Groups, QDMTT priority often simplifies compliance because they deal with one tax authority rather than navigating the application of IIR across multiple parent entities in the ownership chain.

## 3. Qualifying Criteria (Article 10.1)

For a domestic minimum tax to be a "Qualified" DMTT, it must meet three requirements:

### 3.1 Requirement 1: Functional Equivalence

The QDMTT must determine Excess Profits in a manner **equivalent to the GloBE Rules**:

| Element | Must Be Equivalent |
|---------|-------------------|
| GloBE Income calculation | Same adjustments as Articles 3.1-3.5 |
| Covered Taxes calculation | Same as Articles 4.1-4.6 |
| ETR calculation | Same formula as Article 5.1 |
| SBIE calculation | Same payroll/asset carve-outs |
| Excess Profit determination | Same as Article 5.2 |

**Permitted variations:**
- Apply to MNEs below €750M threshold (voluntary extension)
- Apply to purely domestic groups
- Use domestic accounting standards (if consistent outcomes)

### 3.2 Requirement 2: Top-Up to Minimum Rate

The QDMTT must increase domestic tax liability on Excess Profits to the **15% minimum rate**:

```
QDMTT = (15% − Domestic ETR) × Domestic Excess Profits
```

**Key point:** The QDMTT must result in tax **equal to or greater than** what would arise under GloBE Rules. A QDMTT that systematically produces less tax will not qualify.

### 3.3 Requirement 3: Consistent Administration

The QDMTT must be implemented and administered **consistently with GloBE outcomes**:

| Must Avoid | Explanation |
|------------|-------------|
| **Related benefits** | Tax benefits that offset the QDMTT effect |
| **Systematic shortfalls** | Design features that consistently reduce QDMTT below GloBE amount |
| **Cherry-picking** | Selective application to certain MNEs or income types |

The stringent qualifying criteria reflect an underlying concern: that jurisdictions might attempt to implement superficial minimum taxes that appear compliant but systematically produce less revenue than a proper GloBE calculation would yield. The "related benefits" prohibition addresses schemes where a jurisdiction might impose QDMTT but simultaneously offer refundable credits, grants, or other mechanisms that effectively return the tax to the MNE. Such arrangements would undermine the entire purpose of the global minimum tax. The functional equivalence requirement ensures that the domestic calculation mirrors the GloBE calculation closely enough that the source jurisdiction's QDMTT genuinely satisfies the 15% floor rather than creating a facade of compliance while preserving tax advantages.

## 4. QDMTT Safe Harbour

The **QDMTT Safe Harbour** is a permanent simplification mechanism introduced in July 2023.

### 4.1 How It Works

When a jurisdiction has QDMTT Safe Harbour status:

1. **Single calculation:** MNE only needs to calculate Top-Up Tax under domestic QDMTT rules
2. **Deemed nil Top-Up Tax:** GloBE Top-Up Tax is deemed to be zero for that jurisdiction
3. **No duplicate computation:** No need to run parallel GloBE calculations

### 4.2 Eligibility for Safe Harbour

| Criterion | Requirement |
|-----------|-------------|
| **Qualified QDMTT** | Domestic law meets Article 10.1 requirements |
| **Inclusive Framework recognition** | Listed on OECD Central Record |
| **No related benefits** | No tax incentives that reduce QDMTT effectiveness |
| **Transitional or permanent status** | Either transitional qualified status or full peer review |

### 4.3 Benefits of Safe Harbour

| Benefit | Description |
|---------|-------------|
| **Reduced compliance burden** | One calculation instead of two |
| **Administrative simplicity** | No reconciliation between QDMTT and GloBE calculations |
| **Certainty** | Clear outcome based on domestic rules |

The Safe Harbour represents a significant concession to practical compliance concerns. Without it, MNE Groups would face the burden of maintaining two parallel calculation systems—one for QDMTT under domestic law and another for GloBE under the Model Rules—even when the outcomes should theoretically be identical. By deeming the GloBE Top-Up Tax to be zero where a qualified Safe Harbour applies, the Inclusive Framework eliminated redundant compliance work while maintaining the integrity of the minimum tax floor. For practitioners, the Safe Harbour creates a clear decision point: once confirmed that a jurisdiction has Safe Harbour status, they can rely entirely on the domestic QDMTT calculation without second-guessing whether it matches a hypothetical GloBE outcome.

## 5. QDMTT Implementation Status

### 5.1 Jurisdictions with QDMTT (as of 2025)

**European Union (22 of 27 Member States):**

| Country | QDMTT Status | IIR Status | Notes |
|---------|--------------|------------|-------|
| Austria | ✅ 2024 | ✅ 2024 | |
| Belgium | ✅ 2024 | ✅ 2024 | |
| Czech Republic | ✅ 2024 | ✅ 2024 | |
| Denmark | ✅ 2024 | ✅ 2024 | |
| Finland | ✅ 2024 | ✅ 2024 | |
| France | ✅ 2024 | ✅ 2024 | |
| Germany | ✅ 2024 | ✅ 2024 | |
| Hungary | ✅ 2024 | ✅ 2024 | |
| Ireland | ✅ 2024 | ✅ 2024 | Safe Harbour status |
| Italy | ✅ 2024 | ✅ 2024 | |
| Luxembourg | ✅ 2024 | ✅ 2024 | |
| Netherlands | ✅ 2024 | ✅ 2024 | |
| Sweden | ✅ 2024 | ✅ 2024 | |

**Non-EU Europe:**

| Country | QDMTT Status | IIR Status | Notes |
|---------|--------------|------------|-------|
| United Kingdom | ✅ 2024 | ✅ 2024 | Safe Harbour status |
| Switzerland | ✅ 2024 | ✅ 2025 | IIR from 2025 |
| Norway | ✅ 2024 | ✅ 2024 | |
| Liechtenstein | ✅ 2024 | ✅ 2024 | |

**Asia-Pacific:**

| Country | QDMTT Status | IIR Status | Notes |
|---------|--------------|------------|-------|
| South Korea | ✅ 2024 | ✅ 2024 | |
| Japan | ✅ 2024 | ✅ 2024 | Safe Harbour status |
| Australia | ✅ 2024 | ✅ 2024 | Based on draft legislation |
| Singapore | ❌ No QDMTT | ❌ No IIR | Subject to other jurisdictions' IIR |
| Hong Kong | ✅ 2025 | ❌ Pending | QDMTT only initially |

**Other Key Jurisdictions:**

| Country | QDMTT Status | Notes |
|---------|--------------|-------|
| Canada | ✅ 2024 | Safe Harbour status |
| UAE | ✅ 2025 | 15% corporate tax from 2025 |
| Isle of Man | ✅ 2025 | Safe Harbour status |
| Jersey | ✅ 2025 | |
| Guernsey | ✅ 2025 | |

The implementation pattern reveals interesting strategic positioning. Jurisdictions historically considered tax havens or low-tax jurisdictions—such as Ireland, Luxembourg, the Crown Dependencies, and now even the UAE—have moved quickly to adopt QDMTT. This swift action reflects the recognition that without QDMTT, their resident entities would generate Top-Up Tax revenue for foreign treasuries. In contrast, higher-tax jurisdictions like Germany and France implemented QDMTT more as a matter of technical completeness rather than revenue protection, since their domestic rates typically already exceed 15%. The notable exception is Singapore, which has delayed QDMTT implementation—a decision that currently results in Singapore-sourced Top-Up Tax being collected by parent jurisdictions under IIR.

### 5.2 Checking Current Status

**OECD Central Record:** The OECD maintains an updated list of jurisdictions with transitional qualified status for both QDMTT and IIR. Always verify current status before relying on QDMTT offset:

[Central Record of Legislation with Transitional Qualified Status](https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/central-record-of-legislation-with-transitional-qualified-status.html)

## 6. Transitional Qualified Status

### 6.1 What Is Transitional Status?

During the initial implementation period, the Inclusive Framework allows **transitional qualified status** for jurisdictions that have enacted QDMTT legislation but have not yet completed full peer review.

### 4.1 How It Works

| Status | Meaning | Duration |
|--------|---------|----------|
| **Transitional Qualified** | Self-certified compliance; full peer review pending | Until peer review complete |
| **Fully Qualified** | Peer review completed; confirmed compliance | Permanent |
| **Conditional DMTT** | Applies only when MNE is subject to GloBE elsewhere | 2024 only (must become unconditional) |

### 6.3 Elective DMTT Special Rule

Some jurisdictions implemented **Elective DMTTs** in 2024 (where MNEs could choose whether to apply). These can qualify for transitional status if:

1. The DMTT becomes non-elective in subsequent years
2. MNEs cannot claim Safe Harbour if they elected out

The transitional framework acknowledges the practical reality that implementing complex legislation takes time, and full peer review cannot happen instantaneously across all adopting jurisdictions. Self-certification during the transitional period allows the global minimum tax system to function while the OECD undertakes comprehensive reviews. However, this creates an element of risk for MNE Groups: if a jurisdiction's transitional status is later revoked due to non-compliance discovered in peer review, the MNE may face retrospective adjustments. Prudent compliance therefore involves monitoring not just whether a jurisdiction has transitional status, but also tracking the progress of peer review processes and any published concerns about specific jurisdictions' QDMTT design.

## 7. Stratos QDMTT Analysis

### 7.1 Jurisdiction Assessment

| Jurisdiction | QDMTT Status | Impact on Stratos |
|--------------|--------------|-------------------|
| **Germany** | ✅ QDMTT | Not applicable (ETR 23% > 15%) |
| **Singapore** | ❌ No QDMTT | Full Top-Up Tax via IIR |
| **Ireland** | ✅ QDMTT (Safe Harbour) | Ireland retains Top-Up Tax |
| **UK** | ✅ QDMTT (Safe Harbour) | Not applicable (parent; high-tax) |

### 7.2 Detailed Analysis: Ireland

**Without QDMTT:**
- Jurisdictional Top-Up Tax: €426,394
- IIR applies: UK collects €426,394

**With QDMTT:**
- Ireland collects QDMTT: €426,394
- IIR liability: €0
- **Revenue stays in Ireland**

### 7.3 Detailed Analysis: Singapore

**Current status:** Singapore has not implemented QDMTT.

**Impact:**
- Jurisdictional Top-Up Tax: €197,498
- No QDMTT offset available
- IIR applies: UK collects €197,498

**Future consideration:** If Singapore implements QDMTT, the Top-Up Tax would be collected in Singapore rather than the UK.

The Stratos example illustrates a pattern that many UK-parented MNE Groups now face. Where subsidiaries operate in EU jurisdictions that have implemented QDMTT—Ireland, Luxembourg, the Netherlands—the domestic minimum tax captures any Top-Up Tax liability locally. However, subsidiaries in Asian jurisdictions without QDMTT continue to generate IIR liability for the UK parent. This creates a compliance asymmetry: for QDMTT jurisdictions, Stratos relies on the local tax return and payment process, while for non-QDMTT jurisdictions like Singapore, Stratos must include the Top-Up Tax in its UK GloBE Information Return and pay accordingly. The contrast between Ireland (€426,394 retained locally) and Singapore (€197,498 collected by UK) demonstrates the tangible financial consequences of each jurisdiction's policy choices.

## 8. QDMTT Calculation Mechanics

When applying QDMTT, the source jurisdiction typically follows GloBE-equivalent calculations:

### 8.1 Step 1: Determine Domestic GloBE Income

Using domestic implementation of GloBE Income adjustments (same as Chapter 3).

### 8.2 Step 2: Determine Domestic Covered Taxes

Using domestic implementation of Covered Tax adjustments (same as Chapter 4).

### 8.3 Step 3: Calculate Domestic ETR

```
Domestic ETR = Domestic Covered Taxes ÷ Domestic GloBE Income
```

### 8.4 Step 4: Calculate Domestic SBIE

Using domestic implementation of payroll and tangible asset carve-outs.

### 8.5 Step 5: Calculate QDMTT

```
QDMTT = (15% − Domestic ETR) × (Domestic GloBE Income − Domestic SBIE)
```

### 8.6 Potential Variations

QDMTT calculations may differ slightly from GloBE calculations due to:

| Variation | Effect |
|-----------|--------|
| **Domestic accounting standards** | May produce different GloBE Income |
| **Rounding differences** | Minor computational variations |
| **Local elections** | Different election choices than group-wide |

**Key principle:** Any variation must result in QDMTT **equal to or greater than** GloBE Top-Up Tax. If domestic calculation produces less, the jurisdiction loses qualified status.

The permitted variations in QDMTT calculation mechanics reflect practical accommodation for jurisdictions that may use different accounting standards or make different election choices at the domestic level. However, the one-way tolerance (QDMTT must equal or exceed GloBE) prevents jurisdictions from exploiting these variations to systematically undertax. In practice, most well-designed QDMTT regimes produce outcomes very close to the GloBE calculation, with minor differences arising from rounding or timing of guidance. Where differences do emerge, the onus falls on the source jurisdiction to demonstrate that its QDMTT satisfies the floor—and on MNE Groups to document that reliance on QDMTT offset is appropriate.

## 9. Interaction with IIR and UTPR

### 9.1 Offset Mechanics

| Scenario | QDMTT Effect | IIR/UTPR Amount |
|----------|--------------|-----------------|
| QDMTT = Full Top-Up Tax | Full offset | €0 |
| QDMTT < Top-Up Tax | Partial offset | Difference |
| QDMTT > Top-Up Tax | Full offset | €0 (excess not refunded) |

### 9.2 Example: Partial QDMTT Coverage

**Hypothetical:** A jurisdiction's QDMTT covers only 80% of the GloBE Top-Up Tax due to calculation differences.

| Item | Amount |
|------|--------|
| GloBE Jurisdictional Top-Up Tax | €100,000 |
| QDMTT Paid | €80,000 |
| **IIR Liability** | **€20,000** |

**Note:** This scenario is rare. Properly designed QDMTTs should cover the full GloBE amount.

## 10. Common Pitfalls

### 10.1 Pitfall 1: Assuming All Domestic Minimum Taxes Are QDMTTs

**Error:** Treating any domestic minimum tax as qualifying for GloBE offset.

**Correct approach:** Verify the jurisdiction is listed on the OECD Central Record with transitional or permanent qualified status.

### 10.2 Pitfall 2: Ignoring Transitional Status Conditions

**Error:** Relying on QDMTT offset without checking if transitional conditions are met.

**Correct approach:** Confirm the jurisdiction's status is current and any conditions (e.g., non-elective requirement) are satisfied.

### 10.3 Pitfall 3: Forgetting Safe Harbour Election

**Error:** Running full GloBE calculations for a QDMTT Safe Harbour jurisdiction.

**Correct approach:** If Safe Harbour applies, deem GloBE Top-Up Tax as zero and rely on domestic QDMTT calculation.

### 10.4 Pitfall 4: Overlooking Related Benefits

**Error:** Assuming QDMTT qualifies when jurisdiction offers offsetting tax benefits.

**Correct approach:** Check for "related benefits" that may disqualify the QDMTT from qualified status.

### 10.5 Pitfall 5: Not Updating Jurisdiction Lists

**Error:** Using outdated information on which jurisdictions have implemented QDMTT.

**Correct approach:** Regularly check the OECD Central Record for updates, especially for new fiscal years.

## 11. QDMTT Assessment Checklist

Use this checklist when analysing QDMTT impact:

```
QDMTT ASSESSMENT CHECKLIST
Jurisdiction: _________________________
Fiscal Year: _________________________

STEP 1: QDMTT STATUS
☐ Check OECD Central Record for current status
☐ Confirm transitional or permanent qualified status
☐ Verify Safe Harbour eligibility

Status: ☐ No QDMTT  ☐ Transitional Qualified  ☐ Fully Qualified
Safe Harbour: ☐ Yes  ☐ No

STEP 2: TOP-UP TAX EXPOSURE
Is this jurisdiction low-taxed (ETR < 15%)?    ☐ Yes  ☐ No

If NO: QDMTT analysis not required (no Top-Up Tax)

If YES: Continue to Step 3

STEP 3: QDMTT OFFSET
Jurisdictional Top-Up Tax (from Ch. 5.3):      €__________________

QDMTT Amount:
☐ QDMTT covers full Top-Up Tax                 €__________________
☐ QDMTT covers partial amount                  €__________________
☐ No QDMTT (jurisdiction has not implemented)  €0

STEP 4: NET IIR/UTPR LIABILITY
Jurisdictional Top-Up Tax:                     €__________________
Less: QDMTT Offset:                            (€__________________)
                                               ───────────────────
NET IIR/UTPR LIABILITY:                        €__________________

STEP 5: DOCUMENTATION
☐ OECD Central Record screenshot saved
☐ Domestic QDMTT legislation reviewed
☐ QDMTT calculation documented (if applicable)
```

## Concluding Discussion

The QDMTT represents perhaps the most consequential structural element of the GloBE framework from a practical compliance perspective. Its existence fundamentally changes the economics of low-tax jurisdictions: rather than seeing the Pillar Two minimum tax as purely a constraint on tax competition, many jurisdictions have embraced QDMTT as a mechanism to preserve revenue that would otherwise flow to parent jurisdictions. This strategic adaptation has been remarkably swift—within two years of the Model Rules' publication, most significant investment hubs had implemented or announced QDMTT legislation.

For MNE Groups and their advisors, QDMTT introduces both simplification and complexity. Simplification arises because where QDMTT applies with Safe Harbour status, the parallel GloBE calculation can be dispensed with entirely. Complexity arises because the compliance landscape now requires tracking which jurisdictions have QDMTT, whether they have transitional or permanent qualified status, and whether any conditions attach to that status. The OECD Central Record becomes an essential reference point, but it captures only a moment in time—practitioners must remain alert to legislative developments, peer review outcomes, and any challenges to qualified status.

Looking ahead, the relationship between QDMTT and IIR will likely define much of the Pillar Two compliance experience. In a world where most significant jurisdictions implement QDMTT, the IIR increasingly becomes a residual mechanism applicable primarily to subsidiaries in jurisdictions that have declined to adopt their own minimum tax—or that have had their QDMTT status revoked. The UTPR, originally conceived as a backstop, may see limited application if QDMTT and IIR together capture most undertaxed income. Understanding QDMTT is therefore essential not merely for calculating current year liabilities, but for anticipating how the global minimum tax landscape will continue to evolve.

