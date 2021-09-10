def solution(m, musicinfos):
    answer = []
    melodies = []
    for music in musicinfos:
        temp = music.split(',')
        temp[3] = melody_handle(temp[3])
        duration = get_minute(temp[0],temp[1])
        melodies.append((get_full_melody(temp[3],duration),temp[2],temp[0]))

    m = melody_handle(m)
    for melody in melodies:
        if m in melody[0]:
            answer.append(melody)

    return sorted(answer,key=lambda x:(-len(x[0]),x[2]))[0][1] if answer else "(None)"

def melody_handle(melody):
    while melody.find("#") != -1:
            index = melody.find("#")
            melody = melody[:index-1]+(melody[index-1]).lower() + melody[index+1:]
    return melody

def get_minute(start,end):
    start = list(map(int,start.split(":")))
    end = list(map(int,end.split(":")))
    return (end[0]-start[0])*60 + end[1]-start[1]

def get_full_melody(melody,duration):
    temp = ""
    length = len(melody)
    for i in range(duration):
        temp += melody[i%length]
    return temp


print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))