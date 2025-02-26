def solution(progresses, speeds):
    answer = []
    l = len(progresses)
    # 각각 몇일 걸리는지 계산
    days = [0 for _ in range(l)]
    for i in range(l):
        days[i] = (100-progresses[i])//speeds[i]
        if((100-progresses[i])%speeds[i] != 0):
            days[i] += 1
    arm = 0 # '부터' 배포해야 함을 표시하는 포인터 ('큐')
    stand = days[0] # 배포하지 않은 것중 가장 앞의 기능의 소요 일수

    while(arm < l):
        for i in range(arm+1, l):
            if(days[i]>stand):
                break
        if(i== l-1 and days[-1]<= stand):
            answer.append(i-arm+1)
            break
        else:
            answer.append(i-arm)
            arm = i
            stand = days[i]
        
    return answer