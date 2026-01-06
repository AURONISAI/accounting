# Q4 2025 FINAL TODO LIST
## Samis Jackets AB - Korrigeringar och Git Push
## Datum: 2026-01-06

---

# ANALYS AV VISMA EXPORT

Från filen `20240701-20250930 before the final q4 uplaods).se`:

## KONTON SOM FAKTISKT ANVÄNDS I VISMA:

### Bankkonton:
| Konto | Namn | Användning |
|-------|------|------------|
| 1930 | Företagskonto | **ENDAST MARGINALEN** |
| 1941 | Viva.com | Viva bankkonto |
| 1942 | Wise USD | USD |
| 1943 | Wise GBP | GBP |
| 1944 | Wise EUR | EUR |
| 1945 | Wise SEK | SEK |
| 1947 | Worldline | Kortterminaler |
| 2893 | Skulder närstående | **NORDEA, AMEX, KLARNA, REMAMBER** |

### Varuinköp:
| Konto | Namn | Användning |
|-------|------|------------|
| **4110** | Kostnad sålda varor | Varuförbrukning (INTE 4010!) |
| 4545 | Import av varor 25% | Import med moms |

### Övriga konton som används:
- 4001 "Inköp av tjänst" (inte 4010)
- 5460 Förbrukningsmaterial (Temu, Biltema etc)
- 5910 Annonsering (Google Ads, TikTok, Facebook)
- 6540 IT-tjänster (Google GSUITE)
- 6590 Övriga externa tjänster (Shopify)
- 6991/6992 Övriga kostnader

---

# TODO LISTA

## [x] 1. FIXA KONTO 4010 → 4110
- ✅ Bytt alla `#TRANS 4010` till `#TRANS 4110` i Q4_2025_COMPLETE.se
- ✅ Lagt till `#KONTO 4110 "Kostnad sålda varor"`
- ✅ Tagit bort `#KONTO 4010` definition

## [x] 2. UPPDATERA BANKKONTO-MAPPNING
- ✅ 1930 = ENDAST Marginalen
- ✅ 2893 = Nordea Personkonto, Amex, Klarna, Remamber (personliga utlägg)
- ✅ Dokumentation uppdaterad

## [x] 3. FIXA SVENSK TECKENKODNING
- ✅ SIE4-filer använder CP437 (PC8) encoding
- ✅ Svenska tecken: ö=\x94, ä=\x84, å=\x86

## [x] 4. UPPDATERA ACCOUNTING_RULES DOKUMENTATION
- ✅ Fixat KONTOPLAN_OCH_BOKFORINGSREGLER.md med korrekta konton
- ✅ Uppdaterat START_PROMPT för alla kvartal 2026

## [x] 5. UPPDATERA ALLA SE-FILER
- ✅ Q4_2025_COMPLETE.se (final)
- ✅ INVENTORY_Q4_2025.se
- ✅ WISE_Q4_2025.se

## [ ] 6. GIT COMMIT OCH PUSH
- Lägg till alla ändringar
- Commit med beskrivande meddelande
- Push till remote repository

---

# GENOMFÖRANDE

## Steg 1: Kontrollera nuvarande SE-fil
## Steg 2: Applicera korrigeringar
## Steg 3: Verifiera balans
## Steg 4: Uppdatera dokumentation
## Steg 5: Git push

---

*Skapad: 2026-01-06*
