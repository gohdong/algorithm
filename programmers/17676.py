

def solution(lines):
    answer = 0
    log_start = []
    log_end = []
    log_count = len(lines)
    
    for line in lines:
        s_line = line.split()
        end = to_ms(s_line[1])
        start = end - int(float(s_line[2][:-1])*1000) +1
        log_start.append(start)
        log_end.append(end)

    for l in range(0,log_count):
        temp1 = 0
        temp2 = 0

        for j in range(0,log_count):
            if log_start[l] - 999 <= log_start[j] <= log_start[l] or log_start[l] - 999 <= log_end[j] <= log_start[l] or (log_start[j] <= log_start[l] - 999 and log_end[j] >= log_start[l]): 
                temp1+=1
            if log_end[l] <= log_start[j] <= log_end[l]+999 or log_end[l] <= log_end[j] <= log_end[l]+999 or (log_start[j] <= log_end[l] and log_end[j] >= log_end[l]+999): 
                temp2+=1

        answer = max(answer,temp1,temp2)

    return answer

def to_ms(str):
    temp = list(map(float,str.split(':')))
    return int((temp[0] * 60 * 60 + temp[1] * 60 + temp[2])*1000)
	


print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))