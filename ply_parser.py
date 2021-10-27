import ply.yacc as yacc
from lx import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_expression_minus(p):

    p[0] = p[1] - p[4]


def p_expression_term(p):
    'expression : term'
    'term:term TIMES term'
    p[0] = p[1]


def p_termMult(p):
    'term : term TIMES term'
    print('term times', p[1], p[2], p[3])
    p[0] = p[1] * p[3]


def p_term_numberDividi(p):
    'term : NUMBER'

    p[0] = p[1]/p[4]


def p_paren(p):
    'term : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    print('erro codigo')


parser = yacc.yacc()
