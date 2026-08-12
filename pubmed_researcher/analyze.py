# -*- coding: utf-8 -*-
from typing import List, Dict
from collections import Counter
import re

class PubMedAnalyzer:
    def __init__(self, papers):
        self.papers = papers
    
    def publication_trend(self):
        years = Counter(p.get("year", "") for p in self.papers if p.get("year"))
        return dict(sorted(years.items()))
    
    def journal_distribution(self):
        journals = Counter(p.get("journal", "") for p in self.papers if p.get("journal"))
        return dict(journals.most_common(10))
    
    def author_frequency(self):
        all_authors = []
        for p in self.papers:
            all_authors.extend(p.get("authors", []))
        return dict(Counter(all_authors).most_common(10))
    
    def keyword_extraction(self, min_freq=2):
        words = Counter()
        stop_words = {"the", "and", "of", "in", "for", "to", "a", "is", "are", "was", "were", "with", "this", "that", "from", "by", "on", "at"}
        for p in self.papers:
            text = (p.get("title", "") + " " + p.get("abstract", "")).lower()
            tokens = re.findall(r"[a-z]+", text)
            words.update(w for w in tokens if len(w) > 3 and w not in stop_words)
        return [w for w, c in words.most_common(20) if c >= min_freq]
    
    def summarize(self):
        lines = [f"## PubMed Analysis Report ({len(self.papers)} papers)", ""]
        years = self.publication_trend()
        if years:
            lines.append("### Publication Years")
            for y, c in sorted(years.items(), key=lambda x: x[0]):
                lines.append(f"- {y}: {c} papers")
            lines.append("")
        journals = self.journal_distribution()
        if journals:
            lines.append("### Top Journals")
            for j, c in journals.items():
                lines.append(f"- {j}: {c} papers")
            lines.append("")
        keywords = self.keyword_extraction()
        if keywords:
            lines.append("### Key Keywords")
            lines.append(", ".join(keywords))
        return "\n".join(lines)
