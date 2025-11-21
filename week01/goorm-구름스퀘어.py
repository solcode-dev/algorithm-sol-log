# 구름스퀘어
# 활동 선택 문제의 그리디 알고리즘

n = int(input())  # 행사 개수
event = []  # 각 행사를 저장할 빈 리스트

for _ in range(n):
    start, end = map(int, input().split())  # 각 행사의 시작, 종료시간
    event.append((start, end))  # 행사 시작, 종료시간을 튜플로 저장

event.sort(key=lambda x: x[1])  # 튜플의 두번째요소 (종료시간)을 기준으로 정렬

count = 0
ended_time = 0
for start, end in event:
    if (
        start > ended_time
    ):  # 새로 시작할 행사 시간이 앞서 종료된 행사 종료시간보다 늦으면
        count += 1
        ended_time = end

print(count)
