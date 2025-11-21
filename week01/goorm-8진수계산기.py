# 8진수 계산기

n = int(input())  # 주어지는 숫자의 개수
arr = list(map(int, input().split()))  # 주어진 숫자들

sum = 0
for num in arr:
    sum += num

print(oct(sum)[2::])

###

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
print(oct(total)[2::])
