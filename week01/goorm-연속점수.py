n = int(input())  # 문제 개수 (1~n)
scores = list(map(int, input().split()))

max_score = max(scores)
current_score = 0

# 1. 점수를 순회하면서 현재 점수 == (앞 점수 + 1) 인지 확인한다
# 2.1. 맞다면, current_score에 현재 점수를 더한다.
# 2.2. 아니라면, current_score와 max_score를 비교해서 더 큰 값을 max_scor에 넣는다. 그리고 current_score를 0으로 초기화한다.
# 3. max_score를 출력한다.

for i in range(n):  # 0 ~ 5
    if i == 0:
        current_score = scores[i]  # current_score = 2
    elif scores[i] == (scores[i - 1] + 1):
        current_score += scores[i]
    else:
        max_score = max(max_score, current_score)
        current_score = scores[
            i
        ]  # 연속이 끊겼으므로 현재 점수부터 새로운 연속을 시작한다

print(max(max_score, current_score))
