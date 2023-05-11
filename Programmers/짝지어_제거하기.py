# Level 2
# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 23.05.10

s = "cdcd"

def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i: stack.pop()
        else : stack.append(i)
    return 0 if stack else 1

print(solution(s))