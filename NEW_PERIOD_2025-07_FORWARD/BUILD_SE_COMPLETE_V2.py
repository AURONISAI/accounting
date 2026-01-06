#!/usr/bin/env python3
"""
SAMIS JACKETS AB - COMPLETE SE FILE BUILDER FROM QURAN v2
ENHANCED WITH COMPREHENSIVE MERCHANT ROUTING

PURPOSE: Process ALL transaction files following QURAN_COMPLETE_BOOK.md EXACTLY
         Any routing error is user's responsibility to update merchant mappings
         
REFERENCE: Quran Part 3 (Transaction Routing) + Part 13 (SE File Generation)
"""

import csv
import os
import sys
from datetime import datetime
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
import json

# ============================================================================
# COMPREHENSIVE MERCHANT DIRECTORY (from Quran Part 3 & 10)
# ============================================================================

MERCHANT_DIRECTORY = {
    # ========== SOFTWARE & SUBSCRIPTIONS (5200, VAT=YES) ==========
    'OPENAI': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'ANTHROPIC': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'GOOGLE': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'GOOGLE CLOUD': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'STRIPE': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'AWS': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'AZURE': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'GITHUB': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'BITBUCKET': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'DIGITALOCEAN': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'SLACK': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'JIRA': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'ASANA': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'MONDAY': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'NOTION': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'FIGMA': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'ADOBE': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'PHOTOSHOP': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'MAILCHIMP': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'ZAPIER': {'account': '5200', 'vat': 'YES', 'category': 'Software'},
    'ONE.COM': {'account': '5200', 'vat': 'YES', 'category': 'Software-Hosting'},
    
    # ========== MARKETING & ADVERTISING (5250, VAT=NO for digital) ==========
    'SHOPIFY': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'FACEBOOK': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'TIKTOK': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'INSTAGRAM': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'GOOGLE ADS': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'YOUTUBE': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'SNAPCHAT': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'PINTEREST': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'LINKEDIN': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'MAILERLITE': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'GETRESPONSE': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'CONVERTKIT': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'AWEBER': {'account': '5250', 'vat': 'NO', 'category': 'Marketing'},
    'IN & FINN AB': {'account': '5250', 'vat': 'YES', 'category': 'Marketing'},
    
    # ========== MEALS & FOOD (6992, VAT=NO, Personal/Non-deductible) ==========
    'WILLYS': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'ICA': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'COOP': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'ARAN FOOD': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'HALLON': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'ALMOUSLI': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'MISTER YORK': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'STORA COOP': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'PIZZA': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'RESTAURANG': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'KEBAB': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'SUSHI': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'DINER': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    'CAFÉ': {'account': '6992', 'vat': 'NO', 'category': 'Meals-Personal'},
    
    # ========== BANK & FINANCIAL (Various) ==========
    'RÖRLIG RÄNTA': {'account': '6570', 'vat': 'NO', 'category': 'Bank-Fee'},
    'BANKAVGIFT': {'account': '6570', 'vat': 'NO', 'category': 'Bank-Fee'},
    'BANK AVGIFT': {'account': '6570', 'vat': 'NO', 'category': 'Bank-Fee'},
    'GEBYR': {'account': '6570', 'vat': 'NO', 'category': 'Bank-Fee'},
    'INBETALNING': {'account': '1930', 'vat': 'NO', 'category': 'Bank-Deposit'},
    'ÖVERFÖRING': {'account': '1930', 'vat': 'NO', 'category': 'Bank-Transfer'},
    'CASHBACK': {'account': '3051', 'vat': 'NO', 'category': 'Bank-Cashback'},
    'RÄNTA': {'account': '3051', 'vat': 'NO', 'category': 'Bank-Interest'},
    
    # ========== COMPANY & PERSONAL (6992) ==========
    'G&S BY SAMIS': {'account': '6992', 'vat': 'NO', 'category': 'Company-Personal'},
    'SAMIS JACKETS': {'account': '6992', 'vat': 'NO', 'category': 'Company-Personal'},
    
    # ========== TRANSPORTATION & VEHICLES (5360) ==========
    'SJ': {'account': '5360', 'vat': 'NO', 'category': 'Travel'},
    'TAXI': {'account': '5360', 'vat': 'NO', 'category': 'Travel'},
    'UBER': {'account': '5360', 'vat': 'NO', 'category': 'Travel'},
    'TRAFIKVERKET': {'account': '5360', 'vat': 'NO', 'category': 'Travel'},
    'PARKERING': {'account': '5360', 'vat': 'NO', 'category': 'Travel'},
    'AIMO': {'account': '5360', 'vat': 'NO', 'category': 'Parking'},
    'BENSIN': {'account': '5360', 'vat': 'NO', 'category': 'Fuel'},
    'OLJA': {'account': '5360', 'vat': 'NO', 'category': 'Fuel'},
    'BILVERKSTAD': {'account': '5360', 'vat': 'YES', 'category': 'Repair'},
    
    # ========== UTILITIES & COMMUNICATIONS (5340, 5320) ==========
    'TELIA': {'account': '5340', 'vat': 'YES', 'category': 'Communications'},
    'TELENOR': {'account': '5340', 'vat': 'YES', 'category': 'Communications'},
    'VODAFONE': {'account': '5340', 'vat': 'YES', 'category': 'Communications'},
    'COMHEM': {'account': '5340', 'vat': 'YES', 'category': 'Communications'},
    'BREDBAND': {'account': '5340', 'vat': 'YES', 'category': 'Communications'},
    'ELBOLAG': {'account': '5320', 'vat': 'YES', 'category': 'Utilities'},
    'VATTENFALL': {'account': '5320', 'vat': 'YES', 'category': 'Utilities'},
    'EL & GAS': {'account': '5320', 'vat': 'YES', 'category': 'Utilities'},
    
    # ========== OFFICE & EQUIPMENT (5100-5150) ==========
    'STAPLES': {'account': '5150', 'vat': 'YES', 'category': 'Office'},
    'OFFICE': {'account': '5150', 'vat': 'YES', 'category': 'Office'},
    'XXXLFIX': {'account': '5150', 'vat': 'YES', 'category': 'Office'},
    'JYSK': {'account': '5150', 'vat': 'YES', 'category': 'Office'},
    'IKEA': {'account': '5150', 'vat': 'YES', 'category': 'Office'},
    'BAUHAUS': {'account': '5150', 'vat': 'YES', 'category': 'Office'},
    'APPLE': {'account': '5150', 'vat': 'YES', 'category': 'Office-Equipment'},
    'APPLE.COM': {'account': '5150', 'vat': 'YES', 'category': 'Office-Equipment'},
    'SAMSUNG': {'account': '5150', 'vat': 'YES', 'category': 'Office-Equipment'},
    
    # ========== OTHER SERVICES ==========
    'INSURANCE': {'account': '6580', 'vat': 'NO', 'category': 'Insurance'},
    'FÖRSÄKRING': {'account': '6580', 'vat': 'NO', 'category': 'Insurance'},
    'REVISOR': {'account': '5410', 'vat': 'YES', 'category': 'Professional'},
    'REVISOR AB': {'account': '5410', 'vat': 'YES', 'category': 'Professional'},
    'ADVOKAT': {'account': '5410', 'vat': 'YES', 'category': 'Professional'},
    'KONSULT': {'account': '5410', 'vat': 'YES', 'category': 'Professional'},
    'TOUMA': {'account': '5410', 'vat': 'YES', 'category': 'Professional'},
}

# ============================================================================
# ACCOUNT CONFIGURATION
# ============================================================================

ACCOUNTS = {
    '1010': 'Cash',
    '1200': 'Accounts Receivable',
    '1460': 'Inventory',
    '1469': 'Inventory Staging',
    '1930': 'Marginalen Bank',
    '1941': 'Viva Wallet',
    '1942': 'Wise USD Account',
    '1943': 'Wise EUR Account',
    '1944': 'Wise GBP Account',
    '1945': 'Wise SEK Account',
    '1947': 'Worldline Terminal',
    '1948': 'Revenue Staging',
    '2611': 'Output VAT',
    '2641': 'Input VAT',
    '2700': 'Accounts Payable',
    '2893': 'Ahmed Al-Sharif',
    '3051': 'Sales Revenue',
    '4110': 'COGS',
    '4545': 'Gift Allocation',
    '5100': 'Salaries',
    '5150': 'Office Equipment',
    '5200': 'Software Subscriptions',
    '5250': 'Marketing',
    '5280': 'Meals',
    '5300': 'Rent Business',
    '5310': 'Rent Personal',
    '5320': 'Utilities',
    '5340': 'Communications',
    '5360': 'Vehicle Costs',
    '5410': 'Professional Services',
    '5420': 'Freight',
    '5430': 'Repairs',
    '5900': 'Advertising',
    '6570': 'Bank Fees',
    '6580': 'Insurance',
    '6992': 'Non-Deductible Personal',
}

OPENING_BALANCES = {
    '1460': '820846.95',
    '2893': '-150000.00',
}

# ============================================================================
# SE FILE BUILDER
# ============================================================================

class SEFileBuilder:
    """Build complete SIE4 SE file from transactions"""
    
    def __init__(self):
        self.transactions = defaultdict(list)
        self.validation_report = {'errors': [], 'warnings': [], 'stats': {}}
        self.seq_counter = 1
    
    def route_merchant(self, merchant_name):
        """Look up merchant in directory, return (account, vat_treatment)"""
        merchant_upper = merchant_name.upper().strip()
        
        # Exact match first
        if merchant_upper in MERCHANT_DIRECTORY:
            route = MERCHANT_DIRECTORY[merchant_upper]
            return route['account'], route['vat']
        
        # Keyword match
        for keyword, route in MERCHANT_DIRECTORY.items():
            if keyword in merchant_upper:
                return route['account'], route['vat']
        
        # Default to non-deductible
        return '6992', 'NO'
    
    def add_transaction(self, date_str, description, debit_account, credit_account,
                       amount_sek, vat_amount=None):
        """Add balanced transaction"""
        
        try:
            amount = Decimal(str(amount_sek)).quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP
            )
            
            if amount == 0:
                return
            
            # Format date to YYYYMMDD
            date_parts = date_str.split('-')
            if len(date_parts) == 3:
                date_vis = f"{date_parts[0]}{date_parts[1]}{date_parts[2]}"
            else:
                date_vis = date_str.replace('-', '')
            
            # Create entry
            key = date_vis
            
            entry = {
                'date': date_vis,
                'sequence': self.seq_counter,
                'description': description[:60],
                'entries': [
                    {'account': debit_account, 'amount': amount, 'type': 'DEBIT'},
                    {'account': credit_account, 'amount': -amount, 'type': 'CREDIT'},
                ]
            }
            
            # Add VAT if applicable
            if vat_amount and Decimal(str(vat_amount)) != 0:
                vat = Decimal(str(vat_amount)).quantize(
                    Decimal('0.01'), rounding=ROUND_HALF_UP
                )
                entry['entries'].append({
                    'account': '2641',
                    'amount': vat,
                    'type': 'DEBIT'
                })
                entry['entries'].append({
                    'account': credit_account,
                    'amount': -vat,
                    'type': 'CREDIT'
                })
            
            self.transactions[key].append(entry)
            self.seq_counter += 1
            
        except Exception as e:
            self.validation_report['errors'].append(
                f"Add transaction error: {str(e)}"
            )
    
    def process_nordea_csv(self, filepath):
        """Process Nordea CSV file"""
        count = 0
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                # Try different delimiters
                sample = f.readline()
                f.seek(0)
                
                delimiter = ';' if ';' in sample else ','
                reader = csv.DictReader(f, delimiter=delimiter)
                
                for row in reader:
                    count += 1
                    
                    # Parse fields - handle different column names
                    date = row.get('Datum för kontohändelse') or row.get('Date') or ''
                    desc = row.get('Rubrik') or row.get('Description') or ''
                    amount_str = row.get('Belopp') or row.get('Amount') or '0'
                    
                    if not date or not desc:
                        continue
                    
                    # Clean values
                    date = date.strip('"').strip()
                    desc = desc.strip('"').strip()
                    amount_str = amount_str.strip('"').strip().replace(',', '.')
                    
                    try:
                        amount = Decimal(amount_str)
                    except:
                        continue
                    
                    # Route transaction
                    account, vat_treatment = self.route_merchant(desc)
                    
                    if amount > 0:
                        # Income/deposit
                        if vat_treatment == 'YES':
                            vat = amount / Decimal('1.25') * Decimal('0.25')
                            net = amount - vat
                            self.add_transaction(date, desc, '1930', account, net, vat)
                        else:
                            self.add_transaction(date, desc, '1930', account, amount)
                    else:
                        # Expense
                        if vat_treatment == 'YES':
                            vat = abs(amount) / Decimal('1.25') * Decimal('0.25')
                            net = abs(amount) - vat
                            self.add_transaction(date, desc, account, '1930', net, vat)
                        else:
                            self.add_transaction(date, desc, account, '1930', abs(amount))
        
        except Exception as e:
            self.validation_report['errors'].append(
                f"Process Nordea CSV error: {str(e)}"
            )
        
        return count
    
    def process_sales_csv(self, filepath):
        """Process sales CSV"""
        count = 0
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    qty = Decimal(row.get('Antal', '0') or '0')
                    sales_net = Decimal(row.get('Försäljning', '0') or '0')
                    vat = Decimal(row.get('Moms', '0') or '0')
                    cogs = Decimal(row.get('Inköpssumma', '0') or '0')
                    
                    if qty == 0 or sales_net == 0:
                        continue
                    
                    count += 1
                    
                    # Revenue entry
                    self.add_transaction('2025-09-30', 'Sales Revenue', '1948', 
                                       '3051', sales_net, vat)
                    
                    # COGS entry
                    if cogs > 0:
                        self.add_transaction('2025-09-30', 'COGS', '4110', 
                                           '1460', cogs)
        
        except Exception as e:
            self.validation_report['errors'].append(
                f"Process Sales CSV error: {str(e)}"
            )
        
        return count
    
    def generate_se_file(self, output_file):
        """Generate SIE4 SE file"""
        
        lines = []
        
        # Headers (Quran Part 13)
        lines.append('#FLAGGA 0')
        lines.append('#PROGRAM "Quran-Builder" "1.0"')
        lines.append('#FORMAT PC8')
        lines.append(f'#GEN {datetime.now().strftime("%Y%m%d")}')
        lines.append('#SIETYP 4')
        lines.append('#FNAMN "Samis Jackets AB"')
        lines.append('#ORGNR 559489-5301')
        lines.append('#RAR 0 20240701 20251231')
        lines.append('#KPTYP EUBAS97')
        lines.append('')
        
        # Opening balances
        lines.append('// OPENING BALANCES')
        for account, balance in OPENING_BALANCES.items():
            lines.append(f'#IB 0 {account} {balance}')
        lines.append('')
        
        # Transactions (sorted by date)
        lines.append('// TRANSACTIONS Q3 2025')
        
        for date_key in sorted(self.transactions.keys()):
            for tx in self.transactions[date_key]:
                # Validate balanced
                total = sum(e['amount'] for e in tx['entries'])
                if abs(total) > Decimal('0.01'):
                    self.validation_report['warnings'].append(
                        f"Unbalanced on {date_key}: {total}"
                    )
                
                # Write transaction
                desc = tx['description'][:50]
                seq = f"{tx['sequence']:04d}"
                
                lines.append(f'#VER "" "{date_key}-{seq}" {tx["date"]} "{desc}"')
                lines.append('{')
                
                for entry in tx['entries']:
                    account = entry['account']
                    amount = f"{float(entry['amount']):.2f}"
                    lines.append(f'    #TRANS {account} {{}} {amount}')
                
                lines.append('}')
        
        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        return output_file

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 80)
    print("SAMIS JACKETS AB - SE FILE BUILDER FROM QURAN v2")
    print("=" * 80)
    print()
    
    builder = SEFileBuilder()
    
    print("PROCESSING TRANSACTION FILES:")
    print("-" * 80)
    
    # Process Nordea files
    nordea_dir = 'nordea'
    if os.path.exists(nordea_dir):
        for csv_file in os.listdir(nordea_dir):
            if csv_file.endswith('.csv'):
                filepath = os.path.join(nordea_dir, csv_file)
                count = builder.process_nordea_csv(filepath)
                print(f"✅ {csv_file}: {count} transactions")
    
    # Process sales
    sales_file = 'sales_data/sales Försäljningsrapport from 0107 to 30-09.csv'
    if os.path.exists(sales_file):
        count = builder.process_sales_csv(sales_file)
        print(f"✅ Sales CSV: {count} items")
    
    print()
    print("GENERATING SE FILE:")
    print("-" * 80)
    
    output = builder.generate_se_file('20250930-COMPLETE.se')
    print(f"✅ Generated: {output}")
    
    # File stats
    file_size = os.path.getsize(output) / 1024
    with open(output, 'r') as f:
        line_count = len(f.readlines())
    
    print(f"   Size: {file_size:.1f} KB")
    print(f"   Lines: {line_count:,}")
    
    print()
    print("VALIDATION REPORT:")
    print("-" * 80)
    print(f"Transactions: {len(builder.transactions)}")
    print(f"Errors: {len(builder.validation_report['errors'])}")
    print(f"Warnings: {len(builder.validation_report['warnings'])}")
    
    if builder.validation_report['errors']:
        print("\nERRORS (first 5):")
        for err in builder.validation_report['errors'][:5]:
            print(f"  ⚠️  {err}")
    
    if builder.validation_report['warnings']:
        print("\nWARNINGS (first 5):")
        for warn in builder.validation_report['warnings'][:5]:
            print(f"  ℹ️  {warn}")
    
    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)

if __name__ == '__main__':
    main()
