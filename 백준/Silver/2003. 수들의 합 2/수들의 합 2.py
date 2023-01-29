import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
i = 0
j = 1
count = 0

while j<=n and i<=j:
    result = A[i:j]
    total = sum(result)

    if total == m:
        count += 1
        j += 1
    elif total > m:
        i += 1
    else:
        j += 1

print(count)
    