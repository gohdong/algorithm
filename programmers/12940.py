def solution(n, m):
    gcd = 1

    for i in range(2, min(n, m)+1):
        if not(n % i or m % i):
            gcd = i

    return [gcd,n*m//gcd]


print(solution(3, 12))
