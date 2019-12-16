import sympy
from sympy import *
x = Symbol('x')
#user enters equation
#ogeq means original equation
ogeq = eval(input("enter equation: f =  ")) #need to change eval. input does not work
f = ogeq
#user enters how many derivtives of the equations
#diffnumb means the derivatie number
diffnumb = int(input("enter the number of diffs wanted (up to 5): "))
