n = int(input())
a = 100
b = 100

for _ in range(n):
    chang, sang = map(int, input().split())
    if chang > sang:
        b -= chang
    elif chang < sang:
        a-= sang
print(a)
print(b)