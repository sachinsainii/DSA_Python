def two_sum(numbers,target):
    n=len(numbers)
    i=0
    j=n-1
    while(i<j):
        sum=numbers[i]+numbers[j]
        if sum==target:
            return [i,j]
        elif sum<target:
            i += 1
        elif sum>target:
            j -= 1

print(two_sum([2,7,9,11,15],20))