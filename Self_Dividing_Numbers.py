x=int(input())
y=int(input())
for i in range(x,y+1):
    if i%10==0:
        continue
    t=i
    d=i
    c=0
    c1=0
    while d>0:
        r=d%10
        if r==0:
            break
        if i%r==0:
            c+=1
        c1+=1
        d=d//10
    if c==c1:
        print(i,end=" ")