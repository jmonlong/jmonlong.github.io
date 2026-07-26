import yaml
from utils import Article

# read curated yaml
with open('pubs.yaml', 'rt') as inf:
    pubs = yaml.safe_load(inf)
arts = {}
for pub in pubs:
    art = Article()
    art.importYaml(pub)
    pid = '{}_{}'.format(pub['title'], pub['journal'])
    arts[pid] = art

# read openalex yaml
with open('pubs.openalex.yaml', 'rt') as inf:
    pubs_oa = yaml.safe_load(inf)

# record the fields to potentially add
new_pids = []
for pub in pubs_oa:
    pid = '{}_{}'.format(pub['title'], pub['journal'])
    if pid not in arts:
        art = Article()
        art.importYaml(pub)
        arts[pid] = art
        new_pids.append(pid)
    else:
        art = arts[pid]
        # update pmid?
        if art.pmid is None and 'pmid' in pub:
            art.pmid = pub['pmid']
        # update doi?
        if art.doi is None and 'doi' in pub:
            art.doi = pub['doi']
        # update type?
        if art.type is None and 'type' in pub:
            art.type = pub['type']
        # update authors?
        for pos, auth in enumerate(art.authors):
            if pos == 0:
                auth.position = 'first'
            elif pos == len(art.authors) - 1:
                auth.position = 'last'
            else:
                auth.position = 'middle'

# write new yaml
for pub in pubs:
    pid = '{}_{}'.format(pub['title'], pub['journal'])
    arts[pid].printYaml()
    print()
for pid in new_pids:
    arts[pid].printYaml()
    print()
