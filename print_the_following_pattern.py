x=int(input())
a=x
for i in range(1,x+1):
    for j in range(1,x+1):
        print(a,end=" ")
        a=a-1
    a=x
    print()