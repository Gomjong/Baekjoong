num_list = []

for _ in range(5):
    num_list.append(int(input()))
num_list.sort()
print(sum(num_list)//5)
print(num_list[2])