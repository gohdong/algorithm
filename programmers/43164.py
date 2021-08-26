from collections import defaultdict


def solution(tickets):
    answer = []

    ticket_dict = defaultdict(list)

    for i in sorted(tickets):
        ticket_dict[i[0]].append(i[1])

    def dfs(departure):
        while ticket_dict[departure]:
            dfs(ticket_dict[departure].pop(0))

        answer.append(departure)



    dfs('ICN')

    return answer[::-1]