def solution(msg):
    answer = []
    my_dictionary = {}
    d_index = 27
    max_len = 1
    for i,d in enumerate(range(ord('A'),ord('Z')+1)):
        my_dictionary[chr(d)] = i+1

    while msg:
        for i in range(max_len,0,-1):
            if msg[:i] in my_dictionary:
                answer.append(my_dictionary[msg[:i]])
                my_dictionary[msg[:i+1]] = d_index
                msg = msg[i:]
                max_len = max(max_len,i+1)
                d_index+=1
                break

    return answer


print(solution("KAKAO"))