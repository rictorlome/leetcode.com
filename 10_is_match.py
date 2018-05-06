## Approach using curried parser functions
## Current approach fails spec on line 71 - ('ab*a*c*a','aaa')

def is_match(p,s):
    parsers = decompose(p)
    result = sequence(parsers)(s)
    return result['success'] and result['rest'] is ''

def char(c):
    def hidden(input):
        if len(input) > 0 and input[0] is c:
            return {'success': True, 'rest': input[1:]}
        else:
            return {'success': False, 'rest': input}
    return hidden

def wild_card(c):
    def hidden(input):
        if len(input) > 0:
            return {'success': True, 'rest': input[1:]}
        else:
            return {'success': False, 'rest': input}
    return hidden

def zero_or_more(c):
    def hidden(input):
        if c is '.':
            return {'success': True, 'rest': '' }
        for i,ch in enumerate(input):
            if ch is not c:
                return {'success': True, 'rest': input[i:]}
        return {'success': True, 'rest': ''}
    return hidden

def decompose(p):
    parsers, i = [], 0
    while i < len(p):
        ch = p[i]
        if i is len(p)-1 or p[i+1] is not '*':
            parsers.append(wild_card(ch)) if ch is '.' else parsers.append(char(ch))
            i += 1
        else:
            parsers.append(zero_or_more(ch))
            ## This is broken
            while i < len(p) and (p[i] is ch or p[i] is '*'):
                i += 1
    return parsers

def sequence(parsers):
    def hidden(input):
        next = input
        for parser in parsers:
            resObj = parser(next)
            if not resObj['success']:
                return {'success': resObj['success'], 'rest': resObj['rest']}
            else:
                next = resObj['rest']
        return {'success': True, 'rest': next}
    return hidden

matches = [
        ('', ''),
        ('a', 'a'),
        ('ab', 'ab'),
        ('.', 'a'),
        ('..', 'ab'),
        ('a*', ''),
        ('a*', 'a'),
        ('a*', 'aaa'),
        ('a*a','aaa'),
        ('ab*a*c*a','aaa')
        ('a*b', 'aaab'),
        ('a*b', 'b'),
        ('.*', 'abcdefg'),
        ('.*', ''),
        ]

non_matches = [
        ('', 'a'),
        ('a', ''),
        ('.', ''),
        ('..', 'a'),
        ('...', 'ab'),
        ('a*', 'b'),
        ('a*', 'aab'),
        ('a*', 'baaa'),
        ]

tests = 0
for p,s in matches:
    tests += 1
    assert is_match(p,s) , ("No match for [%s] and [%s]" % (p, s))

for p,s in non_matches:
    tests += 1
    assert not is_match(p,s) , ("Incorrect match for [%s] and [%s]" % (p, s))

print("\nDone. %s assertions." % tests)
