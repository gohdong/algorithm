# def solution(board, skill):
#     answer = 0
#     affected_dict = {}
#     for s in skill:
#         if s[0] == 1: # 공격
#             for i in range(s[1],s[3]+1):
#                 for j in range(s[2],s[4]+1):
#                     if (i,j) not in affected_dict:
#                         affected_dict[(i,j)] = board[i][j]
#                     affected_dict[(i,j)] -= s[5]

#         if s[0] == 2: #회복
#             for i in range(s[1],s[3]+1):
#                 for j in range(s[2],s[4]+1):
#                     if (i,j) not in affected_dict:
#                         affected_dict[(i,j)] = board[i][j]
#                     affected_dict[(i,j)] += s[5]

#     cols = len(board[0])
#     rows = len(board)
#     total = cols*rows
#     for row in range(rows):
#         for col in range(cols):
#             for s in skill:
#                 if s[1] <= row <=s[3] and s[2] <= col <= s[4]:
#                     if s[0] == 1:
#                         board[row][col] -= s[5]
#                     else:
#                         board[row][col] += s[5]
#             if board[row][col] <= 0:
#                 total-=1

#     return total


# def print_board(a):
#     for x in a:
#         print(x)




# def solution(board, skill):
#     answer = 0
#     total_building = len(board) * len(board[0])
#     affected_dict = {}
#     for s in skill:
#         if s[0] == 1: # 공격
#             for i in range(s[1],s[3]+1):
#                 for j in range(s[2],s[4]+1):
#                     if (i,j) not in affected_dict:
#                         affected_dict[(i,j)] = board[i][j]
#                     affected_dict[(i,j)] -= s[5]

#         if s[0] == 2: #회복
#             for i in range(s[1],s[3]+1):
#                 for j in range(s[2],s[4]+1):
#                     if (i,j) not in affected_dict:
#                         affected_dict[(i,j)] = board[i][j]
#                     affected_dict[(i,j)] += s[5]

#     for x in affected_dict: 
#         if affected_dict[x]<=0:
#             total_building -= 1

#     return total_building
import numpy

def solution(board, skill):
    answer = 0
    board = numpy.array(board)
    for s in skill:
        if s[0] == 1: # 공격
            board[s[1]:s[3]+1,s[2]:s[4]+1] -= s[5]
            # for i in range(s[1],s[3]+1):    
            #     board[i][s[2]:s[4]+1] = [x-s[5] for x in board[i][s[2]:s[4]+1]]

        if s[0] == 2: #회복
            board[s[1]:s[3]+1,s[2]:s[4]+1] += s[5]

    for x in board:
        print(list(x).count(lambda x : 0))
        # for a in x:
        #     if a >0:
        #         answer+=1

    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))