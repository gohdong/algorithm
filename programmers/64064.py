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
                tree.append({uid})
            else:
                for t in range(0,len(tree)):
                    if(len(tree[t]) == p):
                        temp = tree[t].copy()
                        temp.add(uid)
                        tree.append(temp)


                            
    final = []    
    for x in tree:
        if(len(x) == len(banned_id)):
            if not x in final:
                final.append(x)

        
        
    return len(final)