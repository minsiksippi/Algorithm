import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
arr=[list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result=[]
each=0
def bfs(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    que=deque()
    que.append((x,y))
    global each
    while que:
        p,q=que.popleft()
        for k in range(4):
            nx=p+dx[k]
            ny=q+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]==1 and chk[nx][ny]==False:
                    chk[nx][ny]=True
                    que.append((nx,ny))
                    each += 1



for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and chk[i][j]==False:
            each=0
            chk[i][j]=True
            bfs(i,j)
            result.append(each+1)
result.sort()
print(len(result))
for i in result:
    print(i)
