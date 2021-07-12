def solution(inputString):
    n = 1
    while inputString:
        temp = str(n)
        temp_size = len(temp)
        while temp_size > 0:
            if inputString[:temp_size] in temp:
                inputString = inputString.replace(inputString[:temp_size], "", 1)
                break
            temp_size -= 1

        n += 1

    return n - 1

    # return answer

# 12345
# 2349101
# 7777729
# 7234032479947
print(solution("2349101"))