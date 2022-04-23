import sys
from collections import deque
input=sys.stdin.readline

n,k = map(int, input().split())
que = deque()
chk = [0] * 100001
chk[n] = True
que.append(n)
while que:
    x = que.popleft()
    if x == k:
        print(chk[x]-1)
        break

    if 2*x <= 100000 and chk[2*x]==0:
        que.append(2*x)
        chk[2*x] = chk[x]+1
    if x+1<=100000 and chk[x+1]==0:
        que.append(x+1)
        chk[x+1]=chk[x]+1
    if x-1>=0 and chk[x-1]==0:
        que.append(x-1)
        chk[x-1] = chk[x]+1
