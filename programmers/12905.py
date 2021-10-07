def solution(board):
    max_length = 0
    height = len(board)
    width = len(board[0])
    for i in range(height):
        for j in range(width):
            if board[i][j]:
                if i-1 >= 0 and j -1 >= 0:
                    board[i][j] = min(board[i-1][j],board[i-1][j-1],board[i][j-1])+1
                
                max_length = max(max_length,board[i][j])
                

    return max_length**2


print(solution())