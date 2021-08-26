class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        emptyBottle = 0
        while numBottles>0:
            answer += numBottles
            emptyBottle += numBottles
            numBottles = 0
            
            numBottles +=  emptyBottle//numExchange
            emptyBottle =  emptyBottle%numExchange
            
        return answer