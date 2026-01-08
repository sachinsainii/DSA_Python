def threeSumClosest(nums,target):
    nums.sort()
    n= len(nums)
    diff = float('inf')
    result = 0

    for i in range(0,n-2):
        left = i+1
        right = n-1

        while(left<right):
            cur_sum = nums[i]+nums[left]+nums[right]
            max_diff = abs(target-cur_sum)

            if diff>max_diff:
                diff = max_diff
                result = cur_sum

            if target==cur_sum:
                return result

            elif cur_sum<target:
                left+=1

            else:
                right-=1

    print(result)
threeSumClosest([1,2,3,4,5,6,8,2],2)
