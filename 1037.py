n=int(input())
arr = (list(map(int, input().split())))
num = 1
ans=1

if n==1:
    print(arr[0]**2)

else:
    while True:
        cnt=0
        num = num + 1

        for i in arr:
            if num % i == 0:
                cnt = cnt + 1

        if cnt == n:
            ans = num
            break

    if ans in arr:
        ans = ans * min(arr)
    print(ans)
