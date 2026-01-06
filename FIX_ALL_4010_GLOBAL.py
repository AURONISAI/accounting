#!/usr/bin/env python3
"""
GLOBAL FIX: Change all 4010 to 4110 in ALL SE files
Fixes BOTH #TRANS and #KONTO definitions
"""
import os
import re
from pathlib import Path

base_dir = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip")

# Find ALL .se files
se_files = list(base_dir.rglob("*.se"))
print(f"Found {len(se_files)} SE files to check")

fixed_count = 0
for se_file in se_files:
    try:
        # Try multiple encodings
        for encoding in ['cp437', 'utf-8', 'latin-1']:
            try:
                content = se_file.read_text(encoding=encoding)
                break
            except:
                continue
        
        original = content
        changes = []
        
        # Fix #TRANS 4010 -> #TRANS 4110
        if '#TRANS 4010' in content:
            count = content.count('#TRANS 4010')
            content = content.replace('#TRANS 4010', '#TRANS 4110')
            changes.append(f"  - Changed #TRANS 4010 -> 4110: {count} times")
        
        # Fix #KONTO 4010 -> remove it (4110 should already exist)
        if '#KONTO 4010' in content:
            content = re.sub(r'#KONTO 4010 "[^"]*"\n?', '', content)
            changes.append(f"  - Removed #KONTO 4010 definition")
        
        if content != original:
            # Write back with same encoding
            se_file.write_text(content, encoding='cp437')
            fixed_count += 1
            print(f"\n✅ FIXED: {se_file.relative_to(base_dir)}")
            for change in changes:
                print(change)
    except Exception as e:
        print(f"❌ Error with {se_file}: {e}")

print(f"\n" + "="*60)
print(f"DONE: Fixed {fixed_count} SE files")
print("="*60)
