import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
x = int(input())
cnt = 0
i = 0
j = n-1
num_list.sort()

while i < j and j <= n-1:
    if num_list[i] + num_list[j] == x:
        cnt += 1
        i += 1
    elif num_list[i] + num_list[j] > x:
        j -= 1
    else:
        i += 1
print(cnt)
        