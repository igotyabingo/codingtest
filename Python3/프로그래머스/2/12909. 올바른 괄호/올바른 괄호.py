def solution(s):
    answer = True
    # stack 자료구조 이용 -> 그냥 스택에 있는 원소 개수로만 판단해도 된다.
    cnt = 0
    # (는 스택에 넣음, )는 ( 하나를 pop시킴
    for ch in s:
        if ch == '(':
            cnt += 1
        else:
            if cnt>0: 
                cnt -=1
            else:
                return False
        
    return True if cnt == 0 else False