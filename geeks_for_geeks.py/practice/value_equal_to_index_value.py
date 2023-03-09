n = 5
arr = [15, 2, 45, 12, 7,6]
a = []
for i,item in enumerate(arr):
    print(i+1,item)
    if item == i+1:
        a.append(item)
print(a)
