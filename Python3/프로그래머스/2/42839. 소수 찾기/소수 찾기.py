from itertools import permutations

def is_prime(number):
    if number == 0 or number == 1: 
        return False
    target = int(number ** (0.5))
    for i in range(2, target+1):
        if number % i == 0:
            return False
    
    return True
    
def solution(numbers):
    answer = 0
    digits = [i for i in numbers]
    s = set()
    for l in range(1, len(digits)+1): # 길이가 1인 ~ len(numbers)인 조합 문자열을 모두 고려한다
        lst = list(permutations(numbers, l))
        for perm in lst:
            s.add(int(''.join(perm)))

    for i in s:
        if is_prime(i): 
            print(i)
            answer += 1
    return answer