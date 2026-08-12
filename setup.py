from setuptools import setup, find_packages
setup(
    name="pubmed-researcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["pubmed-researcher=pubmed_researcher.cli:main"]},
)
