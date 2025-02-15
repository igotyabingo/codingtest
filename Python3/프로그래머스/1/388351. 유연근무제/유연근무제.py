def solution(schedules, timelogs, startday):
    answer = 0
    # 주말을 제외하고 모든 날짜에 설정시각 + 10분까지 출근한 직원들의 수를 리턴한다.
    
    # startday를 고려하여 고려해야할 인덱스 (5개) 를 정리해둔다.
    con = [i for i in range(7) if (startday+i) not in [6, 7, 13]]
    
    for i, j in enumerate(schedules): # 한명씩 확인한다.
        limit = convert(j)+10
        answer += 1
        for k in [timelogs[i][p] for p in con]:
            if convert(k) > limit:
                answer -= 1
                break
        
    return answer

# 시간, 분 => 분으로 변환한다.
def convert(time):
    hour = time // 100
    minute = time % 100
    return hour*60 + minute