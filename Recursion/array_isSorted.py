def ArrayInSortedOrder(arr):
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and ArrayInSortedOrder(arr[1:])

arr = [1, 6, 7, 8, 2,9, 10]
print(ArrayInSortedOrder(arr))