def onetonAndntoOne(n):
    if n == 0:
        return
    else:
        print(n)
        onetonAndntoOne(n-1)
        print(n)
print(onetonAndntoOne(5))