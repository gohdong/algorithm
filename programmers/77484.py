# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    max_hit = 7
    min_hit = 7

    lot_set = set(lottos)
    win_set = set(win_nums)

    hit_set = lot_set.intersection(win_set)

    max_hit -= len(hit_set)
    min_hit -= len(hit_set)

    max_hit -= lottos.count(0)
    if max_hit == 7: 
        max_hit -= 1
    if min_hit == 7: 
        min_hit -= 1

    return [max_hit, min_hit]