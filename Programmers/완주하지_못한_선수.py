# Level 1
# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 23.06.12

from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)

    return list(result.keys())[0]

print(solution(participant, completion))