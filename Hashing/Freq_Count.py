def countFrequencies(nums):
        # Your code goes here
    n=len(nums)
    freq={}
    new=[]
    for i in range(n):
        freq[nums[i]] = freq.get(nums[i],0)+1

    for key,value in freq.items():
        new.append([key,value])
        
    return new
print(countFrequencies([1,2,2,3,1]))