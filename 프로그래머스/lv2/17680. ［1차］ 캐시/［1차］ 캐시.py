from collections import deque
def solution(cacheSize, cities):
    for index, value in enumerate(cities):
        cities[index] = cities[index].upper()
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = []
    for city in cities:
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
        else:
            idx = cache.index(city)
            cache.pop(idx)
            cache.append(city)
            answer += 1

    return answer