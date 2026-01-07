# SHOPIFY/STRIPE BOKFÖRINGSFLÖDE - KORREKT METOD

## Samis Jackets AB - Instruktioner för rätt bokföring

---

## ❌ PROBLEMET - VAD SOM BLEV FEL

Du har bokfört **samma försäljning två gånger**:

### Exempel på dubbelbokning:

**A812** (2025-11-28): "Överforing till Marginalen SEK 39934.97"
```
DEBET 1930 Marginalen    39,934.97
KREDIT 3051 Försäljning  31,947.98
KREDIT 2611 Moms         7,986.99
```

**A902** (samma dag): Samma belopp som försäljning IGEN!

⚠️ **Fel:** En överföring från Wise till Marginalen är INTE en ny försäljning!

---

## ✅ KORREKT BOKFÖRINGSFLÖDE

### Steg 1: Kund betalar via Shopify/Stripe (EUR)
**När:** Stripe tar emot kundens betalning

```
DEBET  1940 Wise EUR         €XXX (kundbetalning)
KREDIT 3051 Försäljning      SEK belopp ex moms
KREDIT 2611 Utgående moms    SEK moms 25%
```

**Detta är försäljningen!** Boka här, bara en gång.

---

### Steg 2: Stripe/Shopify betalar ut till Wise
**När:** Stripe överför till ditt Wise-konto

Om pengarna redan är på Wise: **Ingen bokning behövs**
(Stripe går direkt till Wise i de flesta fall)

Om du vill visa Stripe-mellansteg:
```
DEBET  1940 Wise EUR         €XXX
KREDIT 1XXX Stripe/Shopify   €XXX (mellonanvändningskonto)
```

---

### Steg 3: Du växlar EUR till SEK på Wise
**När:** Du konverterar EUR → SEK inne i Wise

```
DEBET  1945 Wise SEK         XXX SEK (efter växling)
KREDIT 1940 Wise EUR         XXX SEK (ursprungligt värde)
KREDIT/DEBET 3960/7960       Valutavinst/förlust
```

---

### Steg 4: Du överför SEK från Wise till Marginalen
**När:** Du flyttar pengar till företagskontot

```
DEBET  1930 Marginalen Bank  39,934.97
KREDIT 1945 Wise SEK         39,934.97
```

**⚠️ VIKTIGT:** Denna transaktion är BARA en överföring mellan dina egna konton. 
- INGEN ny försäljning!
- INGEN ny moms!
- Bara flytt av pengar!

---

## 📊 SAMMANFATTNING

| Händelse | Konto DEBET | Konto KREDIT | Försäljning? |
|----------|-------------|--------------|--------------|
| Kund betalar Stripe | 1940 Wise EUR | 3051 + 2611 | **JA** ✓ |
| Stripe → Wise | Redan på Wise | - | NEJ |
| Wise EUR → SEK | 1945 Wise SEK | 1940 Wise EUR | NEJ |
| Wise → Marginalen | 1930 Marginalen | 1945 Wise SEK | NEJ |

---

## 🔧 HUR DU FIXAR I VISMA

### Alternativ 1: Ta bort A812 eller A902
1. Gå till Verifikationer
2. Hitta A812 (eller A902)
3. Ta bort hela verifikationen

### Alternativ 2: Importera korrigeringsfilen
1. Importera `BOKSLUT_JUSTERINGAR_2025.se`
2. Den korrigerar automatiskt:
   - K2: Fixar A812 (från försäljning till överföring)
   - K3: Tar bort A902 dubbletten

---

## 📋 KONTROLLISTA FÖR FRAMTIDA BOKFÖRING

Innan du bokför en transaktion, fråga dig:

1. ☐ Är detta en kundbetalnig? → Bokför som FÖRSÄLJNING (3051 + 2611)
2. ☐ Är detta en överföring mellan mina egna konton? → Bokför som ÖVERFÖRING (bara tillgångskonton)
3. ☐ Har jag redan bokfört denna försäljning? → Dubbelkolla!

---

## 🎯 RÄTT TÄNK

```
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐    ┌───────────────┐
│   KUND      │───►│ Stripe/      │───►│ Wise EUR        │───►│ Wise SEK      │───►│ Marginalen    │
│  betalar    │    │ Shopify      │    │ (1940)          │    │ (1945)        │    │ (1930)        │
│             │    │              │    │                 │    │               │    │               │
└─────────────┘    └──────────────┘    └─────────────────┘    └───────────────┘    └───────────────┘
       │                                       │                     │                    │
       │                                       │                     │                    │
       ▼                                       ▼                     ▼                    ▼
   FÖRSÄLJNING                            INGET                 VÄXLING             ÖVERFÖRING
   3051 + 2611                            (redan                3960/7960           BARA 
                                          bokfört)              ev. vinst/          TILLGÅNGSKONTON
                                                                förlust
```

**Bara EN försäljningsbokning per kundorder!**

---

*Dokumentet skapat: 2026-01-06*
