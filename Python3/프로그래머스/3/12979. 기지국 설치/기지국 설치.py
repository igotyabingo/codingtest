import math

def solution(n, stations, w):
    # 실제 아파트 번호를 기록하지 않고 수학적으로 풀이한다: 하나의 기지국을 설치하면 -> 2*w+1 만큼이 커버됨
    coverage = 2*w+1
    answer = 0
    pos = 1 # 커버되지 않은 것 중 가장 작은 숫자

    for s in stations:
        start = s - w
        if pos < start:
            answer += math.ceil((start-pos)/coverage)
        pos = s+w+1

    if pos <= n:
        answer += math.ceil((n-pos+1)/coverage)
    
    return answer