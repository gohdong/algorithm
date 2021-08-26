class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        
        for i in range(len(nums)):
            left = 0
            right = len(nums)-1
            
            while left<right:
                if(left == i):
                    left+=1
                    continue
                    
                if(right == i):
                    right -=1
                    continue
                
                temp = nums[i] + nums[left] + nums[right]
                
                if(temp > 0):
                    right -=1
                elif(temp <0):
                    left +=1
                else:
                    answer.append(tuple(sorted((nums[i],nums[left],nums[right]))))
                    right -=1
                    left +=1
        
        
        return list(set(answer))
                