from collections import defaultdict


def solution(gems):
    all_gems = set(gems)
    gem_count = len(all_gems)
    left = 1
    right = 1
    gem_dict = defaultdict(int)
    answer = []

    gem_dict[gems[0]] = 1

    while left <= len(gems) and right <= len(gems):
        if len(gem_dict) == gem_count:
            answer.append([left, right])
            gem_dict[gems[left-1]] -= 1
            if gem_dict[gems[left-1]] == 0:
                gem_dict.pop(gems[left-1])
            left += 1
        else:
            right += 1
            if right > len(gems):
                break
            gem_dict[gems[right-1]] += 1

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]