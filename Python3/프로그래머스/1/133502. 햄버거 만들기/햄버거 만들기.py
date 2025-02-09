def solution(ingredient):
    # 스택의 구조를 사용해야 한다.
    answer = 0
    stack = []
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])  
        if(stack[-4:]==[1, 2, 3, 1]):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1       
    return answer