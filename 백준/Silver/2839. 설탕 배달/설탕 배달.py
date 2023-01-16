sugar = int(input())
bag = 0

while sugar >=0:
    if sugar%5==0:
        print(sugar//5+bag)
        break
    bag += 1
    sugar -=3
else:
    print("-1")