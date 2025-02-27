def solution(cacheSize, cities):
    answer = 0

    if(cacheSize == 0):
        return 5*len(cities)

    for i, j in enumerate(cities):
          cities[i] = j.lower()

    cache = []
    
    for i in cities:
        if i in cache:
            answer += 1
            cache.pop(cache.index(i))
        else:
            answer += 5
            if len(cache) == cacheSize: cache.pop(0)
        cache.append(i)
    
    return answer

# cache = collections.deque(maxlen=cacheSize)
