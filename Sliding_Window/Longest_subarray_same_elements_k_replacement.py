def longestsubarray(nums,k):
    n=len(nums)
    max_len=0
    zero_count=0
    left=0
    right=0
    for right in range(n):
        if nums[right]==0:
            zero_count+=1

        while zero_count>k:
            if nums[left]==0:
                zero_count-=1
            left+=1
        max_len = max(max_len,right-left+1)
    return max_len

print(longestsubarray([1,1,1,1,0,0,0,1,1,1,0,0],2))
