def solution(survey, choices):
    answer = ''
    # 4개 지표 - 2가지 유형씩: 2*2*2*2 = 16가지 
    # 검사지 n개의 질문 - 선택지 7가지씩
    # 질문 하나 당 지표 하나에 대응됨, 선택지마다 점수 크기는 고정적이지만 동의/비동의 방향성은 동적임
    
    score = [0]*8
    dic = {"R":0, "T":1, "C":2, "F":3, "J":4, "M":5, "A":6, "N":7}
    
    for i in range(len(survey)):
        k = choices[i]
    
        if(k>=1 and k<=3):  # 비동의
            score[dic[survey[i][0]]] += 4-k
        else:   # 동의
            score[dic[survey[i][1]]] += k-4   
        
    if score[0] >= score[1]:
        answer += "R"
    else:
        answer += "T"
    if score[2] >= score[3]:
        answer += "C"
    else:
        answer += "F"
    if score[4] >= score[5]:
        answer += "J"
    else:
        answer += "M"
    if score[6] >= score[7]:
        answer += "A"
    else:
        answer += "N"
    
    return answer