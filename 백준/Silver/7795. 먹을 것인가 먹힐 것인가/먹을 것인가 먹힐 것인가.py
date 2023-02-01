import sys
sys.stdin.readline
for _ in range(int(input())):
    result = 0
    count = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        while True:
            if count == m or a[i] <= b[count]:
                result += count
                break
            else:
                count += 1
    print(result)
            
    