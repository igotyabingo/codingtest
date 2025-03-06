def solution(n, k):
    answer = 0
    number = ''
    
    # 1. n을 k진수로 변환한다: 변환한 문자열에는 0~k-1 의 숫자만 존재한다.
    if(k == 10):
        number = str(n)
    else:
        while(n >= k):
            number += str(n%k)
            n = n // k
        number += str(n)
        number = number[::-1]
        
    # 2. 조건에 맞는 수를 찾는다: 0을 기준으로 split한다
    candidates = number.split('0')
    
    # 3. 소수인지 확인한다.
    for c in candidates:
        if c and check(int(c)):
            answer += 1
            
    return answer

def check(n):   # 소수인지 확인하는 함수
    if(n == 1): return False
    if(n%2 == 0):
        if(n ==2): return True
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if(n%i == 0): return False
        return True
        