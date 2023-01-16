num = list(map(int, input().split()))

num.append(num[2]-num[0])
num.append(num[3]-num[1])

print(min(num))