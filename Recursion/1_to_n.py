def oneto_n(n):
    if n == 0:
        return
    else:
        oneto_n(n-1)
        print(n)
    
oneto_n(5)