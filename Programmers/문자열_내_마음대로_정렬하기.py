# Level 1
# 문자열 내 마음대로 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 23.05.19

strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))

print(solution(strings, n))