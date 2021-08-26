# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    def step_one():
        nonlocal new_id
        new_id = new_id.lower()

    def step_two():
        nonlocal new_id
        new_id = re.sub(r"[^a-zA-Z0-9-_.]", "", new_id)

    def step_three():
        nonlocal new_id
        while ".." in new_id:
            new_id = new_id.replace("..", ".")

    def step_four():
        nonlocal new_id
        if new_id and new_id[0] == '.':
            new_id = new_id[1:]
        if new_id and new_id[-1] == '.':
            new_id = new_id[:-1]

    def step_five():
        nonlocal new_id
        if not new_id:
            new_id += 'a'

    def step_six():
        nonlocal new_id
        new_id = new_id[:15]

    def step_seven():
        nonlocal new_id
        while len(new_id) < 3:
            new_id += new_id[-1]

    step_one()
    step_two()
    step_three()
    step_four()
    step_five()
    step_six()
    step_seven()
    step_four()

    return new_id