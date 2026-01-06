#!/usr/bin/env python3
"""
Update all START_PROMPT files with correct account mappings
"""
import os
from pathlib import Path

base_dir = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip")

# The critical section to add after "LÄS DETTA FÖRST"
CRITICAL_SECTION = '''
---

# ⚠️ KRITISKA KONTO-MAPPNINGAR (LÄRDOM FRÅN VISMA-EXPORT)

## BANKKONTON - MYCKET VIKTIGT!

| Konto | Bank/System | Användning |
|-------|-------------|------------|
| **1930** | **ENDAST MARGINALEN** | Företagskontot - ALDRIG Nordea! |
| **2893** | Nordea, Amex, Klarna, Remamber | Skulder närstående - ALLA personliga utlägg |
| **1941** | Viva.com | Viva bankkonto |
| **1942** | Wise USD | Dollar-konto |
| **1943** | Wise GBP | Pund-konto |
| **1944** | Wise EUR | Euro-konto |
| **1945** | Wise SEK | SEK-konto |
| **1947** | Worldline | Kortbetalningar butik |

## VARUINKÖP - ANVÄND RÄTT KONTON!

| Konto | Namn | Användning |
|-------|------|------------|
| **4110** | Kostnad sålda varor | Varuförbrukning (ALDRIG 4010!) |
| **4001** | Inköp av tjänst | Tjänster (el, installation) |
| **4545** | Import av varor 25% | Import med moms |
| **5460** | Förbrukningsmaterial | Temu, förpackning, emballage |

### ⛔ ANVÄND ALDRIG DESSA KONTON:
- **4010** - Finns INTE i Vismas kontoplan! Använd 4110 istället!
- **1946** - Finns INTE! Använd 1940 eller specifika Wise-konton
- **1582** - Finns INTE! Använd 1580 för Shopify clearing
- **8310** - Finns INTE! Använd 8311 för ränteintäkter

'''

# The corrected bank CSV section
CORRECT_BANK_CSV = '''### Bank-CSV-filer att bearbeta:
```
marginalen/*.csv                 → Konto 1930 (ENDAST Marginalen!)
nordea/PERSONKONTO*.csv          → Konto 2893 (personliga utlägg)
amex/*.csv                       → Konto 2893 (personliga utlägg)
klarna/*.csv                     → Konto 2893 (personliga utlägg)
remamber/*.csv                   → Konto 2893 (personliga utlägg)
wise/statement_*_SEK_*.csv       → Konto 1945
wise/statement_*_EUR_*.csv       → Konto 1944
wise/statement_*_USD_*.csv       → Konto 1942
wise/statement_*_GBP_*.csv       → Konto 1943
wise/statement_*_TRY_*.csv       → Konto 1940
viva/*.csv                       → Konto 1941
worldline/*.csv                  → Konto 1947
```
'''

# Find all START_PROMPT files
start_prompts = list(base_dir.glob("Q*_2026*/START_PROMPT*.md"))
print(f"Found {len(start_prompts)} START_PROMPT files")

for file_path in start_prompts:
    content = file_path.read_text(encoding='utf-8')
    original = content
    
    # Add critical section if not present
    if "KRITISKA KONTO-MAPPNINGAR" not in content:
        # Insert after the first "---" following "STEG 2"
        insert_point = content.find("---\n\n# PROJEKTBESKRIVNING")
        if insert_point > 0:
            content = content[:insert_point] + CRITICAL_SECTION + content[insert_point:]
    
    # Fix the bank CSV section - replace old incorrect mapping
    old_patterns = [
        'nordea/PERSONKONTO*.csv          → Konto 1930',
        'nordea/PERSONKONTO*.csv          -> Konto 1930',
    ]
    
    for old in old_patterns:
        if old in content:
            # Find and replace the whole bank-CSV section
            start_idx = content.find("### Bank-CSV-filer att bearbeta:")
            if start_idx > 0:
                # Find the end of this section (next ### or ## or ---)
                end_idx = content.find("### Shopify-data:", start_idx)
                if end_idx == -1:
                    end_idx = content.find("## STEG 2", start_idx + 10)
                if end_idx > start_idx:
                    content = content[:start_idx] + CORRECT_BANK_CSV + "\n" + content[end_idx:]
            break
    
    # Also ensure 4010 references are corrected
    content = content.replace('4010', '4110')
    
    if content != original:
        file_path.write_text(content, encoding='utf-8')
        print(f"✅ Updated: {file_path.name}")
    else:
        print(f"⚪ No changes: {file_path.name}")

print("\nDone updating START_PROMPT files!")
