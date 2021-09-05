def solution(scores):
    answer = ''

    for i in range(0,len(scores)):
        for j in range(0,len(scores)):
            if i > j:
                scores[i][j],scores[j][i] = scores[j][i],scores[i][j]

    for i, score in enumerate(scores):
        my_score = score[i]
        score.remove(my_score)
        if my_score < min(score) or my_score > max(score):
            print(my_score,max(score),min(score))
            answer += grade(sum(score) / (len(scores)-1))

        else:
            answer += grade((sum(score)+my_score) / len(scores))

    return answer


def grade(a):
    if a >= 90:
        return 'A'
    elif a >= 80:
        return 'B'
    elif a >= 70:
        return 'C'
    elif a >= 50:
        return 'D'
    return 'F'


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
      47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
