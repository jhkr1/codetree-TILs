# # 내가 작성한 코드
# n = int(input())
# box_size = 3
# arr_2d = []
# sum = 0
# max_sum = []

# for i in range(n):
#     t = list(map(int, input().split()))
#     arr_2d.append(t)

# if(n <= box_size):
#     for i in range(n):
#         for j in range(n):
#             if(arr_2d[i][j] == 1):
#                 sum += 1
#     print(sum)


def max_coins(grid):
    n = len(grid)
    max_coins = 0

    for i in range(n-2):
        for j in range(n-2):
            current_sum = sum(grid[x][y] for x in range(i, i+3) for y in range(j, j+3))
            max_coins = max(max_coins, current_sum)
    return max_coins
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(max_coins(grid))