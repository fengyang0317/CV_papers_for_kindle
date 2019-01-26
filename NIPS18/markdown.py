from urllib2 import Request
from urllib2 import urlopen
import re
from tqdm import tqdm


c = re.compile('<li><a href="(/paper/[^"]*)">')
req = Request('https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018', headers={'User-Agent': "Magic Browser"})
f = urlopen(req)
html = f.read()
f.close()
html = html.decode("utf-8")
paper_urls = c.findall(html)

c = re.compile('<p class="abstract">([^<]*)</p>')
a = re.compile('<meta name="citation_author" content="([^"]*)">')
t = re.compile('<meta name="citation_title" content="([^"]*)">')
out = open('NIPS18.md', 'w')
out.write('% NIPS18\n\n')

for i in tqdm(paper_urls):
  req = Request('https://papers.nips.cc/' + i, headers={'User-Agent': "Magic Browser"})
  f = urlopen(req)
  html = f.read()
  f.close()
  abs = c.findall(html)
  authors = a.findall(html)
  title = t.findall(html)
  out.write('### ' + title[0] + '\n\n')
  out.write('**' + ', '.join(authors) + '**\n\n')
  out.write(abs[0] + '\n\n')

out.close()
