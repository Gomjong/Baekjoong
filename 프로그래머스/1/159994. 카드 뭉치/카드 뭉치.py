def solution(cards1, cards2, goal):
    answer = []
    for card in goal:
        if cards1 and cards1[0] == card:
            answer.append(cards1[0])
            cards1.pop(0)
        elif cards2 and cards2[0] == card:
            answer.append(cards2[0])
            cards2.pop(0)   
    if goal == answer:
        return "Yes"
    else:
        return "No"
    


