arr1 = []
arr2 = []

n, m = map(int, input().split())

for i in range(n):
    arr1.append(list(map(int, input().split())))

for i in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(arr1[i][j] + arr2[i][j], end=" ")
    print()

