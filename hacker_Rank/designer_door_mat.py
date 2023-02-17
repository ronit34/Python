N, M = map(int, input().split())

# Create the top half of the mat
for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

# Add the welcome message
print("WELCOME".center(M, "-"))

# Create the bottom half of the mat by mirroring the top half
for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))
