def solution(s):
    # use stack. 무조건 빈 상태로 함수가 종료되어야 함
    stack = []
    
    for c in s:
        if c == '(': # (만 넣는다.
            stack.append(1)
        else:
            if stack: # (이 하나라도 있는 경우
                stack.pop()
            else:
                return False
    
    return True if not stack else False
            
