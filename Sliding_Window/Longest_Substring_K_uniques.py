def Longest_Substring(ar,k):
    n=len(ar)
    left=0
    res=-1
    freq={}

    for right in range(n):
        freq[ar[right]]=freq.get(ar[right],0)+1

        while len(freq)>k:
            freq[ar[left]]-=1
            if freq[ar[left]]==0:
                del freq[ar[left]]
            left+=1

        if len(freq)==k:
            res=max(res,right-left+1)
            

    return res
print(Longest_Substring("aabacbebebe",3))

