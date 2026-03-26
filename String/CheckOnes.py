def checkOnesSegment(s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        count=0

        for i in range(n):
            
            if s[i]=='1' and (i == 0 or s[i-1] == '0'):
                count += 1

        return count <=1

print(checkOnesSegment("1001"))