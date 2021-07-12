def solution(k, num, links):
    answer = []

    tree = {}
    for n in range(len(num)):
        tree[n] = {
            "val": num[n],
            "left": links[n][0],
            "right": links[n][1],
        }

    def get_child_sum(node):
        a = node['val']
        if node['left'] != -1:
            a += get_child_sum(tree[node['left']])

        if node['right'] != -1:
            a += get_child_sum(tree[node['right']])

        return a

    for t in tree:
        answer.append(get_child_sum(tree[t]))
    # print(tree)
    answer.sort(reverse=True)

    for i in range(k-1):

        answer[0] = answer[0] - answer[1]
        answer.sort(reverse=True)
        print(answer)

    return max(answer)

#
# print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
#                [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1],
#                 [-1, -1]])
#       )
#
# print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
