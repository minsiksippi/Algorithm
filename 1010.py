def fac(num):
    ans=1
    for i in range(1, num+1):
        ans *= i
    return ans


n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    print(int(fac(b)/ (fac(b-a)*fac(a)) ))

