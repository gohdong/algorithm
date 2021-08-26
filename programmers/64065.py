def solution(s):
    answer = []
    after_process = pre_processing(s)
    
    for x in after_process:
        answer.append(list(set(x) - set(answer))[0])
    
    return answer


def pre_processing(s : str) -> list:
    temp = s[2:-2].replace('},{',' ').split(' ')
    for x in range(0,len(temp)):
        temp[x] = [int(i) for i in temp[x].split(',')]
    return sorted(temp,key= len)