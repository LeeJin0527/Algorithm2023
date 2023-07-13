from collections import defaultdict
def solution(weights):
    answer = 0
    stores = defaultdict(int)
    for weight in weights:
        answer += (stores[weight] + stores[(2 * weight) / 3] + stores[weight / 2]
                   + stores[(3 * weight) / 2] + stores[(3 * weight) / 4] + 
                   stores[2 * weight] + stores[(4 * weight) / 3])
        stores[weight] += 1                  
    return answer