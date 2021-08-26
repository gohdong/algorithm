class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(num1_list : list,num2_list : list):
            if not num2_list:
                answer.append(num1_list)
                return
            
            for n in num2_list:
                temp1 = num1_list[:]
                temp2 = num2_list[:]
                temp1.append(n)
                temp2.remove(n)
                dfs(temp1,temp2)
                
                
                
        dfs([],nums)                
        return answer