def solution(n):
    fibo = []
    for i in range(n+1):
        if i < 2:
            fibo.append(i)
        else:
            fibo.append(fibo[-1]+fibo[-2])
    return fibo[-1]%1234567