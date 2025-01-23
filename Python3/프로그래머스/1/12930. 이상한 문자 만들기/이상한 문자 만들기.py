def solution(s):
    answer = ''
    # 1. 문자열을 공백 기준으로 나눠 <각 단어별로> 리스트로 바꾼다.
    word = ''
    for i in s:
        if(i == ' '):
            if word:
                s = [i for i in word]
                for i, j in enumerate(s):
                    if(i%2 == 0):
                        s[i] = j.upper()
                    else:
                        s[i] = j.lower()
                answer += ''.join(i for i in s)
                word = ''
            answer += " "
        else:
            word += i
    if word:
        s = [i for i in word]
        for i, j in enumerate(s):
            if(i%2 == 0):
                s[i] = j.upper()
            else:
                s[i] = j.lower()
        answer += ''.join(i for i in s)

    return answer