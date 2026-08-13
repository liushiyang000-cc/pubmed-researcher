Title: How I Built a Python Tool to Save Medical Researchers 10+ Hours Per Week

I am a neurointervention neurology fellow and PhD candidate at Universiti Malaysia Sabah.
Every day, I read 20-50 PubMed papers. Every week, I spend 15+ hours on literature reviews.
So I built a tool to automate the boring parts.

Introducing: PubMed Researcher
github.com/liushiyang000-cc/pubmed-researcher

What it does:
Search PubMed, extract structured data, analyze trends - all in Python.

Why I built it:
- Systematic reviews take weeks of manual searching
- Most researchers don't know how to use PubMed APIs
- Paper screening is repetitive and time-consuming

The tool handles:
1. Search: Query PubMed with date filters, article types
2. Extract: Get titles, authors, abstracts, PMCID automatically
3. Analyze: Publication trends, journal distribution, keyword frequency
4. Full text: Retrieve PMC open-access papers

Quick example:
papers = searcher.search("metabolomics ischemic stroke", retmax=20)
print(analyzer.summarize())

In 3 seconds, you get 20 papers with full metadata.
No more manual copy-pasting from PubMed.

I use this daily for my own research.
It handles my metabolomics + stroke projects.
And now I'm opening it to the community.

Try it:
pip install requests
python -m pubmed_researcher.cli "your search query" --retmax 10

If you find bugs or have feature requests, open an issue on GitHub.
I also welcome collaborators.

I am also offering medical research services:
- Literature reviews: -200
- SCI paper editing: -200
- Multi-omics analysis: -500

Let me know what you think!
#AcademicTwitter #MedicalResearch #Python #PubMed #OpenSource
