# *을 n개 출력하되, w개마다 줄바꿈하기

while True:
  n = int(input('몇 개 출력할까? :'))
  w = int(input('몇 개마다 줄바꿈할까? :'))
  if(n > 0 and w > 0):
    break

for _ in range(n //w):
  print('*' * w)

rest = n % w
if rest:
  print('*' * rest)

# for i in list(range(1,8)) + list(range(9,13)):
#   print(i, end=' ')
# print()   