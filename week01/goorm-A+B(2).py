# A+B(2)
# 문제
# 주어지는 두 개의 실수를 합한 값을 출력

from decimal import Decimal

a, b = map(Decimal, input().split())
print(a + b)
