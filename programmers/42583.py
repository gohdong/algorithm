from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    index = 0;
    current_weight = 0
    ing_trucks = deque([0 for i in range(0,bridge_length)])
    
    finished_trucks = []
    truck_weights = truck_weights[::-1]

    
    while not(truck_weights == [] and sum(ing_trucks)==0):
    
        answer +=1
        if(truck_weights != [] and weight - current_weight >= truck_weights[len(truck_weights)-1]):
            temp_in = truck_weights.pop()
            temp_out = ing_trucks.popleft()
            ing_trucks.append(temp_in)
            
            
            current_weight += (temp_in - temp_out)
            
        else:
            temp_out = ing_trucks.popleft()
            current_weight -= temp_out 
            
            if(truck_weights != [] and weight - current_weight >= truck_weights[len(truck_weights)-1]):
                temp_in = truck_weights.pop();
                ing_trucks.append(temp_in)
                current_weight += temp_in
            else:
                ing_trucks.append(0)
            
            
        
        

        
    
    return answer