# Voucher Series Documentation for Samis Jackets AB
## SIE File Reorganization - Version 1.0

**Document Created:** 2026-01-07  
**Created By:** AI CTO Agent  
**Company:** Samis Jackets AB (559489-5301)  
**Fiscal Year:** 2024-07-01 to 2025-12-31  
**Original File:** 1000_CORRECT_UP_TO_Q3_2025.se  
**Backup File:** 1000_CORRECT_UP_TO_Q3_2025_BACKUP_ORIGINAL.se

---

## 1. Executive Summary

This document describes the voucher series categorization system implemented for the SIE accounting file. The original file had all vouchers under series "A". We have reorganized them into logical categories to improve:

- **Audit readability** - Easier to find specific transaction types
- **Financial analysis** - Quick filtering by expense/income category
- **Error detection** - Misclassified transactions become obvious
- **Future AI processing** - Clear categorization for automated systems

---

## 2. Voucher Series Definitions

### Primary Expense Categories

| Series | Swedish Name | English Name | Account Range | Description |
|--------|-------------|--------------|---------------|-------------|
| **B** | Bankavgifter | Bank Fees | 6570, 8311 (bank costs/interest) | All bank charges, fees, and interest |
| **C** | Kommunikation | Communications | 6212, 6540 | Telecom, mobile, SIM cards, IT services |
| **E** | Externa övriga | Other External | 6991, 6992 | Non-deductible expenses, meals, misc |
| **F** | Frakt/Terminal | Freight/Terminal | Cargo fees | Shipping terminal and cargo fees |
| **G** | Försäkring | Insurance | 6310 | Business insurance premiums |
| **H** | Hyra/Lokal | Rent/Premises | 5010, 5070, 1383 | Rent, repairs, deposits for premises |
| **I** | Import/Lager | Import/Inventory | 4545, 1460 | Import purchases and inventory |
| **K** | Skattekonto | Tax Account | 1630, 2510 | Tax account transactions (existing) |
| **L** | Lån | Loans | 2893↔1930 (director loans) | Loans from/to director/related parties |
| **M** | Moms | VAT | 2611, 2641, 2645, 2650 | VAT declarations and payments |
| **N** | Annonsering | Advertising | 5910, 5911 | All advertising/marketing spend |
| **O** | Material/Inventarier | Office/Materials | 5410, 5460, 6110 | Supplies, consumables, office items |
| **P** | Professionella tjänster | Professional Services | 6590 | Shopify fees, external services |
| **R** | Resa | Travel | 5800, 5810, 5830, 5890 | All travel expenses |
| **S** | Försäljning | Sales | 3051, 2611 | Sales revenue and VAT |
| **T** | Transaktioner kort | Card Transactions | 1941, 1947 | Viva/Worldline card settlements |
| **V** | Fordon | Vehicle | 5610, 5611, 5619, 5620 | Fuel, parking, car costs |
| **W** | Inköp tjänster | Work Services | 4001 | Purchased services for business |
| **X** | Valuta | Currency Exchange | 194x accounts | Currency conversions and transfers |
| **Y** | Betalningar leverantör | Supplier Payments | 2441 | Payments to major suppliers |
| **Z** | Korrigeringar | Corrections | Adjustments | Period-end adjustments, corrections |

---

## 3. Detailed Category Rules

### Series B - Bank Fees (Bankavgifter)
**Accounts:** 6570 (Bank costs), 8311 (Bank interest income)
**Identifying Keywords:** 
- "BANKKOSTNADER", "bankavgift", "banktjänster"
- "Sales Clearance Commission Cards" 
- "Billing Fee"
- "Månadsavgift Företagskonto"
- "Kapitaliserad ränta"

**Example Transactions:**
- Monthly account fees
- Card processing commissions
- Foreign currency fees
- Bank interest (credit/debit)

---

### Series C - Communications (Kommunikation)
**Accounts:** 6212 (Mobile phone), 6540 (IT services)
**Identifying Keywords:**
- "simkort", "yesim", "hallon tele"
- "apple.com bill" (for phone services)
- "CHILIMOBIL", "Hi3G", "Tele2"
- "google GSUITE" (IT service)

**Example Transactions:**
- SIM card purchases
- Mobile subscriptions
- IT service subscriptions

---

### Series E - Other External Expenses (Externa övriga)
**Accounts:** 6991, 6992 (Non-deductible external costs)
**Identifying Keywords:**
- WILLYS, LIDL, "max burgers" (food)
- Foreign ATM/bank transactions
- Miscellaneous purchases abroad
- "Fora" (pension fees)

**Example Transactions:**
- Non-business meals
- Non-deductible entertainment
- Miscellaneous external costs

---

### Series F - Freight/Terminal (Frakt/Terminal)
**Accounts:** 6991 (when related to cargo)
**Identifying Keywords:**
- "CARGO CENTER"
- "FLYterminalavgift"
- "Freightseeker"

**Example Transactions:**
- Airport cargo fees
- Freight service fees

---

### Series G - Insurance (Försäkring)
**Accounts:** 6310 (Business insurance), 5620 (Vehicle insurance)
**Identifying Keywords:**
- "FÖRSÄKRINGSPREMIE", "försäkring"
- "LF SÖRMLAND"
- "Bilförsäkring"

---

### Series H - Rent/Premises (Hyra/Lokal)
**Accounts:** 5010 (Rent), 5070 (Repairs), 1383 (Deposits)
**Identifying Keywords:**
- "Lokalhyra", "Hyra"
- "FASTIGHETS AB AKVARIUM"
- "Lokaldeposition"
- Repair items for premises

---

### Series I - Import/Inventory (Import/Lager)
**Accounts:** 4545 (Import goods), 1460 (Inventory), 2615/2645 (Import VAT)
**Identifying Keywords:**
- "Invoice" with USD amounts
- "FIK" reference numbers
- "First China container"
- "Tullavgifter"

---

### Series K - Tax Account (Skattekonto)
**Accounts:** 1630 (Tax account), 2510 (Tax liabilities), 8423 (Tax interest)
**Note:** This series already exists in the file.
**Content:** All Skatteverket transactions.

---

### Series L - Loans (Lån)
**Accounts:** 2893 ↔ 1930 (Director loan transactions)
**Identifying Keywords:**
- "Loan from Director"
- "Repayment of Director's Loan"
- "Cash Flow Support"
- Personal transfers to/from related parties

---

### Series M - VAT/Moms (Moms)
**Accounts:** 2611 (Output VAT), 2641 (Input VAT), 2645 (Import VAT), 2650 (VAT settlement)
**Identifying Keywords:**
- "Momsredovisning"
- "Betalning moms"
- VAT period declarations
- "moms för period"

**Example Transactions:**
- Quarterly VAT declarations
- VAT payments to Skatteverket
- VAT rounding adjustments (3740)

---

### Series N - Advertising (Annonsering)
**Accounts:** 5910 (Advertising), 5911 (AI marketing tools), 5900 (Marketing general)
**Identifying Keywords:**
- "google ads", "Facebook Ads", "meta facebook"
- "TikTok Ads", "SNAP ads"
- "OPENAI", "PictoryAI"
- "Google GSUITE" (when for marketing)

---

### Series O - Office/Materials (Material/Inventarier)
**Accounts:** 5410 (Equipment), 5460 (Consumables), 6110 (Office supplies)
**Identifying Keywords:**
- "Clas Ohlson", "Biltema", "Rusta"
- "TEMU" (supplies)
- "JULA"
- "Dollarstore"

---

### Series P - Professional Services (Professionella tjänster)
**Accounts:** 6590 (External services), 5420 (Software)
**Identifying Keywords:**
- "Shopify" (fees, not ads)
- "Crona kassasystem"
- "Fortnox"
- "Visma software"

---

### Series R - Travel (Resa)
**Accounts:** 5800, 5810 (Tickets), 5830 (Accommodation), 5890 (Other travel)
**Identifying Keywords:**
- "Airfare", "flygbiljett", "Pegasus"
- "hotel", "Booking.com", "OTEL"
- "Ryanair", "EDREAMS", "OPODO"
- "uber", "taksi"
- "sj app"

---

### Series S - Sales (Försäljning)
**Accounts:** 3051 (Sales goods), 2611 (Output VAT), 1948 (Sales account)
**Identifying Keywords:**
- "Sales Period"
- "Crona Kassa Sales"
- "Easy Cashier Sales"
- "Shopify POS Sales"
- STRIPE payments

---

### Series T - Card Transactions (Transaktioner kort)
**Accounts:** 1941 (Viva), 1947 (Worldline)
**Identifying Keywords:**
- "Viva Wallet Card"
- "Worldline kortbetalning"
- "Wallet2Wallet Transfer"
- "Viva Cashback"

---

### Series V - Vehicle (Fordon)
**Accounts:** 5610 (Car costs), 5611 (Fuel), 5619 (Other vehicle), 5620 (Truck), 1240 (Vehicle asset)
**Identifying Keywords:**
- "drivmedel", "ST1", "shell", "okq8", "circle K", "Preem"
- "AIMO PARK", "Aimo Park", "eparkera"
- "Besikta" (vehicle inspection)
- Vehicle purchase

---

### Series W - Work Services (Inköp tjänster)
**Accounts:** 4001 (Purchased services)
**Identifying Keywords:**
- "CVS CENTER"
- "Assemblin EL AB"
- "Elmontering"

---

### Series X - Currency Exchange (Valuta)
**Accounts:** 1942 (Wise USD), 1943 (Wise GBP), 1944 (Wise EUR), 1945 (Wise SEK)
**Identifying Keywords:**
- "Converted"
- "Topped up balance"
- "Balance cashback" (Wise)
- Currency transfers between accounts

---

### Series Y - Supplier Payments (Betalningar leverantör)
**Accounts:** 2441 (Supplier ledger - Future World Tech)
**Identifying Keywords:**
- "FUTURE WORLD TECH"
- Major supplier payments

---

### Series Z - Corrections (Korrigeringar)
**Accounts:** Various
**Identifying Keywords:**
- "Korrigering", "korrigerad"
- "Allokering"
- "Momsredovisning"
- Period-end adjustments

---

## 4. Voucher Number Assignment Rules

Within each series, vouchers are numbered sequentially starting from 1.
**Format:** `#VER [SERIES] [NUMBER] [DATE] "[DESCRIPTION]" [REGISTRATION_DATE]`

**Example:**
```
#VER V 1 20240906 "(ST1 ESKILSTUNA)" 20251212
#VER N 1 20241113 "(google ads 5215017274)" 20251212
#VER L 1 20241205 "Loan from Director to Company" 20251212
```

---

## 5. Edge Cases and Decision Logic

### Multi-Purpose Transactions
When a transaction could fit multiple categories, use this priority:
1. **Primary account** determines category
2. If unclear, use the **dominant amount**
3. If still unclear, use **description keywords**

### Corrections
- Corrections to previous vouchers stay in **Z series**
- Reference the original voucher in the description

### Viva/Worldline Card Purchases
- Card **purchases** for business expenses → categorize by expense type (V, O, R, etc.)
- Card **settlements and fees** → Series T
- **Cashback** → Series B (bank interest income)

### Related Party Transactions
- Director loans (in/out) → Series L
- Personal transfers to Ahmed/Mohammad → Series L
- Shareholder contributions → Series L

---

## 6. Mapping Tables

### Old to New Voucher Reference

The complete mapping is available in the accompanying Excel file or can be derived from the original vs. new file comparison.

**Key Conversions:**
- A 1-7 (external expenses abroad) → E series
- A 4, 6, 8, 10 (travel) → R series
- A 11-12, 38-40 (fuel) → V series
- A 71-73, 100-116 (ads) → N series
- A 164, 169, 171 (director loans) → L series
- A 91-92 (imports) → I series

---

## 7. For Future AI CTOs

### When Adding New Vouchers

1. **Identify the primary account** in the transaction
2. **Match against series definitions** in Section 2
3. **Use the next available number** in that series
4. **Keep descriptions consistent** with existing patterns

### When Auditing

1. Pull all vouchers by series for category-specific review
2. Verify account numbers match series expectations
3. Check for miscategorized transactions (e.g., fuel in advertising)

### Data Integrity Checks

```
For each series, verify:
- Account numbers are consistent with series definition
- Amounts balance (debits = credits)
- Dates are within fiscal year
- No duplicate voucher numbers within series
```

### Extending the System

If new transaction types emerge:
1. Check if they fit an existing series
2. If not, propose a new series letter (available: A, D, J, Q, U)
3. Document the new series in this file
4. Update all downstream systems

---

## 8. File Integrity

**Original File Hash:** [Generate before changes]
**New File Hash:** [Generate after changes]

**Validation Steps:**
1. Total debits = Total credits (balanced)
2. UB (closing balances) unchanged
3. RES (result accounts) unchanged
4. All 763+ original vouchers accounted for

---

## 9. Change Log

| Date | Version | Author | Changes |
|------|---------|--------|---------|
| 2026-01-07 | 1.0 | AI CTO Agent | Initial documentation created |

---

## 10. Appendix: Account Code Reference

### Key Account Codes Used

| Account | Description | Typical Series |
|---------|-------------|----------------|
| 1383 | Long-term deposits | H |
| 1460 | Inventory | I, Z |
| 1630 | Tax account | K |
| 1910 | Cash | S |
| 1930 | Company bank account | Multiple |
| 1941 | Viva.com bank | T |
| 1942 | Wise USD | X |
| 1943 | Wise GBP | X |
| 1944 | Wise EUR | X |
| 1945 | Wise SEK | X |
| 1947 | Worldline | T |
| 1948 | Sales account | S |
| 2441 | Future World Tech (supplier) | Y |
| 2611 | Output VAT 25% | S |
| 2641 | Input VAT | Multiple |
| 2893 | Related party debt | L, E |
| 3051 | Sales goods 25% | S |
| 4001 | Purchased services | W |
| 4545 | Import goods | I |
| 5010 | Rent | H |
| 5070 | Premises repairs | H |
| 5410 | Equipment | O, P |
| 5420 | Software | P |
| 5460 | Consumables | O |
| 5610 | Car costs | V |
| 5611 | Fuel | V |
| 5619 | Other vehicle costs | V |
| 5620 | Truck costs | V |
| 5810 | Tickets | R |
| 5830 | Accommodation | R |
| 5890 | Other travel | R |
| 5900 | Marketing general | N |
| 5910 | Advertising | N |
| 5911 | AI marketing tools | N |
| 6110 | Office supplies | O |
| 6212 | Mobile phone | C |
| 6310 | Business insurance | G |
| 6540 | IT services | C |
| 6570 | Bank costs | B |
| 6590 | External services | P |
| 6991 | External costs (deductible) | E, F |
| 6992 | External costs (non-deductible) | E |

---

**END OF DOCUMENTATION**
