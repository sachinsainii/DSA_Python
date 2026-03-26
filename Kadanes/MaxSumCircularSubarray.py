def MaxSumCircularSubarray(a):
    total=0
    min_end=0
    max_end=0
    min_sum=0
    max_sum=0

    for i in a:
        total+=i

        max_end=max(i,max_end+i)
        max_sum=max(max_end,max_sum)

        min_end=min(i,min_end+i)
        min_sum=min(min_sum,min_end)

    if max_sum<0:
        return max_sum

    return max(max_sum,total-min_sum)

print(MaxSumCircularSubarray([1,-2,3,-2]))
