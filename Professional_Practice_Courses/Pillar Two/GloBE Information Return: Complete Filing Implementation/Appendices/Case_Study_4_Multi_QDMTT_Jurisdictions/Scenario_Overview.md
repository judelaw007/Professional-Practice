# Case Study 4: Atlantic Manufacturing Group - Multi-QDMTT Jurisdictions

## Scenario Context

This case study presents **Atlantic Manufacturing Group plc**, a UK-headquartered industrial conglomerate with operations in five jurisdictions that have all enacted QDMTTs. You will practice understanding how QDMTT offsets IIR and how Top-up Tax is collected locally rather than by the UPE jurisdiction.

## Learning Objectives

By completing this case study, you will be able to:
- Understand GloBE rule ordering (QDMTT → IIR → UTPR)
- Calculate QDMTT offsets against IIR charges
- Coordinate calculations across multiple QDMTT jurisdictions
- Understand the policy outcome of QDMTT (source country retains tax)

## Company Profile

| Attribute | Detail |
|-----------|--------|
| **Ultimate Parent Entity** | Atlantic Manufacturing Group plc (UK) |
| **Headquarters** | Birmingham, United Kingdom |
| **Fiscal Year End** | 31 December 2024 |
| **Consolidated Revenue** | €3.2 billion |
| **Total Constituent Entities** | 85 |
| **QDMTT Jurisdictions** | 5 (UK, Germany, Netherlands, Switzerland, Ireland) |

## QDMTT Jurisdiction Summary

| Jurisdiction | QDMTT Name | ETR Status | Top-up Tax? |
|--------------|------------|------------|-------------|
| UK | Domestic Top-up Tax (DTT) | 25% | No |
| Germany | Nationale Ergänzungssteuer | 30% | No |
| Netherlands | Wet minimumbelasting | 12.36% (IP entity) | Yes - QDMTT |
| Switzerland | Mindeststeuer | 13% | Yes - QDMTT |
| Ireland | QDMTT | 13.9% | Yes - QDMTT |

## Key Concept: QDMTT Offset

```
IIR Charge = Total Top-up Tax - QDMTT Already Paid

If QDMTT = Total Top-up Tax → IIR = 0
```

The QDMTT allows source countries to collect Top-up Tax locally, rather than having it flow to the UPE jurisdiction under IIR.

## Demo Tools to Use

| Tool | Tool ID | Purpose in This Case Study |
|------|---------|----------------------------|
| GIR ETR Calculator | GIR-001 | Calculate ETR for each QDMTT jurisdiction |
| GIR SBIE Calculator | GIR-002 | Calculate SBIE for low-tax jurisdictions |
| GIR Top-Up Tax Calculator | GIR-003 | Calculate Top-up Tax and QDMTT offset |
| GIR Filing Deadline Calculator | GIR-005 | Compare filing deadlines across 5 QDMTT jurisdictions |
| DFE Election Assessment Tool | GIR-007 | Assess filing coordination across QDMTT jurisdictions |
| GIR Practice Form | GIR-008 | Practice Section 2 (Safe Harbours) and Section 3 entries |

## Related Course Sections

- Section 10.4: Multi-QDMTT Jurisdictions Scenario
- Part 1: GloBE Rule Ordering
- Part 2: Jurisdiction-by-Jurisdiction Analysis
- Part 3: Consolidated Top-up Tax Summary
- Part 4: QDMTT Regime Variations

## Instructions

1. Review the sample data for each QDMTT jurisdiction
2. Calculate ETR and Top-up Tax for low-tax jurisdictions
3. Apply QDMTT offset to determine net IIR charge
4. Verify that QDMTT collection equals total Top-up Tax
5. Compare your results to expected outcomes
