def solution(prices):
    answer = [0 for _ in prices]
    
    for x in range(0,len(prices)):
        for y in range(x+1,len(prices)):
            if(prices[y]<prices[x]):
                answer[x]+=1
                break
            else:
                answer[x]+=1        
            
        
            
        
    return answer