import sys
input = sys.stdin.readline
n = int(input())
vote = list(input())
a, b = 0, 0
for i in range(n):
    if vote[i] == "A":
        a += 1
    else:
        b += 1
if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("Tie")
    