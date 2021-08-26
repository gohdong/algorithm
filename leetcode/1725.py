class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_sqr = 0
        count = 0
        for rect in rectangles:
            temp = min(rect)
            if(temp > max_sqr):
                count = 0
            max_sqr = max(max_sqr,temp)
            
            
            
            if(temp == max_sqr):
                count +=1
        return count
            