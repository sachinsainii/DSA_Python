def Min_Size_Subarray_Sum(arr,target):
    n=len(arr)
    left=0
    sum=0
    min_len=float('inf')

    for right in range(n):
        sum+=arr[right]

        while sum>=target:
            min_len = min(min_len,right-left+1)
            sum-=arr[left]
            left+=1

    if min_len==float('inf'):
        return 0
    else:
        return min_len

print(Min_Size_Subarray_Sum([2,4,4],4))
