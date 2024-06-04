score_list = list(map(int, input()))

score_list.sort(reverse=True)
for i in range(len(score_list)):
    print(score_list[i], end = "")