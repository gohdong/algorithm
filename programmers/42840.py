def solution(answers):
    answer = []
    a_pattern = [1, 2, 3, 4, 5]
    b_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    c_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    hit_count = [0, 0, 0]

    for i, a in enumerate(answers):
        if a_pattern[i % len(a_pattern)] == a:
            hit_count[0] += 1
        if b_pattern[i % len(b_pattern)] == a:
            hit_count[1] += 1
        if c_pattern[i % len(c_pattern)] == a:
            hit_count[2] += 1

    max_hit = max(hit_count)

    if hit_count[0] == max_hit:
        answer.append(1)
    if hit_count[1] == max_hit:
        answer.append(2)
    if hit_count[2] == max_hit:
        answer.append(3)

    return answer