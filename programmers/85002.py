from typing import Counter


def solution(weights, head2head):
    answer = []
    for h in range(len(head2head)):
        heavy_win = 0 
        temp = {
            'W' : 0,
            'N' : 0,
            'L' : 0
        }

        for i,b in enumerate(head2head[h]):
            temp[b] += 1
            if b == 'W' and weights[i] > weights[h]:
                heavy_win+=1
                
            

        # temp.update(Counter(head2head[h]))

        win_rate = temp['W'] / (temp['W']+temp['L']) if temp['W'] + temp['L'] else 0
        answer.append([win_rate,heavy_win,weights[h],h+1])


    return [a[3] for a in sorted(answer,key=lambda x : (x[0],x[1],x[2],-x[3]),reverse=True)]


print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))