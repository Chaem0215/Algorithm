# Level1
# 시저암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 23.05.07

s, n = "a B z", 4

def solution(s, n):
    answer = ''
    for i in s:
        ord_s = ord(i)
        count = ord_s + n

        if (ord_s == 32):
            count = ord_s
        if ((ord_s <= 90 and count > 90) or (ord_s <= 122 and count > 122)):
            count -= 26
        
        answer += chr(count)

    return answer

print(solution(s, n))


def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')) # 현재 글자의 숫자 - 알파벳 처음 위치 + 더해야 할 숫자
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)