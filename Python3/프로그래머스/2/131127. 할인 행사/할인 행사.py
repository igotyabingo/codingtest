from collections import Counter

def solution(want, number, discount):
    answer = 0
    # 정현이가 원하는 제품과 수를 딕셔너리로 정리한다.
    jh = dict()
    for i, j in enumerate(want):
        jh[j] = number[i]
    # 처음 10일의 할인 제품을 카운터 -> 딕셔너리로 정리한다.
    mart = dict(Counter(discount[:10]))
    if jh == mart:
        answer += 1

    # 반복
    for i in range(10, len(discount)):
        if discount[i] in mart:
            mart[discount[i]] += 1
        else:
            mart[discount[i]] = 1
        if mart[discount[i-10]] == 1:
            del mart[discount[i-10]]
        else:
            mart[discount[i-10]] -= 1
        
        if jh == mart:
            answer += 1
            
    return answer