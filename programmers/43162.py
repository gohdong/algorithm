def solution(n, computers):
    answer = 0

    def dfs(i, j):
        if i < 0 or i >= len(computers) or j < 0 or j >= len(computers[0]) or computers[i][j] == 0:
            return

        computers[i][j] = 0
        computers[j][i] = 0

        for _i in range(len(computers[i])):
            dfs(i, _i)

        for _j in range(len(computers[j])):
            dfs(j, _j)
        #
        # dfs(i - 1, j)
        # dfs(i + 1, j)
        # dfs(i, j - 1)
        # dfs(i, j + 1)

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                dfs(i, j)
                answer += 1

    return answer