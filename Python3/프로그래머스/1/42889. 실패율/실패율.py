def solution(N, stages):
    # <1. 실패율이 높은 것부터> 내림차순으로 스테이지 번호를 배열에 담아 리턴한다: 길이 N인 배열
    # 실패율이 같은 경우 <2. 스테이지 번호가 작은 것부터> 정렬한다.
    
    # {모든 스테이지의 실패율을 구하여} dictionary (key, value)에서 value기준으로 정렬하도록 한다. 
    dic = {}
    # 모든 스테이지의 실패율을 구하기 위해서는 각 stage번호별 개수를 저장해두는 것이 편리할 것이다.
    count = [0 for _ in range(N+2)]
    
    for i in stages:
        count[i] += 1
    
    for i in range(1, N+1):
        k = sum(count[i:])
        if k != 0:
            dic[i] = count[i] / k
        else:
            dic[i] = 0
    
    # dictionary를 value기준 내림차순 정렬한다. (이미 key기준 오름차순 정렬되어있으므로)
    dic = sorted(dic, key=lambda x:dic[x], reverse=True)
    return dic