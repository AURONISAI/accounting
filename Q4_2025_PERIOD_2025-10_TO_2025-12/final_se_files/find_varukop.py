# -*- coding: utf-8 -*-
import re

with open('Q4_2025_COMPLETE.se', 'r', encoding='cp437') as f:
    content = f.read()

# Find all VER blocks
ver_blocks = re.findall(r'(#VER\s+A\s+\d+\s+\d+\s+"[^"]+"\s*\{[^}]+\})', content, re.DOTALL)

print('TRANSACTIONS WITH 4010 (Varukop):')
print('='*60)
for block in ver_blocks:
    if '#TRANS 4010' in block:
        print(block)
        print()

print('\n' + '='*60)
print('TRANSACTIONS WITH 4000 (Inkop av varor fran Sverige):')
print('='*60)
for block in ver_blocks:
    if '#TRANS 4000' in block:
        print(block)
        print()

print('\n' + '='*60)
print('TRANSACTIONS WITH 2441 (Future World Tech):')
print('='*60)
for block in ver_blocks:
    if '#TRANS 2441' in block:
        print(block)
        print()
