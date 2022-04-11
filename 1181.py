import sys

n=int(sys.stdin.readline())
arr = []
arr2={}
for _ in range(n):
    arr.append(sys.stdin.readline().strip())

arr2=set(arr)
arr=list(arr2)

arr.sort(key = lambda x:(len(x),x))

print('\n'.join(arr))
