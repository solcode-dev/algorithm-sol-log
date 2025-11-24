n = int(input())  # 주어진 정수 개수
nums = set(map(int, input().split()))  # 무작위 정수들
nums_list = sorted(nums)

print(*nums_list)
