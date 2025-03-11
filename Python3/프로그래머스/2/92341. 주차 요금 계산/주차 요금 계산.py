def solution(fees, records):
    answer = []
    # 차번호: [누적금액, 마지막 입차시간(분), 처리되었는지]
    dic = dict()
    
    for record in records:
        time, car, x = record.split(' ')
        hh, mm = time.split(':')
        time = int(hh)*60 + int(mm)
    
        if x == 'OUT':
            dic[car][0] += time - dic[car][1]
            dic[car][2] = True
        elif car not in dic:
            dic[car] = [0, time, False]
        else:
            dic[car][1] = time
            dic[car][2] = False
            
    dic = sorted(dic.items()) 
    # 금액 계산
    for i in dic:
        time = i[1][0]
        if not i[1][2]:
            time += (23*60+59) - i[1][1]
        
        if(time<=fees[0]):
            answer.append(fees[1])
        else:
            exceed = time-fees[0]
            exceed = fees[3]*((exceed//fees[2])+1*(exceed%fees[2]!=0))  
            answer.append(fees[1]+exceed)

    return answer