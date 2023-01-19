while True:
    a, b = map(int, input().split())
    if a == 0:
        break
    elif a > b:
        print("Yes")
    elif a <= b:
        print("No")