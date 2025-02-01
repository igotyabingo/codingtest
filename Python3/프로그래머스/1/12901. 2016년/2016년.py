def solution(a, b):
    # 2 ~ 11월 전체 일수 저장한 리스트 (인덱스: 월 - 2)
    nic = [29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    # 나머지에 따른 인덱스별 요일 리스트
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 1월과 나머지 월을 따로 처리한다.
    if (a == 1):
        return day[(b-1)%7]
    else:
        # range(2, a) 까지 인덱스를 가지고 리스트 값을 다 더한다.
        c = sum(nic[i] for i in range(0, a-2)) + b + 30
        return day[c%7]