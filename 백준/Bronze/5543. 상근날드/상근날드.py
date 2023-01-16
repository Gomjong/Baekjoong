menu = []
for i in range(5):
    menu.append(int(input()))
print(min(menu[0:3])+min(menu[3:5])-50)
