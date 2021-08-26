def solution(n, lost, reserve):
    answer = 0
    
    new_lost = list(set(lost)-set(reserve))
    new_reserve = list(set(reserve)-set(lost))
    
    # print(new_lost)
    # print(new_reserve)
    temp = new_lost[:]
    
    for i in temp:
        if i in new_reserve:
            new_lost.remove(i)
            new_reserve.remove(i)
            continue
        if i-1 in new_reserve:
            new_lost.remove(i)
            new_reserve.remove(i-1)
            continue
            
        if i+1 in new_reserve:
            new_lost.remove(i)
            new_reserve.remove(i+1)
            continue
    
    return n - len(new_lost)