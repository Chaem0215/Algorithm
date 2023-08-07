# 실버 5
# 생일
# https://www.acmicpc.net/problem/5635
# 23.08.07

import sys

n = int(sys.stdin.readline())
lists = list(sys.stdin.readline().split() for _ in range(n))

# ['Mickey', '1', '10', '1991'] 이름, 일, 월, 연도 순
max_stdn = [lists[0][0], int(lists[0][3]+lists[0][2]+lists[0][1])] # 첫번째 사람으로 값 비교
min_stdn = [lists[0][0], int(lists[0][3]+lists[0][2]+lists[0][1])]

print(max_stdn, min_stdn)

for i in range(1, n):
    birth = int(lists[i][3]+lists[i][2]+lists[i][1])
    print(">>>>", max_stdn[1], birth)
    if max_stdn[1] < birth:
        max_stdn = [lists[i][0], birth]
    elif min_stdn[1] > birth:
        min_stdn = [lists[i][0], birth]


print(min_stdn[0], max_stdn[0], sep="\n")