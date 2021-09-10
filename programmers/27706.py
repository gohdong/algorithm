def solution(numbers):    
    return sum([x for x in range(0,10)]) -sum(numbers)



def solution1(grid):
    answer = []
    matrix = [list(g) for g in grid]
    print(matrix)
    return answer


print(solution1(["SL","LR"]))