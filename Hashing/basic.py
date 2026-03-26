def hash(arr,target):
    n=len(arr)
    freq={}
    count=0

    for i in range(n):
        freq[arr[i]] = freq.get(arr[i],0)+1
    

    for i in range(n):
        if arr[i] == target:
            count+=1

    return count,freq

print(hash([1,2,2,5,8,8,5,3],8))
