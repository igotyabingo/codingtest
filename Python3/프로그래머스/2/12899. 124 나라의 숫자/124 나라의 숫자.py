def solution(n):
    # 자리수 k 구하기
    k = 0
    while int(1.5 * (3 ** k - 1)) < n:
        k += 1
    k -= 1  # 초과했으므로 하나 빼줌

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
