# 거스름돈
# 큰 동전부터 최대한 많이 사용하는 그리디 알고리즘

n = int(input())  # 거슬러줘야 하는 총액
coins = [40, 20, 10, 5, 1]
cnt = 0

for coin in coins:
    cnt += n // coin  # 이 동전의 사용개수
    n = n % coin  # 나머지

print(cnt)
