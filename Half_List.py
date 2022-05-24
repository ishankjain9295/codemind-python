def fun(arr,a):
    for i in range(a-1,(a//2)-1,-1):
        print(arr[i],end=' ')
    for i in range(0,a//2):
        print(arr[i],end=' ')
a=int(input())
arr=list(map(int,input().strip().split()))
fun(arr,a)