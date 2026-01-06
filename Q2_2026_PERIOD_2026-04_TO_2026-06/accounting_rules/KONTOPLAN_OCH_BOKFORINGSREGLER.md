# SAMIS JACKETS AB - KONTOPLAN OCH BOKFÖRINGSREGLER
## VERSION 2026-Q1 | UPPDATERAD 2026-01-06

---

# ⚠️ LÄS DETTA FÖRST - OBLIGATORISKT

Innan du gör NÅGOT med bokföringen:
1. Läs HELA detta dokument
2. Läs alla filer i `accounting_rules/` mappen
3. Förstå pengaflödet och kontoplanen
4. CSV-filer från banker är ALLTID 100% korrekta - ändra ALDRIG dem

---

# FÖRETAGSINFORMATION

| Fält | Värde |
|------|-------|
| Företagsnamn | Samis Jackets AB |
| Organisationsnummer | 559489-5301 |
| Momssats | 25% (Sverige) |
| Räkenskapsår | 2024-07-01 till 2025-12-31 (förlängt första år) |
| SE-filformat | SIE4, CP437 (PC8) encoding, CRLF |

---

# KONTOPLAN - ENDAST DESSA KONTON SKA ANVÄNDAS

## 1xxx - TILLGÅNGAR

### Anläggningstillgångar
| Konto | Namn | Användning |
|-------|------|------------|
| 1220 | Inventarier och verktyg | Utrustning, maskiner |
| 1240 | Bilar och transportmedel | Företagsfordon |

### Lager
| Konto | Namn | Användning |
|-------|------|------------|
| **1460** | Lager av handelsvaror | ALLT lager - kläder från Future World Tech |

### Fordringar
| Konto | Namn | Användning |
|-------|------|------------|
| 1510 | Kundfordringar | Fakturerade kunder |
| **1580** | Fordringar | Shopify clearing (pågående betalningar) |
| 1630 | Skattekonto | Avräkning skatter |

### Bankkonton
| Konto | Namn | Användning |
|-------|------|------------|
| 1910 | Kassa | Kontanter |
| **1930** | Företagskonto | Nordea Personkonto (huvudkonto) |
| **1940** | Övriga bankkonton | Wise TRY (turkisk lira) |
| **1942** | Wise USD | Wise dollar |
| **1944** | Wise EUR | Wise euro |
| **1945** | Wise SEK | Wise svenska kronor |
| **1947** | Worldline | Kortbetalningar från butik |

---

## 2xxx - SKULDER & EGET KAPITAL

### Leverantörsskulder
| Konto | Namn | Användning |
|-------|------|------------|
| 2440 | Leverantörsskulder | Allmänna leverantörer |
| **2441** | Future World Tech | ENDAST för FWT-skulder (Kina) |

### Moms
| Konto | Namn | Användning |
|-------|------|------------|
| **2611** | Utgående moms 25% | Moms på försäljning - ANVÄND DETTA |
| **2641** | Ingående moms | Moms på inköp |
| **2650** | Momsredovisning | Betalning till Skatteverket |

### Övriga skulder
| Konto | Namn | Användning |
|-------|------|------------|
| **2893** | Skulder till närstående | Personliga utlägg av ägaren |

---

## 3xxx - INTÄKTER

| Konto | Namn | Användning |
|-------|------|------------|
| **3051** | Försäljning varor 25% sv | ALL försäljning Sverige med moms |
| 3055 | Försäljning export | Momsfri export utanför EU |

---

## 4xxx - VARUINKÖP

| Konto | Namn | Användning |
|-------|------|------------|
| 4000 | Inköp varor Sverige | Svenska leverantörer |
| **4110** | Kostnad sålda varor | Kostnad för sålda varor (från lager) |

---

## 5xxx - KOSTNADER

| Konto | Namn | Användning |
|-------|------|------------|
| **5010** | Lokalhyra | ALL hyra av lokaler |
| 5420 | Programvaror | IT, appar, licenser |
| **5460** | Förbrukningsmaterial | Förpackning, emballage (Temu etc) |
| 5610 | Personbilskostnader | Bilkostnader |
| 5611 | Drivmedel | Bensin, diesel |
| **5700** | Frakter | ALL frakt och transport |
| **5810** | Biljetter | Resor, flyg, tåg |
| **5900** | Reklam och PR | ALL marknadsföring inkl TikTok, Google Ads |

---

## 6xxx - ÖVRIGA KOSTNADER

| Konto | Namn | Användning |
|-------|------|------------|
| 6212 | Mobiltelefon | Telefonabonnemang |
| 6310 | Företagsförsäkringar | Försäkringar (INGEN MOMS!) |
| **6500** | Övriga externa tjänster | Shopify, Google GSUITE, administration |
| **6570** | Bankkostnader | Alla bankavgifter, växlingsavgifter |
| 6590 | Övriga externa tjänster | Diverse tjänster |
| **6990** | Övriga externa kostnader | Förvaltning, diverse |
| 6991 | Övriga kostnader avdragsgilla | Avdragsgilla kostnader |

---

## 8xxx - FINANSIELLA POSTER

| Konto | Namn | Användning |
|-------|------|------------|
| **8311** | Ränteintäkter | Ränta från bank |
| **8400** | Räntekostnader | Ränta på lån/skulder |

---

# PENGAFLÖDE - HUR TRANSAKTIONER SKA BOKFÖRAS

## 1. FÖRSÄLJNING VIA SHOPIFY

```
Shopify-försäljning → 1580 (clearing)
     ↓
När pengar landar i Wise:
     Debet 1944/1945 (Wise EUR/SEK)
     Kredit 1580 (clearing nollställs)
```

**Exempel - Shopify sale:**
```
#VER A xxx yyyymmdd "Shopify Sale"
{
#TRANS 1580 {} 1250.00
#TRANS 3051 {} -1000.00
#TRANS 2611 {} -250.00
}
```

**Exempel - Shopify payout till Wise:**
```
#VER A xxx yyyymmdd "Shopify EUR payout"
{
#TRANS 1944 {} 1250.00
#TRANS 1580 {} -1250.00
}
```

---

## 2. VARUINKÖP FRÅN FUTURE WORLD TECH

**VIKTIGT:** Varor från Kina bokförs ALDRIG på 4000/4110 direkt!

```
Beställning → Lager (1460) ökar
          → Skuld till FWT (2441) ökar

Betalning → Wise/Bank minskar
         → Skuld (2441) minskar
```

**Exempel - Varuinköp FWT:**
```
#VER A xxx yyyymmdd "Varuinköp Future World Tech Q4"
{
#TRANS 1460 {} 415815.45 "Varuinköp - kläder"
#TRANS 2441 {} -415815.45 "Future World Tech skuld"
}
```

**Exempel - Betalning till FWT:**
```
#VER A xxx yyyymmdd "Future World Tech betalning"
{
#TRANS 2441 {} 295641.24
#TRANS 6570 {} 1358.76 "Överföringsavgift"
#TRANS 1945 {} -297000.00
}
```

---

## 3. VARUFÖRBRUKNING (KOSTNAD SÅLDA VAROR)

Vid kvartalsslut, flytta sålda varors kostnad från lager till resultat:

```
#VER A xxx yyyymmdd "Varuförbrukning Q1 2026"
{
#TRANS 4110 {} 150000.00 "Varuförbrukning sålda varor"
#TRANS 1460 {} -150000.00 "Lageruttag"
}
```

---

## 4. PERSONLIGA UTLÄGG (2893)

När ägaren betalar företagskostnader privat:

```
#VER A xxx yyyymmdd "Google GSUITE - privat betalning"
{
#TRANS 6500 {} 63.12
#TRANS 2893 {} -63.12
}
```

**⚠️ VIKTIGT:** 2893 ska ALLTID vara NEGATIVT (kredit) när företaget är skyldig personen pengar!

---

# MOMS-REGLER - KRITISKT!

## HAR MOMS (25%)
- Shopify-försäljning Sverige
- Programvaror från svenska bolag
- Lokalhyra med moms
- Kontorsmaterial
- Inrikes tåg (6% moms)

## HAR INGEN MOMS - LÄGG ALDRIG 2641!
| Typ | Anledning |
|-----|-----------|
| **Google (GSUITE, Ads, Play)** | Faktureras från Irland |
| **TikTok Ads** | Faktureras från utanför EU |
| **Facebook/Meta Ads** | Faktureras från Irland |
| **YouTube Premium** | Google = Irland |
| **Försäkringar (6310)** | Momsfritt i Sverige |
| **Skatteverket** | Myndighetsavgifter |
| **Internationella flygbiljetter** | Momsfritt |
| **Utländska telecom (YESIM etc)** | Utländsk tjänst |

---

# VALUTAHANTERING

## Wise-konton och valutor
| Konto | Valuta |
|-------|--------|
| 1940 | TRY (turkisk lira) |
| 1942 | USD |
| 1944 | EUR |
| 1945 | SEK |

## Valutakonvertering
ALLTID bokför i SEK-värdet, inte utländskt belopp!

**Exempel:**
```
#VER A xxx yyyymmdd "TikTok Ads EUR 23.45"
{
#TRANS 5900 {} 256.81  ← SEK-värde (23.45 × 10.95)
#TRANS 1944 {} -259.10 ← Faktiskt belopp från Wise
#TRANS 6570 {} 2.29    ← Valutaskillnad
}
```

---

# SE-FIL FORMAT

## Header (obligatorisk)
```
#FLAGGA 0
#PROGRAM "Spiris Bokföring" 7.5.0.0
#FORMAT PC8
#GEN 20260106 "Mohammad Sami Alsharef"
#SIETYP 4
#ORGNR 559489-5301
#FNAMN "Samis Jackets AB"
#RAR 0 20240701 20251231
#KPTYP EUBAS97
#VALUTA SEK
```

## VER-format
```
#VER A [nummer] [datum YYYYMMDD] "[beskrivning]"
{
#TRANS [konto] {} [belopp]
#TRANS [konto] {} [belopp]
}
```

## Encoding
- ALLTID CP437 (PC8)
- CRLF radbrytningar
- Svenska tecken: ö=\x94, ä=\x84, å=\x86, Ö=\x99, Ä=\x8E, Å=\x8F

---

# KVARTALSAVSTÄMNING - CHECKLISTA

## Före import till Visma

1. [ ] Alla VER balanserar (debet = kredit)
2. [ ] Total balans = 0.00 SEK
3. [ ] 1580 (Shopify clearing) = 0 vid periodens slut
4. [ ] Alla konton är definierade med #KONTO
5. [ ] Ingen moms på Google/TikTok/försäkring
6. [ ] 2893 är negativt (företaget skyldig ägaren)
7. [ ] Valutatransaktioner i SEK-belopp

## Python-verifiering
```python
import re
with open('file.se', 'r', encoding='cp437') as f:
    content = f.read()

# Check balance
trans = re.findall(r'#TRANS\s+\d+\s+\{\}\s+(-?[\d.]+)', content)
total = sum(float(t) for t in trans)
print(f'Balance: {total:.2f}')

# Check missing accounts
defined = set(re.findall(r'#KONTO\s+(\d+)', content))
used = set(re.findall(r'#TRANS\s+(\d+)', content))
missing = used - defined
print(f'Missing accounts: {missing}')
```

---

# VANLIGA FEL ATT UNDVIKA

| Fel | Rätt |
|-----|------|
| Moms på Google/TikTok | INGEN moms - utländska bolag |
| 2893 positivt belopp | 2893 NEGATIVT när företaget är skyldig |
| USD-belopp i SEK-konto | Konvertera ALLTID till SEK |
| Nytt konto utan #KONTO | Använd befintliga konton |
| Varuinköp direkt på 4110 | Via 1460 (lager) och 2441 (skuld) |

---

# DATAKÄLLOR - SANNINGSKÄLLOR

## CSV-filer (100% korrekta - ÄNDRA ALDRIG)
- `nordea/*.csv` - Nordea kontoutdrag
- `wise/*.csv` - Wise transaktioner
- `remamber/*.csv` - Remamber kort
- `worldline/*.csv` - Kortterminaler

## SE-filer (genererade)
- `final_se_files/Q[X]_2026_COMPLETE.se` - Slutgiltig fil för Visma

---

*Dokument skapat: 2026-01-06*
*Författare: AI Accounting Assistant*
*Version: 1.0*
