# -*- coding: utf-8 -*-
import re

with open('Q4_2025_COMPLETE.se', 'r', encoding='cp437') as f:
    content = f.read()

print('REMAPPING ACCOUNTS TO EXISTING VISMA ACCOUNTS')
print('='*60)

# 1. First fix Temu transactions: 4010 -> 5460 (only for Temu, not Varuforbrukning)
# VER 786 and 793 are Temu - change 4010 to 5460
content = content.replace(
    '#VER A 786 20251017 "Temu forpackning SEK 548.87 SEK"\n{\n#TRANS 4010 {} 548.87',
    '#VER A 786 20251017 "Temu forpackning SEK 548.87 SEK"\n{\n#TRANS 5460 {} 548.87'
)
print('VER 786: Temu 4010 -> 5460 (Forbrukningsmaterial)')

content = content.replace(
    '#VER A 793 20251101 "Temu refund SEK 30.97 SEK"\n{\n#TRANS 1945 {} 30.97\n#TRANS 4010 {} -30.97',
    '#VER A 793 20251101 "Temu refund SEK 30.97 SEK"\n{\n#TRANS 1945 {} 30.97\n#TRANS 5460 {} -30.97'
)
print('VER 793: Temu refund 4010 -> 5460 (Forbrukningsmaterial)')

# 2. Remap all other accounts
mappings = {
    # Account: (new_account, description)
    '1582': ('1580', 'Shopify clearing -> Fordran'),
    '1946': ('1940', 'Wise TRY -> Ovriga bankkonton'),
    '2610': ('2611', 'Utgaende moms -> Utg moms 25%'),
    '3001': ('3051', 'Forsaljning -> Forsaljn varor 25%'),
    '5020': ('5010', 'Hyra kontorslokal -> Lokalhyra'),
    '5710': ('5700', 'Frakter -> Frakter gruppkonto'),
    '5990': ('5900', 'Ovrig reklam -> Reklam PR'),
    '6080': ('6500', 'Foretagstjanster -> Ovriga externa'),
    '6090': ('6990', 'Forvaltning -> Ovriga externa kostn'),
    '6580': ('6570', 'Betalningsformedling -> Bankkostnader'),
    '6700': ('6500', 'Administration -> Ovriga externa'),
    '8310': ('8311', 'Ranteintakter -> Ranteint fran bank'),
    '8410': ('8400', 'Rantekostnader -> Rantekostn gruppkonto'),
}

for old_acc, (new_acc, desc) in mappings.items():
    pattern = f'#TRANS {old_acc} '
    count = content.count(pattern)
    if count > 0:
        content = content.replace(pattern, f'#TRANS {new_acc} ')
        print(f'{old_acc} -> {new_acc}: {count} transactions ({desc})')

# 3. Remove added KONTO definitions for remapped accounts (keep only standard ones)
accounts_to_remove = ['1582', '1946', '2610', '3001', '4010', '5020', '5710', '5990', 
                      '6080', '6090', '6580', '6700', '8310', '8410']

for acc in accounts_to_remove:
    # Remove lines like #KONTO 1582 "..."
    pattern = f'#KONTO {acc} "[^"]*"\n'
    if re.search(pattern, content):
        content = re.sub(pattern, '', content)
        print(f'Removed #KONTO {acc} definition')

# 4. Make sure 5460 is defined (for Temu)
if '#KONTO 5460' not in content:
    content = content.replace(
        '#KONTO 5420 Programvaror\n',
        '#KONTO 5420 Programvaror\n#KONTO 5460 Forbrukningsmaterial\n'
    )
    print('Added #KONTO 5460 Forbrukningsmaterial')

with open('Q4_2025_COMPLETE.se', 'w', encoding='cp437') as f:
    f.write(content)

print('\n' + '='*60)
print('DONE! All accounts remapped to existing Visma accounts.')
