n = int(input())
scores = list(map(int, input().split()))

# Find the maximum score
max_score = max(scores)

# Remove all instances of the maximum score
scores = list(filter(lambda x: x != max_score, scores))

# Find the maximum score from the remaining scores
runner_up_score = max(scores)

# Print the runner-up score
print(runner_up_score)
