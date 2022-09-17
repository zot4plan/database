import json
import common

invalid_words = set([
    'satisfaction', 'satisfactory', 'audition', 'year',
    'better', 'below', 'grade', 'minimum', 'score', 'scores',
    'recommended:','recommemded', 'requirement', 'credit']) 

valid_words = set([
    'sat', 'act', 'ap', 
    'placement', 
    'beh', 
    'psy'
])

replace_words = {
    'PHYS': 'PHYSICS', 
    'ICS': 'I&C SCI', 
    'CS': 'COMPSCI',
    'SE': 'SOCECOL',
    'CEE': 'ENGRCEE',
    'MAE': 'ENGRMAE',
    'STAT': 'STATS',
    'PUBH': 'PUBHLTH',
    'PSYC': 'PSYCH',
    'PS': 'PHY SCI',
    'BIOL': 'BIO SCI',
    'IS': 'INTL ST',
    'ANTH': 'ANTHRO',
    'SOCL': 'SOCIOL',
    'SSCI': 'SOC SCI',
    'ESS': 'EARTHSS',
    'PHMS': 'PHRMSCI',
    'PHIL': 'PHILOS',
    'SPAN': 'SPANISH',
    'CLS': 'CRM/LAW'
}

def build_tree(sentence: str) -> dict:  
    if not sentence:
        return ''

    word = []
    conjunction = ""
    token = [] 
    tokens = [] 
    sentence_length = len(sentence)

    i = 0
    while i < sentence_length:
        # treat all words inside parentheses at a token
        if sentence[i] == '(':
            stack = [] 
            stack.append('(')
            i += 1
            while stack and i < sentence_length:
                if sentence[i] == '(':
                    stack.append('(')
                elif sentence[i] == ')':
                    stack.pop()

                if stack:
                    token.append(sentence[i])
                else:
                    valid_token = check_token("".join(token).split(' '))
                    if valid_token != '':
                        tokens.append(valid_token)
                    token = []
                i += 1  
        # check if word is a conjuction or part of a token
        elif sentence[i] == ' ' or sentence[i] == '.':
            if word:
                temp = "".join(word)
                if temp == "or" or temp == "and":
                    conjunction = temp
                    # Add token before conjunction
                    if token:
                        valid_token = check_token(token)
                        if valid_token:
                            tokens.append(valid_token)
                        token = []
                # Remove whole sentence if contain
                elif temp == "Recommended:" or temp == 'with':
                    while i < sentence_length and sentence[i] != '.':
                        i += 1
                    token = []
                elif sentence[i] == '.':
                    token.append(temp)
                    valid_token = check_token(token)
                    if valid_token:
                        tokens.append(valid_token)
                    token = []
                else:
                    token.append(temp)
                word = []
            i += 1
        # build word
        else:
            word.append(sentence[i])
            i += 1
    
    if word:
        token.append("".join(word))
        valid_token = check_token(token)
        if valid_token:
            tokens.append(valid_token)
    
    if not tokens:
        return ''

    if not conjunction:
        if "placement" in tokens[-1].lower():
            if len(tokens) > 1:
                conjunction = "or"
            else:
                conjunction = "and"
            tokens[-1] = "Placement exam"
        else:
            conjunction = "and"
    
    for i in range(len(tokens)):
        if ' or ' in tokens[i] or ' and ' in tokens[i]:
            tokens[i] = build_tree(tokens[i])
        elif 'placement' in tokens[i].lower():
            tokens[i] = 'Placement exam'

    tree = {conjunction: [token for token in tokens if token]}

    return tree

def check_token (words: list) -> str:
    for word in words:
        if word.lower() in invalid_words:
            return ''

    for word in words:
        w = word.lower()
        if w in valid_words:
            if w == 'placement':
                return 'Placement exam'   

            return " ".join(words).replace('higher on the ','')
    
    if len(words) < 4:
        for i in range(len(words)):
            if words[i] in replace_words:
                words[i] = replace_words[words[i]]

    token = " ".join(words)
    if (' or ' in token 
        or ' and ' in token
        or 'AP' in token 
        or token in common.course_ids
    ):
        return token
    else:
        return ''   

def filter_text(text: str) -> str:
    sentences = text.split('.')
    sentences = [s for s in sentences if not any( w in s.lower() for w in invalid_words)]
    if not sentences:
        return ''
    elif len(sentences) == 1:
        return sentences[0]
    else:
        return '. '.join(sentences)

def build_trees(file_path: str):
    types = ['prerequisite', 'corequisite', 'prerequisite_or_corequisite']
    for course_id, value in common.courses.items():         
        for type in types:
            common.courses[course_id][type + '_tree'] = build_tree(filter_text(value[type]))
            print(course_id + ' - ' + type)
            print(common.courses[course_id][type + '_tree'])
            print()
            
    for course_id, value in common.manually_changes.items():
        for type in types:
            if type in value:
                common.courses[course_id][type] = value[type]
            if (type + '_tree') in value:
                common.courses[course_id][type + '_tree'] = value[type + '_tree']

    with open(file_path, 'w') as f:
        json.dump(common.courses, f, indent=4)

    print('Done\n')
