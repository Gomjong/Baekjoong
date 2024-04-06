n = int(input())
n_list = [n]

n_list = list(map(int, input().split()))

a = max(n_list)
b = min(n_list)

print(a*b)