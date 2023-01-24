import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
number = list(map(int, input().split()))
number.sort()
count = 0
i = 0
j = n - 1

while i<j:
    if number[i] + number[j] == m:
        count += 1
        i += 1
        j -= 1
    elif number[i] + number[j] > m:
        j -= 1
    else:
        i += 1
        
print(count)