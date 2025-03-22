import math

def solution(n, k):
    answer = [] # 1~n 이 모두 포함된 정답 배열
    digit = [i for i in range(1, n+1)]# 사용할 수 있는 숫자 

    for i in range(n): # answer의 i번째 원소를 하나씩 결정해나간다.
        tmp = math.factorial(n-1-i)
        idx = math.ceil(k/tmp)-1
        k -= tmp*idx
        answer.append(digit.pop(idx))

    return answer