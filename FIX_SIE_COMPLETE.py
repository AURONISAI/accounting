# -*- coding: utf-8 -*-
"""
SIE File Swedish Character Fixer
================================
RULE #1: Internal text is UTF-8 with correct Swedish characters (å ä ö)
Output: ISO-8859-1 with #FORMAT ISO for Visma compatibility
"""

import os
import re

# UTF-8 internal strings - correct Swedish characters
ACCOUNT_NAMES = {
    "1210": "Maskiner och andra tekniska anläggningar",
    "1220": "Inventarier och verktyg",
    "1229": "Ackumulerade avskrivningar på inventarier och verktyg",
    "1240": "Bilar och andra transportmedel",
    "1337": "Ackumulerade nedskrivningar av andelar i övriga företag",
    "1357": "Andelar i handelsbolag, andra företag",
    "1382": "Långfristiga fordringar hos anställda",
    "1383": "Lämnade depositioner, långfristiga",
    "1388": "Långfristiga kundfordringar",
    "1460": "Lager av handelsvaror",
    "1469": "Förändring av lager av handelsvaror",
    "1470": "Pågående arbeten",
    "1510": "Kundfordringar",
    "1518": "Ej reskontraförda kundfordringar",
    "1519": "Nedskrivning av kundfordringar",
    "1549": "Nedskrivning av ej reskontraförda kundfordringar",
    "1580": "Fordringar",
    "1630": "Avräkning för skatter och avgifter (skattekonto)",
    "1640": "Skattefordringar",
    "1650": "Momsfordran",
    "1700": "Förutbetalda kostnader/interimsfordringar",
    "1790": "Övriga förutbetalda kostnader och upplupna intäkter",
    "1910": "Kassa",
    "1920": "PlusGiro",
    "1930": "Företagskonto/checkkonto/affärskonto",
    "1940": "Övriga bankkonton",
    "1941": "Annat bankkonto viva.com",
    "1942": "Wise USD",
    "1943": "Wise GBP",
    "1944": "Wise EUR",
    "1945": "Wise SEK",
    "1947": "Worldline",
    "1948": "Sales account",
    "1980": "Valutakonton",
    "2018": "Övriga egna insättningar",
    "2081": "Aktiekapital",
    "2086": "Reservfond",
    "2087": "Bunden överkursfond",
    "2091": "Balanserad vinst eller förlust",
    "2093": "Erhållna aktieägartillskott",
    "2098": "Vinst eller förlust från föregående år",
    "2099": "Årets resultat",
    "2110": "Periodiseringsfonder",
    "2121": "Periodiseringsfond 2021",
    "2122": "Periodiseringsfond 2022",
    "2125": "Periodiseringsfond 2025",
    "2126": "Periodiseringsfond 2026",
    "2127": "Periodiseringsfond 2027",
    "2128": "Periodiseringsfond 2028",
    "2129": "Periodiseringsfond 2019",
    "2130": "Periodiseringsfond 2020 - nr 2",
    "2131": "Periodiseringsfond 2021 - nr 2",
    "2132": "Periodiseringsfond 2022 - nr 2",
    "2133": "Periodiseringsfond 2023 - nr 2",
    "2134": "Periodiseringsfond 2024 - nr 2",
    "2135": "Periodiseringsfond 2025 - nr 2",
    "2136": "Periodiseringsfond 2026 - nr 2",
    "2137": "Periodiseringsfond 2027 - nr 2",
    "2138": "Periodiseringsfond 2028 - nr 2",
    "2139": "Periodiseringsfond 2019 - nr 2",
    "2150": "Ackumulerade överavskrivningar",
    "2390": "Övriga långfristiga skulder",
    "2399": "Övriga långfristiga skulder",
    "2420": "Förskott från kunder",
    "2440": "Leverantörsskulder",
    "2441": "Future World Tech",
    "2448": "Ej reskontraförda leverantörsskulder",
    "2499": "Andra övriga kortfristiga skulder",
    "2510": "Skatteskulder",
    "2518": "Betald F-skatt",
    "2611": "Utgående moms på försäljning inom Sverige, 25%",
    "2612": "Utgående moms på egna uttag, 25%",
    "2614": "Utgående moms, omvänd betalningsskyldighet, 25%",
    "2615": "Utgående moms import av varor 25%",
    "2619": "Utgående moms på försäljning inom EU, OSS",
    "2621": "Utgående moms på försäljning inom Sverige, 12%",
    "2624": "Utgående moms, omvänd betalningsskyldighet, 12%",
    "2631": "Utgående moms på försäljning inom Sverige, 6%",
    "2634": "Utgående moms, omvänd betalningsskyldighet, 6%",
    "2641": "Debiterad ingående moms",
    "2645": "Beräknad ingående moms på förvärv från utlandet",
    "2647": "Ingående moms, omvänd betalningsskyldighet varor och tjänst",
    "2650": "Redovisningskonto för moms",
    "2710": "Personalskatt",
    "2730": "Lagstadgade sociala avgifter och särskild löneskatt",
    "2731": "Avräkning lagstadgade sociala avgifter",
    "2732": "Avräkning särskild löneskatt",
    "2790": "Övriga löneavdrag",
    "2794": "Fackföreningsavgifter",
    "2890": "Övriga kortfristiga skulder",
    "2893": "Skulder till närstående personer, kortfristig del",
    "2910": "Upplupna löner",
    "2920": "Upplupna semesterlöner",
    "2940": "Upplupna lagstadgade sociala och andra avgifter",
    "2941": "Beräknade upplupna lagstadgade sociala avgifter",
    "2950": "Upplupna avtalade sociala avgifter",
    "2959": "Upplupna avtalade pensionsförsäkringsavgifter",
    "2990": "Övriga upplupna kostnader och förutbetalda intäkter",
    "2999": "OBS-konto",
    "3041": "Försäljn tjänst 25% sv",
    "3042": "Försäljn tjänst 12% sv",
    "3043": "Försäljn tjänst 6% sv",
    "3044": "Försäljn tjänst sv momsfri",
    "3045": "Försäljn tjänst utanför EG momsfri",
    "3046": "Försäljn tjänst till EG 25%",
    "3048": "Försäljn tjänst EG momsfri",
    "3051": "Försäljn varor 25% sv",
    "3052": "Försäljn varor 12% sv",
    "3053": "Försäljn varor 6% sv",
    "3054": "Försäljn varor sv momsfri",
    "3055": "Försäljn varor utanför EG momsfri",
    "3056": "Försäljn varor till EG 25% momspliktig",
    "3057": "Treparts försäljn varor till EG 25%",
    "3058": "Försäljn varor EG momsfri",
    "3109": "Försäljning varor till annat EU-land, OSS",
    "3231": "Försäljning inom byggsektorn, omvänd skattskyldighet moms",
    "3309": "Försäljning tjänster till annat EU-land, OSS",
    "3510": "Fakturerat emballage",
    "3520": "Fakturerade frakter",
    "3521": "Fakturerade frakter, EU-land",
    "3522": "Fakturerade frakter, export",
    "3530": "Fakturerade tull- och speditionskostnader m.m.",
    "3540": "Faktureringsavgifter",
    "3541": "Faktureringsavgifter, EU-land",
    "3542": "Faktureringsavgifter, export",
    "3543": "Faktureringavgift 12%",
    "3544": "Faktureringavgift 6%",
    "3590": "Övriga fakturerade kostnader",
    "3596": "Påminnelseavgift",
    "3690": "Övriga sidointäkter",
    "3740": "Öres- och kronutjämning",
    "3950": "Återvunna, tidigare avskrivna kundfordringar",
    "3960": "Valutakursvinster på fordringar och skulder",
    "3970": "Vinst vid avyttring av anläggningar",
    "3971": "Vinst vid avyttring av immateriella anläggningstillgångar",
    "3980": "Erhållna offentliga bidrag",
    "4000": "Inköp av varor från Sverige",
    "4001": "Inköp av tjänst",
    "4056": "Inköp varor 25% EU",
    "4057": "Inköp varor 12% EU",
    "4058": "Inköp varor 6% EU",
    "4059": "Inköp varor EU momsfri",
    "4110": "Kostnad sålda varor",
    "4400": "Momspliktiga inköp i Sverige",
    "4415": "Inköpta varor i Sverige, omvänd betalningsskyldighet, 25 %",
    "4416": "Inköpta varor i Sverige, omvänd betalningsskyldighet, 12 %",
    "4417": "Inköpta varor i Sverige, omvänd betalningsskyldighet, 6 %",
    "4500": "Övriga momspliktiga inköp",
    "4531": "Inköp av tjänster från ett land utanför EU, 25% moms",
    "4532": "Inköp av tjänster från ett land utanför EU, 12 % moms",
    "4533": "Inköp av tjänster från ett land utanför EU, 6 % moms",
    "4545": "Import av varor, 25% moms",
    "4546": "Import av varor, 12 % moms",
    "4547": "Import av varor, 6 % moms",
    "4549": "Motkonto beskattningsunderlag import",
    "4700": "Reduktion av inköpspriser",
    "4900": "Förändring av lager",
    "5000": "Lokalkostnader",
    "5010": "Lokalhyra",
    "5070": "Reparation och underhåll av lokaler",
    "5200": "Hyra av anläggningstillgångar",
    "5400": "Förbrukningsinventarier och förbrukningsmaterial",
    "5410": "Förbrukningsinventarier",
    "5420": "Programvaror",
    "5460": "Förbrukningsmaterial",
    "5480": "Arbetskläder och skyddsmaterial",
    "5600": "Kostnader för transportmedel",
    "5610": "Personbilskostnader",
    "5611": "Drivmedel för personbilar",
    "5612": "Försäkring och skatt för personbilar",
    "5613": "Reparation och underhåll av personbilar",
    "5615": "Leasing av personbilar",
    "5616": "Trängselskatt, avdragsgill",
    "5619": "Övriga personbilskostnader",
    "5620": "Lastbilskostnader",
    "5630": "Truckkostnader",
    "5640": "Kostnader för arbetsmaskiner",
    "5650": "Traktorkostnader",
    "5660": "Motorcykel-, moped- och skoterkostnader",
    "5670": "Båt-, flygplans- och helikopterkostnader",
    "5690": "Övriga kostnader för transportmedel",
    "5700": "Frakter och transporter",
    "5800": "Resekostnader",
    "5810": "Biljetter",
    "5830": "Kost och logi",
    "5890": "Övriga resekostnader",
    "5900": "Reklam och PR",
    "5910": "Annonsering",
    "5911": "AI-marknadsföringsverktyg",
    "5920": "Utomhus- och trafikreklam",
    "6000": "Övriga försäljningskostnader (gruppkonto)",
    "6044": "Avgift kortbetalning Webshop",
    "6071": "Representation, avdragsgill",
    "6072": "Representation, ej avdragsgill",
    "6100": "Kontorsmateriel och trycksaker (gruppkonto)",
    "6110": "Kontorsmateriel",
    "6200": "Tele och post (gruppkonto)",
    "6212": "Mobiltelefon",
    "6250": "Postbefordran",
    "6300": "Företagsförsäkringar och övriga riskkostnader (gruppkonto)",
    "6310": "Företagsförsäkringar",
    "6350": "Förluster på kundfordringar",
    "6351": "Konstaterade förluster på kundfordringar",
    "6352": "Befarade förluster på kundfordringar",
    "6358": "Befarade förluster på kundfordringar, OSS",
    "6359": "Konstaterade förluster på kundfordringar, OSS",
    "6420": "Ersättningar till revisor",
    "6500": "Övriga externa tjänster",
    "6540": "IT-tjänster",
    "6570": "Bankkostnader",
    "6590": "Övriga externa tjänster",
    "6800": "Inhyrd personal (gruppkonto)",
    "6810": "Inhyrd produktionspersonal",
    "6820": "Inhyrd lagerpersonal",
    "6830": "Inhyrd transportpersonal",
    "6840": "Inhyrd kontors- och ekonomipersonal",
    "6850": "Inhyrd IT-personal",
    "6860": "Inhyrd marknads- och försäljningspersonal",
    "6870": "Inhyrd restaurang- och butikspersonal",
    "6880": "Inhyrda företagsledare",
    "6890": "Övrig inhyrd personal",
    "6900": "Övriga externa kostnader (gruppkonto)",
    "6990": "Övriga externa kostnader",
    "6991": "Övriga kostnader, avdragsgilla",
    "6992": "Övriga externa kostnader, ej avdragsgilla",
    "7000": "Löner till kollektivanställda (gruppkonto)",
    "7010": "Löner till kollektivanställda",
    "7210": "Löner till tjänstemän",
    "7220": "Löner till företagsledare",
    "7300": "Kostnadsersättningar och förmåner (gruppkonto)",
    "7321": "Skattefria traktamenten, Sverige",
    "7322": "Skattepliktiga traktamenten, Sverige",
    "7323": "Skattefria traktamenten, utlandet",
    "7324": "Skattepliktiga traktamenten, utlandet",
    "7331": "Skattefria bilersättningar",
    "7332": "Skattepliktiga bilersättningar",
    "7350": "Ersättningar för föreskrivna arbetskläder",
    "7380": "Kostnader för förmåner till anställda",
    "7390": "Övriga kostnadsersättningar och förmåner",
    "7399": "Motkontering förmåner",
    "7410": "Pensionsförsäkringspremier",
    "7500": "Sociala och andra avgifter enligt lag och avtal (gruppkonto)",
    "7510": "Arbetsgivaravgifter",
    "7513": "Arbetsgivaravgift avdrag forskning",
    "7514": "Arbetsgivaravgift första anställd",
    "7533": "Särskild löneskatt för pensionskostnader",
    "7560": "Arbetsgivaravgifter 25,46 %",
    "7600": "Övriga personalkostnader (gruppkonto)",
    "7831": "Avskrivningar på maskiner och andra tekniska anläggningar",
    "7832": "Avskrivning byggnader",
    "7960": "Valutakursförluster",
    "7973": "Förlust vid avyttring av maskiner och inventarier",
    "8311": "Ränteintäkter från bank",
    "8314": "Ränteintäkter från kortfristiga placeringar",
    "8330": "Valutakursdifferenser på kortfristiga fordringar och placeringar",
    "8400": "Räntekostnader",
    "8422": "Dröjsmålsräntor för leverantörsskulder",
    "8423": "Räntekostnader för skatter och avgifter",
    "8430": "Valutakursdifferenser på skulder",
    "8811": "Avsättning till periodiseringsfond",
    "8819": "Återföring från periodiseringsfond",
    "8850": "Förändring av överavskrivningar",
    "8910": "Skatt på årets resultat",
    "8999": "Årets resultat",
}

# Transaction description fixes (corrupted -> correct UTF-8)
DESCRIPTION_FIXES = {
    # Månadsavgift patterns
    "M?nadsavgift": "Månadsavgift",
    "M\x94nadsavgift": "Månadsavgift",
    "Månadsavgift": "Månadsavgift",
    
    # Överföring patterns
    "?verf?ring": "Överföring",
    "\x99verf\x94ring": "Överföring",
    "Överföring": "Överföring",
    "Overforing": "Överföring",
    
    # Försäkring patterns
    "F?rs?kring": "Försäkring",
    "F\x94rs\x84kring": "Försäkring",
    
    # Förseningsavgift patterns
    "f?rseningsavgift": "förseningsavgift",
    "f\x94rseningsavgift": "förseningsavgift",
    
    # Mälardalstrafiken patterns
    "M?LARDALSTRAFIKKEN": "MÄLARDALSTRAFIKEN",
    "MALARDALSTRAFIKKEN": "MÄLARDALSTRAFIKEN",
    "Malardalstrafik": "Mälardalstrafik",
    "M?lardalstrafik": "Mälardalstrafik",
    
    # Ränta patterns
    "R?nta": "Ränta",
    "R\x84nta": "Ränta",
    
    # Tåg patterns
    "T?g": "Tåg",
    "T\x86g": "Tåg",
    
    # Örebro patterns
    "?rebro": "Örebro",
    "\x99rebro": "Örebro",
    
    # Marknadsföring patterns
    "Marknadsf?ring": "Marknadsföring",
    "Marknadsf\x94ring": "Marknadsföring",
    
    # Göteborg patterns
    "G?teborg": "Göteborg",
    "G\x94teborg": "Göteborg",
    
    # Malmö patterns
    "Malm?": "Malmö",
    "Malm\x94": "Malmö",
    
    # Inköp patterns
    "Ink?p": "Inköp",
    "Ink\x94p": "Inköp",
    
    # Återbetalning patterns
    "?terbetalning": "Återbetalning",
    "\x8Fterbetalning": "Återbetalning",
    
    # Företag patterns
    "F?retag": "Företag",
    "F\x94retag": "Företag",
    
    # Försäljning patterns
    "F?rs?ljning": "Försäljning",
    "F\x94rs\x84ljning": "Försäljning",
    
    # Bokföring patterns
    "Bokf?ring": "Bokföring",
    "Bokf\x94ring": "Bokföring",
}

def fix_konto_line(line):
    """Fix #KONTO lines with correct Swedish account names."""
    match = re.match(r'^#KONTO\s+(\d+)\s+".*"', line)
    if match:
        account_num = match.group(1)
        if account_num in ACCOUNT_NAMES:
            return f'#KONTO {account_num} "{ACCOUNT_NAMES[account_num]}"'
    return line

def fix_description(text):
    """Fix corrupted Swedish characters in text."""
    result = text
    for corrupted, correct in DESCRIPTION_FIXES.items():
        result = result.replace(corrupted, correct)
    
    # Additional single-character fixes
    replacements = [
        ('?', 'ä'),   # Most common - ä becomes ?
        ('\x94', 'ö'),
        ('\x84', 'ä'),
        ('\x86', 'å'),
        ('\x8F', 'Å'),
        ('\x99', 'Ö'),
        ('\x9A', 'Ü'),
    ]
    
    # Only apply single-char fixes if they make sense in Swedish context
    # This is handled by the DESCRIPTION_FIXES dict above
    
    return result

def fix_ver_line(line):
    """Fix #VER lines with transaction descriptions."""
    # Match #VER pattern: #VER A 841 20251001 "Description"
    match = re.match(r'^(#VER\s+\w+\s+\d+\s+\d+\s+)"(.+)"(.*)$', line)
    if match:
        prefix = match.group(1)
        description = match.group(2)
        suffix = match.group(3)
        
        # Fix the description
        fixed_desc = fix_description(description)
        return f'{prefix}"{fixed_desc}"{suffix}'
    return line

def process_file(filepath):
    """Process a single SIE file."""
    print(f"Processing: {filepath}")
    
    # Try multiple encodings to read the file
    content = None
    for encoding in ['utf-8', 'iso-8859-1', 'cp437', 'cp1252']:
        try:
            with open(filepath, 'r', encoding=encoding, errors='replace') as f:
                content = f.read()
            break
        except:
            continue
    
    if content is None:
        print(f"  ERROR: Could not read file")
        return False
    
    lines = content.split('\n')
    fixed_lines = []
    fixes_made = 0
    
    # Ensure proper header
    has_format = False
    
    for line in lines:
        original = line
        
        # Check for FORMAT line
        if line.startswith('#FORMAT'):
            has_format = True
            fixed_lines.append('#FORMAT ISO')
            continue
        
        # Fix PROGRAM line that might have FORMAT concatenated
        if '#PROGRAM' in line and '#FORMAT' in line:
            parts = line.split('#FORMAT')
            fixed_lines.append(parts[0].rstrip())
            fixed_lines.append('#FORMAT ISO')
            has_format = True
            fixes_made += 1
            continue
        
        # Add FORMAT after FLAGGA if not present
        if line.startswith('#FLAGGA') and not has_format:
            fixed_lines.append(line)
            fixed_lines.append('')
            continue
        
        # Fix #KONTO lines
        if line.startswith('#KONTO'):
            fixed_line = fix_konto_line(line)
            if fixed_line != original:
                fixes_made += 1
            fixed_lines.append(fixed_line)
            continue
        
        # Fix #VER lines
        if line.startswith('#VER'):
            fixed_line = fix_ver_line(line)
            if fixed_line != original:
                fixes_made += 1
            fixed_lines.append(fixed_line)
            continue
        
        fixed_lines.append(line)
    
    # Ensure FORMAT ISO is present after FLAGGA
    if not has_format:
        for i, line in enumerate(fixed_lines):
            if line.startswith('#FLAGGA'):
                fixed_lines.insert(i + 1, '')
                fixed_lines.insert(i + 2, '#PROGRAM "Spiris Bokföring & Fakturering" 7.5.0.0')
                fixed_lines.insert(i + 3, '#FORMAT ISO')
                break
    
    # Build final content - UTF-8 strings internally
    final_content = '\n'.join(fixed_lines)
    
    # Replace any replacement characters (from bad reads) with ?
    final_content = final_content.replace('\ufffd', '?')
    
    # Clean any remaining unencodable characters
    try:
        # Test encode first
        final_content.encode('iso-8859-1')
    except UnicodeEncodeError:
        # Replace any remaining unencodable chars
        clean_content = []
        for char in final_content:
            try:
                char.encode('iso-8859-1')
                clean_content.append(char)
            except UnicodeEncodeError:
                clean_content.append('?')
        final_content = ''.join(clean_content)
    
    # Write as ISO-8859-1 for Visma
    with open(filepath, 'w', encoding='iso-8859-1', newline='\n') as f:
        f.write(final_content)
    
    print(f"  Fixed {fixes_made} issues, saved as ISO-8859-1")
    return True

def main():
    """Main function to process all SE files."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all .se files
    se_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip .git and .venv directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.venv', '__pycache__']]
        for file in files:
            if file.lower().endswith('.se'):
                se_files.append(os.path.join(root, file))
    
    print(f"Found {len(se_files)} SE files")
    print("=" * 60)
    
    success = 0
    failed = 0
    
    for filepath in se_files:
        if process_file(filepath):
            success += 1
        else:
            failed += 1
    
    print("=" * 60)
    print(f"COMPLETE: {success} files fixed, {failed} failed")
    print()
    print("Output encoding: ISO-8859-1 with #FORMAT ISO")
    print("Swedish characters: å=0xE5, ä=0xE4, ö=0xF6")

if __name__ == "__main__":
    main()
