import sympy
from sympy import diff
from sympy import Symbol
x = Symbol('x')
#user enters equation
#ogeq means original equation
ogeq = eval(input("enter equation: f =  "))
f = ogeq
#user enters how many derivtives of the equations
#diffnumb means the derivatie number
diffnumb = int(input("enter the number of diffs wanted: "))
for i in range(diffnumb):
  f = f.diff(x)
  print(f)