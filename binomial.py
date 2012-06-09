import math
import random
class Binomial:
 def __init__(self,a,b,c):
  self.a=float(a)
  self.b=float(b)
  self.c=float(c)
 def __str__(self):
  binom = str(self.a) + "*x*x"
  if self.b>0 :
   binom +="+" + str(self.b)+"*x"
  else:
   binom += str(self.b) + "*x"
  if self.c>0 :
   binom += "+" + str(self.c)
  else: 
   binom += str(self.c)
  return binom
 def real_roots(self):
  self.d=self.b*self.b-4*self.a*self.c
 # print(self.d)
  if self.d>0:
   return [(-self.b+math.sqrt(self.d))/(2*self.a), 
(-self.b-math.sqrt(self.d))/(2*self.a)]
  if self.d==0:
   return [(-self.b+math.sqrt(self.d))/(2*self.a)]
  else:
   return []
"""a=str(random.uniform(-100,100)) #input("Input a:")
b=str(random.uniform(-100,100)) #input("Input b:")
c=str(random.uniform(-100,100)) #input("Input c:")
binom = Binomial(a,b,c)
print(binom)
print(binom.real_roots())
"""




