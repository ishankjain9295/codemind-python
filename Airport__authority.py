a=int(input())
s=[]
for i in range(a):
    I=int(input())
    s.append(I)
d=int(input())
g=0
for i in range(a):
    if(s[i]<=d):
        g+=1
    else:
        g+=2
print(g)