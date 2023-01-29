import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
count = 0

for k in range(n):
    i = 0
    j = n -1
    find_k = num_list[k]
    while i < j:
        if num_list[i] + num_list[j] == find_k:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif num_list[i] + num_list[j] < find_k:
            i += 1
        else:
            j -= 1
            
    
print(count)