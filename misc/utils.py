import sys
import yaml
import datetime


class Author:
    def __init__(self):
        self.display_name = ''
        self.oa_id = ''
        self.position = ''
        self.firstname = None
        self.lastname = ''
        self.middle = None

    def importOpenAlex(self, auth):
        self.display_name = auth['display_name']
        # remove special characters
        self.display_name = self.display_name.replace(' ', '')
        self.display_name = self.display_name.replace('', '')
        # openalex ID
        self.oa_id = auth['id']
        # guess first/last name
        name = self.display_name.split(' ')
        self.firstname = name[0]
        self.lastname = name[-1]
        self.middle = None
        if len(name) > 2:
            # try to handle this long name
            # remove lastname
            name.pop()
            # try to remove de/der
            if name[-1].lower() in ['de', 'der', '’t']:
                self.lastname = name[-1] + ' ' + self.lastname
                name.pop()
            # now van/von, or mc
            if name[-1].lower() in ['van', 'von', 'mc']:
                self.lastname = name[-1] + ' ' + self.lastname
                name.pop()
            # if remaining are all initials, concatenate them
            all_initials = True
            for ii in range(1, len(name)):
                if len(name[ii].replace('.', '')) > 1:
                    all_initials = False
            # set best guess for a middle name
            if all_initials:
                self.middle = ''.join(name[1:])
            else:
                self.middle = ' '.join(name[1:])
            # show a warning
            warn = 'Long name warning: {} -> {} | {} | {}.'
            print(warn.format(self.display_name, self.firstname,
                              self.middle, self.lastname), file=sys.stderr)

    def importYaml(self, auth):
        if 'firstname' in auth:
            self.firstname = auth['firstname']
        self.lastname = auth['lastname']
        if 'middle' in auth:
            self.middle = auth['middle']
        self.position = auth['position']

    def toStr(self, first_initial=False, last_first=False):
        if self.firstname is None:
            return self.lastname
        firstname = self.firstname
        if self.middle is not None:
            firstname += ' ' + self.middle
        if first_initial:
            firstname = self.firstname[0]
            if self.middle is not None:
                firstname += self.middle.replace('.', '')
        lastname = self.lastname
        if last_first:
            return lastname + ' ' + firstname
        else:
            return firstname + ' ' + lastname


class Article:
    def __init__(self):
        # general information
        self.title = ''
        self.doi = None
        self.type = None
        self.journal = ''
        self.journal_id = ''
        self.year = ''
        self.url = ''
        self.ncited = ''
        self.pmid = None
        self.pressurl = None
        self.scripts = None
        self.preprintdoi = None
        # authors
        self.authors = []

    def importOpenAlex(self, work):
        # general information
        self.title = work['title']
        self.doi = work['doi'].replace('https://doi.org/', '')
        self.type = work['type']
        self.journal = work['primary_location']['source']['display_name']
        if self.journal == "bioRxiv (Cold Spring Harbor Laboratory)":
            self.journal = 'bioRxiv'
        self.journal_id = work['primary_location']['source']['id']
        self.year = work['publication_year']
        self.url = work['doi']
        self.ncited = work['cited_by_count']
        self.pmid = None
        if 'ids' in work and 'pmid' in work['ids']:
            self.pmid = work['ids']['pmid']
            self.pmid = self.pmid.replace('https://pubmed.ncbi.nlm.nih.gov/',
                                          '')
        # authors
        self.authors = []
        for pos, auth_d in enumerate(work['authorships']):
            auth = Author()
            auth.importOpenAlex(auth_d['author'])
            if pos == 0:
                auth.position = 'first'
            elif pos == len(self.authors) - 1:
                auth.position = 'last'
            else:
                auth.position = 'middle'
            self.authors.append(auth)

    def importYaml(self, work):
        # general information
        self.title = work['title']
        if 'doi' in work:
            self.doi = work['doi']
        if 'type' in work:
            self.type = work['type']
        self.journal = work['journal']
        self.year = work['year']
        self.url = work['url']
        self.ncited = work['ncited']
        if 'pmid' in work:
            self.pmid = work['pmid']
        if 'pressurl' in work:
            self.pressurl = work['pressurl']
        if 'scripts' in work:
            self.scripts = work['scripts']
        if 'preprintdoi' in work:
            self.preprintdoi = work['preprintdoi']
        # authors
        for auth_d in work['authors']:
            auth = Author()
            auth.importYaml(auth_d)
            self.authors.append(auth)

    def print(self, first_initial=False, last_first=False):
        print('{}'.format(self.title))
        authors = []
        for auth in self.authors:
            authors.append(auth.toStr(first_initial, last_first))
        print(', '.join(authors))
        print('{} ({})'.format(self.journal, self.year))
        print('Cited: {}. {}'.format(self.ncited, self.url))

    def printYaml(self):
        # start as an element of an array
        print('- title: "{}"'.format(self.title))
        print('  doi: {}'.format(self.doi))
        print('  type: {}'.format(self.type))
        print('  journal: "{}"'.format(self.journal))
        print('  year: {}'.format(self.year))
        print('  url: "{}"'.format(self.url))
        print('  ncited: {}'.format(self.ncited))
        if self.pmid is not None:
            print('  pmid: {}'.format(self.pmid))
        if self.scripts is not None:
            print('  scripts: {}'.format(self.scripts))
        if self.pressurl is not None:
            print('  pressurl: {}'.format(self.pressurl))
        if self.preprintdoi is not None:
            print('  preprintdoi: {}'.format(self.preprintdoi))
        print('  authors:')
        for auth in self.authors:
            print('    - lastname: ' + auth.lastname)
            if auth.firstname is not None:
                print('      firstname: ' + auth.firstname)
            if auth.middle is not None:
                print('      middle: ' + auth.middle)
            print('      position: ' + auth.position)

    def toMdStr(self, first_initial=False, last_first=False, inc_doi=True,
                max_middle_authors=0):
        authors = []
        mid_auths = 0
        skipped_auths = False
        auths_done = set()
        # are there multiple first/last authors?
        nfirst = 0
        nlast = 0
        for auth in self.authors:
            if auth.position == 'first':
                nfirst += 1
            if auth.position == 'last':
                nlast += 1
        # format each author
        for auth in self.authors:
            auth_id = '{} {}'.format(auth.firstname, auth.lastname)
            if auth_id in auths_done:
                continue
            else:
                auths_done.add(auth_id)
            # bold if my name
            a_f = '{}'
            if auth.lastname == "Monlong":
                a_f = '**{}**'
            # don't skip first, last, or me
            if (auth.position in ['first', 'last']
                    or auth.lastname == "Monlong"):
                if auth.position in ['first', 'last']:
                    mid_auths = 0
                # if we were skipping authours, add '...'
                if skipped_auths:
                    authors.append('...')
                    skipped_auths = False
            else:
                mid_auths += 1
            # check if we should skip middle authors
            if (auth.lastname != "Monlong"
                    and max_middle_authors > 0
                    and mid_auths > max_middle_authors):
                skipped_auths = True
                continue
            # add symbol for first/last authors if multiple
            if nfirst > 1 and auth.position == 'first':
                a_f = a_f.format('{}\\*')
            if nlast > 1 and auth.position == 'last':
                a_f = a_f.format('{}+')
            authors.append(a_f.format(auth.toStr(first_initial=first_initial,
                                                 last_first=last_first)))
        ostr = ', '.join(authors) + '. '
        # deal with italic words in the title
        title = self.title.replace('<i>', '*').replace('</i>', '*')
        ostr += title.rstrip('.') + '. '
        ostr += "*{}* {}. ".format(self.journal, self.year)
        if inc_doi:
            ostr += 'DOI: [{}]({})'.format(self.doi, self.url)
        return ostr


def loadYaml(yaml_fn):
    # read curated yaml
    with open(yaml_fn, 'rt') as inf:
        return yaml.safe_load(inf)


def loadPublications(yaml_fn):
    # read curated yaml
    with open(yaml_fn, 'rt') as inf:
        pubs_y = yaml.safe_load(inf)
    pubs = {}
    for pub in pubs_y:
        art = Article()
        art.importYaml(pub)
        pubs[art.doi] = art
    return pubs


def listSortedPubs(pubs, first_initial=True, last_first=False, inc_doi=True,
                   max_middle_authors=5):
    # sort by year
    doi_sorted = sorted(pubs, key=lambda k: pubs[k].year, reverse=True)

    # find published prepints
    published_preprint_dois = set()
    for doi in pubs:
        if pubs[doi].preprintdoi is not None:
            published_preprint_dois.add(pubs[doi].preprintdoi)
    
    # numbered list in markdown
    ii = 0
    for doi in doi_sorted:
        if doi in published_preprint_dois:
            continue
        art = pubs[doi]
        art_s = art.toMdStr(first_initial=first_initial,
                            last_first=last_first,
                            inc_doi=inc_doi,
                            max_middle_authors=max_middle_authors)
        print('{}. {}'.format(ii + 1, art_s))
        ii += 1


class Item:
    def __init__(self, info):
        self.date_start = None
        self.date_end = None
        self.date_upcoming = False
        if 'date' in info:
            self.setDate(info['date'])
        self.title = None
        if 'title' in info:
            self.title = info['title']
        self.event = None
        if 'event' in info:
            self.event = info['event']
        self.url = None
        if 'url' in info:
            self.url = info['url']
        self.location = None
        if 'location' in info:
            self.location = info['location']
        # funding section
        self.amount = None
        if 'amount' in info:
            self.amount = info['amount']
        self.institution = None
        if 'institution' in info:
            self.institution = info['institution']
        # supervision section
        self.name = None
        if 'first_name' in info:
            self.name = '{} {}'.format(info['first_name'],
                                       info['last_name'])
        self.role = None
        if 'role' in info:
            self.role = info['role']
        self.position = None
        if 'position' in info:
            self.position = info['position']
        # teaching section
        self.material = None
        if 'material' in info:
            self.material = info['material']
        # presentation type
        self.type = None
        if 'type' in info:
            self.type = info['type']

    def setDate(self, date_str):
        date = str(date_str)
        if '(upcoming)' in date:
            self.date_upcoming = True
            date = date.replace('(upcoming)', '')
        date = date.split('-')
        self.date_start = int(date[0])
        self.date_end = self.date_start
        if len(date) > 1:
            self.date_end = int(date[1])

    def __lt__(self, other):
        if self.date_start is None or other.date_start is None:
            return None
        return ((self.date_start < other.date_start)
                or (self.date_start == other.date_start
                    and (self.date_end < other.date_end
                         or (not self.date_upcoming and other.date_upcoming))))

    def printItem(self, item_id):
        # we'll try to use the URL but make sure only once
        url_done = False
        # start with date
        date = ''
        if self.date_start is not None:
            if self.date_start == self.date_end:
                date = self.date_start
            else:
                date = '{}-{}'.format(self.date_start,
                                      self.date_end)
            if self.date_upcoming:
                date = str(date) + ' (upcoming)'
            date = '*{}* - '.format(date)
        tstr = '{}. {}'.format(item_id, date)
        # add other information
        if self.location is not None:
            tstr += self.location + '. '
        # person's name and role (for supervision)
        if self.name is not None and self.position is not None:
            tstr += self.name + ', ' + self.position + '. '
        if self.role is not None:
            tstr += self.role + '. '
        # prepare institution
        inst_str = ''
        if self.institution is not None:
            # if there is an URL, make this an url?
            if self.url is not None:
                url_done = True
                inst_str = '[{}]({}). '.format(self.institution,
                                               self.url)
            else:
                inst_str = self.institution + '. '
        # general "title"
        title = ''
        if self.event is not None:
            title = self.event
            if self.url is not None:
                title = '[{}]({})'.format(self.event, self.url)
                url_done = True
            if self.title is not None:
                title = '{}. *{}*'. format(title, self.title.rstrip('.'))
        elif self.title is not None:
            title = self.title
            # if institution is mentioned in title, don't add it and
            # inject the link in the title
            if self.institution is not None and self.institution in title:
                inst_str = ''
                if self.url is not None:
                    url_inj = '[{}]({})'.format(self.institution, self.url)
                    title = title.replace(self.institution, url_inj)
                    url_done = True
            elif inst_str == '' and self.url is not None:
                url_done = True
                title = '[{}]({})'.format(self.title, self.url)
        if title != '':
            tstr += title + '. '
        # add institution info
        tstr += inst_str
        # URL or other links at the end.
        if not url_done and self.url is not None:
            tstr += self.url + '. '
        if self.material is not None:
            tstr += 'Material: ' + self.material + '. '
        # funding amount at the end too
        if self.amount is not None:
            amount = self.amount
            if amount >= 5000:
                amount = round(amount/1000)
                amount = str(amount) + ' k'
            tstr += str(amount) + ' euros. '
        # add type of item
        if (self.type is not None and
                (self.title is None or self.type not in self.title.lower())):
            type = self.type
            if type in ['oral', 'poster']:
                type += ' presentation'
            tstr += type.capitalize() + '. '
        # print formatted string
        print(tstr)


def listSortedItems(items_d):
    items = []
    for ii, item_d in enumerate(items_d):
        # filter unfunded grants
        if 'status' in item_d and item_d['status'] != 'funded':
            continue
        item = Item(item_d)
        items.append(item)
    # sort by start date, then end date
    items.sort(reverse=True)
    for ii, item in enumerate(items):
        # print in markdown format
        item.printItem(ii + 1)


def summarizeReviews(reviews_d):
    tot_rev = 0
    tot_rev_3 = 0
    tot_rev_j = {}
    cur_year = datetime.datetime.now().year
    for journal in reviews_d:
        cpt = 0
        for year in reviews_d[journal]:
            cpt += reviews_d[journal][year]
            if year >= cur_year - 3:
                tot_rev_3 += reviews_d[journal][year]
        tot_rev += cpt
        tot_rev_j[journal] = cpt
    journals_s = sorted(tot_rev_j, key=lambda k: tot_rev_j[k], reverse=True)
    journals_s = ['*{}*'.format(j) for j in journals_s]
    print('{} reviews for academic journals ({} in the past three years)'
          ': {}'.format(tot_rev, tot_rev_3, ', '.join(journals_s)))
