# PubMed Researcher

> A Python toolkit for medical literature research, built on PubMed E-utilities API.

## Features

- Search PubMed with advanced filters (date range, article type)
- Extract structured data (titles, authors, abstracts, PMCID)
- Analyze publication trends, journal distribution, keyword frequency
- Retrieve PMC full-text articles
- Track citation counts and related articles
- CLI tool for quick command-line searches

## Installation

`ash
pip install requests
# Or from source:
pip install -e .
`

## Quick Start

`python
from pubmed_researcher import PubMedSearch, PubMedAnalyzer

searcher = PubMedSearch()
papers = searcher.search("metabolomics ischemic stroke", retmax=20, date_range="2024/01/01-2026/08/01")

for p in papers[:5]:
    print(f"[{p['year']}] {p['title']}")
    print(f"  {p['journal']} | {p['url']}")

analyzer = PubMedAnalyzer(papers)
print(analyzer.summarize())
`

## CLI Usage

`ash
# Search and print
python -m pubmed_researcher.cli "ischemic stroke metabolomics" --retmax 10

# JSON output
python -m pubmed_researcher.cli "stroke" --json --retmax 5

# With analysis
python -m pubmed_researcher.cli "metabolomics" --analyze --retmax 30
`

## Use Cases

- Literature review and paper survey
- Systematic review seed identification
- Research gap analysis via keyword extraction
- Grant writing background research
- Teaching reading list preparation

## License

MIT License

## Author

lousiyue - Medical researcher, neurointervention fellow, UM Sabah PhD candidate
