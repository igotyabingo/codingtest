from collections import deque

def solution(bridge_length, weight, truck_weights):
    time, sum = 0, 0
    bridge = deque(maxlen = bridge_length)
    for _ in range(bridge_length):
        bridge.append(0)

    time = 0
    passed = 0
    l = len(truck_weights)

    while(passed < l):
        tmp = bridge.popleft()
        sum -= tmp
        if tmp != 0: passed += 1

        if truck_weights and truck_weights[0] + sum <= weight:
            sum += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

        time += 1
        
    return time