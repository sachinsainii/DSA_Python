def palindrome(name):
    left = 0
    right = len(name)-1

    while(left<right):
        if name[left] != name[right]:
            # print("not a palindrome")
            return False
        else:
            left += 1
            right -= 1
            return True
    # print("its a palindrome")
print(palindrome("madam"))


   
