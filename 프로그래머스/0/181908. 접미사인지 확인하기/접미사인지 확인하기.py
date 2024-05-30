def solution(my_string, is_suffix):
    answer = 0
    if my_string[-len(is_suffix):] == is_suffix:
        answer = 1
    else:
        answer = 0
    return answer