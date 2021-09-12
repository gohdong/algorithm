def solution(id_list, report, k):
    answer = []
    user_dict = {}
    reported_dict = {}
    banned_user = set()
    for r in report:
        temp = r.split()
        if temp[0] not in user_dict:
            user_dict[temp[0]] = set()

        if temp[1] not in reported_dict:
            reported_dict[temp[1]] = set()

        user_dict[temp[0]].add(temp[1])
        reported_dict[temp[1]].add(temp[0])

    for user in reported_dict:
        if len(reported_dict[user]) >= k:
            banned_user.add(user)

    for user in id_list:
        if user in user_dict:
            answer.append(len(user_dict[user].intersection(banned_user)))
        else:
            answer.append(0)

    return answer    

    
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))