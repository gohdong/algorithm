def solution(places):
    answer = []

    distance_one = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

    distance_two = [
        [2, 0],
        [-2, 0],
        [0, 2],
        [0, -2],
        [1, 1],
        [1, -1],
        [-1, -1],
        [-1, 1]
    ]

    def check_distance(room_index, people):
        if not people:
            return 1
        this_room = places[room_index]

        # 거리 1 체크
        for p in people:
            for c in distance_one:
                temp_x = p[0] + c[0]
                temp_y = p[1] + c[1]

                if temp_x < 0 or temp_y < 0 or temp_x >= 5 or temp_y >= 5:
                    continue
                if this_room[temp_x][temp_y] == "P":
                    return 0

        # 거리 2체크

        for p in people:
            for c in distance_two:
                temp_x = p[0] + c[0]
                temp_y = p[1] + c[1]

                if temp_x < 0 or temp_y < 0 or temp_x >= 5 or temp_y >= 5:
                    continue
                if this_room[temp_x][temp_y] == "P":
                    if abs(c[0]) == 1:
                        check1 = [p[0] + c[0], p[1]]
                        check2 = [p[0], p[1] + c[1]]
                        if this_room[check1[0]][check1[1]] != "X" or this_room[check2[0]][check2[1]] != "X":
                            return 0
                    else:
                        if this_room[(temp_x + p[0]) // 2][(temp_y + p[1]) // 2] != "X":
                            return 0

        return 1

        # if i-2 > 0

    def check_room(rooms):
        people = []
        for i in range(5):

            for j in range(5):
                if places[rooms][i][j] == "P":
                    people.append([i, j])
                    # if not check_distance(rooms, i, j):
                    #     answer.append(0)
        answer.append(check_distance(rooms, people))
        # print(people)

    for room in range(5):
        check_room(room)

    return answer


print(solution([["POOOP",
                 "OXXOX",
                 "OPXPX",
                 "OOXOX",
                 "POXXP"],
                ["POOPX",
                 "OXPXP",
                 "PXXXO",
                 "OXXXO",
                 "OOOPP"],
                ["PXOPX",
                 "OXOXP",
                 "OXPXX",
                 "OXXXP",
                 "POOXX"],
                ["OOOXX",
                 "XOOOX",
                 "OOOXX",
                 "OXOOX",
                 "OOOOO"],
                ["PXPXP",
                 "XPXPX",
                 "PXPXP",
                 "XPXPX",
                 "PXPXP"]]))
