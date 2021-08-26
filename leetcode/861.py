class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        
        def flip_col(i : int):
            for a in A:
                a[i] = int(not a[i])
        
        res = 0
        
        for a in A:
            if(a[0] == 1):
                for x in range(len(a)):
                    a[x] = int(not a[x])
                    
        # print(sorted(A))
        # A.sort()
        print(A)
        flip_col(0)
        print(A)
        
        for i,_ in enumerate(A[0]):
            zero_count = 0
            one_count = 0
            for a in A:
                if(a[i] == 0):
                    zero_count +=1
                else:
                    one_count +=1
            if(zero_count>=one_count):
                flip_col(i)
#             if a == 0:
#                 for b in range(len(A)):
#                     A[b][i] = int(not A[b][i])
        
        print(A)
        for a in A:
            temp = ''
            for x in a:
                temp += str(x)
            res += int(temp,2)
            
        return res
            
#     def row_sum_binary(i):
#         res = 0
#         for index,a in enumerate(A[i]):
#             res += 2**(len(A[i])-index-1)*a
        
#         return res