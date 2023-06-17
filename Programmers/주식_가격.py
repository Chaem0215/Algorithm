# Level 2
# 주식 가격
# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 23.06.13

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    for i, v in enumerate(prices):
        cnt = 0
        for j in prices[i:]:
            if i == len(prices) - 1: break
            elif v <= j: cnt += 1
            else: break
        answer.append(cnt)

    return answer

print(solution(prices))