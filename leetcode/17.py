class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        answer = []
        index = 0
        path = ""
        
        def dfs(index:int, path:str):
            if len(path) == len(digits):
                answer.append(path)
                return
            
            for i in num_dict[digits[index]]:
                dfs(index+1,path + i)
                
                
                
        
        num_dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        dfs(index,path)
        
        return answer