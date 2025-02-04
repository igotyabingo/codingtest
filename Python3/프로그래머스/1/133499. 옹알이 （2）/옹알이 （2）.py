def solution(babbling):
    answer = 0
    
    for i in babbling:
        if check(i):
            answer += 1
            
    return answer

# 발음할 수 있는 단어인지 확인하는 함수를 따로 정의한다.
def check(word):
    pos = 0
    prev = ''
    while(pos<len(word)):
        if(word[pos]=='a' or word[pos]=='w'):
            if(pos+2<len(word)):
                k = word[pos:pos+3]
                if(k!= prev and (k=='aya' or k=='woo')):
                    pos += 3
                    prev = k
                else:
                    return False
            else:
                return False
        elif(word[pos]=='y' or word[pos]=='m'):
            if(pos+1<len(word)):
                k = word[pos:pos+2]
                if(k!= prev and (k=='ye' or k=='ma')):
                    pos += 2
                    prev = k
                else:
                    return False
            else:
                return False
        else:
            return False

    return True

# 훨씬 깔끔한 코드

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')    # 4가지의 각 패턴에 대해 연속하는 경우를 확인하고, 각 패턴을 모두 공백으로 치환시킨다.
        if len(i.strip())==0:    # 공백 제거 했을 때의 길이가 0인 경우 패턴만 존재하는 것이므로 answer을 1 증가시킨다.
            answer +=1
    return answer
