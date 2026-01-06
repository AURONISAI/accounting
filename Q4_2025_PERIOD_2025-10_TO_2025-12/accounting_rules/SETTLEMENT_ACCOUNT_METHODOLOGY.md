# SAMIS JACKETS AB - BOKFÖRINGSMETODIK Q4 2025
## Avräkningskonto-metoden för Betalningsförmedlare

**Version:** 1.0  
**Datum:** 2026-01-05  
**Period:** Q4 2025 (2025-10-01 till 2025-12-31)  

---

## KONTOPLANSÖVERSIKT

### Avräkningskonton (Settlement Accounts)
| Konto | Beskrivning | Används för |
|-------|-------------|-------------|
| **1947** | Worldline avräkning | Kortbetalningar från POS (butik) |
| **1582** | Shopify/Stripe avräkning | E-handelsbetalningar EUR via Stripe |

### Bankkonton
| Konto | Beskrivning |
|-------|-------------|
| **1930** | Marginalen Bank (Företagskonto) |
| **1910** | Kassa (Kontanter) |
| **1942** | Wise USD |
| **1944** | Wise EUR |
| **1945** | Wise SEK |
| **1946** | Wise TRY |

### Försäljningskonton
| Konto | Beskrivning |
|-------|-------------|
| **3001** | Försäljning varor 25% moms |
| **3051** | Övrig försäljning |

### Momskonton
| Konto | Beskrivning |
|-------|-------------|
| **2610** | Utgående moms 25% |
| **2641** | Ingående moms |

---

## METODIK: TRE-STEGS BOKFÖRING

### Steg 1: FÖRSÄLJNING (SALES_Q4_2025.se)
När försäljning sker bokförs den mot avräkningskontot, INTE direkt mot bankkontot.

**Kortförsäljning (Worldline):**
```
Debit  1947 (Worldline avräkning)  +316,289.18 SEK
Credit 3001 (Försäljning ex moms)  -253,031.34 SEK
Credit 2610 (Moms 25%)             -63,257.84 SEK
```

**Shopify EUR-försäljning:**
```
Debit  1582 (Shopify avräkning)    +63,675.16 SEK
Credit 3001 (Försäljning ex moms)  -50,940.13 SEK
Credit 2610 (Moms 25%)             -12,735.03 SEK
```

**Kontantförsäljning:**
```
Debit  1910 (Kassa)                +43,087.75 SEK
Credit 3001 (Försäljning ex moms)  -34,470.20 SEK
Credit 2610 (Moms 25%)             -8,617.55 SEK
```

### Steg 2: INBETALNING (MARGINALEN/WISE SE-filer)
När pengarna kommer till banken bokas avräkningskontot bort.

**Worldline → Marginalen:**
```
Debit  1930 (Bank)                 +75,685.21 SEK
Credit 1947 (Worldline avräkning)  -75,685.21 SEK
```

**Shopify → Wise EUR:**
```
Debit  1944 (Wise EUR)             +1,193.13 SEK
Credit 1582 (Shopify avräkning)    -1,193.13 SEK
```

### Steg 3: AVGIFTER (WORLDLINE/WISE SE-filer)
Avgifter bokförs separat.

**Worldline avgifter:**
```
Debit  6570 (Bankavgifter)         +400.67 SEK
Credit 1947 (Worldline avräkning)  -400.67 SEK
```

---

## FILSTRUKTUR Q4 2025

| Fil | Innehåll |
|-----|----------|
| **SALES_Q4_2025.se** | All försäljning bokförd mot avräkningskonton |
| **MARGINALEN_Q4_2025.se** | Alla banktransaktioner + Worldline inbetalningar |
| **WORLDLINE_Q4_2025.se** | Worldline avgifter + avräkning |
| **WISE_Q4_2025.se** | Alla Wise-transaktioner + Shopify inbetalningar |
| **INVENTORY_Q4_2025.se** | Varuinköp och lagerjustering |

---

## Q4 2025 SUMMERING

### Försäljning:
| Källa | Inkl moms | Ex moms | Moms 25% |
|-------|-----------|---------|----------|
| Worldline (kort) | 316,289.18 | 253,031.34 | 63,257.84 |
| Kontant (kassa) | 43,087.75 | 34,470.20 | 8,617.55 |
| Shopify EUR | 63,675.16 | 50,940.13 | 12,735.03 |
| **TOTALT** | **423,052.09** | **338,441.67** | **84,610.42** |

### Worldline Månadsdata:
| Månad | SALES | REFUNDS | FEES | PAYOUT |
|-------|-------|---------|------|--------|
| Oktober | 78,825.88 | -728.00 | -400.67 | 75,685.21 |
| November | 153,893.99 | -4,815.00 | -811.68 | 153,447.31 |
| December | 91,506.00 | -1,396.00 | -542.83 | 87,156.66 |
| **TOTALT** | 324,225.87 | -6,939.00 | -1,755.18 | 316,289.18 |

### Shopify EUR Inbetalningar:
| Datum | Belopp EUR | Belopp SEK (kurs ~11.5) |
|-------|------------|-------------------------|
| 03-10 | €103.75 | 1,193.13 |
| 10-10 | €86.12 | 990.38 |
| 17-10 | €418.35 | 4,811.03 |
| 24-10 | €154.12 | 1,772.38 |
| 07-11 | €371.75 | 4,275.13 |
| 14-11 | €86.37 | 993.32 |
| 21-11 | €1,398.29 | 16,080.33 |
| 28-11 | €2,199.39 | 25,292.99 |
| 05-12 | €573.75 | 6,598.13 |
| 12-12 | €58.31 | 670.55 |
| 29-12 | €86.77 | 997.85 |
| **TOTALT** | **€5,536.97** | **63,675.22** |

---

## AVSTÄMNING

### Worldline 1947 ska nollas:
```
+ Försäljning till 1947: 316,289.18
- Payout till 1930:      316,289.18
- Avgifter till 6570:      1,755.18
- Refunds:                 6,939.00 (ingår i payout)
= Saldo 1947:                  0.00 ✓
```

### Shopify 1582 ska nollas:
```
+ Försäljning till 1582:  63,675.16
- Inbetalning till 1944:  63,675.16
= Saldo 1582:                  0.00 ✓
```

---

## KODNING PER TRANSAKTIONSTYP

### Inköp/Kostnader:
| Typ | Konto Debet | Moms 2641 | Konto Kredit |
|-----|-------------|-----------|--------------|
| Hyra butik | 5010 | - | 1930 |
| Hyra lager | 5010 | - | 1930 |
| Frakt/Transport | 5710 | ✓ 25% | 1930/1944 |
| Marknadsföring | 5900 | ✓ 25% | 1942/1944 |
| Programvara | 5420 | ✓ 25% | 1930/1942 |
| Telefon | 6212 | ✓ 25% | 1942/1944/1945 |
| Drivmedel | 5610 | ✓ 25% | 1942/1944 |
| Resa tjänst | 5810 | ✓ 6-25% | 1942/1944 |
| Bankavgifter | 6570 | - | 1930/1947 |
| Myndighetsavgift | 6991 | - | 1942 |

### Privata uttag:
| Typ | Konto Debet | Konto Kredit |
|-----|-------------|--------------|
| Privat utgift | 2893 | 1930/1942/1944/1946 |
| Ägarlån | 2893 | 1930/1946 |

---

*Dokument skapat 2026-01-05*
*Samis Jackets AB - Org.nr 559489-5301*
