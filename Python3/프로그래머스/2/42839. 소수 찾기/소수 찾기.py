from itertools import permutations

def solution(numbers):
    answer = 0
    # numbers의 길이가 최대 7이므로 모든 경우의 수를 생각해보아도 시간 복잡도가 크지 않다.
    digits = [i for i in numbers]
    com = set()
    
    for l in range(1, len(numbers)+1):
        lst = list(permutations(digits, l))
        for l in lst:
            com.add(int(''.join(l)))
    
    for c in com:
        if check(c):
            answer += 1
    
    return answer

# 소수인지 판별하는 함수
def check(n):
    if n==1 or (n!=2 and n%2==0):
        return False
    elif n==2:
        return True
    else:
        for i in range(3, int(n**(1/2))+1):
            if(n%i == 0):
                return False
    
    return True