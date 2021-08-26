# 키패드 누르기

def solution(numbers, hand):
    def get_distance(n, other) -> int:
        return abs(coordinate_map[n][0]-coordinate_map[other][0]) + abs(coordinate_map[n][1]-coordinate_map[other][1])
    answer = ''
    coordinate_map = {n : make_coordinate(n) for n in range(1,13)}

    
    current_left = 10
    current_right = 12
    distance_from_left = 0
    distance_from_right = 0
    for n in numbers:
        if(n == 0):
            n=11
        if(n %3 ==1):
            answer += 'L'
            current_left = n
        elif(n % 3 == 0):
            answer += 'R'
            current_right = n
        else:
            distance_from_left = get_distance(n,current_left)
            distance_from_right = get_distance(n,current_right)
            if(distance_from_left == distance_from_right):
                if(hand == 'right'):
                    current_right = n
                    answer += 'R'
                else:
                    answer += 'L'
                    current_left = n
            elif(distance_from_left<distance_from_right):
                answer += 'L'
                current_left = n
            else:
                answer += 'R'
                current_right = n
            
    return answer

    

def make_coordinate(n : int) -> list:
    if(n == 0):
        return [3,1]

    elif(n%3 == 0):
        return [(n -1)//3, 2 ]
    return [n//3,(n%3)-1]