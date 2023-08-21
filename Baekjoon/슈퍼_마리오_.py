# 브론즈 1
# 슈퍼 마리오
# https://www.acmicpc.net/problem/2851
# 23.08.15

n = list(int(input()) for _ in range(10))
score = [0]
result = 0

for i, v in enumerate(n):
    score.append(score[i] + v)

    if score[i] >= 100:
        after = abs(100 - score[i])
        before = abs(100 - score[i - 1])

        if after > before: print(score[i - 1])
        else: print(score[i])

        break
