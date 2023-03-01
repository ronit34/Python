# any()
# print(any([1>0,1==0,1<0]))
# print(any([1<0,2<1,3<2]))

# all()
# print(all(['a'<'b','b'<'c']))
# print(all(['a'<'b','c'<'b']))

n = int(input())
new_l = input().split()
print(all(int(i) > 0 for i in new_l) and any(j == j[::-1] for j in new_l))
    





