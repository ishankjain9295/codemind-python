principle,rate,time=map(int,input().split())
CI = principle *(pow((1 + rate / 100), time))
print("%.2f"%CI)