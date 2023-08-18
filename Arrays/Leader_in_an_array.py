def leader(l):
    for i in range(len(l)):
        flag = False
        for j in range(i+1,len(l)):
            if(l[i]<=l[j]):
                flag = True
                break
        if flag == False:
            print(l[i])
print(leader([7,10,4,10,6,5,2]))