# Check whether the array is in sorted order with recursion
def isArrayInSorted(A):
    if len(A)==1:
        return True
    return A[0] <= A[1] and isArrayInSorted(A[1:])
A = [127,100,330,530]
print(isArrayInSorted(A))