def solution(arr):
    answer = []
    temp = arr[0] - 1
    for i in arr:
        if i != temp:
            temp = i
            answer.append(i)
    print('Hello Python')
    return answer