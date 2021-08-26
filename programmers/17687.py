def solution(n, t, m, p):
    def n_numeric(a, n_th):
        temp = ""
        while True:
            t = a % n_th
            if t >= 10:
                if t == 10:
                    temp += "A"
                if t == 11:
                    temp += "B"
                if t == 12:
                    temp += "C"
                if t == 13:
                    temp += "D"
                if t == 14:
                    temp += "E"
                if t == 15:
                    temp += "F"
            else:
                temp += str(t)
            a = a // n_th
            if not a:
                break
        return temp[::-1]

    total = ""
    answer = ""
    start = 0
    for _ in range(t):
        for a in range(m):
            total += n_numeric(start, n)
            start += 1

    for i in range(t):
        answer += total[(p - 1) + m * i]

    return answer