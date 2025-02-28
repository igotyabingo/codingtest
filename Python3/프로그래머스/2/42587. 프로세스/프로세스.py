def solution(priorities, location):
    queue = []  # 프로세스에 이름 붙이기
    dic = dict()    # 프로세스별 우선순위 딕셔너리로 정리
    target = chr(65+location)   # 순서 찾는 프로세스 알파벳 저장
    p = dict()  # 우선순위별 잔여 프로세스 개수 딕셔너리로 정리
    
    for i in priorities:
        if i in p:
            p[i] += 1
        else:
            p[i] = 1
    
    for i in range(len(priorities)):
        queue.append(chr(65+i))  
        dic[chr(65+i)] = priorities[i]
    answer = 0
    
    while(True):
        answer += 1
        mx = max(p)        
        
        while(True):
            k = queue[0]
            
            if dic[k] == mx:
                queue.pop(0)
                p[mx] -= 1
                if p[mx] == 0:
                    del p[mx]
                break
            else:
                queue.append(queue.pop(0))
        if(k == target):
            return answer