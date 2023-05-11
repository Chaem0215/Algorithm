# Level 1
# 핸드폰 번호 가리기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 23.05.08

s = "027778888"

def solution(phone_number):
    answer = (len(phone_number) - 4) * '*' + phone_number[-4:]
    return answer

print(solution(s))