import sys
def solution(n, data, limit):
    answer = []
    time_limit = sys.maxsize if int(limit.split(' ')[0]) == 0 else int(limit.split(' ')[0])
    space_limit = sys.maxsize if int(limit.split(' ')[1]) == 0 else int(limit.split(' ')[1])
    comb = []
    algo_dict = {}
    possible_answer = []

    def comb_generator(c, l):
        if c == n + 1:
            comb.append(l)
            return

        if str(c) in algo_dict:
            for algo in algo_dict[str(c)]:
                # if c == 1:
                #     comb_generator(c + 1, [algo])
                # else:
                comb_generator(c + 1, l + [algo])

    for d in data:
        temp = d.split(' ')
        if temp[1] not in algo_dict:
            algo_dict[temp[1]] = []
        algo_dict[temp[1]].append([temp[0]] + [int(a) for a in temp[2:]])
    # for i in range(1, n + 1):
    #     print(algo_dict[str(i)])
    comb_generator(1, [])
    # print(comb)
    for c in comb:
        temp = [[], 0, 0]
        for d in c:
            temp[0].append(d[0])
            temp[1] += d[1]
            temp[2] += d[2]

        if temp[1] <= time_limit and temp[2] <= space_limit:
            possible_answer.append(temp[0] + [temp[1] + temp[2]])

    # print(possible_answer)
    ## 마지막에 효율성 항목을 추가 해놓음, 그거 기준으로 정렬 하고 그거 제외하고 리턴해줌
    return [] if not possible_answer else sorted(possible_answer, key=lambda x: x[-1])[0][:-1]


# 2, ["a1 1 6 6", "a2 1 2 9", "b1 2 3 3", "b2 2 4 1"], "0 0"
# 1, ["a1 1 1 4", "a2 1 4 1", "a3 1 2 3", "a4 1 2 2"], "3 5"
# 3, ["a1 1 5 9", "a2 1 9 5", "b1 2 3 3"], "0 0"
# 3, ["a1 1 1 4", "a2 1 4 1", "a3 1 3 3", "b1 2 5 6", "b2 2 1 4", "b3 2 4 2", "c1 3 3 6", "c2 3 6 3"], "10 10"