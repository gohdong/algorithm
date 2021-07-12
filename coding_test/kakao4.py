from collections import defaultdict


def solution(n, start, end, roads, traps):
    answer = [0]
    roads.sort()
    road_dict =
    right_load = defaultdict(list)
    reverse_load = defaultdict(list)

    for r in roads:
        right_load[r[0]].append([r[1], r[2]])
        reverse_load[r[1]].append([r[0], r[2]])

    print(right_load)
    print(reverse_load)

    is_reverse = False

    def dfs(current_location, index, price, reverse, right):
        if current_location == end:
            return


        nonlocal is_reverse
        if is_reverse:
            if not reverse[current_location]:
                return

            if reverse_load[current_location][index][0] in traps:
                is_reverse = False

        else:
            if not right[c]

            if right_load[current_location][index][0] in traps:
                is_reverse = True

        if not is_reverse:
            for r in right_load[current_location]:

    dfs(start, 0, 0, reverse_load.copy(), right_load.copy())

    return min(answer)


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
