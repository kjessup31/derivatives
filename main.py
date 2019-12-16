import sympy
from sympy import diff
fr
x = Symbol('x')
#user enters equation
#ogeq means original equation
ogeq = eval(input("enter equation: f =  ")) #need to change eval. input does not work
f = ogeq
#user enters how many derivtives of the equations
#diffnumb means the derivatie number
diffnumb = int(input("enter the number of diffs wanted (up to 5): "))
if diffnumb == 1:
  f_prime = f.diff(x)
  print(f_prime)
elif diffnumb == 2:
  f_prime = f.diff(x)
  print(f_prime)
  f2prime = f_prime
  f_2prime = f2prime.diff(x)
  print(f_2prime)
elif diffnumb == 3:
  f_prime = f.diff(x)
  print(f_prime)
  f2prime = f_prime
  f_2prime = f2prime.diff(x)
  print(f_2prime)
  f3prime = f_2prime
  f_3prime = f3prime.diff(x)
  print(f_3prime)
elif diffnumb == 4:
  f_prime = f.diff(x)
  print(f_prime)
  f2prime = f_prime
  f_2prime = f2prime.diff(x)
  print(f_2prime)
  f3prime = f_2prime
  f_3prime = f3prime.diff(x)
  print(f_3prime)
  f4prime = f_3prime
  f_4prime = f4prime.diff(x)
  print(f_4prime)
elif diffnumb == 5:
  f_prime = f.diff(x)
  print(f_prime)
  f2prime = f_prime
  f_2prime = f2prime.diff(x)
  print(f_2prime)
  f3prime = f_2prime
  f_3prime = f3prime.diff(x)
  print(f_3prime)
  f4prime = f_3prime
  f_4prime = f4prime.diff(x)
  print(f_4prime)
  f5prime = f_4prime
  f_5prime = f5prime.diff(x)
  print(f_5prime)
else:
  print("Can only differentiate up to five times")