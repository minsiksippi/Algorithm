import sys
from collections import Counter

n = int(sys.stdin.readline())
lis=[]
for _ in range(n):
    lis.append(sys.stdin.readline())

lis.sort()
print(Counter(lis).most_common(1)[0][0])
