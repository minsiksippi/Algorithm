
import sys
input=sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    rs = 1
    q = [(x,y)]
    while q:
        ex, ey = q.pop()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if map[nx][ny] == 1 and chk[nx][ny]==False:
                    rs+=1
                    chk[nx][ny]=True
                    q.append((nx,ny))
    return rs
cnt = 0
maxv = 0
for i in range(n):
    for j in range(m):
        if map[i][j]==1 and chk[i][j]==False:
            chk[i][j]=True
            cnt+=1
            maxv=max(maxv,bfs(i,j))

print(cnt)
print(maxv)
