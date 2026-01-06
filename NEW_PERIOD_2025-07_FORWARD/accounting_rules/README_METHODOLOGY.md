# 🆕 NEW ACCOUNTING PERIOD - JULY 2025 FORWARD
## Samis Jackets AB - Continuation Methodology

**PERIOD:** 01-07-2025 to 30-06-2026  
**PURPOSE:** Prepare for Swedish VAT (moms) declaration  
**METHODOLOGY:** Apply proven corrected accounting principles from previous period

---

## 📁 FOLDER STRUCTURE

### `/nordea/` - Nordea Bank Data
- Raw bank statements from 01-07-2025 forward
- Will create filtered BUSINESS_ONLY_xx files (same as current system)
- Separate private vs company transactions using proven methodology

### `/wise/` - Wise Multi-Currency
- All currencies: USD (1942), EUR (1944), GBP (1943), SEK (1945)
- Apply COST VALUATION method (no artificial FX gains/losses)
- Categorize using established BAS 2024 accounts

### `/viva/` - Viva Wallet
- Apply same audit methodology as previous period
- Balance verification, sales extraction, failed transfer cleanup

### `/sales_data/` - POS & E-commerce
- EasyCashier continuation from 30-06-2025
- Shopify data for new period
- Any new POS systems

### `/inventory/` - Stock Management
- Opening inventory values as of 01-07-2025
- Continue weighted average cost method
- Import/purchase documentation

### `/final_se_files/` - SIE4 Output
- Clean files ready for Visma import
- Swedish BAS 2024 compliant
- VAT declaration ready

### `/receipts_documentation/` - Audit Trail
- All supporting documents
- Business justification for expenses
- Travel and business purpose documentation

### `/accounting_rules/` - Period-Specific Rules
- Copy proven methodology from current period
- Document any adaptations for new period

---

## 🎯 PROVEN METHODOLOGY TO APPLY

### ✅ CORRECTED PRINCIPLES (Established)
1. **Currency Cost Valuation:** Foreign currency at actual SEK cost paid
2. **Failed Transfer Deletion:** Remove failed transfer pairs completely  
3. **Payment System Audits:** Systematic balance verification methodology
4. **Business Filtering:** Proven private vs company separation for Nordea

### 🏦 ACCOUNT STRUCTURE (BAS 2024)
- **1930:** Main company account (SEK)
- **1942-1945:** Multi-currency accounts (cost valuation method)
- **2611/2641/2615:** VAT accounts (25% Swedish rate)
- **2893/2895:** Related party and foreign investor loans
- **3051:** Sales revenue (net, excluding VAT)
- **4010/4016:** Cost of goods (Turkey/China imports)

### 📋 FILTERING METHODOLOGY
Apply same business categorization as current period:
- `BUSINESS_ONLY_00_oversikt_kategorier.csv`
- `BUSINESS_ONLY_01_programvaror_prenumerationer.csv`
- `BUSINESS_ONLY_02_marknadsforing_reklam.csv`
- `BUSINESS_ONLY_03_resekostnader.csv`
- `BUSINESS_ONLY_04_foretag_kontorsmaterial.csv`
- `BUSINESS_ONLY_05_bil_fordon.csv`
- `BUSINESS_ONLY_06_myndigheter_avgifter.csv`

---

## 📊 NEXT STEPS

1. **USER:** Place all raw data files in appropriate folders
2. **AI:** Apply filtering and categorization using proven methodology
3. **AI:** Generate clean SIE4 files for Visma import
4. **RESULT:** Ready for Swedish VAT declaration filing

---

*Created: 2025-09-29*  
*Purpose: Systematic continuation of proven Swedish accounting methodology*


