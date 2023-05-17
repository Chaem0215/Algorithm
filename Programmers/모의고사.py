# Level 1
# 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 23.05.17

answers = [1,3,2,4,2]
student = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
total = [0,0,0]
# def solution(answers):
#     for i, score in enumerate(student):
#         for j, v in enumerate(answers):
#             if v == score[j % len(score)]: total[i] += 1
            
#     results = []
#     for i, v in enumerate(total):
#         if max(total) == v:
#             results.append(i + 1)
#     return results

def solution(answers):
    for i, score in enumerate(student):
        count = 0
        print(score)
        for j in score:
            if count >= len(answers): count = 0
            if answers[count] == j: total[i] += 1
            
            print(count)
            count += 1
            
    results = []
    for i, v in enumerate(total):
        if max(total) == v:
            results.append(i + 1)
    return results

print(solution(answers))