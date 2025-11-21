# 문제 이해하기밀도란?

# 밀도 = 무게 ÷ 부피
# 목표: 가장 밀도가 높은 물질의 번호 찾기
# 우선순위 (같을 때):
# 밀도가 높은 물질
# 밀도가 같으면 → 더 무거운 물질
# 밀도와 무게가 같으면 → 번호가 작은 물질


# 입력: 물질의 개수
n = int(input())

# 가장 좋은 물질 정보 저장 (초기값)
best_number = 1  # 가장 좋은 물질의 번호
best_density = 0  # 가장 높은 밀도
best_weight = 0  # 가장 높은 무게

# 각 물질 확인
for i in range(1, n + 1):  # 물질 번호는 1번부터 시작
    # 무게와 부피 입력받기
    weight, volume = map(int, input().split())

    # 현재 물질의 밀도 계산
    density = weight / volume

    # 현재 물질이 더 좋은지 확인
    # 조건1: 밀도가 더 높으면 선택
    if density > best_density:
        best_number = i
        best_density = density
        best_weight = weight

    # 조건2: 밀도가 같고 무게가 더 무거우면 선택
    elif density == best_density and weight > best_weight:
        best_number = i
        best_weight = weight

    # 조건3: 밀도와 무게가 같으면 번호가 작은 것이 이미 선택됨
    # (아무것도 안 해도 됨)

# 결과 출력
print(best_number)


## 실행 과정 (자세히)

# 입력:
# 4
# 1 2
# 2 1
# 3 1
# 5 1

# 초기: best_number=1, best_density=0, best_weight=0

# i=1: weight=1, volume=2, density=0.5
#      0.5 > 0 → 갱신
#      best_number=1, best_density=0.5, best_weight=1

# i=2: weight=2, volume=1, density=2.0
#      2.0 > 0.5 → 갱신
#      best_number=2, best_density=2.0, best_weight=2

# i=3: weight=3, volume=1, density=3.0
#      3.0 > 2.0 → 갱신
#      best_number=3, best_density=3.0, best_weight=3

# i=4: weight=5, volume=1, density=5.0
#      5.0 > 3.0 → 갱신
#      best_number=4, best_density=5.0, best_weight=5

# 출력: 4
