from __future__ import division
import re, itertools, string

def solve(formula):
    for p in fill_in(formula):
        if valid(p):
            return p

def fast_solve(formula):
    f, letters = compile_formula(formula, True)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError: pass

def compile_formula(formula, verbose=False):
    leading = [w[0] for w in set(re.findall(r'[A-Z]+', formula))]

    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split(r'([A-Z]+)', formula))
    body = ''.join(tokens)

    f = 'lambda %s: %s%s' %(parms, body, no_zero(leading))
    if verbose: print f
    return eval(f), letters

def compile_word(word):
    if word.isupper():
        terms = [('%s*%s' %(10**i, d))
                for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

def no_zero(a_list):
    result = ''
    for n in a_list:
        result += ' and %s != 0' %(n)
    return result

def fill_in(formula):
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def valid(f):
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

print fast_solve('OEE + AEE == AFF')
#print compile_word('SOME')