import random
from max import max_of

num = int(input('난수의 개수 : '))
lo = int(input('난수의 최솟값 : '))
hi = int(input('난수의 최댓값 : '))
x = [None] * num

for i in range(num):
  x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'최대값: {max_of(x)}')