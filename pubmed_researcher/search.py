# -*- coding: utf-8 -*-
import requests
from typing import List, Dict, Optional
import xml.etree.ElementTree as ET

class PubMedSearch:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "PubMedResearcher/0.1.0 (academic; contact@example.com)"})
    
    def search(self, query, retmax=20, sort="relevance", date_range=None):
        params = {"db": "pubmed", "term": query, "retmax": retmax, "retmode": "json", "sort": sort}
        if date_range:
            params["datetype"] = "pdat"
            parts = date_range.split("-")
            params["mindate"], params["maxdate"] = parts[0], parts[1]
        resp = self.session.get(f"{self.BASE_URL}/esearch.fcgi", params=params)
        data = resp.json()
        ids = data.get("esearchresult", {}).get("idlist", [])
        return self._fetch_details(ids) if ids else []
    
    def _fetch_details(self, ids):
        ids_str = ",".join(ids[:200])
        resp = self.session.get(f"{self.BASE_URL}/efetch.fcgi", params={"db": "pubmed", "id": ids_str, "retmode": "xml", "rettype": "abstract"})
        return self._parse_xml(resp.content)
    
    def _parse_xml(self, xml_bytes):
        papers = []
        try:
            root = ET.fromstring(xml_bytes)
            for paper in root.findall(".//PubmedArticle"):
                article = paper.find(".//Article")
                pid = paper.find(".//PMID").text if paper.find(".//PMID") is not None else ""
                title = ""
                if article is not None:
                    t = article.find(".//Title")
                    if t is not None: title = t.text or ""
                authors = []
                if article is not None:
                    for a in article.findall(".//Author"):
                        ln = a.find("LastName").text if a.find("LastName") is not None else ""
                        fn = a.find("ForeName").text if a.find("ForeName") is not None else ""
                        authors.append(f"{fn} {ln}" if fn else ln)
                journal = ""
                if article is not None:
                    j = article.find(".//Journal/Title")
                    if j is not None: journal = j.text or ""
                year = ""
                if article is not None:
                    y = article.find(".//PubDate/Year")
                    if y is not None: year = y.text or ""
                abst = ""
                if article is not None:
                    ab = article.find(".//Abstract/AbstractText")
                    if ab is not None and ab.text: abst = ab.text[:500]
                pmc = ""
                pmc_elem = paper.find(".//PMC")
                if pmc_elem is not None: pmc = pmc_elem.text or ""
                papers.append({
                    "pmid": pid, "pmcid": pmc, "title": title,
                    "authors": authors[:5], "journal": journal,
                    "year": year, "abstract": abst,
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pid}/"
                })
        except Exception as e:
            print(f"Parse error: {e}")
        return papers
    
    def citation_count(self, query):
        resp = self.session.get(f"{self.BASE_URL}/esearch.fcgi", params={"db": "pubmed", "term": query, "retmax": 0, "retmode": "json"})
        return int(resp.json().get("esearchresult", {}).get("count", 0))
    
    def related_articles(self, pmid, retmax=10):
        resp = self.session.get(f"{self.BASE_URL}/elink.fcgi", params={"dbfrom": "pubmed", "db": "pubmed", "linkname": "pubmed_pubmed_references", "id": pmid, "retmax": retmax, "retmode": "json"})
        refs = resp.json().get("eLinkResult", {}).get("LinkSetDb[0]", {}).get("Link", [])
        ids = [ref["Id"] for ref in refs]
        return self._fetch_details(ids) if ids else []
