def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = arr1[i] | arr2[i]
        temp = str(bin(arr1[i]))[2:]
        if len(temp) != n:
            temp = "0"*(n-len(temp)) + temp
        answer.append(temp.replace("1","#").replace("0"," "))

    return answer


print(solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))