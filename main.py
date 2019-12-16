"""import sympy
from sympy import diff
from sympy import Symbol
from sympy import var
from sympy.utilities.lambdify import lambdify
f = lambdify(x, expr)
x = var('x')
ogeq = input("enter equation: f =  ")
f = ogeq
diffnumb = int(input("enter the number of diffs wanted: "))
for i in range(diffnumb):
  f = f.diff(x)
  print(f)"""
import sympy
from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify
f = input("")
x = var('x')
expr = f.diff(x)
r = lambdify(x, expr)
print(r)