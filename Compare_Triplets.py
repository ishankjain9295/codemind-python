a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
al=0
bo=0
for i in range(3):
    if(a[i]>b[i]):
        al+=1
    elif(a[i]<b[i]):
        bo+=1
print(al,bo)