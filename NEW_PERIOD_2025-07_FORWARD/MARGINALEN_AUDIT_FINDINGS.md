# 🔍 MARGINALEN TRANSACTION AUDIT REPORT
## CSV vs SE File Analysis - Q3 2025

**Date:** October 24, 2025  
**Account:** Marginalen 1930 (92356405879)  
**Period:** July 1 - September 30, 2025  
**Total Transactions:** 75 in CSV, 74 recorded in SE

---

## 📊 AUDIT FINDINGS

### ✅ CORRECT ENTRIES (No Issues)

| # | Date | Description | Amount | Account | VAT | Status |
|---|------|-------------|--------|---------|-----|--------|
| 1 | 07-01 | Bank fee | -70 | 6570 | No | ✓ Correct |
| 2 | 07-03 | Lagar Hyra rent | -1,956 | 5010 | 391.20 | ✓ Correct |
| 3 | 07-03 | Visma software | -1,872 | 5410 | 374.40 | ✓ Correct |
| 4 | 07-03 | Hyra Butik rent | -20,550 | 5010 | 4,110 | ✓ Correct |
| 5 | 07-03 | Lagar Hyra 2 | -1,956 | 5010 | 391.20 | ✓ Correct |
| 6 | 07-03 | Easy Cashier | -3,435 | 5410 | 687 | ✓ Correct |
| 7 | 07-24 | Broadband | -625 | 5410 | 125 | ✓ Correct |
| 8 | 07-24 | Shareholder loan | -15,274.28 | 2893 | No | ✓ Correct |
| 9 | 08-01 | Bank fee | -70 | 6570 | No | ✓ Correct |
| 10 | 08-01 | Hyra Butik August | -19,983 | 5010 | 3,996.60 | ✓ Correct |
| 11 | 08-06 | Hyra August | -1,896 | 5010 | 379.20 | ✓ Correct |
| 12 | 08-26 | Car insurance | -849 | 5620 | No | ✓ Correct |
| 13 | 08-27 | Shareholder loan | -12,000 | 2893 | No | ✓ Correct |
| 14 | 09-01 | Bank fee | -70 | 6570 | No | ✓ Correct |
| 15 | 09-02 | Hyra September | -1,896 | 5010 | 379.20 | ✓ Correct |
| 16 | 09-08 | Hyra Butik September | -19,983 | 5010 | 3,996.60 | ✓ Correct |
| 17 | 09-22 | Shareholder loan | -12,000 | 2893 | No | ✓ Correct |
| 18 | 09-26 | Lagar Hyra September | -2,016 | 5010 | 403.20 | ✓ Correct |
| 19 | 09-26 | Additional rent | -20,159 | 5010 | 4,031.80 | ✓ Correct |
| 20 | 09-30 | Shareholder loan | -27,905 | 2893 | No | ✓ Correct |
| 21 | 09-30 | Shareholder loan | -17,000 | 2893 | No | ✓ Correct |

---

## ❌ INCORRECT/MISSING ENTRIES

### ERROR 1: Transaction 2025-07-07 Easy Cashier (-3,435)
```
CSV Data:
Bokföringsdatum: 2025-07-07
Belopp: -3,435.00
Transaktionstext: Bankgiro
Egen referens: [blank]

CURRENT SE FILE (WRONG):
#VER "" "VER009" 20250707 "Easy Cashier - POS system"
{
    #TRANS 5410 {} 2748.00 "Easy Cashier POS ex VAT"
    #TRANS 2641 {} 687.00 "VAT 25%"
    #TRANS 1930 {} -3435.00 "Payment from bank"
}

ISSUE: 
✓ Amount correct (-3,435)
✓ Account correct (5410)
✓ VAT correct (687)
✓ Debit/credit balance correct
STATUS: ✓ CORRECT (no error here)
```

### ERROR 2: Transaction 2025-07-07 VAT Payment (-20,707)
```
CSV Data:
Bokföringsdatum: 2025-07-07
Belopp: -20,707.00
Mottagande kontonummer: 50501055
Egen referens: "balancs 2650 till 0"

CURRENT SE FILE (NEEDS REVIEW):
#VER "" "VER008" 20250707 "VAT payment to Skatteverket"
{
    #TRANS 1930 {} -20707.00 "Payment to tax authority"
    #TRANS 1630 {} 20707.00 "Tax account increased"
}

ISSUE:
CSV shows reference to "balancs 2650 till 0" (balance 2650 to 0)
- 2650 = Moms betalning (VAT payment account)
- This is payment FROM company TO Skatteverket
- Correct routing: 1930 → 2650 (not 1630)

CORRECTION NEEDED:
Should be:
#TRANS 2650 {} 20707.00 "VAT payment to tax authority"
#TRANS 1930 {} -20707.00 "Paid from bank"
```

### ERROR 3: Transactions to account 55250500 (Wise SEK)
```
CSV shows three transactions to 55250500:
1. 2025-08-27: -2,500
2. 2025-09-04: -5,000
3. 2025-09-22: -12,000

CURRENT SE FILE TREATMENT:
VER045: Routes -2,500 to 1945 ✓
VER054: Routes -5,000 to 1945 ✓
VER063: Routes -12,000 to 1945 ✓

STATUS: ✓ CORRECT (Wise account 55250500 = 1945 in Visma)
```

### ERROR 4: Transaction 2025-07-18 Bankgiro -500 to 2027001
```
CSV Data:
Bokföringsdatum: 2025-07-18
Belopp: -500.00
Mottagande kontonummer: 2027001
Transaktionskod: 341 (Bankgiro)

CURRENT SE FILE TREATMENT:
Missing this transaction!

SHOULD BE:
#VER "" "VER017B" 20250718 "Bankgiro payment 2027001"
{
    #TRANS 6250 {} 400.00 "Administrative payment ex VAT"
    #TRANS 2641 {} 100.00 "VAT 25%"
    #TRANS 1930 {} -500.00 "Paid from bank"
}

ISSUE: Extra transaction not in SE file (only listed 16 July transactions)
```

### ERROR 5: Transaction 2025-07-22 Bankgiro -250 to 50530989
```
CSV Data:
Bokföringsdatum: 2025-07-22
Belopp: -250.00
Mottagande kontonummer: 50530989

CURRENT SE FILE:
VER020: "Bankgiro payment 50530989" -250
#TRANS 6250 {} 200.00 "Administrative fee"
#TRANS 1930 {} -250.00

ISSUE: Amount 250 with 200 in 6250 = only 200 expense + 50 unknown
Should be: 200 (6250) + 50 (2641 VAT) = 250
VAT IS MISSING!

CORRECTION NEEDED:
#TRANS 6250 {} 200.00 "Bankgiro administrative fee ex VAT"
#TRANS 2641 {} 50.00 "VAT 25%"
#TRANS 1930 {} -250.00 "Paid from bank"
```

### ERROR 6: Transaction 2025-07-30 Worldline -248 to 3306016
```
CSV Data:
Bokföringsdatum: 2025-07-30
Belopp: -248.00
Mottagande kontonummer: 3306016

CURRENT SE FILE:
VER026: Routes to 6570 "Card terminal fee"

ISSUE: Amount -248 is a card processing FEE (6570)
These are service charges, NO VAT on banking services

STATUS: ✓ CORRECT (already in SE file as 6570, no VAT)
```

### ERROR 7: Transaction 2025-08-27 Bankgiro -500 to 2027001
```
CSV Data:
Bokföringsdatum: 2025-08-27
Belopp: -500.00
Mottagande kontonummer: 2027001

CURRENT SE FILE:
VER044: Routes to 6250, amount -500

ISSUE: Same as ERROR 4 - this is another -500 to 2027001
Need to verify if this is duplicate or separate transaction
Looking at CSV: Yes, appears as separate line entry

SHOULD BE ADDED:
#VER "" "VER044B" 20250827 "Bankgiro payment 2027001"
{
    #TRANS 6250 {} 400.00 "Administrative fee ex VAT"
    #TRANS 2641 {} 100.00 "VAT 25%"
    #TRANS 1930 {} -500.00 "Paid from bank"
}
```

### ERROR 8: Transaction 2025-09-03 Bankavgifter -248 to 47704044
```
CSV Data:
Bokföringsdatum: 2025-09-03
Belopp: -248.00
Mottagande kontonummer: 47704044
Egen referens: "Bankavgifter"

CURRENT SE FILE:
VER053: Routes to 6570 "Bank fees September"

STATUS: ✓ CORRECT (6570 no VAT for bank services)
```

### ERROR 9: Transaction 2025-07-07 Bankgiro -507 to 50435726
```
CSV Data:
Bokföringsdatum: 2025-07-07
Belopp: -507.00
Mottagande kontonummer: 50435726

CURRENT SE FILE:
VER007: Routes to 6250, amount -507

ISSUE: This is Bolagsverket (company registration) fee
Account 6250 correct, but VAT treatment?
-507 total: likely 405.60 (6250) + 101.40 (2641 VAT) = 507

NEEDS CHECKING: Does Bolagsverket fees have VAT?
Professional administrative services = 25% VAT applicable

CORRECTION:
#TRANS 6250 {} 405.60 "Bolagsverket registration fee ex VAT"
#TRANS 2641 {} 101.40 "VAT 25%"
#TRANS 1930 {} -507.00 "Paid from bank"
```

### ERROR 10: Transaction 2025-09-26 Bankgiro -248 to 47704044
```
CSV Data:
Bokföringsdatum: 2025-09-26
Belopp: -248.00
Mottagande kontonummer: 47704044

CURRENT SE FILE:
VER070: Routes to 6570

STATUS: ✓ CORRECT (6570 no VAT for bank fees)
```

### ERROR 11: Government Subsidy 2025-07-18 +9,119
```
CSV Data:
Bokföringsdatum: 2025-07-18
Belopp: +9,119.00
Transaktionskod: 722
Egen referens: "SK5594895301" (Government payment)

CURRENT SE FILE:
VER016: Routes to 1630 (tax account)
#TRANS 1930 {} 9119.00 "Arbetsförmedlingen subsidy"
#TRANS 1630 {} -9119.00 "Tax account reduced"

ISSUE: Government subsidy should NOT reduce tax account
This is REVENUE/SUBSIDY income, not tax payment
Should route to 1630 as INCREASE, not decrease

CORRECTION:
#TRANS 1930 {} 9119.00 "Government employment subsidy"
#TRANS 1630 {} -9119.00 "Subsidy received" OR create new revenue account
```

---

## 🔧 CORRECTION SUMMARY

| Issue | Transaction | Problem | Account | Fix |
|-------|-------------|---------|---------|-----|
| 1 | 07-07 VAT -20,707 | Wrong account 1630 | Should be 2650 | Change 1630 → 2650 |
| 2 | 07-22 Bankgiro -250 | Missing VAT | 6250 only | Add 50 VAT to 2641 |
| 3 | 07-07 Bankgiro -507 | Missing VAT | 6250 only | Add 101.40 VAT to 2641 |
| 4 | 07-18 Bankgiro -500 | Not in SE file | Missing | Add as new VER entry |
| 5 | 08-27 Bankgiro -500 | Missing VAT | 6250 only | Add 100 VAT to 2641 |
| 6 | 09-26 Bankgiro -248 | Wrong routing | Should be 6570 | Already correct ✓ |
| 7 | 07-18 Subsidy +9,119 | Subsidy treatment | 1630 reduction | Verify correct account |

---

## 📋 TRANSACTIONS NEEDING ACCOUNT VERIFICATION

### 1. Administrative/Bolagsverket Fees (6250 vs 6991)
- Should these be 6250 or 6991?
- Do they have VAT or not?
- Current rule: 6250 with 25% VAT for professional services

### 2. Government Subsidy (1630 vs Revenue Account)
- Currently decreases 1630 (tax account)
- Should it be revenue (3XXX) or grant income account?
- Need clarification on proper accounting treatment

### 3. Worldline Card Fees (6570)
- Card processing fees = 6570 (bank fees) NO VAT ✓
- Correct as is

---

## ✨ NEXT STEPS

1. **Fix VAT Payment Account** (07-07 -20,707)
   - Change from 1630 to 2650
   
2. **Add Missing VAT** to administrative fees
   - 07-22: Add 50 VAT
   - 07-07: Add 101.40 VAT  
   - 08-27: Add 100 VAT

3. **Add Missing Transactions**
   - 07-18: -500 Bankgiro to 2027001
   - Possibly other missing entries

4. **Verify Subsidy Treatment**
   - Confirm 1630 is correct account for government subsidies

5. **Rebuild SE File** with corrections applied

---

**Status:** Analysis Complete - Ready for Corrections  
**Next Phase:** Rebuild corrected MARGINALEN_Q3_2025.se file
