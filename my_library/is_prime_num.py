def is_prime(a: int):
    if a == 1 or a == 0:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True