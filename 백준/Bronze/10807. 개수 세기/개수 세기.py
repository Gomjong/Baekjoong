n = int(input())
num_list = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(0, n):
    if num_list[i] == v:
        cnt += 1
print(cnt)
