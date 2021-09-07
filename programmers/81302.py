def solution(places):
    answer = []
    direction = {
        'U' : [-1,0],
        'R' : [0 ,1],
        'D' : [ 1,0],
        'L' : [0,-1],
    }
    def check_around(room,i,j,i2,j2):
        is_ok = True
        for d in direction:
            y = i + direction[d][0]
            x = j + direction[d][1]
            if y == i2 and x == j2:
                continue

            elif y <0 or y > 4 or x <0 or x > 4:
                continue
            
            else:
                if room[y][x] == 'P':
                    return False
                
                elif room[y][x] == 'X':
                    continue

                elif i==i2 and j==j2:
                    is_ok = is_ok and check_around(room,y,x,i,j)

        return is_ok

    for room in places:
        flag = 1
        for i,row in enumerate(room):
            if flag:
                for j,object in enumerate(row):
                    if object == 'P':
                        if not check_around(room,i,j,i,j):
                            flag = 0
                            break
        answer.append(flag)


    return answer




print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))