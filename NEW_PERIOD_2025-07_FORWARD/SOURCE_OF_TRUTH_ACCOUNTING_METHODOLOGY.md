# 📋 SOURCE OF TRUTH - SAMIS JACKETS AB ACCOUNTING METHODOLOGY
**Company:** Samis Jackets AB  
**Organization Number:** 559489-5301  
**Accounting Standard:** EUBAS97 (Swedish Accounting Standards)  
**Software:** Visma eEkonomi  
**Period:** Q3 2025 (July 1 - September 30, 2025)  
**Last Updated:** October 23, 2025  

---

## 🎯 EXECUTIVE SUMMARY

This document serves as the comprehensive source of truth for all accounting procedures, rules, and methodologies used for Samis Jackets AB. It contains all prompts, rules, and procedures discussed and established during the Q3 2025 accounting period setup.

### Key Principles:
- **100% Accuracy:** No invented or estimated transactions
- **Source Verification:** All transactions must be traceable to original CSV/bank statements
- **VAT Compliance:** 25% deductible VAT on all eligible business expenses
- **EUBAS97 Compliance:** Swedish accounting standards for small businesses
- **Audit Trail:** Complete traceability from source documents to SE file entries

---

## 📊 ACCOUNT CHART - EUBAS97 MAPPINGS

### Revenue Accounts (3XXX)
- **3051** - Försäljning varor 25% sv (Sales of goods 25% VAT Sweden) - Primary sales revenue
- **3051** - Försäljning tjänster (Sales of services) - Service revenue if applicable

### Expense Accounts (4XXX-8XXX)
- **1220** - Maskiner och inventarier (Machinery and equipment)
- **1460** - Varor under tillverkning och handel (Goods in trade)
- **2441** - Leverantörsskulder (Supplier liabilities)
- **5010** - Lokalhyra (Rent) - Office/store rent (25% VAT deductible)
- **5410** - Programvaror/verktyg (Software/tools) - Business software subscriptions
- **5420** - Programvaror/verktyg (Software purchases) - One-time software purchases
- **5460** - Förbrukningsmaterial (Office supplies) - Business supplies/materials
- **5610** - Resekostnader (Travel expenses) - Business travel (25% VAT deductible)
- **5700** - Frakt- och transportkostnader (Freight and transport costs)
- **5800** - Resekostnader (Travel expenses) - Additional travel expenses
- **5900** - Annonsering (Advertising) - Marketing and advertising expenses
- **5910** - Annonsering (Advertising) - General advertising expenses
- **5911** - AI-marknadsföringsverktyg (AI marketing tools) - AI-specific marketing tools
- **6570** - Bankkostnader (Bank fees) - Bank charges, card processing fees
- **6991** - Övriga externa kostnader (Other external costs) - Administrative fees with VAT
- **6992** - Övriga externa kostnader (Other external costs) - Administrative fees without VAT
- **7010** - Löner (Salaries) - Employee salaries

### Balance Sheet Accounts (1XXX-2XXX)
- **1220** - Maskiner och inventarier (Machinery and equipment)
- **1460** - Varor under tillverkning och handel (Goods in trade)
- **1630** - Skatteskonto (Tax account) - Government subsidies/tax receivables
- **1910** - Kassa (Cash) - Cash sales revenue
- **1930** - Bank (Bank account) - Marginalen bank account 92356405879
- **1940** - Utland konto (Foreign account) - Viva Wallet main account
- **1941** - Utland konto (Foreign account) - Viva Wallet card account
- **1942** - Utland USD (Foreign currency USD) - Wise USD account
- **1944** - Utland EUR (Foreign currency EUR) - Wise EUR account
- **1945** - Utland SEK (Foreign currency SEK) - Wise SEK account
- **1947** - Kundfordringar (Accounts receivable) - Worldline card settlement receivable
- **1948** - Övriga fordringar (Other receivables) - Shopify/Stripe receivables
- **2091** - Balanserat resultat (Retained earnings)
- **2093** - Överkursfond (Share premium)

### Equity & Liabilities (28XX-29XX)
- **2448** - Övriga skulder (Other liabilities)
- **2893** - Skulder till närstående (Liabilities to related parties) - Shareholder loans/advances

### VAT Accounts (26XX)
- **2611** - Moms utgående (Output VAT) - 25% VAT on sales
- **2641** - Moms ingående (Input VAT) - 25% VAT on purchases (deductible)
- **2645** - Moms ingående (Input VAT) - Import VAT
- **2650** - Moms betalning (VAT payment) - VAT payments to Skatteverket

### Interest & Financial Accounts (83XX)
- **8311** - Ränteintäkter (Interest income) - Interest earned on accounts

---

## 💳 PAYMENT METHOD ACCOUNTING RULES

### 1. Personal Card Payments (2893 Shareholder Loan)
**When:** Business expenses paid with personal cards (Nordea, Remamber, Klarna)  
**Accounting:**
```
DEBIT: Expense account (5900, 5410, etc.)
CREDIT: 2893 (Skulder till närstående)
```
**Rationale:** Creates shareholder loan that can be repaid later or treated as equity contribution.

### 1.5 Viva Wallet Card (1941)
**When:** Business expenses paid with Viva Wallet card
**Accounting:**
```
DEBIT: Expense account (5910, 6991, etc.)
CREDIT: 1941 (Utland konto - Viva card)
```
**Rationale:** Viva card is treated as a separate foreign currency account.

### 2. Wise Multi-Currency Payments
**SEK Account (1945):**
```
DEBIT: Expense account
CREDIT: 1945 (Utland SEK)
```

**USD Account (1942):**
```
DEBIT: Expense account
CREDIT: 1942 (Utland USD)
```

**EUR Account (1944):**
```
DEBIT: Expense account
CREDIT: 1944 (Utland EUR)
```

### 3. Bank Account Direct Payments (1930)
**Accounting:**
```
DEBIT: Expense account (+ VAT account if applicable)
CREDIT: 1930 (Bank)
```

### 4. Worldline Card Settlements (1947 → 1930)
**Monthly settlements:**
```
DEBIT: 1930 (Bank)
CREDIT: 1947 (Kundfordringar)
```

### 5. Sales Revenue (3051)

**Card sales through Worldline:**

```text
DEBIT: 1947 (Worldline receivable)
CREDIT: 3051 (Sales revenue)
CREDIT: 2611 (Output VAT 25%)
```

**Cash sales:**

```text
DEBIT: 1910 (Cash)
CREDIT: 3051 (Sales revenue)
CREDIT: 2611 (Output VAT 25%)
```

---

## 🏦 BANK ACCOUNT SPECIFICATIONS

### Marginalen Bank Account (1930)

- **Account Number:** 92356405879
- **Purpose:** Primary business bank account
- **Transactions:** All direct bank payments, settlements, shareholder repayments

### Wise Multi-Currency Accounts

- **SEK (1945):** Swedish Krona transactions
- **USD (1942):** US Dollar transactions
- **EUR (1944):** Euro transactions
- **GBP (1947):** British Pound (if used)
- **CNY (19XX):** Chinese Yuan (if used)
- **TRY (19XX):** Turkish Lira (if used)

### Worldline Card Processing (1947)

- **Purpose:** Card sales settlement receivable
- **Settlement:** Monthly transfers to bank account 1930

---

## 🛒 EXPENSE CATEGORIZATION RULES

### Marketing & Advertising (5900)

- TikTok Ads campaigns
- Facebook Ads campaigns
- Google Ads
- Other social media advertising
- Marketing materials and promotional items

### Software & Tools (5410)

- Shopify e-commerce platform
- Google Workspace/GSuite
- Accounting software (Fortnox, Visma)
- POS systems (Easy Cashier)
- Other business software subscriptions

### Office Supplies (5460)

- Business supplies from TEMU, HEMKOP, etc.
- Office materials
- Small equipment purchases

### Travel Expenses (5610)

- Business flights (BUDGETAIR)
- Train tickets (RESECENTRUM)
- UK travel (National Express)
- Parking fees for business vehicles

### Vehicle Costs (5610-5620)

- Fuel for company vehicles (St1, etc.)
- Car insurance (FORA)
- Vehicle maintenance

### Rent (5010 + 2640)

- Store/office rent (25% VAT deductible)
- **Formula:** Rent amount ÷ 1.25 = Net rent (5010), 25% = VAT (2640)

### Bank & Administrative Fees (6570, 6250)

- Monthly bank fees
- Card processing fees (G&S, Worldline)
- Bolagsverket registration fees
- Insurance premiums

---

## 🇪🇺 VAT RULES (25% Standard Rate)

### Deductible VAT (Ingående Moms - 2640)

**Eligible Expenses:**
- Rent (5010)
- Software subscriptions (5410)
- Office supplies (5460)
- Travel expenses (5610)
- Insurance (5920)

**VAT Calculation:**

```text
Gross Amount = Net Amount + VAT
VAT = Net Amount × 0.25
Net Amount = Gross Amount ÷ 1.25
```

### Output VAT (Utgående Moms - 2610)

**On Sales Revenue:**
- Card sales: 25% of net sales amount
- Cash sales: 25% of net sales amount

**Sales VAT Split:**

```text
Total Sales Amount = Net Sales + VAT
Net Sales (3000/1910) = Total Sales ÷ 1.25
VAT (2610) = Total Sales × 0.20 (or Net Sales × 0.25)
```

---

## 💰 SALES REVENUE ACCOUNTING

### Card Sales via Worldline

1. **Daily Sales:** Recorded as receivable in 1947
2. **Monthly Settlement:** Transfer from 1947 to 1930
3. **VAT Split:** 80% net sales (3051) + 20% VAT (2611)

### Cash Sales

1. **Direct to Cash Account:** 1910
2. **VAT Split:** Same as card sales

### Foreign Currency Sales (Wise)

1. **Shopify/Stripe Deposits:** EUR to 1944 account
2. **Conversion:** If needed, convert between Wise currency accounts
3. **VAT:** Apply 25% output VAT on sales value

---

## 🔄 MULTI-ACCOUNT TRANSACTION DEDUPLICATION LOGIC

### ⚠️ CRITICAL PRINCIPLE: NO DOUBLE-ENTRY OF SAME TRANSACTION

**Rule:** When a transaction appears in MARGINALEN (main bank account 1930), DO NOT repeat it in other SE files.

### Example 1: Shareholder Loan Repayment
```
MARGINALEN_Q3_2025.se (Contains the ONLY entry):
#VER "" "MARG-LOAN-001" 20250724 "Shareholder loan repayment"
{
    #TRANS 2893 {} 15274.28 "Loan repayment"
    #TRANS 1930 {} -15274.28 "Paid from bank"
}

PERSONKONTO_Q3_2025.se:
✓ DO NOT repeat this transaction
✗ It already happened in MARGINALEN (main source)
```

### Example 2: Bank Transfer to Wise (1930 → 1945)
```
MARGINALEN_Q3_2025.se (Contains the ONLY entry):
#VER "" "MARG-WISE-001" 20250827 "Top-up Wise SEK account"
{
    #TRANS 1945 {} 2500.00 "Transfer to Wise SEK"
    #TRANS 1930 {} -2500.00 "Payment from bank"
}

WISE_Q3_2025.se:
✓ DO NOT repeat this top-up transaction
✗ The flow is already in MARGINALEN
✓ DO list what was SPENT from 1945 (e.g., supplier payments)
```

### How Multi-Account System Works

**PRINCIPLE:** Each SE file represents a specific "perspective" on accounts:

| SE File | Primary Account | What to Include | What to EXCLUDE |
|---------|-----------------|-----------------|-----------------|
| **MARGINALEN** | 1930 (bank) | ALL transactions from 1930 | None - this is main source |
| **PERSONKONTO** | 2893 (shareholder) | Only personal card expenses → 2893 | Payments already in MARGINALEN |
| **KLARNA** | 2893 (Klarna card) | Only Klarna card expenses → 2893 | Payments already in MARGINALEN |
| **REMAMBER** | 2893 (Remamber card) | Only Remamber expenses → 2893 | Payments already in MARGINALEN |
| **NORDEA_PREMIUM** | 2893 (Nordea) | Only Nordea Premium expenses → 2893 | Payments already in MARGINALEN |
| **WISE** | 1945/1942/1944 (currencies) | Only SPENDING from Wise accounts | Deposits from 1930 (already in MARGINALEN) |
| **SALES** | 3051/2611 (revenue) | Only sales revenue entries | NOT card settlements (already 1947→1930) |

### Multi-Currency Example: When to Include/Exclude

```
TRANSACTION: "2025-08-15 Supplier payment from Wise USD account"
Amount: USD 500 = SEK 5,330

WISE_Q3_2025.se INCLUDES:
#VER "" "WISE-USD-001" 20250815 "Supplier payment via Wise USD"
{
    #TRANS 6250 {} 4264.00 "Supplier cost (ex VAT)"
    #TRANS 2641 {} 1066.00 "VAT 25%"
    #TRANS 1942 {} -5330.00 "Paid from Wise USD account"
}
✓ Correctly records spending FROM Wise account

MARGINALEN_Q3_2025.se EXCLUDES:
✗ DOES NOT include this transaction
✗ It comes from Wise (1942), not from Marginalen bank (1930)
✗ Marginalen only shows: transfer FROM 1930 TO 1942 (the deposit)
```

### Deduplication Checklist

**For each transaction, ask:**

1. **Where is the PRIMARY source of money?**
   - If 1930 (bank) → Include in MARGINALEN ✓
   - If 2893 (card) → Include in that card's SE file ✓
   - If 1945/1942/1944 (Wise) → Include in WISE SE file ✓

2. **Is this already captured in MARGINALEN?**
   - If YES → Do NOT repeat ✗
   - If NO → Include in appropriate file ✓

3. **Is this a flow between accounts (1930 → 1945)?**
   - If YES → Include in MARGINALEN ONLY ✓
   - Wise file shows spending FROM 1945, not the deposit TO 1945 ✓

4. **Is this personal card expense?**
   - If YES → Appears in both card file AND creates 2893 balance ✓
   - Card file documents the expense category
   - Shareholder loan (2893) tracks the total debt

### Real-World Example: Complete Flow

**Scenario:** Purchase TikTok ads with Klarna card

```
KLARNA_Q3_2025.se:
#VER "" "KLARNA-001" 20250710 "TikTok Ads via Klarna"
{
    #TRANS 5900 {} 1600.00 "TikTok advertising (ex VAT)"
    #TRANS 2641 {} 400.00 "VAT 25%"
    #TRANS 2893 {} -2000.00 "Klarna payment (to shareholder debt)"
}
✓ Shows what was spent on ads
✓ Shows VAT treatment
✓ Creates 2000 SEK entry in shareholder debt

MARGINALEN_Q3_2025.se:
[Later, when Klarna bill is paid from bank]:
#VER "" "MARG-KLARNA-001" 20250815 "Klarna payment settlement"
{
    #TRANS 2893 {} 2000.00 "Klarna debt payment"
    #TRANS 1930 {} -2000.00 "Paid from bank"
}
✓ Shows when 2893 debt was paid with bank funds
✓ Reduces shareholder loan balance

KEY: The TikTok ad expense (5900) only appears ONCE in KLARNA file
The payment flow (2893 → 1930) only appears ONCE in MARGINALEN
NO DUPLICATION
```

### Summary
- **MARGINALEN = Master record for all 1930 bank flows**
- **Other files = Detailed breakdown of where funds came from BEFORE hitting bank**
- **No transaction appears twice**
- **System records complete flow: Expense Category → Payment Method → Bank Settlement**

---

## 🔄 CURRENCY CONVERSION RULES

### Wise Internal Conversions

#### Example: SEK to USD

```text
DEBIT: 1942 (USD account) + converted amount
CREDIT: 1945 (SEK account) - original SEK amount
CREDIT: 6570 (Bank fees) - conversion fee
```

### Exchange Rate Documentation

- Always document the exchange rate used
- Use Wise's actual conversion rates
- Format: "SEK to USD @ 0.10658 SEK/USD"

---

## 📋 TRANSACTION VERIFICATION PROTOCOL

### 1. Source Document Verification
- [ ] CSV file exists and is from correct period
- [ ] Transaction dates within Q3 2025 (2025-07-01 to 2025-09-30)
- [ ] Amounts match between source and SE file
- [ ] No duplicate transactions

### 2. Business Purpose Verification
- [ ] Transaction serves legitimate business purpose
- [ ] Expense category appropriate
- [ ] VAT treatment correct (if applicable)

### 3. Accounting Rule Application
- [ ] Correct EUBAS97 account codes used
- [ ] Debit/credit rules followed
- [ ] Shareholder loan accounting (2893) applied correctly

### 4. SE File Format Compliance
- [ ] Proper SIE4 format
- [ ] Correct VER structure
- [ ] TRANS entries balanced (debits = credits)
- [ ] Descriptive references included

---

## 🛠️ SIE FILE GENERATION RULES

### Header Structure (Required)
```
#FLAGGA 0
#PROGRAM "GitHub Copilot" "1.0"
#FORMAT PC8
#GEN YYYYMMDD
#SIETYP 4
#FNAMN "Samis Jackets AB"
#ORGNR 559489-5301
#RAR 0 20240701 20251231
#KPTYP EUBAS97
```

### VER Entry Format
```
#VER "" "UNIQUE-ID" YYYYMMDD "Description"
{
    #TRANS ACCOUNT {} AMOUNT "Description"
    #TRANS ACCOUNT {} AMOUNT "Description"
}
```

### Unique ID Format
- **Klarna:** KLARNA-001, KLARNA-002, etc.
- **Remamber:** REMAMBER-001, REMAMBER-002, etc.
- **Nordea Premium:** NORDEA-PREMIUM-001, etc.
- **Wise:** WISE-SEK-001, WISE-USD-001, etc.
- **Marginalen:** MARG-001, MARG-002, etc.
- **Sales:** SALES-Q3-001, SALES-Q3-002, etc.

---

## 🔍 AUDIT CHECKLIST

### Pre-Import Verification
- [ ] All transactions have valid dates (Q3 2025)
- [ ] No duplicate VER IDs
- [ ] All TRANS entries balance (debits = credits)
- [ ] Account codes exist in EUBAS97 chart
- [ ] VAT calculations are correct
- [ ] Currency conversions documented
- [ ] Exchange rates reasonable

### Post-Import Verification
- [ ] Visma accepts SE file without errors
- [ ] Account balances reconcile with bank statements
- [ ] VAT return calculations match
- [ ] Shareholder loan balance correct
- [ ] Multi-currency accounts balance

---

## 🚨 COMMON ERRORS & CORRECTIONS

### 1. Date Format Issues
**Error:** Using YYYY-MM-DD instead of YYYYMMDD in VER entries
**Correction:** Convert 2025-07-19 to 20250719

### 2. Duplicate Transactions
**Error:** Same transaction appears multiple times
**Correction:** Cross-reference with source CSV, remove duplicates

### 3. Wrong Account Codes
**Error:** Using incorrect EUBAS97 account numbers
**Correction:** Verify against official account chart

### 4. VAT Miscalculation
**Error:** Incorrect VAT split or deduction
**Correction:** Use formulas: Net = Gross ÷ 1.25, VAT = Gross × 0.20

### 5. Currency Conversion Errors
**Error:** Wrong exchange rates or missing fee accounting
**Correction:** Use actual Wise rates, account for fees in 6570

### 6. Shareholder Loan Misapplication
**Error:** Not using 2893 for personal card payments
**Correction:** All personal payments → 2893 (creates loan to owner)

---

## 📁 FILE ORGANIZATION STRUCTURE

```
NEW_PERIOD_2025-07_FORWARD/
├── 00_IMPORT_SEQUENCE.md
├── accounting_rules/
│   ├── ACCOUNT_2893_EXPLANATION_Q3_2025.md
│   └── [other rule files]
├── final_se_files/
│   ├── KLARNA_Q3_2025.se
│   ├── REMAMBER_Q3_2025.se
│   ├── NORDEA_PREMIUM_Q3_2025.se
│   ├── NORDEA_GOLD_Q3_2025.se
│   ├── NORDEA_PERSONKONTO_Q3_2025.se
│   ├── WISE_Q3_2025.se
│   ├── MARGINALEN_Q3_2025.se
│   ├── SALES_Q3_2025.se
│   └── Q3_2025_COMPLETE_UNIFIED.se
├── [source CSV files]
└── [analysis files]
```

---

## 🔄 WORKFLOW FOR FUTURE PERIODS

### 1. Data Collection
- Export all bank/card statements as CSV
- Ensure Q3 date range (July 1 - Sept 30)
- Backup original files

### 2. Transaction Analysis
- Categorize each transaction by business purpose
- Apply VAT rules where applicable
- Identify personal vs business expenses

### 3. SE File Generation
- Use correct EUBAS97 account codes
- Follow debit/credit rules
- Include descriptive references

### 4. Quality Assurance
- Run audit checklist
- Verify against source documents
- Test import in Visma

### 5. Documentation
- Update this source of truth document
- Record any new accounting rules
- Document exceptions or special cases

---

## 📞 SUPPORT & ESCALATION

### For Accounting Questions:
1. Check this document first
2. Review EUBAS97 official documentation
3. Consult with certified accountant if needed

### For Technical Issues:
1. Verify CSV format and encoding
2. Check SIE file syntax
3. Test with small transaction set first

### For VAT Compliance:
1. Always apply 25% rate for eligible expenses
2. Document VAT calculations clearly
3. Retain all source documents for 7 years

---

## 📝 CHANGE LOG

| Date | Change | Author |
|------|--------|--------|
| 2025-10-23 | Initial comprehensive source of truth document | GitHub Copilot |
| 2025-10-19 | Q3 2025 accounting setup established | Accounting Team |
| 2025-07-01 | Q3 2025 period begins | System |

---

*This document represents the complete accounting methodology for Samis Jackets AB. All future accounting work must comply with these rules and procedures. For any deviations, document the exception and reasoning clearly.*</content>
<parameter name="filePath">c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\NEW_PERIOD_2025-07_FORWARD\SOURCE_OF_TRUTH_ACCOUNTING_METHODOLOGY.md
