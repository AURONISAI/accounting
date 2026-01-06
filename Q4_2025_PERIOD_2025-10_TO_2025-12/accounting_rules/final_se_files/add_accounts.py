# -*- coding: utf-8 -*-
import re

with open('Q4_2025_COMPLETE.se', 'r', encoding='cp437') as f:
    content = f.read()

# Add 8310 before 8311
content = content.replace(
    '#KONTO 8311',
    '#KONTO 8310 "Ranteintakter"\n#KONTO 8311'
)

# Add 8410 between 8400 and 8422
content = content.replace(
    '#KONTO 8422',
    '#KONTO 8410 "Rantekostnader for langfristiga skulder"\n#KONTO 8422'
)

with open('Q4_2025_COMPLETE.se', 'w', encoding='cp437') as f:
    f.write(content)

print('Added 8310 and 8410')
