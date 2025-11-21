# 수열

n = int(input())


def fib(n):
    # 특별한 경우들
    if n == 1:
        return 0
    elif n == 2:
        return 1

    # 처음 두 개의 피보나치 수
    first = 0
    second = 1

    # 3번째부터 n번째까지 하나씩 계산. 두 수를 계속 "한 칸씩 앞으로" 이동시킨다.
    for i in range(3, n + 1):
        # ① 앞의 두 수를 더하기.
        new_num = first + second
        new_num = new_num % 1000000007

        # ② 한 칸씩 앞으로 이동
        first = second  # second를 first 자리로
        second = new_num  # new_num을 second 자리로

    return new_num


print(fib(n))
