from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[i] for i in rowSum]
        
        for i in matrix:
            for j in range(len(colSum)-1):
                i.append(0)
        
        def get_col_sum(i : int):
            res = 0

            for x in range(len(rowSum)):
                res += matrix[x][i]
                if(res > colSum[i]):
                    temp = res - colSum[i]
                    matrix[x][i+1] += temp
                    matrix[x][i] -= temp
                    res -= temp

        

                
                
        for i in range(len(colSum)-1):
            get_col_sum(i)
                
        return matrix
                    

                
    
    