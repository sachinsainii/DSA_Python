def duplicate(arr):
    low=0
    n=len(arr)
    unique=1
    arr.sort()
    for high in range(1,n):
        if arr[high] != arr[high-1]:
            low += 1
            arr[low]=arr[high]
            unique += 1

    print(f'without duplicates : {arr[:low+1]}')
    print(f'total numbers of elements : {unique}')
duplicate([1,1,2,3,6,6,9,4])


