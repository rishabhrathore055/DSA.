import array
arr = array.array('i',[1,2,3,4])

# print("The new created array is : ",end=" ")
# for i in range(len(arr)):
#     print(arr[i],end=" ")

print("\n")
# arr.append(5) # append add the new value in the end of the array
# for i in range(len(arr)):
#     print(arr[i],end=" ")
# arr.insert(5,6) # insert the new value in the 5th position of the array
# print("\r")
# for i in range(len(arr)):
#     print(arr[i],end=" ")

# arr.pop() # remove the the last element from the array
# for i in range(len(arr)):
#     print(arr[i],end=" ")

# arr.pop(0) # pop with arguments/ position it remove the position element from the array
# for i in range(len(arr)):
#     print(arr[i],end=" ")

# some other functions
# remove it remove the first occurrence of the value from the array
# index it return the index of first occurrence
# reverse it return reverse form of the array

arr = [1,2,3,4,5,6]

## operation in array

# Display the array
def Display(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
# Display(arr)

# Append/add the element in the array
def add(arr, value):
    arr.append(value)
    Display(arr)

while True:
    choice = int(input("Enter the choice 1. Display 2. Add 3. Exit"))
    if choice == 1:
        Display(arr)
    elif choice == 2:
        value = int(input("Enter the value"))
        add(arr,value)
    elif choice == 3:
        break


