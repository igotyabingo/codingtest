from itertools import product

def solution(numbers, target):
    answer = 0
    # (+, -)로 만들 수 있는 모든 len(numbers) 길이의 순서쌍 (product) -> 완전탐색?
    
    cal = [1, -1]
    calculations = list(product(cal, repeat = len(numbers)))
    
    for calculation in calculations:
        tmp = 0
        for i, number in enumerate(numbers):
            tmp += calculation[i]*number
        if tmp == target:
            answer += 1
    
    return answer