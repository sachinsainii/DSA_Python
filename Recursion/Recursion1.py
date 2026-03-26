# print name 5 times by using recursion
def Printname(i,n):
    if i>n:
        return
    print("hello")
    Printname(i+1,n)
Printname(1,5)

# print 1 to 5 numbers by using recursion
def fun(i,n):
    if i > n:
        return
    print(i)
    fun(i+1,n)
fun(1,5)

# print 5 to 1 numbers by using recursion
def fun(i,n):
    if i<n:
        return
    print(i)
    fun(i-1,n)
fun(5,1)

# print 1 to 5 numbers by backtracking+recursion
def fun(i,n):
    if i<n:
        return
    fun(i-1,n)
    print(i)
fun(5,1)

# print 5 to 1 numbers by backtracking+recursion
def fun(i,n):
    if i>n:
        return
    fun(i+1,n)
    print(i)
fun(1,5)
