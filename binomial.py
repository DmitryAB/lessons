class Binomial:
def __init__(self):
a=input("Input a:")
b=input("Input b:")
c=input("Input c:")
binom = (a.str() + "*x*x")
if(b>0) binom+=("+" + b.str()+"*x")
else binom+=(b.str() + "*x")
if(c>0) binom+=("+" + c.str())
else binom+=c.str()

def real_roots(self,a,b,c)
d=b*b-4*a*c
if(d>=0) return [(-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)]
else return []


