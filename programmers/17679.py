def solution(m, n, board):
    answer = 0
    trans = [[] for _ in range(n)]
    
    for b in board[::-1]: 
        for i,x in enumerate(b):
            trans[i].append(x) 

    while True:
        buffer = set()
        for x in range(n):
            for y in range(m):
                if x + 1 < n and y+1 < m:
                    if trans[x][y] == trans[x+1][y] == trans[x][y+1] == trans[x+1][y+1] != " ":
                        buffer.update(((x,y),(x+1,y),(x,y+1),(x+1,y+1)))

        if not len(buffer):
            break

        answer+=len(buffer)


        for b in sorted(buffer,key=lambda x : x[0]):
            trans[b[0]][b[1]] = "X"

        for t in trans:
            for _ in range(t.count('X')):
                t.remove('X')
                t.append(" ")

        buffer.clear()

    return answer

def print_board(board):
    for b in board:
        print(b)

# print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'] )) #14
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'] )) #15
# print(solution(4, 5, ['AAAAA', 'AUUUA', 'AUUAA', 'AAAAA'] )) #14
# print(solution(2,2,["AA", "AA"])) # 4
# print(solution(2,2, ["AA", "AB"])) # 0
# print(solution(3,2, ["AA", "AA", "AB"])) # 4
# print(solution(4,2, ["CC", "AA", "AA", "CC"])) # 8
# print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"])) # 12
# print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"])) # 8
# print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])) # 8
# print(solution(5,6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"])) # 24
# print(solution(6,6, ["AABBEE", "AAAEEE", "VAAEEV", "AABBEE", "AACCEE", "VVCCEE "])) # 32
# print(solution(4,4, ["ABCD", "BACE", "BCDD", "BCDD"])) # 8
