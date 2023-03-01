n = 5
arr = [1,2,3,4]
c = n*(n+1)//2  
print(c)
sum = 0
for i in arr:
    sum += i
print(sum)    
print(c-sum)    
# for i in range(1,n):
#     if i not in arr:
#         print(i)