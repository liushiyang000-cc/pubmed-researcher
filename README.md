# PubMed Researcher

> A Python toolkit for medical literature research, built on PubMed E-utilities API.

## Features

- **Search**: Query PubMed with advanced filters (date range, article type)
- **Extract**: Get structured data from papers (titles, authors, abstracts, PMCID)
- **Analyze**: Publication trends, journal distribution, keyword extraction
- **Full Text**: Retrieve PMC open-access full text
- **Citations**: Track citation counts and related articles
- **CLI**: Command-line tool for quick searches

## Installation

`ash
pip install requests
# Or from source:
pip install -e .
`

## Quick Start

`python
from pubmed_researcher import PubMedSearch, PubMedAnalyzer

# Search papers
searcher = PubMedSearch()
papers = searcher.search("metabolomics ischemic stroke", retmax=20, date_range="2024/01/01-2026/08/01")

# Print results
for p in papers[:5]:
    print(f"[{p['year']}] {p['title']}")
    print(f"  Journal: {p['journal']}")
    print(f"  URL: {p['url']}")

# Analyze
analyzer = PubMedAnalyzer(papers)
print(analyzer.summarize())
`

## CLI Usage

`ash
# Search from command line
python -m pubmed_researcher.cli "ischemic stroke metabolomics" --retmax 10 --date 2024-2026

# JSON output
python -m pubmed_researcher.cli "stroke" --json --retmax 5

# With analysis
python -m pubmed_researcher.cli "metabolomics" --analyze --retmax 30
`

## Use Cases

- **Literature Review**: Quick survey of recent papers on a topic
- **Systematic Review**: Seed paper identification and citation tracking
- **Research Gap Analysis**: Identify understudied areas via keyword extraction
- **Grant Writing**: Background research for proposals
- **Teaching**: Prepare reading lists for students

## Author

**lousiyang000-cc** ? Neurointervention neurology fellow, PhD candidate at Universiti Malaysia Sabah (UMS).

## Monetization & Services

- **GitHub Sponsors**: Support this project ? https://github.com/sponsors/liushiyang000-cc
- **Fiverr**: Medical literature review, SCI editing, PubMed data extraction
- **Upwork**: Medical research consulting, multi-omics analysis
- **Gumroad**: Premium templates and guides

## License

MIT License

## Citing

`ibtex
@misc{pubmed-researcher,
  title={PubMed Researcher: A Python Toolkit for Medical Literature Research},
  author={liushiyang000-cc},
  year={2026},
  url={https://github.com/liushiyang000-cc/pubmed-researcher}
}
`
