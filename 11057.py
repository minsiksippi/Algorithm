import sys
input = sys.stdin.readline

n = int(input())

dp=[[0 for _ in range(10)] for _ in range(n+1)]

for i in range(10):
    dp[0][i]=1
for i in range(n+1):
    dp[i][0]=1

for i in range(1,10):
    for j in range(1,n+1):
        dp[j][i]= dp[j][i-1] + dp[j-1][i]


print(dp[n][9]%10007)
