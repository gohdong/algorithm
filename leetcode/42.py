class Solution:
    def trap(self, height: List[int]) -> int:
        
        answer = 0
        
        max_height = 0
        last_max = 0
        
        for i,h in enumerate(height):
            max_height = max(max_height, h)
            
            if h == max_height:
                last_max = i
                
        left = height[:last_max]
        right = height[last_max+1:][::-1]
        
        left_max = 0
        right_max = 0
        
        for l in left :
            left_max = max(left_max,l)

            answer += left_max - l
            
        for r in right:
            right_max = max(right_max,r)

            answer += right_max - r
            
        return answer
            
        