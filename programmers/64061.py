# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in board:
            if(j[i-1] != 0):
                temp = j[i-1]
                j[i-1] = 0
                if(basket != [] and basket[-1] == temp):
                    basket.pop()
                    answer+=2
                else:
                    basket.append(temp)
                    
                break
                
    return answer