# 파일명 정리

from collections import defaultdict 

def solution(files):
    answer = []
    dict_by_head = defaultdict(list)
    for file in files:
        num_flag = 0
        for i,c in enumerate(file):
            if not num_flag and c.isdecimal():
                num_flag = i
            elif num_flag and not c.isdecimal():
                dict_by_head[file[:num_flag].lower()].append([int(file[num_flag:i]),file])
                break

            if num_flag and i == len(file)-1:
                dict_by_head[file[:num_flag].lower()].append([int(file[num_flag:i+1]),file])

    for head in sorted(dict_by_head):
        for file in sorted(dict_by_head[head],key=lambda x : x[0]):
            answer.append(file[1])


    return answer


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))