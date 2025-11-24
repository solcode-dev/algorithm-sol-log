from decimal import Decimal

n, k = map(int, input().split())  # 사람수, 몇번째
people = []

for _ in range(n):
    name, height = map(str, input().split())
    height = Decimal(height)
    people.append((name, height))

people.sort(key=lambda x: (x[0], x[1]))
print(people[k - 1][0], people[k - 1][1])
