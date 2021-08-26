def solution(clothes):
    answer = 1
    hashmap = {}
    
    for x in clothes:
        if not x[1] in hashmap:
            hashmap[x[1]] = []
        hashmap[x[1]].append(x[0])
    
    

    for x in hashmap:
        answer *= len(hashmap[x])+1
    
    
    return answer -1