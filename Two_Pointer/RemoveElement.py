def removeElement(nums,k):
    n= len(nums)
    slow = 0
    fast = 0
    for fast in range(n):
        if nums[fast]!=k:
            nums[slow]=nums[fast]
            slow+=1
    print(slow)
    print(nums[:slow])
removeElement([2,2,2,3,3],3)