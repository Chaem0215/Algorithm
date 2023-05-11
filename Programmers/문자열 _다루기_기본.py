# Level 1
# 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 23.05.08

s = "111111"

def solution(s):
    answer = s.isdigit() and (len(s) == 4 or len(s) == 6)
    return answer

print(solution(s))

def solution2(s):
    return s.isdigit() and len(s) in [4,6]