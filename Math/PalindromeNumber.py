def palindromeNumber(n):
    num=n
    rev=0
    while n>0:
        digit = n%10
        rev= rev*10+digit
        n = n//10

    if num==rev:
        return "palindrome"
    else:
        return "not palindrome"

print(palindromeNumber(121))