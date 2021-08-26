# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    u_dict = {}
    for re in record:
        if re.split(' ')[0] != "Leave":
            u_dict[re.split(' ')[1]] = re.split(' ')[2]

    for re in record:
        if re.split(' ')[0] == "Enter":
            answer.append(f"{u_dict[re.split(' ')[1]]}님이 들어왔습니다.")
        if re.split(' ')[0] == "Leave":
            answer.append(f"{u_dict[re.split(' ')[1]]}님이 나갔습니다.")

    return answer