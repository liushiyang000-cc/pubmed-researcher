# -*- coding: utf-8 -*-
from pubmed_researcher import PubMedSearch, PubMedAnalyzer

if __name__ == "__main__":
    searcher = PubMedSearch()
    papers = searcher.search("metabolomics ischemic stroke", retmax=5, date_range="2024/01/01-2026/08/01")
    print(f"Found {len(papers)} papers")
    for p in papers:
        print(f"  [{p["year"]}] {p["title"]}")
        print(f"    {p["journal"]} | PMID: {p["pmid"]}")
