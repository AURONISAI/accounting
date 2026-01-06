# -*- coding: utf-8 -*-
import re

with open('Q4_2025_COMPLETE.se', 'r', encoding='cp437') as f:
    content = f.read()

# Parse all TRANS entries
trans_pattern = r'#TRANS\s+(\d+)\s+\{\}\s+(-?[\d.]+)'
all_trans = re.findall(trans_pattern, content)

# Calculate sum per account
account_sums = {}
for account, amount in all_trans:
    account_sums[account] = account_sums.get(account, 0) + float(amount)

# Calculate total balance
total = sum(account_sums.values())

print('='*60)
print('FINAL BALANCE CHECK')
print('='*60)
print(f'Total balance: {total:.2f} SEK')
print()
print('Key account balances:')
print(f'  2641 (Ingaende moms): {account_sums.get("2641", 0):.2f}')
print(f'  2610 (Utgaende moms): {account_sums.get("2610", 0):.2f}')
print(f'  2650 (Moms redovisning): {account_sums.get("2650", 0):.2f}')
print(f'  2893 (Personal debt): {account_sums.get("2893", 0):.2f}')
print(f'  1582 (Shopify clearing): {account_sums.get("1582", 0):.2f}')
print(f'  1947 (Worldline clearing): {account_sums.get("1947", 0):.2f}')
print()

# Count VER blocks
ver_count = len(re.findall(r'#VER\s+A\s+\d+', content))
print(f'Total VER entries: {ver_count}')
print()

if abs(total) < 0.01:
    print('FILE IS BALANCED!')
else:
    print('FILE IS NOT BALANCED!')

# Check for remaining incorrect VAT
print()
print('='*60)
print('REMAINING MOMS ISSUES')
print('='*60)

ver_blocks = re.findall(r'(#VER\s+A\s+\d+\s+\d+\s+"[^"]+"\s*\{[^}]+\})', content, re.DOTALL)

no_vat_keywords = ['google', 'tiktok', 'facebook', 'meta', 'instagram', 'forsakring', 
                   'insurance', 'skatteverket', 'pegasus', 'turkish', 'yesim']

problems = []
for block in ver_blocks:
    if '#TRANS 2641' in block:
        desc_match = re.search(r'"([^"]+)"', block)
        desc = desc_match.group(1).lower() if desc_match else ''
        
        for keyword in no_vat_keywords:
            if keyword in desc:
                ver_match = re.search(r'VER\s+A\s+(\d+)', block)
                ver_num = ver_match.group(1) if ver_match else 'Unknown'
                problems.append(f'VER {ver_num}: {desc_match.group(1)}')
                break

if problems:
    for p in problems:
        print(f'PROBLEM: {p}')
else:
    print('No remaining moms issues found!')
