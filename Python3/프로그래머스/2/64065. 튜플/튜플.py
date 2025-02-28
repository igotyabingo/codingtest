def solution(s):
    answer = []
    sets = s[1:-1].split('},{')
    sets[0] = sets[0][1:]
    sets[-1] = sets[-1][:-1]
    
    dic = dict()
    dic[0] = set()
    # 집합의 길이를 키로 가지는 딕셔너리로 정리
    for i in sets:
        c = i.split(',')
        dic[len(c)] = set(int(j) for j in c)
    
    for i in range(1, len(sets)+1):
        answer.append(list(dic[i] - dic[i-1])[0])
    return answer