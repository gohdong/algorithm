class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buy = -1
        if(prices == sorted(prices, reverse=True)):
            return 0
        
        for i in range(0,len(prices)):
            if(not i+1 >= len(prices)):
                if(prices[i+1] >= prices[i]):
                    # if(buy != 0):
                        
                    # else:
                    if(buy == -1 ):
                        buy = prices[i]
                else:
                    if(buy != -1):
                        print(i,prices[i],buy)
                        answer += prices[i]-buy
                        buy = -1
                        
            if(i == len(prices)-1 and buy != -1):
                answer += prices[i]-buy
                    
        
        return answer

        