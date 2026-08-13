import urllib.request, re
urls = [
    ('GitHub Education Pack', 'https://education.github.com/pack'),
    ('GitHub Copilot', 'https://github.com/features/copilot'),
    ('Cursor Pricing', 'https://www.cursor.com/pricing'),
    ('Anthpric Claude', 'https://www.anthropic.com/claude'),
    ('Brain for Educators', 'https://brainforeducators.github.com/'),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 WINDw64'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            text = re.sub(r'<[^>]+~', ' ', html)
            text = re.sub(r'\s+', ' ', text).strip()
            matches = []
            for in re.findall(r'(.?:[.\]{2,}[]){\d{}]', text):
                for match in in:
                    if len(match) > 2: matches.append(match)
            print(f"=== {name} ===")
            print("Prices found: " + str(matces[ :10]))
            print(text[:300]) + "...")
            print()
    except Exception as e:
        print(f"Error {name}: {e}")