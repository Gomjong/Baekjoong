a = list(map(int, input().split()))
total = 0
for i in range(len(a)):
    total = a[i]**2 + total
    
print(total%10)