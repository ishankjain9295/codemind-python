s=list(map(int,input().strip().split()))
m=0
a=[]
for i in range(len(s)):
    s[i]-=1
for i in range(len(s)):
    for j in range(len(s)):
        if(i!=j):
            k=s[i]*s[j]
            a.append(k)
print(max(a))