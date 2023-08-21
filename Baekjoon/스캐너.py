# 브론즈 1
# 스캐너
# https://www.acmicpc.net/problem/3035
# 23.08.20

import sys

R, C, ZR, ZC = map(int, sys.stdin.readline().split())
lists = []
for _ in range(R):
    news = sys.stdin.readline()
    news_str = ""
    for i in news:
        news_str += i * ZC
    for _ in range(ZR):
        lists.append(news_str)

for i in lists:
    print(i)

#print(*lists, sep="\n")

# 1. 출력 형식이 잘못되었습니다.
# import sys

# R, C, ZR, ZC = map(int, sys.stdin.readline().split())
# lists = []
# for _ in range(R):
#     news = sys.stdin.readline()
#     news_str = ""
#     for i in news:
#         news_str += i * ZC
#     lists.append(news_str * ZR)
    
# print(*lists, sep="\n")

# 1. 출력 형식이 잘못되었습니다.
# import sys

# R, C, ZR, ZC = map(int, sys.stdin.readline().split())

# for _ in range(R):
#     news = sys.stdin.readline()
#     scan_news = ""
#     for i in news:
#         scan_news += i * ZC
    
#     for j in range(ZR):
#         print(scan_news)


# 2. 다른 사람 풀이
# r, c, zr, zc = map(int, input().split())
# news = [input() for _ in range(r)]

# for i in range(r):
#     for _ in range(zr):
#         print(''.join([ch*zc for ch in news[i]]))