def solution(s):
    answer = 0
    # 모든 x에 대해 확인해볼 수 밖에 없다. 확인 과정을 효율적으로 구성한다. 
    target = s
    for x in range(len(s)):
        target = target[1:] + target[0]
        if check(target): answer += 1
        
    return answer

def check(target):  # 스택 구조를 활용한다: [, {, ( 만 담는다.
    stack = []
    for i in target:
        if (i=='[' or i=='{' or i=='('):
            stack.append(i)
        else:
            if(i==']'):
                if(stack and stack[-1]=='['):
                    stack.pop()
                else:
                    return False
            if(i=='}'):
                if(stack and stack[-1]=='{'):
                    stack.pop()
                else:
                    return False
            if(i==')'):
                if(stack and stack[-1]=='('):
                    stack.pop()
                else:
                    return False
    return False if stack else True