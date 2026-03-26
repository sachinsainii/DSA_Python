def SubArraySumEqualsToK(nums,k):
    n=len(nums)
    sum=0
    freq={0:1}
    res=0


    for i in range(n):
        sum+=nums[i]
        red = sum-k
        if red in freq:
            res += freq[red]
        freq[sum] = freq.get(sum,0)+1
    return res

print(SubArraySumEqualsToK([1,1,1],2))