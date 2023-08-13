def seprator(l1):
    Even = []
    Odd = []
    for n in l1:
        if n%2==0:
            Even.append(n)
        else:
            Odd.append(n)
    return Even,Odd


print(seprator(list(map(int,input("Enter a list : ").split()))))
# print(avg_of_list(list(map(int,input("Enter a list : ").split()))))
# print(seprator([10,20,30,23,22,12]))