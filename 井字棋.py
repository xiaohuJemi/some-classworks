import copy

# 打印棋盘
def print_board(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            print(f' {cell} ', end='')
            if j != 2:
                print('|', end='')
        print()
        if i != 2:
            print('-' * 11)
    print()

# 检查是否有玩家获胜
def check_win(board, player):
    # 检查行
    for row in board:
        if all(cell == player for cell in row):
            return True
    # 检查列
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # 检查对角线
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# 检查是否平局
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row) and not (check_win(board, 'X') or check_win(board, 'O'))

# 极大极小算法
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -1
    elif check_win(board, 'O'):
        return 1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = 'O'
                    score = minimax(new_board, depth + 1, False)
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = 'X'
                    score = minimax(new_board, depth + 1, True)
                    best_score = min(best_score, score)
        return best_score

# 获取电脑的最佳移动
def get_best_move(board):
    d = sum(cell != ' ' for row in board for cell in row)
    best_score = float('-inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = copy.deepcopy(board)
                new_board[i][j] = 'O'
                score = minimax(new_board, d, False)
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# 主游戏循环
def play_game():
    board = [[' '] * 3 for _ in range(3)]
    player_turn = input("选择先手(X)或后手(O): ").upper()
    while True:
        print_board(board)
        if player_turn == 'X':
            moveit = int(input("输入你的移动（1 - 9）: "))
            row, col = divmod(moveit - 1, 3)
            while board[row][col] != ' ':
                print("该位置已被占用，请重新选择！")
                moveit = int(input("输入你的移动（1 - 9）: "))
                row, col = divmod(moveit - 1, 3)
            board[row][col] = 'X'
            if check_win(board, 'X'):
                print_board(board)
                print("你赢了！")
                break
            elif check_draw(board):
                print_board(board)
                print("平局！")
                break
            player_turn = 'O'
        else:
            row, col = get_best_move(board)
            board[row][col] = 'O'
            print('AI已确定落子位置:')
            if check_win(board, 'O'):
                print_board(board)
                print("AI赢了！")
                break
            elif check_draw(board):
                print_board(board)
                print("平局！")
                break
            player_turn = 'X'

play_game()




