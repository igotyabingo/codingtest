def solution(plans):
    queue = [] # 지금 처리중인 거 저장
    answer = [] # 다 끝난 거 저장
    stack = [] # 보류해둔 거 저장

    for i, p in enumerate(plans):
        plans[i] = [p[0], calculate(p[1]), int(p[2])]

    plans.sort(key = lambda x: x[1])
    clock = plans[0][1] # 현재시간을 기록해둔다.

    for i in plans: # 하나씩 넣는다.
        if queue: # 처리 중인게 있었던 경우
            tmp = queue.pop(0)
            if tmp[1] + tmp[2] <= i[1]: # 완료
                answer.append(tmp[0])
                clock = tmp[1] + tmp[2]
            else: # 보류시켜야 하는 경우
                stack.append([tmp[0], tmp[2] - (i[1] - tmp[1])])
                clock = i[1]

        while(clock < i[1] and stack): # 시간이 남는 경우
            tmp = stack.pop()
            if (i[1] - clock >= tmp[1]):
                clock += tmp[1]
                answer.append(tmp[0])
            else:
                stack.append([tmp[0], tmp[1]-(i[1]-clock)])
                clock = i[1]

        queue.append(i)

    if queue:
        answer.append(queue[0][0])
        clock = queue[0][1] + queue[0][2]

    while stack:
        answer.append(stack.pop()[0])
        
    return answer

def calculate(time):
    hh, mm = time.split(":")
    return 60*int(hh) + int(mm)