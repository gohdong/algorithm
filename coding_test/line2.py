import bisect
from collections import defaultdict
from itertools import combinations
import math
from typing import List


def solution(endingTime, jobs):
    time = 0
    answer = []
    current_job = None

    while time < endingTime:

        for job in jobs:
            if job[2] < time:
                jobs.remove(job)

            if job[1] <= time:
                if not current_job:
                    current_job = job + [time]
                    jobs.remove(job)
                    break

        # if current_job and time == current_job[2]:
        #     current_job = None

        if current_job and time == current_job[4] + current_job[3]:
            if current_job[2] >= time:
                answer.append(current_job[0])
            current_job = None
        print(time, current_job)
        time += 1

    return answer

# 0, [[1, 10, 20, 4], [2, 12, 20, 2]]
# 30, [[1, 10, 20, 6], [2, 12, 20, 8], [3, 20, 30, 2], [4, 25, 40, 10]]
print(solution(40, [[1, 10, 20, 3], [2, 14, 20, 9], [3, 18, 24, 2], [4, 25, 40, 5], [5, 28, 40, 1]]))
# print(solution([3, 3, 3, 3, 2, 2, 2, 2]))
