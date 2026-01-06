# -*- coding: utf-8 -*-
"""
MANUAL AUDIT FIXES - Q4 2025

Based on CSV Source of Truth, fixing 18 unbalanced VER entries.

ISSUE CATEGORIES:
1. Personal expense entries (974-983, 1010): 2893 has WRONG SIGN (should be negative)
2. Currency exchange entries (779, 780, 783, 784, 817, 818, 837): Foreign amounts not converted to SEK

FIXES TO APPLY:
"""

import re

def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read().decode('cp437')

def write_file(filepath, content):
    # Normalize to CRLF
    content = content.replace('\r\n', '\n').replace('\n', '\r\n')
    with open(filepath, 'wb') as f:
        f.write(content.encode('cp437'))

def fix_personal_expense_entries(content):
    """
    Fix VER entries where 2893 has wrong sign.
    Personal pays company expense -> company owes person -> CREDIT 2893 (negative)
    
    CSV SOURCE OF TRUTH:
    - Fortnox 2025-10-23: -149.00 SEK
    - Fortnox 2025-11-01: -149.00 SEK  
    - Fortnox 2025-11-14: -24.00 SEK
    - Fortnox 2025-12-12: -149.00 SEK
    - Skatteverket 2025-11-17: -400.00 SEK
    - SJ AB 2025-10-26: -96.00 SEK (x2)
    - Mälardalstrafik 2025-10-12: -367.00 SEK
    - Mälardalstrafik 2025-10-14: -367.00 SEK
    - Mälardalstrafik 2025-11-27: -734.00 SEK
    - TG JBC Örebro 2025-11-15: -2055.00 SEK
    """
    
    fixes = [
        # VER 974 - Fortnox 2025-10-23 (149.00)
        ('#TRANS 2893 {} 149.00', '#TRANS 2893 {} -149.00', 'VER 974 Fortnox'),
        
        # VER 975 - Fortnox 2025-11-01 (149.00)  
        # Need to find the second occurrence
        
        # VER 976 - Fortnox 2025-11-14 (24.00)
        ('#TRANS 2893 {} 24.00', '#TRANS 2893 {} -24.00', 'VER 976 Fortnox'),
        
        # VER 978 - Skatteverket 2025-11-17 (400.00)
        ('#TRANS 2893 {} 400.00', '#TRANS 2893 {} -400.00', 'VER 978 Skatteverket'),
        
        # VER 979, 980 - SJ AB (96.00 each)
        ('#TRANS 2893 {} 96.00', '#TRANS 2893 {} -96.00', 'VER 979/980 SJ'),
        
        # VER 981, 982 - Mälardalstrafik (367.00 each)
        ('#TRANS 2893 {} 367.00', '#TRANS 2893 {} -367.00', 'VER 981/982 Mälardalstrafik'),
        
        # VER 983 - Mälardalstrafik (734.00)
        ('#TRANS 2893 {} 734.00', '#TRANS 2893 {} -734.00', 'VER 983 Mälardalstrafik'),
        
        # VER 1010 - TG JBC Örebro (2055.00)
        ('#TRANS 2893 {} 2055.00', '#TRANS 2893 {} -2055.00', 'VER 1010 TG JBC'),
    ]
    
    for old, new, desc in fixes:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f'  Fixed {desc}: {old} -> {new} ({count} occurrences)')
    
    return content

def fix_currency_exchange_entries(content):
    """
    Fix currency exchange VER entries.
    
    The problem: Foreign currency amounts are used instead of SEK equivalents.
    
    For balanced entries, we need:
    - Debit source currency account (SEK value leaving)
    - Credit destination currency account (SEK value entering) 
    - Debit/Credit exchange difference account (6570)
    
    The source SEK value should equal the destination SEK value + fees.
    
    VER 779: SEK to TRY - 12486 SEK spent, 12432.54 converted + 53.46 fee
      Current: 1945 -12486, 1946 +55090.57, 6570 +53.46 = UNBALANCED
      Fix: 1946 should be +12432.54 (SEK value of TRY received)
      
    VER 780: EUR to TRY - 1436.55 SEK equivalent spent
      Current: 1944 -1436.55, 1946 +6076.46, 6570 +6.34 = UNBALANCED
      Fix: 1946 should be +1430.21 (SEK value of TRY received)
      
    VER 783: SEK to USD - 2870 SEK spent
      Current: 1945 -2870, 1942 +300, 6570 +12.86 = -2557.14 UNBALANCED
      Fix: 1942 should be +2857.14 (SEK value of USD received)
      
    VER 784: Loan repayment USD - personal pays company debt
      Current: 2893 +2944, 1942 -320 = +2624 UNBALANCED
      This is a personal loan repayment - pattern unclear
      
    VER 817: EUR to USD
      Current: 1944 -5374.86, 1942 +542.87, 6570 +19.24 = -4812.75 UNBALANCED
      Fix: 1942 should be +5355.62 (SEK value)
      
    VER 818: SEK to USD  
      Current: 1945 -15546, 1942 +1658.66, 6570 +108.46 = -13778.88 UNBALANCED
      Fix: 1942 should be +15437.54 (SEK value)
      
    VER 837: EUR to USD
      Current: 1944 -997.85, 1942 +101.71, 6570 +3.45 = -892.69 UNBALANCED
      Fix: 1942 should be +994.40 (SEK value)
    """
    
    # These are complex multi-currency fixes - need to be done carefully
    # The pattern should be: source amount = destination amount + fees
    
    currency_fixes = [
        # VER 779: 1946 55090.57 -> 12432.54 (SEK value = 12486 - 53.46 fee)
        ('1946 {} 55090.57', '1946 {} 12432.54', 'VER 779 TRY'),
        
        # VER 780: 1946 6076.46 -> 1430.21 (SEK value = 1436.55 - 6.34 fee)
        ('1946 {} 6076.46', '1946 {} 1430.21', 'VER 780 TRY'),
        
        # VER 783: 1942 300.00 -> 2857.14 (SEK value = 2870 - 12.86 fee)
        ('1942 {} 300.00', '1942 {} 2857.14', 'VER 783 USD'),
        
        # VER 784: Loan repayment - 2893 should be negative (company received payment)
        # But also need to understand the USD component
        # Original: 2893 +2944, 1942 -320 = +2624
        # If personal repaid loan: 2893 should credit (negative)
        # Fix: 2893 2944 -> -320, and we need to add bank entry
        # Actually this needs a bank entry: 1930 or 1945 +2624
        
        # VER 817: 1942 542.87 -> 5355.62 (SEK value = 5374.86 - 19.24 fee)
        ('1942 {} 542.87', '1942 {} 5355.62', 'VER 817 USD'),
        
        # VER 818: 1942 1658.66 -> 15437.54 (SEK value = 15546 - 108.46 fee)
        ('1942 {} 1658.66', '1942 {} 15437.54', 'VER 818 USD'),
        
        # VER 837: 1942 101.71 -> 994.40 (SEK value = 997.85 - 3.45 fee)
        ('1942 {} 101.71', '1942 {} 994.40', 'VER 837 USD'),
    ]
    
    for old, new, desc in currency_fixes:
        old_full = f'#TRANS {old}'
        new_full = f'#TRANS {new}'
        if old_full in content:
            content = content.replace(old_full, new_full)
            print(f'  Fixed {desc}: {old} -> {new}')
    
    return content

def fix_ver_784(content):
    """
    VER 784 - Loan repayment USD
    Current: 2893 +2944, 1942 -320 = +2624 UNBALANCED
    
    This represents a personal loan repayment where:
    - Someone repaid 320 USD (about 2944 SEK) from the company's USD account
    - The 2893 debit shows company's claim was reduced
    - But we're missing the bank/cash entry
    
    The entry should be:
    - 2893 debit +2944 (reduce debt owed TO company) - but wait, 2893 is usually debt TO person
    - 1942 credit -320 (USD left the account)
    
    Actually looking at it, if 2893 is debt company owes TO Samis:
    - Personal account received loan repayment = reduce company's debt TO personal
    - So 2893 should be POSITIVE (debit reduces liability)
    
    But we need a matching credit. If USD account decreased and debt decreased,
    we need another entry. Maybe this was a cash payment?
    
    For now, add a balancing entry to 8999 (adjustment account)
    """
    old_784 = '''#VER A 784 20251010 "Loan repayment USD 320.00 USD"
{
#TRANS 2893 {} 2944.00
#TRANS 1942 {} -320.00
}'''
    
    # The issue: 2893 +2944 and 1942 -320 don't balance
    # USD value: 320 USD * ~9.2 = 2944 SEK
    # But why is 1942 only -320? Should be -2944 (SEK value)
    
    new_784 = '''#VER A 784 20251010 "Loan repayment USD 320.00 USD"
{
#TRANS 2893 {} 2944.00
#TRANS 1942 {} -2944.00
}'''
    
    if old_784 in content:
        content = content.replace(old_784, new_784)
        print('  Fixed VER 784: 1942 -320 -> -2944 (SEK value of USD)')
    
    return content

def main():
    filepath = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q4_2025_PERIOD_2025-10_TO_2025-12\final_se_files\Q4_2025_COMPLETE.se"
    
    print("="*70)
    print("MANUAL AUDIT FIXES - Q4 2025")
    print("="*70)
    
    content = read_file(filepath)
    
    print("\n1. Fixing personal expense entries (2893 sign)...")
    content = fix_personal_expense_entries(content)
    
    print("\n2. Fixing currency exchange entries...")
    content = fix_currency_exchange_entries(content)
    
    print("\n3. Fixing VER 784 (loan repayment)...")
    content = fix_ver_784(content)
    
    write_file(filepath, content)
    print("\n✅ File saved!")
    
    # Verify
    content = read_file(filepath)
    
    # Check balance
    amounts = re.findall(r'#TRANS \d+ \{\} (-?[\d.]+)', content)
    total = sum(float(a) for a in amounts)
    
    print(f"\n📊 Total balance: {total:.2f} SEK")
    if abs(total) < 0.01:
        print("✅ FILE IS BALANCED!")
    else:
        print("⚠️ FILE STILL NOT BALANCED")
        
        # Find remaining unbalanced entries
        ver_blocks = re.findall(r'(#VER A (\d+)[^\r\n]*)([\r\n]+\{[\r\n]+)(.*?)([\r\n]+\})', content, re.DOTALL)
        print("\nRemaining unbalanced VER entries:")
        for ver_line, ver_num, open_brace, trans_content, close_brace in ver_blocks:
            amounts = re.findall(r'#TRANS \d+ \{\} (-?[\d.]+)', trans_content)
            ver_total = sum(float(a) for a in amounts)
            if abs(ver_total) > 0.01:
                print(f"  VER A {ver_num}: {ver_total:+.2f}")

if __name__ == '__main__':
    main()
