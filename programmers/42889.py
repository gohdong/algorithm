from collections import Counter

def solution(N, stages):
    temp = []
    players = len(stages)
    a = Counter(stages)

    for s in range(1,N+1):
        if s in a :
            temp.append([s,a[s] / players])
            players -= a[s]
        else:
            temp.append([s,0])

    return [y[0] for y in sorted(temp,key=lambda x:x[1],reverse=True)]