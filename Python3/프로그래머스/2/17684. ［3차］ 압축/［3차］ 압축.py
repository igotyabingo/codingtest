def solution(msg):
    answer = []
    
    # 1. 사전을 초기화 한다.
    dictionary = dict()
    for i in range(26):
        dictionary[chr(65+i)] = i+1
    
    while True:
        # 마지막 집합 처리
        if msg in dictionary:
            answer.append(dictionary[msg])
            break
        else:
            for i in range(1, len(msg)+1):
                if msg[0:i] not in dictionary:  # 0부터 슬라이싱하여 i-1 범위 처리를 하지 않아도 되게 한다
                    answer.append(dictionary[msg[0:i-1]])
                    dictionary[msg[0:i]] = len(dictionary)+1
                    msg = msg[i-1:]
                    break
   
    return answer