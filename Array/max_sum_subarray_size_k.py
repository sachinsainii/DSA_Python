def maxSumSubarray(arr,k):
    n=len(arr)
    low=0
    high=k

    if n<k:
        return False

    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i in range(k,n):
        window_sum += arr[i]-arr[i-k]
        max_sum = max(max_sum,window_sum)

    return max_sum

print(maxSumSubarray([2,3,4,5,7],2))
