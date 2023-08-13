def avg_of_list(lst):
    size = len(lst)
    Sum = 0
    for n in lst:
        Sum+=n
    return Sum/size
print(avg_of_list(list(map(int,input("Enter a list : ").split()))))