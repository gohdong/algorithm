from itertools import combinations

def solution(relation):
    answer = []
    row_count = len(relation)
    keys = []
    columns = [i for i in range(len(relation[0]))]
    for c in columns:
        keys += list(combinations(columns,c+1)) 
    
    for key in keys:
        temp = set()
        for r in relation:
            temp2 = []
            for k in key:
                temp2.append(r[k])
            temp.add(tuple(temp2))
        if len(temp) == row_count:
            answer.append(set(key))  

    index = 0
    temp3 = set()
    while index < len(answer):
        for i in range(index+1,len(answer)):
            if answer[index].issubset(answer[i]):
                temp3.add(tuple(answer[i]))
        index+=1

    return len([i for i in answer if tuple(i) not in temp3])


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))