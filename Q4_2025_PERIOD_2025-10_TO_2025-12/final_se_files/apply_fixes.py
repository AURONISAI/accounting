# -*- coding: utf-8 -*-
"""
Complete fix script:
1. Fix insurance (remove moms from försäkring)
2. Add missing Shopify sale for VER A 902 settlement
"""
import re

def read_file_cp437(filepath):
    """Read file with CP437 encoding"""
    with open(filepath, 'rb') as f:
        content = f.read()
    content = content.replace(b'\r\n', b'\n')
    return content.decode('cp437')

def write_file_cp437(filepath, content):
    """Write file with CP437 encoding and CRLF line endings"""
    lines = content.split('\n')
    with open(filepath, 'wb') as f:
        for i, line in enumerate(lines):
            f.write(line.encode('cp437'))
            if i < len(lines) - 1:
                f.write(b'\r\n')

def main():
    filepath = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q4_2025_PERIOD_2025-10_TO_2025-12\final_se_files\Q4_2025_COMPLETE.se"
    
    print("=" * 60)
    print("FIXING Q4_2025_COMPLETE.se")
    print("=" * 60)
    
    content = read_file_cp437(filepath)
    
    # 1. Fix insurance transaction (VER A 856)
    # Find and replace the försäkring transaction
    old_insurance = '''#VER A 856 20251017 "Försäkring 53020525"
{
#TRANS 6310 {} 3010.40
#TRANS 2641 {} 752.60
#TRANS 1930 {} -3763.00
}'''
    
    new_insurance = '''#VER A 856 20251017 "Försäkring 53020525"
{
#TRANS 6310 {} 3763.00
#TRANS 1930 {} -3763.00
}'''
    
    if old_insurance in content:
        content = content.replace(old_insurance, new_insurance)
        print("✅ Fixed insurance transaction (removed moms)")
    else:
        print("ℹ️ Insurance already fixed or not found")
    
    # 2. Add missing Shopify sale at the end
    # Check if VER A 1011 already exists
    if '#VER A 1011' in content:
        print("ℹ️ VER A 1011 already exists")
    else:
        # The 39934.97 SEK settlement needs a corresponding sale
        # 39934.97 incl moms = 31947.98 exkl moms + 7986.99 moms (25%)
        total = 39934.97
        sales_excl_moms = round(total / 1.25, 2)  # 31947.98
        moms = round(total - sales_excl_moms, 2)  # 7986.99
        
        new_ver = f'''

#VER A 1011 20251128 "Shopify Sale for Wise payout"
{{
#TRANS 1582 {{}} {total:.2f}
#TRANS 3001 {{}} -{sales_excl_moms:.2f}
#TRANS 2610 {{}} -{moms:.2f}
}}'''
        
        content = content.rstrip() + new_ver
        print(f"✅ Added VER A 1011 - Shopify Sale ({total:.2f} SEK)")
    
    # Write file
    write_file_cp437(filepath, content)
    print("\n✅ File saved!")
    
    # Verify balances
    content = read_file_cp437(filepath)
    
    # Check 1582 balance
    trans_1582 = re.findall(r'#TRANS 1582 \{\} (-?[\d.]+)', content)
    total_1582 = sum(float(amt) for amt in trans_1582)
    print(f"\n📊 Account 1582 (Shopify) balance: {total_1582:.2f} SEK")
    if abs(total_1582) < 0.01:
        print("   ✅ BALANCED!")
    else:
        print(f"   ⚠️ Not balanced")
    
    # Check 1947 balance
    trans_1947 = re.findall(r'#TRANS 1947 \{\} (-?[\d.]+)', content)
    total_1947 = sum(float(amt) for amt in trans_1947)
    print(f"\n📊 Account 1947 (Worldline) balance: {total_1947:.2f} SEK")
    print("   ℹ️ This represents pending deposits at Q4 end")
    
    # Count VER entries
    ver_count = len(re.findall(r'#VER A \d+', content))
    print(f"\n📊 Total VER entries: {ver_count}")

if __name__ == '__main__':
    main()
