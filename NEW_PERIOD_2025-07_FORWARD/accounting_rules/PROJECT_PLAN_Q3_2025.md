# 🎯 Q3 2025 ACCOUNTING PROJECT PLAN
**Period:** July 1 - September 30, 2025  
**Company:** Samis Jackets AB (559489-5301)  
**Date Created:** October 19, 2025  
**Status:** PLANNING PHASE  

---

## 📋 PROJECT OVERVIEW

### **Completed:**
✅ Inventory accounting (COGS + Marketing gifts)

### **Remaining Work:**
1. **Wise Multi-Currency** - Company account (4 currencies: USD, GBP, EUR, SEK)
2. **Nordea Cards** - Personal cards with SOME business transactions
3. **Worldline** - Card payment sales (exclude cash sales)
4. **Viva** - Payment system transactions
5. **Sales Reconciliation** - Match Worldline to Easy Cashier data

---

## 🏦 ACCOUNT STRUCTURE (From Master Branch)

### **Wise Multi-Currency Accounts:**
- **1942** - Wise USD (US Dollar transactions)
- **1943** - Wise GBP (British Pound transactions)
- **1944** - Wise EUR (Euro transactions)
- **1945** - Wise SEK (Swedish Krona transactions)
- **6570** - Bank fees (Wise conversion fees, transfer fees)
- **8330** - Currency exchange differences (if needed)

### **Other Bank Accounts:**
- **1930** - Nordea company account (SEK)
- **1941** - Viva.com payment account
- **1947** - Worldline card payments
- **1948** - Sales account

### **Expense Accounts (Business Only):**
- **5900** - Marketing/PR (TikTok ads, social media)
- **5410** - Tools/software (OpenAI, Anthropic, AI tools)
- **5460** - Office supplies
- **5610** - Vehicle costs
- **6570** - Bank fees

---

## 📊 DATA SOURCES AVAILABLE

### **1. Wise Multi-Currency Statement**
**Location:** `statement Wise Multi curruncey _2025-07-01_2025-09-30/`
**Type:** COMPANY ACCOUNT
**Currencies:** USD, GBP, EUR, SEK
**Complexity:** HIGH - Multi-currency conversions, exchange rates, fees

**Tasks:**
- Extract all transactions per currency
- Identify currency conversions (e.g., GBP→USD, SEK→EUR)
- Record exchange rates used
- Separate conversion fees
- Calculate ending balance per currency
- Convert all to SEK for Visma

---

### **2. Nordea Personal Cards**
**Files:**
- `Nordea Gold - 2025-10-19 12.55.00.csv` (39 transactions)
- `Nordea Premium - 2025-10-19 12.54.04.csv`
- `PERSONKONTO-STUDENT nordea 3086 00 59626 - 2025-10-19 12.52.30.csv`
- `Kontohändelser_2025-07-01_2025-09-30.csv`
- `Kontohändelser Remamber _2025-07-01_2025-09-30.csv`

**Type:** PERSONAL CARDS - Extract BUSINESS ONLY

**Business Indicators (Include):**
- ✅ TikTok (ads/marketing)
- ✅ OpenAI (business AI tools)
- ✅ Anthropic (Claude AI for business)
- ✅ Temu (business supplies)
- ✅ Klarna (business purchases)
- ✅ G&S By Samis jackets (company fees)
- ✅ Any transaction mentioning company account **92356405879**

**Personal (Exclude):**
- ❌ Grocery stores (WILLYS, ARAN FOOD AB, etc.)
- ❌ Phone bills (hallon)
- ❌ Restaurants (Mister York, Almousli)
- ❌ Interest charges (RÖRLIG RÄNTA)
- ❌ Personal shopping
- ❌ IN & FINN AB (personal)

---

### **3. Worldline Card Payment Reports**
**Files:**
- `World line monthly_report_detailed_202507.pdf`
- `World line monthly_report_detailed_202508.pdf`
- `World line monthly_report_detailed_202509.pdf`

**Type:** CARD SALES ONLY (Exclude cash)
**Account:** 1947 (Worldline)

**Purpose:**
- Extract total card payments received
- Compare with Easy Cashier sales data
- Identify CARD vs CASH split
- Ensure no double-counting with cash sales

**Cross-Reference:**
- `sales Försäljningsrapport from 0107 to 30-09.csv` (433 records)

---

### **4. Viva Payment System**
**Location:** `viva/` folder (currently empty - may need statements)
**Account:** 1941
**Status:** TBD - check if statements available

---

## 🔄 MULTI-CURRENCY CONVERSION LOGIC

### **Example from Master Branch:**

```
Transaction: Convert £1,000 GBP to SEK
Exchange Rate: 13.64 SEK/GBP
SEK Amount: 13,639.88 SEK
Conversion Fee: 35.46 SEK

SIE Entry:
#VER "A" 1 20250127 "GBP→SEK Conversion £1,000"
{
    #TRANS 1945 {} 13639.88 "GBP→SEK £1,000 @ 13.64 SEK/GBP"
    #TRANS 1943 {} -13639.88 "Currency conversion"
}

#VER "A" 2 20250127 "Wise Conversion Fee"
{
    #TRANS 6570 {} 35.46 "Wise GBP→SEK conversion fee"
    #TRANS 1943 {} -35.46 "Bank fees"
}
```

### **Currency Conversion Rules:**
1. ✅ Always show original currency amount in description
2. ✅ Always include exchange rate in description
3. ✅ Convert to SEK for accounting
4. ✅ Record fees separately in account 6570
5. ✅ DEBIT destination currency account
6. ✅ CREDIT source currency account
7. ✅ All amounts in SEK equivalent

---

## 📝 WORKFLOW - STEP BY STEP

### **Phase 1: Analysis (Current)**
1. ✅ Read all accounting methodology files
2. ⏳ Analyze Wise multi-currency statement
3. ⏳ Analyze Nordea personal cards for business transactions
4. ⏳ Analyze Worldline card payment reports
5. ⏳ Check Viva folder for statements

### **Phase 2: Documentation**
6. ⏳ Create `WISE_Q3_2025_ANALYSIS.md`
   - All transactions per currency
   - Conversions with exchange rates
   - Fees summary
   - Ending balances (1942/1943/1944/1945)
   - Business expenses paid via Wise

7. ⏳ Create `NORDEA_BUSINESS_Q3_2025.md`
   - ONLY verified business transactions
   - Suggested BAS account numbers
   - Descriptions and amounts
   - Total business expenses from personal cards

8. ⏳ Create `WORLDLINE_SALES_Q3_2025.md`
   - Card payment totals per month
   - Compare with Easy Cashier sales
   - Identify card vs cash split
   - Prepare sales accounting entries

9. ⏳ Create `VIVA_Q3_2025.md` (if applicable)

### **Phase 3: User Review** ⚠️ CRITICAL
10. ⏳ Present ALL MD files to user
11. ⏳ User reviews and confirms:
    - Which Nordea transactions are business
    - Correct account assignments
    - Worldline sales split logic
12. ⏳ User approval before ANY SIE files created

### **Phase 4: SIE File Creation** (ONLY AFTER APPROVAL)
13. ⏳ Create `wise/WISE_Q3_2025.se`
    - Multi-currency transactions
    - Conversions with rates
    - Fees to 6570
    - Follow master-branch logic exactly

14. ⏳ Create `nordea/NORDEA_BUSINESS_Q3_2025.se`
    - Approved business transactions only
    - From personal cards
    - Proper expense categorization

15. ⏳ Create `sales_data/WORLDLINE_SALES_Q3_2025.se`
    - Card payment sales
    - Coordinate with inventory COGS
    - Avoid double-counting

16. ⏳ Create `viva/VIVA_Q3_2025.se` (if applicable)

### **Phase 5: Final Verification**
17. ⏳ Create `00_IMPORT_SEQUENCE.md`
    - Order for importing SIE files
    - What each file contains
    - Verification checklist

18. ⏳ User final review
19. ⏳ Import to Visma in correct sequence

---

## 🚨 CRITICAL RULES

### **NEVER Guess or Assume:**
- ❌ Do NOT include personal expenses as business
- ❌ Do NOT assume a transaction is business without clear indicators
- ❌ Do NOT create SIE files before user approval
- ❌ Do NOT duplicate transactions across multiple files

### **ALWAYS Verify:**
- ✅ User confirms business vs personal
- ✅ User confirms correct BAS accounts
- ✅ Cross-check balances
- ✅ Follow multi-currency logic from master branch
- ✅ Include exchange rates in descriptions
- ✅ Separate fees to 6570

---

## 📁 FOLDER STRUCTURE

```
NEW_PERIOD_2025-07_FORWARD/
├── final_se_files/
│   ├── INVENTORY_Q3_2025_FINAL_CORRECTED.se ✅ DONE
│   └── (Other SIE files will be reviewed first)
├── wise/
│   ├── WISE_Q3_2025_ANALYSIS.md (to create)
│   └── WISE_Q3_2025.se (after approval)
├── nordea/
│   ├── NORDEA_BUSINESS_Q3_2025.md (to create)
│   └── NORDEA_BUSINESS_Q3_2025.se (after approval)
├── sales_data/
│   ├── WORLDLINE_SALES_Q3_2025.md (to create)
│   └── WORLDLINE_SALES_Q3_2025.se (after approval)
├── viva/
│   ├── VIVA_Q3_2025.md (to create if applicable)
│   └── VIVA_Q3_2025.se (after approval)
└── 00_IMPORT_SEQUENCE.md (final documentation)
```

---

## 🎯 SUCCESS CRITERIA

1. ✅ All multi-currency conversions properly recorded
2. ✅ ONLY verified business transactions from personal cards
3. ✅ Card sales properly separated from cash sales
4. ✅ No duplicate transactions
5. ✅ All amounts balance
6. ✅ User approval before SIE creation
7. ✅ Clear documentation for audit trail
8. ✅ Ready for sequential Visma import

---

## ⏭️ NEXT STEP

**Start with TODO #1:** Read all methodology files to understand:
- Multi-currency accounting rules
- Wise account structure (1942/1943/1944/1945)
- Business expense categories
- Failed transaction handling
- Exchange rate recording

**Then proceed to Wise analysis (TODO #2)**

---

*Samis Jackets AB - Q3 2025 Accounting Project*  
*Organization Number: 559489-5301*  
*Project Manager: AI Accounting Assistant*  
*Start Date: October 19, 2025*
