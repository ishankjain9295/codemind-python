n=int(input())
import math
s=math.sqrt(n)
x=s-math.floor(s)
if x==0:
    print('True')
else:
    print('False')