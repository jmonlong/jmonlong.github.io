# Get publication info for all articles

```sh
source venv/bin/activate

rm -f pubs.openalex.yaml
for DOI in `cat all.dois.txt`
do
    echo $DOI
    python3 get_openalex_info.py -d $DOI -c >> pubs.openalex.yaml
done
```

Then edit and save to a different file, for example `pubs.yaml`.

- Check for warning with names and fix manually (for now)
- Add more fields
    - *preprintdoi* if there was a preprint
    - *pressurl* if I made a page on the website to gather press coverage
    - *scripts* if there is a repo associated with the article
    - *pmid* if there is a PMC article? (maybe a better way to do this automatically)
- Update first/last if there are co-authorships.

## Adding a new publication

```sh
python3 get_openalex_info.py -d 10.64898/2026.07.21.739710 -c
```

Add to the end of `pubs.yaml` and check as above


## For the website

- Change the home page to use the yaml
    - don't include preprint if published
