import sympy
from sympy import *
x = Symbol('x')
#user enters equation
#ogeq means original equation
ogeq = eval(input("enter equation: f =  ")) #need to change eval. input does not work
f = ogeq
for i in range(5):
  f