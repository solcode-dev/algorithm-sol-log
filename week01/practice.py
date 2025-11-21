command_cnt, size = map(int, input().split())
queue = []

for _ in range(command_cnt):
    command = input().split()

    # 명령이 push라면
    if command[0] == "push":
        if len(queue) == size:
            print("Overflow")
        else:
            queue.append(int(command[1]))

    # 명령이 pop이라면
    if command[0] == "pop":
        if len(queue) == 0:
            print("Underflow")
        else:
            print(queue.pop())


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
            # 큐가 꽉 찼으면 Overflow 출력
            print("Overflow")
        else:
            # 큐에 여유가 있으면 값 추가
            queue.append(value)

    else:  # command[0] == "pop"
        # pop 명령 처리

        if len(queue) == 0:
            # 큐가 비었으면 Underflow 출력
            print("Underflow")
        else:
            # 큐의 맨 앞 요소를 제거하고 출력
            print(queue.pop(0))
