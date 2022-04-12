import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
sum=0
a.sort()
for i in a:
    sum+=i*b.pop(b.index(max(b)))

print(sum)


