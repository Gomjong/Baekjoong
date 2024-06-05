from functools import cmp_to_key
def compare(x,y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
    
def solution(numbers):
    str_numbers = list(map(str, numbers))
    sorted_numbers = sorted(str_numbers, key=cmp_to_key(compare))
    largest_number = ''.join(sorted_numbers)
    
    return str(int(largest_number))