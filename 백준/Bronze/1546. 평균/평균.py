n = int(input())
test = list(map(int, input().split()))
gara = max(test)
sum = 0

for i in range(len(test)):
    sum = sum + test[i]/gara*100
print(sum/n)