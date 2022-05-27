x=int(input())
r=0
c=0
d=x
a=d
i=0
f=1
sum=0
while x>0:
    c=c+1
    x=x//10
while d>0:
    r=d%10
    for i in range(1,r+1):
        f=f*i
    sum+=f
    f=1
    d=d//10
if a==sum:
    print('The number',a,'is a strong number')
else:
    print('The number',a,'is not a strong number')