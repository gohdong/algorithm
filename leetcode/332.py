from collections import defaultdict


# import collections

class Solution:
    def findItinerary(self, tickets):
        answer = []

        ticket_dict = defaultdict(list)

        for i in sorted(tickets):
            ticket_dict[i[0]].append(i[1])

        def dfs(departure):
            while ticket_dict[departure]:
                dfs(ticket_dict[departure].pop(0))
            
            answer.append(departure)

            

        dfs('JFK')

        return answer[::-1]