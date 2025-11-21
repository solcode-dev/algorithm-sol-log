# 카드 모으기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 모아야 할 카드 목록 (1부터 N까지)
needed_cards = set(range(1, n + 1))

# M장의 카드를 순서대로 받기
for i in range(m):
    card = int(input())

    # 필요한 카드면 제거
    if card in needed_cards:
        needed_cards.remove(card)

    # 다 모았으면 (i+1)장 받았다는 의미
    if len(needed_cards) == 0:
        print(i + 1)  # 받은 카드 장수 출력
        break
else:
    # M장 다 받아도 못 모았으면
    print(-1)
