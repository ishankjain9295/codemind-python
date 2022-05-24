n=int(input())
a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
c=[]
for i in range(n):
    l=a[i]+b[i]
    c.append(l)
print(*c)