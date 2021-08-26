def solution(phone_book):
    answer = True
    hash_map = {x : 0 for x in phone_book}
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer