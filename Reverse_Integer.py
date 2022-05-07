n=int(input())
s=0
i=n
if n<0:
    n=n*-1
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if i<0:
    s=s*-1
print(s)