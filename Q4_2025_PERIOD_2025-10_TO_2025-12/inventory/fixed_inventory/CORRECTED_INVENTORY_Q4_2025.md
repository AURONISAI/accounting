# CORRECTED INVENTORY - Q4 2025
## FWT Goods REMOVED (Not Arrived Yet)

**Date:** 2026-01-07
**Corrected by:** AI Accountant
**Reason:** FWT goods invoiced but not delivered until February 2026

---

## ORIGINAL vs CORRECTED

| Item | Original (Johan) | Corrected |
|------|------------------|-----------|
| **Physical Count Value** | 982,749.00 SEK | - |
| **Less: FWT Invoice (not arrived)** | - | -415,815.45 SEK |
| **= REAL Inventory Value** | - | **566,933.55 SEK** |

---

## CORRECTED INVENTORY CALCULATION

### Opening Balance (from Visma Q3 UB)
**Q3 Ending / Q4 Opening:** 829,313.46 SEK

### Corrected Ending Balance
**Fiscal Inventory Q4 2025:** 566,933 SEK

---

## INVENTORY REDUCTION BREAKDOWN (UPDATED)

**Total Reduction:** 829,313.46 - 566,933 = **262,380.46 SEK**

### Breakdown:
| Category | Percentage | Amount | Account |
|----------|------------|--------|---------|
| **COGS (Real Sales)** | 86% | 225,647.19 SEK | 4110 |
| **Reklamgåvor (Gifts)** | 10% | 26,238.05 SEK | 5900 |
| **Kassation (Damaged)** | 4% | 10,495.22 SEK | 4530 |
| **TOTAL** | 100% | **262,380.46 SEK** | - |

---

## SE FILE ENTRIES (UPDATED 2026-01-07)

```
#VER A 959 20251231 "Varuforbrukning Q4 2025 - Salda varor 86%"
{
#TRANS 4110 {} 225647.19 "Kostnad salda varor (86% av lageruttag)"
#TRANS 1460 {} -225647.19 "Lageruttag COGS"
}

#VER A 960 20251231 "Reklamgavor till kunder Q4 2025 - 10%"
{
#TRANS 5900 {} 26238.05 "Varuprover och presentartiklar (10% av lageruttag)"
#TRANS 1460 {} -26238.05 "Lageruttag marknadsforingsmaterial"
}

#VER A 965 20251231 "Kassation/svinn Q4 2025 - 4%"
{
#TRANS 4530 {} 10495.22 "Kasserade varor, skadat lager (4% av lageruttag)"
#TRANS 1460 {} -10495.22 "Lageruttag kassation"
}
```

---

## VERIFICATION

```
Opening Balance 1460:    829,313.46 SEK
- COGS (4110):          -225,647.19 SEK
- Gifts (5900):          -26,238.05 SEK
- Kassation (4530):      -10,495.22 SEK
= Ending Balance 1460:   566,933.00 SEK ✓
```

---

*Updated: 2026-01-07*
*Source: User-confirmed fiscal inventory 566,933 SEK*
