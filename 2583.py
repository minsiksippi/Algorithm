import sys
from collections import deque
m,n,r = map(int, input().split())

input = sys.stdin.readline
arr = [[0 for _ in range(n)] for _ in range(m)]
chk = [[False for _ in range(n)] for _ in range(m)]
res=[]
for _ in range(r):
    a,b,c,d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            arr[j][i]=1
cnt = 0

def bfs(x,y):
    que = deque()
    que.append((x,y))
    cnt2=1
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while que:
        p,q = que.popleft()
        for k in range(4):
            nx = p + dx[k]
            ny = q + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if chk[nx][ny]==False and arr[nx][ny]==0:
                    chk[nx][ny]=True
                    arr[nx][ny]=1
                    que.append((nx,ny))
                    cnt2 += 1
    res.append(cnt2)

for i in range(m):
    for j in range(n):
        if arr[i][j]==0 and chk[i][j]==False:
            arr[i][j]=1
            chk[i][j]=True
            bfs(i,j)
            cnt+=1

res.sort()
print(cnt)
for i in res:
    print(i, end=' ')


