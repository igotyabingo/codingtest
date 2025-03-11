def solution(record):
    answer = []
    
    # 들어오고 나간 순서를 저장함 (아이디, IN/OUT) 튜플로
    order = list()
    # 아이디별 최종 닉네임을 업데이트 해나감
    nickname = dict()
    
    for r in record:
        if r[0] == 'E': # Enter
            _, i, n = r.split(' ')
            order.append((i, "IN"))
            nickname[i] = n
        elif r[0] == 'L':   # Leave
            _, i = r.split(' ')
            order.append((i, "OUT"))
        else:   # Change
            _, i, n = r.split(' ')
            nickname[i] = n
            
    for o in order:
        message = f"{nickname[o[0]]}님이 "
        if o[1] == "IN":
            answer.append(message+"들어왔습니다.")
        else:
            answer.append(message+"나갔습니다.")
        
    return answer