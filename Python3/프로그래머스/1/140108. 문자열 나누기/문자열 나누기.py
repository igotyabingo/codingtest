def solution(s):
    answer = 1
    # 분해한 문자열의 '개수'를 리턴하는 것이므로, 직접 분해까지 수행할 필요가 없다.
    
    standard = s[0] # 일단 첫번째 문자를 기준으로 확인해야 한다
    cnt1 = 1 # standard와 같은 문자의 개수를 셀 변수
    cnt2 = 0 # standard와 다른 문자의 개수를 셀 변수
    
    for i in range(1, len(s)-1):
        if(s[i] == standard):
            cnt1 += 1
        else:
            cnt2 += 1
            
        if(cnt1 == cnt2):
            answer += 1
            standard = s[i+1]
            cnt1 = 0
            cnt2 = 0
    
    return answer