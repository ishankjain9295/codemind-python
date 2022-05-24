n=int(input())
arr=list(map(int,input().strip().split()))
s=0
for i in range(0,n):
    s+=arr[i]
print(s)