# -*- coding: utf-8 -*-
import argparse
import json
from .search import PubMedSearch
from .analyze import PubMedAnalyzer

def main():
    parser = argparse.ArgumentParser(description="PubMed Literature Research Tool")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--retmax", type=int, default=20)
    parser.add_argument("--date", help="Date range e.g. 2024-2026")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--analyze", action="store_true")
    args = parser.parse_args()
    
    searcher = PubMedSearch()
    date_range = f"{args.date.split(chr(45))[0]}/01/01-{args.date.split(chr(45))[1]}/12/31" if args.date else None
    papers = searcher.search(args.query, retmax=args.retmax, date_range=date_range)
    
    if args.json:
        print(json.dumps(papers, ensure_ascii=False, indent=2))
    else:
        for i, p in enumerate(papers, 1):
            print(f"{i}. [{p[chr(121)+chr(101)+chr(97)+chr(114)]}] {p[chr(116)+chr(105)+chr(116)+chr(108)+chr(101)]}")
            print(f"   {p[chr(106)+chr(111)+chr(117)+chr(114)+chr(110)+chr(97)+chr(108)]} | {p[chr(112)+chr(109)+chr(105)+chr(100)]}")
            print(f"   {p[chr(117)+chr(114)+chr(108)]}")
        if args.analyze and papers:
            analyzer = PubMedAnalyzer(papers)
            print("\n" + analyzer.summarize())

if __name__ == "__main__":
    main()
