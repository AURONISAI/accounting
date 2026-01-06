# 🔍 COMPANY ACCOUNT LOGIC ANALYSIS - FROM 20250720.SE

**Source File:** `master-branch/20250720.se`  
**Analysis Date:** October 19, 2025  
**Purpose:** Extract exact accounting logic and account usage for inventory transactions  

---

## 📋 **CRITICAL FINDINGS: ACCOUNT 1469 LOGIC**

### **What Account 1469 Actually Is:**
**Swedish:** "Förändring av lager av handelsvaror"  
**English:** "Change in inventory of goods"  
**BAS Category:** ASSET ACCOUNT (Balance Sheet)  
**Purpose:** STAGING/ALLOCATION account for inventory movements

---

## 🎯 **THE ACTUAL INVENTORY LOGIC FROM PREVIOUS PERIOD**

### **Transaction Flow for Marketing Gifts (From VER 609, 618, 620):**

#### **STEP 1: Initial Import Allocation (VER 609)**
```
Date: 2025-06-30
Description: "Allokering marknadsföringslager 15% från import"
Translation: "Allocation of marketing inventory 15% from import"

#TRANS 1469 {} 134382.80    [DEBIT: Marketing inventory allocation]
#TRANS 4545 {} -134382.80   [CREDIT: Reduce import cost]
```
**Logic:** When importing goods, 15% allocated to marketing inventory staging (1469)

#### **STEP 2: Marketing Gift Expense (VER 618)**
```
Date: 2025-06-30
Description: "Marknadsföringsgåvor enligt 15% policy för kinaprodukter"
Translation: "Marketing gifts according to 15% policy for China products"

#TRANS 5900 {} 18181.70     [DEBIT: Marketing expense]
#TRANS 1469 {} -18181.70    [CREDIT: Reduce staging account]
```
**Logic:** Record marketing gifts as expense, reduce allocation account

#### **STEP 3: Transfer to Main Inventory (VER 620)**
```
Date: 2025-09-26
Description: "Varor bags skor biliga for markiting to assest mellan att dela de"
Translation: "Goods bags shoes cheap for marketing to assets between sharing them"

#TRANS 1460 {} 134382.00    [DEBIT: Increase main inventory]
#TRANS 1469 {} -134382.00   [CREDIT: Clear staging account]
```
**Logic:** Transfer remaining marketing allocation back to main inventory

---

## 💡 **KEY INSIGHT: THE CORRECT 3-STEP PROCESS**

The previous period shows that marketing gifts follow this workflow:

1. **ALLOCATE** (Import time): 1469 receives allocation from import (4545)
2. **EXPENSE** (Period end): 5900 receives gifts, 1469 reduced
3. **TRANSFER** (Correction): Remaining 1469 balance transferred to 1460

**ENDING BALANCE FOR 1469:** -18,180.90 SEK (small negative = timing difference)

---

## 📊 **COMPLETE ACCOUNT STRUCTURE FOR INVENTORY**

### **Primary Accounts:**

| Account | Name | Type | Purpose |
|---------|------|------|---------|
| **1460** | Lager av handelsvaror | ASSET | Main inventory account |
| **1469** | Förändring av lager av handelsvaror | ASSET | Inventory change staging |
| **4110** | Kostnad sålda varor | EXPENSE | Cost of goods sold (COGS) |
| **4545** | Import av varor 25% moms | EXPENSE | Import purchases |
| **5460** | Förbrukningsmaterial | EXPENSE | Consumable materials |
| **5700** | Frakter och transporter | EXPENSE | Freight and transport |
| **5900** | Reklam och PR | EXPENSE | Marketing and PR (gifts) |
| **6990** | Övriga kostnader | EXPENSE | Other costs (damaged goods) |

---

## 🔄 **COST OF GOODS SOLD LOGIC (VER 614, 615)**

### **Transaction Structure:**

#### **Lady Coats COGS (VER 614)**
```
Date: 2025-06-30
Description: "KSV för sålda damjackor oktober 2024 - juni 2025"
Translation: "COGS for sold lady jackets October 2024 - June 2025"

#TRANS 4110 {} 163049.24    [DEBIT: COGS expense]
#TRANS 1460 {} -163049.24   [CREDIT: Reduce inventory]
```

#### **China Products COGS (VER 615)**
```
Date: 2025-06-30
Description: "KSV för sålda kinaprodukter oktober 2024 - juni 2025"
Translation: "COGS for sold China products October 2024 - June 2025"

#TRANS 4110 {} 42970.00     [DEBIT: COGS expense]
#TRANS 1460 {} -42970.00    [CREDIT: Reduce inventory]
```

**Total COGS:** 206,019.24 SEK

---

## 🎨 **INVENTORY ALLOCATION AT IMPORT (VER 608-611)**

The company allocates imported goods to multiple categories:

### **From Total Import (4545):**

1. **85% to Trading Inventory (VER 608)**
   ```
   #TRANS 1460 {} 761502.53    [Main inventory]
   #TRANS 4545 {} -761502.53
   ```

2. **15% to Marketing Inventory (VER 609)**
   ```
   #TRANS 1469 {} 134382.80    [Marketing allocation]
   #TRANS 4545 {} -134382.80
   ```

3. **Consumables (VER 610)**
   ```
   #TRANS 5460 {} 2249.62      [Materials]
   #TRANS 4545 {} -2249.62
   ```

4. **Freight Costs (VER 611)**
   ```
   #TRANS 5700 {} 114392.93    [Transport]
   #TRANS 4545 {} -114392.93
   ```

**Policy:** 85% trading, 15% marketing gifts

---

## 🚨 **DAMAGED/STOLEN GOODS LOGIC (VER 616, 617)**

### **Damaged Goods (VER 616)**
```
Date: 2025-06-30
Description: "Avskrivning av skadade damjackor (transport/knappar)"
Translation: "Write-off of damaged lady jackets (transport/buttons)"

#TRANS 6990 {} 9245.06       [DEBIT: Other expenses]
#TRANS 1460 {} -9245.06      [CREDIT: Reduce inventory]
```

### **Stolen Goods (VER 617)**
```
Date: 2025-01-31
Description: "Avskrivning av stulna damjackor (första 4 månader)"
Translation: "Write-off of stolen lady jackets (first 4 months)"

#TRANS 6990 {} 5462.99       [DEBIT: Other expenses]
#TRANS 1460 {} -5462.99      [CREDIT: Reduce inventory]
```

**Account for losses:** 6990 (Övriga kostnader / Other costs)

---

## 📈 **OPENING AND CLOSING BALANCES**

### **Account 1460 (Main Inventory):**
- **Closing Balance (UB):** 885,995.24 SEK

### **Account 1469 (Inventory Change Staging):**
- **Closing Balance (UB):** -18,180.90 SEK (negative = credit balance)

### **Account 4110 (COGS):**
- **Period Total (RES):** 206,019.24 SEK

### **Account 5900 (Marketing/PR):**
- **Period Total (RES):** 55,919.99 SEK (includes gifts 18,181.70)

---

## ✅ **CORRECT LOGIC FOR NEW PERIOD (Q3 2025)**

Based on the previous period analysis, here's what we should do:

### **For 25% Marketing Gift Policy:**

1. **Cost of Goods Sold (Normal Sales - 75%)**
   ```
   #TRANS 4110 {} [COGS Amount]
   #TRANS 1460 {} -[COGS Amount]
   ```

2. **Marketing Gifts (25% of Units)**
   ```
   #TRANS 5900 {} [Gift Value]
   #TRANS 1460 {} -[Gift Value]
   ```

**NOTE:** We do NOT use 1469 unless we're allocating at import time!

### **When to Use Account 1469:**
- ✅ **AT IMPORT:** Allocate portion to marketing inventory staging
- ✅ **DURING PERIOD:** Transfer from staging to main inventory or expense
- ❌ **NOT FOR:** Recording gifts when products already in main inventory (1460)

---

## 🔧 **CORRECTION NEEDED FOR OUR Q3 2025 FILE**

### **CURRENT (INCORRECT) LOGIC:**
```
Transaction 2: 5900 debit, 1469 credit (wrong - uses staging)
Transaction 3: 1460 debit, 1469 credit (wrong - unnecessary)
```

### **CORRECT LOGIC:**
```
Transaction 1: COGS
  4110 debit 45,344.24
  1460 credit -45,344.24

Transaction 2: Marketing Gifts (SIMPLIFIED)
  5900 debit 11,337.54
  1460 credit -11,337.54
```

**Reason:** Products are already in main inventory (1460). We don't need staging account (1469) because this isn't an import allocation - it's recording gifts from existing inventory.

---

## 📊 **ACCOUNT USAGE SUMMARY**

### **When Products Are In Main Inventory (1460):**
- Sales → 4110 (COGS) + reduce 1460
- Gifts → 5900 (Marketing) + reduce 1460
- Damaged → 6990 (Other costs) + reduce 1460

### **When Allocating At Import:**
- 85% → 1460 (main inventory)
- 15% → 1469 (marketing staging)
- Then expense gifts: 5900 + reduce 1469
- Then transfer remainder: 1460 + reduce 1469

---

## 🎯 **CONCLUSION**

**The correct approach for Q3 2025 inventory:**

Since we're working with existing inventory (not a new import), we should:
1. Record COGS directly: 4110 ↔ 1460
2. Record marketing gifts directly: 5900 ↔ 1460
3. **DO NOT use 1469** (staging account only for import allocations)

This matches Swedish accounting standards and company's proven methodology.

---

*Analysis completed based on 4,214 lines of previous period SE file*  
*Samis Jackets AB - Organization Number: 559489-5301*
