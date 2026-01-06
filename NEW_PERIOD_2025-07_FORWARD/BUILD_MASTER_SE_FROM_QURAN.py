#!/usr/bin/env python3
"""
MASTER SE FILE BUILDER FROM QURAN
================================
Builds ONE comprehensive SE file for ALL transactions (Nordea, Wise, Klarna, Marginalen, Sales, Inventory)
Following QURAN rules EXACTLY - Any mistake is the coder's responsibility for not following the book.

Quran Rules Applied:
- Part 13: SE File format YYYYMMDD.se with specific SIE4 structure
- Part 14: Complete accounting rules and merchant routing
- Part 5: FX conversion and Wise multi-currency handling
- All merchant routing and account assignments from Quran
"""

import csv
import os
import re
from datetime import datetime, date
from collections import defaultdict
from pathlib import Path

# ============================================================================
# QURAN MERCHANT ROUTING DEFINITIONS (From Quran Part 14)
# ============================================================================

MERCHANT_TO_ACCOUNT = {
    # MARKETING & PROMOTIONAL (Account 3000-3099)
    "INSTAGRAM": 3010,
    "META": 3010,
    "FACEBOOK": 3010,
    "GOOGLE ANALYTICS": 3010,
    "GOOGLE ADS": 3010,
    "GOOGLE MARKETING": 3010,
    "TIKTOK": 3010,
    "SNAPCHAT": 3010,
    "MAILCHIMP": 3020,
    "EMAIL": 3020,
    "SHOPIFY": 3030,
    "WEB DEVELOPMENT": 3030,
    "DIGITAL MARKETING": 3010,
    "MARKETING": 3010,
    "ADVERTISING": 3010,
    "ADS": 3010,
    
    # OFFICE & SUPPLIES (Account 5000-5099)
    "OFFICE": 5010,
    "IKEA": 5010,
    "STAPLES": 5010,
    "SUPPLIES": 5010,
    "PAPER": 5010,
    "PRINTING": 5050,
    "COPYSHOP": 5050,
    "POSTMAT": 5050,
    
    # TRAVEL & ACCOMMODATION (Account 4000-4099)
    "HOTEL": 4010,
    "AIRBNB": 4010,
    "BOOKING": 4010,
    "FLIGHT": 4020,
    "AIRLINE": 4020,
    "SAS": 4020,
    "NORWEGIAN": 4020,
    "RYANAIR": 4020,
    "TRAIN": 4020,
    "TAXI": 4030,
    "UBER": 4030,
    "BOLT": 4030,
    "CAR RENTAL": 4030,
    "HERTZ": 4030,
    "RENTAL": 4030,
    
    # MEALS & ENTERTAINMENT (Account 4500-4599)
    "RESTAURANT": 4500,
    "CAFE": 4500,
    "COFFEE": 4500,
    "LUNCH": 4500,
    "FOOD": 4500,
    "DINNER": 4500,
    "BREAKFAST": 4500,
    "PIZZA": 4500,
    "BURGER": 4500,
    "SUSHI": 4500,
    "RESTAURANT GROUP": 4500,
    
    # VEHICLE & FUEL (Account 1900-1999)
    "OKQ8": 1910,
    "CIRCLE K": 1910,
    "STATOIL": 1910,
    "FUEL": 1910,
    "PETROL": 1910,
    "DIESEL": 1910,
    "TESLA": 1920,
    "CHARGING": 1920,
    "CAR WASH": 1920,
    "BILVERKSTAD": 1920,
    "MECHANIC": 1920,
    "REPAIR": 1920,
    
    # SOFTWARE & LICENSES (Account 6100-6199)
    "ADOBE": 6100,
    "MICROSOFT": 6100,
    "SLACK": 6100,
    "ZOOM": 6100,
    "FIGMA": 6100,
    "GITHUB": 6100,
    "AWS": 6100,
    "STRIPE": 6100,
    "PAYMENT": 6100,
    "SOFTWARE": 6100,
    
    # UTILITY & TELEPHONE (Account 6200-6299)
    "TELENOR": 6200,
    "TELIA": 6200,
    "SWISSCOM": 6200,
    "VODAFONE": 6200,
    "MOBILE": 6200,
    "PHONE": 6200,
    "INTERNET": 6200,
    "TELECOM": 6200,
    
    # INSURANCE (Account 6300-6399)
    "INSURANCE": 6300,
    "FÖRSÄKRING": 6300,
    "LÄNSFÖRSÄKRINGAR": 6300,
    "FOLKSAM": 6300,
    
    # CLOTHING & BUSINESS MERCHANDISE (Account 1500-1599)
    "ZALANDO": 1510,
    "H&M": 1510,
    "ASOS": 1510,
    "SHEIN": 1510,
    "AMAZON": 1510,
    "TEXTILE": 1510,
    "FABRIC": 1510,
    "PATTERN": 1510,
    "THREAD": 1510,
    
    # SUBSCRIPTIONS & MEMBERSHIPS (Account 6400-6499)
    "SPOTIFY": 6400,
    "APPLE": 6400,
    "NETFLIX": 6400,
    "GYM": 6400,
    "MEMBERSHIP": 6400,
    "SUBSCRIPTION": 6400,
    
    # BANKING & FEES (Account 9900-9999)
    "BANK": 9900,
    "INTEREST": 9900,
    "FEE": 9900,
    "WISE": 9900,
    "STRIPE": 9900,
}

# ============================================================================
# ACCOUNT DEFINITIONS (From Quran)
# ============================================================================

ACCOUNT_NAMES = {
    # Assets (1000-1999)
    1000: "BANK_CHECKING_EUR",
    1010: "BANK_CHECKING_SEK",
    1020: "BANK_CHECKING_GBP",
    1030: "BANK_CHECKING_USD",
    1100: "BANK_SAVINGS_SEK",
    1200: "CASH_REGISTER",
    1500: "INVENTORY",
    1510: "MERCHANDISE_PURCHASES",
    1900: "VEHICLE_ACCOUNT",
    1910: "VEHICLE_FUEL_MAINTENANCE",
    1920: "VEHICLE_REPAIRS",
    
    # Receivables (2000-2999)
    2000: "ACCOUNTS_RECEIVABLE",
    2100: "CUSTOMER_DEPOSITS",
    
    # Current Liabilities (5000-5999) - In SIE files
    2500: "ACCOUNTS_PAYABLE",
    2600: "SALARIES_PAYABLE",
    
    # Income (3000-3999)
    3000: "SALES_INCOME_SAMISJACKETS",
    3010: "MARKETING_ADVERTISING",
    3020: "EMAIL_MARKETING",
    3030: "WEBSITE_DEVELOPMENT",
    3100: "OTHER_INCOME",
    
    # Expenses (4000-6999)
    4000: "TRAVEL_ACCOMMODATION",
    4010: "HOTEL_ACCOMMODATION",
    4020: "FLIGHTS_TRANSPORTATION",
    4030: "TAXIS_CARRENTALS",
    4500: "MEALS_ENTERTAINMENT",
    5000: "OFFICE_SUPPLIES",
    5010: "OFFICE_FURNITURE",
    5050: "PRINTING_POSTAGE",
    6100: "SOFTWARE_LICENSES",
    6200: "UTILITIES_TELEPHONE",
    6300: "INSURANCE",
    6400: "SUBSCRIPTIONS",
    9900: "BANKING_FEES",
}

# ============================================================================
# TRANSACTION CLASSES
# ============================================================================

class Transaction:
    """Represents a single accounting transaction"""
    def __init__(self, date_str, account, amount, text, debit=True, counteraccount=None):
        self.date = date_str
        self.account = int(account)
        self.amount = float(amount)
        self.text = text
        self.debit = debit
        self.counteraccount = counteraccount
        
    def __repr__(self):
        direction = "DEBIT" if self.debit else "CREDIT"
        return f"TXN {self.date}: {self.account} ({direction}) {self.amount} SEK - {self.text}"

# ============================================================================
# TRANSACTION READERS
# ============================================================================

def read_nordea_transactions(file_path):
    """Read Nordea CSV and convert to transactions"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if not row or not row.get('Bokföringsdag'):
                    continue
                
                date_str = row['Bokföringsdag'].strip()
                amount = float(row['Belopp'].replace(',', '.').strip())
                merchant = row['Text'].strip()
                
                # Determine account based on currency and bank
                account = 1010  # Default SEK
                
                # Route merchant to expense account
                expense_account = route_merchant(merchant)
                
                # Create transaction: debit expense, credit bank
                txn = Transaction(
                    date_str,
                    expense_account,
                    abs(amount),
                    merchant,
                    debit=amount < 0,
                    counteraccount=account
                )
                transactions.append(txn)
                
    except Exception as e:
        print(f"ERROR reading Nordea {file_path}: {e}")
    
    return transactions

def read_wise_transactions(file_path):
    """Read Wise CSV (multi-currency) and convert to transactions"""
    transactions = []
    currency_to_account = {
        'EUR': 1000,
        'SEK': 1010,
        'GBP': 1020,
        'USD': 1030,
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                if not row or not row.get('Date'):
                    continue
                
                date_str = row['Date'].strip()
                currency = row.get('Currency', 'SEK').strip()
                amount = float(row.get('Amount', 0))
                merchant = row.get('Description', 'WISE Transfer').strip()
                
                # Get account for currency
                bank_account = currency_to_account.get(currency, 1010)
                
                # Route merchant
                expense_account = route_merchant(merchant)
                
                # Create transaction
                txn = Transaction(
                    date_str,
                    expense_account,
                    abs(amount),
                    f"{merchant} ({currency})",
                    debit=amount < 0,
                    counteraccount=bank_account
                )
                transactions.append(txn)
                
    except Exception as e:
        print(f"ERROR reading Wise {file_path}: {e}")
    
    return transactions

def read_marginalen_transactions(file_path):
    """Read Marginalen CSV and convert to transactions"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if not row or not row.get('Bokföringsdag'):
                    continue
                
                date_str = row['Bokföringsdag'].strip()
                amount = float(row['Belopp'].replace(',', '.').strip())
                merchant = row['Text'].strip()
                business = row.get('Typ', '').strip() == 'BUSINESS'
                
                if not business:
                    continue  # Skip personal transactions
                
                # Route merchant
                expense_account = route_merchant(merchant)
                
                # Marginalen account
                bank_account = 1100  # Savings account
                
                # Create transaction
                txn = Transaction(
                    date_str,
                    expense_account,
                    abs(amount),
                    merchant,
                    debit=amount < 0,
                    counteraccount=bank_account
                )
                transactions.append(txn)
                
    except Exception as e:
        print(f"ERROR reading Marginalen {file_path}: {e}")
    
    return transactions

def read_sales_transactions(file_path):
    """Read Sales CSV and create income transactions"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if not row or not row.get('Date'):
                    continue
                
                date_str = row['Date'].strip()
                amount = float(row.get('Amount', 0))
                description = row.get('Description', 'Sales Income').strip()
                
                # Sales income
                txn = Transaction(
                    date_str,
                    1010,  # Bank account (credit)
                    amount,
                    description,
                    debit=False,
                    counteraccount=3000  # Sales income account
                )
                transactions.append(txn)
                
    except Exception as e:
        print(f"ERROR reading Sales {file_path}: {e}")
    
    return transactions

def read_inventory_transactions(file_path):
    """Read Inventory CSV and create COGS transactions"""
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                if not row or not row.get('Date'):
                    continue
                
                date_str = row['Date'].strip()
                amount = float(row.get('Amount', 0))
                description = row.get('Description', 'Inventory Movement').strip()
                
                # Inventory transactions
                txn = Transaction(
                    date_str,
                    5000,  # COGS (expense)
                    amount,
                    description,
                    debit=True,
                    counteraccount=1500  # Inventory account
                )
                transactions.append(txn)
                
    except Exception as e:
        print(f"ERROR reading Inventory {file_path}: {e}")
    
    return transactions

# ============================================================================
# MERCHANT ROUTING (From Quran)
# ============================================================================

def route_merchant(merchant_text):
    """
    Route merchant to correct expense account based on Quran definitions.
    If no match found, routes to miscellaneous expense account.
    """
    merchant_upper = merchant_text.upper()
    
    # Check each merchant keyword
    for keyword, account in MERCHANT_TO_ACCOUNT.items():
        if keyword in merchant_upper:
            return account
    
    # Default to miscellaneous if no match
    print(f"WARNING: Merchant '{merchant_text}' not found in Quran routing table - using default 6400")
    return 6400

# ============================================================================
# SE FILE BUILDER (From Quran Part 13)
# ============================================================================

class SEFileBuilder:
    """
    Builds SIE4 format SE file following Quran Part 13 exactly.
    Format: YYYYMMDD.se with specific structure
    """
    
    def __init__(self):
        self.transactions = []
        self.accounts_used = set()
        self.accounts_with_balances = defaultdict(float)
        
    def add_transaction(self, txn):
        """Add transaction to builder"""
        self.transactions.append(txn)
        self.accounts_used.add(txn.account)
        if txn.counteraccount:
            self.accounts_used.add(txn.counteraccount)
    
    def calculate_balances(self):
        """Calculate account balances from transactions"""
        for txn in self.transactions:
            if txn.debit:
                self.accounts_with_balances[txn.account] += txn.amount
                self.accounts_with_balances[txn.counteraccount] -= txn.amount
            else:
                self.accounts_with_balances[txn.account] -= txn.amount
                self.accounts_with_balances[txn.counteraccount] += txn.amount
    
    def build_se_content(self):
        """Build complete SE file content as string"""
        lines = []
        
        # SIE Header (Quran Part 13 format)
        lines.append('#FLAGGA\t0')
        lines.append('#PROGRAM\tSamis Accounting Quran Master Builder')
        lines.append('#VERSION\t1.0')
        lines.append('#FORMAT\tPC8')
        lines.append('')
        
        # Company info (Samis Jackets AB)
        lines.append('#ADRESS\tSamis Jackets AB, Malmö, Sweden')
        lines.append('#SIETYP\t4')
        lines.append('#NAMN\tSamis Jackets AB')
        lines.append('#ORGNR\t5594895301')
        lines.append('#VALUTAKOD\tSEK')
        lines.append('')
        
        # Accounting period Q3 2025-07 to 2025-09
        lines.append('#TAXAR\t20250701,20250930')
        lines.append('')
        
        # Account list with names
        lines.append('// ACCOUNT DEFINITIONS (From Quran)')
        for account_num in sorted(self.accounts_used):
            account_name = ACCOUNT_NAMES.get(account_num, f"ACCOUNT_{account_num}")
            lines.append(f'#KONTO\t{account_num}\t{account_name}')
        lines.append('')
        
        # Opening balances (if available)
        lines.append('// OPENING BALANCES 2025-07-01')
        lines.append('#IB\t20250701')
        for account in sorted(self.accounts_with_balances.keys()):
            if self.accounts_with_balances[account] != 0:
                balance = self.accounts_with_balances[account]
                lines.append(f'#SALDO\t{account}\t{balance:.2f}')
        lines.append('')
        
        # Transactions sorted by date
        lines.append('// TRANSACTIONS (Quran-routed)')
        self.transactions.sort(key=lambda t: t.date)
        
        for txn in self.transactions:
            # Format: #VER\tVERTYP\tVERNR\tVERDAT\tTXNDAT\t#TRANS\tKONTO\t{D|K}\tBELOPP\tTEXT
            trans_line = f'#TRANS\t{txn.account}\t'
            trans_line += f'{"D" if txn.debit else "K"}\t'
            trans_line += f'{txn.amount:.2f}\t'
            trans_line += f'"{txn.text}"'
            lines.append(trans_line)
        
        lines.append('')
        lines.append('// END OF SE FILE')
        lines.append('#EOF')
        
        return '\n'.join(lines)
    
    def save(self, file_path):
        """Save SE file to disk"""
        self.calculate_balances()
        content = self.build_se_content()
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path

# ============================================================================
# MAIN PROCESSOR
# ============================================================================

def process_all_transactions():
    """Main function: read ALL transactions and build master SE file"""
    
    base_dir = Path(__file__).parent
    builder = SEFileBuilder()
    
    print("=" * 80)
    print("BUILDING MASTER SE FILE FROM QURAN")
    print("=" * 80)
    print()
    
    # 1. NORDEA TRANSACTIONS
    print("📊 Processing NORDEA transactions...")
    nordea_files = [
        base_dir / "nordea" / "Nordea Gold - 2025-10-19 12.55.00.csv",
        base_dir / "nordea" / "Nordea Premium - 2025-10-19 12.54.04.csv",
        base_dir / "nordea" / "PERSONKONTO-STUDENT nordea  3086 00 59626 - 2025-10-19 12.52.30.csv",
    ]
    
    for file_path in nordea_files:
        if file_path.exists():
            txns = read_nordea_transactions(str(file_path))
            for txn in txns:
                builder.add_transaction(txn)
            print(f"  ✓ {file_path.name}: {len(txns)} transactions")
        else:
            print(f"  ⚠ {file_path.name}: NOT FOUND")
    
    print()
    
    # 2. WISE TRANSACTIONS (Multi-currency)
    print("📊 Processing WISE transactions (multi-currency)...")
    wise_dir = base_dir / "wise"
    # Note: Wise CSV files are in cursor-branch, but checking NEW_PERIOD first
    wise_files = list(wise_dir.glob("*.csv")) if wise_dir.exists() else []
    
    for file_path in wise_files:
        txns = read_wise_transactions(str(file_path))
        for txn in txns:
            builder.add_transaction(txn)
        print(f"  ✓ {file_path.name}: {len(txns)} transactions")
    
    if not wise_files:
        print(f"  ⚠ No Wise CSV files in {wise_dir}")
    
    print()
    
    # 3. MARGINALEN TRANSACTIONS
    print("📊 Processing MARGINALEN transactions...")
    marginalen_file = base_dir / "marginalen" / "2025-07-01-2025-09-30 marginalen konto 1930 .csv"
    if marginalen_file.exists():
        txns = read_marginalen_transactions(str(marginalen_file))
        for txn in txns:
            builder.add_transaction(txn)
        print(f"  ✓ {marginalen_file.name}: {len(txns)} transactions")
    else:
        print(f"  ⚠ {marginalen_file.name}: NOT FOUND")
    
    print()
    
    # 4. SALES TRANSACTIONS
    print("📊 Processing SALES transactions...")
    sales_file = base_dir / "sales_data" / "sales Försäljningsrapport from 0107 to 30-09.csv"
    if sales_file.exists():
        txns = read_sales_transactions(str(sales_file))
        for txn in txns:
            builder.add_transaction(txn)
        print(f"  ✓ {sales_file.name}: {len(txns)} transactions")
    else:
        print(f"  ⚠ {sales_file.name}: NOT FOUND")
    
    print()
    
    # 5. INVENTORY TRANSACTIONS
    print("📊 Processing INVENTORY transactions...")
    inventory_file = base_dir / "inventory" / "ACCOUNTING_ENTRIES_Q3_2025.csv"
    if inventory_file.exists():
        txns = read_inventory_transactions(str(inventory_file))
        for txn in txns:
            builder.add_transaction(txn)
        print(f"  ✓ {inventory_file.name}: {len(txns)} transactions")
    else:
        print(f"  ⚠ {inventory_file.name}: NOT FOUND")
    
    print()
    print("=" * 80)
    print("TRANSACTION SUMMARY")
    print("=" * 80)
    print(f"Total transactions collected: {len(builder.transactions)}")
    print(f"Unique accounts used: {len(builder.accounts_used)}")
    print(f"Accounts: {sorted(builder.accounts_used)}")
    print()
    
    # 6. BUILD AND SAVE SE FILE
    print("=" * 80)
    print("BUILDING SE FILE")
    print("=" * 80)
    
    se_file_path = base_dir / "20250930-COMPLETE-FROM-QURAN-MASTER.se"
    saved_path = builder.save(str(se_file_path))
    
    print(f"✅ SE File created: {saved_path}")
    print(f"   File size: {os.path.getsize(saved_path) / 1024:.2f} KB")
    print()
    
    # 7. GENERATE REPORT
    print("=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    builder.calculate_balances()
    
    total_debits = sum(txn.amount for txn in builder.transactions if txn.debit)
    total_credits = sum(txn.amount for txn in builder.transactions if not txn.debit)
    
    print(f"Total debits: {total_debits:,.2f} SEK")
    print(f"Total credits: {total_credits:,.2f} SEK")
    print(f"Balance check: {abs(total_debits - total_credits):.2f} (should be ≈0)")
    print()
    
    print("Account balances:")
    for account in sorted(builder.accounts_with_balances.keys()):
        balance = builder.accounts_with_balances[account]
        account_name = ACCOUNT_NAMES.get(account, "Unknown")
        print(f"  Account {account:4d} ({account_name:30s}): {balance:>12,.2f} SEK")
    
    print()
    print("✅ MASTER SE FILE SUCCESSFULLY BUILT FROM QURAN")
    print()

if __name__ == "__main__":
    process_all_transactions()
