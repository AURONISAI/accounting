# 🧾 MOMSREGLER FÖR TJÄNSTER - SAMIS JACKETS AB
## Referens för bokföring av inköp från olika leverantörer

---

## 📋 SNABBGUIDE

| Typ av tjänst | Moms? | Kontroll |
|---------------|-------|----------|
| Svenska tjänster (standard) | ✅ JA 25% | Dra av ingående moms 2641 |
| EU-tjänster B2B (omvänd skattskyldighet) | ✅ JA 25% | Redovisa omvänd moms 2614/2641 |
| Tjänster utanför EU | ❌ NEJ | Ingen moms att dra av |
| Digitala annonser (TikTok, Google, Meta) | ❌ NEJ | Inget momsavdrag* |

*Digitala annonser från Irland/utlandet - omvänd skattskyldighet kan tillämpas men ofta ej värt administrationen för småföretag.

---

## 🇸🇪 SVENSKA TJÄNSTER (25% MOMS)

### Teleoperatörer
| Leverantör | Moms | Konto |
|------------|------|-------|
| **Hallon** | ✅ 25% | 6212 (ex moms) + 2641 |
| Telia | ✅ 25% | 6212 + 2641 |
| Telenor | ✅ 25% | 6212 + 2641 |
| Tre | ✅ 25% | 6212 + 2641 |

**Beräkning:** Hallon 129 SEK inkl moms = 103.20 ex moms + 25.80 ingående moms

### Frakt & Transport
| Leverantör | Moms | Konto |
|------------|------|-------|
| **Shipit.se** | ✅ 25% | 5710 (ex moms) + 2641 |
| Postnord | ✅ 25% | 5710 + 2641 |
| Schenker | ✅ 25% | 5710 + 2641 |

### Bensin & Drivmedel
| Leverantör | Moms | Konto |
|------------|------|-------|
| **St1** | ✅ 25% | 5610 (ex moms) + 2641 |
| **Circle K** | ✅ 25% | 5610 (ex moms) + 2641 |
| Preem | ✅ 25% | 5610 + 2641 |
| OKQ8 | ✅ 25% | 5610 + 2641 |

### Myndigheter & Registreringar
| Leverantör | Moms | Konto |
|------------|------|-------|
| **Bolagsverket** | ❌ NEJ | 6991 |
| **PRV** | ❌ NEJ | 6991 |
| Skatteverket | ❌ NEJ | 6991 |

### Tandvård & Sjukvård
| Leverantör | Moms | Konto |
|------------|------|-------|
| **Folktandvården** | ❌ NEJ | Momsfri sjukvård |

---

## 🌐 DIGITALA TJÄNSTER (UTLÄNDSKA)

### Annonsering - INGEN MOMS ATT DRA AV
| Leverantör | Land | Moms i Sverige | Konto |
|------------|------|----------------|-------|
| **TikTok Ads** | Irland | ❌ NEJ* | 5900 |
| **Meta/Facebook Ads** | Irland | ❌ NEJ* | 5900 |
| **Google Ads** | Irland | ❌ NEJ* | 5900 |

*Tekniskt: Omvänd skattskyldighet kan tillämpas (köpare redovisar moms), men för småföretag under omsättningsgräns eller för enkelhetens skull bokförs ofta hela beloppet som kostnad utan momshantering.

### Programvara & Appar
| Leverantör | Land | Moms | Konto |
|------------|------|------|-------|
| **Shopify** | Irland/Kanada | EU-land med omvänd moms | 5420/6570 |
| **Google Play** | Irland | ✅ 25% (EU-moms ingår) | 5420 |
| **YouTube Premium** | Irland | ✅ 25% (EU-moms ingår) | 5420 |
| **One.com** | Danmark | ✅ 25% (dansk moms) | 5420 |

### E-handel
| Leverantör | Land | Moms | Konto |
|------------|------|------|-------|
| **Temu** | Kina | ❌ NEJ | 4010 (varor) |

---

## ✈️ RESOR

### Flygbiljetter
| Leverantör | Moms | Konto |
|------------|------|-------|
| **Booking.com Flights** | ❌ NEJ (momsfri transport) | 5810 |
| SAS | ❌ NEJ | 5810 |
| Norwegian | ❌ NEJ | 5810 |

### Tåg & Kollektivtrafik
| Leverantör | Moms | Konto |
|------------|------|-------|
| **Mälardalen Trafik** | ✅ 6% (lågbeskattad) | 5810 + 2641 (6%) |
| SJ | ✅ 6% | 5810 + 2641 |

### Hotell & Logi
| Typ | Moms | Konto |
|-----|------|-------|
| Hotell Sverige | ✅ 12% | 5810 + 2641 (12%) |
| Hotell utomlands | ❌ NEJ | 5810 |

### Mat på resa
| Typ | Moms | Konto |
|-----|------|-------|
| Restaurang Sverige | ✅ 12% | 5810 + 2641 (12%) |
| Mat utomlands | ❌ NEJ | 5810 |
| **Jureskog Arlanda** | ✅ 12% | 5810 + 2641 |
| **Forex** | ✅ 25% | 5810 + 2641 |

---

## 📌 BOKFÖRINGSEXEMPEL

### Svenska tjänster med 25% moms:
```
Shipit.se 1,000 SEK inkl moms:
DEBIT  5710 Frakt          800.00
DEBIT  2641 Ingående moms  200.00
KREDIT 1944 Wise EUR    -1,000.00
```

### Utländska annonser utan moms:
```
TikTok Ads 1,962 SEK:
DEBIT  5900 Marknadsföring  1,962.00
KREDIT 1944 Wise EUR       -1,962.00
```

### Bensin med 25% moms:
```
St1 2,000 SEK inkl moms (netto efter återbetalning 415.94):
DEBIT  5610 Drivmedel        332.75
DEBIT  2641 Ingående moms     83.19
KREDIT 1944 Wise EUR        -415.94
```

---

## ⚠️ VIKTIGT ATT KOMMA IHÅG

1. **Kvitto krävs** för momsavdrag - spara alla kvitton!
2. **Omvänd skattskyldighet** gäller B2B-köp från EU för digitala tjänster
3. **Förenklad bokföring** - för småföretag kan det vara enklare att bokföra utan momsavdrag på små utlandsköp
4. **Bensinavdrag** - endast för fordon i företaget med körjournal

---

*Uppdaterad: 2026-01-05*
*Källa: Skatteverket.se, BFN vägledningar*
