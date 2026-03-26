def ContiguousArrayWithOneAndZero(nums):
    n=len(nums)
    zero=0
    one=0
    f={}
    res=0

    for i in range(n):
        if nums[i]==0:
            zero+=1
        else:
            one+=1

        diff = zero-one

        if diff==0:
            res = i+1

        elif diff not in f:
            f[diff] = i

        else:
            length = i-f[diff]
            res = max(res,length)

    return res

print(ContiguousArrayWithOneAndZero([0,1,1,1,1,1,0,0,0]))