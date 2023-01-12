sum_value = 1
for i in range(1,4):
    n = int(input())
    sum_value = n * sum_value
    
sum_value = str(sum_value)

for i in range(10):
    print(sum_value.count(str(i)))