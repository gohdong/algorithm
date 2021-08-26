from collections import Counter


def solution(N, stages):
    answer = []
    fail_rate = []

    challengers = len(stages)
    fail_dict = Counter(stages)

    for c in range(1, N + 1):
        if challengers == 0:
            fail_rate.append([c,0])
        else:
            fail_rate.append([c,fail_dict[c] / challengers])
        challengers -= fail_dict[c]

    fail_rate.sort(key=lambda x: x[1],reverse=True)
    return [x[0] for x in fail_rate ]