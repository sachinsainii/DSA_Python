def dup(head):
    low=0
    high=1
    unique=1
    n=len(head)
    while(high<n):
        if (head[high]==head[high-1]):
            high += 1
            continue
        else:
            low += 1
            head[low]=head[high]
            high += 1
            unique += 1
    print(f'without duplicate values array are:',head[:unique])
    print(f"Total unique elements are:",unique)
dup([1,1,2,2,3,5,6])
