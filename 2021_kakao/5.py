from collections import defaultdict


def solution(info, edges):
    answer = 0
    path = defaultdict(list)
    sheep_dict = []
    for e in edges:
        path[e[0]].append(e[1])


    def dfs(node,sheep_count,wolf_count):
        if info[node]:
            wolf_count +=1
        else:
            sheep_count+=1
            sheep_dict.append((node,wolf_count))
        # print(node,sheep_count,wolf_count)
        if node not in path:
            return
        
        for p in path[node]:
            dfs(p,sheep_count,wolf_count)

    dfs(0,0,0)
    sheep = 0
    wolf = 0
    print(sorted(sheep_dict,key=lambda x : (x[1],x[0])))
    for a in sorted(sheep_dict,key=lambda x : (x[1],x[0])):
        wolf += a[1]
        sheep +=1
        if wolf < sheep:
            answer+=1

    return answer

    
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))