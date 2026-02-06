def longestcharreplace(s,k):
    n=len(s)
    freq={}
    max_freq=0
    max_len=0
    left=0

    for right in range(n):
        ch=s[right]
        freq[ch]=freq.get(ch,0)+1

        max_freq=max(max_freq,freq[ch])

        window_size=right-left+1

        if window_size-max_freq>k:
            freq[s[left]]-=1
            left+=1

        max_len=max(max_len,right-left+1)

    return max_len

print(longestcharreplace("AABABBA",1))
