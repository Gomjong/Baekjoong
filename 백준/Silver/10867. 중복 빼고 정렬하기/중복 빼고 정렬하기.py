n = int(input())
num_list = list(map(int, input().split()))
result = []

for i in num_list:
    if i not in result:
        result.append(i)
result.sort()

for j in result:
    print(j,end= ' ')