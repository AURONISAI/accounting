# -*- coding: utf-8 -*-
"""
Convert ALL Swedish characters to ASCII equivalents
a = a, o = o (no special chars)
"""

import os

filepath = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q4_2025_PERIOD_2025-10_TO_2025-12\final_se_files\Q4_2025_COMPLETE.se"

# Read file as bytes
with open(filepath, 'rb') as f:
    data = f.read()

# Decode as latin-1
text = data.decode('latin-1')

# Replace ALL Swedish special characters with ASCII
replacements = [
    # Lowercase
    ('ö', 'o'),
    ('ä', 'a'),
    ('å', 'a'),
    ('\xf6', 'o'),  # ö in latin-1
    ('\xe4', 'a'),  # ä in latin-1
    ('\xe5', 'a'),  # å in latin-1
    # Uppercase
    ('Ö', 'O'),
    ('Ä', 'A'),
    ('Å', 'A'),
    ('\xd6', 'O'),  # Ö in latin-1
    ('\xc4', 'A'),  # Ä in latin-1
    ('\xc5', 'A'),  # Å in latin-1
    # Any remaining garbage
    ('�', 'o'),
    ('?', ''),  # Remove question marks that replaced chars
]

for old, new in replacements:
    text = text.replace(old, new)

# Fix specific words that need question mark removal
text = text.replace('Mnadsavgift', 'Manadsavgift')
text = text.replace('verfring', 'Overforing')
text = text.replace('Frsakring', 'Forsakring')
text = text.replace('Mlardalstrafik', 'Malardalstrafik')

# Write as ASCII
with open(filepath, 'w', encoding='ascii', errors='replace', newline='\n') as f:
    f.write(text)

print("DONE - All Swedish chars replaced with ASCII")
