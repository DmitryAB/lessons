import math
class Binomial:
 def __init__(self,a,b,c):
  self.a=float(a)
  self.b=float(b)
  self.c=float(c)
 def __str__(self):
  binom = a + "*x*x"
  if self.b>0 :
   binom +="+" + b+"*x"
  else:
   binom += b + "*x"
  if self.c>0 :
   binom += "+" + c
  else: 
   binom += c
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
a=input("Input a:")
b=input("Input b:")
c=input("Input c:")
binom = Binomial(a,b,c)
print(binom)
print(binom.real_roots())





