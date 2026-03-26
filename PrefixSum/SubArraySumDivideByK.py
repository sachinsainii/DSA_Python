def SubArraySumDivideByK(nums,k):
    n=len(nums)
    sum=0
    f={}
    f[0]=1
    res=0

    for i in range(n):
        sum+=nums[i]
        rem = sum%k
        if rem<0:
            rem = rem+k
        f[rem] = f.get(rem,0)
        res+=f[rem]
        f[rem]+=1
    return res

print(SubArraySumDivideByK([4,5,0,-2,-3,1],5))
