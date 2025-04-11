def solution(p):      
    return replay(p)

def check(u): # 올바른 괄호 문자열인지 확인. 스택 이용
    stack = []

    for val in u:
        if val == '(':
            stack.append('(')
        else:
            if stack: stack.pop()
            else: return False
    
    return False if stack else True

def split(w): # w -> u, v
    a, b = 0, 0 # (와 )의 개수를 각각 카운트 함
    
    for i, val in enumerate(w):
        if val == '(':
            a += 1
        else:
            b += 1
        
        if a == b:
            return (w[:i+1], w[i+1:])
        
def replay(s):
    if not s or check(s):
        return s
    
    u, v = split(s)
    
    if check(u):
        return u + replay(v)
    else:
        tmp = ''
        for val in u[1:-1]:
            if val == '(':
                tmp += ')'
            else:
                tmp += '('

        return '(' + replay(v) + ')' + tmp