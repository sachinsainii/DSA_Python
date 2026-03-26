def MinSumSubarray(a):
    n=len(a)
    best=a[0]
    res=a[0]
    for i in range(1,n):
        v1=a[i]
        v2=a[i]+best
        best=min(v1,v2)
        res=min(res,best)
    return res
print(MinSumSubarray([3,-4, 2,-3,-1, 7,-5]))