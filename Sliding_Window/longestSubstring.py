def longestSubstringWithoutDuplicate(nums):
    # n=len(nums)
    max_len=0
    freq={}
    left=0

    for right,ch in enumerate(nums):
        if ch in freq and freq[ch]>=left:
            left = freq[ch]+1

        freq[ch]=right
        max_len=max(max_len,right-left+1)
        start_index=left

    return max_len
    # return nums[start_index:start_index+max_len]

print(longestSubstringWithoutDuplicate("abcebca"))
