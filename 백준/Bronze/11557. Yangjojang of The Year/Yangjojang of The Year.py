t = int(input())

for i in range(t):
    n = int(input())
    max = 0
    mname = ""
    for n in range(n):   
        name, num = input().split()
        num = int(num)
        if num > max:
            max = num
            mname = name
    print(mname)