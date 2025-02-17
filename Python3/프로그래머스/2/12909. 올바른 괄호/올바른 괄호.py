def solution(s):
    # 1. )로 시작한 경우 바로 False
    # 2. 스택에서 (-1와 )-2 가 순서대로 만나면 pop하고, s 순회가 끝났는데 스택에 무언가 남아있으면 False
    stack = []
    
    if(s[0] == ')'):
        return False
    else:
        stack.append(1)
        for i in s[1:]:
            if(i=='('):
                stack.append(1)
            else:
                if stack and stack[-1] == 1:
                    stack.pop()
                else:
                    stack.append(2)
        if stack:
            return False
        else:
            return True

# i가 )일때는 스택에 굳이 원소를 추가하지 않고 짝지을 (가 있는지 확인하는 것만으로 충분하다. 
# s를 끝까지 순회하지 않고도 빨리 끝낼 수 있다. 다음 코드의 예외처리문 형태를 확인하자.
        '''
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False
        '''
