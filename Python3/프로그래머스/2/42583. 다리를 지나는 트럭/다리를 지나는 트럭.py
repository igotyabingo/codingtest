from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 새로 다리에 올라올 때는 1초에 한대씩만 올라올 수 있음
    
    on_length = 0 # 다리 위에 있는 트럭 개수
    on_weight = 0 # 다리 위에 있는 트럭 무게 합
    on_time = deque([0]*bridge_length, maxlen = bridge_length) # 1초씩 이동 (각 원소: 트럭 무게)

    t = 0
    # 각 초마다 확인, 업데이트
    trucks = deque(truck_weights)
    out = 0
    
    while out < len(truck_weights): # 종료 조건
        # 1. 다리를 다 지난 것 부터 빼기 ***
        out_weight = on_time.popleft()
        if out_weight != 0:   
            on_weight -= out_weight
            on_length -= 1
            out += 1
        # 2. 다리 올라올 수 있는 지 확인
        if trucks:
            if on_length + 1 <= bridge_length and on_weight + trucks[0] <= weight:
                in_weight = trucks.popleft()
                on_length += 1
                on_weight += in_weight
                on_time.append(in_weight)
            else:
                on_time.append(0)

        # 3. 시간 +1
        t +=1 
        
    
    return t
        