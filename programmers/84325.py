def solution(table, languages, preference):
    answer = []
    d_dict = {}
    for t in table:
        temp = t.split()
        for i,x in enumerate(temp):
            if i == 0:
                d_dict[x] = {}
            else:
                d_dict[temp[0]][x] = 6-i

    for d in d_dict:
        temp = 0
        for i in range(0,len(languages)):
            if languages[i] in d_dict[d]:
                temp += d_dict[d][languages[i]] * preference[i]
        answer.append([temp,d])



    return sorted(answer,key=lambda x : (-x[0],x[1]))[0][1]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))