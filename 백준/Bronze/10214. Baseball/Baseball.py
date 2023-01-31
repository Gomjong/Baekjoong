import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        a += y
        b += k
    if a > b:
        print("Yonsei")
    elif a < b:
        print("Korea")
    else:
        print("Drew")
    