# 구름 아이돌
# N명의 지원자 (1번~ n번)

n = int(input())
score = list(map(int, input().split()))  # [10, 3, 7, 4, 1]
high_score_3 = sorted(score)[n - 3 :]

res = []
for el in high_score_3:
    res.append(score.index(el) + 1)

print(*res[::-1])

# 입력
n = int(input())  # 지원자 수
score = list(map(int, input().split()))  # 지원자별 점수 (순서대로)

# 인덱스 n-3부터 끝까지 가져온다. 즉, 뒤에서 3개를 가져오는 것
high_score_3 = sorted(score)[n - 3 :]

# 인덱스(지원자)를 가져온다
res = []
for el in high_score_3:  # high_score_3에서 값을 하나씩 꺼낸다
    res.append(
        score.index(el) + 1
    )  # score에서 해당 값의 인덱스를 가져와서 1을 더한다 (지원자는 1부터니까)

print(*res[::-1])  # 점수 높은 순으로 출력하라는 문제에 맞춰 역순 정렬
