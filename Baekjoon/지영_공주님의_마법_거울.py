# 브론즈 3
# 지영 공주님의 마법 거울
# https://www.acmicpc.net/problem/11586
# 23.08.28

import sys

N = int(sys.stdin.readline())
lists = [sys.stdin.readline().rstrip() for _ in range(N)]
K = int(sys.stdin.readline())


if K == 1:
    print(*[i for i in lists], sep="\n")
elif K == 3:
    print(*[i for i in lists[::-1]], sep="\n")
else:
    for i in lists:
        str_revers = ""
        for j in i[::-1]:
            str_revers += j
        print(str_revers)


# 다른 사람 풀이
# n = int(input())
# matrix = [list(input()) for _ in range(n)]
# k = int(input())

# if k==1:
#     for i in range(n):
#         print(*matrix[i],sep='')
# elif k==2:
#     for i in range(n):
#         print(*matrix[i][::-1],sep='')
# else:
#     for i in range(n):
#         print(*matrix[n-1-i],sep='')

# 다른 사람 풀이 2
# import sys
# input = sys.stdin.readline

# n = int(input())
# mirror = [input().rstrip() for _ in range(n)]
# k = int(input())

# if k == 1:  # 원본 출력
#     print(*mirror, sep='\n')
# elif k == 2:  # 좌우 반전
#     print(*[i[::-1] for i in mirror], sep='\n')
# else:  # 상하 반전
#     print(*mirror[::-1], sep='\n')