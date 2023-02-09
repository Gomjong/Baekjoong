import sys
input = sys.stdin.readline
n, s = map(int, input().split())
cow_list = []
cnt = 0 
for _ in range(n):
    cow_list.append(int(input()))
cow_list.sort()

for i in range(n):
    for j in range(i+1, n):
        if cow_list[i] + cow_list[j] <= s:
            cnt +=1
print(cnt)
            