n = int(input())
cnt = 0
first_n = n
while True:
    t=n//10+n%10
    n = n%10*10+(t%10)
    cnt += 1
    if first_n == n:
        break
print(cnt)
    