def solution(k, d):
    answer = 0
    
    # x, y 대칭성 고려 -> x <= y 크기 관계 고정
    for x in range(0, int(d/1.4) + 1, k):
        # y가 가능한 범위를 바로 계산한다
        tmp = (int((d**2-x**2)**(1/2)) - x) //k + 1
        if tmp > 0: answer += 2*tmp-1

    return answer