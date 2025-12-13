# 세 정수를 입력받아 중앙값 구하기1

def med(a,b,c):
  """a,b,c의 중앙값을 구하여 반환한다"""
  if a >= b:
    if b >= c:
      return b
    elif a <= c:
      return a
    else:
      return c
  elif a > c:
    return a
  elif b > c:
    return c
  else:
    return b


print('세 정수의 중앙값을 구한다')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print(f'세 정수의 중앙값은 {med(a,b,c)} ')