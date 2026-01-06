# -*- coding: utf-8 -*-
"""
Update all accounting documentation files
Changes 4010 to 4110 and fixes bank account mappings
"""
import os
import re

base_path = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip"

# All accounting rules files
md_files = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file == 'KONTOPLAN_OCH_BOKFORINGSREGLER.md':
            md_files.append(os.path.join(root, file))
        if file.startswith('START_PROMPT'):
            md_files.append(os.path.join(root, file))

print(f"Found {len(md_files)} documentation files to update")

for filepath in md_files:
    print(f"\nUpdating: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace 4010 with 4110
    content = content.replace('4010', '4110')
    content = content.replace('| 4110 | Varuförbrukning |', '| 4110 | Kostnad sålda varor |')
    content = content.replace('| **4110** | Varuförbrukning |', '| **4110** | Kostnad sålda varor |')
    
    # Fix bank mappings in quick reference tables
    content = content.replace('| Kostnad | 4110 | Varuförbrukning |', '| Kostnad | 4110 | Kostnad sålda varor |')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated!")

print("\n" + "="*60)
print("All documentation files updated!")
print("="*60)
