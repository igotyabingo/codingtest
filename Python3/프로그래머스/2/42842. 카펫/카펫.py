def solution(brown, yellow):
    answer = []
    # yellow = (가로 - 2) * (세로 - 2)
    # brown = (가로*세로) - yellow = 둘레 - 4 
    
    # x + y = (brown + 4) // 2
    # 모든 경우의 수 확인하기 (곱)
    
    # 소수 확인하는 것과 같이 [곱 -> 합] 확인
    # 곱 = brown + yellow
    # 합 = (brown + 4) // 2
    
    mul = brown + yellow
    plus = (brown + 4) // 2
    
    target = int(mul**0.5)
    
    for i in range(1, target+1):
        if mul % i == 0:
            a, b = i, mul//i  # a =< b
            if a + b == plus:
                return [b, a]