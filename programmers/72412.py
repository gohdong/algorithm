from collections import defaultdict
import bisect


def solution(info, query):
    answer = []
    query_dict = defaultdict(list)

    for inf in info:
        temp = inf.split()
        score = int(temp[-1])
        query_dict[f'{temp[0]}{temp[1]}{temp[2]}{temp[3]}'].append(score)
        query_dict[f'-{temp[1]}{temp[2]}{temp[3]}'].append(score)
        query_dict[f'{temp[0]}-{temp[2]}{temp[3]}'].append(score)
        query_dict[f'{temp[0]}{temp[1]}-{temp[3]}'].append(score)
        query_dict[f'{temp[0]}{temp[1]}{temp[2]}-'].append(score)
        query_dict[f'--{temp[2]}{temp[3]}'].append(score)
        query_dict[f'{temp[0]}--{temp[3]}'].append(score)
        query_dict[f'{temp[0]}{temp[1]}--'].append(score)
        query_dict[f'-{temp[1]}-{temp[3]}'].append(score)
        query_dict[f'-{temp[1]}{temp[2]}-'].append(score)
        query_dict[f'{temp[0]}-{temp[2]}-'].append(score)
        query_dict[f'---{temp[3]}'].append(score)
        query_dict[f'-{temp[1]}--'].append(score)
        query_dict[f'--{temp[2]}-'].append(score)
        query_dict[f'{temp[0]}---'].append(score)
        query_dict[f'----'].append(score)

    for k in query_dict:
        query_dict[k].sort()

    for i in query:
        temp = i.split()
        score = int(temp[-1])
        q = f'{temp[0]}{temp[2]}{temp[4]}{temp[6]}'


        answer.append(len(query_dict[q][bisect.bisect_left(query_dict[q],score):]))

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))


# 시간초과
# from collections import defaultdict
# import bisect
# 
# 
# def solution(info, query):
#     answer = []
#     wild_card = set()
#     plang_dict = defaultdict(set)
#     job_dict = defaultdict(set)
#     career_dict = defaultdict(set)
#     soul_dict = defaultdict(set)

#     for i, deveoper in enumerate(info):
#         temp = deveoper.split()
#         wild_card.add((i, int(temp[4])))
#         plang_dict[temp[0]].add((i, int(temp[4])))
#         job_dict[temp[1]].add((i, int(temp[4])))
#         career_dict[temp[2]].add((i, int(temp[4])))
#         soul_dict[temp[3]].add((i, int(temp[4])))

#     for q in query:


#         temp = q.split()
#         temp2 = wild_card.copy()
#         if temp[0] != '-':
#             temp2 &= plang_dict[temp[0]] 
#         if temp[2] != '-':
#             temp2 &= job_dict[temp[2]] 
#         if temp[4] != '-':
#             temp2 &= career_dict[temp[4]] 
#         if temp[6] != '-':
#             temp2 &= soul_dict[temp[6]] 
#         coding_score = int(temp[7])
#         # print()
#         combine = sorted([x[1] for x in temp2])
#         # print(combine)
#         answer.append(len(combine[bisect.bisect_left(combine,coding_score):]))
#         # count = 0
#         # for i,c in enumerate(temp2):
#         #     if c[1] >= coding_score:
#         #         count+=1
#         # # print(plang,job,career,soul,coding_score)
#         # answer.append(count)

#     return answer