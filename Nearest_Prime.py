x=int(input())
for i in range(1,x+1):
    n=int(input())
    d=n
    for j in range(n,1,-1):
        c=0
        for k in range(1,j+1):
            if j%k==0:
                c=c+1
        if c==2:
            min=j
            break
    while True:
        c=0
        for k in range(1,n+1):
            if n%k==0:
                c=c+1
        if c==2:
            max=n
            break
        n=n+1
    r1=d-min
    r2=max-d
    if r1<r2:
        print(min)
    elif r1==r2:
        print(min)
    else:
        print(max)