class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for _ in range(K):
            A.sort(reverse = True)
            A.append(-A.pop())
        
        
        return sum(A)