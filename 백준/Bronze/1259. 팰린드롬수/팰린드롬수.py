while True:
    num = list(map(int, input()))
    if num[0] == 0:
        break
    elif num == num[::-1]:
        print("yes")
    elif num != num[::-1]:
        print("no")