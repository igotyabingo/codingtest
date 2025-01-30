def solution(food):
    # 중앙에 있는 물을 기준으로 음식의 종류가 대칭을 이루어야 함 (칼로리가 낮은 것부터)
    # 음식 한 종류의 총 개수는 짝수개여야함
    answer = ''
    
    for i in range(1, len(food)):
        a = food[i]
        if a % 2 == 1:
            a -= 1
        a = a // 2
        answer += str(i)*a
    # 한쪽 문자열 완성
    tag = answer[::-1]
    
    answer = answer + '0' + tag
    
    return answer