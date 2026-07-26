import utils

cv = utils.loadYaml('cv.yaml')

print('\n# Grants\n')
utils.listSortedItems(cv['grants'])

print('\n# Awards\n')
utils.listSortedItems(cv['awards'])

print('\n# Presentations\n')
utils.listSortedItems(cv['presentations'])

print('\n# Supervision\n')
utils.listSortedItems(cv['supervision'])

print('\n# Teaching\n')
utils.listSortedItems(cv['teaching'])

print('\n# Responsabilities\n')
utils.listSortedItems(cv['responsabilities'])

print('\n# Reviews\n')
revs = utils.loadYaml('reviews.yaml')
utils.summarizeReviews(revs)

print('\n# Misc\n')
utils.listSortedItems(cv['misc'])

print('\n# Softwares\n')
utils.listSortedItems(cv['softwares'])

print('\n# Publications\n')
pubs = utils.loadPublications('pubs.yaml')
utils.listSortedPubs(pubs, first_initial=True, last_first=False,
                     inc_doi=True, max_middle_authors=5)
