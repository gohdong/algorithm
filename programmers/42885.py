from collections import deque

def solution(people, limit):
    answer = 0
    a = deque(sorted(people))

    while a:
        if len(a) > 1:
            if a[0]+a[-1] <= limit:
                a.popleft()
                a.pop()
                answer+=1
            else:
                a.pop()
                answer+=1

        elif len(a) == 1:
            a.pop()
            answer+=1

        else:
            break



    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([30, 30, 70, 70], 100))
