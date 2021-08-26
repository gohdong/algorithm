def solution(participant : list, completion : list):
    participant_dict = {}
    completion_dict = {}
    # completion_dictary : dict = {i:0 for i in completion}
    # answer = ''
    
    for i in participant :
        if(not (i in participant_dict)):
            participant_dict[i] = 0
        participant_dict[i] +=1


    for i in completion :
        if(not (i in completion_dict)):
            completion_dict[i] = 0
        completion_dict[i] +=1


    for x in completion_dict:
        participant_dict[x] -= completion_dict[x]
        if(participant_dict[x] == 0):
            participant_dict.pop(x)

    return list(participant_dict.keys())[0]