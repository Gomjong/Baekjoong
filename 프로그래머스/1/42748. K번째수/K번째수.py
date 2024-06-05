def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start, end, k = commands[i]
        sorted_array = sorted(array[start-1:end])
        answer.append(sorted_array[k-1])
        
    return answer