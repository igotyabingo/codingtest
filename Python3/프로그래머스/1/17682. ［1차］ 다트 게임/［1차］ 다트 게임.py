import re

def solution(dartResult):
    score = [0, 0, 0]
    # 1회, 2회, 3회의 문자열을 나누어서 계산할 수 있어야 함
    # S, D, T의 위치를 찾고, 앞의 숫자를 다룬 다음 뒤에 옵션이 있는지 확인하여 해당 회차의 점수 계산을 끝냄
    # -> 문자열 패턴 정규식을 사용한다.
    ind = 0 # 계산이 끝난 회차의 끝 문자+1 인덱스를 저장해둠
    
    for i in range(3):  # 3회 반복한다.
        al = re.search(r'[SDT]', dartResult[ind:])
        k = al.start() + ind
        if(al.group() == 'S'):
            p = 1
        elif(al.group() == 'D'):
            p = 2
        else:
            p = 3

        score[i] = int(dartResult[ind:k])**p
        if(len(dartResult)>k+1 and dartResult[k+1]=='*'):
            score[i] *= 2
            if(i != 0):
                score[i-1] *= 2
            ind = k+2
        elif(len(dartResult)>k+1 and dartResult[k+1]=='#'):
            score[i] *= (-1)
            ind = k+2
        else:
            ind = k+1
    
    return sum(score)

# 정규 표현식을 다음과 같이 사용하여 더 깔끔하게 구현할 수 있다.
# p = re.compile('(\d+)([SDT])([*#]?)')
# dart = p.findall(dartResult)
