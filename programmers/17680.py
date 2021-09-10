from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    def cacheHandler(city):
        if cacheSize == 0:
            return 5

        if not cache:
            cache.append(city)
            return 5

        elif city in cache:
            cache.remove(city)
            cache.append(city)
            return 1
        else:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()

            return 5

    for city in cities:
        answer += cacheHandler(city.lower())
    return answer



print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))