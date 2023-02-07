import sys
input = sys.stdin.readline
n, m = map(int, input().split())
user_list = list(map(int, input().split()))
start = 0
end = n-1
cnt = 0
user_list.sort()

while start < end:
    if user_list[start] + user_list[end] >= m:
        cnt += 1
        start += 1
        end -=1
    elif user_list[start] + user_list[end] < m:
        start += 1
print(cnt)

    