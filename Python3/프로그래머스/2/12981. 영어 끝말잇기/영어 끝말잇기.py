def solution(n, words):
    # '이전에 나온 단어인지'를 어떻게 판단할 것인지: 리턴할 값은 쉽게 구할 수 있는 값임
    dic = {}
    prev = words[0][0]
    # 1. 시작 문자 기준으로 dictionary에 차례로 저장해둔다. - 'hash'
    # + 한 글자인 단어, 마지막 문자 확인
    for i, j in enumerate(words):
        k = j[0]
        
        if(len(j) == 1):
            return cal(i, n)
        if(k != prev):
            return cal(i, n)
        if(k not in dic):
            dic[k] = [j]
        else:
            if(j in dic[k]):
                return cal(i, n)
            else:
                dic[k].append(j)
                
        prev = j[-1]
    
    return [0, 0]

def cal(i, n):
    k = (i+1)%n
    if(k==0):
        a = n
    else:
        a = k
        
    return [a, (i-a+n+1)//n]