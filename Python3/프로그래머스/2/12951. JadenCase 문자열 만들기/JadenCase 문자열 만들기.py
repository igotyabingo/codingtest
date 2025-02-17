def solution(s):
    # 공백문자가 연속해서 나오는 경우 리턴시 똑같이 여러개를 붙여 출력해야 하는 것에 주의한다.
    # --> s.split(' ') 을 수행하면 하나 초과의 공백은 '' 로 split 배열에 포함된다.
    answer = ''
    lst = s.split(' ')
    
    for i in lst:
        if i== '':
            answer += ' '
            
        else:
            answer += i[0].upper()+i[1:].lower()
            answer += ' '
    return answer[:-1]