# https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

def getMinMax( a, n):
    max = a[0]
    min = a[0]
    for i in range(n):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]
    return min, max

arr = [12,50,1,123,1332]   
print(getMinMax(arr,5))