import factorization


def lcm(a: int, b: int):
    result = 1
    a_fact = factorization.factorization(a)

    a_fact.update(factorization.factorization(b))

    for prime in a_fact:
        result *= prime

    return result


def gcp(a: int, b: int):
	return a*b//lcm(a,b)

print(lcm(18, 24))
print(gcp(18, 24))

