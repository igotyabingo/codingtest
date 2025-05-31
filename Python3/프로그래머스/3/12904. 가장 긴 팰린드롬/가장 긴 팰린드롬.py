def solution(s):
    answer = 1
    test = '#'

    for alp in s:
        test += alp
        test += '#'

    for i, alp in enumerate(test):
        for k in range(1, len(test)):
            if i-k <0 or i+k >= len(test) or test[i-k]!=test[i+k]:
                answer = max(answer, k-1)
                break

    return answer