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