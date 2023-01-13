cnt = []

for i in range(10):
    n = int(input())
    r = n%42
    cnt.append(r)
print(len(set(cnt)))
