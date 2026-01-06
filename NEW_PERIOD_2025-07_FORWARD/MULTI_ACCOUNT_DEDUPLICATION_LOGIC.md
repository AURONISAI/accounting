# 🔄 MULTI-ACCOUNT DEDUPLICATION LOGIC
## NO DOUBLE-ENTRY OF SAME TRANSACTION

**Date:** October 24, 2025  
**Purpose:** Master reference for handling transactions across multiple SE files  
**Status:** ACTIVE RULE

---

## 🎯 CORE PRINCIPLE

**WHEN A TRANSACTION APPEARS IN MARGINALEN (1930), DO NOT REPEAT IT IN OTHER FILES**

The Marginalen bank account is the **PRIMARY SOURCE OF TRUTH** for all money flows through the company.

---

## 📊 SE FILE HIERARCHY

```
MARGINALEN (1930) - MASTER FILE
└── All bank transactions appear here FIRST
    ├── Direct payments from bank
    ├── Shareholder repayments (2893 payments)
    ├── Transfers to Wise (1945/1942/1944)
    ├── Worldline settlements (1947→1930)
    └── Tax payments (1630)

PERSONAL CARD FILES (Secondary)
├── PERSONKONTO (2893) - Detail what was spent
├── KLARNA (2893) - Detail what was spent
├── REMAMBER (2893) - Detail what was spent
├── NORDEA_PREMIUM (2893) - Detail what was spent
├── NORDEA_GOLD (2893) - Detail what was spent
└── NOTE: Only show EXPENSE → 2893 flow
         Do NOT show 2893 → 1930 payment (already in MARGINALEN)

FOREIGN ACCOUNT FILES (Secondary)
├── WISE (1942/1944/1945) - Detail what was SPENT from these accounts
│   └── Include: Supplier payments FROM Wise
│   └── EXCLUDE: Deposits to Wise FROM 1930 (already in MARGINALEN)
│
└── VIVA_WALLET (1941) - Detail what was SPENT from Viva
    └── Include: Supplier payments FROM Viva
    └── EXCLUDE: Deposits to Viva (if applicable)

REVENUE FILES (Secondary)
└── SALES (3051/2611) - Detail sales revenue only
    └── EXCLUDE: Worldline settlements (1947→1930 already in MARGINALEN)
```

---

## ✅ INCLUDE / ❌ EXCLUDE MATRIX

| Transaction Type | MARGINALEN | Card File | WISE File | SALES File |
|------------------|-----------|-----------|-----------|-----------|
| Direct bank payment to supplier | ✅ | ❌ | ❌ | ❌ |
| Personal card purchase (e.g., TikTok ads) | ❌ | ✅ | ❌ | ❌ |
| Card payment settled from bank (2893→1930) | ✅ | ❌ | ❌ | ❌ |
| Wise transfer from bank (1930→1945) | ✅ | ❌ | ❌ | ❌ |
| Supplier payment FROM Wise USD | ❌ | ❌ | ✅ | ❌ |
| Worldline card settlement (1947→1930) | ✅ | ❌ | ❌ | ❌ |
| Worldline sales to 1947 receivable | ❌ | ❌ | ❌ | ✅ |
| Cash sales to 1910 | ❌ | ❌ | ❌ | ✅ |
| VAT payment (1930→1630) | ✅ | ❌ | ❌ | ❌ |
| Government subsidy (1630→1930) | ✅ | ❌ | ❌ | ❌ |

---

## 📝 DETAILED EXAMPLES

### Example 1: Klarna Card Purchase
```
Scenario: TikTok ads purchased 2025-07-19 for 2,000 SEK on Klarna card
Later paid from bank 2025-08-15

KLARNA_Q3_2025.se:
#VER "" "KLARNA-001" 20250719 "TikTok Ads"
{
    #TRANS 5900 {} 1600.00 "TikTok ad ex VAT"
    #TRANS 2641 {} 400.00 "VAT 25%"
    #TRANS 2893 {} -2000.00 "Klarna charge (shareholder debt)"
}
✓ Records: Expense category, VAT, and creates 2893 debt

MARGINALEN_Q3_2025.se (2025-08-15 when paid):
#VER "" "MARG-2893-PAY-001" 20250815 "Klarna debt payment"
{
    #TRANS 2893 {} 2000.00 "Payment reduces shareholder debt"
    #TRANS 1930 {} -2000.00 "Paid from bank"
}
✓ Records: When debt was settled with bank funds

RULE: The 2000 SEK TikTok expense appears ONCE (in KLARNA)
      The payment flow appears ONCE (in MARGINALEN)
      NO DUPLICATION
```

### Example 2: Wise Currency Top-Up
```
Scenario: Transfer 5,000 SEK from bank to Wise USD account
Amount converts to USD 470 at rate 0.094

MARGINALEN_Q3_2025.se (20250815):
#VER "" "MARG-WISE-001" 20250815 "Top-up Wise USD"
{
    #TRANS 1942 {} 5000.00 "Converted to USD 470"
    #TRANS 1930 {} -5000.00 "Paid from bank"
}
✓ Records: Bank to Wise transfer

WISE_Q3_2025.se:
❌ DO NOT repeat the top-up
✅ DO include later when supplier is paid FROM Wise:

#VER "" "WISE-USD-001" 20250822 "Supplier payment from Wise USD"
{
    #TRANS 5800 {} 2000.00 "Supplier cost ex VAT"
    #TRANS 2641 {} 500.00 "VAT 25%"
    #TRANS 1942 {} -2500.00 "Paid from Wise USD (USD 235)"
}
✓ Records: What was spent FROM Wise account
```

### Example 3: Worldline Card Sales
```
Scenario: July card sales total 27,351.76 SEK
Sales record: 25,305 SEK net + 2,046.76 SEK VAT

SALES_Q3_2025.se:
#VER "" "SALES-WL-JULY-001" 20250731 "Worldline card sales July"
{
    #TRANS 1947 {} 25305.00 "Card sales revenue net"
    #TRANS 2611 {} 2046.76 "Output VAT 25%"
    #TRANS 3051 {} -27351.76 "Sales revenue recorded"
}
✓ Records: What was sold

MARGINALEN_Q3_2025.se:
#VER "" "MARG-WL-JULY-001" 20250731 "Worldline settlement July"
{
    #TRANS 1930 {} 27351.76 "Settlement from Worldline to bank"
    #TRANS 1947 {} -27351.76 "Reduces receivable"
}
✓ Records: When cash settled to bank

RULE: Sales revenue appears in SALES file
      Settlement appears in MARGINALEN file
      Amount is the same (27,351.76)
      NO DUPLICATION
```

---

## 🚨 DEDUPLICATION CHECKLIST

Before adding transaction to ANY SE file, verify:

**QUESTION 1:** Does this involve account 1930 (Marginalen bank)?
- ✅ YES → Include in MARGINALEN
- ❌ NO → Do not include in MARGINALEN

**QUESTION 2:** Is this already in MARGINALEN?
- ✅ YES → Do NOT add to other files
- ❌ NO → Proceed to next question

**QUESTION 3:** What is the PRIMARY account?
- 2893 (card) → Include in card's SE file
- 1942/1944/1945 (Wise) → Include in WISE file
- 3051 (sales) → Include in SALES file
- 1930 (bank) → Include in MARGINALEN

**QUESTION 4:** Is this a payment FROM another account?
- ✅ YES → Include in that account's file
- ❌ NO (it's a deposit) → Include in destination account file

---

## 💡 MEMORY RULE

**Think of it as a FLOW:**

```
Expense Happens → Recorded in Payment Source File
                    (KLARNA, WISE, NORDEA, etc.)
                         ↓
Payment Leaves → Recorded in MARGINALEN File
(from 1930)     (when 2893/1942/1945 is paid)
                         ↓
MARGINALEN is the FINAL place money leaves the company
Other files are DETAILS of where it came from before MARGINALEN
```

---

## 📌 FINAL RULE

**ONE TRANSACTION = ONE ENTRY IN ONE FILE**

Do not let the same transaction appear in:
- ❌ MARGINALEN and KLARNA (same payment)
- ❌ MARGINALEN and WISE (same transfer)
- ❌ SALES and MARGINALEN (same settlement)
- ❌ WISE and MARGINALEN (same top-up)

Each transaction has ONE home file where it is recorded ONCE.
Other files show DETAILS or RELATED entries, not duplicates.

---

## 🔄 MULTI-CURRENCY EXAMPLE

**Scenario:** EUR payment from Wise EUR account

```
TRANSACTION SEQUENCE:

1. EUR 300 supplier invoice received
2. Payment made from Wise EUR account (1944)
3. Equivalent to SEK 3,300

WISE_Q3_2025.se:
#VER "" "WISE-EUR-001" 20250815 "Supplier payment from EUR"
{
    #TRANS 5800 {} 2640.00 "Supplier cost ex VAT"
    #TRANS 2641 {} 660.00 "VAT 25%"
    #TRANS 1944 {} -3300.00 "Paid from Wise EUR (EUR 300)"
}
✓ Records spending FROM Wise EUR account

MARGINALEN_Q3_2025.se:
❌ DO NOT include this payment (it's from 1944, not 1930)
✅ DO include if money was transferred TO 1944 FROM 1930:

#VER "" "MARG-WISE-EUR" 20250810 "Top-up Wise EUR account"
{
    #TRANS 1944 {} 5000.00 "Top-up Wise EUR"
    #TRANS 1930 {} -5000.00 "Paid from bank"
}
✓ Only includes the DEPOSIT to Wise, not the payment FROM Wise
```

---

## ✨ SUMMARY

| Concept | Rule |
|---------|------|
| **Master File** | MARGINALEN (all 1930 transactions) |
| **Deduplication** | Same transaction = ONE file only |
| **Cross-File Logic** | Show expense in source file, show payment in MARGINALEN |
| **Multi-Currency** | Each currency account can have separate file |
| **Personal Cards** | Show expense in card file, payment settlement in MARGINALEN |
| **Deposits vs Payments** | Deposits appear in destination file, payments in source file |
| **Verification** | Ask: "Where did the money LEAVE from?" That's the home file |

---

**Last Updated:** October 24, 2025  
**Status:** ACTIVE METHODOLOGY  
**Apply to:** All Q3 2025+ SE files
