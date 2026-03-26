def Max_Size_Subarray_total(arr,target):
    low=0
    n=len(arr)
    max_len=0
    total=0
    
    for high in range(n):
        total += arr[high]

        while total>target:
            # max_len = max(max_len,high-low+1)
            total -= arr[low]
            low += 1
        if total==target:
            max_len = max(max_len,high-low+1)

    return max_len

print(Max_Size_Subarray_total([1,2,0,7,3,9],10))
