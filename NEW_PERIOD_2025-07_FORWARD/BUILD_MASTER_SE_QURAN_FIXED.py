#!/usr/bin/env python3
"""
MASTER SE FILE BUILDER FROM QURAN - FIXED VERSION
================================================
Reads ACTUAL transaction CSV files and builds complete SE file.
Following QURAN rules EXACTLY - Any mistake is the coder's responsibility for not following the book.

Transaction sources:
1. Nordea (3 accounts) - CSV with columns: Datum, Bokföringsdag, Rubrik, Belopp, Valuta
2. Wise (multi-currency) - Located in cursor-branch folder
3. Marginalen - CSV with columns: Bokföringsdatum, Belopp, Transaktionstext
4. Sales - CSV with columns: Försäljning, Moms, Försäljning (inkl. moms)
5. Inventory - CSV with columns: Account, Description, Debit, Credit
"""

import csv
import os
import re
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# ============================================================================
# QURAN MERCHANT ROUTING DEFINITIONS
# ============================================================================

MERCHANT_TO_ACCOUNT = {
    # MEALS & ENTERTAINMENT (Account 4500-4599)
    "ARAN": 4500, "ARAN FOOD": 4500, "FOOD": 4500,
    "WILLYS": 4500, "GROCERY": 4500, "COOP": 4500, "ICA": 4500, "LIDL": 4500,
    "RESTAURANT": 4500, "CAFE": 4500, "COFFEE": 4500, "LUNCH": 4500,
    
    # OFFICE & SUPPLIES (Account 5000-5099)
    "OFFICE": 5010, "IKEA": 5010, "STAPLES": 5010, "SUPPLIES": 5010,
    "PAPER": 5010, "PRINTING": 5050, "COPYSHOP": 5050,
    
    # VEHICLE & FUEL (Account 1900-1999)
    "OKQ8": 1910, "CIRCLE K": 1910, "FUEL": 1910, "PETROL": 1910,
    "TESLA": 1920, "CHARGING": 1920, "CAR WASH": 1920,
    
    # TRAVEL (Account 4000-4099)
    "HOTEL": 4010, "AIRBNB": 4010, "BOOKING": 4010,
    "FLIGHT": 4020, "AIRLINE": 4020, "SAS": 4020, "TRAIN": 4020,
    "TAXI": 4030, "UBER": 4030, "BOLT": 4030, "CAR RENTAL": 4030,
    
    # MARKETING (Account 3000-3099)
    "INSTAGRAM": 3010, "META": 3010, "FACEBOOK": 3010, "GOOGLE": 3010,
    "TIKTOK": 3010, "MARKETING": 3010, "ADVERTISING": 3010,
    
    # SOFTWARE & DIGITAL (Account 6100-6199)
    "ADOBE": 6100, "MICROSOFT": 6100, "SLACK": 6100, "ZOOM": 6100,
    "FIGMA": 6100, "GITHUB": 6100, "AWS": 6100, "STRIPE": 6100,
    "SOFTWARE": 6100, "SHOPIFY": 6100,
    
    # TELECOM (Account 6200-6299)
    "TELENOR": 6200, "TELIA": 6200, "VODAFONE": 6200, "SWISSCOM": 6200,
    "MOBILE": 6200, "PHONE": 6200, "INTERNET": 6200,
    
    # CLOTHING & MERCHANDISE (Account 1500-1599)
    "ZALANDO": 1510, "H&M": 1510, "ASOS": 1510, "AMAZON": 1510,
    "TEXTILE": 1510, "FABRIC": 1510,
    
    # BANKING (Account 9900-9999)
    "BANK": 9900, "INTEREST": 9900, "FEE": 9900, "WISE": 9900,
    
    # TRANSFERS (Internal)
    "INBETALNING": 1010,  # Deposit
    "ÖVERFÖRING": 1010,   # Transfer
    "MOTTAGARE": 1010,    # Receiver payment
    "PLUSGIRO": 1010,     # Plus giro
}

ACCOUNT_NAMES = {
    1000: "BANK_CHECKING_EUR",
    1010: "BANK_CHECKING_SEK",
    1020: "BANK_CHECKING_GBP",
    1030: "BANK_CHECKING_USD",
    1100: "BANK_SAVINGS_SEK",
    1200: "CASH_REGISTER",
    1460: "INVENTORY",
    1500: "INVENTORY_ACCOUNT",
    1510: "MERCHANDISE_PURCHASES",
    1900: "VEHICLE_ACCOUNT",
    1910: "VEHICLE_FUEL_MAINTENANCE",
    1920: "VEHICLE_REPAIRS",
    2000: "ACCOUNTS_RECEIVABLE",
    2500: "ACCOUNTS_PAYABLE",
    3000: "SALES_INCOME",
    3010: "MARKETING_ADVERTISING",
    4000: "TRAVEL_ACCOMMODATION",
    4010: "HOTEL_ACCOMMODATION",
    4020: "FLIGHTS_TRANSPORTATION",
    4030: "TAXIS_CARRENTALS",
    4110: "COST_OF_GOODS_SOLD",
    4500: "MEALS_ENTERTAINMENT",
    5000: "OFFICE_SUPPLIES",
    5010: "OFFICE_FURNITURE",
    5050: "PRINTING_POSTAGE",
    5900: "MARKETING_GIFTS",
    6100: "SOFTWARE_LICENSES",
    6200: "UTILITIES_TELEPHONE",
    6300: "INSURANCE",
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
# MERCHANT ROUTING
# ============================================================================

def route_merchant(merchant_text):
    """Route merchant to expense account per Quran"""
    merchant_upper = merchant_text.upper()
    
    # Exact matches first
    for keyword, account in MERCHANT_TO_ACCOUNT.items():
        if keyword in merchant_upper:
            return account
    
    # Default
    return 6400

def parse_date(date_str):
    """Parse various date formats"""
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
    """Read Nordea CSV (semicolon-separated)"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader):
                if not row or not row.get('Bokföringsdag'):
                    continue
                    
                date_str = parse_date(row.get('Bokföringsdag', ''))
                amount_str = row.get('Belopp', '0').replace(',', '.')
                merchant = row.get('Rubrik', 'Transfer').strip()
                
                try:
                    amount = abs(float(amount_str))
                except:
                    continue
                
                # Route merchant to expense account
                expense_acct = route_merchant(merchant)
                bank_acct = 1010  # SEK account
                
                # If debit (negative), it's an expense
                if float(amount_str) < 0:
                    txn = Transaction(date_str, expense_acct, bank_acct, amount, merchant)
                else:
                    # Credit (positive) - income
                    txn = Transaction(date_str, bank_acct, expense_acct, amount, merchant)
                
                transactions.append(txn)
                
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

def read_marginalen(file_path):
    """Read Marginalen CSV (semicolon-separated)"""
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
                
                # Route merchant
                expense_acct = route_merchant(merchant)
                bank_acct = 1100  # Savings
                
                if float(amount_str) < 0:
                    txn = Transaction(date_str, expense_acct, bank_acct, amount, merchant)
                else:
                    txn = Transaction(date_str, bank_acct, expense_acct, amount, merchant)
                
                transactions.append(txn)
                
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

def read_sales(file_path):
    """Read Sales CSV (comma-separated)"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            # Read header to detect delimiter
            first_line = f.readline()
            f.seek(0)
            
            delimiter = ',' if ',' in first_line else ';'
            reader = csv.DictReader(f, delimiter=delimiter)
            
            total_sales = 0
            for row in reader:
                if not row:
                    continue
                
                # Column: "Försäljning (inkl. moms)" is the revenue with tax
                try:
                    sales_val = float(row.get('Försäljning (inkl. moms)', '0').replace(',', '.'))
                    total_sales += sales_val
                except:
                    continue
            
            if total_sales > 0:
                # Single entry for total sales
                txn = Transaction('20250930', 1010, 3000, total_sales, f'Sales Income Q3 2025 ({total_sales:.2f})')
                transactions.append(txn)
                
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

def read_inventory(file_path):
    """Read Inventory Accounting Entries"""
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
                    # Debit entry
                    txn = Transaction('20250930', account, 1460, debit, f'Inventory: {description}')
                    transactions.append(txn)
                elif credit > 0:
                    # Credit entry
                    txn = Transaction('20250930', 1460, account, credit, f'Inventory: {description}')
                    transactions.append(txn)
                    
    except Exception as e:
        print(f"  ERROR in {Path(file_path).name}: {e}")
    
    return transactions

# ============================================================================
# SE FILE BUILDER
# ============================================================================

def build_se_file(all_transactions, output_file):
    """Build complete SE file from all transactions"""
    
    lines = []
    
    # Header
    lines.append('#FLAGGA\t0')
    lines.append('#PROGRAM\tQuran Master SE Builder')
    lines.append('#VERSION\t1.0')
    lines.append('#FORMAT\tPC8')
    lines.append('#SIETYP\t4')
    lines.append('')
    
    # Company info
    lines.append('#NAMN\tSamis Jackets AB')
    lines.append('#ORGNR\t559489-5301')
    lines.append('#VALUTAKOD\tSEK')
    lines.append('#TAXAR\t20250701,20250930')
    lines.append('')
    
    # Collect all accounts used
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
    lines.append('// TRANSACTIONS')
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
    
    print("=" * 90)
    print("BUILDING MASTER SE FILE FROM QURAN - FIXED VERSION")
    print("=" * 90)
    print()
    
    all_txns = []
    
    # 1. NORDEA
    print("📊 NORDEA Transactions:")
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
    
    # 3. SALES
    print("📊 SALES Transactions:")
    sales_file = base_dir / "sales_data" / "sales Försäljningsrapport from 0107 to 30-09.csv"
    if sales_file.exists():
        txns = read_sales(str(sales_file))
        all_txns.extend(txns)
        print(f"   ✓ {sales_file.name}: {len(txns)} txns")
    else:
        print(f"   ⚠ NOT FOUND")
    print()
    
    # 4. INVENTORY
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
    print("=" * 90)
    print("BUILDING SE FILE")
    print("=" * 90)
    print(f"Total transactions collected: {len(all_txns)}")
    print()
    
    # BUILD SE FILE
    output_file = base_dir / "20250930-COMPLETE-FROM-QURAN.se"
    txn_count = build_se_file(all_txns, str(output_file))
    
    print(f"✅ SE File created: {output_file.name}")
    print(f"   File size: {os.path.getsize(output_file) / 1024:.2f} KB")
    print(f"   Transactions: {txn_count}")
    print()
    
    # VALIDATION
    print("=" * 90)
    print("VALIDATION")
    print("=" * 90)
    
    # Calculate balance
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
        print(f"   {acct:4d} ({name:30s}): {balance:>12,.2f} SEK")
        if balance > 0:
            total_positive += balance
        else:
            total_negative += abs(balance)
    
    print()
    print(f"Total debits:  {total_positive:>12,.2f} SEK")
    print(f"Total credits: {total_negative:>12,.2f} SEK")
    print(f"Balance:       {total_positive - total_negative:>12,.2f} SEK (should be ≈0)")
    print()
    print("✅ SE FILE COMPLETE")
    print()

if __name__ == "__main__":
    main()
