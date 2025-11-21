# 숫자배열

N = int(input())

num = 1  # 시작 숫자

for i in range(N):  # N개의 행
    row = []  # 한 줄을 저장할 리스트

    for j in range(N):  # N개의 열
        row.append(str(num))
        num += 1

    print(" ".join(row))
