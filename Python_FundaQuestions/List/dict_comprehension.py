l1 = [1,3,4,3,5]
d1 = {x:x**3 for x in l1}
print(d1)

l2 = [1,2,3,4,5,6]
l3 = ["Python","R","Java","C","C++","JavaScript"]
d2 = {l2[i]:l3[i] for i in range(len(l2))}
print(d2)

d3 = dict(zip(l2,l3))
print(d3)

d4 = {101:"Ram",102:"Radhe",104:"shyaam"}
d5 = {v:k for(k,v) in d4.items()}
print(d5)