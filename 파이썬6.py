import sys

for line in sys.stdin.readlines()[1:]:
    a, b = map(int, line.split())
    print(a + b)
