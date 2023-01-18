k = int(input())
num_list = []
for i in range(k):
    num_list.append(int(input()))
    if num_list[-1] == 0:
        num_list.pop()
        num_list.pop()
    
print(sum(num_list))