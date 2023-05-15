# 실버3
# 문자열 집합
# https://www.acmicpc.net/problem/14425
# 23.05.15

N, M = map(int, input().split(' '))
S = set()
for i in range(N):
    S.add(input())
ex = []
for i in range(M):
    ex.append(input())

cnt = 0
for i in S:
    cnt += ex.count(i)
    
print(cnt)

# sys.stdin.readline().split() 참고