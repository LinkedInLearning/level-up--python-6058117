from itertools import product

def solve_sudoku(puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:  # 找到一个未分配的单元格
            for num in range(1, 10):
                allowed = True  # 检查数字是否允许在行/列/盒中
                for i in range(0, 9):
                    if num in (puzzle[i][col], puzzle[row][i]):
                        allowed = False
                        break  # 不允许在行或列中
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False
                        break  # 不允许在盒子中
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    puzzle[row][col] = 0
            return False  # 不允许在此单元格中放置数字
    return puzzle

def print_sudoku(puzzle):
    # 将零替换为破折号
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if ((row % 3 == 0) and (row != 0)):
            print('-' * 33)  # 画水平线
        for col in range(0, 9):
            if ((col % 3 == 0) and (col != 0)):
                print(' | ', end='')  # 画垂直线
            print(f' {puzzle[row][col]} ', end='')
        print()
    print()

test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     print_sudoku(test_puzzle)
#     solution = solve_sudoku(test_puzzle)
#     print_sudoku(solution)
