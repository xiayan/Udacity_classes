#!/usr/bin/python

import re

def recursive_replace(source, splitlist, seq):
    if len(splitlist) > 0:
        source = source.replace(splitlist[0], seq)
        return recursive_replace(source, splitlist[1:], seq)
    else:
        return source

def old_split_string(source,splitlist):
    seq = splitlist[0]
    regex = re.compile("%s*"%seq)
    final = recursive_replace(source, splitlist, seq)
    final = re.split(regex, final.rstrip())
    if final[-1] == '':
        final.pop()
    return final

def split_string(source, splitlist):
    the_seq = splitlist[0]
    for sep in splitlist:
        source = source.replace(sep, the_seq)
    print source
    final = source.split(the_seq)
    while '' in final:
        final.remove('')
    return final

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

out = split_string('Hi! I am your Assistant Instructor, Peter.', '! ,.')
print out