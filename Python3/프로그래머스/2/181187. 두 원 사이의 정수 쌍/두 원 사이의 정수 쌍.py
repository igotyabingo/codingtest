import math

def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2):
        answer += math.floor((r2**2-x**2)**0.5) + 1 - math.ceil(max(0, r1**2-x**2)**0.5)

    return 4*(answer+1)