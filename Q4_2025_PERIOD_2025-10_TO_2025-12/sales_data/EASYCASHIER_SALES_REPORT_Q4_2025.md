# SAMIS JACKETS AB - Q4 2025 SALES REPORT
## EasyCashier (POS Sales)

**Report Period:** 2025-10-01 to 2025-12-31
**Generated:** 2026-01-05
**Data Source:** Försäljningsrapport 2026-01-02 17-55.csv

---

## Summary

| Metric | Value |
|--------|-------|
| Total Product Lines | 625 |
| Total Units Sold | 1,618 |
| Försäljning (ex moms) | 287,501.53 SEK |
| Moms (25%) | 71,875.40 SEK |
| Försäljning (inkl. moms) | 359,376.93 SEK |
| Inköpssumma (COGS) | 274,527.90 SEK |
| Vinst (Brutto) | 12,973.63 SEK |
| Bruttomarginal | 4.51% |

---

## Analysis

EasyCashier POS-systemet visar försäljning från fysisk butik under Q4 2025. 

**Observationer:**
- Låg bruttomarginal (4.51%) indikerar att majoriteten av försäljningen var kampanjprodukter med rabatterade priser
- Inköpssumma representerar det faktiska kostnadsvärdet för sålda varor
- Moms-beräkning är korrekt på 25%

---

## Bokföringsunderlag - KORRIGERAT (Source of Truth: Worldline Excel)

### Betalningsmetod-uppdelning:
| Betalningsmetod | Inkl moms | Ex moms | Moms 25% |
|-----------------|-----------|---------|----------|
| **KORT (Worldline Payout)** | 316,289.18 | 253,031.34 | 63,257.84 |
| **KONTANT (Kassa)** | 43,087.75 | 34,470.20 | 8,617.55 |
| **TOTALT** | 359,376.93 | 287,501.54 | 71,875.39 |

### Bokföring - Kortförsäljning (Worldline → 1930):
| Konto | Debet | Kredit | Beskrivning |
|-------|-------|--------|-------------|
| 1930 | 316,289.18 | | Marginalen Bank (Worldline payout) |
| 3001 | | 253,031.34 | Försäljning varor 25% moms |
| 2610 | | 63,257.84 | Utgående moms 25% |

### Bokföring - Kontantförsäljning (→ 1910):
| Konto | Debet | Kredit | Beskrivning |
|-------|-------|--------|-------------|
| 1910 | 43,087.75 | | Kassa - kontant |
| 3001 | | 34,470.20 | Försäljning varor 25% moms |
| 2610 | | 8,617.55 | Utgående moms 25% |

### Worldline Avgifter (→ 6570):
| Konto | Debet | Kredit | Beskrivning |
|-------|-------|--------|-------------|
| 6570 | 1,755.18 | | Bankavgifter (Worldline fees) |
| 2893 | | 1,755.18 | Worldline fee (ingår i brutto) |

### Worldline Månadsdata (från xlsx):
| Månad | SALES | REFUNDS | FEES | PAYOUT → 1930 |
|-------|-------|---------|------|---------------|
| Oktober | 78,825.88 | -728.00 | -400.67 | 75,685.21 |
| November | 153,893.99 | -4,815.00 | -811.68 | 153,447.31 |
| December | 91,506.00 | -1,396.00 | -542.83 | 87,156.66 |
| **TOTAL** | **324,225.87** | **-6,939.00** | **-1,755.18** | **316,289.18** |

**Note:** Refunds (-6,939.00) är redan avdragna från SALES i PAYOUT. Fees bokas separat till 6570.

### COGS-bokning (75% av försäljning ex moms):
| Konto | Debet | Kredit | Beskrivning |
|-------|-------|--------|-------------|
| 4010 | 215,626.16 | | Varuförbrukning (287,501.54 × 75%) |
| 1460 | | 215,626.16 | Lager av handelsvaror |

---

**SOURCE OF TRUTH:**
- EasyCashier: Försäljningsrapport 2026-01-02 17-55.csv (total sales)
- Worldline: monthly_report_202510.xlsx, monthly_report_202511.xlsx, monthly_report_202512.xlsx (card sales)
- Cash = EasyCashier Total - Worldline SALES

*Rapport uppdaterad 2026-01-05*
