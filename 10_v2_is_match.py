def is_match(p,s):
    if len(p) is 0: return len(s) is 0
    if len(p) > 1 and p[1] is '*':
        return is_match(p[2:],s) or (len(s) > 0 and (p[0] is s[0] or p[0] is '.') and is_match(p,s[1:]))
    if len(s) is 0: return False
    return (p[0] is s[0] or p[0] is '.') and is_match(p[1:],s[1:])


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
        ('a*c*a','a'),
        ('.*a','a'),
        ('ab*a*c*a','aaa'),
        ('a*b', 'aaab'),
        ('a*b', 'b'),
        ('.*', 'abcdefg'),
        ('.*', ''),
        ]

non_matches = [
        ('', 'a'),
        ('a', ''),
        ('a','.*..a*'),
        ('.', ''),
        ('..', 'a'),
        ('...', 'ab'),
        ('a*', 'b'),
        ('.*c','ab'),
        ('a*', 'aab'),
        ('a*', 'baaa'),
        ]

tests = 0
for p,s in matches:
    tests += 1
    assert is_match(p,s) , ("No match for [%s] and [%s]" % (p, s))

for p,s in non_matches:
    print(p,s)
    tests += 1
    assert not is_match(p,s) , ("Incorrect match for [%s] and [%s]" % (p, s))

print("\nDone. %s assertions." % tests)
