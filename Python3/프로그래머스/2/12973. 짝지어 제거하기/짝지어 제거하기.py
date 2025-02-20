def solution(s):
    # 정규표현식 매칭으로 풀면 시간 초과. 스택으로 구현해보자.
    stack = [s[0]]
    
    for i in s[1:]:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    return 0 if stack else 1