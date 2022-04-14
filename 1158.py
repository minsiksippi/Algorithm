n, k = map(int, input().split())

arr = [i+1 for i in range(n)]
new=[]
ind=0
while arr:
    ind=(ind+k-1)%(len(arr))
    new.append(arr.pop(ind))
print("<", ', '.join(str(i) for i in new), ">", sep='')


