stemmed_word = {}

# Set the vowel letter for comparing purpose
vowel_set = ('A', 'I', 'U', 'O', 'E')
step_dec = {
    'SSES':'SS', 'IES':'I', 'SS':'SS', 'S':'',
    'EED':'ED', 'ED':'', 'ING':'',
    'AT':'ATE', 'BL':'BLE','IZ':'IZE',
    'Y':'I',
    'ATIONAL': 'ATE', 'TIONAL': 'TION', 'ENCI':'ENCE', 'ANCI':'ANCE', 'IZER':'IZE', 'ABLI':'ABLE', 'ALLI':'AL', 'ENTLI':'ENT', 'ELI':'E', 'OUSLI':'OUS', 'IZATION':'IZE',
    'ATION':'ATE', 'ATOR':'ATE', 'ALISM':'AL', 'IVENESS':'IVE', 'FULNESS':'FUL', 'OUSNESS':'OUS', 'ALITI':'AL', 'IVITI':'IVE', 'BILITI':'BLE',
    'ICATE':'IC', 'ATIVE':'', 'ALIZE':'AL', 'ICITI':'IC', 'ICAL':'IC', 'FUL':'', 'NESS':'',
    'AL':'', 'ANCE':'', 'ENCE':'', 'ER':'', 'IC':'', 'ABLE':'', 'IBLE':'', 'ANT':'', 'EMENT':'', 'MENT':'', 'ENT':'', 'ION':'',
    'OU':'', 'ISM':'', 'ATE':'', 'ITI':'', 'OUS':'', 'IVE':'', 'IZE':'',
    'E':''
}
def change(token, suffix, measure, vowel, position, step=0):
    mT, vT = 0,0
    if not measure:
        if not vowel:
            stemmed_word[suffix] = token.replace(suffix, step_dec[suffix])
            return stemmed_word[suffix]
        else:
            vT = v(token[:position])
            if vT > 0:
                return change(token, suffix, measure, False, position)
            return 0
    else:
        mT = m(token[:position])
        if step == 1 and mT > 0 or step == 2 and mT > 0 or step == 3 and mT > 0 or step == 4 and mT > 1:
            return change(token, suffix, False, vowel, position)
        return 0
# Checking if the token contian (Vowel Consonant), Return the m :: which m = the count of (Vowel Consonant)
def m(token):
    n = 0
    prv = None
    for char in token:
        if prv in vowel_set and char not in vowel_set:
            n+=1
        prv = char
    return n

# Checking if the token has a vowel on it, Return #False or #True
def v(token):
    n = 0
    for char in token:
        if char in vowel_set:
            return True
    return False

# CVC Checking, and checking it not end with 'W' or 'X' or 'Y', Return #False or #True
def cvc(token):
    prv, cur = None, None
    for t in token:
        if prv not in vowel_set and cur in vowel_set and t not in vowel_set:
            if t not in ['W', 'X', 'Y']:
                return True
        prv = cur
        cur = t
    return False

# Double Char checking, Return #False or #True
def doubleChar(token):
    if token[-2] == token [-1]:
        return True
    return False

def step1a(token):
    if token[-2:] == 'ES':
        if token[-4:] == 'SSES':
            change(token, 'SSES', False, False, -4)
        elif token[-3:] == 'IES':
            change(token, 'IES', False, False, -3)
    else:
        if token[-2:] == 'SS':
            change(token, 'SS', False, False, -2)
        elif token[-1:] == 'S':
            change(token, 'S', False, False, -1)
def step1b(token):
    if token[-2:] == 'ED':
        if token[-3:] == 'EED':
            change(token, 'EED', True, False, -3, 1)
        elif token[-2:] == 'ED':
            print(change(token, 'ED', False, True, -2))
            step1bE(change(token, 'ED', False, True, -2))
    else:
        if token[-3:] == 'ING':
            step1bE(change(token, 'ING', False, True, -3))
def step1bE(token):
    if token[-2:] == 'AT':
        change(token, 'AT', False, False, -2)
    elif token[-2:] == 'BL':
        change(token, 'BL', False, False, -2)
    elif token[-2:] == 'IZ':
        change(token, 'IZ', False, False, -2)
    elif not token[-1] in ['L', 'Z', 'S'] and doubleChar(token):
        stemmed_word[token[-2]] = token.replace(token[-2], token[-1])
    elif cvc(token) and m(token) == 1:
        stemmed_word['CVC for '+token] = token + 'E'
def step1c(token):
    if token[-1:] == 'Y':
        change(token, 'Y', False, True, -1)

def step2(token):
    if token[-7:] == 'ATIONAL':
        change(token, 'ATIONAL', True, False, -7, 2)
    if token[-6:] == 'TIONAL':
        change(token, 'TIONAL', True, False, -6, 2)
    if token[-4:] == 'ENCI':
        change(token, 'ENCI', True, False, -4, 2)
    if token[-4:] == 'ANCI':
        change(token, 'ANCI', True, False, -4, 2)
    if token[-4:] == 'IZER':
        change(token, 'IZER', True, False, -4, 2)
    if token[-4:] == 'ABLI':
        change(token, 'ABLI', True, False, -4, 2)
    if token[-4:] == 'ALLI':
        change(token, 'ALLI', True, False, -4, 2)
    if token[-5:] == 'ENTLI':
        change(token, 'ENTLI', True, False, -5, 2)
    if token[-5:] == 'OUSLI':
        change(token, 'OUSLI', True, False, -5, 2)
    if token[-7:] == 'IZATION':
        change(token, 'IZATION', True, False, -7, 2)
    if token[-5:] == 'ATION':
        change(token, 'ATION', True, False, -5, 2)
    if token[-4:] == 'ATOR':
        change(token, 'ATOR', True, False, -4, 2)
    if token[-5:] == 'ALISM':
        change(token, 'ALISM', True, False, -5, 2)
    if token[-7:] == 'IVENESS':
        change(token, 'IVENESS', True, False, -7, 2)
    if token[-7:] == 'FULNESS':
        change(token, 'FULNESS', True, False, -7, 2)
    if token[-7:] == 'OUSNESS':
        change(token, 'OUSNESS', True, False, -7, 2)
    if token[-5:] == 'ALITI':
        change(token, 'ALITI', True, False, -5, 2)
    if token[-5:] == 'IVITI':
        change(token, 'IVITI', True, False, -5, 2)
    if token[-6:] == 'BILITI':
        change(token, 'BILITI', True, False, -6, 2)

def step3(token):
    if token[-5:] == 'ICATE':
        change(token, 'ICATE', True, False, -5, 3)
    if token[-5:] == 'ATIVE':
        change(token, 'ATIVE', True, False, -5, 3)
    if token[-5:] == 'ALIZE':
        change(token, 'ALIZE', True, False, -5, 3)
    if token[-5:] == 'ICITI':
        change(token, 'ICITI', True, False, -5, 3)
    if token[-4:] == 'ICAL':
        change(token, 'ICAL', True, False, -4, 3)
    if token[-3:] == 'FUL':
        change(token, 'FUL', True, False, -3, 3)
    if token[-4:] == 'NESS':
        change(token, 'NESS', True, False, -4, 3)

def step4(token):
    if token[-2:] == 'AL':
        change(token, 'AL', True, False, -2, 4)
    if token[-4:] == 'ANCE':
        change(token, 'ANCE', True, False, -4, 4)
    if token[-4:] == 'ENCE':
        change(token, 'ENCE', True, False, -4, 4)
    if token[-2:] == 'ER':
        change(token, 'ER', True, False, -2, 4)
    if token[-2:] == 'IC':
        change(token, 'IC', True, False, -2, 4)
    if token[-4:] == 'ABLE':
        change(token, 'ABLE', True, False, -4, 4)
    if token[-4:] == 'IBLE':
        change(token, 'IBLE', True, False, -4, 4)
    if token[-3:] == 'ANT':
        change(token, 'ANT', True, False, -3, 4)
    if token[-5:] == 'EMENT':
        change(token, 'EMENT', True, False, -5, 4)
    if token[-4:] == 'MENT':
        change(token, 'MENT', True, False, -4, 4)
    if token[-3:] == 'ENT':
        change(token, 'ENT', True, False, -3, 4)
    if token[-4] == 'S' or token[-4] == 'T' and token[-3:] == 'ION':
        change(token, 'ENT', True, False, -3, 4)
    if token[-2:] == 'OU':
        change(token, 'OU', True, False, -2, 4)
    if token[-3:] == 'ISM':
        change(token, 'ISM', True, False, -3, 4)
    if token[-3:] == 'ATE':
        change(token, 'ATE', True, False, -3, 4)
    if token[-3:] == 'ITI':
        change(token, 'ITI', True, False, -3, 4)
    if token[-3:] == 'OUS':
        change(token, 'OUS', True, False, -3, 4)
    if token[-3:] == 'IVE':
        change(token, 'IVE', True, False, -3, 4)
    if token[-3:] == 'IZE':
        change(token, 'IZE', True, False, -3, 4)

def step5a(token):
    if token[-1:] == 'E' and m(token) > 1:
        change(token, 'E', False, False, -3, 5)
    if token[-1:] == 'E' and m(token) == 1 and not cvc(token):
        change(token, 'E', False, False, -3, 5)

def step5b(token):
    if token[-1:] == 'L' and doubleChar(token) > 1 and m(token) > 1:
        stemmed_word[token[-2]] = token.replace(token[-2], token[-1])


def stemmer(word):
    step1a(word)
    step1b(word)
    step1c(word)
    step2(word)
    step3(word)
    step4(word)
    step5a(word)
    step5b(word)
    return stemmed_word
