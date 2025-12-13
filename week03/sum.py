# a부터 b까지 정수의 합 구하기

a = int(input('정수 a: '))
b = int(input('정수 b: '))
print(f'{a}부터 {b}까지 정수의 합을 구합니다...')


if a > b:
  a, b = b, a # 오름차순으로 정렬

sum = 0
for i in range(a, b+1):
  sum += i

print(f'{a}부터 {b}까지 정수의 합: {sum}')