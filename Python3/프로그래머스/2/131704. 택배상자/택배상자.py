def solution(order):
    answer = 0 
    stack = []  # 보조 벨트
    
    for i in range(1, len(order)+1):
        stack.append(i)   # 메인 벨트 처리
        
        # 반복문 변수 설정과, stack - while문 사용
        while (stack and stack[-1] == order[answer]):   
            # order[answer]로 아직 처리되지 않은 order 순차적으로 해결 **
            stack.pop()
            answer += 1
        
        
    return answer