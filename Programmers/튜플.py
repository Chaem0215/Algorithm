# Level 2
# 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 23.05.07

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

def solution(s):
    lists = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    answer = list()
    for i in lists:
        i = list(map(int, i.split(',')))
        for j in i:
            if j not in answer:
                answer.append(j)
        
    return answer


# answer를 dict 으로 하면 O(1) 로 빠르다.
def solution2(s):
    lists = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    answer = {}
    for i in lists:
        i = list(map(int, i.split(',')))
        for j in i:
            if j not in answer:
                answer[j] = 1 # 값은 아무거나
        
    return list(answer)


print(solution2(s))
