"""
1. Get
2. Set
3. Max
4. Min
5. Sum
6. Avg
"""
import array as arr
arr = arr.array('i', [4,8,10,15,18,21,24,29,33,34,37,39,41,43])

def Get(arr, index):
    if index>=0 and index<=len(arr):
        return arr[index]
    else:
        print("Give the valid Index")

def Set(arr, index, value):
    if index>=0 and index<=len(arr):
        arr.insert(index, value)
        # arr[index] = value
        for i in range(len(arr)):
            print(arr[i], end=" ")
    else:
        print("Give the valid Index")
def Min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i]< min:
            min = arr[i]
    return min
def Max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i]> max:
            max = arr[i]
    return max

def Sum(arr):
    sm = 0
    for i in range(len(arr)):
        sm+=arr[i]
    return sm
def Average(arr):
    return Sum(arr)/len(arr)

while(True):
    print("Enter the choice 1.Get 2.Set 3.Max 4.Min 5.Sum 6.Avg 7.Exit")
    choice = int(input())
    if choice == 1: 
        index = int(input("Enter the index: "))
        print(Get(arr, index))
    elif choice == 2:
        index = int(input("Enter the index: "))
        value = int(input("Enter the value: "))
        print(Set(arr, index, value))
    elif choice == 3:
        print(Max(arr))
    elif choice == 4:
        print(Min(arr))
    elif choice == 5:
        print(Sum(arr))
    elif choice == 6:
        print(Sum(arr)/len(arr))
    elif choice == 7:
        break
   

