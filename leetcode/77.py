class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        num_list = [i for i in range(1,n+1)]
        
        def dfs(list1,list2):
            if(len(list1)==k):
                answer.append(list1)
                return
            
            for i in list2:
                if(not list1 or i > list1[-1]):
                    temp1 = list1[:]
                    temp2 = list2[:]
                    temp1.append(i)
                    temp2.remove(i)

                    dfs(temp1,temp2)
        
        dfs([],num_list)
        
        return answer