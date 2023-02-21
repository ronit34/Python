s = "1 w 2 r  3g"
b = s.split(" ")
a = []
for i in b: 
    q = i.capitalize()
    a.append(q)

d = " ".join(a)
print(d)
