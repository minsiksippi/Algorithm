import sys
n,m=map(int, sys.stdin.readline().split())
cnt=0
z = int(float(m/n) * 100)
num=z
if n==m:
    print(-1)
else:
    while True:
        if num != z:
            break
        cnt+=1
        z = int(float((m + cnt) / (n+cnt)) * 100)

    print(cnt)
