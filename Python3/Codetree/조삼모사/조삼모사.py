# n개의 일을 아침 조합 n/2개, 밤 조합 n/2개 로 분할
# 같은 조합에 있는 경우 상성을 고려하여 강도의 합이 계산됨
# 모든 순서쌍(combination)에 대한 상성을 계산해야 함

# 목표: 아침 조합 강도 합과 저녁 조합 강도 합의 '차이의 최솟값'

# 1. 모든 (n/2개, n/2개) 순서쌍 나누기 (조합)
# *** 아침 <-> 저녁 순서쌍 중복 제거를 위해 항상 0번을 밤에 포함 시킨다.
from itertools import combinations

n = int(input())
idx = set(i for i in range(1, n))

# dictionary 형태로 상성 저장 -> power[i] = list
from collections import defaultdict
power = defaultdict(list)
for i in range(n):
    power[i] = list(map(int, input().split()))

answer = 100*n*n
# 2. 각 순서쌍에 대해 합을 계산함
for candidate in combinations(idx, n//2): 
    dawn = set(candidate)
    dusk = [i for i in range(n) if i not in dawn]

    dawn_sum, dusk_sum = 0, 0

    for i, j in combinations(dawn, 2):
        dawn_sum += power[i][j] + power[j][i]
    for i, j in combinations(dusk, 2):
        dusk_sum += power[i][j] + power[j][i]
    answer = min(answer, max(dawn_sum-dusk_sum, dusk_sum-dawn_sum))

print(answer)