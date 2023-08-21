# 브론즈 1
# 핸드폰 번호 궁합
# https://www.acmicpc.net/problem/17202
# 23.08.12

A = list(input())
B = list(input())
num = []

def compatibility(lists):
    tmp = []
    if len(lists) < 3:
        return lists
    
    for i in range(0, len(lists) - 1):
        total = (lists[i] + lists[i + 1]) % 10 # 더해서 두자리수 나오는거 방지
        tmp.append(total)

    return compatibility(tmp)

for i in range(len(A)):
    num.append(int(A[i]))
    num.append(int(B[i]))

result = compatibility(num)
print(f"{result[0]}{result[1]}") # print(*result, sep='')