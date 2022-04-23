import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
out=list(map(int, input().split()))
cnt=0
que = deque([i for i in range(1,n+1)])
for x in out:
    while True:
        if que[0]==x:
            que.popleft()
            break
        else:
            if que.index(x) > (len(que)/2):
                while que[0] !=x:
                    que.appendleft(que.pop())
                    cnt+=1

            else:
                while que[0] !=x:
                    que.append(que.popleft())
                    cnt+=1


print(cnt)
