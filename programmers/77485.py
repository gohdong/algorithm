def solution(rows, columns, queries):
    answer = []
    # Generate Matrix
    p = 1
    matrix = []
    for _ in range(rows):
        temp = []
        for _ in range(columns):
            temp.append(p)
            p += 1
        matrix.append(temp)

    for que in queries:
        position = [que[0] - 1, que[1] - 1]

        pivot = matrix[position[0]][position[1]]
        min_n = pivot

        for _ in range(que[1], que[3]):
            position[1] += 1

            matrix[position[0]][position[1]], pivot = pivot, matrix[position[0]][position[1]]
            min_n = min(min_n, pivot)

        for _ in range(que[0], que[2]):
            position[0] += 1
            pivot, matrix[position[0]][position[1]] = matrix[position[0]][position[1]], pivot
            min_n = min(min_n, pivot)

        for _ in range(que[1], que[3]):
            position[1] -= 1
            pivot, matrix[position[0]][position[1]] = matrix[position[0]][position[1]], pivot
            min_n = min(min_n, pivot)

        for _ in range(que[0], que[2]):
            position[0] -= 1
            pivot, matrix[position[0]][position[1]] = matrix[position[0]][position[1]], pivot
            min_n = min(min_n, pivot)

        answer.append(min_n)
    return answer