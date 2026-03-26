def MaxSumSubarray(a):
    n=len(a)
    best=a[0]
    res=a[0]
    for i in range(1,n):
        v1=a[i]
        v2=best+a[i]

        best=max(v1,v2)
        
        res=max(res,best)
    return res
    # return a[:res+1]
print(MaxSumSubarray([-2,1,-3,4,-1,2,1,-5,4]))
