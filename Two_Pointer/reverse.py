def reverse_string(name):
    name = list(name)
    left = 0
    right = len(name)-1
    while(left<right):
        name[left],name[right]=name[right],name[left]
        left += 1
        right -= 1

    return "".join(name)
print(reverse_string("sachin"))


def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left += 1
        right -= 1
    return arr
print(reverse_list([1,2,3,4,5]))