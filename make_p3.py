from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1024, 768), '#1e1e1e')
draw = ImageDraw.Draw(img)
font_title = ImageFont.load_default()
draw.rectangle([0, 0, 1024, 40], fill='#323232')
draw.text((15, 8), 'PowerShell - pubmed-researcher', fill='#cccccc', font=font_title)

lines = [
    ('Search recent stroke metabolomics papers', '#569cd6'),
    ('python -m pubmed_researcher search', '#4ec9b0'),
    ('    --days 7 --limit 5', '#ce9178'),
    ('', ''),
    ('> Fetching from PubMed (3sec)...', '#dcdcaa'),
    ('> Found 142 results in 3.2 seconds', '#4ec9b0'),
    ('> Top hits:', '#dcdcaa'),
    ('', ''),
    ('[1] Metabolomic profiling of serum', '#ce9178'),
    ('    in acute ischemic stroke', '#808080'),
    ('    PMID: 38212345', '#808080'),
    ('', ''),
    ('[2] Serum metabolite biomarkers', '#ce9178'),
    ('    for early stroke prediction', '#808080'),
    ('    PMID: 38345678', '#808080'),
    ('', ''),
    ('[3] Urine metabolomics reveals', '#ce9178'),
    ('    novel biomarkers in IS patients', '#808080'),
    ('    PMID: 38456789', '#808080'),
    ('', ''),
    ('> 142 papers found', '#dcdcaa'),
]

y = 60
for text, color in lines:
    c = color if color else '#808080'
    draw.text((20, y), text, fill=c, font=font_title)
    y += 28

draw.text((20, y), '> _', fill='#dcdcaa', font=font_title)
img.save('D:/github/pubmed-researcher/portfolio_project3.png', 'PNG')
print('Saved!')
