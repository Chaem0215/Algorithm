# 실버 3
# 고양이 카페
# https://www.acmicpc.net/problem/28353
# 23.08.20

N, K = map(int, input().split())
lists = sorted(list(map(int, input().split())))
start, end, cnt = 0, len(lists) - 1, 0

while start < end:
    total = lists[start] + lists[end]
    if total <= K:
        cnt += 1
        start += 1
    end -= 1
    
print(cnt)