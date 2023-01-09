cnt = 0
c_cnt = 0
max = 0

while cnt < 9:
    n = int(input())
    cnt = cnt + 1
    if n > max:
        max = n
        c_cnt = cnt
print(max)
print(c_cnt)