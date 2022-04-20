import math
import sys

def func(p):
    cnt=0
    num=int(math.sqrt(p))
    for i in range(2,num+1):
        #print(p, i)
        if p%(i**2)==0:
            cnt+=1
    if cnt==0:
        return True
    else:
        return False

n,m=map(int, sys.stdin.readline().split())
cnt2=0
for i in range(n,m+1):
    if func(i)==True:
        cnt2+=1
print(cnt2)
