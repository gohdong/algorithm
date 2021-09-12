def solution(n, k):
    answer = 0
    temp = str(n) if k == 10 else n_numeric(n, k)

    n_to_list = num_to_list(temp)

    # if is_prime(int(temp)):
    #     answer += 1

    for num in n_to_list:
        print(num)
        if num != '0' and is_prime(int(num)):
            answer+=1

    return answer


def num_to_list(s):
    temp = []
    str_temp = ""
    if int(s) == 0 :
        return temp

    for i, x in enumerate(s):
        if x != '0':
            str_temp += x
        else:
            if str_temp:
                temp.append(str_temp)
            str_temp = ""
            temp.append('0')

        if i == len(s)-1:
            if str_temp:
                temp.append(str_temp)

    return temp


def is_prime(a: int):
    if a == 1 or a == 0:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True


def n_numeric(a, n_th):
    temp = ""
    while True:
        temp += str(a % n_th)
        a = a // n_th
        if not a:
            break
    return temp[::-1]


# print(solution(437674, 3))
print(solution(120,10))


# print(solution())
