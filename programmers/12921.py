def solution(n):
    answer = 0
    for i in range(n+1):
        if is_prime(i):
            answer+=1

    return answer

## 아리스토텔레스의 체
def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

def is_prime(a: int):
    if a == 1 or a == 0:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True

print(solution(10))