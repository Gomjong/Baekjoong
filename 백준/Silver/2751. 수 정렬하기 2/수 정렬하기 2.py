import sys
n = int(input())
num = [0]*n

for i in range(n):
    num[i] = int(sys.stdin.readline())
    
num.sort()
for j in num:
    print(j)