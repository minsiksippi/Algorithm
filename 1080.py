def reverse(arr,i,j):
    for p in range(i,i+3):
        for q in range(j,j+3):
            arr[p][q]=1-arr[p][q]

n, m = map(int, input().split())
cnt=0
lisA=list(list(map(int,input())) for _ in range(n))
lisB=list(list(map(int,input())) for _ in range(n))

for i in range(n-2):
    for j in range(m-2):
        if lisA[i][j] != lisB[i][j]:
            reverse(lisA,i,j)
            cnt+=1

cnt2=0
for i in range(n):
    for j in range(m):
        if lisA[i][j]!=lisB[i][j]:
            cnt2+=1

if cnt2==0:
    print(cnt)
else:
    print(-1)


