def MaxSubarraySumOneDelete(arr):
    nodel=arr[0]
    onedelete=float('-inf')
    pre_nodelete=0
    n=len(arr)
    res=arr[0]

    for i in range(1,n):
        pre_nodelete = nodel

        nodel = max(arr[i],nodel+arr[i])

        onedelete = max(pre_nodelete,onedelete+arr[i])

        res = max(res,nodel,onedelete)

    return res

print(MaxSubarraySumOneDelete([1,-2,3,4]))

