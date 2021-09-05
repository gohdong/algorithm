from datetime import date, datetime


def solution(a, b):
    day_dict = {
        0: 'MON',1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"
    }
    return day_dict[datetime(year=2016, month=a, day=b).weekday()]


print(solution(1, 5))
