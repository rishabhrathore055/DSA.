num = int(input("Enter a number: "))
def sum_of_num_1(num):
    return (num * (num + 1)) / 2 #Constant time complexity

def sum_of_num_2(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i #Linear time complexity
    return sum

print("Sum of first", num, "natural numbers is: ", sum_of_num_1(num))