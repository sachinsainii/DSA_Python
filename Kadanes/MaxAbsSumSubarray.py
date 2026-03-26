def MaxAbsSumSubarray(nums):
    min_end=0
    min_sum=0
    max_end=0
    max_sum=0

    for i in nums:
        min_end = min(i,min_end+i)
        min_sum = min(min_end,min_sum)

        max_end = max(i,max_end+i)
        max_sum = max(max_end,max_sum)

    return max(abs(min_sum),abs(max_sum))

print(MaxAbsSumSubarray([1,-3,2,3,-4]))
