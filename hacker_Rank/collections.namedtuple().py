from collections import namedtuple

N, STUDENT = int(input()), namedtuple('Student', input())

print("{:.2f}".format(sum([int(STUDENT(*input().split()).MARKS) for _ in range(N)]) / N))