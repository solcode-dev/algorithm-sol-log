# 입력: 명령 개수 N과 큐 크기 K
n, k = map(int, input().split())

# 큐를 빈 리스트로 초기화
queue = []

# N개의 명령 처리
for _ in range(n):
    command = input().split()  # 명령 입력받기

    if command[0] == "push":
        # push 명령 처리
        value = int(command[1])  # 추가할 값

        if len(queue) >= k:
            # 큐의 현재 크기가 최대 크기 이상이면 Overflow 출력
            print("Overflow")
        else:
            # 큐에 여유가 있으면 값 추가
            queue.append(value)

    else:  # command[0] == "pop"
        # pop 명령 처리

        if len(queue) == 0:
            # 큐에 아무것도 없으면 Underflow 출력
            print("Underflow")
        else:
            # 큐의 맨 앞 요소를 제거하고 출력
            print(queue.pop(0))  # 인덱스 0(맨 앞) 요소를 제거하고 반환
