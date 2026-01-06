# 📖 ACCOUNTING RULES - MASTER REFERENCE Q4 2025
## Swedish EUBAS97 Standards for Samis Jackets AB

**Period:** Q4 2025 (October 1 - December 31, 2025)  
**Standard:** EUBAS97 (Swedish Small Business Accounting)  
**VAT Rate:** 25% (Swedish standard)  

---

## 🎯 QUICK REFERENCE - EXPENSE ROUTING

### WITH 25% VAT DEDUCTION (Moms Ingående → 2641)
| Expense | Account | Example Merchants |
|---------|---------|-------------------|
| Rent/Lokalhyra | 5010 | Lagar Hyra, office rent |
| Software | 5410 | Fortnox, Visma, Google Suite, Shopify |
| Office supplies | 5460 | Hemköp, TEMU (bulk), Clas Ohlson |
| Admin fees | 6250 | Bolagsverket, registration fees |

**VAT Calculation:** Net = Total ÷ 1.25, VAT = Total × 0.20

### WITHOUT VAT DEDUCTION (0% / Exempt)
| Expense | Account | Example Merchants |
|---------|---------|-------------------|
| Travel | 5610 | Flights, hotels, Moneygram |
| Vehicle insurance | 5620 | If Försäkring, car insurance |
| Advertising | 5900 | TikTok, Facebook, Google Ads |
| Bank fees | 6570 | Monthly fees, card charges |

---

## 💳 PAYMENT SOURCE → CREDIT ACCOUNT

| Payment Source | Credit Account | Description |
|----------------|----------------|-------------|
| Marginalen Bank | 1930 | Primary business bank |
| Personal cards (Nordea, Klarna, Remamber) | 2893 | Shareholder debt |
| Wise SEK | 1945 | Multi-currency SEK |
| Wise USD | 1942 | Multi-currency USD |
| Wise EUR | 1944 | Multi-currency EUR |
| Viva Wallet | 1941 | Card payment platform |

---

## 📊 TRANSACTION TEMPLATES

### Template 1: Software with VAT (from Marginalen)
```
#VER "" "VER-XXX" YYYYMMDD "Software description"
{
    #TRANS 5410 {} [Net amount] "Software expense"
    #TRANS 2641 {} [VAT amount] "Input VAT 25%"
    #TRANS 1930 {} -[Total] "Marginalen payment"
}
```

### Template 2: Advertising NO VAT (from Personal Card)
```
#VER "" "VER-XXX" YYYYMMDD "TikTok Ads"
{
    #TRANS 5900 {} [Total amount] "Advertising expense"
    #TRANS 2893 {} -[Total amount] "Personal card debt"
}
```

### Template 3: Bank Fee (from Marginalen)
```
#VER "" "VER-XXX" YYYYMMDD "Monthly bank fee"
{
    #TRANS 6570 {} [Amount] "Bank fee"
    #TRANS 1930 {} -[Amount] "Marginalen"
}
```

### Template 4: Sales Revenue (Worldline)
```
#VER "" "VER-XXX" YYYYMMDD "Daily sales"
{
    #TRANS 1947 {} [Total] "Worldline receivable"
    #TRANS 3051 {} -[Net] "Sales revenue"
    #TRANS 2611 {} -[VAT] "Output VAT 25%"
}
```

### Template 5: Worldline Settlement
```
#VER "" "VER-XXX" YYYYMMDD "Worldline settlement"
{
    #TRANS 1930 {} [Amount] "Bank receives"
    #TRANS 1947 {} -[Amount] "Worldline cleared"
}
```

### Template 6: COGS (Inventory Reduction)
```
#VER "" "VER-XXX" YYYYMMDD "Cost of goods sold Q4"
{
    #TRANS 4110 {} [COGS amount] "Cost of goods sold"
    #TRANS 1460 {} -[COGS amount] "Inventory reduction"
}
```

---

## 🔍 MERCHANT CLASSIFICATION RULES

### 5900 - Advertising/Marketing (NO VAT)
- TikTok Ads
- Facebook/Meta Ads
- Google Ads
- Instagram promotion
- Marketing agency fees

### 5410 - Software/Subscriptions (25% VAT)
- Fortnox
- Visma
- Google Workspace/G Suite
- Shopify
- Microsoft 365
- Easy Cashier POS

### 5460 - Office Supplies (25% VAT)
- TEMU (bulk orders for business)
- Hemköp
- Clas Ohlson
- IKEA (office furniture)
- Amazon (office items)

### 5610 - Travel Expenses (NO VAT)
- SAS/Norwegian/other airlines
- Hotels
- Taxi/Uber for business
- Moneygram (business transfers)
- Aviation fees

### 6570 - Bank Fees (NO VAT)
- Marginalen monthly fee
- Card transaction fees
- Currency exchange fees
- Account maintenance

### 5010 - Rent (25% VAT)
- Lagar Hyra
- Office/store rent
- Warehouse rent

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Wrong VAT account for payments:**
   - ❌ 1630 for VAT paid to Skatteverket
   - ✅ 2650 for VAT paid to Skatteverket

2. **Double-counting transfers:**
   - ❌ Recording Marginalen → Wise from BOTH accounts
   - ✅ Recording ONLY from sending account (Marginalen)

3. **VAT on advertising:**
   - ❌ Adding 25% VAT to TikTok/Facebook ads
   - ✅ No VAT deduction on advertising

4. **Personal expenses:**
   - ❌ Including personal purchases from Nordea/Klarna
   - ✅ Filtering to business-only transactions

5. **Wrong inventory account:**
   - ❌ Using 1469 for existing inventory COGS
   - ✅ Using 1460 direct for COGS from existing stock

---

## 📅 Q4 2025 - YEAR-END CLOSING NOTES

⚠️ **THIS IS THE FINAL QUARTER OF FISCAL YEAR 2025**

1. **Opening Inventory:** 764,165.17 SEK (from Q3 2025 ending)
2. **Period End:** December 31, 2025
3. **🎯 YEAR-END REQUIREMENTS:**
   - **Physical inventory count** as of December 31, 2025
   - Review all receivables for collectibility (write-offs?)
   - Verify all payables are recorded
   - Check for accrued expenses (services received, not invoiced)
   - Check for prepaid expenses (paid in 2025, benefit in 2026)
   - Annual VAT reconciliation
   - Prepare for Årsredovisning (Annual Report)
   - Prepare for Bokslut (Annual Closing)

---

**Reference:** Based on Q3 2025 methodology (proven successful)
