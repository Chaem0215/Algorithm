# 실버 2
# DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 23.11.02

from collections import deque

N, M, V = map(int, input().split())

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

lists= [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lists[a][b] = True
    lists[b][a] = True

def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")

    for i in range(1, N + 1):
        if not dfs_visited[i] and lists[v][i]:
            dfs(i)

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        bfs_visited[v] = True
        print(v, end=" ")
        
        for i in range(1, N + 1):
            if not bfs_visited[i] and lists[v][i]:
                queue.append(i)
                bfs_visited[i] = True

dfs(V)
print()
bfs(V)
