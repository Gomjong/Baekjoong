n = int(input())
for _ in range(n):
    mars = list(input().split())
    sum = 0
    for i in range(len(mars)):
        if i == 0:
            sum = sum + float(mars[i])
        else:
            if mars[i] == "#":
                sum -= 7
            elif mars[i] == "%":
                sum += 5
            elif mars[i] == "@":
                sum *= 3
    print("%0.2f"%sum)