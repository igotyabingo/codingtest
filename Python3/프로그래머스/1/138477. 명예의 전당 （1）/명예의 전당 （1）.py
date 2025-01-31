def solution(k, score):
    answer = [] # 발표 점수 (리턴 값, 길이: len(score))
    mei = []    # 명예의 전당 (길이: k)
    
    for i in score: 
        # 1. 명예의 전당에 포함시킬지 확인
        if len(mei) < k:
            # 처음 k일이 지나기 전
            mei.append(i)
        else:
            # 이후
            if i > min(mei):
                mei.sort()
                mei[0] = i
            
        # 2. 업데이트된 명예의 전당을 기준으로 최솟값을 발표한다.
        answer.append(min(mei))    
        
    return answer