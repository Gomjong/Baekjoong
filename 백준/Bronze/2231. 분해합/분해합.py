def find_smallest_constructor(N):
    for M in range(1, N + 1):
        decomposition_sum = M
        temp = M
        
        while temp > 0:
            decomposition_sum += temp % 10
            temp = temp // 10
        
        if decomposition_sum == N:
            return M
    return 0
N = int(input())
result = find_smallest_constructor(N)
print(result)