import math as m
def prime(n):
    for i in range(2,m.ceil(n**.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
while(n):
    n-=1 
    a=int(input())
    b=a
    c=a
    while(1): 
        if prime(b)==1:
            break
        b+=1 
    while(1):
        if prime(c)==1:
         break
        c-=1 
    if abs(b-a)==abs(a-c):
       print(c) 
    elif abs(b-a)>abs(a-c):
       print(c) 
    elif abs(b-a)<abs(a-c):
       print(b)