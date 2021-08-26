def solution(numbers):
    answer = ""
    i = 1

    while i < len(numbers):
        j = i
        while j > 0 and str(numbers[j - 1]) + str(numbers[j]) < str(numbers[j]) + str(numbers[j-1]):
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]

            j -= 1

        i += 1

    return str(int(''.join(map(str, numbers))))