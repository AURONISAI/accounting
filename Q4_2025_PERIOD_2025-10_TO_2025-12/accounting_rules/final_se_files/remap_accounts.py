# -*- coding: utf-8 -*-
import re

with open('Q4_2025_COMPLETE.se', 'r', encoding='cp437') as f:
    content = f.read()

# Mapping: old account -> existing account in Visma
mappings = {
    '1582': '1580',   # Shopify clearing -> Fordran hos kunder
    '1946': '1940',   # Wise TRY -> Ovriga bankkonton
    '2610': '2611',   # Utgaende moms -> Utg moms 25% sv
    '3001': '3051',   # Forsaljning -> Forsaljn varor 25% sv
    '4010': '4000',   # Varukop -> Inkop av varor fran Sverige
    '5020': '5010',   # Hyra kontorslokal -> Lokalhyra
    '5710': '5700',   # Frakter -> Frakter och transporter
    '5990': '5900',   # Ovrig reklam -> Reklam och PR
    '6080': '6500',   # Foretagstjanster -> Ovriga externa tjanster
    '6090': '6990',   # Forvaltningskostnader -> Ovriga externa kostnader
    '6580': '6570',   # Betalningsformedling -> Bankkostnader
    '6700': '6500',   # Administrationskostnader -> Ovriga externa tjanster
    '8310': '8311',   # Ranteintakter -> Ranteintakter fran bank
    '8410': '8400',   # Rantekostnader -> Rantekostnader gruppkonto
}

# Replace in TRANS lines only
for old_acc, new_acc in mappings.items():
    # Replace #TRANS old_acc with #TRANS new_acc
    pattern = f'#TRANS {old_acc} '
    replacement = f'#TRANS {new_acc} '
    count = content.count(pattern)
    content = content.replace(pattern, replacement)
    if count > 0:
        print(f'Replaced {old_acc} -> {new_acc}: {count} times')

# Also remove the added KONTO definitions for these accounts
for old_acc in mappings.keys():
    # Remove lines like #KONTO 1582 "..."
    pattern = f'#KONTO {old_acc} "[^"]*"\n'
    content = re.sub(pattern, '', content)

with open('Q4_2025_COMPLETE.se', 'w', encoding='cp437') as f:
    f.write(content)

print('\nDone! Accounts remapped to existing Visma accounts.')
