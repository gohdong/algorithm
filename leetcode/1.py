class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {e:i for i,e in enumerate(nums)}
        
        for i,x in enumerate(num_dict):
            if((target - x) in num_dict and i != num_dict[target - x] ):
                return [i,num_dict[target - x]]