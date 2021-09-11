from itertools import combinations

def solution(n, info):
    can_shoot = set()
    answer = []
    if n == 1 and info[0] == 1:
        return [-1]

    apeach_info = info[::-1]
    ryan_info = [0]*11
    a_dict = {}
    may_answer = {}
    for i,s in enumerate(apeach_info):
        a_dict[i] = s


    def recursion(remain,now,info):
        if remain <= 0:
            if sum(info) == n:
                can_shoot.add(tuple(info))
            return

        if now == 0:

            temp = info[::]
            temp[0] = remain
            if sum(temp) == n:
                can_shoot.add(tuple(temp))
            return
        
        temp = info[::]
        temp[now] = a_dict[now]+1 if a_dict[now] + 1 <=remain else remain
        recursion(remain-a_dict[now]-1,now-1,temp)
        recursion(remain,now-1,info)


    recursion(n,10,ryan_info)

    for c in can_shoot:
        temp = calc_score(apeach_info,c)
        if temp[1] > temp[0]:
            if temp[1]-temp[0] not in may_answer:
                may_answer[temp[1]-temp[0]] = []
            may_answer[temp[1]-temp[0]].append(c)

    max_differ = sorted(may_answer,reverse=True)[0] if may_answer else 0



    return list(sorted(may_answer[max_differ],reverse=True)[0][::-1]) if may_answer else [-1]
def calc_score(list1,list2):
    apeach_score = 0
    ryan_score = 0
    for i,_ in enumerate(list1):
        if list1[i] == list2[i] == 0:
            continue

        elif list1[i] >= list2[i]:
            apeach_score += i
        else:
            ryan_score += i
    return (apeach_score,ryan_score)


# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(0,[0,0,0,0,0,0,0,0,0,0,0]))
    # free_score = []
    # start_at = 0

    # for i,a in enumerate(apeach_info):
    #     if a == 0:
    #         free_score.append(i)
    # for i in range(n):
    #     if free_score:
    #         temp = free_score.pop()
    #         start_at = max(start_at,temp)
    #         ryan_info[temp] = 1
    #     else:
    #         ryan_info[0] +=1

    # while start_at<11:
        
    #     need_shot = apeach_info[start_at]+1
    #     for i in range(11):
    #         buf = ryan_info[i]

    #         if buf > 0:
    #             if buf <= need_shot:
    #                 need_shot -= buf
    #                 ryan_info[i] = 0
    #             else:
    #                 need_shot -= (buf-need_shot)
    #                 ryan_info[i] -= buf-need_shot
    #         print("!!",ryan_info)
    #         if not need_shot:
    #             break

    #     ryan_info[start_at] = apeach_info[start_at]+1

    #     temp = calc_score(apeach_info,ryan_info)
    #     print(ryan_info,temp)
    #     if temp[1] > temp[0]:
    #         answer.append((temp[1]-temp[0],ryan_info[::]))


    #     start_at+=1

    # return answer    