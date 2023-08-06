import sys

N = int(sys.stdin.readline())
for i in range(2 * N - 1):
    tmp = abs(i - N + 1)
    print(' ' * tmp + '*' * (2 *(N - tmp) - 1))