from collections import deque
import sys
input=sys.stdin.readline
n,m = map(int, input().split())
arr=[[] for _ in range(n+1)]
chk=[False] * (n+1)
result=[]

def bfs(arr,num):
    cnt=0
    que=deque()
    que.append(num)
    while que:
        num2 = que.popleft()
        for i in arr[num2]:
            if 0<=i<n:
                if chk[i]==False:
                    chk[i]=True
                    cnt += 1
                    que.append(i)
    return cnt

for _ in range(m):
    x,y = map(int,input().split())
    arr[y].append(x)

for i in range(1, n+1):
    chk=[False] * (n+1)
    if chk[i]==False:
        chk[i]=True
        result.append(bfs(arr,i))

new=[]
for i in range(len(result)):
    if result[i]==max(result):
        new.append(i+1)
new.sort()

print(*new)
