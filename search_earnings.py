import urllib.request, urllib.parse, re

queries = [
    'best freelance platforms medical writing 2026',
    'passive income ideas doctors researchers',
    'high paying side gigs medical professionals',
    'best platforms make money online 2026',
    'reddit ways to make money as researcher',
]

for query in queries:
    encoded = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            results = re.findall(r'result__a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
            print(f'--- {query} ---')
            for link, title in results[:8]:
                clean = re.sub(r'<[^>]+>', '', title)[:60]
                print(f'  {clean} -> {link}')
            print()
    except Exception as e:
        print(f'Error {query}: {e}')
