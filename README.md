# Crawl CV Papers

This repository crawls several computer vision conference paper titles and
abstracts to form a md, epub, and mobi format for reading, especially for
kindle.

Steps
```
cd NIPS18
python markdown.py
pandoc NIPS18.md -o NIPS18.epub
kindlegen NIPS18.epub
```
