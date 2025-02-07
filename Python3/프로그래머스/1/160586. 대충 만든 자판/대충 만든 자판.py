def solution(keymap, targets):
    answer = []
    dic = {}
    # key를 알파벳, value를 순서쌍을 원소로 가지는 리스트 로 하는 딕셔너리 생성
    # value (k번째 키, p번)
    
    for n, i in enumerate(keymap):
        for m, j in enumerate(i):
            if j not in dic:
                dic[j] = (n+1, m+1)
            else:
                if dic[j][1] > m+1: # 더 작게 누르는 경우에만 업데이트한다.
                    dic[j] = (n+1, m+1)

    for i in targets:
        print(i)
        p = 0
        for j in i:
            if j not in dic:
                answer.append(-1)
                p = 0
                break
            else:
                p += dic[j][1]
        if p!=0:
            answer.append(p)
        
    return answer