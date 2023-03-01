S = sorted("Sorting1234")
lower = ""
upper = ""
odd = ""
even = ""
for i in S:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    elif int(i) % 2 != 0:
        odd += i
    else:
        even += i


print(lower+upper+odd+even)