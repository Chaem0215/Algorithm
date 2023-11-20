# 실버 2
# 섬의 개수
# https://www.acmicpc.net/problem/4963
# 23.11.15

dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 대각선까지 확인하기 위해 추가
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs(i, j):
    que_lists = [(i, j)]
    lists[i][j] = 0

    while que_lists:
        i, j = que_lists.pop(0)
        
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
        
            if x < 0 or y < 0 or x >= h or y >= w: continue
            elif lists[x][y] == 1:
                que_lists.append((x, y))
                lists[x][y] = 0
    return

while True:
    w, h = map(int, input().rstrip().split())
    lists = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    if w == 0 and h == 0: break
    else: 
        for i in range(h):
            for j in range(w):
                if lists[i][j] == 1:
                    bfs(i, j)
                    cnt += 1
        
    print(cnt)