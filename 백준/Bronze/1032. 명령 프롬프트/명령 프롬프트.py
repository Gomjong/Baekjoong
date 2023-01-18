n = int(input())
first_list = list(input())

for i in range(n-1):
    cmd_list = list(input())
    for j in range(len(first_list)):
        if first_list[j] != cmd_list[j]:
            first_list[j] = "?"
            
print(''.join(first_list))
