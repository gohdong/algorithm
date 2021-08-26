class Solution(object):
    def minDeletionSize(self, A):
        A2 = zip(*A)
        output = 0
        
        for i in range(len(A2)):
            if A2[i] != tuple(sorted(A2[i])):
                output += 1
        
        return output