import re

for _ in range(int(input())):
    try:
        a = re.compile(input())
        print("True")
    except Exception:
        print("False")