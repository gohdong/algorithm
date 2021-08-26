def factorization(a: int):
	result = {}
	
	prime = 2
	while a != 1:
		if a % prime == 0:
			if prime not in result:
				result[prime] = 1
			else:
				result[prime] +=1
			a /= prime
		else:
			prime +=1

	return(result)
