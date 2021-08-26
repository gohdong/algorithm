class Solution:
    def combinationSum(self, candidates, target: int):
        answer = []

        def dfs(temp_sum: int, n_list: list, c_list: list):
            if temp_sum < 0:
                return

            if temp_sum == 0:
                answer.append(n_list)
                return

            for c in range(len(c_list)):
                temp = n_list[:]
                temp.append(c_list[c])
                dfs(temp_sum-c_list[c],temp,c_list[c:])

        dfs(target, [], candidates)
        return answer
