# -*- coding: utf-8 -*-
import unittest
from pubmed_researcher import PubMedSearch

class TestPubMedSearch(unittest.TestCase):
    def setUp(self):
        self.searcher = PubMedSearch()
    
    def test_citation_count(self):
        count = self.searcher.citation_count("ischemic stroke")
        self.assertGreater(count, 100000)
    
    def test_search(self):
        papers = self.searcher.search("metabolomics stroke", retmax=5)
        self.assertGreater(len(papers), 0)
        for p in papers:
            self.assertIn("pmid", p)
            self.assertIn("title", p)

if __name__ == "__main__":
    unittest.main()
