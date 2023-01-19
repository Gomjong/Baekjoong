h, m, s = map(int, input().split())
ct = int(input())
total = h*3600+m*60+s
cooktime = total + ct
if cooktime>=86400:
    cooktime = cooktime-(86400*(cooktime//86400))
print(cooktime//3600, cooktime%3600//60, cooktime%60)