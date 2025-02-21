def solution(n):
    # 피보나치 수와 동일하다. f(n) = f(n-1) + f(n-2): 처음에 1칸/2칸 뛰는 방법의 합
    a, b = 1, 1
    
    for _ in range(n-1):
        a, b = a+b, a
        
    return a%1234567