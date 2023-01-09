X = int(input())
n = int(input())
total = 0

for i in range(1,n+1):
    a, b = map(int, input().split())
    total = total + a*b
if total == X:
    print("Yes")
else:
    print("No")