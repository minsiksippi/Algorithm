def fun(num):
    li=list(str(num))
    li.reverse()
    n = int(str(''.join(li)))
    return n

a, b = map(int, input().split())
print(fun(fun(a)+fun(b)))