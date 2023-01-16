t = int(input())
xx = 0
yy = 0
for i in range(0,t):
    
    h, w, n = map(int, input().split())
    yy = n % h
    xx = n // h + 1
    if yy == 0:
        yy = h
        xx -= 1
    print(yy*100+xx)