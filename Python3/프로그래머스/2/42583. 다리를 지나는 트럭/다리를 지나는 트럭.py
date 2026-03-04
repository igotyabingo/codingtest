from collections import deque

def solution(bridge_length, weight, truck_weights):
    # use queue.
    truck_weights = deque(truck_weights)
    on_bridge = deque() # [(트럭 무게, 다리에 있었던 시간)]
    # 매 초마다 확인해야 할 것
    # 1. 다리에 있는 것들 다리에 있었던 시간+1 (초기화 = 0): 2면 내보냄
    # 2. 개수 확인 -> 총 무게 확인
    
    sum_weights = 0
    time = 0
    while on_bridge or truck_weights:
        l = len(on_bridge)
        for _ in range(l): # 하나씩 확인한다는 의미
            if on_bridge[0][1] == bridge_length-1:
                sum_weights -= on_bridge[0][0]
                on_bridge.popleft()
            else:
                on_bridge.append((on_bridge[0][0], on_bridge[0][1]+1))
                on_bridge.popleft()
        
        if truck_weights and truck_weights[0] + sum_weights <= weight:
            w = truck_weights.popleft()
            on_bridge.append((w, 0))
            sum_weights += w
                
        time += 1
    
    return time