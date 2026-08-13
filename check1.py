import urllib.request, re
url = 'https://github.com/features/coplotit'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        text = re.sub(r'<[^>]+>', ' ', html)
        text = re.sub(r'\s+', ' ', text).strip()
        for s in text.split('.'):
            low = s.lower()
            if any(k in low for k in ['free','trial','student','education','30']):
                if len(s.strip()) > 20: print(s.strip()[:150])
except Exception as e: print(f'Error: {e}')