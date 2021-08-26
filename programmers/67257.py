def solution(expression):
    result_list = []
    order_list = [
        ['*','-','+'],
        ['*','+','-'],
        ['-','*','+'],
        ['-','+','*'],
        ['+','*','-'],
        ['+','-','*'],
    ]

    expression_list = string_to_list(expression)
    
    for order in order_list:
        temp = expression_list[:]
        o_index = 0
        while len(temp) != 1:
            for i,x in enumerate(temp):
                if(not order[o_index] in temp):
                    o_index +=1
                    break
                
                if(x == order[o_index]):

                    a = temp.pop(i-1)
                    oper = temp.pop(i-1)
                    b =temp.pop(i-1)

                    temp.insert(i-1,calculate(a,b,oper))
                    break

            # if(order[o_index] in temp):


        result_list.append(abs(temp[0]))

    
    
    
    
    
    
    print(result_list)
    return max(result_list)







def string_to_list(exp : str) -> list:
    res = []
    temp_int = ''
    for index,c in enumerate(exp):
        if(index == len(exp)-1):
            temp_int += c
            res.append(int(temp_int))
        
        elif(c == '-' or c == '+' or c == '*'):
            res.append(int(temp_int))
            res.append(c)
            temp_int = ''
        else:
            temp_int +=c
    return res
    

def calculate(a,b,operation):
    if(operation == '+'):
        return a+b
    elif(operation == '-'):
        return a-b
    return a*b