def solution(genres, plays):
    answer = []
    hashmap = {}
    for i in range(0,len(plays)):
        if(not genres[i] in hashmap):
            hashmap[genres[i]] = {
                'count' : plays[i],
                'list' : [[i,plays[i]]]
            }
        else:
            hashmap[genres[i]]['count'] = hashmap[genres[i]]['count']+ plays[i]
            hashmap[genres[i]]['list'].append([i,plays[i]])
            
    for i in hashmap:
        hashmap[i]['list'].sort(key = lambda x: x[1],reverse=True)
                
                
    for i in sorted(hashmap,key=lambda x: hashmap[x]['count'],reverse=True):
        for y in range(0,2):
            answer.append(hashmap[i]['list'][y][0])
            if(len(hashmap[i]['list'])==1):
                break

    return answer