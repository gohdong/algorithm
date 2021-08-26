import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if(len(scoville) ==1 and scoville[0]<K):
            answer = -1
            break
        if(scoville[0] >= K):
            break
        answer += 1
        temp1 = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        heapq.heappush(scoville,temp1 + 2*temp2)
        
        
        
    
    # print(sorted(scoville))
    
    
    
    return answer