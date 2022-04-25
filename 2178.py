import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
arr=[list(map(int,input().strip())) for _ in range(n)]
chk=[[False] * m for _ in range(n)]
visit=[[0] * m for _ in range(n)]
cnt=0
def bfs(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    que = deque()
    que.append((x,y))
    while que:
        (p,q)=que.popleft()
        for k in range(4):
            nx = p + dx[k]
            ny = q + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0 and arr[nx][ny]==1:
                    visit[nx][ny]=visit[p][q]+1
                    que.append((nx,ny))

visit[0][0]=1
bfs(0,0)
print(visit[n-1][m-1])

