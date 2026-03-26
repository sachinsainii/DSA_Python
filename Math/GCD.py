def GCD(n1,n2):
    # if n1>n2:
    #     n1=n1%n2
    #     return n1
    # else:
    #     n2=n2%n1
    #     return n2

    while n2 != 0:
        n1,n2=n2,n1%n2
    return n1
    
print(GCD(6,12))