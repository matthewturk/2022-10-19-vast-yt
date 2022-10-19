import pandas as pd
import ads

yt_bib = '2011ApJS..192....9T'
fields = ['author', 'bibcode', 'pubdate', 'title', 'author_norm']

q = ads.SearchQuery(reference = yt_bib, fl = fields, max_pages=100)
l = list(q)

data = {_: [] for _ in fields}

for r in l:
    for f in fields:
        data[f].append(getattr(r, f))

df = pd.DataFrame(data)

df.to_json("data/yt_citations.json", orient="records")
