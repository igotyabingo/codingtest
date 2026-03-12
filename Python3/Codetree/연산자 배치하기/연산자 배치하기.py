n = int(input())

# 연산자 간의 우선 순위를 무시하고 앞에서부터 차례대로 (두 정수) 연산한다.
# 덧셈, 뺄셈, 곱셈의 각 개수가 조건으로 주어짐
# 가능한 식의 최솟값과 최댓값을 출력
import sys
min_val = sys.maxsize
max_val = -sys.maxsize

# 모든 경우 탐색
# '경우'를 어떻게 표현할 것인가?
# 덧셈 자리 찾기 -> 뺄셈 자리 찾기 -> 나머지: 곱셈? -> n중 for문으로

nums = list(map(int, input().split()))
limits = list(map(int, input().split()))

from itertools import combinations

lst = set([i for i in range(n-1)])

for p_idx in combinations(lst, limits[0]):
    lst_except_p = set([i for i in range(n-1) if i not in p_idx])
    for m_idx in combinations(lst_except_p, limits[1]):
        mul_lst = set([i for i in range(n-1) if i not in p_idx and i not in m_idx])

        # 계산
        value = nums[0]
        for i in range(n-1):
            if i in p_idx: # '+'
                value += nums[i+1]
            elif i in m_idx: # '-'
                value -= nums[i+1]
            else: # '*'
                value *= nums[i+1]
        
        min_val = min(min_val, value)
        max_val = max(max_val, value)

print(f"{min_val} {max_val}")