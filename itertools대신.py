def comb(arr,n):
    result=[]
    if n>len(arr):
        return arr
    if n==1:
        for i in arr:
            result.append([i])
        return result
    elif n>1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    return result

def perm(arr,n):
    result = []
    if n > len(arr):
        return arr
    if n == 1:
        for i in arr:
            result.append([i])
        return result
    elif n>1:
        for i in range(len(arr)):
            ans = [p for p in arr]
            ans.remove(arr[i])
            for j in perm(ans,n-1):
                result.append([arr[i]]+j)
    return result
arr = [1,2,3,4,5]
print(comb(arr,1))
print(comb(arr,2))
print(comb(arr,3))

print(perm(arr,1))
print(perm(arr,2))
print(perm(arr,3))

