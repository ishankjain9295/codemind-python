r=int(input())
c=int(input())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
s=0
for i in range(r):
    for j in range(c):
        s+=mat[i][j]
print(s)