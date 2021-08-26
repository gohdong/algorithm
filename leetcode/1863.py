class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer = 0
        subsets = []

        def subset(n: List, index: int):

            subsets.append(n)

            if index == len(nums) - 1:
                return

            for i, j in enumerate(nums):
                if i > index:
                    subset(n + [j], i)

        subset([], -1)

        for s in subsets:
            temp = 0
            for e in s:
                temp ^= e

            answer += temp

        return answer