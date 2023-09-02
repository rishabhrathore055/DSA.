txt = input("Enter text here : ")
pattern = input("Enter pattern here : ")

par = txt.find(pattern)
while par>=0:
    print(par)
    par = txt.find(pattern,par+1)