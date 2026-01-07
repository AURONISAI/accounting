# 🔴 KRITISK REVISIONSPLAN - SAMIS JACKETS AB
## Bokslut 2024-07-01 till 2025-12-31

**Skapad:** 2026-01-06  
**Uppdaterad:** 2026-01-07  
**Utförs:** 2026-01-07 och framåt  
**Ansvarig:** Mohammad Sami Alsharef (VD/Bokförare)  
**Org.nr:** 559489-5301

---

# � NY STRATEGI: FULL RESET I VISMA

## Beslut: Börja om från 2025-10-01

Istället för att korrigera hundratals fel → **RESET och bygg rätt från början!**

### Varför reset?
- För många fel att korrigera individuellt
- Enklare att bygga rätt från start
- Renare bokföring = lättare revision
- Mindre risk för nya fel

---

# 📋 MASTER WORKFLOW - FULL RESET

## STEG 1: FÖRBEREDELSE (Innan reset)

| Status | Uppgift |
|--------|---------|
| ☐ | **EXPORTERA** nuvarande Huvudbok som backup |
| ☐ | **EXPORTERA** nuvarande Balansräkning som backup |
| ☐ | **EXPORTERA** nuvarande Resultaträkning som backup |
| ☐ | **SPARA** alla SE-filer som backup |
| ☐ | **DOKUMENTERA** alla kända saldon per 2025-09-30 |

---

## STEG 2: SAMLA KÄLLDATA (Rätt underlag)

### 2A. Bankkonton - Hämta verkliga saldon
| Status | Konto | Källa | Saldo 2025-09-30 | Saldo 2025-12-31 |
|--------|-------|-------|------------------|------------------|
| ☐ | 1930 Marginalen | Bankutdrag | _________ | _________ |
| ☐ | 1940 Wise EUR | Wise export | _________ | _________ |
| ☐ | 1945 Wise SEK | Wise export | _________ | _________ |
| ☐ | 1947 Wise USD | Wise export | _________ | _________ |
| ☐ | 1630 Skattekonto | Skatteverket | _________ | _________ |

### 2B. Försäljning - Hämta rätt data
| Status | Källa | Period | Antal ordrar | Belopp ex moms |
|--------|-------|--------|--------------|----------------|
| ☐ | Shopify | Okt-Dec 2025 | _________ | _________ |
| ☐ | Easy Cashier | Okt-Dec 2025 | _________ | _________ |
| ☐ | Worldline | Okt-Dec 2025 | _________ | _________ |
| ☐ | Klarna | Okt-Dec 2025 | _________ | _________ |

### 2C. Lager - Fysisk inventering
| Status | Uppgift |
|--------|---------|
| ☐ | Räkna ALLA produkter i lagerlokalen |
| ☐ | Dokumentera: Produkttyp, Antal, Inköpspris |
| ☐ | Beräkna totalt lagervärde (basket method) |
| ☐ | Jämför med Shopify inventory |

### 2D. Kostnader - Samla fakturor
| Status | Uppgift |
|--------|---------|
| ☐ | Hyra oktober-december |
| ☐ | Försäkringar |
| ☐ | Marknadsföring (TikTok, Facebook, Google) |
| ☐ | Frakt |
| ☐ | Övriga kostnader |

---

## STEG 3: RESET I VISMA

| Status | Uppgift |
|--------|---------|
| ☐ | **BACKUP:** Exportera allt före reset |
| ☐ | **RESET:** Ta bort Q4 2025 (oktober-december) |
| ☐ | **BEHÅLL:** Ingående balans per 2025-10-01 |
| ☐ | **VERIFIERA:** IB per 2025-10-01 är korrekt |

### Ingående Balans 2025-10-01 (ska vara korrekt)
```
Tillgångar:
- 1220 Inventarier: [från Q3 SE-fil]
- 1240 Bilar: [från Q3 SE-fil]
- 1460 Lager: [från Q3 SE-fil] (exkl FWT!)
- 1910 Kassa: [från Q3 SE-fil]
- 1930 Marginalen: [verkligt saldo 2025-09-30]
- Wise-konton: [verkliga saldon 2025-09-30]

Skulder:
- 2081 Aktiekapital: -25,000.00
- 2091 Balanserad förlust: [från Q3]
- 2893 Skuld närstående: [från Q3]
- Momsskuld: [beräknad Q3]
```

---

## STEG 4: BYGG NY SE-FIL FÖR Q4 2025

### Struktur för ny SE-fil
```
#FLAGGA 0
#FORMAT PC8
#SIETYP 4
#PROGRAM "Samis Jackets Clean Q4" 1.0
#GEN 20260107
#ORGNR 5594895301
#FNAMN "Samis Jackets AB"
#RAR 0 20240701 20251231

# === INGÅENDE BALANS 2025-10-01 ===
#IB 0 1220 [belopp]
#IB 0 1240 [belopp]
#IB 0 1460 [belopp]
... etc

# === OKTOBER 2025 ===
#VER A 1 20251001 "..."
...

# === NOVEMBER 2025 ===
#VER A xx 20251101 "..."
...

# === DECEMBER 2025 ===
#VER A xx 20251201 "..."
...

# === BOKSLUTSJUSTERINGAR ===
#VER B 1 20251231 "Moms Q4"
#VER B 2 20251231 "Avskrivningar"
#VER B 3 20251231 "Årets resultat"
```

---

## STEG 5: KORREKT BOKFÖRINGSLOGIK

### ⚠️ KRITISK REGEL: INGEN DUBBELBOKNING!

```
┌─────────────────────────────────────────────────────────────────────┐
│  FÖRSÄLJNING BOKFÖRS ENDAST EN GÅNG - VID STRIPE/SHOPIFY BETALNING  │
│                                                                      │
│  Kund → Stripe → Wise = FÖRSÄLJNING (3051 + 2611)                   │
│  Wise → Marginalen = INTERN ÖVERFÖRING (bara 1930 ↔ 1945)           │
│                                                                      │
│  ❌ ALDRIG bokför försäljning vid Wise→Marginalen överföring!       │
└─────────────────────────────────────────────────────────────────────┘
```

### 5A. Försäljning (Shopify/Stripe) - ENDAST HÄR BOKFÖRS FÖRSÄLJNING
```
NÄR: Stripe bekräftar betalning till Wise
DEBET  1940/1945 Wise     [belopp inkl moms]
KREDIT 3051 Försäljning   [belopp ex moms]
KREDIT 2611 Utg moms 25%  [moms]

⚠️ DETTA ÄR ENDA TILLFÄLLET ATT BOKFÖRA SHOPIFY-FÖRSÄLJNING!
```

### 5A2. Intern överföring Wise → Marginalen (INGEN FÖRSÄLJNING!)
```
NÄR: Du flyttar pengar från Wise till Marginalen
DEBET  1930 Marginalen    [belopp]
KREDIT 1945 Wise SEK      [belopp]

❌ INGEN försäljning!
❌ INGEN moms!
✓ Bara flytt mellan egna konton
✓ Bokför ENDAST från 1930-sidan (Marginalen kontoutdrag)
```

### 5B. Försäljning (Easy Cashier/Worldline)
```
NÄR: Worldline insättning till Marginalen
DEBET  1930 Marginalen    [belopp inkl moms]
KREDIT 3051 Försäljning   [belopp ex moms]
KREDIT 2611 Utg moms 25%  [moms]

✓ HÄR bokförs försäljning eftersom Worldline = direkt från kund
```

### 5C. Kontantförsäljning
```
DEBET  1910 Kassa         [belopp inkl moms]
KREDIT 3051 Försäljning   [belopp ex moms]
KREDIT 2611 Utg moms 25%  [moms]
```

### 5C2. Kassa → Låneåterbetalning (slutet av perioden)
```
NÄR: 2025-12-31 - Kontanter betalas till närstående som låneåterbetalning
DEBET  2893 Skuld närstående  [kassa-saldo]
KREDIT 1910 Kassa             [kassa-saldo]

⚠️ VIKTIGT: All kassa per 2025-12-31 betalades som låneåterbetalning!
Kassa-saldo efter denna bokning = 0 kr
```

### 5D. Inköp med moms
```
DEBET  [kostnadskonto]    [belopp ex moms]
DEBET  2641 Ing moms      [moms]
KREDIT 1930 Bank          [belopp inkl moms]
```

### 5E. Kostnad sålda varor (KSV)
```
Baserat på VERKLIG inventering + basket method:

DEBET  4110 KSV           [antal sålda × genomsnittspris]
KREDIT 1460 Lager         [samma belopp]
```

---

## STEG 6: ANTI-DUBBLERINGS REGLER

### 🚫 REGLER FÖR ATT UNDVIKA DUBBELBOKNING

| Regel | Beskrivning |
|-------|-------------|
| **R1** | Shopify-försäljning bokförs ENDAST vid Stripe→Wise, ALDRIG vid Wise→Marginalen |
| **R2** | Interna överföringar mellan egna konton = ENDAST kontosaldo-flytt, ingen försäljning |
| **R3** | Varje transaktion får endast bokföras EN gång från EN källa |
| **R4** | Marginalen-transaktioner: Använd Marginalen kontoutdrag som källa |
| **R5** | Wise-transaktioner: Använd Wise export som källa |
| **R6** | Om samma belopp syns i både Wise och Marginalen = INTERN ÖVERFÖRING, bokför endast en gång |

### Kontrollflöde för att undvika dubbelbokningar:

```
INNAN DU BOKFÖR, FRÅGA:

1. Är detta en KUNDBETALNING?
   JA → Bokför som försäljning (3051 + 2611)
   NEJ → Gå till steg 2

2. Är detta en ÖVERFÖRING mellan egna konton?
   JA → Bokför ENDAST som kontoöverföring (1930 ↔ 1940/1945)
        Bokför från MOTTAGARENS kontoutdrag (t.ex. Marginalen)
   NEJ → Gå till steg 3

3. Är detta en KOSTNAD/UTGIFT?
   JA → Bokför som kostnad med moms
   NEJ → Undersök vidare

4. HAR JAG REDAN BOKFÖRT DENNA TRANSAKTION?
   JA → STOPPA! Dubbelbokning!
   NEJ → OK att bokföra
```

---

## STEG 7: VIKTIGA REGLER

### ❌ TA INTE MED I 2025:
| Vad | Varför |
|-----|--------|
| Future World Tech fakturor | Varorna anländer februari 2026 |
| Ej levererade varor | Bokförs vid leverans |
| Förskottsbetalningar till FWT | Bokförs som fordran, ej lager |

### ✅ TA MED I 2025:
| Vad | Hur |
|-----|-----|
| Alla FAKTISKA banktransaktioner | Från kontoutdrag |
| Alla LEVERERADE varor | Med korrekt värde |
| Alla BETALDA kostnader | Med moms separerat |
| Alla BEKRÄFTADE försäljningar | Från Shopify + Easy Cashier |

---

## STEG 7: KVALITETSKONTROLL

### Kontrollpunkter innan bokslut
| Status | Kontroll | Förväntat |
|--------|----------|-----------|
| ☐ | Alla bankkonton = verkligt saldo | ✓ Inga negativa |
| ☐ | 1630 Skattekonto = SKV saldo | ✓ Stämmer |
| ☐ | 1460 Lager = fysisk inventering | ✓ Stämmer |
| ☐ | 3051 × 1.25 = totalt inkl moms | ✓ Stämmer |
| ☐ | 2611 = 3051 × 0.25 | ✓ Stämmer |
| ☐ | Balansräkning balanserar | ✓ T = S + EK |
| ☐ | Inga negativa tillgångskonton | ✓ Alla ≥ 0 |

---

## STEG 8: BOKSLUT OCH LÅS

| Status | Uppgift |
|--------|---------|
| ☐ | Importera ren SE-fil till Visma |
| ☐ | Kör Huvudbok - kontrollera |
| ☐ | Kör Balansräkning - ska balansera |
| ☐ | Kör Resultaträkning - beräkna resultat |
| ☐ | Bokför momsskuld Q4 (till 2650) |
| ☐ | Bokför avskrivningar |
| ☐ | Bokför årets resultat till 2099 |
| ☐ | **LÅS PERIODEN 2025-12-31** |
| ☐ | Exportera slutlig SE-fil som backup |

---

### ❌ PROBLEM 1: Konto 1940 Övriga bankkonton = -47,203.66 kr
| Status | Uppgift |
|--------|---------|
| ☐ | **UTREDNING:** Identifiera vilket bankkonto 1940 representerar |
| ☐ | Kontrollera ALLA verifikationer på konto 1940 |
| ☐ | Jämför med verkligt bankutdrag |
| ☐ | Identifiera felaktiga bokningar |
| ☐ | Skapa korrigeringsverifikationer |
| ☐ | Verifiera att saldo = 0 eller korrekt positivt belopp |

**🔴 HITTAT FEL - Verifikation A781:**
```
A779: SEK till TRY 12,432.54 SEK (debet) ✓
A780: EUR till TRY 1,430.21 SEK (debet) ✓
A781: Loan repayment TRY 61,066.41 → BOKFÖRT SOM 61,066.41 SEK (kredit) ❌

FELET: TRY är INTE SEK!
61,066 TRY ÷ 4.43 kurs = ca 13,786 SEK
Differens: 61,066 - 13,786 = 47,280 SEK FEL!
```

**KORRIGERING:**
```
DEBET  1940  47,280.00 kr (minska krediten)
KREDIT 2893  47,280.00 kr (minska skuld närstående)
```

**Audit Flow:**
```
1. Huvudbok → Exportera alla transaktioner på 1940
2. Bankutdrag → Hämta verkligt saldo
3. Jämför rad för rad
4. Hitta differens
5. Korrigera felbokningar
```

---

### ❌ PROBLEM 2: Konto 1630 Skattekonto = -6,581.00 kr
| Status | Uppgift |
|--------|---------|
| ☐ | **UTREDNING:** Logga in på Skatteverket och hämta verkligt saldo |
| ☐ | Exportera skattekontoutdrag från SKV |
| ☐ | Jämför med bokfört saldo |
| ☐ | Identifiera: A651 Arbetsförmedlingen FEL bokförd på 1630 |
| ☐ | Flytta A651 (9,119 kr) till konto 3990 (bidrag/stöd) |
| ☐ | Verifiera alla momsbetalningar är korrekt bokförda |
| ☐ | Stäm av till 0 kr (eller korrekt belopp enligt SKV) |

**Kända fel:**
- A651: Arbetsförmedlingen 9,119 kr bokförd som KREDIT 1630 → Ska vara KREDIT 3990
- Efter korrigering: -6,581 + 9,119 = +2,538 kr

---

### ❌ PROBLEM 3: Momskonton - Fullständig avstämning krävs

#### 3A. Konto 2611 Utgående moms 25% = -84,610.44 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Exportera alla transaktioner på 2611 |
| ☐ | Beräkna: Försäljning 3051 × 25% = förväntad moms |
| ☐ | Jämför med bokförd moms |
| ☐ | Identifiera differenser |
| ☐ | Korrigera felbokningar |

**Kontroll:**
- 3051 Försäljning: 788,606.16 kr
- Förväntad moms 25%: 788,606.16 × 0.25 = 197,151.54 kr
- Bokförd 2611: 84,610.44 kr (?)
- **DIFFERENS: ~112,500 kr - VARFÖR?**

---

#### 3B. Konto 2615 Utgående moms import = 0.00 kr ✓
| Status | Uppgift |
|--------|---------|
| ☐ | Verifiera att importmoms är korrekt nollställd |
| ☐ | Kontrollera mot 2645 (ska vara lika) |

---

#### 3C. Konto 2641 Ingående moms = 10,954.62 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Kontrollera att alla inköp med moms är bokförda |
| ☐ | Verifiera mot leverantörsfakturor |
| ☐ | Stäm av mot periodens kostnader |

---

#### 3D. Konto 2645 Beräknad ingående moms förvärv = 0.00 kr ✓
| Status | Uppgift |
|--------|---------|
| ☐ | Verifiera att importmoms är korrekt matchad mot 2615 |

---

#### 3E. Konto 2650 Momsredovisning = 400.00 kr
| Status | Uppgift |
|--------|---------|
| ☐ | **UTREDNING:** Vad är dessa 400 kr? |
| ☐ | Ska vara 0 efter alla momsbetalningar |
| ☐ | Identifiera obetalda momsperioder |
| ☐ | Beräkna Q4 2025 moms att betala |

---

### ❌ PROBLEM 4: Future World Tech (FWT) fakturor - MÅSTE TAS BORT
| Status | Uppgift |
|--------|---------|
| ☐ | **KRITISKT:** FWT-varorna har INTE anlänt ännu (anländer februari 2026) |
| ☐ | Identifiera ALLA FWT-relaterade verifikationer |
| ☐ | Ta bort/reversera alla FWT-bokningar från konto 1460 (lager) |
| ☐ | Ta bort/reversera alla FWT-bokningar från konto 2441 (leverantörsskuld) |
| ☐ | Ta bort/reversera alla FWT-relaterade betalningar |
| ☐ | Varor som inte anlänt = INTE bokföras förrän leverans |
| ☐ | Bokför FWT när varorna faktiskt anländer i februari 2026 |

**Princip:**
```
Varor ska bokföras när de LEVERERAS, inte när faktura skickas!
FWT-leverans: Februari 2026 → Bokförs i 2026, INTE 2025
```

**Åtgärd:**
- Hitta alla verifikationer med "Future World Tech" eller "FWT"
- Skapa reverseringsverifikationer
- Ta bort från 2025 bokslut
- Lägg in på nytt när varorna anländer 2026

---

### ❌ PROBLEM 5: Kostnad Sålda Varor (KSV) - OMRÄKNING KRÄVS
| Status | Uppgift |
|--------|---------|
| ☐ | **STEG 1:** Räkna fysiskt lager i lagerlokal (inventering 2025-12-31) |
| ☐ | **STEG 2:** Hämta Shopify försäljningsrapport (antal sålda produkter) |
| ☐ | **STEG 3:** Hämta Easy Cashier försäljningsrapport (antal sålda produkter) |
| ☐ | **STEG 4:** Beräkna totalt antal sålda enheter |
| ☐ | **STEG 5:** Beräkna genomsnittspris per enhet (basket/weighted average) |
| ☐ | **STEG 6:** Multiplicera antal sålda × genomsnittspris = Verklig KSV |
| ☐ | **STEG 7:** Jämför med bokförd KSV (konto 4110) |
| ☐ | **STEG 8:** Korrigera differens |

**Basket Logic - Beräkningsmetod:**
```
STEG 1: Inventering
- Räkna alla produkter i lagerlokalen
- Dokumentera: Produkttyp, Antal, Inköpspris

STEG 2: Beräkna totalt inköp
- Summa av alla inköpsfakturor (exkl FWT som ej anlänt)
- Total inköpskostnad ÷ Total antal inköpta = GENOMSNITTSPRIS

STEG 3: Beräkna sålda enheter
- Shopify: Exportera ordrar → Räkna antal produkter
- Easy Cashier: Exportera kvitton → Räkna antal produkter
- TOTAL SÅLD = Shopify + Easy Cashier

STEG 4: Verklig KSV
- KSV = Antal sålda × Genomsnittspris per enhet

STEG 5: Kontrollera
- Bokförd KSV (4110): 487,504.98 kr
- Verklig KSV: ??? kr
- Om differens → Korrigera
```

**Formel:**
```
Genomsnittspris = (Ingående lager + Inköp) ÷ (Ingående antal + Inköpt antal)

KSV = Antal sålda enheter × Genomsnittspris

Utgående lager = (Ingående antal + Inköpt antal - Sålt antal) × Genomsnittspris
```

---

## 🟡 PRIORITET 2: BANKKONTON ATT VERIFIERA

### Konto 1941 Viva Wallet = -0.55 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Kontrollera Viva Wallet saldo |
| ☐ | Korrigera öresavrundning om nödvändigt |

---

### Konto 1942 Wise USD = 1,749.90 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Logga in på Wise |
| ☐ | Exportera USD-kontoutdrag |
| ☐ | Jämför med bokfört saldo |
| ☐ | Korrigera valutadifferenser |

---

### Konto 1943 Wise GBP = 1,847.99 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Exportera GBP-kontoutdrag från Wise |
| ☐ | Beräkna SEK-värde med aktuell kurs |
| ☐ | Korrigera valutadifferenser |

---

### Konto 1944 Wise EUR = 2,004.58 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Exportera EUR-kontoutdrag från Wise |
| ☐ | Beräkna SEK-värde med aktuell kurs |
| ☐ | Korrigera valutadifferenser |

---

### Konto 1945 Wise SEK = 8,166.88 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Verifiera mot Wise SEK-saldo |
| ☐ | Stäm av mot kontoutdrag |

---

### Konto 1947 Worldline = 10,971.97 kr
| Status | Uppgift |
|--------|---------|
| ☐ | Logga in på Worldline |
| ☐ | Verifiera innestående belopp |
| ☐ | Kontrollera att alla insättningar till Marginalen är bokförda |

---

## 🟡 PRIORITET 3: KOSTNADER ATT GRANSKA

### Konto 6570 Bankkostnader = 13,922.88 kr
| Status | Uppgift |
|--------|---------|
| ☐ | **UTREDNING:** Är detta rimligt för 18 månader? |
| ☐ | Exportera alla transaktioner på 6570 |
| ☐ | Granska varje post |
| ☐ | Identifiera eventuella felbokningar |
| ☐ | Flytta kostnader till rätt konto om nödvändigt |

**Beräkning:**
- 18 månader × 70 kr/månad avgift = 1,260 kr
- Övriga avgifter: ~2,000 kr rimligt
- **Bokfört 13,922 kr = Troligen FEL!**

---

## 🟢 PRIORITET 4: SLUTFÖRANDE

### Steg-för-steg Bokslut i Visma

| Steg | Status | Uppgift |
|------|--------|---------|
| 1 | ☐ | Korrigera alla fel identifierade ovan |
| 2 | ☐ | Importera BOKSLUT_JUSTERINGAR_2025.se |
| 3 | ☐ | Verifiera alla bankkonton mot utdrag |
| 4 | ☐ | Kör Huvudbok - kontrollera inga negativa bankkonton |
| 5 | ☐ | Kör Balansräkning - ska balansera |
| 6 | ☐ | Kör Resultaträkning - beräkna årets resultat |
| 7 | ☐ | Bokför momsskuld Q4 (2611→2650) |
| 8 | ☐ | Bokför avskrivningar (om ej gjort) |
| 9 | ☐ | Bokför årets resultat till 2099 |
| 10 | ☐ | Lås perioden 2025-12-31 |
| 11 | ☐ | Skapa årsredovisning |
| 12 | ☐ | Signera och arkivera |

---

# 🔍 AUDIT WORKFLOW - FULLSTÄNDIG VERIFIERING

## DAG 1: Bankkonton

### Morning: Samla alla kontoutdrag
```
□ Marginalen - Hämta saldo 2025-12-31
□ Wise - Exportera alla valutor
□ Worldline - Hämta rapport
□ Viva Wallet - Om aktiv, hämta saldo
□ Skatteverket - Logga in och hämta skattekontoutdrag
```

### Afternoon: Jämförelse
```
□ Skapa Excel med: Konto | Bokfört | Verkligt | Differens
□ Identifiera alla differenser
□ Lista alla korrigeringar som behövs
```

---

## DAG 2: Korrigeringar

### Skapa korrigeringsverifikationer
```
□ En verifikation per korrigering
□ Tydlig beskrivning: "Korrigering av fel X"
□ Dokumentera i separat fil
```

### Importera till Visma
```
□ Testa i testmiljö först om möjligt
□ Importera SE-fil
□ Kontrollera att saldon stämmer
```

---

## DAG 3: Moms

### Momsavstämning
```
□ Beräkna utgående moms från försäljning
□ Beräkna ingående moms från inköp
□ Jämför med bokförda värden
□ Korrigera differenser
□ Beräkna Q4 2025 momsdeklaration
```

---

## DAG 4: Bokslut

### Slutjusteringar
```
□ Avskrivningar
□ Periodiseringar (om några)
□ Årets resultat
□ Balansräkning balanserar
```

### Lås perioden
```
□ Visma → Inställningar → Lås period
□ Välj 2025-12-31
□ Bekräfta
```

---

# 📊 VERIFIERINGSCHECKLISTA FÖR REVISOR

## Bankkonton
| Konto | Bokfört | Verkligt | Differens | Åtgärd | OK |
|-------|---------|----------|-----------|--------|-----|
| 1930 Marginalen | 90,532.72 | ? | ? | | ☐ |
| 1940 Övriga | -47,203.66 | 0 | ? | KRITISK | ☐ |
| 1941 Viva | -0.55 | ? | ? | | ☐ |
| 1942 Wise USD | 1,749.90 | ? | ? | | ☐ |
| 1943 Wise GBP | 1,847.99 | ? | ? | | ☐ |
| 1944 Wise EUR | 2,004.58 | ? | ? | | ☐ |
| 1945 Wise SEK | 8,166.88 | ? | ? | | ☐ |
| 1947 Worldline | 10,971.97 | ? | ? | | ☐ |
| 1630 Skattekonto | -6,581.00 | 0 | ? | KRITISK | ☐ |

## Momskonton
| Konto | Bokfört | Beräknat | Differens | Åtgärd | OK |
|-------|---------|----------|-----------|--------|-----|
| 2611 Utg moms | -84,610.44 | ? | ? | KRITISK | ☐ |
| 2641 Ing moms | 10,954.62 | ? | ? | | ☐ |
| 2650 Momsred | 400.00 | 0 | 400 | | ☐ |

---

# ✅ SKATTEKONTO 1630 - KORRIGERAT 2026-01-07

## Bakgrund
Skattekontot (1630) stämde inte med Skatteverkets kontoutdrag.

| Period | Före korrigering | Efter korrigering | Skatteverket | Status |
|--------|------------------|-------------------|--------------|--------|
| Q1-Q3 | -6,581 kr | 100 kr | 100 kr | ✅ |
| Q4 | - | 108 kr | 108 kr | ✅ |

## Skapade korrigeringsfiler

| Fil | Syfte | Verifikationer |
|-----|-------|----------------|
| `SKATTEKONTO_1630_KORRIGERING_Q1-Q3.se` | Korrigera Q1-Q3 till 100 kr | K3-K15 |
| `SKATTEKONTO_1630_Q4_2025.se` | Q4 transaktioner 100→108 kr | S1-S6 |

## Q1-Q3 Korrigeringar (summa +6,681 kr)

| Ver | Datum | Beskrivning | Belopp |
|-----|-------|-------------|--------|
| K3 | 2025-06-12 | Arb.avg + skatt maj debitering | -16,233 kr |
| K4 | 2025-06-12 | Anställningsstöd IN juni → 3980 | +21,027 kr |
| K5 | 2025-07-05 | Intäktsränta | +7 kr |
| K6 | 2025-07-08 | Inbetalning moms | +20,707 kr |
| K7 | 2025-07-09 | Moms sept 2024 beslut | +1,485 kr |
| K8 | 2025-07-09 | Moms okt-dec 2024 beslut | +16,027 kr |
| K9 | 2025-07-14 | Arb.avg + skatt juni | -6,707 kr |
| K10 | 2025-07-14 | Anställningsstöd IN juli → 3980 | +9,112 kr |
| K11 | 2025-08-02 | Intäktsränta | +116 kr |
| K12 | 2025-08-12 | Moms jan-mar 2025 beslut | -11,551 kr |
| K13 | 2025-08-18 | Moms apr-jun 2025 | -26,668 kr |
| K14 | 2025-09-06 | Ränta (netto) | -16 kr |
| K15 | 2025-09-30 | Flytta A166 till Q4 (fel datum) | -625 kr |

## Q4 Transaktioner (från Marginalen 1930)

| Ver | Datum | Beskrivning | Från 1930 | Till 1630 |
|-----|-------|-------------|-----------|-----------|
| S1 | 2025-10-09 | Inbetalning till skattekonto | -625 kr | +625 kr |
| S1K | 2025-10-09 | Korr A847 (var ej förseningsavgift) | - | - |
| S2 | 2025-10-29 | Inbetalning moms Q3 | -15,714 kr | +15,714 kr |
| S3 | 2025-11-01 | Intäktsränta | - | +3 kr |
| S4 | 2025-11-12 | Förseningsavgift → 6530 | - | -625 kr |
| S5 | 2025-11-12 | Moms jul-sep debiterat | - | -15,714 kr |
| S6 | 2025-12-06 | Intäktsränta | - | +5 kr |

### ⚠️ OBS: A847 i MARGINALEN_Q4_2025.se var FEL!
A847 bokförde 625 kr som förseningsavgift (6590) på 2025-10-08.
Men enligt Skatteverket:
- 2025-10-09: INBETALNING +625 kr (inte förseningsavgift!)
- 2025-11-12: Förseningsavgift -625 kr (DENNA är förseningsavgiften!)

**S1K korrigerar detta genom att återföra felaktig 6590-bokning.**

## Motkonton

| Skattekonto-transaktion | Motkonto |
|-------------------------|----------|
| Arbetsgivaravgift/skatt debitering | 2510 Skatteskulder |
| Anställningsstöd IN | 3980 Erhållna bidrag |
| Inbetalning moms | 2650 Momsredovisning |
| Momsdebitering | 2650 Momsredovisning |
| Intäktsränta | 8314 Skattefria ränteintäkter |
| Förseningsavgift | 6530 Förseningsavgifter |
| Betalning från bank | 1930 Marginalen |

---

# 📁 DOKUMENT ATT SAMLA

| Dokument | Status | Plats |
|----------|--------|-------|
| ✅ Marginalen kontoutdrag 2025-12-31 | HÄMTAT | Q4_2025_PERIOD/ |
| ☐ Wise kontoutdrag alla valutor | | |
| ☐ Worldline rapport | | |
| ✅ Skatteverket skattekontoutdrag | HÄMTAT | CSV bifogat |
| ☐ Alla leverantörsfakturor Q4 | | |
| ☐ Alla kundfakturor Q4 | | |
| ☐ Låneavtal Ahmed Gheyath | | last results csv/ |
| ☐ Styrelsebeslut VD utan lön | | last results csv/ |
| ☐ Lagerinventering 2025-12-31 | | |

---

# ⚠️ VARNINGAR FÖR REVISION

## Röda flaggor att förklara:

1. **Skuld närstående 1.6 MSEK** 
   - ✓ Dokumenterat med låneavtal
   
2. **VD utan lön**
   - ✓ Dokumenterat med styrelsebeslut
   
3. **Högt lager (983k) vs låg försäljning (789k)**
   - Förklaring: Uppstartsfas, stort initialt inköp

4. **Förlust första året**
   - Normalt för uppstartsbolag

5. **Skattekonto korrigerat**
   - ✅ Avstämt mot Skatteverkets kontoutdrag
   - ✅ Korrigeringsfiler skapade

---

# 🎯 MÅL: REVISIONSÄKER BOKFÖRING

Efter att alla steg är slutförda ska:

- ✅ Skattekonto stämma med SKV (KLART!)
- ✓ Alla bankkonton ha korrekt saldo (inte negativt om ej kredit)
- ✓ Moms vara korrekt beräknad och bokförd
- ✓ Balansräkning balansera
- ✓ Alla transaktioner ha verifikation
- ✓ Alla lån vara dokumenterade
- ✓ Årsredovisning vara komplett

---

*Skapad: 2026-01-06*
*Uppdaterad: 2026-01-07 (Skattekonto 1630 avstämt)*
*Version: 2.0*
*Nästa granskning: Efter Q4 import*
