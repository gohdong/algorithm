from collections import defaultdict, Counter
from itertools import permutations, combinations


def solution(orders, course):
    answer = []
    course_dict = defaultdict(list)

    for c in course:
        for o in orders:
            for x in combinations(o, c):
                course_dict[c].append(tuple(sorted(x)))

        # print(Counter(course_dict[c]))
        if course_dict[c]:
            max_count = Counter(course_dict[c]).most_common(1)[0][1]
            if max_count > 1:
                for cd in Counter(course_dict[c]):
                    if Counter(course_dict[c])[cd] == max_count:
                        answer.append("".join(cd))
    return sorted(answer)