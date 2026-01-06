# ✅ Klarna Q3 2025 - Updated Transactions

**File Updated:** MASTER_Q3_2025_COMPLETE.SE  
**Update Date:** October 27, 2025  
**Changes:** Removed old Klarna entries, added correct 3 transactions from Klarna analysis

---

## 📋 Updated Klarna Transactions in SE File

### **FINAL-013: TEMU.COM - Business supplies**
**Date:** July 3, 2025  
**Amount:** 339.00 SEK  
**Account:** 5460 (Förbrukningsmaterial - Office supplies)  
**From:** 2893 (Skulder till närstående - Personal advance)

```
#VER "" "FINAL-013" 20250703 "TEMU.COM - Business supplies"
{
    #TRANS 5460 {} 339.00 "Office supplies from TEMU"
    #TRANS 2893 {} -339.00 "Paid via Klarna - personal advance"
}
```

---

### **FINAL-014: TEMU.COM - Business supplies**
**Date:** July 8, 2025  
**Amount:** 702.00 SEK  
**Account:** 5460 (Förbrukningsmaterial - Office supplies)  
**From:** 2893 (Skulder till närstående - Personal advance)

```
#VER "" "FINAL-014" 20250708 "TEMU.COM - Business supplies"
{
    #TRANS 5460 {} 702.00 "Office supplies from TEMU"
    #TRANS 2893 {} -702.00 "Paid via Klarna - personal advance"
}
```

---

### **FINAL-015: TikTok Ads - Marketing expense**
**Date:** July 19, 2025  
**Amount:** 2,000.00 SEK  
**Account:** 5900 (Reklam och PR - Marketing/Advertising) - NO VAT  
**From:** 2893 (Skulder till närstående - Personal advance)

```
#VER "" "FINAL-015" 20250719 "TikTok Ads - Marketing expense"
{
    #TRANS 5900 {} 2000.00 "TikTok advertising campaign NO VAT"
    #TRANS 2893 {} -2000.00 "Paid via Klarna - personal advance"
}
```

---

## 💰 Summary

| Date | Transaction | Amount | Account | Category |
|------|-------------|--------|---------|----------|
| 2025-07-03 | TEMU business supplies | 339.00 | 5460 | Office supplies |
| 2025-07-08 | TEMU business supplies | 702.00 | 5460 | Office supplies |
| 2025-07-19 | TikTok advertising | 2,000.00 | 5900 | Marketing (NO VAT) |
| **TOTAL** | | **3,041.00** | | |

---

## ✅ Accounting Structure

All transactions follow the pattern:
- **DEBIT:** Expense account (5460 or 5900)
- **CREDIT:** Account 2893 (Skulder till närstående - Personal advance/debt to related party)

This correctly reflects:
1. Business expense recorded in appropriate expense account
2. Payment made from personal funds (debt to company)
3. Can be repaid later or remain as shareholder loan

---

## 📝 Removed Entries

**OLD Entries (No longer in SE file):**
- ~~FINAL-013: Aviation fee - flight booking~~ (was duplicate/incorrect)
- ~~FINAL-014: Klarna account interest charge~~ (was incorrect)

**NEW Entries (Now in SE file):**
- FINAL-013: TEMU July 3 (339 SEK)
- FINAL-014: TEMU July 8 (702 SEK)
- FINAL-015: TikTok July 19 (2,000 SEK)

---

**All Klarna transactions now properly recorded in MASTER_Q3_2025_COMPLETE.SE**
