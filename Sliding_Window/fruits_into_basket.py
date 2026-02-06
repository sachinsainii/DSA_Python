def fruits_into_basket(fruits):
    n=len(fruits)
    left=0
    freq={}
    max_length=0

    for right in range(n):
        fruit = fruits[right]
        freq[fruit]=freq.get(fruit,0)+1

        while len(freq)>2:
            freq[fruits[left]]-=1
            if freq[fruits[left]]==0:
                del freq[fruits[left]]
            left+=1

        max_length=max(max_length,right-left+1)

    return max_length
print(fruits_into_basket([1,2,1]))
