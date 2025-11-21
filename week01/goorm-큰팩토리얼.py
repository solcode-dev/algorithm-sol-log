# 큰 팩토리얼
# 문제
# N이 주어지면 N!값을 출력
# N! = 1 x 2 x 3 x .. x N
# 출력은 N! 값을 1_000_000_007 로 나눈 나머지

n = int(input())
res = 1

for i in range(1, n + 1):
    res *= i

print(res % 1_000_000_007)
