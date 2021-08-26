def solution(numbers):
    def is_prime(a: int):
        if a == 1 or a == 0:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False

        return True

    n_to_list = list(numbers)
    num_list = set()
    answer = 0

    def num_generate(s, n_l):  # list
        if not n_l:
            return

        for i in n_l:
            temp = s + str(i)
            temp2 = n_l[:]
            num_list.add(int(temp))
            temp2.remove(i)
            num_generate(temp, temp2)

    num_generate("", n_to_list)

    for a in num_list:
        if is_prime(a):
            answer += 1

    return answer