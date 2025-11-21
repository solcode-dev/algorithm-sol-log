n = int(input())

# 2. 격자판 입력받기
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)  # [[3,0,3], [2,4,2], [2,2,1]]

# 3. 0을 찾고, 동시에 가로줄 합과 세로줄 합 구하기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            # 0을 찾았다!

            # 가로줄 합 (i번째 줄의 모든 숫자)
            row_sum = sum(grid[i])

            # 세로줄 합 (j번째 칸의 모든 숫자)
            col_sum = 0
            for k in range(n):
                col_sum += grid[k][j]

            # 결과 출력하고 끝
            print(row_sum + col_sum)
