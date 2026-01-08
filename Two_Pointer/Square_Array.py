from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        neg = []
        pos =[]
        res = []

        #separate negative and positive
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)

        # #case 1: no negative numbers
        # if len(neg)==0:
        #     [i*i for i in pos]
            
        # #case2: no positives numbers
        # if len(pos) == 0:
        #     [i*i for i in neg][::-1]
            

        #case3: both exist
        neg = [i*i for i in neg][::-1]
        pos = [i*i for i in pos]
        n,m = len(neg), len(pos)

        i=j=0
        while i<n and j<m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1

        #after loop finish
        while i<n:
            res.append(neg[i])
            i+=1

        while j<m:
            res.append(pos[j])
            j+=1

        return res
        
s = Solution()
print(s.sortedSquares([-4,-2,-1,0,3,5,6]))
