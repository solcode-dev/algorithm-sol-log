a, b = input().split()
print(
    max(eval(a), eval(b))
)  # eval: 문자열로 된 수식을 실제로 계산해주는 함수 (연산자 우선순위 자동 적용)
