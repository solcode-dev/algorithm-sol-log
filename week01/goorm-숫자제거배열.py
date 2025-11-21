# 숫자 제거 배열
# 문제
# N개의 정수 중에 문자열 K가 포함되어 있으면

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

filtered = [x for x in arr if str(k) not in str(x)]
print(len(filtered))


######

n, k = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if str(k) in str(num):
        count += 1

print(n - count)
