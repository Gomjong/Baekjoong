a, b = map(int, input().split( ))

if a == 0 and b < 45:
    a = 24

if b > 44:
    print(a, b-45)
else:
    print(a-1, b+15)
