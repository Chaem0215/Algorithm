# 실버 5
# 막대기
# https://www.acmicpc.net/problem/1094
# 23.08.29

X = int(input())
result, bar = [], 64

while sum(result) < X:
    bar //= 2 # 절반 자름
    total = sum(result) + bar

    if X == 64: # 64일 경우
        result.append(X)
    elif total <= X:
        result.append(bar)

print(len(result))


# 다른 사람 풀이
# n = int(input())
# lists = [64,32,16,8,4,2,1]
# ans = 0

# for i in lists:
#     while n - i >= 0:
#         n -= i
#         ans += 1
# print(ans)