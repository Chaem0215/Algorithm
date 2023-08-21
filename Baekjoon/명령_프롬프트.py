# 브론즈 1
# 명령 프롬프트
# https://www.acmicpc.net/problem/1032
# 23.08.21
 
import sys
N = int(sys.stdin.readline())
result = list(sys.stdin.readline().rstrip()) # 처음 비교할 대상 정해줌.

for _ in range(N - 1):
    str = sys.stdin.readline().rstrip()

    for i, v in enumerate(str):
        if result[i] != v:
            result[i] = "?" # 문자열은 immutable type 이라 수정 불가 // list 사용하여 원하는 위치에서 문자 변경하도록 // 문자열의 replace는 특정 패턴의 문자라...

print(''.join(result))