# -*- coding: utf-8 -*-
import re

fp = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q4_2025_PERIOD_2025-10_TO_2025-12\final_se_files\Q4_2025_COMPLETE.se"
with open(fp, 'rb') as f:
    c = f.read().decode('cp437')

print("="*70)
print("MOMS AUDIT - CHECKING FOR INCORRECT VAT")
print("="*70)

# NO-VAT keywords (should NOT have 2641)
no_vat_keywords = [
    'google', 'tiktok', 'facebook', 'meta', 'instagram',  # Advertising
    'försäkring', 'forsakring', 'insurance',  # Insurance
    'skatteverket',  # Government
]

# Find all VER blocks
ver_blocks = re.findall(r'(#VER A (\d+) (\d{8}) "([^"]+)"[\r\n]+\{[\r\n]+)(.*?)([\r\n]+\})', c, re.DOTALL)

print(f"Total VER blocks: {len(ver_blocks)}")
print()

problems = []
for full_match in ver_blocks:
    ver_line, ver_num, date, desc, trans, close = full_match
    
    has_2641 = '#TRANS 2641' in trans
    desc_lower = desc.lower()
    
    # Check if this should NOT have VAT but does
    for keyword in no_vat_keywords:
        if keyword in desc_lower and has_2641:
            moms_match = re.search(r'#TRANS 2641 \{\} (-?[\d.]+)', trans)
            moms_amt = moms_match.group(1) if moms_match else "?"
            problems.append((ver_num, date, desc, moms_amt, keyword.upper()))

print("PROBLEMS - TRANSACTIONS WITH VAT THAT SHOULD NOT HAVE VAT:")
print("-"*70)
if problems:
    for ver_num, date, desc, moms_amt, keyword in problems:
        print(f"VER A {ver_num} ({date[:4]}-{date[4:6]}-{date[6:8]})")
        print(f"  Description: {desc}")
        print(f"  Moms (2641): {moms_amt} SEK")
        print(f"  Issue: {keyword} - SHOULD NOT HAVE VAT")
        print()
else:
    print("  None found!")
    
print()
print("="*70)
print("CHECKING TRAVEL EXPENSES (might have VAT issues)")
print("="*70)

travel_keywords = ['sj ab', 'mälardalstrafik', 'tåg', 'flyg', 'flight', 'resa']
for full_match in ver_blocks:
    ver_line, ver_num, date, desc, trans, close = full_match
    desc_lower = desc.lower()
    
    for keyword in travel_keywords:
        if keyword in desc_lower and '#TRANS 2641' in trans:
            moms_match = re.search(r'#TRANS 2641 \{\} (-?[\d.]+)', trans)
            moms_amt = moms_match.group(1) if moms_match else "?"
            print(f"VER A {ver_num}: {desc}")
            print(f"  Has moms: {moms_amt} SEK")
            print(f"  Note: Swedish domestic train tickets CAN have VAT (6%)")
            print()
