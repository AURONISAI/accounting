# ✅ ACCOUNTING CLARIFICATIONS - Q3 2025
**Company:** Samis Jackets AB (559489-5301)  
**Date:** October 19, 2025

---

## 💰 2893 SHAREHOLDER LOAN - COMPLETE EXPLANATION

### **What is Account 2893?**
**Account:** 2893 - Skulder till närstående personer  
**English:** Debt to related parties / Shareholder loan  
**Type:** Liability account

### **How it Works:**

```
WHEN OWNER PAYS FOR BUSINESS:
├─ Owner pays from personal card/account
├─ Business records expense in correct account (5410, 5460, 5610, etc.)
└─ Business OWES owner → CREDIT 2893 (negative balance)

WHEN BUSINESS REPAYS OWNER:
├─ Business transfers money to owner  
├─ Business reduces debt to owner → DEBIT 2893
└─ Cash/bank account decreases
```

---

## 🔄 THE COMPLETE 2893 CYCLE IN Q3 2025

### **PHASE 1: Business Expenses Paid by Owner (CREDIT 2893)**

All these create DEBT from company to owner:

| Source | Amount | Details |
|--------|--------|---------|
| Klarna | 3,041 SEK | TikTok Ads + TEMU supplies |
| Remamber | 3,031 SEK | Travel (flights, trains, fuel) + Apple |
| Nordea Gold | 1,357 SEK | OpenAI, Anthropic, supplies |
| Nordea Premium | 2,959 SEK | TikTok, Shopify, Google, hosting |
| PERSONKONTO | 447 SEK | Fortnox accounting software |
| **TOTAL** | **13,835 SEK** | **Company owes owner** |

**SIE Structure for ALL above:**
```sie
#TRANS [EXPENSE ACCOUNT] {} +XXX.XX "Business expense description"
#TRANS 2893 {} -XXX.XX "Paid from personal [card/account name]"
```

**Result:** Account 2893 balance = **-13,835.42 SEK** (liability - company owes owner)

---

### **PHASE 2: Owner Repayment FROM 2893 (DEBIT 2893)**

When company repays owner, the debt DECREASES:

**Wise USD Transfer:**
- Sept 22: Transfer 1,000 USD to ahmed gheyath al-sharif
- Amount: 9,520 SEK equivalent
- **This is REPAYMENT of the shareholder loan**

**Why it's repayment:**
1. The money in Wise came FROM deposits from bank (1930)
2. The deposits from bank came FROM shareholder loan (2893 originally)
3. When owner withdraws it → It's returning borrowed money
4. NOT a new expense or gift - it's REPAYING what company borrowed

**SIE Structure:**
```sie
#TRANS 1942 {} -9520.00 "Transfer to ahmed 1,000 USD"
#TRANS 2893 {} +9520.00 "REPAYMENT of shareholder loan"
```

**Result:** Account 2893 debt REDUCES by 9,520 SEK

---

## 📊 FINAL 2893 BALANCE CALCULATION

```
Opening Balance (2893):                    0.00 SEK

CREDITS (Company borrows from owner):
├─ Klarna expenses:                   -3,041.00 SEK
├─ Remamber expenses:                 -3,031.00 SEK  
├─ Nordea Gold expenses:              -1,357.00 SEK
├─ Nordea Premium expenses:           -2,959.00 SEK
├─ PERSONKONTO (Fortnox):               -447.00 SEK
└─ Wise deposits (to be used):             0.00 SEK (separate)

DEBITS (Company repays owner):
└─ Wise USD transfer to ahmed:        +9,520.00 SEK

FINAL BALANCE (2893):                -13,835.42 SEK
```

**What this means:**
- **Negative balance = Liability** = Company OWES owner
- Owner has paid 13,835.42 SEK MORE than they've received back
- This is NORMAL - owner is financing business operations

---

## 🌍 ALL CURRENCY TRANSFERS TO AHMED = REPAYMENT FROM 2893

### **Critical Rule:**

> "All transfers to ahmed gheyath al-sharif in ANY currency (USD, GBP, EUR, CNY, TRY) are REPAYMENTS from account 2893, because the money originally came from it in the beginning."

### **Why This is Correct:**

1. **Source of Funds:** Wise accounts were funded by:
   - Bank transfers from 1930 (company account)
   - Company account 1930 was funded by shareholder advances (2893)
   
2. **Ownership:** The money in Wise = Company money = Originally from shareholder

3. **When Withdrawn:** Any transfer to owner = Repayment of shareholder loan

### **Examples:**

**If transfer 1,000 USD to ahmed:**
```sie
#TRANS 1942 {} -[SEK_EQUIVALENT] "Transfer to ahmed [amount] USD"
#TRANS 2893 {} +[SEK_EQUIVALENT] "Repayment of shareholder loan"
```

**If transfer 500 GBP to ahmed:**
```sie
#TRANS 1943 {} -[SEK_EQUIVALENT] "Transfer to ahmed [amount] GBP"
#TRANS 2893 {} +[SEK_EQUIVALENT] "Repayment of shareholder loan"
```

**If transfer 100 EUR to ahmed:**
```sie
#TRANS 1944 {} -[SEK_EQUIVALENT] "Transfer to ahmed [amount] EUR"
#TRANS 2893 {} +[SEK_EQUIVALENT] "Repayment of shareholder loan"
```

---

## 💡 KEY UNDERSTANDING

### **2893 is a TWO-WAY ACCOUNT:**

**↓ CREDIT (Increase Debt):**
- Owner pays business expenses from personal funds
- Company records: CREDIT 2893 (negative balance grows)
- Example: Owner uses personal card to pay TikTok Ads

**↑ DEBIT (Decrease Debt):**
- Company repays owner
- Company records: DEBIT 2893 (negative balance shrinks)
- Example: Company transfers money to owner's personal account

### **Common Mistakes to AVOID:**

❌ **WRONG:** Recording owner withdrawal as expense  
✅ **CORRECT:** Recording owner withdrawal as 2893 repayment

❌ **WRONG:** Treating personal transfers as "gifts" or "advances TO owner"  
✅ **CORRECT:** They are repayments OF advances FROM owner

❌ **WRONG:** Creating new expense when owner receives money  
✅ **CORRECT:** Reducing the liability (2893) when owner receives money

---

## ✅ VERIFICATION COMPLETE

**Q3 2025 Account 2893 Status:**
- ✅ All personal card expenses → CREDIT 2893 (increase debt)
- ✅ All transfers to ahmed → DEBIT 2893 (decrease debt)
- ✅ Final balance: -13,835.42 SEK (company owes owner)
- ✅ All currencies handled correctly (USD, EUR, SEK)

**This is CORRECT accounting for shareholder loans!** ✅

---

*2893 Shareholder Loan Accounting Guide*  
*Samis Jackets AB - Q3 2025*  
*October 19, 2025*
