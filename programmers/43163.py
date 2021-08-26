def solution(begin, target, words):
    answer = []
    if target not in words:
        return 0

    def can_change(str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        if count == 1:
            return True
        return False

    def dfs(count, now, word_list):
        if now == target:
            answer.append(count)

        for w in word_list:
            if can_change(w, now) == 1:
                temp = word_list[:]
                temp.remove(w)
                dfs(count + 1, w, temp)

    dfs(0, begin, words[:])
    return min(answer)