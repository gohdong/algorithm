class Solution:
    def subsets(self, nums):
        answer = []
        max_len = len(nums)

        def dfs(n_list, index):
            answer.append(n_list)
            if len(n_list) == max_len:
                return

            for i in range(index, len(nums)):
                dfs(n_list+[nums[i]], i+1)

        dfs([], 0)

        return answer