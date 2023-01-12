s = input().upper()
s_set = list(set(s))
cnt = []
for i in range(len(s_set)):
    cnt.append(list(s).count(s_set[i]))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(s_set[cnt.index(max(cnt))])