
'''
from typing import Tuple
from collections import namedtuple
                                         
term = namedtuple("term", "coeff vars")
var = namedtuple("var", "locs coeff")

term1 = term(1, [('x',3)])
term2 = term(6, [('y', 2)])
term3 = term(-3, [()])
func = [term1, term2, term3]
'''

# Using sympy
from sympy import symbols, cos, diff

'''
Example Function:
f(x,y) = yx^3 + 6y^2 - 3
'''

vars = symbols('x y', real=True)
x,y = vars

function = y*x**3 + 6*y**2 - 3

gradient = {}

for v in vars:
    gradient[f'wrt {v}'] = diff(function, v)

print(gradient)
