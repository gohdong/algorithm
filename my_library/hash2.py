def solution(user_id, banned_id):
    answer = 0
    possibliy_banned = []
    for i,ban in enumerate(banned_id):
        temp_list = []
        
        # 자리수 판별
        for index,uid in enumerate(user_id):
            if(len(uid) == len(ban)):
                temp_list.append(uid)
                
                
        # 문자별 판별        
        will_delete = []        
        for x in range(0,len(ban)):
            if(ban[x] =='*'):
                continue
            else:
                for uid in temp_list:
                    if (uid[x] != ban[x]):
                        will_delete.append(uid)
        possibliy_banned.append(list(set(temp_list) - set(will_delete)))
        
    
    tree = []
    for p in range(0,len(possibliy_banned)):

        for uid in possibliy_banned[p]:
            if(p == 0):
                tree.append([uid])
            else:
                for x in possibliy_banned[p]:
                    for t in tree:
                        if(len(t) == p and (not x in t)):
                            temp = t[:]
                            temp.append(x)
                            tree.append(temp)
                    #     print(t)

                
    # print(tree)
    # print("11",possibliy_banned)
    # test = []
    # for p in range(0,len(possibliy_banned)):
    #     for element in possibliy_banned[p]:
    #         if(p == 0):
    #             test.append([element])
    #         else:
    #             print(test)
    #             print("11",possibliy_banned[p])
    #             print("22",element)
    #             for x in range(0,len(test)):
    #                 print("33",test[x])
    #                 temp = test[x]
    #                 if(len(temp)==p):
    #                     if(not element in test[x]):
    #                         temp.append(element)
    #                         test.append(temp)
    #                 print("44",test[x])
                            
    # final process
    final = []    
    for x in tree:
        if(len(x) == len(banned_id)):
            x.sort()
            if not x in final:
                final.append(x)
    
    # print(final)
# 
        
        
            
        
        

        
        
    return len(final)