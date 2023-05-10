from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridges = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)

    while bridges:
        x = bridges.popleft()
        answer += 1
        if truck_weights:
            if sum(bridges) + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridges.append(truck)
            else:
                bridges.append(0)
    return answer