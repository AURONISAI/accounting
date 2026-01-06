# SAMIS JACKETS AB - ACCOUNTING RULES REFERENCE
## DO NOT MODIFY - Reference Only

---

## EXPENSE CLASSIFICATION

### WITH 25% VAT (Ingående moms 2641)

| Account | Description | Merchants |
|---------|-------------|-----------|
| 5010 | Lokalhyra (Rent) | Lagar Hyra, office rent |
| 5410 | Programvaror (Software) | Fortnox, Visma, Google Suite, Shopify |
| 5460 | Förbrukningsinventarier | TEMU business, Hemköp, Clas Ohlson |
| 6110 | Kontorsmaterial | Office supplies |
| 6250 | Administrativa avgifter | Bolagsverket |
| 6700 | Bokföringskostnader | Accounting software |

### WITHOUT VAT (0% / Undantag)

| Account | Description | Merchants |
|---------|-------------|-----------|
| 5020 | Resekostnader | SJ, Mälardalstrafiken, flights |
| 5610 | Reskostnader | Travel, hotels |
| 5620 | Bilförsäkring | Vehicle insurance |
| 5900 | Annonsering | TikTok, Facebook, Google Ads |
| 6310 | Företagsförsäkring | All insurance premiums |
| 6570 | Bankavgifter | Bank fees, Wise fees |
| 6800 | Skatteavgifter | Skatteverket fees |

---

## PAYMENT SOURCE → CREDIT ACCOUNT

| Payment Source | Account | Type |
|----------------|---------|------|
| Marginalen Bank | 1930 | Business |
| Wise SEK | 1945 | Business |
| Wise EUR | 1944 | Business |
| Wise USD | 1942 | Business |
| Wise TRY | 1946 | Business |
| Nordea Personkonto | 2893 | Personal |
| Nordea Premium | 2893 | Personal |
| Nordea Gold | 2893 | Personal |
| Klarna | 2893 | Personal |
| Remamber/Golf | 2893 | Personal |
| AMEX | 2893 | Personal |

---

## SALES RECOGNITION

### Worldline (POS in-store)
```
Debit  1947  Total amount (inc. VAT)
Credit 3001  Net sales (excl. VAT)
Credit 2610  Output VAT 25%
```

### Shopify (Online EUR)
```
Debit  1582  Total amount in SEK
Credit 3001  Net sales (excl. VAT)
Credit 2610  Output VAT 25%
```

### Cash Sales
```
Debit  1910  Total amount
Credit 3001  Net sales (excl. VAT)
Credit 2610  Output VAT 25%
```

---

## SETTLEMENT ENTRIES

### Worldline → Marginalen
```
Debit  1930  Settlement amount
Credit 1947  Same amount (clears receivable)
```

### Shopify → Wise
```
Debit  1944  EUR amount in SEK
Credit 1582  Same amount (clears receivable)
```

---

## CURRENCY EXCHANGE RULES

1. ALL amounts must be in SEK
2. Use exchange rate from Wise statement
3. Source SEK = Destination SEK + Fees
4. Record fee in 6570

Example: 2870 SEK → 300 USD
```
#TRANS 1945 {} -2870.00     ← SEK out
#TRANS 1942 {} 2857.14      ← SEK value of USD
#TRANS 6570 {} 12.86        ← Exchange fee
```

---

## PERSONAL EXPENSE RULES

When business expense is paid from personal account:

```
#TRANS [EXPENSE] {} [Net amount]
#TRANS 2641 {} [VAT amount]         ← Only if VAT applicable
#TRANS 2893 {} -[Total amount]      ← ALWAYS NEGATIVE!
```

⚠️ 2893 MUST BE NEGATIVE (credit = company owes person)

---

## NO-VAT EXPENSES

These expense types NEVER have VAT deduction:
- Insurance (6310) - VAT exempt in Sweden
- Advertising (5900) - Foreign platforms
- Bank fees (6570) - Financial services
- Travel tickets (5020) - Transport services
- Government fees (6800) - Public services

---

## YEAR-END CLOSING CHECKLIST

- [ ] All bank accounts reconciled
- [ ] Settlement accounts cleared (1582, 1947)
- [ ] Inventory count completed
- [ ] VAT declarations filed
- [ ] Personal account (2893) reconciled
- [ ] All VER entries balanced
