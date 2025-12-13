def card_conv(x: int, r: int) -> str:
  d = '' # 변환 후 문자열
  dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  while x > 0:
    d += dchar[x % r]
    x //= r

  return d[::-1]