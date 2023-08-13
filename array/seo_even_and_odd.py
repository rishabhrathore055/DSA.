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
