# 📖 SAMIS JACKETS AB - ACCOUNTING MASTER GUIDE
## Q1 2026 (January 1 - March 31, 2026)

---

# ⚠️ READ THIS FIRST - CRITICAL INFORMATION

## 🎯 WHAT TO UPLOAD TO VISMA
**ONLY upload the final combined SE file:**
```
final_se_files/Q1_2026_COMPLETE.se
```

This single file contains ALL transactions for the quarter, properly balanced and formatted.

---

# 📁 FOLDER STRUCTURE

```
Q1_2026_PERIOD_2026-01_TO_2026-03/
├── README.md                    ← YOU ARE HERE (Master Guide)
├── accounting_rules/            ← DO NOT MODIFY - Reference only
│   └── ACCOUNTING_RULES.md
├── source_csv/                  ← RAW BANK EXPORTS (Source of Truth)
│   ├── nordea/
│   │   ├── Nordea_Gold_Q1_2026.csv
│   │   ├── Nordea_Premium_Q1_2026.csv
│   │   └── Nordea_Personkonto_Q1_2026.csv
│   ├── marginalen/
│   │   └── Marginalen_Q1_2026.csv
│   ├── wise/
│   │   ├── statement_SEK.csv
│   │   ├── statement_EUR.csv
│   │   ├── statement_USD.csv
│   │   ├── statement_GBP.csv
│   │   └── statement_TRY.csv
│   ├── amex/
│   │   └── amex_Q1_2026.csv
│   ├── worldline/
│   │   └── worldline_Q1_2026.csv
│   └── sales_data/
│       └── shopify_orders_Q1_2026.csv
├── standalone_se_files/         ← Individual SE files per source
│   ├── AMEX_Q1_2026.se
│   ├── WISE_Q1_2026.se
│   ├── MARGINALEN_Q1_2026.se
│   ├── WORLDLINE_Q1_2026.se
│   ├── SALES_Q1_2026.se
│   ├── INVENTORY_Q1_2026.se
│   ├── NORDEA_PERSONKONTO_Q1_2026.se
│   ├── NORDEA_PREMIUM_Q1_2026.se
│   └── NORDEA_GOLD_Q1_2026.se
└── final_se_files/              ← COMBINED FILE FOR VISMA
    └── Q1_2026_COMPLETE.se      ← UPLOAD THIS TO VISMA
```

---

# 🏦 BANK ACCOUNTS (KONTOKLASS 1)

| Account | Name | Description |
|---------|------|-------------|
| **1220** | Inventarier | Equipment/Fixtures |
| **1460** | Lager | Inventory/Stock |
| **1582** | Shopify fordran | Shopify settlement (EUR→SEK) |
| **1910** | Kassa | Cash register |
| **1930** | Marginalen Bank | Primary business bank |
| **1941** | Viva Wallet | Card payment platform |
| **1942** | Wise USD | Multi-currency USD |
| **1944** | Wise EUR | Multi-currency EUR |
| **1945** | Wise SEK | Multi-currency SEK |
| **1946** | Wise TRY | Multi-currency TRY |
| **1947** | Worldline avräkning | POS card payment settlement |

---

# 💰 REVENUE ACCOUNTS (KONTOKLASS 3)

| Account | Name | VAT | Use For |
|---------|------|-----|---------|
| **3001** | Försäljning SE 25% | 25% | Swedish domestic sales |
| **3051** | Övrig försäljning | Varies | Other sales |
| **3740** | Öres/kronorsavrundning | 0% | Rounding differences |

---

# 📦 COST OF GOODS SOLD (KONTOKLASS 4)

| Account | Name | Use For |
|---------|------|---------|
| **4000** | Inköp varor | Purchase of goods for resale |
| **4110** | Varuinköp | Cost of goods sold |
| **4545** | Tull/importavgifter | Customs duties |

---

# 💸 EXPENSE ACCOUNTS (KONTOKLASS 5-6)

## WITH 25% VAT DEDUCTION
| Account | Name | Example Merchants |
|---------|------|-------------------|
| **5010** | Lokalhyra | Rent, Lagar Hyra |
| **5410** | Programvaror | Fortnox, Google Suite, Shopify |
| **5460** | Förbrukningsinventarier | Office supplies, TEMU business |
| **6110** | Kontorsmaterial | Office materials |
| **6250** | Administrativa avgifter | Bolagsverket, registration |

## WITHOUT VAT DEDUCTION (0%)
| Account | Name | Example Merchants |
|---------|------|-------------------|
| **5020** | Resor tjänsteresor | SJ, Mälardalstrafiken, flights |
| **5610** | Resekostnader | Travel expenses general |
| **5620** | Bilförsäkring | Vehicle insurance |
| **5900** | Annonsering | TikTok, Facebook, Google Ads |
| **6310** | Försäkring | Insurance (NO VAT in Sweden) |
| **6570** | Bankavgifter | Bank fees, Wise fees |

---

# 📊 MOMS (VAT) ACCOUNTS (KONTOKLASS 26)

| Account | Name | Use For |
|---------|------|---------|
| **2610** | Utgående moms 25% | Output VAT on sales |
| **2641** | Ingående moms | Input VAT on purchases |
| **2650** | Redovisningskonto moms | VAT paid to Skatteverket |

---

# 👤 LIABILITY ACCOUNTS (KONTOKLASS 2)

| Account | Name | Use For |
|---------|------|---------|
| **2893** | Skuld Samis (ägare) | Shareholder debt - personal expenses |

---

# 🔄 SETTLEMENT ACCOUNT METHOD (Avräkningsmetoden)

## The Three-Step Process:

### Step 1: SALE (Record when sale happens)
```
#VER A XXX YYYYMMDD "Daily Sales"
{
#TRANS 1947 {} 1250.00       ← Worldline receivable (DEBIT)
#TRANS 3001 {} -1000.00      ← Sales revenue (CREDIT)
#TRANS 2610 {} -250.00       ← Output VAT 25% (CREDIT)
}
```

### Step 2: SETTLEMENT (Record when money arrives in bank)
```
#VER A XXX YYYYMMDD "Worldline settlement"
{
#TRANS 1930 {} 1250.00       ← Bank receives (DEBIT)
#TRANS 1947 {} -1250.00      ← Worldline cleared (CREDIT)
}
```

### Step 3: FEES (Record platform fees separately)
```
#VER A XXX YYYYMMDD "Worldline fee"
{
#TRANS 6570 {} 15.00         ← Bank fee (DEBIT)
#TRANS 1947 {} -15.00        ← Reduces receivable (CREDIT)
}
```

## Expected Account Balances at Period End:
- **1947 (Worldline)**: Should equal pending settlements not yet received
- **1582 (Shopify)**: Should equal pending Shopify payouts = **0 at end**

---

# 💱 MULTI-CURRENCY ACCOUNTING (CRITICAL!)

## ⚠️ ALL AMOUNTS MUST BE IN SEK

Swedish accounting requires all amounts in SEK. When recording foreign currency transactions:

### Currency Exchange Entry:
```
#VER A XXX YYYYMMDD "SEK till USD 2870 SEK kurs 0.105"
{
#TRANS 1945 {} -2870.00      ← SEK leaves (DEBIT source)
#TRANS 1942 {} 2857.14       ← SEK VALUE of USD received (CREDIT)
#TRANS 6570 {} 12.86         ← Exchange fee (DEBIT)
}
```

### ❌ WRONG - Using foreign currency amounts:
```
#TRANS 1942 {} 300.00        ← This is USD, not SEK!
```

### ✅ CORRECT - Using SEK equivalent:
```
#TRANS 1942 {} 2857.14       ← SEK value of 300 USD
```

### Exchange Rate Calculation:
- Get rate from Wise CSV "Exchange Rate" column
- Multiply foreign amount × rate = SEK value
- Or use: Source SEK amount - fees = destination SEK value

---

# 👤 PERSONAL ACCOUNT TRANSACTIONS

When company expenses are paid from PERSONAL bank accounts (Nordea Personkonto, Klarna, Remamber):

### Pattern:
```
#VER A XXX YYYYMMDD "Fortnox Bokföringsprogram"
{
#TRANS 6700 {} 119.20        ← Expense (DEBIT)
#TRANS 2641 {} 29.80         ← Input VAT (DEBIT)
#TRANS 2893 {} -149.00       ← Company owes person (CREDIT - NEGATIVE!)
}
```

### ⚠️ CRITICAL: 2893 MUST BE NEGATIVE
- Personal pays company expense → Company owes person
- This creates a LIABILITY (credit = negative)
- CSV shows: -149.00 (money left personal account)
- SE file: 2893 {} -149.00 (company owes 149)

---

# 📋 SE FILE FORMAT (SIE4 Standard)

## File Encoding: CP437 (PC8)
Swedish characters in CP437:
- ä = \x84
- ö = \x94  
- å = \x86
- Ä = \x8E
- Ö = \x99
- Å = \x8F

## File Structure:
```
#FLAGGA 0
#PROGRAM "Samis Jackets Accounting" 1.0
#FORMAT PC8
#GEN 20260106
#SIETYP 4
#FNAMN "Samis Jackets AB"
#ORGNR 559362-2498
#RAR 0 20260101 20260331

#VER A 1 20260105 "Description"
{
#TRANS 5410 {} 119.20
#TRANS 2641 {} 29.80
#TRANS 1930 {} -149.00
}

#VER A 2 20260106 "Another transaction"
{
#TRANS 5900 {} 500.00
#TRANS 2893 {} -500.00
}
```

## VER Format:
```
#VER A [VER_NUMBER] [YYYYMMDD] "Description"
{
#TRANS [ACCOUNT] {} [AMOUNT]
#TRANS [ACCOUNT] {} [AMOUNT]
}
```

## Rules:
1. Each VER must balance (debits = credits, sum = 0)
2. VER numbers must be sequential (1, 2, 3...)
3. Dates in YYYYMMDD format
4. Amounts: positive = debit, negative = credit
5. Line endings: CRLF (\r\n)

---

# ⚠️ COMMON ERRORS & FIXES

## Error 1: Wrong VAT on Insurance
❌ Wrong:
```
#TRANS 6310 {} 3010.40    ← 80% of total
#TRANS 2641 {} 752.60     ← 20% VAT
#TRANS 1930 {} -3763.00
```
✅ Correct (Insurance has NO VAT in Sweden):
```
#TRANS 6310 {} 3763.00    ← Full amount
#TRANS 1930 {} -3763.00
```

## Error 2: Wrong Sign on Personal Expenses
❌ Wrong:
```
#TRANS 2893 {} 149.00     ← POSITIVE = wrong!
```
✅ Correct:
```
#TRANS 2893 {} -149.00    ← NEGATIVE = company owes person
```

## Error 3: Foreign Currency Not Converted
❌ Wrong:
```
#TRANS 1942 {} 320.00     ← USD amount, not SEK!
```
✅ Correct:
```
#TRANS 1942 {} 2944.00    ← SEK equivalent (320 USD × 9.2)
```

## Error 4: Settlement Account Not Cleared
❌ Problem: 1582 or 1947 shows balance at period end
✅ Fix: Ensure all settlements are recorded, or add missing sale/settlement entries

## Error 5: Duplicate Transactions
❌ Problem: Same transaction appears twice
✅ Check: Same date + same amount + same description = likely duplicate
✅ Solution: Verify against CSV source, remove true duplicates

---

# 🔍 AUDIT CHECKLIST

Before finalizing Q1_2026_COMPLETE.se:

## Balance Checks:
- [ ] Total balance = 0 (all debits equal all credits)
- [ ] Each VER block balances individually
- [ ] 1582 (Shopify) = 0 (all settled) or equals pending payouts
- [ ] 1947 (Worldline) = pending deposits only

## Source Verification:
- [ ] All Marginalen CSV transactions accounted for
- [ ] All Wise CSV transactions accounted for  
- [ ] All AMEX CSV transactions accounted for
- [ ] All Nordea personal account business transactions accounted for
- [ ] Sales data matches Shopify/EasyCashier reports

## Format Checks:
- [ ] File encoding is CP437
- [ ] All VER numbers are sequential
- [ ] All dates are YYYYMMDD format
- [ ] No foreign currency amounts (all in SEK)

---

# 📊 VAT CALCULATION REFERENCE

## Swedish VAT Rate: 25%

### From Total (inkl. moms) to Net:
```
Net = Total ÷ 1.25
VAT = Total - Net = Total × 0.20
```

**Example:** 149.00 SEK total
- Net: 149.00 ÷ 1.25 = 119.20 SEK
- VAT: 149.00 × 0.20 = 29.80 SEK

### From Net (exkl. moms) to Total:
```
VAT = Net × 0.25
Total = Net × 1.25
```

---

# 📅 PERIOD DATES

| Quarter | Start Date | End Date | SE File Name |
|---------|------------|----------|--------------|
| Q1 2026 | 2026-01-01 | 2026-03-31 | Q1_2026_COMPLETE.se |
| Q2 2026 | 2026-04-01 | 2026-06-30 | Q2_2026_COMPLETE.se |
| Q3 2026 | 2026-07-01 | 2026-09-30 | Q3_2026_COMPLETE.se |
| Q4 2026 | 2026-10-01 | 2026-12-31 | Q4_2026_COMPLETE.se |

---

# 🤖 AI INSTRUCTIONS

When processing accounting for Samis Jackets AB:

1. **CSV files are SOURCE OF TRUTH** - never modify them
2. **All amounts in SEK** - convert foreign currencies
3. **Each VER must balance** - sum of all TRANS = 0
4. **2893 for personal expenses is NEGATIVE** (credit)
5. **Insurance (6310) has NO VAT** in Sweden
6. **Advertising (5900) has NO VAT** deduction
7. **Check settlement accounts** (1582, 1947) clear properly
8. **Use CP437 encoding** for Swedish characters
9. **Sequential VER numbering** starting from 1
10. **Verify against CSV** before finalizing

---

**Last Updated:** 2026-01-06
**Created By:** Accounting AI System
**Company:** Samis Jackets AB (559362-2498)
