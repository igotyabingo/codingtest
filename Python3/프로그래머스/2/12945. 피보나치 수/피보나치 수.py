def solution(n):
    # 앞선 계산값들을 배열에 저장해둔다. (시간 복잡도)
    fib = [0, 1, 1, 2]
    for i in range(4, n+1):
        fib.append(fib[i-1]+fib[i-2])
    
    return fib[n]%1234567

# 파이썬의 특징인 swap을 이용하여 더 쉽게 구현할 수 있다.
'''
a, b = 1, 0
for i in range():
    a, b = a+b, a
'''
