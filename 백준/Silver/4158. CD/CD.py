from collections import defaultdict
import sys
input = sys.stdin.readline

while True:
    cd = defaultdict(bool)
    n, m = map(int, input().split())
    cnt = 0
    if n == 0 and m == 0:
        break
    for _ in range(n):
        cd[int(input())] = True
    for _ in range(m):
        if cd[int(input())]:
            cnt += 1

    print(cnt)