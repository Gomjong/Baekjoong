import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = []
s= [0]
a = list(map(int, input().split()))
start = 0
end = k
temp = 0
max_sum = 0
for i in a:
    temp += i
    s.append(temp)


while end <= n:
    sum = 0
    sum = s[end] - s[start]
    if sum > max_sum:
        max_sum = sum
    elif max_sum == 0:
        max_sum = sum
    start += 1
    end += 1
print(max_sum)