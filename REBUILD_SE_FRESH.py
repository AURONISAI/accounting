# -*- coding: utf-8 -*-
"""
Rebuild SE file from scratch with CORRECT Swedish characters
Output: ISO-8859-1 with #FORMAT ISO
"""

import os

def rebuild_q4_complete():
    filepath = r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q4_2025_PERIOD_2025-10_TO_2025-12\final_se_files\Q4_2025_COMPLETE.se"
    
    # Read with latin-1 to get raw bytes
    with open(filepath, 'rb') as f:
        raw_bytes = f.read()
    
    # Decode as latin-1 (preserves all bytes)
    content = raw_bytes.decode('latin-1')
    
    # Swedish character mappings - replace ALL variants
    replacements = [
        # ö replacements (various corrupted forms)
        ('ö', 'ö'),  # Already correct
        ('\xf6', 'ö'),  # ISO-8859-1 ö
        ('\x94', 'ö'),  # CP437 ö
        ('?', ''),  # Will handle ? separately based on context
        
        # ä replacements
        ('ä', 'ä'),
        ('\xe4', 'ä'),
        ('\x84', 'ä'),
        
        # å replacements
        ('å', 'å'),
        ('\xe5', 'å'),
        ('\x86', 'å'),
        
        # Ö replacements
        ('Ö', 'Ö'),
        ('\xd6', 'Ö'),
        ('\x99', 'Ö'),
        
        # Ä replacements
        ('Ä', 'Ä'),
        ('\xc4', 'Ä'),
        ('\x8e', 'Ä'),
        
        # Å replacements
        ('Å', 'Å'),
        ('\xc5', 'Å'),
        ('\x8f', 'Å'),
    ]
    
    # Word-level fixes for common Swedish accounting terms with ? inside
    word_fixes = [
        # Header
        ("Bokf?ring", "Bokföring"),
        ("Spiris Bokföring", "Spiris Bokföring"),
        
        # Account names with ö
        ("anl?ggningar", "anläggningar"),
        ("anläggningar", "anläggningar"),
        ("avskrivningar p?", "avskrivningar på"),
        ("avskrivningar på", "avskrivningar på"),
        ("?vriga f?retag", "övriga företag"),
        ("övriga företag", "övriga företag"),
        ("L?ngfristiga", "Långfristiga"),
        ("Långfristiga", "Långfristiga"),
        ("anst?llda", "anställda"),
        ("anställda", "anställda"),
        ("L?mnade", "Lämnade"),
        ("Lämnade", "Lämnade"),
        ("l?ngfristiga", "långfristiga"),
        ("långfristiga", "långfristiga"),
        ("F?r?ndring", "Förändring"),
        ("Förändring", "Förändring"),
        ("P?g?ende", "Pågående"),
        ("Pågående", "Pågående"),
        ("reskontraf?rda", "reskontraförda"),
        ("reskontraförda", "reskontraförda"),
        ("Avr?kning", "Avräkning"),
        ("Avräkning", "Avräkning"),
        ("f?r skatter", "för skatter"),
        ("för skatter", "för skatter"),
        ("F?rutbetalda", "Förutbetalda"),
        ("Förutbetalda", "Förutbetalda"),
        ("?vriga", "Övriga"),
        ("Övriga", "Övriga"),
        ("upplupna int?kter", "upplupna intäkter"),
        ("upplupna intäkter", "upplupna intäkter"),
        ("F?retagskonto", "Företagskonto"),
        ("Företagskonto", "Företagskonto"),
        ("aff?rskonto", "affärskonto"),
        ("affärskonto", "affärskonto"),
        ("ins?ttningar", "insättningar"),
        ("insättningar", "insättningar"),
        ("?verkursfond", "överkursfond"),
        ("överkursfond", "överkursfond"),
        ("f?rlust", "förlust"),
        ("förlust", "förlust"),
        ("Erh?llna", "Erhållna"),
        ("Erhållna", "Erhållna"),
        ("aktie?gartillskott", "aktieägartillskott"),
        ("aktieägartillskott", "aktieägartillskott"),
        ("f?reg?ende", "föregående"),
        ("föregående", "föregående"),
        ("?rets", "Årets"),
        ("Årets", "Årets"),
        ("?veravskrivningar", "överavskrivningar"),
        ("överavskrivningar", "överavskrivningar"),
        ("F?rskott", "Förskott"),
        ("Förskott", "Förskott"),
        ("fr?n kunder", "från kunder"),
        ("från kunder", "från kunder"),
        ("Leverant?rsskulder", "Leverantörsskulder"),
        ("Leverantörsskulder", "Leverantörsskulder"),
        ("leverant?rsskulder", "leverantörsskulder"),
        ("leverantörsskulder", "leverantörsskulder"),
        ("Utg?ende", "Utgående"),
        ("Utgående", "Utgående"),
        ("moms p?", "moms på"),
        ("moms på", "moms på"),
        ("f?rs?ljning", "försäljning"),
        ("försäljning", "försäljning"),
        ("omv?nd", "omvänd"),
        ("omvänd", "omvänd"),
        ("ing?ende", "ingående"),
        ("ingående", "ingående"),
        ("Ber?knad", "Beräknad"),
        ("Beräknad", "Beräknad"),
        ("f?rv?rv", "förvärv"),
        ("förvärv", "förvärv"),
        ("fr?n utlandet", "från utlandet"),
        ("från utlandet", "från utlandet"),
        ("tj?nst", "tjänst"),
        ("tjänst", "tjänst"),
        ("f?r moms", "för moms"),
        ("för moms", "för moms"),
        ("s?rskild", "särskild"),
        ("särskild", "särskild"),
        ("l?neskatt", "löneskatt"),
        ("löneskatt", "löneskatt"),
        ("l?neavdrag", "löneavdrag"),
        ("löneavdrag", "löneavdrag"),
        ("Fackf?reningsavgifter", "Fackföreningsavgifter"),
        ("Fackföreningsavgifter", "Fackföreningsavgifter"),
        ("n?rst?ende", "närstående"),
        ("närstående", "närstående"),
        ("l?ner", "löner"),
        ("löner", "löner"),
        ("semesterl?ner", "semesterlöner"),
        ("semesterlöner", "semesterlöner"),
        ("pensionsf?rs?kringsavgifter", "pensionsförsäkringsavgifter"),
        ("pensionsförsäkringsavgifter", "pensionsförsäkringsavgifter"),
        ("f?rutbetalda", "förutbetalda"),
        ("förutbetalda", "förutbetalda"),
        ("F?rs?ljn", "Försäljn"),
        ("Försäljn", "Försäljn"),
        ("tj?nst", "tjänst"),
        ("utanf?r", "utanför"),
        ("utanför", "utanför"),
        ("F?rs?ljning", "Försäljning"),
        ("Försäljning", "Försäljning"),
        ("tj?nster", "tjänster"),
        ("tjänster", "tjänster"),
        ("P?minnelseavgift", "Påminnelseavgift"),
        ("Påminnelseavgift", "Påminnelseavgift"),
        ("sidoint?kter", "sidointäkter"),
        ("sidointäkter", "sidointäkter"),
        ("?res-", "Öres-"),
        ("Öres-", "Öres-"),
        ("kronutj?mning", "kronutjämning"),
        ("kronutjämning", "kronutjämning"),
        ("?tervunna", "Återvunna"),
        ("Återvunna", "Återvunna"),
        ("Valutakursvinster p?", "Valutakursvinster på"),
        ("Valutakursvinster på", "Valutakursvinster på"),
        ("anl?ggningar", "anläggningar"),
        ("anl?ggningstillg?ngar", "anläggningstillgångar"),
        ("anläggningstillgångar", "anläggningstillgångar"),
        ("Ink?p", "Inköp"),
        ("Inköp", "Inköp"),
        ("ink?p", "inköp"),
        ("inköp", "inköp"),
        ("fr?n Sverige", "från Sverige"),
        ("från Sverige", "från Sverige"),
        ("s?lda", "sålda"),
        ("sålda", "sålda"),
        ("Ink?pta", "Inköpta"),
        ("Inköpta", "Inköpta"),
        ("ink?pspriser", "inköpspriser"),
        ("inköpspriser", "inköpspriser"),
        ("underh?ll", "underhåll"),
        ("underhåll", "underhåll"),
        ("F?rbrukningsinventarier", "Förbrukningsinventarier"),
        ("Förbrukningsinventarier", "Förbrukningsinventarier"),
        ("f?rbrukningsmaterial", "förbrukningsmaterial"),
        ("förbrukningsmaterial", "förbrukningsmaterial"),
        ("F?rbrukningsmaterial", "Förbrukningsmaterial"),
        ("Förbrukningsmaterial", "Förbrukningsmaterial"),
        ("Arbetskl?der", "Arbetskläder"),
        ("Arbetskläder", "Arbetskläder"),
        ("arbetskl?der", "arbetskläder"),
        ("arbetskläder", "arbetskläder"),
        ("f?r transportmedel", "för transportmedel"),
        ("för transportmedel", "för transportmedel"),
        ("f?r personbilar", "för personbilar"),
        ("för personbilar", "för personbilar"),
        ("F?rs?kring", "Försäkring"),
        ("Försäkring", "Försäkring"),
        ("f?rs?kring", "försäkring"),
        ("försäkring", "försäkring"),
        ("Tr?ngselskatt", "Trängselskatt"),
        ("Trängselskatt", "Trängselskatt"),
        ("f?r arbetsmaskiner", "för arbetsmaskiner"),
        ("för arbetsmaskiner", "för arbetsmaskiner"),
        ("B?t-", "Båt-"),
        ("Båt-", "Båt-"),
        ("?vriga resekostnader", "Övriga resekostnader"),
        ("Övriga resekostnader", "Övriga resekostnader"),
        ("marknadsf?ringsverktyg", "marknadsföringsverktyg"),
        ("marknadsföringsverktyg", "marknadsföringsverktyg"),
        ("F?retagsf?rs?kringar", "Företagsförsäkringar"),
        ("Företagsförsäkringar", "Företagsförsäkringar"),
        ("F?rluster", "Förluster"),
        ("Förluster", "Förluster"),
        ("f?rluster", "förluster"),
        ("förluster", "förluster"),
        ("p? kundfordringar", "på kundfordringar"),
        ("på kundfordringar", "på kundfordringar"),
        ("Ers?ttningar", "Ersättningar"),
        ("Ersättningar", "Ersättningar"),
        ("ers?ttningar", "ersättningar"),
        ("ersättningar", "ersättningar"),
        ("IT-tj?nster", "IT-tjänster"),
        ("IT-tjänster", "IT-tjänster"),
        ("f?rs?ljningspersonal", "försäljningspersonal"),
        ("försäljningspersonal", "försäljningspersonal"),
        ("f?retagsledare", "företagsledare"),
        ("företagsledare", "företagsledare"),
        ("L?ner", "Löner"),
        ("Löner", "Löner"),
        ("kollektivanst?llda", "kollektivanställda"),
        ("kollektivanställda", "kollektivanställda"),
        ("tj?nstem?n", "tjänstemän"),
        ("tjänstemän", "tjänstemän"),
        ("Kostnadsers?ttningar", "Kostnadsersättningar"),
        ("Kostnadsersättningar", "Kostnadsersättningar"),
        ("f?rm?ner", "förmåner"),
        ("förmåner", "förmåner"),
        ("bilers?ttningar", "bilersättningar"),
        ("bilersättningar", "bilersättningar"),
        ("f?reskrivna", "föreskrivna"),
        ("föreskrivna", "föreskrivna"),
        ("Motkontering f?rm?ner", "Motkontering förmåner"),
        ("Motkontering förmåner", "Motkontering förmåner"),
        ("Pensionsf?rs?kringspremier", "Pensionsförsäkringspremier"),
        ("Pensionsförsäkringspremier", "Pensionsförsäkringspremier"),
        ("f?rsta anst?lld", "första anställd"),
        ("första anställd", "första anställd"),
        ("S?rskild", "Särskild"),
        ("Särskild", "Särskild"),
        ("f?r pensionskostnader", "för pensionskostnader"),
        ("för pensionskostnader", "för pensionskostnader"),
        ("p? maskiner", "på maskiner"),
        ("på maskiner", "på maskiner"),
        ("Valutakursf?rluster", "Valutakursförluster"),
        ("Valutakursförluster", "Valutakursförluster"),
        ("F?rlust vid avyttring", "Förlust vid avyttring"),
        ("Förlust vid avyttring", "Förlust vid avyttring"),
        ("R?nteint?kter", "Ränteintäkter"),
        ("Ränteintäkter", "Ränteintäkter"),
        ("fr?n bank", "från bank"),
        ("från bank", "från bank"),
        ("Valutakursdifferenser p?", "Valutakursdifferenser på"),
        ("Valutakursdifferenser på", "Valutakursdifferenser på"),
        ("R?ntekostnader", "Räntekostnader"),
        ("Räntekostnader", "Räntekostnader"),
        ("Dr?jsm?lsr?ntor", "Dröjsmålsräntor"),
        ("Dröjsmålsräntor", "Dröjsmålsräntor"),
        ("f?r leverant?rsskulder", "för leverantörsskulder"),
        ("för leverantörsskulder", "för leverantörsskulder"),
        ("p? skulder", "på skulder"),
        ("på skulder", "på skulder"),
        ("Avs?ttning", "Avsättning"),
        ("Avsättning", "Avsättning"),
        ("?terf?ring", "Återföring"),
        ("Återföring", "Återföring"),
        ("fr?n periodiseringsfond", "från periodiseringsfond"),
        ("från periodiseringsfond", "från periodiseringsfond"),
        ("F?r?ndring av ?veravskrivningar", "Förändring av överavskrivningar"),
        ("Förändring av överavskrivningar", "Förändring av överavskrivningar"),
        ("p? ?rets resultat", "på årets resultat"),
        ("på årets resultat", "på årets resultat"),
        
        # Transaction descriptions
        ("M?nadsavgift", "Månadsavgift"),
        ("Månadsavgift", "Månadsavgift"),
        ("?verf?ring", "Överföring"),
        ("Överföring", "Överföring"),
        ("f?rseningsavgift", "förseningsavgift"),
        ("förseningsavgift", "förseningsavgift"),
        ("F?retagskonto", "Företagskonto"),
        ("M?lardalstrafik", "Mälardalstrafik"),
        ("Mälardalstrafik", "Mälardalstrafik"),
        ("f?rpackning", "förpackning"),
        ("förpackning", "förpackning"),
        
        # Fix remaining ? that should be ö
        ("?vriga", "Övriga"),
        ("?vrig", "Övrig"),
    ]
    
    # Apply all word fixes
    for old, new in word_fixes:
        content = content.replace(old, new)
    
    # Fix remaining standalone issues
    # Replace remaining single ? chars in common Swedish patterns
    remaining_fixes = [
        ("F?r", "För"),
        ("f?r", "för"),
        ("?r", "år"),  # Be careful with this one
        ("p?", "på"),
        ("?", "ö"),  # Last resort for remaining ?
    ]
    
    # Don't apply the last resort - too dangerous
    # Only apply specific fixes
    
    # Write as ISO-8859-1
    with open(filepath, 'w', encoding='iso-8859-1', newline='\n') as f:
        f.write(content)
    
    print(f"Fixed: {filepath}")
    
    # Verify
    with open(filepath, 'rb') as f:
        data = f.read(500)
    print(f"First 500 bytes (hex): {data[:200].hex()}")

if __name__ == "__main__":
    rebuild_q4_complete()
