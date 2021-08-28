def factorization(a: int):
    result = {}

    prime = 2
    while a != 1:
        if a % prime == 0:
            if prime not in result:
                result[prime] = 1
            else:
                result[prime] += 1
            a /= prime
        else:
            prime += 1

    return(result)


def gcp(a: int, b: int):
    result = 1
    a_fact = factorization(a)
    b_fact = factorization(b)

    temp = {}
    for a_f in a_fact:
        if a_f in b_fact:
            temp[a_f] = min(a_fact[a_f],b_fact[a_f])
    #     else:
    #         temp[a_f] = a_fact[a_f]

    # for b_f in b_fact:
    #     if b_f not in temp:
    #         temp[b_f] = b_fact[b_f]

    for t in temp:
        result *= t**temp[t]

    return result


def lcm(a: int, b: int):
    return a*b//gcp(a, b)

count = int(input())
for x in range(count):
	a,b = input().split()
	print(lcm(int(a),int(b)))



