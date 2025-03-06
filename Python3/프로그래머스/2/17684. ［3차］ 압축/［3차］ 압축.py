def solution(msg):
    answer = []
    
    # 1. 사전을 초기화 한다.
    dictionary = dict()
    for i in range(26):
        dictionary[chr(65+i)] = i+1
    
    while(msg):
        # 2. 현재 입력과 일치하는 가장 긴 문자열을 찾는다.
        val = False
        for i in range(1, len(msg)+1):
            if msg[:i] not in dictionary:
                val = True
                break
        if i>1 and val:
             answer.append(dictionary[msg[:i-1]])      
        else:
             answer.append(dictionary[msg])
        
        if(val):
             dictionary[msg[:i]] = len(dictionary)+1
             msg = msg[i-1:]
        else:
             break
   
    return answer