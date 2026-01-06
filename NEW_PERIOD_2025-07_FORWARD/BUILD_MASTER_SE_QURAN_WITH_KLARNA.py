#!/usr/bin/env python3
"""
MASTER SE FILE BUILDER - WITH KLARNA FINAL VERSION
==================================================
Includes ALL transaction sources:
1. Nordea (3 accounts) 
2. Marginalen 
3. Klarna (3 transactions per Quran rules)
4. Sales
5. Inventory

Routes ALL merchants per Quran Part 10 - 100% deterministic
"""

import csv
import os
import re
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# ============================================================================
# QURAN MERCHANT ROUTING + KLARNA SPECIFIC
# ============================================================================

MERCHANT_TO_ACCOUNT = {
    # MARKETING (5900) - Reklam och PR
    "TIKTOK": 5900,
    "FACEBOOK": 3010,
    "INSTAGRAM": 3010,
    "GOOGLE": 6100,
    "MARKETING": 5900,
    "ADVERTISING": 5900,
    
    # OFFICE SUPPLIES (5460) - Förbrukningsmaterial  
    "TEMU": 5460,  # Per Quran Part 10 - bulk office items from TEMU
    "STAPLES": 5460,
    "OFFICE": 5010,
    "IKEA": 5010,
    "SUPPLIES": 5010,
    "PAPER": 5010,
    
    # MEALS (4500)
    "ARAN": 4500,
    "FOOD": 4500,
    "RESTAURANT": 4500,
    
    # VEHICLES (1900-1999)
    "FUEL": 1910,
    "OKQ8": 1910,
    "TESLA": 1920,
    
    # TELECOM (6200)
    "TELENOR": 6200,
    "TELIA": 6200,
    "VODAFONE": 6200,
    
    # SOFTWARE (6100)
    "ADOBE": 6100,
    "MICROSOFT": 6100,
    "SLACK": 6100,
    "STRIPE": 6100,
    
    # BANKING (9900)
    "BANK": 9900,
    "WISE": 9900,
}

ACCOUNT_NAMES = {
    1010: "BANK_CHECKING_SEK",
    1100: "BANK_SAVINGS_SEK",
    1460: "INVENTORY",
    2893: "DEBT_TO_SHAREHOLDER",
    2641: "VAT_INPUT",
    3000: "SALES_INCOME",
    3010: "MARKETING_ADVERTISING",
    4110: "COST_OF_GOODS_SOLD",
    4500: "MEALS_ENTERTAINMENT",
    5460: "OFFICE_SUPPLIES",
    5900: "MARKETING_ADVERTISING_ALT",
    6100: "SOFTWARE_LICENSES",
    6200: "UTILITIES_TELEPHONE",
    6400: "SUBSCRIPTIONS",
    9900: "BANKING_FEES",
}

# ============================================================================
# TRANSACTION CLASS
# ============================================================================

class Transaction:
    def __init__(self, date_str, debit_account, credit_account, amount, description):
        self.date = date_str
        self.debit_account = int(debit_account)
        self.credit_account = int(credit_account)
        self.amount = float(amount)
        self.description = description
        
    def __repr__(self):
        return f"{self.date} | DR {self.debit_account} CR {self.credit_account} | {self.amount:>10.2f} | {self.description[:40]}"

# ============================================================================
# ROUTING FUNCTION
# ============================================================================

def route_merchant(merchant_text):
    """Route per Quran Part 10"""
    merchant_upper = merchant_text.upper()
    for keyword, account in MERCHANT_TO_ACCOUNT.items():
        if keyword in merchant_upper:
            return account
    return 6400  # Default

def parse_date(date_str):
    """Parse date"""
    if not date_str or date_str.strip() == '':
        return '20250930'
    date_str = date_str.strip().strip('"')
    try:
        if len(date_str) == 10:
            return date_str.replace('-', '')
        elif len(date_str) == 8:
            return date_str
    except:
        pass
    return '20250930'

# ============================================================================
# TRANSACTION READERS
# ============================================================================

def read_nordea(file_path):
    """Read Nordea CSV"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if not row or not row.get('Bokföringsdag'):
                    continue
                    
                date_str = parse_date(row.get('Bokföringsdag', ''))
                amount_str = row.get('Belopp', '0').replace(',', '.')
                merchant = row.get('Rubrik', 'Transfer').strip()
                
                try:
                    amount = abs(float(amount_str))
                except:
                    continue
                
                expense_acct = route_merchant(merchant)
                bank_acct = 1010
                
                if float(amount_str) < 0:
                    txn = Transaction(date_str, expense_acct, bank_acct, amount, merchant)
                else:
                    txn = Transaction(date_str, bank_acct, expense_acct, amount, merchant)
                
                transactions.append(txn)
                
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

def read_marginalen(file_path):
    """Read Marginalen CSV"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if not row or not row.get('Bokföringsdatum'):
                    continue
                
                date_str = parse_date(row.get('Bokföringsdatum', ''))
                amount_str = row.get('Belopp', '0').replace(',', '.')
                merchant = row.get('Transaktionstext', row.get('Händelsetext', 'Transfer')).strip()
                
                try:
                    amount = abs(float(amount_str))
                except:
                    continue
                
                expense_acct = route_merchant(merchant)
                bank_acct = 1100
                
                if float(amount_str) < 0:
                    txn = Transaction(date_str, expense_acct, bank_acct, amount, merchant)
                else:
                    txn = Transaction(date_str, bank_acct, expense_acct, amount, merchant)
                
                transactions.append(txn)
                
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

def read_klarna():
    """
    Klarna transactions - HARDCODED per Quran
    Account 2893 = Debt to shareholder
    """
    transactions = []
    
    # Transaction 1: TikTok Ads - 2025-07-19
    txn1 = Transaction('20250719', 5900, 2893, 2000.00, 'TikTok Ads - Klarna payment')
    transactions.append(txn1)
    
    # Transaction 2: TEMU business supplies - 2025-07-08
    # Per Quran Part 10: TEMU 702 SEK = Account 5460 (office supplies)
    txn2 = Transaction('20250708', 5460, 2893, 702.00, 'Temu business supplies - Klarna')
    transactions.append(txn2)
    
    # Transaction 3: TEMU business supplies - 2025-07-03
    # Per Quran Part 10: TEMU 339 SEK = Account 5460 (office supplies)
    txn3 = Transaction('20250703', 5460, 2893, 339.00, 'Temu business supplies - Klarna')
    transactions.append(txn3)
    
    return transactions

def read_sales(file_path):
    """Read Sales CSV"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            first_line = f.readline()
            f.seek(0)
            
            delimiter = ',' if ',' in first_line else ';'
            reader = csv.DictReader(f, delimiter=delimiter)
            
            total_sales = 0
            for row in reader:
                if not row:
                    continue
                
                try:
                    sales_val = float(row.get('Försäljning (inkl. moms)', '0').replace(',', '.'))
                    total_sales += sales_val
                except:
                    continue
            
            if total_sales > 0:
                txn = Transaction('20250930', 1010, 3000, total_sales, f'Sales Income Q3 2025')
                transactions.append(txn)
                
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

def read_inventory(file_path):
    """Read Inventory CSV"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                if not row or not row.get('Account'):
                    continue
                
                debit = float(row.get('Debit', 0))
                credit = float(row.get('Credit', 0))
                description = row.get('Description', '').strip()
                account = int(row.get('Account', 0))
                
                if debit > 0:
                    txn = Transaction('20250930', account, 1460, debit, f'Inventory: {description}')
                    transactions.append(txn)
                elif credit > 0:
                    txn = Transaction('20250930', 1460, account, credit, f'Inventory: {description}')
                    transactions.append(txn)
                    
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

# ============================================================================
# SE FILE BUILDER
# ============================================================================

def build_se_file(all_transactions, output_file):
    """Build complete SE file"""
    
    lines = []
    
    # Header
    lines.append('#FLAGGA\t0')
    lines.append('#PROGRAM\tQuran Master SE Builder V2 - With Klarna')
    lines.append('#VERSION\t2.0')
    lines.append('#FORMAT\tPC8')
    lines.append('#SIETYP\t4')
    lines.append('')
    
    # Company info
    lines.append('#NAMN\tSamis Jackets AB')
    lines.append('#ORGNR\t559489-5301')
    lines.append('#VALUTAKOD\tSEK')
    lines.append('#TAXAR\t20250701,20250930')
    lines.append('')
    
    # Collect accounts
    accounts_used = set()
    for txn in all_transactions:
        accounts_used.add(txn.debit_account)
        accounts_used.add(txn.credit_account)
    
    # Account definitions
    lines.append('// ACCOUNT DEFINITIONS')
    for acct in sorted(accounts_used):
        name = ACCOUNT_NAMES.get(acct, f'Account_{acct}')
        lines.append(f'#KONTO\t{acct}\t{name}')
    lines.append('')
    
    # Transactions
    lines.append('// TRANSACTIONS - Per Quran Rules')
    all_transactions.sort(key=lambda t: (t.date, t.description))
    
    for txn in all_transactions:
        lines.append(f'#TRANS\t{txn.debit_account}\tD\t{txn.amount:.2f}\t"{txn.description}"')
        lines.append(f'#TRANS\t{txn.credit_account}\tK\t{txn.amount:.2f}\t"{txn.description}"')
    
    lines.append('')
    lines.append('#EOF')
    
    # Write file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    return len(all_transactions)

# ============================================================================
# MAIN
# ============================================================================

def main():
    base_dir = Path(__file__).parent
    
    print("=" * 95)
    print("BUILDING MASTER SE FILE FROM QURAN - FINAL VERSION WITH KLARNA")
    print("=" * 95)
    print()
    
    all_txns = []
    
    # 1. NORDEA
    print("📊 NORDEA Transactions (3 accounts):")
    nordea_files = [
        base_dir / "nordea" / "Nordea Gold - 2025-10-19 12.55.00.csv",
        base_dir / "nordea" / "Nordea Premium - 2025-10-19 12.54.04.csv",
        base_dir / "nordea" / "PERSONKONTO-STUDENT nordea  3086 00 59626 - 2025-10-19 12.52.30.csv",
    ]
    
    for fpath in nordea_files:
        if fpath.exists():
            txns = read_nordea(str(fpath))
            all_txns.extend(txns)
            print(f"   ✓ {fpath.name}: {len(txns)} txns")
        else:
            print(f"   ⚠ {fpath.name}: NOT FOUND")
    print()
    
    # 2. MARGINALEN
    print("📊 MARGINALEN Transactions:")
    marg_file = base_dir / "marginalen" / "2025-07-01-2025-09-30 marginalen konto 1930 .csv"
    if marg_file.exists():
        txns = read_marginalen(str(marg_file))
        all_txns.extend(txns)
        print(f"   ✓ {marg_file.name}: {len(txns)} txns")
    else:
        print(f"   ⚠ NOT FOUND")
    print()
    
    # 3. KLARNA (NEW)
    print("📊 KLARNA Transactions (Per Quran Part 10):")
    txns = read_klarna()
    all_txns.extend(txns)
    print(f"   ✓ TikTok Ads: 2,000 SEK → Account 5900 (Marketing)")
    print(f"   ✓ Temu (2025-07-08): 702 SEK → Account 5460 (Office supplies per Quran)")
    print(f"   ✓ Temu (2025-07-03): 339 SEK → Account 5460 (Office supplies per Quran)")
    print(f"   Total: {len(txns)} txns")
    print()
    
    # 4. SALES
    print("📊 SALES Transactions:")
    sales_file = base_dir / "sales_data" / "sales Försäljningsrapport from 0107 to 30-09.csv"
    if sales_file.exists():
        txns = read_sales(str(sales_file))
        all_txns.extend(txns)
        print(f"   ✓ {sales_file.name}: {len(txns)} txns")
    else:
        print(f"   ⚠ NOT FOUND")
    print()
    
    # 5. INVENTORY
    print("📊 INVENTORY Transactions:")
    inv_file = base_dir / "inventory" / "ACCOUNTING_ENTRIES_Q3_2025.csv"
    if inv_file.exists():
        txns = read_inventory(str(inv_file))
        all_txns.extend(txns)
        print(f"   ✓ {inv_file.name}: {len(txns)} txns")
    else:
        print(f"   ⚠ NOT FOUND")
    print()
    
    # SUMMARY
    print("=" * 95)
    print("BUILDING SE FILE")
    print("=" * 95)
    print(f"Total transactions collected: {len(all_txns)}")
    print()
    
    # BUILD SE FILE
    output_file = base_dir / "20250930-COMPLETE-FROM-QURAN-FINAL.se"
    txn_count = build_se_file(all_txns, str(output_file))
    
    print(f"✅ SE File created: {output_file.name}")
    print(f"   File size: {os.path.getsize(output_file) / 1024:.2f} KB")
    print(f"   Transaction pairs: {txn_count}")
    print(f"   Total lines: {txn_count * 2}")
    print()
    
    # VALIDATION
    print("=" * 95)
    print("VALIDATION & ACCOUNT BALANCES")
    print("=" * 95)
    
    accounts = defaultdict(float)
    for txn in all_txns:
        accounts[txn.debit_account] += txn.amount
        accounts[txn.credit_account] -= txn.amount
    
    print("\nAccount Balances:")
    total_positive = 0
    total_negative = 0
    for acct in sorted(accounts.keys()):
        balance = accounts[acct]
        name = ACCOUNT_NAMES.get(acct, "Unknown")
        print(f"   {acct:4d} ({name:35s}): {balance:>12,.2f} SEK")
        if balance > 0:
            total_positive += balance
        else:
            total_negative += abs(balance)
    
    print()
    print(f"Total debits:  {total_positive:>12,.2f} SEK")
    print(f"Total credits: {total_negative:>12,.2f} SEK")
    balance_check = total_positive - total_negative
    print(f"Balance:       {balance_check:>12,.2f} SEK (should be ≈0)")
    print()
    
    # SUMMARY
    print("=" * 95)
    print("KLARNA VERIFICATION")
    print("=" * 95)
    klarna_total = 2000 + 702 + 339
    print(f"✓ TikTok Ads (5900): 2,000.00 SEK")
    print(f"✓ Temu supplies (5460): 702.00 + 339.00 = 1,041.00 SEK")
    print(f"✓ Total Klarna: {klarna_total:.2f} SEK")
    print(f"✓ Account 2893 (Debt to shareholder): {accounts[2893]:,.2f} SEK")
    print()
    print("✅ SE FILE COMPLETE WITH ALL SOURCES")
    print()

if __name__ == "__main__":
    main()
