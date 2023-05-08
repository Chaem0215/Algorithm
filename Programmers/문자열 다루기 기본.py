# Level 1
# 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 23.05.08

s = "12234"

def solution(s):
    answer = s.isdigit() and (len(s) == (4 or 6))
    return answer

print(solution(s))