
n, m = map(int, input().split())

marks = []
for i in range(m):
    marks.append(list(map(float, input().split())))


for student_marks in zip(*marks):
    avg = sum(student_marks) / len(student_marks)
    # print("{:.1f}".format(avg))
    print(avg)