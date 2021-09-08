def solution(name):
    answer = []
    neet_to_change = [i for i, x in enumerate(name) if x != 'A']
    begin = "A"*len(name)

    if begin == name:
        return 0

    def go_to(now, to_go):
        if now < to_go:
            return min(to_go-now, len(name) - to_go + now)
        else:
            return min(len(name)-now+to_go, now-to_go)
    
    def change_char(target):
        if ord(target) > 78:
            return 91 - ord(target)
        else:
            return ord(target) - 65

    
    def recursion(index,count,temp_list):
        temp = temp_list[::]
        if index in temp_list:
            temp.remove(index)
            count += change_char(name[index])
        if not temp:
            answer.append(count)
            return


        if temp[0] != temp[-1] and go_to(index,temp[0]) == go_to(index,temp[-1]):
            recursion(temp[0],count + go_to(index,temp[0]),temp)
            recursion(temp[-1],count + go_to(index,temp[-1]),temp)
        
        else:
            will_go = temp[0] if go_to(index,temp[0])<=go_to(index,temp[-1]) else temp[-1]
            recursion(will_go,count + go_to(index,will_go),temp)



    recursion(0,0,neet_to_change) #index, change
    

    return min(answer)




print(solution("BBBAAAB"))


# 시간 초과
# def solution(name):
#     answer = sum([change_char(x)+1 for x in name]) - 1
#     begin = "A"*len(name)

#     def recursion(name2, count, index):
#         nonlocal answer
#         if count > answer:
#             return

#         if name == name2:
#             answer = min(answer,count-1)
#             return
#         # 알파벳 변환
#         if name[index] != name2[index]:
#             count += change_char(name[index])
#         name2 = name2[:index] + name[index] + name2[index+1:]

#         # 오른쪽 이동
#         temp_index = index + 1 if index + 1 < len(name) else 0
#         recursion(name2, count + 1, temp_index)

#         # 왼쪽 이동
#         temp_index = index - 1 if index - 1 >= 0 else len(name)-1
#         recursion(name2, count + 1, temp_index)

#         return

#     if name == begin:
#         return 0
#     else:
#         recursion(begin,0,0)
#     return answer
