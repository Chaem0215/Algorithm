# 실버 2
# 유기농 배추
# https://www.acmicpc.net/problem/1012
# 23.11.14

T = int(input()) #테스트케이스의 개수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):           
    queue = [(x,y)]
    lists[x][y] = False # 방문처리

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if lists[nx][ny] == True:
                queue.append((nx,ny))
                lists[nx][ny] = False

# 행렬만들기
for i in range(T):
    M, N, K = map(int,input().split())
    lists = [[False]*(N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        lists[x][y] = True

    for i in range(M):
        for j in range(N):
            if lists[i][j] == True:
                BFS(i, j)
                cnt += 1

    print(cnt)






# T = int(input())

# def bfs():
#     cnt = 0
#     queue = []

#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j] and lists[i][j]:
#                 visited[i][j] = True
#                 queue.append([i, j])
#                 dfs(i, j)
            
#             if (len(queue) > 0 and not lists[i][j]) or (j == (M - 1) and len(queue) > 0):
#                 cnt += 1
#                 while queue: queue.pop()
#     return cnt

# def dfs(i, j):
#     i += 1
#     if i >= N: return
#     elif not visited[i][j] and lists[i][j]:
#         visited[i][j] = True
#         dfs(i, j)
#     else: return


# for _ in range(T):
#     M, N, K = map(int, input().split())
#     visited = [[False] * M for _ in range(N)]
#     lists = [[False] * M for _ in range(N)]

#     for _ in range(K):
#         a, b = map(int, input().split())
#         lists[b][a] = True

#     print(bfs())
    
