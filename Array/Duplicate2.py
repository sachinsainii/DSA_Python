nums=[1,1,4,5,5,2,3,8,7,7,2]

left=0
nums.sort()
dup=[]
for right in range(1,len(nums)):
    if nums[right] != nums[right-1]:
        left+=1
        nums[left]=nums[right]
    else:
        dup.append(nums[right])

unique = nums[:left+1]     
print(unique)#unique list
print(len(unique))#count
print(dup)#duplicates list