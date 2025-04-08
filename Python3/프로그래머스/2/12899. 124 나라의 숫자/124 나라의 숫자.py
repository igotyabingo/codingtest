# 지수 연산의 정밀도

def solution(n):
    # 1, 2, 4로 만들 수 있는 숫자 중 N번째로 큰 수를 구한다.
    # 구하는 수는 k자리 수의 마지막이거나, (k+1) 자리 수 그룹 중 하나임
    k = 0
    while int(1.5 * (3 ** k - 1)) < n:
        k += 1
    k -= 1  

    until_k = int(1.5 * (3 ** k - 1))

    if n == until_k:
        return '4' * k

    n -= until_k
    answer = ''
    for i in range(k + 1):
        unit = 3 ** (k - i)
        if n <= unit:
            answer += '1'
        elif n <= 2 * unit:
            answer += '2'
            n -= unit
        else:
            answer += '4'
            n -= 2 * unit

    return answer
