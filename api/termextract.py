#!//anaconda/bin/python
from topia.termextract import extract
from pprint import pprint

def get_matching_lines(text, term):
    text = text.lower()
    lines = parse_text(text)
    matching_lines = []
    for line in lines:
        if term in line:
            matching_lines.append(line)

    return set(matching_lines)

def parse_text(text):
    terms = get_terms(text)
    only_terms = []
    bterms = ['the', 'and', 'so', 'hence', 'analysis', 'approach'  ,  'area' ,   'assessment' , 'assume' , 'authority' ,  'available' ,  'benefit' ,'concept' ,'consistent' ,'constitutional' ,  'context', 'contract'  ,  'create',  'data'  ,  'definition' , 'derived', 'distribution' ,   'economic'   , 'environment', 'established', 'estimate' ,   'evidence',   'export' , 'factor'  ,'financial' ,  'formula', 'function'  ,  'identified' , 'income' , 'indicate' ,'individual' ,  'involved' ,   'issue'  , 'labour' , 'legal'  , 'legislation' ,'major'  , 'method'  ,'occur'  , 'percent', 'period'  ,'policy' , 'principle'  , 'procedure'  , 'process' ,'required'   , 'research'   , 'response'  ,  'role'  ,  'section', 'sector', 'significant' , 'similar' ,'source' , 'specific',    'structure'  , 'theory', 'variable']
    for term in terms:
        if len(term[0]) > 2: #Reject single/double character terms
            for bterm in bterms:
                if bterm != term[0]:
                    only_terms.append(term[0])

    #pprint(only_terms)
    shortened_text = []
    for line in text.split('.'):
        for term in only_terms:
            if term in line:
                shortened_text.append(line)
    return set(shortened_text)

def get_terms(text):
    extractor = extract.TermExtractor()
    terms = extractor(text)
    return terms

if __name__ == "__main__":
    text = ''
    with open('sample2') as f:
        text = f.read()
    shortened_text = parse_text(text)
    while(1):
        keyw = raw_input('Enter phrase: ')
        for text in shortened_text:
            if keyw in text[1]:
                print text
