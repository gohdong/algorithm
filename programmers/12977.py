#https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
def solution(answers):
    count = 0

    def is_prime(a: int):
        if a == 1:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False

        return True

    for sub_set in list(combinations(answers, 3)):
        if is_prime(sum(sub_set)):
            count += 1

    return count