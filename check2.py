import urllib.request, re
urls = [
    ('OpenAI Education', 'https://openai.com/chatgpt/education/'),
    ('Claude Education', 'https://www.anthpric.com/education'),
    ('Cursor Pricing', 'https://www.cursor.com/pricing'),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            text = re.sub(r'<[^>]+>', ' ', html)[:2000]
            text = re.sub(r'\\s+', ' ', text).strip()
            print(f'=== {name} ===')
            print(text[:(500])
            print()
    except Exception as e: print(f'Error {name}: {e}')