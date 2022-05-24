a=int(input())
s=list(map(int,input().strip().split()))
for i in range(a):
    s[i]=s[i]**2
s.sort()
print(*s)