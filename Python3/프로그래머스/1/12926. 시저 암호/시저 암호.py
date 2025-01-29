def solution(s, n):
    answer = ''
    
    # ASCII code 이용
    for i in s:
        # 한 문자씩 확인
        if i.isalpha():
            st = chr(ord(i) + n)
            # 문자가 아닐 경우 / 대문자 -> 소문자로 바뀐 경우
            if (not st.isalpha()) or (i.isupper() and st.islower()):
                st = chr(ord(i) + n - 26)
            answer += st
        else:
            answer += ' '
    
    return answer