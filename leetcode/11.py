class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        answer = 0
        while left < right:

            answer = max(answer, (right-left)*min(height[left], height[right]))
                
            if(height[right]<=height[left]):
                right-=1
            else:
                left+=1

        return answer