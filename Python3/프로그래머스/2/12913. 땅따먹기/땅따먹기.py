# 풀이 정리 필요: dynamic programming 관련

from itertools import product

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][k] for k in range(4) if j!=k])
    
    return max(land[-1])