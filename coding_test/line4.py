def solution(n, queries):
    answer = []
    stack_dict = {}
    center = None
    for i in range(n):
        stack_dict[i + 1] = []

    for i,q in enumerate(queries):
        print(q,stack_dict)
        if q[1] > 0:
            if not center:
                center = q[1]
            else:
                stack_dict[q[0]].append(q[1])
        else:

            if stack_dict[q[0]]:
                answer.append(stack_dict[q[0]].pop())
            elif not center:
                answer.append(-1)
                continue
            else:
                answer.append(center)
                center = None
                t = 1
                if i == len(queries)-1:
                    break
                while not center:
                    temp = (q[0] + t) % n if (q[0] + t) % n != 0 else n
                    # print(q[0],stack_dict)
                    if stack_dict[temp]:
                        center = stack_dict[temp].pop(0)
                    t += 1

        # print(q)
        # print(q, center,stack_dict)

    # print(stack_dict)
    return answer


# print(solution(3, [[1, 4], [2, 2], [1, 3], [1, 6], [3, -1], [2, -1]]))
# print(solution(4, [[1, 3], [1, 2], [3, 6],[3,-1],[4,5],[2,-1],[3,-1],[1,-1] ]))
print(solution(	5, [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1]]))