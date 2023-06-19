# Level 1
# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 23.06.12

from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

# 2. list 이용
def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]
 
print(solution(participant, completion))


# 1. for 문 이용
from collections import Counter
def solution(participant, completion):
    result = ''
    for i in (Counter(participant) - Counter(completion)):
        result = i
    return result