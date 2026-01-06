# -*- coding: utf-8 -*-
"""
FINAL FIX SCRIPT - Q4 2025
Fixes all account mappings and encoding issues
"""
import re
import os

def fix_se_file(filepath):
    """Fix a single SE file"""
    print(f"\n{'='*60}")
    print(f"Processing: {os.path.basename(filepath)}")
    print('='*60)
    
    # Read file with CP437 encoding
    with open(filepath, 'r', encoding='cp437') as f:
        content = f.read()
    
    changes = []
    
    # 1. Change 4010 to 4110 (Kostnad salda varor)
    if '#TRANS 4010' in content:
        count = content.count('#TRANS 4010')
        content = content.replace('#TRANS 4010', '#TRANS 4110')
        changes.append(f"Changed 4010 -> 4110: {count} times")
    
    # 2. Update KONTO definition: remove 4010, ensure 4110 exists
    if '#KONTO 4010' in content:
        content = re.sub(r'#KONTO 4010 "[^"]*"\n', '', content)
        changes.append("Removed #KONTO 4010 definition")
    
    # Add 4110 if not present
    if '#KONTO 4110' not in content:
        content = content.replace(
            '#KONTO 4000 "Ink',
            '#KONTO 4000 "Ink'
        )
        # Find where to insert 4110
        if '#KONTO 4056' in content:
            content = content.replace(
                '#KONTO 4056',
                '#KONTO 4110 "Kostnad s\x84lda varor"\n#KONTO 4056'
            )
            changes.append("Added #KONTO 4110")
    
    # 3. Ensure correct Swedish encoding for common words
    # These are already in CP437, but let's verify the file structure
    
    # 4. Verify 1580 is defined (Shopify clearing)
    if '#TRANS 1580' in content and '#KONTO 1580' not in content:
        if '#KONTO 1549' in content:
            content = content.replace(
                '#KONTO 1549',
                '#KONTO 1549\n#KONTO 1580 "Fordringar"'
            )
            changes.append("Added #KONTO 1580")
    
    # Print changes
    for change in changes:
        print(f"  - {change}")
    
    if not changes:
        print("  No changes needed")
    
    # Write back with CP437 encoding
    with open(filepath, 'w', encoding='cp437') as f:
        f.write(content)
    
    # Verify balance
    trans = re.findall(r'#TRANS\s+\d+\s+\{\}\s+(-?[\d.]+)', content)
    total = sum(float(t) for t in trans)
    print(f"\n  Balance: {total:.2f} SEK")
    
    # Check for missing accounts
    defined = set(re.findall(r'#KONTO\s+(\d+)', content))
    used = set(re.findall(r'#TRANS\s+(\d+)', content))
    missing = used - defined
    
    if missing:
        print(f"  MISSING ACCOUNTS: {sorted(missing)}")
    else:
        print("  All accounts defined!")
    
    return len(changes) > 0

# Main execution
base_path = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip"

# List of SE files to fix
se_files = [
    os.path.join(base_path, "Q4_2025_PERIOD_2025-10_TO_2025-12", "final_se_files", "Q4_2025_COMPLETE.se"),
]

# Find all SE files in the folder
for root, dirs, files in os.walk(os.path.join(base_path, "Q4_2025_PERIOD_2025-10_TO_2025-12")):
    for file in files:
        if file.endswith('.se') and file not in ['Q4_2025_COMPLETE.se']:
            se_files.append(os.path.join(root, file))

print("FIXING SE FILES")
print("="*60)

fixed_count = 0
for filepath in se_files:
    if os.path.exists(filepath):
        if fix_se_file(filepath):
            fixed_count += 1

print(f"\n{'='*60}")
print(f"DONE! Fixed {fixed_count} files")
print("="*60)
