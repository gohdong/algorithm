def solution(s):
    if s.isnumeric():
        return int(s)
    answer = ""

    num_dict = {
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9",
        'zero': "0"
    }

    left = 0
    right = 0

    while left != len(s):
        right += 1
        if s[left:right] in num_dict:
            answer += num_dict[s[left:right]]
            left = right
        if s[left:right].isnumeric():
            answer += s[left:right]
            left = right
        # left += 1

    return answer


print(solution("one4seveneight"))
