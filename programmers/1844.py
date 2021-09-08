def solution(maps):
    answer = []
    def next(y1,x1):
        q = []
        direction = {
            'U' : [-1,0],
            'R' : [0,1],
            'D' : [1,0],
            'L' : [0,-1],
        }
        for d in direction:
            y2 = y1 - direction[d][0]
            x2 = x1 - direction[d][1]

            if 0 <= y2 < len(maps) and 0 <= x2 < len(maps[0]) and maps[y2][x2] == 1:
                q.append([y2,x2])

        return q
    maps[0][0] = 0
    q = [[[0,0],1]]

    while q:
        temp = q.pop(0)
        now = temp[0]
        count = temp[1]

        if now == [len(maps)-1,len(maps[0])-1]:
            return count

        nexts = next(now[0],now[1])

        for n in nexts:
            q.append([n,count+1])
            maps[n[0]][n[1]] = 0

    return -1

    # def recursion(y1,x1,count,maps2,visited):
    #     count+=1
    #     if y1 == len(maps)-1 and x1 == len(maps[0])-1:
    #         answer.append(count)
    #         return
        
    #     # temp_map = [row[::] for row in maps2]
    #     # temp_map[y1][x1] = 0
    #     visited.append([y1,x1])


    #     flag = False
        
        
    #     if not flag:
    #         return

    # recursion(0,0,0,maps,[])

    # return min(answer) if answer else -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))