def solution(relation):
    answer = 0
    row_count = len(relation)
    column_count = len(relation[0])
    for t in relation:
        print(t)

    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))