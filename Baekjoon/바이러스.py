# 실버 3
# 바이러스
# https://www.acmicpc.net/problem/2606
# 23.11.13

#dfs
N = int(input())
M = int(input())
result = 0

computer = [[False] * (N + 1)  for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    computer[a][b] = True
    computer[b][a] = True

dfs_visited = [False] * (N + 1)

def dfs(virus):
    global result
    dfs_visited[virus] = True
    
    for i in range(1, N + 1):
        if not dfs_visited[i] and computer[virus][i]:
            result += 1
            dfs(i)
        
dfs(1)
print(result)


# bfs
from collections import deque

N = int(input())
M = int(input())
result = 0

computer = [[False] * (N + 1)  for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    computer[a][b] = True
    computer[b][a] = True

visited = [False] * (N + 1)

def bfs(virus):
    queue = deque([virus])
    global result
    visited[virus] = True

    while queue:
        n = queue.popleft()
        for i, v in enumerate(computer[n]):
            if not visited[i] and computer[n][i]:
                queue.append(i)
                visited[i] = True
                result += 1
            
bfs(1)
print(result)
