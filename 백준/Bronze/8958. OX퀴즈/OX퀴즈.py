n = int(input())
for _ in range(1,n+1):
    OX_list = list(input())
    score = 0
    sum_score = 0
    for ox in OX_list:
        if ox == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)