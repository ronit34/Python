a = int(input())
SET_A = set(map(int, input().split()))

b = int(input())
SET_B = set(map(int, input().split()))
New_set = SET_A.difference(SET_B)
print(len(New_set))