import sys
input = sys.stdin.readline
check_list = [0]*4
my_list = [0]*4
check_count = 0


def myadd(c):
    global check_list, my_list, check_count
    if c == "A":
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            check_count += 1
    elif c == "C":
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            check_count += 1
    elif c == "G":
        my_list[2] += 1
        if my_list[2] == check_list[2]:
            check_count += 1
    elif c == "T":
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            check_count += 1
            
def myremove(c):
    global check_list, my_list, check_count
    if c == "A":
        if my_list[0] == check_list[0]:
            check_count -= 1
        my_list[0] -= 1
    elif c == "C":
        if my_list[1] == check_list[1]:
            check_count -= 1
        my_list[1] -= 1
    elif c == "G":
        if my_list[2] == check_list[2]:
            check_count -= 1
        my_list[2] -= 1
    elif c == "T":
        if my_list[3] == check_list[3]:
            check_count -= 1
        my_list[3] -= 1

S, P = map(int, input().split())
result = 0
DNA_list = list(input())
check_list = list(map(int, input().split()))
for i in range(4):
    if check_list[i] == 0:
        check_count += 1
for i in range(P):
    myadd(DNA_list[i])
if check_count == 4:
    result += 1

for i in range(P, S):
    j = i - P
    myadd(DNA_list[i])
    myremove(DNA_list[j])
    if check_count == 4:
        result += 1
print(result)