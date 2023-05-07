# Level 1
# 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 23.05.07

s = "try hello world"

def solution(s):
    lists = s.split(' ')
    new_lists = list()
    for i in lists:
        new = ''
        for j in range(len(i)):
            if j % 2 == 0:
                new += i[j].upper()
            else:
                new += i[j].lower()
        new_lists.append(new)
    results = ' '.join(new_lists)
    return results

print(solution(s))


def solution2(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))