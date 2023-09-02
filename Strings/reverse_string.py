def Reverse(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
print(Reverse("Rishabh") )

s1 = "Hello World"
print(s1[::-1])