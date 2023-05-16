# Level 1
# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 23.05.16

n = 626331

def solution(num):
    cnt = 0
    return rec(num, cnt)

def rec(num, cnt): # 재귀 함수 이용
    if cnt >= 500: return -1
    elif num == 1: return cnt
    elif num % 2 == 0: num = num / 2
    else : num = num * 3 + 1
    return rec(num, cnt + 1)

print(solution(n))


def solution2(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1