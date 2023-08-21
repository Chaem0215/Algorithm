# 실버 3
# 꿀 아르바이트
# https://www.acmicpc.net/problem/12847
# 23.08.20

n, m = map(int, input().split())
lists = list(map(int, input().split()))
max = 0

for i in range(len(lists[:len(lists) - (m - 1)])):
    total = sum(lists[i:i + m])
    if max < total:
        max = sum(lists[i:i + m])

print(max)

# https://velog.io/@rooster100/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-12847%EB%B2%88-%EA%BF%80-%EC%95%84%EB%A5%B4%EB%B0%94%EC%9D%B4%ED%8A%B8

# 1. 시간 초과
# n, m = map(int, input().split())
# lists = list(map(int, input().split()))
# result = []

# for i in range(len(lists[:len(lists) - (m - 1)])):
#     result.append(sum(lists[i:i + m]))

# print(max(result))