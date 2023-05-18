# Level 1
# 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 23.05.18

numbers = [5, 0, 2, 7]
result = set()

def solution(numbers):
    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            result.add(numbers[i] + j)

    return sorted(list(result))

print(solution(numbers))

# set() 은 중복이 제거되기 때문에 set() 을 이용하였다.