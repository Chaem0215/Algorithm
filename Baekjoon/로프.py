# 실버 4
# 로프
# https://www.acmicpc.net/problem/2217
# 23.08.21

import sys

N = int(sys.stdin.readline())
lists = sorted(list(int(sys.stdin.readline()) for _ in range(N)), reverse = True)
result = 0

# 중량을 나눌 수 있고 모든 로프를 다 써야되는게 아님
for i, v in enumerate(lists): # 몇번째로 큰 로프인지 확인, 로프가 들 수 있는 중량 뽑아냄
    tmp = (i + 1) * v # w/k 만큼의 중량이 걸림, i + 1개의 로프 중 v 중량을 tmp에 담아 비교
    if result < tmp: result = tmp

print(result)