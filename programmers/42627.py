import heapq as hq

def solution(jobs):
    answer = 0
    count = len(jobs)
    hq.heapify(jobs)
    current_work = []
    will_finish = 0
    now = 0

    waiting_queue = []
    
    while True:
        # print("========================")
        # print(now)
#         print("waiting queue : ", waiting_queue)
#         print("current job : ", current_work)
        
        if(len(jobs)==0 and waiting_queue==[]):
            break
            
        if(not len(jobs)==0 and now >= jobs[0][0]):
            waiting_queue.append(hq.heappop(jobs))
            waiting_queue.sort(key = lambda x : x[1],reverse = True)
            
        if(current_work == []):
            if(waiting_queue != []):
                current_work = waiting_queue.pop() 
                will_finish = now + current_work[1]
                answer += (current_work[1] + now - current_work[0]) 

            
        else:
            if(now == will_finish):
                current_work = []
                if(waiting_queue != []):
                    current_work = waiting_queue.pop()
                    will_finish = now + current_work[1]
                    answer += (current_work[1] + now - current_work[0]) 
            
        now += 1
        # print("≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")

    return answer // count