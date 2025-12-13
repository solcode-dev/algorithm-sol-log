# 1부터 n까지의 정수의 합 구하기

n = int(input('n값을 입력하시오: '))
print(f'1부터 {n}까지 정수의 합을 구하는 중..')

sum = 0
for i in range(1, n+1):
  sum += i

print(f'1부터 {n}까지 정수의 합: {sum}')  