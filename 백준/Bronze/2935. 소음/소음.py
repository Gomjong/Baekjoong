math = []

for _ in range(3):
    math.append(input())

if math[1] == "*":
    print(int(math[0])*int(math[2]))
elif math[1] == "+":
    print(int(math[0])+int(math[2]))