def solution(numbers, target):
    answer = 0

    def dfs(index, calc):
        if index == len(numbers)-1 and calc == target:
            nonlocal answer
            answer += 1
        if not numbers[index:]:
            return

        dfs(index + 1, calc + numbers[index])
        dfs(index + 1, calc - numbers[index])

    dfs(-1, 0)
    # dfs(0, -numbers[0])
    return answer