from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while bridge:
        x = bridge.popleft()

        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                temp = truck_weights.popleft()
                bridge.append(temp)
            else:
                bridge.append(0)

        answer += 1
                
    return answer