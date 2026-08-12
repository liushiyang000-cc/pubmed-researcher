# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET

class PubMedExtractor:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "PubMedResearcher/0.1.0"})
    
    def get_full_text(self, pmcid):
        if not pmcid: return ""
        resp = self.session.get(f"{self.BASE_URL}/efetch.fcgi", params={"db": "pmc", "id": pmcid, "retmode": "xml"})
        return resp.text[:50000]
    
    def get_citations(self, pmid):
        resp = self.session.get(f"{self.BASE_URL}/elink.fcgi", params={"dbfrom": "pubmed", "db": "pubmed", "linkname": "pubmed_pubmed_citedin", "id": pmid})
        links = resp.json().get("eLinkResult", {}).get("LinkSetDb[1]", {}).get("Link", [])
        return len(links)
    
    def get_keywords(self, pmid):
        resp = self.session.get(f"{self.BASE_URL}/efetch.fcgi", params={"db": "pubmed", "id": pmid, "retmode": "xml", "rettype": "abstract"})
        keywords = []
        try:
            root = ET.fromstring(resp.text)
            for mesh in root.findall(".//MeshHeading"):
                term = mesh.find(".//DescriptorName")
                if term is not None: keywords.append(term.text)
        except: pass
        return keywords
