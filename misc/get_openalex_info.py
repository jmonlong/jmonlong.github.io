import json
import sys
import os
import argparse
import pyalex
# https://github.com/J535D165/pyalex
from utils import Article


parser = argparse.ArgumentParser()
parser.add_argument('-d', help='DOI')
parser.add_argument('-c', help='use cache json file',
                    action='store_true')
args = parser.parse_args()


# try to read cache
if not os.path.exists('cache.openalex.json'):
    init_f = open('cache.openalex.json', 'wt')
    init_f.write('{}')
    init_f.close()
with open('cache.openalex.json', 'rt') as cache_inf:
    cache = json.load(cache_inf)

# is this DOI already in the cache?
in_cache = False
for doi in cache:
    if doi == args.d:
        in_cache = True

# either use the cache or the OpenAlex API
w = None
if args.c and in_cache:
    print('Reading from cache...', file=sys.stderr)
    w = cache[args.d]
else:
    print('Querying OpenAlex...', file=sys.stderr)
    w = pyalex.Works()["https://doi.org/" + args.d]
    cache[args.d] = w

# update cache
if not in_cache:
    with open('cache.openalex.json', 'wt') as cache_outf:
        json.dump(cache, cache_outf)

# w = pyalex.Works()["https://doi.org/" + '10.1158/1078-0432.CCR-20-1439']
# format using Article/Author class and write yaml
art = Article()
art.importOpenAlex(w)
# art.print()
# art.print(first_initial=True, last_first=True)
art.printYaml()
print()
