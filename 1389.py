import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
arr=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

def bfs(graph,start):
    num = [0] * (n+1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                num[i] = num[a]+1
                q.append(i)
                visited[i] = 1
    return sum(num)


for _ in range(m):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

result=[]
for i in range(1,n+1):
    visited=[0 for _ in range(n+1)]
    result.append(bfs(arr,i))

print(result.index(min(result))+1)
