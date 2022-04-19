import sys

def fac(m):
    if m==0:
        return 1
    elif m==1:
        return 1
    return m * fac(m-1)

n = int(sys.stdin.readline())
cnt=0
lis = list(str(fac(n)))
for i in lis[::-1]:
    if i=='0':
        cnt+=1
    else:
        break

print(cnt)
