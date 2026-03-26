def PivotIndex(nums):
    n=len(nums)
    left=0
    right=0
    sum=0

    for i in range(n):
        sum+=nums[i]

    for i in range(n):
        right = sum-left-nums[i]

        if right==left:
            return i

        left+=nums[i]

    return -1

print(PivotIndex([1,7,3,6,5,6]))