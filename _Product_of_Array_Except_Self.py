# import math
a=int(input())
b=list(map(int,input().split()))[:a]
c=1
for i in b:
    c*=i
for i in b:
    print(int(c/i),end=' ')