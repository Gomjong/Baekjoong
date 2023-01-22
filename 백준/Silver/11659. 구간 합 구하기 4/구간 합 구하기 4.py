import sys
input = sys.stdin.readline
suNo, quNo = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
cnt = 0

for i in num_list:
    cnt += i
    sum_list.append(cnt)

for _ in range(quNo):
    start, end = map(int, input().split())
    print(sum_list[end]-sum_list[start-1])
    
