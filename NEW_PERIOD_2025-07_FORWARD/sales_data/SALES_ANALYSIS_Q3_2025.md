# 📊 SALES ANALYSIS - Q3 2025
**Period:** July 1 - September 30, 2025  
**Source:** Easy Cashier POS System  
**File:** `sales Försäljningsrapport from 0107 to 30-09.csv`  
**Total Products Sold:** 433 line items  

---

## 💰 SALES SUMMARY

| Description | Amount SEK |
|-------------|------------|
| **Total Sales (ex VAT)** | **145,641.42** |
| **Total VAT (25%)** | **36,410.45** |
| **Total Sales (incl VAT)** | **182,051.87** |
| **Total COGS** | **93,505.25** |
| **Total Gross Profit** | **52,136.17** |
| **Gross Profit Margin** | **35.8%** |

---

## 🔍 IMPORTANT NOTES

### **COGS Discrepancy Found:**
- **Easy Cashier COGS:** 93,505.25 SEK
- **Inventory SIE COGS:** 45,344.24 SEK
- **Difference:** 48,161.01 SEK ⚠️

**Explanation:**
The Easy Cashier report shows COGS from the POS system perspective (what items cost when purchased). The inventory SIE file shows actual inventory movement during Q3 2025. The difference could be due to:
1. Inventory purchased in previous periods but sold in Q3
2. Different COGS calculation methods
3. Opening inventory values

**For this SIE file:** We will record ONLY the sales revenue and VAT. The COGS has already been recorded in the inventory SIE file (45,344.24 SEK), which represents actual inventory changes during Q3.

---

## 💳 PAYMENT BREAKDOWN

**Assumed:** All sales via Worldline card terminal (standard for retail)
- If cash sales exist, they are NOT tracked in Easy Cashier report
- Worldline processes card payments only

**Transaction Structure:**
1. DEBIT 1947 (Worldline - card payments): 182,051.87 SEK (sales + VAT)
2. CREDIT 3000 (Sales revenue): 145,641.42 SEK (ex VAT)
3. CREDIT 2610 (Utgående moms - VAT payable): 36,410.45 SEK

---

## 📋 PRODUCTS SOLD - TOP CATEGORIES

**Product Categories:**
- Women's coats and jackets (Model 1001-1048 series)
- Men's puffer jackets (018, 221, 8805, 8806, 9921, 9922 series)
- Women's puffer jackets (GY series, 5860, 618, 837, etc.)
- Children's jackets (INCI series - 111, 444, TM series)
- Leggings (multiple models - 1668, 6607, 9901, 9903, 9956, JJ1001, JJ1002)
- Sneakers (HZ series - men's and women's)
- Slippers (DY series - 615, 71504, 71602)
- Handbags (MS series - D8666, G8666, SY series, T8666)
- Men's sweaters (YR series - 24819, Model_3, Model_5)
- Sportswear/Tracksuits (MG series - AD256, BAJ, DL596, DV507, GD303, TZ302-304)
- Special items (Alex, LL knit sweaters, CF series, JP series)

**Top Sellers by Quantity:**
- Alex products: 74 units total
- LL Women's Knit Sweater: 27 units
- Leggings (various models): 50+ units
- Women's coats (Model 1000 series): 30+ units

---

## ✅ READY FOR SIE FILE

**Sales Transaction:**
- Recording Q3 2025 total sales from Easy Cashier POS
- All sales assumed via Worldline card terminal
- VAT at 25% standard rate
- COGS already recorded separately in inventory file

---

*Sales Analysis - Q3 2025*  
*Samis Jackets AB - Organization Number: 559489-5301*  
*Analysis Date: October 19, 2025*
