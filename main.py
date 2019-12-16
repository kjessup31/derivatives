import sympy
from sympy import diff
from sympy import Symbol
x = Symbol('x')
f = x**10
for i in range(5):
  f_prime = f.diff(x)
  print(f_prime)