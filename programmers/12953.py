def solution(arr):
    def gcd(n,m):
        if n > m:
            m, n = n, m
        if n == 0:
            return m
        if m % n == 0:
            return n
        else:
            return gcd(n, m%n)

    while len(arr)>1:
        a = arr.pop()
        b = arr.pop()
        arr.append(a*b//gcd(a,b))

    return arr[0]

print(solution([2,6,8,14]))