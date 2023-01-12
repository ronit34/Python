import random
import time

start = time.time()
a = 0
for numbers in range(100000000):
    numbers = random.randint(6000000000,9999999999)
    strnum = str(numbers)
    a += 1
    print(a)
    with open('10 crore.txt', 'a') as obj:    
        obj.write(strnum)
        obj.write('\n')
end = time.time()
Time = end - start
print(f"{Time} Seconds time to create {a} numbers")
        

# 5598.409481048584 Seconds time to create 100000000 numbers


# ab = 'Hoehdsgujfgcjsgdfjsjfdgjsdsjsdjbsjuhdjmhkhd jasddj jbd diha h jasj khdikd'

        # obj.write('\n')