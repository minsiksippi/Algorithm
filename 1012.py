import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(arr,x,y):
    que=deque()
    que.append((x,y))
    arr[x][y]=0

    while que:
        p,q = que.popleft()
        for i in range(4):
            nx=p+dx[i]
            ny=q+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                que.append((nx, ny))
    return

T = int(input())
for _ in range(T):
    n,m,k = map(int, input().split())
    arr=[[0] * m for _ in range(n)]
    cnt=0
    for _ in range(k):
        a,b=map(int, input().split())
        arr[a][b]=1

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 :
                bfs(arr,i,j)
                cnt+=1
    print(cnt)
