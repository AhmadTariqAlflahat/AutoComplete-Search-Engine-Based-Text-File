vowel = ('A','E','U','O','I')
def v(token):
    for t in token:
        if t in vowel:
            return True
    return False

def m(token):
    m = 0
    prv = None
    for t in token:
        if prv in vowel and t not in vowel:
            m += 1
        prv = t
    return m

def cvc(token):
    first = None
    mid = None
    for last in token:
        if first not in vowel and mid in vowel and last not in vowel and last not in  ['W', 'X', 'Y']:
            return True
        first = mid
        mid = last
    return False

def doubleChar(token):
    if token[-1]==token[-2]:
        return True
    return False
