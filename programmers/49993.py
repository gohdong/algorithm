def solution(skill, skill_trees):
    answer = 0
    skill_dict = {x: '' for x in skill}
    p = 0

    for st in skill_trees:
        p = 0
        flag = True
        for s in st:
            if p == len(skill):
                break
            if s in skill_dict:
                if skill[p] == s:
                    p += 1
                else:
                    flag = False
                    break

        if flag:
            answer += 1

    return answer


print(solution())
