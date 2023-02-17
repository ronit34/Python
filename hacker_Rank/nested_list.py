n = int(input())
students = []

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

# Find the second lowest score
scores = set([student[1] for student in students])
second_lowest_score = sorted(scores)[1]

# Find the names of all students with the second lowest score
names = sorted([student[0] for student in students if student[1] == second_lowest_score])

# Print the names of the students
for name in names:
    print(name)
