def solution(n):
    answer = 0
    temp = bin(n)[2:]
    count = 0
    p = 0 
    for i in range(len(temp)-1,-1,-1):
        if temp[i] == '1':
            count += 1
            if i - 1 <0:
                temp = '10'+ temp[1:]
                count -= 1
                p = 2
            
            elif temp[i-1] == '0':
                temp = temp[:i-1] + '10' + temp[i+1:]
                count -= 1
                p = i+1
                break
    
    temp = temp[:p] + '0'*(len(temp[p:])-count) + '1' * count
    
    return int(temp,2)


print(solution())