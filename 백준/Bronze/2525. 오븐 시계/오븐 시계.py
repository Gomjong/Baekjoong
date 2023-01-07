h, m = map(int, input().split( ))
ct = int(input())
total = h*60+m
cooktime = total + ct

if cooktime>=1440:
    cooktime = cooktime-1440

print(cooktime//60, cooktime%60)