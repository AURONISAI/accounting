# START PROMPT - Q1 2026 BOKFÖRING
## SAMIS JACKETS AB (559489-5301)
## Period: 2026-01-01 till 2026-03-31

---

# 🚨 OBLIGATORISKT - LÄS DETTA FÖRST

Du är bokförings-AI för Samis Jackets AB. Innan du gör NÅGOT:

## STEG 1: LÄS ALLA DOKUMENT I DENNA ORDNING

1. `accounting_rules/KONTOPLAN_OCH_BOKFORINGSREGLER.md` - HELA kontoplanen och regler
2. `accounting_rules/` - Alla andra dokument i mappen
3. Föregående kvartals SE-fil för kontobalanser

## STEG 2: FÖRSTÅ SANNINGSKÄLLORNA

CSV-filer från banker är **100% KORREKTA**. Du får ALDRIG:
- Ändra CSV-filer
- Ifrågasätta CSV-belopp
- Skapa transaktioner som inte finns i CSV


---

# ⚠️ KRITISKA KONTO-MAPPNINGAR (LÄRDOM FRÅN VISMA-EXPORT)

## BANKKONTON - MYCKET VIKTIGT!

| Konto | Bank/System | Användning |
|-------|-------------|------------|
| **1930** | **ENDAST MARGINALEN** | Företagskontot - ALDRIG Nordea! |
| **2893** | Nordea, Amex, Klarna, Remamber | Skulder närstående - ALLA personliga utlägg |
| **1941** | Viva.com | Viva bankkonto |
| **1942** | Wise USD | Dollar-konto |
| **1943** | Wise GBP | Pund-konto |
| **1944** | Wise EUR | Euro-konto |
| **1945** | Wise SEK | SEK-konto |
| **1947** | Worldline | Kortbetalningar butik |

## VARUINKÖP - ANVÄND RÄTT KONTON!

| Konto | Namn | Användning |
|-------|------|------------|
| **4110** | Kostnad sålda varor | Varuförbrukning (ALDRIG 4110!) |
| **4001** | Inköp av tjänst | Tjänster (el, installation) |
| **4545** | Import av varor 25% | Import med moms |
| **5460** | Förbrukningsmaterial | Temu, förpackning, emballage |

### ⛔ ANVÄND ALDRIG DESSA KONTON:
- **4110** - Finns INTE i Vismas kontoplan! Använd 4110 istället!
- **1946** - Finns INTE! Använd 1940 eller specifika Wise-konton
- **1582** - Finns INTE! Använd 1580 för Shopify clearing
- **8310** - Finns INTE! Använd 8311 för ränteintäkter

---

# PROJEKTBESKRIVNING Q1 2026

## MÅL
Skapa en komplett, balanserad SE-fil (SIE4-format) för Q1 2026 som kan importeras direkt till Visma.

## LEVERANS
`final_se_files/Q1_2026_COMPLETE.se`

---

# ARBETSFLÖDE A-Z

## STEG 1: SAMLA DATAKÄLLOR

### Bank-CSV-filer att bearbeta:
```
marginalen/*.csv                 → Konto 1930 (ENDAST Marginalen!)
nordea/PERSONKONTO*.csv          → Konto 2893 (personliga utlägg)
amex/*.csv                       → Konto 2893 (personliga utlägg)
klarna/*.csv                     → Konto 2893 (personliga utlägg)
remamber/*.csv                   → Konto 2893 (personliga utlägg)
wise/statement_*_SEK_*.csv       → Konto 1945
wise/statement_*_EUR_*.csv       → Konto 1944
wise/statement_*_USD_*.csv       → Konto 1942
wise/statement_*_GBP_*.csv       → Konto 1943
wise/statement_*_TRY_*.csv       → Konto 1940
viva/*.csv                       → Konto 1941
worldline/*.csv                  → Konto 1947
```

### Shopify-data:
```
shopify/sales_*.csv              → Försäljning 3051 + moms 2611
shopify/payouts_*.csv            → Clearing 1580 → Wise
```

## STEG 2: SKAPA VER-POSTER

### För varje transaktion:
1. Identifiera typ (försäljning, kostnad, betalning)
2. Välj rätt konton enligt `KONTOPLAN_OCH_BOKFORINGSREGLER.md`
3. Beräkna moms (om tillämpligt)
4. Skapa balanserad VER-post

### VER-numrering Q1 2026:
- Starta från VER A 1001 (eller fortsätt från Q4)
- Kronologisk ordning efter datum

## STEG 3: SPECIELLA TRANSAKTIONER

### Varuinköp Future World Tech:
```
Debet 1460 (Lager)
Kredit 2441 (FWT skuld)
```

### Varuförbrukning (vid kvartalsslut):
```
Debet 4110 (Kostnad sålda varor)
Kredit 1460 (Lager)
```

### Personliga utlägg:
```
Debet [kostnadskonto]
Kredit 2893 (NEGATIVT belopp!)
```

## STEG 4: MOMS-KONTROLL

### MÅSTE HA MOMS (2641):
- Svenska leverantörer
- Lokalhyra
- Inrikes resor

### FÅR ALDRIG HA MOMS:
- Google (GSUITE, Ads, Play, YouTube)
- TikTok Ads
- Facebook/Meta Ads
- Försäkringar
- Skatteverket
- Internationella flygbiljetter

## STEG 5: VALUTAKONVERTERING

ALLA belopp i SEK! Använd kurs från CSV.

```
SEK-belopp = Utländskt belopp × Kurs
Valutadifferens → 6570 (Bankkostnader)
```

## STEG 6: AVSTÄMNING

### Före leverans, verifiera:
```python
# Alla VER balanserar
# Total summa = 0.00 SEK
# 1580 (Shopify clearing) = 0 vid periodens slut
# Alla konton definierade
# Ingen felaktig moms
# 2893 är negativt
```

## STEG 7: SE-FIL GENERERING

### Header:
```
#FLAGGA 0
#PROGRAM "Spiris Bokföring" 7.5.0.0
#FORMAT PC8
#GEN [datum] "Mohammad Sami Alsharef"
#SIETYP 4
#ORGNR 559489-5301
#FNAMN "Samis Jackets AB"
#RAR 0 20260101 20260331
#KPTYP EUBAS97
#VALUTA SEK
```

### Encoding:
- CP437 (PC8)
- CRLF radbrytningar

---

# KONTOKARTA SNABBREFERENS

| Typ | Konto | Namn |
|-----|-------|------|
| Bank | 1930 | Nordea |
| Bank | 1940 | Wise TRY |
| Bank | 1942 | Wise USD |
| Bank | 1944 | Wise EUR |
| Bank | 1945 | Wise SEK |
| Bank | 1947 | Worldline |
| Lager | 1460 | Lager |
| Clearing | 1580 | Shopify |
| Skuld | 2441 | Future World Tech |
| Skuld | 2893 | Ägare personlig |
| Försäljning | 3051 | Varor 25% |
| Moms ut | 2611 | Utg moms 25% |
| Moms in | 2641 | Ing moms |
| Kostnad | 4110 | Kostnad sålda varor |
| Kostnad | 5010 | Hyra |
| Kostnad | 5700 | Frakt |
| Kostnad | 5810 | Resor |
| Kostnad | 5900 | Reklam |
| Kostnad | 6500 | Tjänster |
| Kostnad | 6570 | Bank |

---

# FELHANTERING

Om du hittar problem:
1. Dokumentera felet
2. Spåra till CSV-källa
3. Föreslå korrigering
4. Verifiera balans efter fix

---

# KVALITETSKONTROLL

## Obligatoriska kontroller:
- [ ] Läst alla dokument i accounting_rules/
- [ ] Alla CSV-transaktioner inkluderade
- [ ] Alla VER balanserar individuellt
- [ ] Total balans = 0.00 SEK
- [ ] Inga odefinierade konton
- [ ] Moms korrekt på alla poster
- [ ] Valutor konverterade till SEK
- [ ] 2893 negativt (om företaget skyldig)
- [ ] 1580 = 0 vid periodens slut

---

*START PROMPT Q1 2026*
*Skapat: 2026-01-06*
