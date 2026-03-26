def MaxProductSum(a):
    n=len(a)
    minend=a[0]
    maxend=a[0]
    res=a[0]

    for i in range(1,n):
        v1=a[i]
        v2=a[i]*minend
        v3=a[i]*maxend

        minend=min(v1,min(v2,v3))
        maxend=max(v1,max(v2,v3))

        res=max(res,maxend)
    return res
print(MaxProductSum([2,3,-2,4]))