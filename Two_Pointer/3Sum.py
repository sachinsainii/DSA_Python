def threesum(nums):
    nums.sort()
    n= len(nums)
    result = []

    for i in range(0,n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left = i+1
        right = n-1
        target = -nums[i]

        while(left<right):
            sum = nums[left]+nums[right]

            if (sum==target):
                result.append([nums[i],nums[left],nums[right]])
                left +=1
                right -=1

                if left<n and nums[left]==nums[left-1]:
                    left +=1

                if right>=0 and nums[right]==nums[right+1]:
                    right -=1

            elif (sum<target):
                left +=1
            else:
                right -=1

    print(result)
threesum([-1,0,1,2,-1,-4])
                