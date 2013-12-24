# JavaScript: Comments & Keywords
#
# In this exercise you will write token definition rules for all of the
# tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and
# STRING. In addition, you will handle // end of line comments
# as well as /* delimited comments */.
#
# We will assume that JavaScript is case sensitive and that keywords like
# 'if' and 'true' must be written in lowercase. There are 26 possible
# tokens that you must handle. The 'tokens' variable below has been
# initialized below, listing each token's formal name (i.e., the value of
# token.type). In addition, each token has its associated textual string
# listed in a comment. For example, your lexer must convert && to a token
# with token.type 'ANDAND' (unless the && is found inside a comment).
#
# Hint 1: Use an exclusive state for /* comments */. You may want to define
# t_comment_ignore and t_comment_error as well.

import ply.lex as lex

def test_lexer(lexer,input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem.
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

#
# Write your code here.
#
states = (('comment', 'exclusive'),
          ('doubleslash', 'exclusive'))

def t_ANDAND(token):
  r'&&'
  return token

def t_COMMA(token):
  r','
  return token

def t_doubleslash(token):
  r'//'
  token.lexer.begin('doubleslash')

def t_doubleslash_end(token):
  r'\n'
  token.lexer.lineno += 1
  token.lexer.begin('INITIAL')

def t_comment(token):
  r'/\*'
  token.lexer.lineno += token.value.count('\n')
  token.lexer.begin('comment')

def t_comment_end(token):
  r'\*/'
  token.lexer.begin('INITIAL')

def t_DIVIDE(token):
  r'/'
  return token

def t_ELSE(token):
  r'else'
  return token

def t_EQUALEQUAL(token):
  r'=='
  return token

def t_EQUAL(token):
  r'='
  return token

def t_FALSE(token):
  r'false'
  return token

def t_FUNCTION(token):
  r'function'
  return token

def t_GE(token):
  r'>='
  return token

def t_GT(token):
  r'>'
  return token

def t_IF(token):
  r'if'
  return token

def t_LBRACE(token):
  r'{'
  return token

def t_LE(token):
  r'<='
  return token

def t_LPAREN(token):
  r'\('
  return token

def t_LT(token):
  r'<'
  return token

def t_MINUS(token):
  r'-'
  return token

def t_NOT(token):
  r'!'
  return token

def t_OROR(token):
  r'\|\|'
  return token

def t_PLUS(token):
  r'\+'
  return token

def t_RBRACE(token):
  r'}'
  return token

def t_RETURN(token):
  r'return'
  return token

def t_RPAREN(token):
  r'\)'
  return token

def t_SEMICOLON(token):
  r';'
  return token

def t_TIMES(token):
  r'\*'
  return token

def t_TRUE(token):
  r'true'
  return token

def t_VAR(token):
  r'var'
  return token

t_ignore = ' \t\v\r' # whitespace
t_comment_ignore = ' \t\v\r' # whitespace
t_doubleslash_ignore = '\t\v\r'

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print "JavaScript Lexer: Illegal character " + t.value[0]
        t.lexer.skip(1)

def t_comment_error(token):
  token.lexer.skip(1)

def t_doubleslash_error(token):
  token.lexer.skip(1)

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own.

lexer = lex.lex()

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1)
print test_lexer(input1) == output1

input2 = """
if // else mystery
=/*=*/=
true /* false
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']
print test_lexer(input2)
print test_lexer(input2) == output2